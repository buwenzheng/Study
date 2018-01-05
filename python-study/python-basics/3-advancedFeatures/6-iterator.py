# 可以直接作用于for循环的数据类型有以下几种：

# 一类是集合数据类型，如list、tuple、dict、set、str等；
#
# 一类是generator，包括生成器和带yield的generator function。
#
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
#
# 可以使用isinstance()判断一个对象是否是Iterable对象

for x in [1,2,3,4,5,6]:
    pass
#  等价于

it = iter([1,2,3,4,5,6])
while True:
    try:
        x = next(it)
    except StopIteration:
        break
#  for 循环是通过不断的调用next()函数
