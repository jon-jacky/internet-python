"""
write a file with contents of each web page identified in file,
each line in file has one url
"""

import sys
import urllib2

urlfilename = 'urls.txt'

if len(sys.argv) > 1:
    urlfilename = sys.argv[1]

urlfile = open(urlfilename, 'r')

for (i, url) in enumerate(urlfile):
    wd = urllib2.urlopen(url)
    fd = open('file'+str(i)+'.html', 'w')
    page = wd.read()
    fd.write(page)
    wd.close()
    fd.close()
