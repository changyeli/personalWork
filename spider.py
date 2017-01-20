# import module
from bs4 import BeautifulSoup as bs
import re
import urllib2
import csv

# function
## get title
def getTitle():
	for title in soup.findAll('h3', attrs = {'class': 'yt-lockup-title'}):
		temp = title.find('a').text.strip().encode('utf-8')
		head.append(temp)
	return head[2:]

## get uploader information
def getUser():
	for author in soup.findAll('div', attrs = {'class': 'yt-lockup-byline'}):
		u1 = str(author.find('a')['href'][6:])
		uploader.append(u1)
	return uploader[2:]

## get number of view
def getView():
	for views in soup.findAll('ul', attrs = {'class': 'yt-lockup-meta-info'}):
		s1 = str(views.findAll('li')).replace(',', '')
		s1 = re.findall('\d+', s1)
		if len(s1) == 2:
			view.append(s1[1])
	return view

## get description of video
def getDesc():
	for dess in soup.findAll('div', attrs = {'class': 'yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2'}):
		desc.append(dess.text.encode('utf-8')[:-11])
	return desc[2:]

## get next page
def getNext(count):
	pages = []
	pref = 'https://www.youtube.com'
	direction = 'Go to page ' + str(count)
	for link in soup.findAll('a', attrs = {'aria-label': direction}):
		pages.append(pref + link['href'])
	return pages[0].encode('utf-8')

# na speaker
url = 'https://www.youtube.com/results?sp=EgIQAQ%253D%253D&q=na+speaker'
count = 1
datas = []

while (count < 29):

	my_page = urllib2.urlopen(url)
	soup = bs(my_page, 'lxml') # with order
	# inilization
	head = []
	uploader = []
	view = []
	desc = []

	head = getTitle()
	unloader = getUser()
	view = getView()
	desc = getDesc()
	datas = zip(head, uploader, view, desc) # change to tuple

	count += 1
	url = getNext(count)

	with open('info_na.csv', 'a') as f: # a to append
		writer = csv.writer(f)
		for row in datas:
			writer.writerow(row)

# aa speaker
url = 'https://www.youtube.com/results?sp=EgIQAQ%253D%253D&q=aa+speaker'
count = 1
datas = []

while (count < 28):

	my_page = urllib2.urlopen(url)
	soup = bs(my_page, 'lxml') # with order
	# inilization
	head = []
	uploader = []
	view = []
	desc = []

	head = getTitle()
	unloader = getUser()
	view = getView()
	desc = getDesc()
	datas = zip(head, uploader, view, desc) # change to tuple

	count += 1
	url = getNext(count)

	with open('info_aa.csv', 'a') as f: # a to append
		writer = csv.writer(f)
		for row in datas:
			writer.writerow(row)
