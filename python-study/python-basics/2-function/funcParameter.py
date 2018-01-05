#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  得出一个数的n次方
# def power(x, n):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s

# 不可变参数
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# 可变参数
def calc(*numbers):
    sun = 0
    for n in numbers:
        sun = sun + n * n
    return sun
