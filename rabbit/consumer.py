import json
import os
import sys

import msgpack
import pika


def main():

    connection_parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()

    channel.exchange_declare(exchange='topic_logs',
                             exchange_type='topic')

    channel.queue_declare(queue='rabbit_queue')
    binding_keys = ['request.send.post', 'request.send.get']

    for binding_key in binding_keys:
        channel.queue_bind(
         exchange='topic_logs', queue='rabbit_queue', routing_key=binding_key)

    def callback(ch, method, properties, body):
        routing_key = method.routing_key
        content_type = properties.content_type
        message = body

        # ifs to decode the body based on the serization user provided
        if content_type == 'application/json':
            message = json.loads(body.decode('utf-8'))

        elif content_type == 'application/msgpack':

            message = msgpack.unpackb(body)

        # ifs to check the routing key
        # based on the method POST or GET user provided
        if routing_key == 'request.send.get':

            print(f'received: {message} from {routing_key}')

        elif routing_key == 'request.send.post':

            print(f'received: {message} from {routing_key}')

        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue='rabbit_queue',
                          on_message_callback=callback, auto_ack=False)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
