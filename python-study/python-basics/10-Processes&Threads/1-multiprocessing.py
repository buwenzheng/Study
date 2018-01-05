# 多进程

# Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。

# 子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。

# Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程


# print('Processes (%s) start...' % os.getpid())
# fork方法仅在Unix内核的系统上使用
# pid = os.fork()
# if pid == 0:
#     print('I\'m child processes (%s) and my parent is %s' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getppid, os.getpid()))    


# multiprocessing 跨平台多进程模块
from multiprocessing import Process
import os, time, random

def run_proc(name):
    print('Run child processes %s (%s) and ParentPid---(%s)' % (name, os.getpid(), os.getppid()))

if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = Process(target=run_proc, args=('test',))   
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

# Pool进程池模块
# look at Pool.py


# 子进程
# look at subprocess2

# 进程之间通信
# look at interprocesses commiunication.py