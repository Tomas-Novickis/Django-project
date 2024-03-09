import json

import msgpack
import pika
from rabbit.serializers import RabbitSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class PublisherView(APIView):
    serializer_class = RabbitSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            methods = serializer.validated_data['methods']
            url = serializer.validated_data['url']
            formats = serializer.validated_data['formats']

            # connect to RabbitMQ
            connection_parameters = pika.ConnectionParameters('localhost')
            connection = pika.BlockingConnection(connection_parameters)
            channel = connection.channel()
            channel.exchange_declare(exchange='topic_logs',
                                     exchange_type='topic')

            if methods == 'POST':
                routing_key = 'request.send.post'
            else:
                routing_key = 'request.send.get'

            if formats == 'json':
                message = json.dumps(url)
                content_type = 'application/json'
            else:
                message = msgpack.packb(url)
                content_type = 'application/msgpack'

            properties = pika.BasicProperties(content_type=content_type)
            channel.basic_publish(exchange='topic_logs',
                                  routing_key=routing_key,
                                  body=message,
                                  properties=properties)
            connection.close()
            return Response("Message sent to RabbitMQ", status=201)
        return Response(serializer.errors, status=400)
