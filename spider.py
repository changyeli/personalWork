# import module
from bs4 import BeautifulSoup as bs
import re
import urllib2
import csv

# initialize data storage
head = []
uploader = []
des = []
view = []

# function
def getTitle():
	for title in soup.findAll('h3', attrs = {'class': 'yt-lockup-title'}):
		temp = title.find('a').text.strip()
		head.append(temp.encode('utf-8'))


def getUser():
	for author in soup.findAll('div', attrs = {'class': 'yt-lockup-byline'}):
		uploader.append(str(author.find('a')['href'][6:]))


def getView():
	for views in soup.findAll('ul', attrs = {'class': 'yt-lockup-meta-info'}):
		s1 = str(views.findAll('li')).replace(',', '')
		s1 = re.findall('\d+', s1)[1]
		print s1
		view.append(s1)

def getDesc():
	for dess in soup.findAll('div', attrs = {'class': 'yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2'}):
		des.append(dess.text.encode('utf-8'))


# spider process

base = 'https://www.youtube.com/results?search_query='
query = ['na+speaker', 'aa+speaker']
count = 1 # starting page
page = '&page='


url = base + 'na+speaker' + page + str(count)
my_page = urllib2.urlopen(url)
soup = bs(my_page, 'html.parser')
getDesc()
print des