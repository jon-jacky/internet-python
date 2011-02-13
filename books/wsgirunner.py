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
from optparse import OptionParser

usage = """wsgirunner [options] app_module
"""

parser = OptionParser(usage=usage)

def parse_args():
  parser.add_option('-p', '--port', type='int', default=8000,
                  help='Action to include in generated FSM, as many as needed, if no -a include all actions')
  return parser.parse_args()


def print_help():
  parser.print_help()  # must have at least one arg, not optional

def stub(environ, start_response):
    """ default application to run if none named on command line"""
    response_body = 'The request method was %s' % environ['REQUEST_METHOD']
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]
    
def main():
    (options, args) = parse_args()

    if len(args) > 0:
        app_module = args[0]
        app = __import__(app_module)
        application = app.application
    else:
        app_module = "default stub app"
        application = stub
    print "Running %s - point your browser at http://localhost:%s/" \
        % (app_module, options.port)
    httpd = simple_server.WSGIServer(('', options.port), 
                                     simple_server.WSGIRequestHandler)
    httpd.set_app(application)
    httpd.serve_forever()

if __name__ == '__main__':
    main()
