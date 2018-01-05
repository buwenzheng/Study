# !/user/bin/env python3
# -*- conding: utf-8 -*-

# 面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同

# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的
class Student(object):
# 类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
# 且__init__的第一个参数一直是self，表示创建的实例本身
    def __init__(self, name, score):
        self.name = name
        self.score = score

# 数据封装
    def print_score(self): #构建一个函数来访问上面键入的数据
        print('%s: %s' % (self.name, self.score))

    def print_grade(self):
        if self.score >= 90:
            print('A')
        elif self.score >= 60:
            print('B')
        else:
            print('C')            
