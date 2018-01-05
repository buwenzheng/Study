# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性.
class Student(object):
    pass

# 接着尝试绑定一个属性
s = Student()
s.name = 'fuckoff'
print(s.name)
# fuckoff

# 还可以绑定一个方法
def set_age(self, age):
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s) #給实例绑定方法
s.set_age(12)
print(s.age)
# 12

# 给一个实例绑定的方法，对于另外一个实例是不起作用的
s2 = Student()
# s2.set_age(13)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Student' object has no attribute 'set_age

# 为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score = score
Student.set_score = set_score
# 这样的话所有的实例就都可用set_score方法


#  使用__slots__
# 如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Students(object):
    __slots__ = ('name', 'age') #用tuple定义允许绑定的属性名称
ss = Students()
ss.name = 'mi'
# ss.score = 2
#  Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Student' object has no attribute 'score'   

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Students):
    pass
g = GraduateStudent()
g.score = 17 #此时设置属性不受影响    