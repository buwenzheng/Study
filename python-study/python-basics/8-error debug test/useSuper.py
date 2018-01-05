class A(object):
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        # A.__init__(self)
        super(B, self).__init__()
        print('B')        

class C(B, A):
    def __init__(self):
        # A.__init__(self)
        # B.__init__(self)
        super(C, self).__init__()
        print('C')

s = C()
# 使用super函数来调用父类的函数，只会每个父类调用一次，不会重复调用，且在子类中，不用到处写出所有的父类名字，符合DRY原则
