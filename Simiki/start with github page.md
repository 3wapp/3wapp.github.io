---
title: "start github page"
date: 2016-01-17 15:50
---

# Simiki 快速开始

### install

```
pip isntall simiki
```

### update

```
pip install -U simiki
```

### Init Site

```
mkdir mywiki && cd mywiki

simiki init
```

### Create a new wiki

```
simiki new -t "start" -c Simiki
```

### Generate

```
simiki generate
```

### Preview

```
simiki preview
```


# github page

### 创建用户页面。

* 1.创建一个库名为 <Username> .github.io 。<Username>是您的Github上的用户名。

* 2.切换到你的本地站点，设置输出目录中的主分支：

```
cd output
git init
git add .
git commit -m 'your comment'
# These steps will be shown when you create a repo in Github:
git remote add origin git@github.com:<Username>/<Username>.github.io
git push -u origin master
```

* 3.回到父目录，并新建.gitignore文件：

```
cd ../
touch .gitignore
```

* 4.编辑.gitignore的内容：

```
*.pyc
output
```

* 5.安装源分支：

```
git init
git checkout -b wiki
git add .
git commit -m 'your comment'
# These steps will be shown when you create a repo in Github:
git remote add origin git@github.com:<Username>/<Username>.github.io
git push -u origin wiki
```

等待一段时间，访问 HTTPS:// <Username> .github.io 


# 在其他地方同步github，并继续写作

```bash
mydir mywiki
cd mywiki
git init
git remote add origin git@github.com:<Username>/<Username>.github.io
git pull origin wiki:master     #同步的是 wiki 分支, 保存的是源文件
simiki generate
cd output
git init 
git remote add origin git@github.com:<Username>/<Username>.github.io
git pull origin master:master     #同步的是 master 分支, 保存的是输出文件
```

产生更新后，分别推送 源文件 和 输出文件 到相应分支

* mywiki 目录下

```bash
git push origin master:wiki
```

* output 目录下

```bash
git push origin master:master
```


# 备注

1. simiki generate 必须在主目录下
2. output 在github **master**分支，而源文件资源在**wiki**分支