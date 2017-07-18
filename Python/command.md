---
title: "命令执行"
date: 2016-06-27 14:51
---


# subprocess

可以创建新的进程，可以与新建进程的输入/输出/错误管道连通，并可以获得新建进程执行的返回状态. `使用subprocess模块的目的是替代os.system()、os.popen*()、commands.*等旧的函数或模块。`

注意： 当执行命令的参数或者返回中包含了中文文字，那么建议使用subprocess，如果使用os.popen则会出现错误

## subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False)

> 执行args 描述的命令, `等待命令完成`，然后返回returncode属性。 

> 不要使用stdout=PIPE或stderr=PIPE，基于子进程的输出流量可能导致死锁。需要管道时，使用Popen和它的communicate()方法

* demo

```python
>>> subprocess.call(["ls", "-l"])
0

>>> subprocess.call("exit 1", shell=True)
1
```

### 经常用到的参数

* args 

一个`字符串`或者一个程序参数的`序列`。一般倾向于提供一个参数的序列，让该模块来处理参数的转义和引用（例如允许文件名中包含空格）。
如果传递一个单一的字符串，`shell必须为True`，或者该字符串必须`不带任何参数`。

* stdin、stdout 和stderr 

分别指定程序的标准输入、标准输出和标准错误文件的句柄。

合法的值有PIPE、一个已经存在的文件描述符（一个正整数）、一个已经存在的文件对象和None。
PIPE表示应该为子进程创建一个新的管道。如果为默认设置None，则不会发生重定向；子进程的文件句柄将从父进程中继承。

stderr 可以为STDOUT，表示来自子进程中标准错误的数据捕获到和标准输出相同的文件中。

当stdout 或者stderr 为管道时且universal_newlines 为True，那么所有的行结束符将被转换成'\n' ，正如open()的universal newlines 'U' 模式参数所描述的一样。

* shell 

`shell=True`，则指定的命令将通过shell执行。方便地访问shell功能，例如shell 管道、文件名通配符、环境变量的扩展以及~访问某个用户的home目录

## subprocess.check_call

```
subprocess.check_call(args, *, stdin=None, stdout=None, stderr=None, shell=False)
```

> 执行带参数的命令, `等待命令完成`。如果返回码是`零`则返回，否则抛出`CalledProcessError`， 返回码在`returncode`属性中。

> 不要使用stdout=PIPE或stderr=PIPE，基于子进程的输出流量可能导致死锁。需要管道时，使用Popen和它的communicate()方法

## subprocess.check_output

```python
subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False)
```

> 执行带参数的命令并将它的输出作为`字节字符串`返回。如果返回码非零，引发CalledProcessError, 返回码保存在`returncode`属性中并把任何输出都保存在`output`属性中。

> 不要使用stdout=PIPE或stderr=PIPE，基于子进程的输出流量可能导致死锁。需要管道时，使用Popen和它的communicate()方法

* demo

```python
In [2]: subprocess.check_output(['echo', '123'])
Out[2]: '123\n'

# 结果中捕获标准错误，可以使用 stderr=subprocess.STDOUT：
In [15]: subprocess.check_output( "ls ff; exit 0", stderr=subprocess.STDOUT, shell=True)
Out[15]: "ls: cannot access 'ff': No such file or directory\n"
```

## subprocess.Popen

```
class subprocess.Popen(args, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=False, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0)
```

> 在Unix上，shell=True，默认为/bin/sh

* demo 

```python
# 替换shell 的管道
# output=`dmesg | grep hda`
p1 = Popen(["dmesg"], stdout=PIPE)
p2 = Popen(["grep", "hda"], stdin=p1.stdout, stdout=PIPE)
# Allow p1 to receive a SIGPIPE if p2 exits.
p1.stdout.close()  		
output = p2.communicate()[0]

# or
output=check_output("dmesg | grep hda", shell=True)

# communicate()方法来使用PIPE给子进程输入:
import subprocess
child = subprocess.Popen(["cat"], stdin=subprocess.PIPE)
child.communicate("vamei")

import shlex, subprocess
>>> command_line = raw_input()
/bin/vikings -input eggs.txt -output "spam spam.txt" -cmd "echo '$MONEY'"
>>> args = shlex.split(command_line)		# args正确的分词
>>> print args
['/bin/vikings', '-input', 'eggs.txt', '-output', 'spam spam.txt', '-cmd', "echo '$MONEY'"]
>>> p = subprocess.Popen(args)
```

* Popen 类的实例

```
Popen.poll()	检查子进程是否已经终止。设置并返回returncode属性。
Popen.wait()	等待子进程终止。设置并返回returncode属性。
Popen.communicate(input=None) 与进程交互：将数据发送到标准输出。从标准输出和标准错误读取数据，直至到达文件末尾。等待进程终止。
		可选的input 参数应该是一个要发送给子进程的字符串，如果没有数据要发送给子进程则应该为None。
		communicate()返回一个元组(stdoutdata, stderrdata)。
		该方法会阻塞父进程，直到子进程完成
Popen.send_signal(signal)	发送信号signal 给子进程。
Popen.terminate()	终止子进程
Popen.kill()		杀死子进程

# 下面的属性也可以访问， 
# 使用communicate()而不要用.stdin.write、.stdout.read 或.stderr.read，避免由于其它操作系统管道缓存填满并阻塞子进程引起的死锁。
Popen.stdin		如果stdin 参数为PIPE，则该属性为一个文件对象，它提供子进程的输入。
			否则，为None。
Popen.stdout		如果stdout 参数为PIPE，则该属性是一个文件对象，提供子进程中的输出。
			否则，为None。
Popen.stderr		如果stderr 参数为PIPE，则该属性是一个文件对象，提供子进程中的错误输出。
			否则，为None。
Popen.pid		子进程的进程ID。shell为True，为产生的shell的进程ID。
Popen.returncode	子进程的返回码, None值表示子进程还没有终止。
			负值-N表示子进程被信号N终止（Unix）。
```

## 0x01 os

### os.system()

> 不返回shell命令的输出

```
In [28]: os.system('ls')
tmp
Out[28]: 0
```

### os.popen()

> 返回输出结果

```
>>>tmp = os.popen('ls *.sh').readlines()  
>>>tmp  
['install_zabbix.sh\n', 'manage_deploy.sh\n', 'mysql_setup.sh\n', 'python_manage_deploy.sh\n', 'setup.sh\n'] 
```

## 0x02 commands

可以很方便的取得命令的输出（包括标准和错误输出）和执行状态位

### commands.getstatusoutput(cmd)   

返回（status,output)

```
import commands
a,b = commands.getstatusoutput('ls')
a是退出状态
b是输出的结果。
>>> import commands
>>> a,b = commands.getstatusoutput('ls')
>>> print a
0
>>> print b
anaconda-ks.cfg
install.log
install.log.syslog
```

### commands.getoutput(cmd)        

只返回输出结果


