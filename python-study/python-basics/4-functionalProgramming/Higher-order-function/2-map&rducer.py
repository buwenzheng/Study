# Python 内建了map() 和 reducer() 函数

# map函数 接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
# map更改一个list
def multiply(c):
    return c * c
arr = [1,2,3,5]
r = map(multiply, arr)
print('change list', list(r))

# list转字符串
res = list(map(str, [1,2,3,4,5,6,6]))
print('转字符串', res)


# reduce函数把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做 累积 计算

# 求总和
from functools import reduce
def summing(x, y):
    return x + x
rres = reduce(summing, [1,2,3,4])
print('reduce求和', rres)

# 把序列[1, 3, 5, 7, 9]变换成整数13579
def sum2(x, y):
    return x * 10 + y
res2 = reduce(sum2, [1,3,5,7,9])
print('变整数', res2)

# 配合map实现int功能
def chart2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
res3 = reduce(sum2, map(chart2num, '1233'))
print('仿int', res3)

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
    return name.title()
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    def multiply2(x,y):
        return x * y
    return reduce(multiply2, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
