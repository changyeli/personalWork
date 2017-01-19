# import module
from bs4 import BeautifulSoup as bs
import re
import urllib2
import csv

# function
## get title
def getTitle():
	for title in soup.findAll('h3', attrs = {'class': 'yt-lockup-title'}):
		temp = title.find('a').text.strip()
		return (temp.encode('utf-8'))

## get uploader information
def getUser():
	for author in soup.findAll('div', attrs = {'class': 'yt-lockup-byline'}):
		return (str(author.find('a')['href'][6:]))

## get number of view
def getView():
	for views in soup.findAll('ul', attrs = {'class': 'yt-lockup-meta-info'}):
		s1 = str(views.findAll('li')).replace(',', '')
		s1 = re.findall('\d+', s1)[1]
		return s1

## get description of video
def getDesc():
	for dess in soup.findAll('div', attrs = {'class': 'yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2'}):
		return (dess.text.encode('utf-8')[:-11])

## get next page
def getNext(count):
	pages = []
	pref = 'https://www.youtube.com'
	direction = 'Go to page ' + str(count)
	for link in soup.findAll('a', attrs = {'aria-label': direction}):
		pages.append(pref + link['href'])
	return pages[0].encode('utf-8')

# na speaker

url = 'https://www.youtube.com/results?q=na+speaker&sp=EgIQAQ%253D%253D'
count = 1
datas = []

while (count < 30):
	count +=1
	my_page = urllib2.urlopen(url)
	soup = bs(my_page, 'html.parser')
	title = getTitle()
	user = getUser()
	desc = getDesc()
	view =getView()
	url = getNext(count)
	tup1 = (title, user, desc, view)
	datas.append(tup1)

# write to .csv file
with open('info_na.csv', 'wb') as f:
	fileWriter = csv.writer(f)
	for row in datas:
		fileWriter.writerow(row)

# aa speaker
url = 'https://www.youtube.com/results?q=aa+speaker&sp=EgIQAQ%253D%253D'
count = 1
datas = []

while (count < 29):
	count +=1
	my_page = urllib2.urlopen(url)
	soup = bs(my_page, 'html.parser')
	title = getTitle()
	user = getUser()
	desc = getDesc()
	view =getView()
	url = getNext(count)
	tup1 = (title, user, desc, view)
	datas.append(tup1)

# write to .csv file
with open('info_aa.csv', 'wb') as f:
	fileWriter = csv.writer(f)
	for row in datas:
		fileWriter.writerow(row)