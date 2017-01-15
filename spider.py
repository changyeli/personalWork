# import module
from bs4 import BeautifulSoup as bs
import re
import urllib2
import csv

url = 'https://www.youtube.com/results?sp=EgIQAQ%253D%253D&q=na+speakers'
head = []
uploader = []
des = []
view = []
my_page = urllib2.urlopen(url)
soup = bs(my_page, 'lxml')

# test No.1
def getTitle():
	for title in soup.findAll('h3', attrs = {'class': 'yt-lockup-title'}):
		temp = title.find('a').text.strip()
		head.append(temp.encode('utf-8'))


def getUser():
	for author in soup.findAll('div', attrs = {'class': 'yt-lockup-byline'}):
		uploader.append(str(author.find('a')['href'][6:]))


def getView():
	for views in soup.findAll('ul', attrs = {'class': 'yt-lockup-meta-info'}):
		s1 = str(views.findAll('li')[1]).replace(',', '')
		s1 = re.findall('\d+', s1)[0]
		view.append(s1)

def getDesc():
	for dess in soup.findAll('div', attrs = {'class': 'yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2'}):
		des.append(dess.text.encode('utf-8'))