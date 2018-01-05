#  排序算法
# sorted()函数就可以对list进行排序
# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序, key指定的函数回作用于list的每一个元素
# 用绝对值进行排序
sorted([36, 5, -12, 9, -21], key=abs)

# 按照姓名排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

L2 = sorted(L, key=by_name)
print(L2)

# 成绩排序
def by_score(t):
    return t[1]
L3 = sorted(L, key=by_score, reverse=True)
print(L3)
