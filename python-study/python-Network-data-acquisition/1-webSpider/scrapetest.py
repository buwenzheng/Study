from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# try:
#     html = urlopen("http://pythonscraping.com/pages/page1.html") 
# except HTTPError as e:
#     print('-------------------')
#     print(e)
#     # 返回空值，中断程序，或者执行另外一个方案
     
# bsObj = BeautifulSoup(html.read(), 'html.parser')
# print(bsObj)


# 完整写法
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle('http://pythonscraping.com/pages/page1.html')

if title == None:
    print('Title could not be found')
else:
    print(title)