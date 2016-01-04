import urllib
from BeautifulSoup import *
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
tags = soup('span')
summary = 0
for tag in tags:
	print 'Contents:',tag.contents[0]
	summary = summary +int(tag.contents[0])
print summary
