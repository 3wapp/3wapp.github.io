---
title: "进(线)程处理"
date: 2016-05-28 11:41
---

## 0x00 介绍

[python 线程与协程][4]

并行: 简单来说并行就是我们现实世界运行的样子，每个人都是独立的执行单元，各自完成自己的任务，这对应着计算机中的分布式（多台计算机）或多核（多个CPU）运作模式

并发: 并发对应计算机中充分利用单核（一个CPU）实现（看起来）多个任务同时执行

一般来说，CPU密集型选用多进程，IO密集型选用多线程

```
0x01 parallel python
0x02 multiprocessing
0x03 threading
```

## 0x01 parallel 

> version: py 2,3

[parallel 官网][1]

[parallel demo][2]

Parallel Python 提供了 python 并发执行的机制，支持 SMP(systems with multiple processors or cores) 和 网络集群系统 (clusters)

### install

1. [parallel 官网][1] download and install

2. `pip install pp`

### module

Server

```
__init__(self, ncpus='autodetect', ppservers=(), secret=None, restart=False, proto=2, socket_timeout=3600)

submit(self, func, args=(), depfuncs=(), modules=(), callback=None, callbackargs=(), group='default', globals=None)
    Submits function to the execution queue
    
    func - function to be executed
    args - tuple with arguments of the 'func'
    depfuncs - tuple with functions which might be called from 'func'
    modules - tuple with module names to import
    callback - callback function which will be called with argument 
            list equal to callbackargs+(result,) 
            as soon as calculation is done
    callbackargs - additional arguments for callback function
    group - job group, is used when wait(group) is called to wait for
    jobs in a given group to finish
    globals - dictionary from which all modules, functions and classes
    will be imported, for instance: globals=globals()
```

### guide

SMP

```
1) Import pp module:

    import pp

2) Start pp execution server with the number of workers set to the number of processors in the system

    job_server = pp.Server() 

3) Submit all the tasks for parallel execution:

    f1 = job_server.submit(func1, args1, depfuncs1, modules1)
    f2 = job_server.submit(func1, args2, depfuncs1, modules1)
    f3 = job_server.submit(func2, args3, depfuncs2, modules2) 
   ...etc...

4) Retrieve the results as needed:

    r1 = f1()
    r2 = f2()
    r3 = f3()
``` 

## 0x02 multiprocessing

> 标准库

python 多进程管理

[document][3]

### 常用类

```
class multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={})

class multiprocessing.Pool([processes[, initializer[, initargs[, maxtasksperchild]]]])
# functions
apply_async(func[, args[, kwds[, callback]]])   非阻塞
apply(func[, args[, kwds]])     阻塞
map_async(func, iterable[, chunksize[, callback]])
map(func, iterable[, chunksize])    return list
close()        关闭pool，使其不在接受新的任务。
terminate()    结束工作进程，不在处理未完成的任务。
join()         主进程阻塞，等待子进程的退出， join方法要在close或terminate之后使用

class multiprocessing.pool.AsyncResult
    The class of the result returned by Pool.apply_async() and Pool.map_async()
# functions
get([timeout])  Return the result when it arrives
wait([timeout]) Wait until the result is available or until timeout seconds pass.
ready()         Return whether the call has completed
successful()    Return whether the call completed without raising an exception
```

** Pool: ** 启动大量的子进程，可以用进程池的方式批量创建子进程：

* demo

1. Process

```
```

2. Pool

```
def worker(arg1):
    print arg1
    return arg1

result = []
pool = multiprocessing.Pool(4)
for i in xrange(6):
    msg = "hello %d" %i
    result.append(pool.apply_async(worker, (msg,)))

pool.close()
pool.join()

for r in result:
    print r.get()

#     
multiple_results = [pool.apply_async(worker, (i,)) for i in range(6)]
print [res.get(timeout=1) for res in multiple_results]

#
print pool.map(worker, range(6)) 
```

### ** multiprocessing.dummy **

dummy 作用于线程

```
from multiprocessing.dummy import Pool as ThreadPool
```

### 备注 

在UNIX平台上，当某个进程终结之后，该进程需要被其父进程调用wait，否则进程成为僵尸进程(Zombie)， 所以，有必要对每个Process对象调用join()方法 (实际上等同于wait)。对于多线程来说，由于只有一个进程，所以不存在此必要性。

multiprocessing提供了threading包中没有的IPC(比如Pipe和Queue)，效率上更高。应优先考虑Pipe和Queue，避免使用Lock/Event/Semaphore/Condition等同步方式 (因为它们占据的不是用户进程的资源)。

多进程应该避免共享资源。在多线程中，我们可以比较容易地共享资源，比如使用全局变量或者传递参数。在多进程情况下，由于每个进程有自己独立的内存空间，以上方法并不合适。此时我们可以通过共享内存和Manager的方法来共享资源。但这样做提高了程序的复杂度，并因为同步的需要而降低了程序的效率

## 0x03 threading

> 标准库

[document][5]

### 常用类

```
class threading.Thread(group=None, target=None, name=None, args=(), kwargs={})
```






[1]: http://www.parallelpython.com/
[2]: http://www.parallelpython.com/content/view/17/31/
[3]: https://docs.python.org/2/library/multiprocessing.html
[4]: http://blog.rainy.im/2016/04/07/python-thread-and-coroutine/
[5]: https://docs.python.org/2/library/threading.html