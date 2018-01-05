# 运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：
from functools import reduce

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    print('ss', ss)
    ns = list(map(str2num, ss))
    print('ns', ns)
    # 要在传入参数之前将ns 转成list类型
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7')
    print('99 + 88 + 7 =', r)

main()