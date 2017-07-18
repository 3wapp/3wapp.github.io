## fd (file descriptor）

文件描述符（file descriptor）是内核为了高效管理已被打开的文件所创建的索引，其是一个非负整数（通常是小整数），用于指代被打开的文件，所有执行I/O操作的系统调用都通过文件描述符

程序刚刚启动的时候，0是标准输入，1是标准输出，2是标准错误。如果此时去打开一个新的文件，它的文件描述符会是3。POSIX标准要求每次打开文件时（含socket）必须使用当前进程中最小可用的文件描述符号码

## /proc

[PROC(5) Linux Programmer's Manual](http://man7.org/linux/man-pages/man5/proc.5.html)

Linux系统上的/proc目录是一种文件系统，即proc文件系统。与其它常见的文件系统不同的是，/proc是一种伪文件系统（也即虚拟文件系统），存储的是当前内核运行状态的一系列特殊文件，用户可以通过这些文件查看有关系统硬件及当前正在运行进程的信息，甚至可以通过更改其中某些文件来改变内核的运行状态. 这些特殊文件中大多数文件的时间及日期属性通常为当前系统时间和日期，这跟它们随时会被刷新（存储于RAM中）有关

### 常用文件介绍

file | descript
 --- | ---
version | Linux内核版本和gcc版本
cmdline | 启动时传递给kernel的参数信息
cpuinfo | cpu的信息
filesystems | 内核当前支持的文件系统类型
sched_debug | 提供cpu上正在运行的进程信息，获得进程的pid号，配合后面pid的利用
mounts | 挂载的文件系统列表

/proc/sched_debug  
/proc/



```
/proc#cat /version
Linux version 4.8.0-kali2-amd64 (devel@kali.org) (gcc version 5.4.1 20161019 (Debian 5.4.1-3) ) #1 SMP Debian 4.8.11-1kali1 (2016-12-08)
```

### 目录

* /proc/N -- N 为数字，表示进程PID

```
#ls /proc/1/
attr        coredump_filter  gid_map    mountinfo   oom_score      schedstat  status
autogroup   cpuset           io         mounts      oom_score_adj  sessionid  syscall
auxv        cwd              limits     mountstats  pagemap        setgroups  task
cgroup      environ          loginuid   net         personality    smaps      timers
clear_refs  exe              map_files  ns          projid_map     stack      timerslack_ns
cmdline     fd               maps       numa_maps   root           stat       uid_map
comm        fdinfo           mem        oom_adj     sched          statm      wchan
```

items | description
 --- | ----
cmdline | 启动当前进程的完整命令，但僵尸进程目录中的此文件不包含任何信息
cwd | 指向当前进程运行目录的一个符号链接
environ | 进程环境变量列表,彼此间用空字符（NULL）隔开；变量用大写字母表示，其值用小写字母表示
exe | 指向启动当前进程的可执行文件（完整路径）的符号链接,通过`/proc/N/exe`可以启动当前进程的一个拷贝
fd | 目录,包含当前进程打开的每一个文件的文件描述符,这些文件描述符是指向实际文件的一个符号链接
maps | 与进程相关的内存映射信息
mem | 指代进程持有的内存，不可读
root | 指向当前进程运行根目录的符号链接
stat | 当前进程的状态信息，包含一系统格式化后的数据列，可读性差，通常由ps命令使用
statm | 进程使用的内存的状态
status | 进程状态信息，比stat/statm更具可读性
mountinfo | 文件系统挂载的信息，例如读docker文件映射



```
/proc# cat 1/cmdline
/sbin/init

/proc# ls -ald 1/cwd
lrwxrwxrwx 1 root root 0 12月 19 13:44 1/cwd -> /

/proc# cat 1/environ
CRYPTSETUP=yesSHLVL=1HOME=/init=/sbin/initTERM=linuxdrop_caps=BOOT_IMAGE=/boot/vmlinuz-4.8.0-kali2-amd64PATH=/sbin:/usr/sbin:/bin:/usr/bininitrd=/install/gtk/initrd.gzPWD=/rootmnt=/root

/proc# ls -al 1/exe
lrwxrwxrwx 1 root root 0 12月 19 13:35 1/exe -> /lib/systemd/systemd

/proc# ls 1/fd
0    101  108  111  14  18  21  25  29  32  36  41  46  5   55  6   64  71  75  92
1    102  109  112  15  19  22  26  3   33  39  42  47  50  56  60  65  72  8   99
10   103  11   12   16  2   23  27  30  34  4   43  48  52  58  62  66  73  9
100  107  110  13   17  20  24  28  31  35  40  45  49  54  59  63  7   74  90
```

* **/proc/self** 链接到当前正在运行的进程

* /proc/sys 系统信息和内核参数

```
/proc# ls sys
abi  debug  dev  fs  kernel  net  vm
```

* /proc/net 网卡设备信息

items | description
--- | ----
arp  | arp表，可以获得内网其他机器的地址
route | 路由表信息
tcp | tcp 连接信息
udp  | udp 连接信息
fib_trie | 路由缓存
