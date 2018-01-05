# 文档测试
# 代码与其他说明可以写在注释中，然后，由一些工具来自动生成文档。既然这些代码本身就可以粘贴出来直接运行，那么，可不可以自动执行写在注释中的这些代码呢？

# def abs(n):
#      '''
#      Function to get absolute value of number.

#      Example:

#      >>> abs(1)
#      1
#      >>> abs(-1)
#      1
#      >>> abs(0)
#      0
#      '''
#      return n if n >= 0 else (-n)

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()

# 练习
# 对函数fact(n)编写doctest并执行
def fact(n):
    '''
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()