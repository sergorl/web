import re

def app(environ, start_response):

	def parseQuery(query):
	    values = re.findall(r'(\w+\=\w+)', query)

	    data = ''
	    for v in values:
	        data += v + '\n'

   		return data

    """Simplest possible application object"""
    data = parseQuery(environ['QUERY_STRING'])

    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    
    return iter([data])