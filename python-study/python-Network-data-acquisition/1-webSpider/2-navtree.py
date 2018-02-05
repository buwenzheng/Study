from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')

bsObj = BeautifulSoup(html.read(), 'html.parser')

# 打印所有的标签
# n = 0
# for child in bsObj.find('table', {'id': 'giftList'}).children:
#     n+=1
#     print(n)
#     print(child)

# 处理兄弟标签
# for sibling in bsObj.find('table', {'id': 'giftList'}).tr.next_siblings:
    # print(sibling)

# 父标签处理
print(bsObj.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text()) 

print('-------------------')

# 配合正则查找图片路径
images = bsObj.findAll('img', {'src': re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
# print(images)
for image in images:
    for at in image.attrs:
        print(at == 'src')        

print('-------------------')

# 配合lambda表达式
lamTags = bsObj.findAll(lambda tag: len(tag.attrs) == 2)  
# print(lamTags)

