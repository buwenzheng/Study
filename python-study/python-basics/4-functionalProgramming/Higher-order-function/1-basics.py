# 高阶函数英文叫Higher-order function
# 1、变量可以指向函数
f = abs
f(-1)

# 简单高阶函数
def add(x, y, f):
    return f(x) + f(y)
s = add(-5, 3, abs)
print(s)
