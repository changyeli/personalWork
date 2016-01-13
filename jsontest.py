import json
import urllib

url = raw_input("Enter URL:")
data = urllib.urlopen(url).read()
info = json.loads(data)
count = 0

for item in info['comments']:
	count = count + int(item['count'])
print count