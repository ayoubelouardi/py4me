import json
import urllib.request
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('URL - ')
data = urllib.request.urlopen(url, context=ctx).read()
json_data = json.loads(data)

count = 0
for comment in json_data["comments"]:
    count += comment["count"]
    print(comment["count"], count)

print(count)
