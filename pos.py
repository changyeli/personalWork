import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
count = raw_input('Enter count: ')
position = raw_input('Enter position: ')

count = int(count)
position = int(position)

while (count>0):
	soup = BeautifulSoup(html)
	tags = soup('a')
	urls = []
	contents = []
	for tag in tags:
		urls = urls + [str(tag.get('href', None))]
		contents = contents + [str(tag.contents[0])]
	print contents[position-1]
	html = urllib.urlopen(urls[position-1]).read()
	count -= 1
