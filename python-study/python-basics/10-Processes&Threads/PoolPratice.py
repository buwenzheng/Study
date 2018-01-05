from multiprocessing import Pool
import os, time, random

# 创建子进程执行函数
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds' % (name, (end - start)))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    # Pool()里面的参数设置最多同时执行多少个进程
    p = Pool(10)
    for i in range(1000):
        p.apply_async(long_time_task, args=(i,))    
    print('Watting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
