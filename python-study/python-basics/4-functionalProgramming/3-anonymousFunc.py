# 在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数
# lambda表示匿名函数

list(map(lambda x: x * x, [1,2,3,4,5]))
# >>>[1,4,9,16,25]
# 这里的 lambda 等于 def f(x): return x*x

# 请用匿名函数改造下面的代码：
def is_odd(n):
    return n % 2 == 1

L = list(filter(lambda x: x % 2 == 1, range(1, 20)))

print(L)
