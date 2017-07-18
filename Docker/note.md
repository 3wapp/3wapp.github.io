---
title: "note"
date: 2016-02-19 17:47
---

* docker 镜像

ubuntu
debian
alpine  体积小，内置完整的包管理器(apk)
busybox

* read

[Dockerfile 最佳实践][5]

[10张图带你深入理解Docker容器和镜像][6]

## [ Daocloud ][2]

[docker 简明教程][4]

## [ Docker Hub ][3]

* login

```
docker login
# then input username, email password
```

* push

```
# build
docker build -t username/newimage:tag .

# http://hub.docker.com > Create Repository
docker push username/newimage
```

删除 Volumes
Volume 只有在下列情况下才能被删除：
docker rm -v 删除容器时添加了 -v 选项
docker run –rm 运行容器时添加了 –rm 选项
否则，会在 /var/lib/docker/vfs/dir 目录中遗留很多不明目录。


Docker的文件系统AUFS，一种“增量文件系统”，用户所做修改以增量的方式保存，决定了其分层存储特性。


```
# 查看环境信息
docker info  
docker version

# 在官方仓库中查找镜像
docker search ubuntu

# 下载获取ubuntu镜像
docker pull ubuntu

# 列出本机拥有的镜像
docker images

# 列出目前运行的容器
docker ps

# 列出最近的容器，包含未正在运行的
docker ps -l

# 挂载一个正在后台运行的容器
docker attach 23ad234

# 列出并追踪容器的运行日志
docker logs -f -t 23ad234

# 暂停运行的容器
docker pause 23ad234

# 恢复暂停的容器
docker unpause 23ad234

# 启动/停止/重启容器(start/stop/restart)
docker start 23ad234

# 显示容器内运行的进程, 每2s刷新一次
docker top 23ad234 -d 2

# 查看容器运行的详细信息
docker inspect 23ad234

# 杀掉正在运行的容器
docker kill 23ad234

# 显示容器文件系统的改动
docker diff 23ad234

# 复制容器中的文件或文件夹到主机系统中
docker cp 23ad234:~/test.txt ./test.txt

# 将容器导出为tar包
docker export 23ad234 > mytest.docker.tar

# 创建一个空容器并导入tar包
docker import ./mytest.docker.tar

# 将容器改动提交到镜像中
docker commit -m mytest 23ad234 ijse/test:mytag

# 列出镜像的历史
docker history ijse/test:mytag

# 登陆官方仓库账户
docker login

# 修改本地镜像名称
docker rename ijse/test ijse/mytest

# 将镜像推送到仓库中
docker push ijse/mytest:mytag

# 删除一个容器 及其关联的数据卷
docker rm -v 23ad234

# 删除一个镜像
docker rmi ubuntu

# 将本机镜像保存为tar包
docker save -o ijse.test.tar ijse/mytest

# 通过Dockerfile来创建一个镜像
docker build ./Dockerfile
```

Docker相关术语

### LXC

LXC（Linux Container）Linux Container容器是一种内核虚拟化技术，可以提供轻量级的虚拟化，以便隔离进程和资源，而且不需要提供指令解释机制以及全虚拟化的其他复杂性。相当于C++中的NameSpace。容器有效地将由单个操作系统管理的资源划分到孤立的组中，以更好地在孤立的组之间平衡有冲突的资源使用需求。与传统虚拟化技术相比，它的优势在于:

* 与宿主机使用同一个内核，性能损耗小；
* 不需要指令级模拟；
* 不需要即时(Just-in-time)编译；
* 容器可以在CPU核心的本地运行指令，不需要任何专门的解释机制；
* 避免了准虚拟化和系统调用替换中的复杂性；
* 轻量级隔离，在隔离的同时还提供共享机制，以实现容器与宿主机的资源共享。

总结：Linux Container是一种轻量级的虚拟化的手段。Linux Container提供了在单一可控主机节点上支持多个相互隔离的server container同时执行的机制。Linux Container有点像chroot，提供了一个拥有自己进程和网络空间的虚拟环境，但又有别于虚拟机，因为lxc是一种操作系统层次上的资源的虚拟化。

### Hypervisor

Hypervisor是一种运行在物理服务器和操作系统之间的中间软件层,可允许多个操作系统和应用共享一套基础物理硬件，因此也可以看作是虚拟环境中的“元”操作系统，它可以协调访问服务器上的所有物理设备和虚拟机，也叫虚拟机监视器（Virtual Machine Monitor）。Hypervisor是所有虚拟化技术的核心。非中断地支持多工作负载迁移的能力是Hypervisor的基本功能。当服务器启动并执行Hypervisor时，它会给每一台虚拟机分配适量的内存、CPU、网络和磁盘，并加载所有虚拟机的客户操作系统。

### 容器VS 虚拟机

容器会比虚拟机更高效，因为它们能够分享一个内核和分享应用程序库。相比虚拟机系统，这也将使得 Docker使用的内存更小，即便虚拟机利用了内存超量使用的技术。部署容器时共享底层的镜像层也可以减少存储占用。IBM 的 Boden Russel 已经做了一些基准测试来说明两者之间的不同。

相比虚拟机系统，容器具有较低系统开销的优势，所以在容器中，应用程序的运行效率将会等效于在同样的应用程序在虚拟机中运行，甚至效果更佳。

## 利用git仓库， docker镜像更新自动化

[镜像管理][7]

镜像制作方面，应该坚持三个原则，第一是坚持镜像总是从Dockerfile生成。这样做最大的好处是可以通过Dockerfile“阅读”镜像，在后续的协作、升级维护等方面会带来巨大的便利。第二是镜像之间应该避免依赖过深，建议为三层，这三层分别是基础的操作系统镜像、中间件镜像和应用镜像。第三是坚持所有镜像都应该有对应的Git仓库，以方便后续的更新。

镜像的更新需要一个自动化的流程，这可以通过SCM和CI系统自动触发实现。具体的流程如下图所示。开发者首先将代码和Dockerfile提交到Git仓库，然后Git通过webhook方式触发Jenkins的主动获取代码和Dockerfile文件，Jenkins再通过Docker相关的插件生成镜像并推送镜像到私有的Registry。这样，在服务器上就可以通过拉取新的镜像部署容器。

## Docker方案

* [Kitematic][1]

Kitematic 是一个具有现代化的界面设计的自由开源软件，它可以让我们在 Docker 中交互式执行任务。Kitematic 设计的非常漂亮、界面美观。使用它，我们可以简单快速地开箱搭建我们的容器而不需要输入命令，可以在图形用户界面中通过简单的点击从而在容器上部署我们的应用。

Kitematic 集成了 Docker Hub，允许我们搜索、拉取任何需要的镜像，并在上面部署应用。它同时也能很好地切换到命令行用户接口模式。目前，它包括了自动映射端口、可视化更改环境变量、配置卷、流式日志以及其它功能。

## docker container support utf-8

write to Dockerfile

```
# Install program to configure locales
RUN apt-get update \
    && apt-get install -y locales \
    && dpkg-reconfigure locales && \
        locale-gen C.UTF-8 \
    && /usr/sbin/update-locale LANG=C.UTF-8

# Install needed default locale for Makefly
RUN echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen \
    && locale-gen

# Set default locale for the environment
ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
```

## 权限

```
/var/run/docker.sock
srw-rw----  1 root     docker        0 Mar 17 12:52 docker.sock
```

用户加入docker用户组中，免去输入sudo语句。

```
$ sudo usermod -aG docker <用户名>
```

> 注意：这条语句需要重新登陆终端才能生效

> 注意：docker用户组的权限等同于root用户组，在生产环境中这样做可能会导致安全问题!

## docker 实战

[http://dockone.io/article/217][8]


[1]: https://github.com/docker/kitematic
[2]: https://account.daocloud.io/signup
[3]: https://hub.docker.com/
[4]: http://blog.saymagic.cn/2015/06/01/learning-docker.html
[5]: https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/
[6]: http://dockone.io/article/783
[7]: http://www.infoq.com/cn/news/2015/04/several-docker-practice
[8]: http://dockone.io/article/217
