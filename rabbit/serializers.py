from rest_framework import serializers


class RabbitSerializer(serializers.Serializer):
    METHOD_CHOICES = (
        ('GET', 'GET'),
        ('POST', 'POST'),
    )

    FORMAT_CHOICES = (
        ('json', 'JSON'),
        ('msgpack', 'MsgPack'),
    )
    methods = serializers.ChoiceField(choices=METHOD_CHOICES)
    url = serializers.URLField()
    formats = serializers.ChoiceField(choices=FORMAT_CHOICES)
