# !/user/bin/env python3
# -*- conding: utf-8 -*-

# 在OPP程序设计中,当我们定义一个class的时候,可以从某个现有的class继承,新的class称为(Subclass),而被继承的class称为基类 父类或者超类(Baseclass, Superclass)

# 比如，我们已经编写了一个名为Animal的class，有一个run()方法可以直接
class Animal(object):
    def run(self):
        print('Animal is running')

# 当我们编写Dog和Cat类的时候，可以从Animal类继承
class Dog(Animal):
    # 可以对子类增加一些方法
    def run(self):
        print('Dog is running')

    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    def run(self):
        print('Cat is running')

# 对于Dog来说，Animal就是他的父类，对于Animal来说，Dog就是它的子类。
# 继承的好处，子类获取了父类的全部功能。Dog与Cat两个子类都会有Animal类的run方法
# 但是当子类和父类都存在相同的run()方法的时候，子类的run()会覆盖掉父类的run()。在代码运行的时候总是会调用子类的run()方法，这就是继承的里一个好处: 多态

# 在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行
b = Animal()
isinstance(b, Dog) # 输出false

# 理解多态的好处，我们还需要再编写一个函数，这个函数接受一个Animal类型的变量
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly')


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog())
run_twice(Tortoise())
# 新增一个Animal的子类，不必对run_twice()做任何修改，实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。
# 多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思

# 对于一个变量，我们之需要知道他是Animal类型，无需确切的知道他的子类型，就可以放心的调用run()方法，而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则
# 对拓展开放：允许新增Animal子类
# 对修改开放: 不需要依赖Animal类型的run_twice()等函数
# 继承还可以一级一级地继承下来，就好比从爷爷到爸爸、再到儿子这样的关系。而任何类，最终都可以追溯到根类object，这些继承关系看上去就像一颗倒着的树。


# 静态语言 vs 动态语言

# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。

# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
# Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。但是，许多对象，只要有read()方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。

# 小结

# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。

# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。
