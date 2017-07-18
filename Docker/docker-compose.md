---
title: "Docker Compose"
date: 2016-02-23 19:58
---

[dockercompose doc][1]

## 0x02 yml模板文件

### command

重写默认的命令，支持两种格式

```
command: bundle exec thin -p 3000
command: [bundle, exec, thin, -p, 3000]
```

command 不支持 多条命令通过 `&&` 连接执行，可以使用 `bash -c "cmd1 && cmd2"`
## 介绍

Docker Compose 是官方提供的容器业务流程框架(曾经的项目名称是Fig)。

Docker Compose 处理Docker容器部署分布式应用，可以定义哪个容器运行哪个应用。

使用Compose，只需要定义一个多容器应用的yml文件(docker-compose.yml)，然后使用一条命令(docker-compose up)即可部署运行所有的容器。

## 安装

```
pip install docker-compose

# 确认安装正确
docker-compose --version
```

## 使用方法

使用官网的简单示例

* 准备

```
mkdir compose_test
cd compose_test
```

新建 app.py ，使用flash web框架，数据库使用redis

```python
import os

from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return "Hello, i have been seen {n} times".format(n=redis.get('hits'))
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
```

创建 requirements.txt

```
flask
redis
```

* 创建镜像

Dockerfile创建镜像,

```
FROM python:2.7
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
```

* 定义服务

创建docker-compose.yml

```
web:
    build: .
    command: python app.py
    ports:
        - "5000:5000"
    volumes:
        - .:/code
    links:
        - redis

redis:
    image: redis
```

- web服务：该容器从当前文件夹的dockerfile创建，并运行 python app.py 命令; 将web容器内端口映射到主机5000端口;挂载当前文件夹到容器内部的/code文件夹，将web容器与redis容器连接

- redis服务：直接由官方的redis镜像创建

* 启动

```
docker-compose up
```

先启动redis容器，再启动web容器，然后两者连接起来

* 访问

firefox > 127.0.0.1:5000

```
curl 127.0.0.1:5000
```

[1]: https://docs.docker.com/v1.8/compose/yml/