---
title: "Centos7"
date: 2016-01-21 04:42
---


注：
（1）源：http://pkgs.repoforge.org/

## 安装google-chrome：

wge获取安装：https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm 

OR:

```
# wget http://chrome.richardlloyd.org.uk/install_chrome.sh
# chmod u+x install_chrome.sh
# ./install_chrome.sh
```

## 网络开机自启

修改/etc/sysconfig/network-scripts/ifcfg-eno16777736 ：ONBOOT=yes

## 用户赋予“sudo”权限

1）切换到root环境：$ su -
2) 输入：#visudo
3） 增加一行：your_user_name ALL=(ALL)  ALL

## install ns2

1）获取ns-allinone-2.35，解压：/home/zh/Downloads

2) $./install

3)问题：

A.  tk8.4.18 make failed! Exiting …  

```
$sudo yum install libX11-devel 
$sudo yum install libXmu-devel
```

B.  tclcl-1.19make failed! Exiting ...  make: g++:命令未找到 

```
$sudo yum install gcc-c++，注意，这个软件包叫gcc-c++，不是g++
```

C.error: make:***[linkstate/ls.o] 

修改ls文件：

```
ns-2.35/linkstate/ls.h  第137行
void eraseAll() { erase(baseMap::begin(), baseMap::end()); }改为：
void eraseAll() { this->erase(baseMap::begin(), baseMap::end()); }
```

得到如下信息：

```
IMPORTANT NOTICES:
(1) You MUST put /home/zh/Downloads/ns-allinone-2.35/otcl-1.14, /home/zh/Downloads/ns-allinone-2.35/lib, 
    into your LD_LIBRARY_PATH environment variable.
    If it complains about X libraries, add path to your X libraries 
    into LD_LIBRARY_PATH.
    If you are using csh, you can set it like:
                setenv LD_LIBRARY_PATH <paths>
    If you are using sh, you can set it like:
                export LD_LIBRARY_PATH=<paths>

(2) You MUST put /home/zh/Downloads/ns-allinone-2.35/tcl8.5.10/library into your TCL_LIBRARY environmental
    variable. Otherwise ns/nam will complain during startup.
```

按着提示修改环境变量：

```
vim ~/.bashrc,然后添加三行：
export PATH=$PATH:你的路径
export LD_LIBRARY_PATH=你的路径
export TCL_LIBRARY=你的路径
export PATH="$PATH:/home/zh/Downloads/ns-allinone-2.35/bin:/home/zh/Downloads/ns-allinone-2.35/tcl8.5.10/unix:/home/zh/Downloads/ns-allinone-2.35/tk8.5.10/unix"

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/home/zh/Downloads/ns-allinone-2.35/otcl-1.14:/home/zh/Downloads/ns-allinone-2.35/lib"
   
export TCL_LIBRARY="$TCL_LIBRARY:/home/zh/Downloads/ns-allinone-2.35/tcl8.5.10/library"
```

然后关闭shell窗口并重新打开，执行ns命令出现%符号，说明环境变量也配置好了
