import re


def app(environ, start_response):
    def parse_query():
        values = re.findall(r'(\w+\=\w+)', environ['QUERY_STRING'])

        data = ''
        for v in values:
            data += v + '\n'

        return data

    content = parse_query()

    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(content)))
    ]
    start_response(status, response_headers)

    return iter([content])
