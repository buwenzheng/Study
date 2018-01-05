# Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。要注意，这里的偏函数和数学意义上的偏函数不一样。(这里的偏函数是为了降低函数调用的难度)
import functools
int2 = functools.partial(int, base=2)

print(int2('100'))
