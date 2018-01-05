# !/user/bin/env python3
# -*- conding: utf-8 -*-


# 作用域
# 在一个模块中，可能会定义很多函数和变量，有些时候我们希望这些变量给别人使用，有些时候只希望在模块内部使用。在python中是通过_前缀来实现的
# 正常的函数和变量名是公开的（public），可以被直接引用，譬如: abc, x123
# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是属特殊用途
# 类似_xxx和__xxx这样的函数或者变量就是非公开的（private），不应该被直接引用
# 但是并不是以这种形式定义变量或者函数就不可以被访问了，python内部并没有限制，这是一种编程习惯（写python是的习惯）

# private 函数的作用
' a test modules '

__author__ = 'buwenzheng'


def _private_1(name):
     res = 'Hello, %s' % name
     print(res)
     return

def _private_2(name):
     res = 'Hi, %s' % name
     print(res)
     return

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

if __name__ == '__main__':
    greeting('default')

# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public
