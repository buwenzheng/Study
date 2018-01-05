# !/user/bin/env python3
# -*- conding: utf-8 -*-

# 获取对象信息
# type()获取对象的类型，基本类型都可以用type()，来判断

type(123) # 输出 <class 'init'>

type(abs)
# <class 'builtin_function_or_method'>

# 但是type()函数返回的是什么类型？它返回对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同

type(123)==type(456)
# True
type(123)==int
# True
type('abc')==type('123')
# True
type('abc')==str
# True
type('abc')==type(123)
# False

# 判断基本数据类型可以直接写int,str等，但是如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量:

import types
def fn():
    pass

type(fn) == types.FunctionType
# True

type(abs) == types.BuiltinFunctionType
# True

type(lambda x: x)==types.LambdaType
# True

type((x for x in range(10)))==types.GeneratorType
# True

# 使用isinstance()
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数
# isinstance()可以告诉我们，一个对象是否是某种类型。先创建3种类型的对象

class Animal(object):
    def run(self):
        print('Animal is running')

class Dog(Animal):
    def run(self):
        print('Dog is running')        

class Cat(Dog):
    def run(self):
        print('Cat is running')        

a = Animal()
d = Dog()
c = Cat()

print(isinstance(a, Animal))
# True

print(isinstance(c, Dog))
# True

print(isinstance(c, Animal))
# True

# 能用type()判断的基本类型也可以用isinstance()判断

isinstance('234', str)
# True

# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple
isinstance(([1,2,3]), (list, tuple))
# True


# 使用dir()
dir('asd')
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的
len('abc')
# 3
'abc'.__len__
# 3

# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法
class myDog(object):
    def __len__(self):
        return 12
dog = myDog()
print(len(dog)) # 12

# 剩下的都是普通属性或方法，比如lower()返回小写的字符串
'ABC'.lower()
# 'abc'

# 仅仅把属性和方法列出来是不够的，配合getattr(),setattr(),hasattr()，可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 6
    def power(self):
        return self.x * self.x
obj = MyObject()

hasattr(obj, 'x') # 是否有属性'x'    
# True
hasattr(obj, 'y') # 是否有'y'
# False
setattr(obj, 'y', 19) # 设置一个属性'y'
hasattr(obj, 'y') 
# True
obj.y # 此时设置了属性y
# 19

# 如果试图获取不存在的属性，会抛出AttributeError的错误
getattr(obj, 'z') # 获取属性'z'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'MyObject' object has no attribute 'z'

# 可以传入一个default参数，如果属性不存在，就返回默认值
getattr(obj, 'z', 404) # 获取属性'z'，如果不存在的话就返回404

# 也可以获取对象的方法
hasattr(obj, 'power') # 确认有无
getattr(obj, 'power') # 获取对象的power方法

# 小结

# 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：

# sum = obj.x + obj.y
# 就不要写：

# sum = getattr(obj, 'x') + getattr(obj, 'y')
# 一个正确的用法的例子如下：

# def readImage(fp):
#     if hasattr(fp, 'read'):
#         return readData(fp)
#     return None
# 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。

# 请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能

