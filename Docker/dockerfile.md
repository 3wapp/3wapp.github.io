---
title: "Dockerfile"
date: 2016-02-20 10:39
---

## Dockerfile 指令选项:

```
FROM
MAINTAINER
RUN
CMD
EXPOSE
ENV
ADD
COPY
ENTRYPOINT
VOLUME
USER
WORKDIR
ONBUILD
```

* FROM 

```
FROM <image>
```

FROM 指定构建镜像的基础源镜像，如果本地没有指定的镜像，则会自动从 Docker 的公共库 pull 镜像下来。

FROM 必须是 Dockerfile 中非注释行的第一个指令，即一个 Dockerfile 从 FROM 语句开始。

FROM 可以在一个 Dockerfile 中出现多次

如果 FROM 语句没有指定镜像标签，则默认使用 latest 标签。

* MAINTAINER 

```
MAINTAINER <name>  --指定创建镜像的用户
```

* EXPOSE

```
EXPOSE <port> [<port>...]
```

告诉 Docker 服务端容器对外映射的本地端口，需要在 docker run 的时候使用 -p 或者 -P 选项生效

* CMD

CMD 会在启动容器的时候执行，build 时不执行，而 RUN 只是在构建镜像的时候执行，后续镜像构建完成之后，启动容器就与 RUN 无关了

* ENV

```
ENV <key> <value>       # 只能设置一个变量
ENV <key>=<value> ...   # 允许一次设置多个变量
```

指定一个环节变量，会被后续 RUN 指令使用，并在容器运行时保留。

例子:
```
ENV myName="John Doe" myDog=Rex\ The\ Dog \
    myCat=fluffy
```

等同于

```
ENV myName John Doe
ENV myDog Rex The Dog
ENV myCat fluffy
```

* USER

使用哪个用户跑container

* ADD

```
ADD <src>... <dest>
```

ADD 复制本地主机文件、目录或者远程文件 URLS 从 <src> 并且添加到容器指定路径中 <dest>。

<src> 支持通过 GO 的正则模糊匹配，具体规则可参见 Go filepath.Match

```
ADD hom* /mydir/        # adds all files starting with "hom"
ADD hom?.txt /mydir/    # ? is replaced with any single character
```

<dest> 路径必须是绝对路径，如果 <dest> 不存在，会自动创建对应目录
<src> 路径必须是 Dockerfile 所在路径的相对路径
<src> 如果是一个目录，只会复制目录下的内容，而目录本身则不会被复制

注:

> 所有拷贝到container中的文件和文件夹权限, 和原文件权限保持一致？？？

* COPY

```
COPY <src>... <dest>
```

COPY 复制新文件或者目录从 <src> 添加到容器指定路径中 <dest>。用法同 ADD，唯一的不同是不能指定远程文件 URLS。

下面一条命令，会出现 ##镜像中文件层次结构错乱的情况##，暂不清楚是什么造成的，仅记之

```
COPY code/* /root/code  # code 目录与 Dockerfile 位于同一级目录
```

正确的格式如下：

```
COPY code/ /root/code/  
```

* VOLUME

```
# 在容器内新建 /data 目录
VOLUME ["/data"]
```

VOLUME指令用来在容器中设置一个挂载点，可以用来让主机或其他容器挂载，以实现数据共享或对容器数据的备份、恢复或迁移

## note

* 1.避免使用 RUN apt-get upgrade

这样会打乱镜像中包的依赖，可能会出现问题
 
* 2.apt-get update 和 apt-get install 连接使用，避免缓存问题

```
RUN apt-get update && apt-get install -y \
    python   
```

* 3.COPY vs ADD

ADD 比 COPY 多了2个功能--下载URL和解压，其他一样

如果不希望压缩文件拷贝到container后会被解压，则使用COPY
如果需要自动下载URL并拷贝到container，则使用ADD

参考：

[docker 学习笔记][1]

[1]: http://blog.opskumu.com/docker.html
