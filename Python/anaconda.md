---
title: "Anaconda"
date: 2016-07-12 07:51
---

# 0x00 Anaconda

Anaconda 是一个免费的Python科学计算环境， 下载地址： [Download](https://www.continuum.io/downloads) ， 文档: [Document](https://docs.continuum.io/anaconda/index).

[Linux Installation](https://docs.continuum.io/anaconda/install#linux-install):

* Download the installer.  
* In your terminal window type one of the below and follow the instructions:

Python 2.7: `bash Anaconda2-4.1.1-Linux-x86_64.sh`  
Python 3.5: `bash Anaconda3-4.1.1-Linux-x86_64.sh`

NOTE: Include the "bash" command even if you are not using the bash shell.

update: `conda update anaconda`.

## 0x01 包管理 conda

Anaconda 提供了包管理工具: `conda`, 文档: [conda document](http://conda.pydata.org/docs/index.html) 

```
conda list              列出已安装的python包/框架
conda install swapi     安装特定的包
conda install setuptools==1.9.2     安装特定的版本
cpnda uninstall setuptools          卸载包
conda update conda
conda create --name py3 python=3
```

## 0x02 Anaconda Navigator  

Anaconda Navigator is a desktop graphical user interface included in Anaconda that allows you to easily manage conda packages, environments and channels without the need to use the command line

install:`conda install anaconda-navigator`.