# 错误处理
# 在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，这样，就可以知道是否有错，以及出错的原因。在操作系统提供的调用中，返回错误码非常常见。比如打开文件的函数open()，成功时返回文件描述符（就是一个整数），出错时返回-1。

# 用错误码来表示是否出错十分不便，因为函数本身应该返回的正常结果和错误码混在一起，造成调用者必须用大量的代码来判断是否出错
# 所以高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外。

# try
# 机制
try:
    print('try')
    # r = 10 / 0 错误发生的时候 这句之后的代码不会执行 因为捕获到了ZeroDivisionError
    r = 10 / int('a')
    print('result', r)
except ValueError as e:
    print('Value', e)    
except ZeroDivisionError as e:
    print('except', e)
# 没有遇到上面的错误的时候会执行else语句 
else:
    print('no Error!')    
finally:
    print('finally...')        
print('END')

# 第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了
# try:
#     foo()
# except ValueError as e:
#     print('ValueError')
# except UnicodeError as e:
#     print('UnicodeError')    

# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理

def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        print('Error', e)
    finally:
        print('Finally...')        


# 调用栈
# look err.py


# 抛出错误
# 因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误
# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例。

class BooError(ValueError):
    pass

def boo(s):    
    n = int(s)
    if n == 0:
        raise BooError('invalid value: %s' % s)
    return 10 / n
boo('0')



