#/usr/bin/python

from bs4 import BeautifulSoup, Comment

import requests

url = raw_input("Enter a website to extract the URL's from: ")

r  = requests.get(url)

data = r.text


soup = BeautifulSoup(data,"lxml")
for link in soup.find_all('a'):
    print(link.get('href'))

'''
comments= soup.findAll(text=lambda text:isinstance(text, Comment))
    #if comment in ['UNIQUE COMMENT', 'SECOND UNIQUE COMMENT']:
for c in comments:
	print '#####################'
        print c.next_element.strip()
	print c.extract()
	print '2222222222222222222222'
	print c.decompose()
#print soup.prettify()[0:200]
print '333333333333333333333'
'''


