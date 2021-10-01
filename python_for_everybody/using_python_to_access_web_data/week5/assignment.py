import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL sertificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1355249.xml'
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
stuff = ET.fromstring(data)
lst = stuff.findall('comments/comment')

for_sum = list()
for item in lst:
    for_sum.append(int(item.find('count').text))

print(sum(for_sum))


