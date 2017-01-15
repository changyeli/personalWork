# import module
from bs4 import BeautifulSoup as bs
import re
import urllib2
import csv

# test No.1

url = 'https://www.youtube.com/results?q=na+speakers&sp=EgIQAQ%253D%253D'
head = []
uploader = []
des = []
view = []
my_page = urllib2.urlopen(url)
soup = bs(my_page, 'lxml')

## get title information

for title in soup.findAll('h3', attrs = {'class': 'yt-lockup-title'}):
	temp = title.find('a').text.strip()
	head.append(temp.encode('utf-8'))

## get uploader information
for author in soup.findAll('div', attrs = {'class': 'yt-lockup-byline'}):
	uploader.append(str(author.find('a')['href'][6:]))
print uploader
print head