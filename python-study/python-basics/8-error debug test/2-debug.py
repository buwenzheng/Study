#  调试
# 断言

# 使用print()来辅助查看的地方可以使用断言(assert)来替代
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero'
    return 10 / n

def main():
    foo('0') 

# main()
# 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O(大写的o)参数来关闭assert,python -O filesName.py

# logging
# 把print()替换成logging是第三种方式，和assert比，logging不会抛出错误，而且可以输出到文件

import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
# 这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。

# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件


# pdb

