# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数

# >>> def now():
# ...     print('2015-3-25')
# ...
# >>> f = now
# >>> f()
# 2015-3-25
# 函数对象有一个__name__属性，可以拿到函数的名字：
#
# >>> now.__name__
# 'now'
# >>> f.__name__
# 'now'
# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

import functools,time # 利用functools模块复制原本的函数属性 保持返回的函数属性与传入的一致

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s() %s' % (func.__name__, text)) # 输出当前调用函数的__name__
            return func(*args, **kw) # 返回调用函数
        return wrapper
    return decorator

@log('lala')
def now():
    print('Now2012/12/12')

# n = log('lala')(now)

# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
def metric(fn):
    start_time = time.time()
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('%s executed in %s ms' % (fn.__name__, time.time() - start_time))
        return fn(*args, **kw)
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
