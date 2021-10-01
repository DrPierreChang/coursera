import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL sertificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve  all of the anchor tags
tags = soup('span')

for_sum = list()
for tag in tags:
    for_sum.append(int(tag.contents[0]))
    #print(re.findall('[0-9]+', str(tag)))
print(sum(for_sum))