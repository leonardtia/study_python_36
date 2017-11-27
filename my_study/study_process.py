import os
import random
import subprocess
import time

print('Process (%s) start...' % os.getpid())
pid = os.fork()  # 操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回
if pid == 0:
    # 1932创建了子进程8566
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    # 8566创建了子进程8567
    print('I (%s) just created a child process(%s).' % (os.getppid(), os.getpid()))
print('-----------------------------------')
from multiprocessing import Process, Pool


def run_proc(name):
    '''
    创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    '''
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end')
print('-----------------------------------')


# 启动大量的子进程
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done..')
    p.close()
    p.join()
    print('All subprocesses done.')

print('$ nslookup www.baidu.com')
r = subprocess.call(['nslookup', 'www.baidu.com'])
print('Exit code:', r)
