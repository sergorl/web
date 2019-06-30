from cgi import parse_qs


def app(environ, start_response):

    qs = parse_qs(environ['QUERY_STRING'])

    response_headers = [
        ('Content-type', 'text/plain'),
    ]
    start_response('200 OK', response_headers)

    return ['%s=%s<br>' % (k, qs[k][0]) fro k in qs]
    
