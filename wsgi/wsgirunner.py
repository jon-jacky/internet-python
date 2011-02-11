"""
Import the module named in the command line argument,
use wsgiref to run its application function.

So if we have testwsgi.py which contains a function, application:

  python wsgirunner.py app

Based on http://hg.moinmo.in/moin/1.8/raw-file/tip/wiki/server/test.wsgi
copyright 2008 by MoinMoin:ThomasWaldmann, wity Python License

stub application based on wsgi_test.py from 
http://webpython.codepoint.net/wsgi_application_interface
"""

import sys
from wsgiref import simple_server

def stub(environ, start_response):
    """ default application to run if none named on command line"""
    response_body = 'The request method was %s' % environ['REQUEST_METHOD']
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]
    
def main():
    if len(sys.argv) > 1:
        appname = sys.argv[1]
        app = __import__(appname)
        application = app.application
    else:
        appname = "default stub app"
        application = stub

    print "Running %s - point your browser at http://localhost:8000/ ..." \
        % appname
    httpd = simple_server.WSGIServer(('', 8000), 
                                     simple_server.WSGIRequestHandler)
    httpd.set_app(application)
    httpd.serve_forever()

if __name__ == '__main__':
    main()
