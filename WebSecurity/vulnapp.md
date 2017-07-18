---
title: "Vulnapp"
date: 2016-01-26 17:08
---

## docker vuln Environment

* [https://hub.docker.com/u/vulnerables/](https://hub.docker.com/u/vulnerables/)
* [https://github.com/Medicean/VulApps](https://github.com/Medicean/VulApps)
* [https://github.com/MyKings/docker-vulnerability-environment](https://github.com/MyKings/docker-vulnerability-environment)

## OWASP SecurityShepherd

[https://github.com/OWASP/SecurityShepherd](https://github.com/OWASP/SecurityShepherd)

虚拟机/安装包

https://github.com/OWASP/SecurityShepherd/releases/tag/v3.0

Docker镜像

https://hub.docker.com/r/ismisepaul/securityshepherd/

获取镜像：

```
docker pull ismisepaul/securityshepherd
```

获取shell：

```
docker run -i -p 80:80 -p 443:443 -p 27017:27017 -t ismisepaul/securityshepherd /bin/bash
```

运行mysql和tomcat：

```
/usr/bin/mongod &
/usr/bin/mysqld_safe &
service tomcat7 start
```

如果你没有安装配置authbind：

```
sudo apt-get install authbind
touch /etc/authbind/byport/80
touch /etc/authbind/byport/443
chmod 550 /etc/authbind/byport/80
chmod 550 /etc/authbind/byport/443
chown tomcat7 /etc/authbind/byport/80
chown tomcat7 /etc/authbind/byport/443
```

### 配置

参见：https://github.com/OWASP/SecurityShepherd/wiki

## dvwa

[github dvwa][1]
[install dvwa on ubuntu14][2]

[1]: https://github.com/RandomStorm/DVWA
[2]: http://hackthistv.com/blog/how-to-install-dvwa-on-ubuntu-server-14-04/

* linux install requirements

```
apt-get -y install apache2 mysql-server php5 php5-mysql php5-gd
```

* 默认用户

DVWA默认的用户有5个，用户名密码如下：

```
admin/password

gordonb/abc123

1337/charley

pablo/letmein

smithy/password
```
