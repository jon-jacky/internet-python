#!/usr/bin/python

# use the following instead on Windows
#!C:\Python26\python.exe

import cgi
import cgitb
import time
import urlparse
import os

cgitb.enable()

json_page = """{
"result": %s,
"uwnetid": "jon",
"time": %s
}
"""


print 'Content-type: text/json' # for testing in browser, use text/plain
print 

query = os.getenv('QUERY_STRING')
vars = urlparse.parse_qs(query)
# print 'vars %s' % vars # DEBUG

print json_page % (int(vars['a'][0]) + int(vars['b'][0]), time.time())


