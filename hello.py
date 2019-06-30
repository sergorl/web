import re


def app(environ, start_response):

    body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]

    response_headers = [
        ('Content-type', 'text/plain')
    ]
    start_response('200 OK', response_headers)

    return body
