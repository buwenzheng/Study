# !/user/bin/env python3
# -*- conding: utf-8 -*-
' a test moudle ' # __doc__可读取注释
__author__ = 'BW'

# import sys
#
# def test():
#     args = sys.argv
#     if len(args) == 1:
#         print('Hello World')
#     elif len(args) == 2:
#         print('Hello %s' % args[1])
#     else:
#         print('Too many arguments!')
#
# print(test.__name__)
# if __name__ == '__main__':  # __name__有两个取值 当模块是被其他模块调用执行的时候取值是模块的名字 当模块是直接执行的时候 就取值为__main__ 所以在python模式执行的时候是不会执行test()
#     test()
' a test modules '

__author__ = 'buwenzheng'

import sys

def _private_1(name):
     res = 'Hello, %s' % len(name)
     print(res)
     return

def _private_2(name):
     res = 'Hi, %s' % name[1]
     print(res)
     return

def greeting():
    args = sys.argv
    print(len(args)) # 这里的sys模块的argv最终会返回个list，第一个是模块文件路径，后面是输入的变量
    if len(args) == 1:
        return _private_1(args)
    elif len(args) > 3:
        return _private_1('sb')
    else:
        return _private_2(args)

if __name__ == '__main__':
    greeting()
