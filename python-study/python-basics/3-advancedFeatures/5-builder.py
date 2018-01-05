# 元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator
# 定义斐波那契数列生成函数
# 带yield关键字的函数是generator 是一种定义generator的方式
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# f = fib(9)
# print(f)
# for i in f:
#     print(i)

# 输出杨辉三角
def triangles(n):
    L = [1]
    while len(L) < n+1:
        yield list(L)
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]
n = 10
results = []
for t in triangles(n):
    print(t)
    results.append(t)
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
