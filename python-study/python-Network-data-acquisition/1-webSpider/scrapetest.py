from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# try:
#     html = urlopen("http://pythonscraping.com/pages/page1.html") 
# except HTTPError as e:
#     print(e)
#     # 返回空值，中断程序，或者执行另外一个方案
     
# bsObj = BeautifulSoup(html.read())


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None  
    try:
        bsObj = BeautifulSoup(html.read())    
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title    

tite = getTitle("http://pythonscraping.com/pages/page1.html")


if tite == None:
    print("Title could not be found")    
else:
    print(tite)

