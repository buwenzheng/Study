# 如果你听说过“测试驱动开发”（TDD：Test-Driven Development），单元测试就不陌生。
# 单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。

# 比如对函数abs()，我们可以编写出以下几个测试用例：

# 输入正数，比如1、1.2、0.99，期待返回值与输入相同；

# 输入负数，比如-1、-1.2、-0.99，期待返回值与输入相反；

# 输入0，期待返回0；

# 输入非数值类型，比如None、[]、{}，期待抛出TypeError。

# 把上面的测试用例放到一个测试模块里，就是一个完整的单元测试。

# look 3-mydict.py & 3-mydict_test.py


# practice 

import unittest

# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def get_grade(self):
#         if self.score >= 60:
#             return 'B'
#         if self.score >= 80:
#             return 'A'
#         return 'C'

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if 100 < self.score or self.score < 0:
            raise ValueError('Invalid score: %s' % self.score)
        elif self.score >= 60 and self.score < 80:
            return 'B'
        elif self.score >= 80:
            return 'A'
        return 'C'

class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

if __name__ == '__main__':
    unittest.main()    