# 定制类
# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
# __slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。
# 除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类

# __str__
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__ # s = Student()  s 此时会调用的是__repr__，为开发调试服务
print(Student('bob'))
# Student object (name: bob)
# 这样可一自己定义打印出来的东西，且表达清晰


# __iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

# 以斐波那契数列为例子

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器

    def __iter__(self):
        return self # 实例本身就是迭代对象，所以要返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算
        if self.a > 10000:
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)        


# __getitem__ 
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行,要表现得像list那样按照下标取出元素，需要实现__getitem__()方法

class Fib2(object):
    # 为了兼容list的切片方法。需要做出处理
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None: # 如果没有开始索引则默认为0
                start = 0
            a, b = 1, 1  
            L = []
            for x in range(stop):
                if x >= start: 
                    L.append(a)
                a, b = b, a+b
            return L  

            
print(Fib2()[0])
print(Fib2()[:10])
# __getattr__ 
# 在没有找到属性的情况下才会调用__getattr__

class Human(object):
    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \' %s\'' % attr)

t = Human()
print(t.age())
#  25 

# 如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改
# 利用完全动态的__getattr__，我们可以写出一个链式调用
class Chain(object):
    # 初始化路径信息
    def __init__(self, path=''):
        self._path = path

    # 利用__getattr__的特性拼接地址
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    # 设置打印出来的地址 
    def __str__(self):
        return self._path

    # 开发调试赋值 
    __repr__ = __str__

print('Chain path:   ', Chain().baidu.users.userCenter.ChirsDay)


# __call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用

class Student3(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s' % self.name)

s = Student3('Buwenzheng')
# 通过对__call__对与类的自定义，可以时这个类被直接调用
s()

# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。

# 如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。

# 通过callable()函数能查看一个对象是否为可调用对象
callable(s)
# True
callable(abs)
# True
callable('123')
# false