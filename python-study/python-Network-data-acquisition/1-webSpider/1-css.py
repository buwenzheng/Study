# !/usr/bin/env python
# -*- coding: utf-8 -*-


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsObj = BeautifulSoup(html.read(), 'html.parser')

# nameList = bsObj.findAll('span', {'class':{ 'green', 'red' }})
nameList = bsObj.div.findAll(class_='green')
for name in nameList:
    print(name)

