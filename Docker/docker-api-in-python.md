---
title: "docker api in python"
date: 2016-03-17 16:44
---

## docker 远程访问

[docker config][3]

默认情况下，Docker守护进程会生成一个socket（/var/run/docker.sock）文件来进行本地进程通信，而不会监听任何端口，因此只能在本地使用docker客户端或者使用Docker API进行操作。
 
如果想在其他主机上操作Docker主机，就需要让Docker守护进程监听一个端口，这样才能实现远程通信。

```
$ sudo vim /etc/default/docker

DOCKER_OPTS="-H unix:///var/run/docker.sock -H tcp://0.0.0.0:2375"

$ sudo service docker restart
```

这样就可以本地和远程访问docker进程了。

## docker-py

[Python API 操作][1]
[docker-py api][2]

## install

```
pip install docker-py
```

## Client API

实例化Client class,与Dokcer daemon通信

```
from docker import Client
cli = Client(base_url='unix://var/run/docker.sock')
```

params:

* base_url(str)
* version(str)

参考 ##protocol + hostname + port ## 方式

```
base_url = 'tcp://127.0.0.1:2375'
base_url = 'unix://var/run/docker.sock' 
```

## create_container


## start

params:

* contaner(str): The container to start

```
# 'ubuntu' is a container's name
c.start('ubuntu') 
```

return:

None if success

## stop

params:

* container(str): The container to start
* timeout(int): Timeout in seconds to wait for the container to shop before sending a SIGKILL

```
# 'ubuntu' is a container's name
c.stop('ubuntu') 
```

return:

None if success

## stop




[1]: https://letong.gitbooks.io/docker/content/API/python_api.html
[2]: https://docker-py.readthedocs.org/en/latest/api/
[3]: https://docs.docker.com/engine/admin/configuring/
