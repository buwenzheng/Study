# !/usr/bin/env python
# -*- coding: utf-8 -*-


# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
# 首先，我们看看itertools提供的几个“无限”迭代器：

import itertools
# natuals = itertools.count(1)
# for n in natuals:
#     print(n)

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：

ns  = itertools.repeat('ABC', 3)
for i in ns:
    print(i)

print('-------------------')

# 无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。

# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：

ns2 = itertools.count(1,2)
ns2list = itertools.takewhile(lambda x: x < 10, ns2)
print(list(ns2list)) 

print('-------------------')

# chain()
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for i in itertools.chain('ABC', 'ZXY'):
    print(i)

print('-------------------')


# groupby()
# groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key,group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

print('-------------------')

# 练习
# 计算圆周率可以根据公式：
# 利用Python提供的itertools模块，我们来计算这个序列的前N项和：

import itertools

def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...

    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.

    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...

    # step 4: 求和:
    c = itertools.cycle([4, -4])
    s = sum(next(c) / (2*x - 1) for x in range(1, N+1))
    return s
    # return sum(next(itertools.cycle([4,-4])) / (itertools.count(1,2) for i in range(1, N+1)))

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')

for x in range(2, 10):
    print(x)