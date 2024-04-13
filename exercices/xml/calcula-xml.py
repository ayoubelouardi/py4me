import xml.etree.ElementTree as ET
import urllib.request
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('URL - ')
data = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(data)

# Find all <count> tags and print their text content
count = 0
for tag in tree.findall('.//count'):
    count += int(tag.text)
    print(tag.text, count)

print(count)
