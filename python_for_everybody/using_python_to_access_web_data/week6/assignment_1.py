import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL sertificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1355250.json'
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
data = json.loads(data)

keep_sum = 0
for item in (data['comments']):
    keep_sum += int(item['count'])

print(keep_sum)
