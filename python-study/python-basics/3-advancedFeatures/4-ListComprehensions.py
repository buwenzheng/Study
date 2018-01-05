# 简单的列表表达式
list(range(1, 4)) # [1,2,3]

[x * x for x in range(1, 11)] # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

[x * x for x in range(1, 10) if x % 2 == 0] #[4, 16, 36, 64, 100] 偶数相乘

[m + n for m in 'ABC' for n in 'XYZ'] # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ'] 内外层循环


#  请修改列表生成式，通过添加if语句保证列表生成式能正确地执行
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x for x in L1 if isinstance(x, str)]
print(L2)
