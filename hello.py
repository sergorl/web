import re


def app(environ, start_response):

    content = [v + '\n' for v in re.findall(r'(\w+\=\w+)', environ['QUERY_STRING'])]

    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(content)))
    ]
    start_response(status, response_headers)

    return [bytes(content, 'utf-8')]
