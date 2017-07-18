## docker for mac

不同于linux原生支持docker, windows和mac都需要一层虚拟机来支持docker, 因此使用方面也有了一定的限制, 参考 [Networking features in Docker for Mac](https://docs.docker.com/docker-for-mac/networking/)

### macOS 没有 `docker0 bridge`

macOS现在对docker的虚拟化支持是由`HyperKit`实现的，因此网络接口也是在HyperKit里面，在macOS就看不到`docker0 bridge`了

### 主机和容器互访

* 主机不能通过容器ip访问容器服务

linux中，主机可以通过容器的ip访问容器里面的服务，而mac的实现方式不同于linux,因此，容器所在的网络，对mac主机来说是不可达的。

* 容器不能通过网关访问主机服务

## 解决方案

### 容器访问主机的服务

由于mac主机的ip可能经常变化，或者没有ip(在没有网络接入的情况下)，因此容器通过mac主机的ip来访问主机服务就很不方便。推荐做法是：绑定一个不用的ip在mac的`lo0`接口上，如：`sudo ifconfig lo0 alias 10.10.10.1/24`, 然后确信你主机的服务监听在这个ip或`0.0.0.0`(而不是127.0.0.1)，这样容器就可以访问主机的服务了。

### 主机访问容器的服务

实现主机访问容器的服务，可以通过`docker`的`-p`参数实现端口映射，从而实现主机访问容器的服务, 如: `docker run -d -p 80:80 --name webserver nginx`

