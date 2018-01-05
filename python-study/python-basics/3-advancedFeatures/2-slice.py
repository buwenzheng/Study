#  切片拓展符
n = [1,2,3]
# print(n[1:])

# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
def trim(num):
    if len(num) == 0:
        return num
    if num[:1] == ' ':
        return trim(num[1:])
    if num[-1:] == ' ':
        return trim(num[:-1])
    else:
        return num

# print(trim('    q w e  '))
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!1')
elif trim('  hello') != 'hello':
    print('测试失败!2')
elif trim('  hello  ') != 'hello':
    print('测试失败!3')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
