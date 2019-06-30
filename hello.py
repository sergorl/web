import re


def app(environ, start_response):

	content = []
    for matches in re.findall(r'(\w+\=\w+)', environ['QUERY_STRING']):
    	for m in matches:
    		content += m
    	m += '\n'	

    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(content)))
    ]
    start_response(status, response_headers)

    return iter(content)
