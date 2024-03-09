import logging

logger = logging.getLogger('django')


class RequestResponseLogging:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log the request
        logger.info('Request received')

        response = self.get_response(request)

        # Log the response
        logger.info('Response sent')

        return response
