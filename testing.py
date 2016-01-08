import urllib
import xml.etree.ElementTree as ET

address = raw_input('Enter location: ')
count = 0

#url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
uh = urllib.urlopen(address)
data = uh.read()
tree = ET.fromstring(data)
results = tree.findall('comments/comment')
for line in results:
    count = count + int(line.find("count").text)
print count