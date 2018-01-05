from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')

bsObj = BeautifulSoup(html.read())

nameList = bsObj.findAll('span', {'class': 'green'})

# for name in nameList:
#     print(name.get_text()) # get_text()会把这些超链接，段落和标签都清除掉，只取文本节点


# 可以根据文本内容查找   
nameList1 = bsObj.findAll(text='red')

print(len(nameList1))


# 关键词参数keyword，可以选择指定属性的标签,不可使用class class是python保留字
allText = bsObj.findAll(id='text') # => bsObj.findAll('', {'id': 'text'})
allText2 = bsObj.findAll(class_='red')

print(allText2[0].get_text())


# 范围限制参数limit，虽然只限制于findALl方法。find其实等价于findAll的limit等于1时的情形。
