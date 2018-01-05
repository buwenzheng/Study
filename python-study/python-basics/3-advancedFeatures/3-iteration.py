#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
# 判断一个对象是否可以迭代
# 从collections集合引入Iterable模块
from collections import Iterable
isinstance('abc', Iterable)

def findMinAndMax(B):
    if B == []:
        return (None, None)
    m = n = B[0]
    for i in B:
        if m > i:
            m = i
        if n < i:
            n = i
    return m, n

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
