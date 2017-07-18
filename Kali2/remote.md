---
title: "Remote access"
date: 2016-01-24 18:52
---

## ssh

* ssh login

```
ssh -l root ip

or

ssh root@ip
```

* ssh-keygen [-f <filename>]

ssh-keygen 生成公钥和私钥文件，将公钥文件的内容，放到远程主机 $HOME/.ssh/authorized_keys 文件中，以后就可以免密码登录

* ssh 长连接设置

** client **

```
su
cd /etc/ssh
echo "    ServerAliveInterval 60" >> ssh_config
service ssh restart
exit
```

### SSH断开后 进程仍然在后台运行

当用户注销（logout）或者网络断开时，终端会收到 HUP（hangup）信号从而关闭其所有子进程, 而bash 是 sshd 的子进程，当 ssh 断开连接时，HUP 信号会影响到它下面的所有子进程


#### 解决思路

* 让进程运行在新的session(会话)里即不属于此终端的子进程。

* 可以实现让进程忽略HUP信号

#### 解决方法

* nohup命令

功能：不挂断地运行命令，忽略HUP信号。

语法：nohup command &

* setsid命令

功能：run a program in a new session在新的会话中运行程序

```
setsid ping www.baidu.com > /dev/null 
```

进程的父ID(PPID)是init

* () 内执行命令

```
(ping www.baidu.com > /dev/null &)
```

进程的父ID(PPID)是init

* screen命令

screen 是 init（PID为1）的子进程

## rdesktop

rdesktop is an implementation of a client software for Microsoft's proprietary Remote Desktop Protocol (RDP). Rdesktop is free and open-source software, 