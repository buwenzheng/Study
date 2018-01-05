#!/usr/bin/env python3
# -*- coding: utf-8 -*-
sum = 0
for i in range(101):
    sum += i
print(sum)

# 请利用循环依次对list中的每个名字打印出Hello, xxx!
L = ['Bart', 'Lisa', 'Adam']
for i in L:
    print('hello', i)

# 打印1-10
n = 0
while n <= 100:
    if n > 10:
        break
    print(n)
    n += 1
print('END')

# 打印1-10之间的奇数
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
