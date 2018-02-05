# !/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl
# 禁止掉ssl证书的请求,防止报错
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bsObj = BeautifulSoup(html, 'html.parser')

rex = '^(/wiki/)((?!:).)*$'

for link in bsObj.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile(rex)):
    if 'href' in link.attrs:
        print(link.attrs['href'])
# print(bsObj.find('div', {'id': 'bodyContent'}))
# t = '/wiki/sb'
# r = re.match(rex, t).span()
# print(r)