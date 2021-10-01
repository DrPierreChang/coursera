import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL sertificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Sandra.html'

for i in range(7):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve  all of the anchor tags
    tags = soup('a')
    url = re.findall('http.+html', str(tags[17]))[0]
    print(i+1, url)
print(re.findall('by_(.+?)\.html', url)[0])