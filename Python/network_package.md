---
title: "network package"
date: 2016-01-24 18:49
---

## 0x00 简介

## 0x01 pypcap

> 捕获数据包

### install

```
# kali2 install 
apt-get install libpcap-dev
pip install pypcap
```

### demo

```
import pcap

pc = pcap.pcap('eth0')
pc.setfilter('tcp port 80')
for ptime, pdata in pc:
    # ptime:收到的时间， pdata:收到的数据
    print ptime, pdata
```

## 0x02 dpkt

> 数据包解析，解析离线/实时 pcap 数据包

理解以太网数据的基本格式，逐层解析

```
eth = dpkt.ethernet.Ethernet(buf)   # buf 可以是 pypcap 捕获的数据包 pdata
ip = eth.data
src = socket.inet_ntoa(ip.src)
dst = socket.inet_ntoa(ip.dst)

tcp = ip.data 
udp = ip.dta
http = tcp.data
ftp = tcp.data
```

```
dpkt.pcap.Reader
```

## 0x03 scapy

## 0x04 scapy-http

> 格式化数据包为 http 数据信息

## 0x05 IPy

* install

```
pip install IPy
```

* example

```
from IPy import IP
IP('192.168.1.1').int()
IP('192.168.1.1').strHex()
IP('192.168.1.1').strBin()
```

