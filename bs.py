#/usr/bin/python

from bs4 import BeautifulSoup

import requests

url = raw_input("Enter a website to extract the URL's from: ")

r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data)
for link in soup.find_all('a'):
    print(link.get('href'))

#print soup

#print soup.prettify()[0:1000]

'''
from IPython.display import Image
Image('http://www.openbookproject.net/tutorials/getdown/css/images/lesson4/HTMLDOMTree.png')
'''





