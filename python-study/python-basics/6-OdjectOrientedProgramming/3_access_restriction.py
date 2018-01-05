# !/user/bin/env python3
# -*- conding: utf-8 -*-

# 访问限制
# 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改

# class Student(object):
#
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     def print_score(self):
#         print('%s: %s' % (self.__name, self.__score))
#
#
# linkin = Student('linkin', 20)
# print(linkin.__name) # 这里是是不可以直接访问到实例中的值

# 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性

class Student(object):

    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender


# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')        
