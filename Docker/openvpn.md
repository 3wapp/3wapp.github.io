---
title: "openvpn"
date: 2016-02-20 14:08
---

## 获取镜像

```
docker pull kylemanna/openvpn
```

## quick start

```
OVPN_DATA="ovpn-data"

# 初始化ovpn_data容器，包含配置文件和证书
docker run --name $OVPN_DATA -v /etc/openvpn busybox

#
docker run --volumes-from $OVPN_DATA --rm kylemanna/openvpn ovpn_genconfig -u udp://VPN.SERVERNAME.COM  #更改VPN.SERVERNAME.COM为你的ip或域名

# 生成EasyRSA PKI 证书授权中心
docker run --volumes-from $OVPN_DATA --rm -it kylemanna/openvpn ovpn_initpki

# input ca pssword for securiry
...

#sart openvpn server process
docker run --volumes-from $OVPN_DATA -d -p 1194:1194/udp --cap-add=NET_ADMIN kylemanna/openvpn
```

* sh 文件配置

```
#!/bin/bash
set -ex
OVPN_DATA=ovpn-data
CLIENT=xx-client
IMG=kylemanna/openvpn

#
# Create a docker container with the config data
# 初始化ovpn_data容器，包含配置文件和证书
docker run --name $OVPN_DATA -v /etc/openvpn busybox

# fetch host ip
ip addr ls
SERV_IP=$(ip -4 -o addr show scope global  | awk '{print $4}' | sed -e 's:/.*::' | head -n1)


docker run --volumes-from $OVPN_DATA --rm $IMG ovpn_genconfig -u udp://$SERV_IP

# nopass is insecure
docker run --volumes-from $OVPN_DATA --rm -it -e "EASYRSA_BATCH=1" -e "EASYRSA_REQ_CN=Travis-CI Test CA" $IMG ovpn_initpki nopass

docker run --volumes-from $OVPN_DATA --rm -it $IMG easyrsa build-client-full $CLIENT nopass

docker run --volumes-from $OVPN_DATA --rm $IMG ovpn_getclient $CLIENT > $CLIENT.ovpn

#
# Fire up the server
#
iptables -N DOCKER
ptables -I FORWARD -j DOCKER

# run in shell bg to get logs
docker run --name "ovpn-server" --volumes-from $OVPN_DATA --rm -p 1194:1194/udp --privileged $IMG  1>/root/ovpn_info.log 2>/root/ovpn_error.log &
```

* 生成客户端证书和配置文件

替换CLIENTNAME, 客户端的名字是用来识别正在运行的OpenVPN客户端的机器, e.g. CLIENTNAME:phone

```
# 创建客户端证书
docker run --volumes-from $OVPN_DATA --rm -it kylemanna/openvpn easyrsa build-client-full CLIENTNAME nopass

# 传送到客户端证书和配置文件
docker run --volumes-from $OVPN_DATA --rm kylemanna/openvpn ovpn_getclient CLIENTNAME > CLIENTNAME.ovpn
```

## 配置 openvpn 客户端

在Ubuntu12.04/14.04和Debian wheezy/jessie客户端（或者类似的）：
安装OpenVPN：

```
sudo apt-get install openvpn
```

* 命令行启动

```
sudo openvpn CLIENTNAME.ovpn
```

*  OpenVPN Network Manager plugin

```
sudo apt-get install network-manager-openvpn-gnome
```
 then import .ovpn file

* note

The OpenVPN protocol requires the client and server to have synchronized time. If the time on your local PC is incorrect you may see the error ##TLS Error: Unroutable control packet received## from in your logs

solve [TLS Error: Unroutable control packet received][3]

## 验证操作

有几种通过VPN路由来验证网络连接的方法。

* 网页浏览器

访问网站来确定外部IP地址。外部IP地址应该是OpenVPN服务器。
试试google“what is my ip”或icanhazip.com。


* 命令行

从命令行，wget或curl命令派上用场。以curl为例：

```
curl icanhazip.com
```

以wget为例：

```
wget -qO - icanhazip.com
```

预期的反应应该是OpenVPN服务器的IP地址。

另一个选择是使用dig或使用host到一个特殊配置的DNS服务器做专用的DNS查询。基于host的例子：

```
host -t A myip.opendns.com resolver1.opendns.com
```

基于dig的例子：

```
dig +short myip.opendns.com @resolver1.opendns.com
```

预期的反应应该是OpenVPN服务器的IP地址。

## 参考

[在Ubuntu14.04的Docker容器中运行OpenVPN][1]

[kylemanna/openvpn OpenVPN for Docker][2]

[1]: http://dockone.io/article/214
[2]: https://hub.docker.com/r/kylemanna/openvpn/
[3]: https://www.ivpn.net/knowledgebase/152/TLS-Error-Unroutable-control-packet-received.html
