import time
import datetime

print """<html>
<head><title>Time</title></head>
<body>

<p>Here is the time: %s</p>

<p>and again: %s</p>

</body>
</html>
""" % (time.time(), datetime.datetime.now())
