---
title: "git remote operation"
date: 2016-01-18 14:07
---

# git clone

* git clone <版本库的网址> [本地目录名]

1. 本地目录名可选，不指定的话，新建与远程目录名同名的本地目录

2. git clone支持多种协议，除了HTTP(s)以外，还支持SSH、Git、本地文件协议等，下面是一些例子。

```
$ git clone git@github.com:<username>/repo

$ git clone http[s]://example.com/path/to/repo.git/
$ git clone ssh://example.com/path/to/repo.git/
$ git clone git://example.com/path/to/repo.git/
$ git clone /opt/git/project.git 
$ git clone file:///opt/git/project.git
$ git clone ftp[s]://example.com/path/to/repo.git/
$ git clone rsync://example.com/path/to/repo.git/
```

一般来说，Git协议下载速度最快

3. 克隆版本库的时候，所使用的远程主机自动被Git命名为origin。如果想用其他的主机名，需要用git clone命令的-o选项指定。

```
$ git clone -o jQuery https://github.com/jquery/jquery.git
```

上面命令表示，克隆的时候，指定远程主机叫做jQuery。

# git remote

为了便于管理，Git要求每个远程主机都必须指定一个主机名。git remote命令就用于管理主机名。

不带选项的时候，git remote命令列出所有远程主机。
使用-v选项，可以参看远程主机的网址。

```
$ git remote
origin

$ git remote -v
origin  git@github.com:jquery/jquery.git (fetch)
origin  git@github.com:jquery/jquery.git (push)
```

上面命令表示，当前只有一台远程主机，叫做origin，以及它的网址。

* git remote show <主机名>, 查看该主机的详细信息。

* git remote add <主机名> <网址> 添加远程主机
 
* git remote rm <主机名> 删除远程主机。

* git remote rename  <原主机名> <新主机名> 远程主机的改名。


# git fetch

* git fetch <远程主机名> <分支名>

```
git fetch origin master
```

取回远程主机的更新以后，可以在它的基础上，使用git checkout命令创建一个新的分支

* $ git checkout -b newBrach origin/master 在origin/master的基础上，创建一个新分支

* git merge origin/master 本地分支上合并远程分支 origin/master

# git pull

git pull命令的作用是，取回远程主机某个分支的更新，再与本地的指定分支合并

* $ git pull <远程主机名> <远程分支名>[:<本地分支名>]

```
#取回origin主机的next分支，与本地的master分支合并
$ git pull origin next:master
```

如果远程分支是与当前分支合并，则冒号及其后面的部分可以省略

# git push

git push命令用于将本地分支的更新，推送到远程主机。它的格式与git pull命令相仿。

* $ git push <远程主机名> <本地分支名>:<远程分支名>

1. 如果省略远程分支名，则表示将本地分支推送与之存在"追踪关系"的远程分支(一般同名).如果该远程分支不存在，则会被新建。

2. 如果省略本地分支名，则表示删除指定的远程分支，因为这等同于推送一个空的本地分支到远程分支。

```
$ git push origin :master
# 等同于
$ git push origin --delete master
```

3. 如果当前分支与多个主机存在追踪关系，则可以使用-u选项指定一个默认主机，这样后面就可以不加任何参数使用git push。

```
$ git push -u origin master
```

4. 如果远程主机的版本比本地版本更新，推送时Git会报错，要求先在本地做git pull合并差异，然后再推送到远程主机。如果一定要推送，可以使用--force选项。

```
$ git push --force origin
```
 
使用--force选项，结果导致远程主机上更新的版本被覆盖。