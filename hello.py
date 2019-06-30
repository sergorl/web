import re


def app(environ, start_response):

    content = []

    for matches in re.findall(r'(\w+\=\w+)', environ['QUERY_STRING']):
        for m in matches:
            content.append(m)

        m.append('\n')

    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(content)))
    ]
    start_response('200 OK', response_headers)

    return iter(content)
