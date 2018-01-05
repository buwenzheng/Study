import logging # logging模块会打印错误信息， 并且程序会一直执行下去 如果没有logging模块，出错会停止运行

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try: 
        bar('0')
    except Exception as e:
        logging.exception(e)    

main()
print('END')

# 报错 
# Traceback (most recent call last): 错误的跟踪信息  
#   File "err.py", line 11, in <module>  调用main出错在err.py的第11行 原因在第9行
#     main()
#   File "err.py", line 9, in main 调用bar('0')出错在err.py的第9行 原因在第6行
#     bar('0')
#   File "err.py", line 6, in bar 原因是return foo(s) * 2 这个语句，但是不是最终原因
#     return foo(s) * 2
#   File "err.py", line 3, in foo 原因是return 10 / int(s) 这个语句出错， 这里是错误的源头， 因为底下打印的ZeroDivisionError: division by zero
#     return 10 / int(s)
# ZeroDivisionError: division by zero  根据错误类型ZeroDivisionError 判断，int(s)本身没有错误，但是int(s)返回0， 至此，找到错误源头
# 出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置

