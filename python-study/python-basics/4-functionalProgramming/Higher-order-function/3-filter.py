# Python内建的filter()函数用于过滤序列
# 将序列中空字符串删掉
def not_empty(n):
    return n and n.strip()
# print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

# 用filter求素数
# 首先构建一个3开始的技术列的Iterator
# Iterable是惰性计算的，所以在python里面可以表示一个素数的集合等
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

# 筛选器
def _not_divisible(n):
     return lambda x: x % n > 0

# 定义素数生成器
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

# 生成素数数列
arr = []
for n in primes():
    if n < 100:
        arr.append(n)
    else:
        break
print(arr)

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
# 测试
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
