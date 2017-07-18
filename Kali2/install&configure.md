---
title: "install and configure"
date: 2016-01-20 21:20
---

# rolling

## source

```
deb http://http.kali.org/kali kali-rolling main contrib non-free

# 中科大
deb http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
deb-src http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
deb http://mirrors.ustc.edu.cn/kali-security kali-current/updates main contrib non-free
deb-src http://mirrors.ustc.edu.cn/kali-security kali-current/updates main contrib non-free
```

kali的各种deb包: [http://http.kali.org/kali/pool/main/l/linux/](http://http.kali.org/kali/pool/main/l/linux/)

## ssh

* 1.编辑sshd_config文件: `vi /etc/ssh/sshd_config`
* 2.修改`PermitRootLogin prohibit-password`为`PermitRootLogin yes`
* 3.命令启动SSH服务: `/etc/init.d/ssh start` 或 `service ssh start` 或 `systemctl start ssh`
* 4.设置系统开机自动启动SSH服务:
`update-rc.d ssh enable  //系统自动启动SSH服务` 或 `systemctl enable ssh`

### 私钥登录

* 1. 本地生成SSH公私钥：`ssh-keygen -t rsa -C "your_email"`, 保存文件名为`xxx`
* 2. 将公钥`xxx.pub`的内容写入kali用户`.ssh/authorized_keys`文件中
* 本地`/etc/hosts`文件添加`kali`记录: `ip kali`
* 3. 本地`.ssh/config`加入如下内容：

```
Host kali
HostName kali
User root
IdentityFile ~/.ssh/xxx
```

* 4. ssh 登录：`ssh kali`

## reboot shutdown不能关机

solution:

先做 用户注销，然后返回到登录页面，点击关机或重启

## 不能挂载 exfat 格式硬盘

solution:

```
sudo apt-get install exfat-fuse exfat-utils
```

## zip 解压含中文文件名乱码

解决方案：

1. `unar file.zip`， unar 会自动检测文件编码， `-e` 选项指定文件编码

# kali2 sana

## 更新源

vim /etc/apt/sources.list

```
#中科大源
deb http://mirrors.ustc.edu.cn/kali sana main non-free contrib
deb-src http://mirrors.ustc.edu.cn/kali sana main non-free contrib
deb http://mirrors.ustc.edu.cn/kali-security/ sana/updates main contrib non-free
deb-src http://mirrors.ustc.edu.cn/kali-security/ sana/updates main contrib non-free
#阿里云kali源
deb http://mirrors.aliyun.com/kali sana main non-free contrib
deb http://mirrors.aliyun.com/kali-security/ sana/updates main contrib non-free
deb-src http://mirrors.aliyun.com/kali-security/ sana/updates main contrib non-free
```

## 安装输入法

```
apt-get install fcitx fcitx-googlepinyin
```

配置：应用程序>常用程序>系统工具>首选项>Fcitx配置 添加拼音

重启或用户注销

## upgrade to kali Rolling

```
root@kali:# cat << EOF >/etc/apt/sources.list
> deb http://http.kali.org/kali kali-rolling main non-free contrib
> EOF
root@kali:#apt-get update
root@kali:#apt-get dist-upgrade
root@kali:#reboot
```

## 设置 root 密码

```
sudo passwd
#输入root密码
#确认root密码

su root
```

## 安装火狐
```
apt-get remove iceweasel
echo -e "\ndeb http://downloads.sourceforge.net/project/ubuntuzilla/mozilla/apt all main" | tee -a /etc/apt/sources.list > /dev/null
apt-key adv --recv-keys --keyserver keyserver.ubuntu.com C1289A29
apt-get update
apt-get install firefox-mozilla-build
```
## 安装Chromium

```
sudo apt-get isntall chromium
```

## java

[install java tutorials][10]

### Download latest Java SE SDK :

To Download Java Select the file according to your operating system from the list.

Download Link : http://www.java.com/en/download/linux_manual.jsp

Java will be saved on Downloads/ folder or save it on /root.

Uncompress archive:

```
root@k4linux:~# tar -zxvf jre*.tar.gz
```

Move the extracted folder to /opt:

```
root@k4linux:~# mv jre* /opt
```

And go to the folder :

```
root@k4linux:~# cd /opt/jre*
```

### Install and register binaries Of Java :

This step registers the downloaded version of Java as an alternative, and switches it to be used as the default:

```
update-alternatives --install /usr/bin/java java /opt/jre*/bin/java 1
update-alternatives --install /usr/lib/mozilla/plugins/libjavaplugin.s­o mozilla-javaplugin.so /opt/jre*/lib/amd64/libnpjp2.so 1
update-alternatives --set java /opt/jre*/bin/java
update-alternatives --set javac /opt/jre*/bin/javac
update-alternatives --set mozilla-javaplugin.so /opt/jre*/lib/amd64/libnpjp2.so
```

Testing your installation OF Java on Kali Linux 2.0:

To check the browser plugin, restart your webrowser, and click “Do I have Java?”

To check the version of Java you are now running:

```
 root@k4linux:~# java -version
java version "1.8.0_60"
Java(TM) SE Runtime Environment (build 1.8.0_60-b27)
Java HotSpot(TM) 64-Bit Server VM (build 25.60-b23, mixed mode)
```

## proxy

* shadowsocks

install

```
pip install shadowsocks
```

run

```
sslocal -s <remote_ip> -p <remote_port> -k <password>
```

run with user login

```
vim ~/opt/ss.sh
    sslocal -s <remote_ip> -p <remote_port> -k <password>   #add to ss.sh

chmod u+x ss.sh

vim ~/.profile
    sh ~/opt/ss.sh 1>/dev/null 2>~/opt/ss.log &     #add to file end, 1:stdout 2:stderr
```

* socks proxy

1.安装

```
$ sudo apt-get install proxychains
```

2.编辑proxychains配置

```
$ vim /etc/proxychains.conf
```

3.将socks4 127.0.0.1 9095改为

> socks5 127.0.0.1 1080

ps: 默认的socks4 127.0.0.1 9095是tor代理，而socks5 127.0.0.1 1080是shadowsocks的代理

4.使用方法

在需要代理的命令前加上 proxychains ，如：

```
$ sudo proxychains apt-get update
```

## beef

beef use ruby-2.1.5

Debian / Ubuntu

* Install dependencies

```
gpg2 --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
or
curl -sSL https://rvm.io/mpapis.asc | gpg2 --import -

sudo apt-get update
sudo apt-get install curl git
curl -sSL https://raw.githubusercontent.com/wayneeseguin/rvm/master/binscripts/rvm-installer | bash -s stable
source ~/.rvm/scripts/rvm

# openssl patch, because openssl update that affects 2.1.5 compiling
curl https://github.com/ruby/ruby/commit/801e1fe46d83c856844ba18ae4751478c59af0d1.diff > openssl.patch
rvm install --patch ./openssl.patch 2.0.0

rvm install 2.1.5
rvm use 2.1.5 -- default
gem install bundler
```

Follow this instruction http://rvm.io/integration/gnome-terminal

* Download BeEF

```
git clone git://github.com/beefproject/beef.git
```

* Install gems and launch

```
cd beef
bundle install
./beef
```

## install docker

```
sudo vim /etc/apt/sources.list
    # add follow line in the file
    deb http://http.debian.net/debian jessie-backports main

sudo apt-get update
sudo apt-get install docker.io      

or

curl -sSL https://get.docker.com/ | sh
```

## irc

* irssi

```
sudo apt-get install irssi
```

## zbar -- decode 二维码

```
$ apt-get install libzbar-dev

$ pip install zbar
```

## 安装vpn

* openvpn

```
apt-get install -y openvpn
```

配置

```
vim ovpn.sh

=== ovpn.sh ===
#!/bin/bash

# run openvpn with configuration
# need root privilige
openvpn --config clientname.ovpn 1>ovpn_info.log 2>ovpn_error.log &
================

chmod u+x ovpn.sh

# run
sudo ./ovpn.sh
```

## 新增用户

```
useradd -m username
passwd username
usermod -a -G sudo username
chsh -s /bin/bash username
id username         #查看配置
```

## 开启SSH服务

```
#vi /etc/ssh/sshd_config   
```

将#PasswordAuthentication no的注释去掉，并且将NO修改为YES
将#PermitRootLogin yes的注释去掉

启动SSH服务

```
#/etc/init.d/ssh start    //or service ssh start
```

验证SSH服务状态

```
#/etc/init.d/ssh status
```

## 开机自启动

```
# vi /etc/rc.local

/etc/init.d/apache2 start
/etc/init.d/mysql start
exit 0
```

## terminal 设置

* 快捷键

设置>键盘>快捷键>自定义快捷键

名称：终端/terminal
命令：gnome-terminal

添加后，单击 disabled，按下 ctrl+alt+T

* menu

Edit menu -> Preferences

1.去掉 Show menubar by default in terminals 的勾选

2.Shortcuts menu, 勾选Enable shortcuts, Hide and Show toolbar 绑定快捷键F2.

> 设置 F2 显示或隐藏菜单栏，默认是隐藏菜单栏

## office

[wps][12]
[12]: http://wps-community.org/download.html


## gdb

kali2 默认安装好了gdb

#### peda

* install

```
git clone https://github.com/longld/peda.git ~/peda
echo "source ~/peda/peda.py" >> ~/.gdbinit
```

## nodejs

## source install ##

[nodejs download][9]

Prerequisites:

* `gcc` and `g++` 4.8 or newer, or
* `clang` and `clang++` 3.4 or newer
* Python 2.6 or 2.7
* GNU Make 3.81 or newer
* libexecinfo (FreeBSD and OpenBSD only)

```
$ ./configure
$ make
$ [sudo] make install
```

If your Python binary is in a non-standard location or has a
non-standard name, run the following instead:

```
$ export PYTHON=/path/to/python
$ $PYTHON ./configure
$ make
$ [sudo] make install
```

To run the tests:

```
$ make test
```

To build the documentation:

```
$ make doc
```

To read the documentation:

```
$ man doc/node.1
```

To test if Node.js was built correctly:

```
$ node -e "console.log('Hello from Node.js ' + process.version)"
```

## electronic-wechat 微信

[electronic-wechat github][8]

* install

1.intall nodejs

then

```
# 下载仓库
git clone https://github.com/geeeeeeeeek/electronic-wechat.git

# 进入仓库
cd electronic-wechat

# 安装依赖, 运行应用
npm install -g

npm start
```

或者下载 realease 的可执行安装包

## note

* use ~/.profile instead of ~/.bash_profile

## flash

```
su root
apt-get install flashplugin-nonfree
update-flashplugin-nonfree --install
```

* 安装百度云

首先先git一下：https://github.com/LiuLang/bcloud-packages

然后安装自己对应版本（32bit or 64bit）

```
dpkg -i bcloud-x.x.x.deb
apt-get -f install
```

* 安装网易云音乐

```
git clone https://github.com/cosven/FeelUOwn.git
cd FeelUOwn
./install.sh
```

> 注：遇到有什么依赖没有安装，根据提示缺少什么依赖安装什么依赖即可。

## ftp

* vsftp

install

```
$apt-get install vsftpd
```

config

```
$vim /etc/vsftpd.conf
    Write_enable=YES 将前面的#去掉
    chroot_local_user=YES 将前面的#去掉
$mkdir /home/hx/ftp
$chmod -R 777 ftp
$chmod a-w ftp
$sudo useradd -g ftp -d /home/hx/ftp/ <user>
$sudo passwd <user>
$sudo service vsftpd restart
```


## web环境(LAMP)配置

1.apache 服务启动     
```
sudo service apache2 start
```

2.修改网站默认打开路径

    /etc/apache2/sites-enabled/000-default.conf    
            修改“DocumentRoot /var/www/html" to "DocumentRoot yourpath"     这是修改80端口
    /etc/apache2/sites-available/default*
            修改“DocumentRoot /var/www/html" to "DocumentRoot yourpath"     这是修改443端口（可选）
    /etc/apache2/apache2.conf
            增加如下内容--进入权限
            <Directory yourpath>
                Options Indexes FollowSymLinks
                AllowOverride None
                Require all granted
            </Directory>

2.mysql 服务启动    

```
sudo service mysql start
```

* mysql root 默认无密码，设置密码

```
mysql -u root
>use mysql;
>UPDATE user SET Password=PASSWORD('<passwd>') WHERE User='root';
>flush privileges;
>exit;
```

3.php 配置      

直接在/var/www/html/(默认情况)目录放php文件，即可通过 http://127.0.0.1/xx.php 来访问
修改php.ini文件， 改为"display_errors = On"     重启apache生效

4.织梦模板

下载织梦源码包，解压，按要求操作！
a.安装GD扩展库：     
```
apt-get install php5-gd
```
b.php.ini(/etc/php5/apache2/php.ini) 找到 ”[gd]“， 在该区域下增加一行”extension=gd.so“

## funny tool

* 1.fuck

install

```
$ wget -O - https://raw.githubusercontent.com/nvbn/thefuck/master/install.sh | sh - && $0
```

use

```
$ fuck
```

## 命令行锁屏

```
# apt-get install gnome-screensaver
$ gnome-screensaver-command -l     #lock
$ gnome-screensaver-command -a     #active
```


## 系统设置


* 设置屏幕刷新率

```
$xrandr -r 60
```

## vmware

1. Install linux-headers-$(uname -r)
```
apt-get install linux-headers-$(uname -r)
```

2. Download and Install VMWare as normal

3. Patch for Kernel 4.0

```
$ curl http://pastie.org/pastes/9934018/download -o /tmp/vmnet-3.19.patch
Extract the vmnet module sources:
$ cd /usr/lib/vmware/modules/source


# tar -xf vmnet.tar
Apply the patch:
# patch -p0 -i /tmp/vmnet-3.19.patch
Recreate the archive:
# tar -cf vmnet.tar vmnet-only
Remove leftover:
# rm -r -only
Rebuild modules:
# vmware-modconfig --console --install-all

Fix network vitural not complie
# - as root user
$ cd /usr/lib/vmware/modules/source
$ tar -xvf vmnet.tar
# - edit the file vmnet-only/netif.c and replace the line that looks like
dev = allocnetdev(sizeof netIf, deviceName, VNetNetIfSetup);
to
dev = allocnetdev(sizeof netIf, deviceName, NETNAMEUNKNOWN, VNetNetIfSetup);
$ tar -cvf vmnet.tar vmnet-only/
$ rm -rf vmnet-only/
```

key：1A2ZZ-8RH06-AZTJ1-7A17H-32RM8


## webgoat

* 快速使用

    + 已安装java的条件下，根据github上说明进行安装，下载"*jar"文件

    ```
    https://github.com/WebGoat/WebGoat-Legacy/releases
    ```

    + run

    ```
    java -jar WebGoat-6.0.1-war.exec.jar".
    ```

    + browse

    ```
     http://localhost:8080/WebGoat
    ```

* 安装源码（for developers）

    + 下载source文件
    + 下载JAVA JDK，满足安装要求的版本，Kali自带java jdk且满足要求
    + 下载配置maven， http://maven.apache.org/  

    按要求下载 apache-maven-3.2.3-bin.tar.gz    

    下载文件解压至/usr/local/目录下

    vi /etc/profile 设置全局变量

```
M2_HOME=/usr/local/apache-maven-3.2.3
export M2_HOME
PATH=$PATH:$M2_HOME/bin
export PATH
```

```
#source /etc/profile  生效
```

测试是否成功

```
#mvn -v
```

maven 修建项目

```
#cd webgoat* #(webgoat 源码解压目录),
#mvn clean package
#mvn tomcat:run-war
```

选用eclipse，安装maven插件，

    name为：m2e,

    location为：http://download.eclipse.org/technology/m2e/releases

    当这样安装插件时会报错，原因是m2e插件和eclipse版本不匹配导致，location改为：http://download.eclipse.org/technology/m2e/releases/1.4 即可。



[8]: https://github.com/geeeeeeeeek/electronic-wechat/blob/master/README_zh.md?hmsr=toutiao.io&utm_medium=toutiao.io&utm_source=toutiao.io
[9]: https://nodejs.org/en/download/
[10]: http://www.k4linux.com/2015/11/kali-linux-2-0-tutorials-java.html
