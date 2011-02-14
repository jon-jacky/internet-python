"""
Books database web application - week05 assignment

Raw WSGI, no framework
"""
import sys

# uncomment this line to run via apache mod_wsgi on bluebox vm
# needed for import below
# sys.path.append('/usr/local/wsgi-scripts')

import bookdb

frame = """
<html>
<head>
<title>
%s
</title>
</head>
<body>
%s
</body>
"""

index_template = """
<h2>Books</h2>

<ol>
%s
</ol>
"""

detail_template = """
<h2>%(title)s</h2>
<dl>
<dt>Author:</dt><dd>%(author)s</dd>
<dt>Publisher:</dt><dd>%(publisher)s</dd>
<dt>ISBN:</dt><dd>%(isbn)s</dd>
</dl>
"""

template_404 = """
<h2>404 Not Found</h2>

<p>%s does not exist on this server</p>
"""

def make_index(home_url, database):
    entries = [ '<li><a href="http://%s/%s">%s</li>' % \
                    (home_url, id, database[id]['title']) for id in database ] 
    return '\n'.join(entries)

def application(environ, start_response):
    host = environ['HTTP_HOST']
    pathstr = environ['PATH_INFO']
    path = pathstr.split('/')
    print 'pathstr "%s"' % pathstr
    path = [ name for name in path if name ] # eliminate ''
    print 'path entries %s' % path
    if path:
        home_dir = path[0]
        home_url = '%s/%s' % (host, home_dir)
        print 'home_dir %s' % home_dir
        print 'home_url %s' % home_url

    # index page 
    if path and len(path) == 1 and home_dir == 'books':
        index = index_template % make_index(home_url, bookdb.database)
        page = frame % ('Books', index)
        status = '200 OK'
        response_headers = [('Content-Type', 'text/html'),
                        ('Content-Length', str(len(page)))]
        start_response(status, response_headers)
        return [page]

    # detail page 
    if path and len(path) > 1 and home_dir == 'books' and path[1] in bookdb.database:
        detail = detail_template % bookdb.database[path[1]]
        page = frame % (bookdb.database[path[1]]['title'], detail)
        status = '200 OK'
        response_headers = [('Content-Type', 'text/html'),
                        ('Content-Length', str(len(page)))]
        start_response(status, response_headers)
        return [page]

    else: # wrong path, no path should probably be treated differently
        page = frame % ('404 Not Found', template_404 % pathstr)
        status = '404 Not Found'
        response_headers = [('Content-Type', 'text/html'),
                        ('Content-Length', str(len(page)))]
        start_response(status, response_headers)
        return [page]
