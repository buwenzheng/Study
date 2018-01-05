# StringIO
# 很多时候，数据读写不一定是文件，也可以在内存中读写。

# StringIO顾名思义就是在内存中读写str。

# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可

from io import StringIO,BytesIO

f = StringIO('hello\nhi\ngoodbye')

while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# BytesIO 
# 操作二进制数据
n = BytesIO()
n.write('年后'.encode('utf-8'))
print(n.getvalue())
