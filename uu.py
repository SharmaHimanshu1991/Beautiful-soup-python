#/usr/bin/python

import bs4 as bs
import urllib2
from bs4 import BeautifulSoup

import requests

#source = requests.get('https://pythonprogramming.net/parsememcparseface/')
source = urllib2.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

#Then, we create the "soup." This is a beautiful soup object
#data=source.text
soup = bs.BeautifulSoup(source,'lxml')
#soup= soup.prettify()

# title of the page
print(soup.title)
print '#####################################'
# get attributes:
print(soup.title.name)
print '#####################################'
# get values:
print(soup.title.string)
print '#####################################'
# beginning navigation:
print(soup.title.parent.name)
print '#####################################'
# getting specific values:
print(soup.p)
print '#####################################'
#Finding paragraph tags <p> is a fairly common task. In the case above, we're just finding the first one. What if we wanted to find them all?
print(soup.find_all('p'))
print '#####################################'
for url in soup.find_all('a'):
    print(url.get('href'))
print '#####################################'
print(soup.get_text())
