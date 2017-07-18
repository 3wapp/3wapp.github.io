

## configure

修改Redis的配置

* 使用Redis的访问账号

默认情况下，访问Redis服务器是不需要密码的，为了增加安全性我们需要设置Redis服务器的访问密码。设置访问密码为redisredis。


```
~ sudo vi /etc/redis/redis.conf

#取消注释requirepass
requirepass redisredis
```

* 让Redis服务器被远程访问

默认情况下，Redis服务器不允许远程访问，只允许本机访问，所以我们需要设置打开远程访问的功能。

```
~ sudo vi /etc/redis/redis.conf

#注释bind
#bind 127.0.0.1
```

修改后，重启Redis服务器。


未使用密码登陆Redis服务器

```
~ redis-cli

redis 127.0.0.1:6379> keys *
(error) ERR operation not permitted
```

发现可以登陆，但无法执行命令了。

登陆Redis服务器，输入密码

```
~  redis-cli -a redisredis

redis 127.0.0.1:6379> keys *
1) "key2"
2) "key3"
3) "key4"
```

登陆后，一切正常。

检查Redis服务器占用端口

```
~ netstat -nlt|grep 6379
tcp        0      0 0.0.0.0:6379            0.0.0.0:*               LISTEN
```

我们看到从之间的网络监听从 127.0.0.1:3306 变成 0 0.0.0.0:3306，表示Redis已经允许远程登陆访问。

我们在远程的另一台Linux访问Redis服务器

```
~ redis-cli -a redisredis -h 192.168.1.199

redis 192.168.1.199:6379> keys *
1) "key2"
2) "key3"
3) "key4"
```

远程访问正常。通过上面的操作，我们就把Redis数据库服务器，在Linux Ubuntu中的系统安装完成

## Redis Desktop Manager

[build Redis Desktop Manager](http://docs.redisdesktop.com/en/latest/install/#build-from-source)

* ubuntu

```
# 国内某些第三方包获取不到的情况下，可以在vps上获取，然后回传
git clone --recursive https://github.com/uglide/RedisDesktopManager.git -b 0.8.8
cd RedisDesktopManager/src/
./configure
source /opt/qt56/bin/qt56-env.sh && qmake && make && sudo make install
cd /usr/share/redis-desktop-manager/bin
sudo mv qt.conf qt.backup

sudo ln -s /usr/share/redis-desktop-manager/bin/rdm /usr/bin/redis-client

echo "source /opt/qt56/bin/qt56-env.sh" >> ~/.bashrc
```

`redis-client` to run Redis Desktop Manager