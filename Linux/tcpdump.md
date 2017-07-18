## info

tcpdump是一个抓包工具。它能够监听、记录通过某一个主机进出的网络流量。并且可以保存到文件，或者再从文件读取抓下来的数据包。

## usage

* usage 

```
tcpdump [ -AbdDefhHIJKlLnNOpqRStuUvxX# ] [ -B buffer_size ]
        [ -c count ]
        [ -C file_size ] [ -G rotate_seconds ] [ -F file ]
        [ -i interface ] [ -j tstamp_type ] [ -m module ] [ -M secret ]
        [ --number ] [ -Q in|out|inout ]
        [ -r file ] [ -V file ] [ -s snaplen ] [ -T type ] [ -w file ]
        [ -W filecount ]
        [ -E spi@ipaddr algo:secret,...  ]
        [ -y datalinktype ] [ -z postrotate-command ] [ -Z user ]
        [ --time-stamp-precision=tstamp_precision ]
        [ --immediate-mode ] [ --version ]
        [ expression ]
```

* args

```
-i      指定监听的网络接口.
-c      收到指定的包的数目后，停止tcpdump.
-t      输出不打印时间戳
-w      直接将包写入文件中，并不分析和打印出来.
-r      从指定的文件中读取包(这些包一般通过-w选项产生).
-s snaplen      snaplen表示从一个包中截取的字节数。0表示包不截断，抓完整的数据包。默认tcpdump 只显示68字节。
-X      协议头和包内容都原原本本的显示出来（tcpdump会以16进制和ASCII的形式显示）-- 这在进行协议分析时是绝对的利器
-e      在输出行打印出数据链路层的头部信息，包括源mac和目的mac，以及网络层的协议；
-n      指定将每个监听到数据包中的域名转换成IP地址后显示，不把网络地址转换成名字；
-nn     指定将每个监听到的数据包中的域名转换成IP、端口从应用名称转换成端口号后显示

-a      将网络地址和广播地址转变成名字.
-d      将匹配信息包的代码以人们能够理解的汇编格式给出.
-dd     将匹配信息包的代码以c语言程序段的格式给出.
-ddd    将匹配信息包的代码以十进制的形式给出.
-e      在输出行打印出数据链路层的头部信息.
-f      将外部的Internet地址以数字的形式打印出来.
-l      使标准输出变为缓冲行形式.
-n      不把网络地址转换成名字.
-t      在输出的每一行不打印时间戳.
-v      输出一个稍微详细的信息，例如在ip包中可以包括ttl和服务类型的信息.
-vv     输出详细的报文信息.
-F      从指定的文件中读取表达式,忽略其它的表达式.
-T      将监听到的包直接解释为指定的类型的报文，常见的类型有rpc （远程过程调用）和snmp（简单网络管理协议.）
-p：    将网卡设置为非混杂模式，不能与host或broadcast一起使用
```

* protocal

```
ether   – 链路层协议
fddi    – 链路层协议
tr      – 链路层协议
wlan    – 链路层协议
ppp     – 链路层协议
slip    – 链路层协议
link    – 链路层协议
ip
arp
rarp
tcp
udp
icmp
ip6
radio
```

* 运算符

```
and     运算符 使用 and 或者 &&
OR      使用 or 或者 ||
EXCEPT  使用not 或者 ！
```


## 过滤

过滤表达式大体可以分成三种过滤条件，“类型”、“方向”和“协议”

* 网卡

```
tcpdump -i eth0
# 监听所有网卡
tcpdump -i any
```

* 主机

```
tcpdump host 192.168.0.2
# 源地址
tcpdump src host 192.168.0.2
# 目标地址
tcpdump dst host 192.168.0.1
```

* 端口

```
tcpdump port 80
# 端口范围
tcpdump portrange 21-23
# 源端口
tcpdump src port 1025
# 目的端口 
tcpdump dst port 389
```

* 网络

```
tcpdump net 192.168
tcpdump src net 192.168
tcpdump dst net 192.168
```

* 协议

```
tcpdump arp
tcpdump ip
tcpdump tcp
tcpdump udp
tcpdump icmp

```

* 大小

```
# 包大小过滤
tcpdump less 32
tcpdump greater 128
# 也可以这样使用
tcpdump >32
tcpdump <= 100
```


### 常用

* 抓取所有经过eth1，目的地址是192.168.1.254或192.168.1.200端口是80的TCP数据

```
tcpdump -i eth1 '((tcp) and (port 80) and ((dst host 192.168.1.254) or (dst host 192.168.1.200)))'
```

* 抓取所有经过eth1，目标MAC地址是00:01:02:03:04:05的ICMP数据

```
tcpdump -i eth1 '((icmp) and ((ether dst host 00:01:02:03:04:05)))'
```

* 抓取所有经过eth1，目的网络是192.168，但目的主机不是192.168.1.200的TCP数据

```
tcpdump -i eth1 '((tcp) and ((dst net 192.168) and (not dst host 192.168.1.200)))'
```