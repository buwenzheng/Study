# 函数作为返回值
def createCounter():
    def counter():
        i = 1
        while True:
            yield i
            i += 1
    return counter().__next__

# 相当于上面的解释
# def createCounter():
#     def counter():
#         i = 0
#         while True:
#             i += 1
#             yield i
#     y = counter()
#     def sum():
#         return next(y)
#     return sum

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
