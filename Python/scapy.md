---
title: "Scapy"
date: 2016-01-18 17:45
---

# DNS

## IP反向查询域名 Reverse IP Domain Check

# ARP

## ARP scan

局域网主机探测扫描，含有线或无线局域网

方式1 ARP请求

```
$sudo scapy

>pkt=Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(hwtype=1,ptype=0x0800,op=1,pdst="192.168.199.0/24")

>srp(pkt,timeout=5)

Begin emission:
Finished to send 256 packets.
.......
Received 7 packets, got 0 answers, remaining 256 packets
(<Results: TCP:0 UDP:0 ICMP:0 Other:0>, <Unanswered: TCP:0 UDP:0 ICMP:0 Other:256>)

>ans,unans=_

>ans.summary(lambda(s,r):r.sprintf("%Ehter.src%:%ARP.psrc%"))

??:192.168.199.1
```

opcode:1(请求包)
hardware type:1(以太网)
protocol type:0x0800(IP)


## send & receive

```
sr()
-- The sr() function is for sending packets and receiving answers. The function returns
a couple of packet and answers, and the unanswered packets.

sr1() 
-- This function is a variant that only returns one packet that answered the sent
packet (or the packet set) sent.

srp()
-- The function srp() does the same for layer 2 packets (Ethernet, 802.3, etc).
```

## 构造数据包常用参数

* IP()

```
src   e.g. src="192.168.222.222"
dst   e.g. dst="192.168.0.1"
ttl   e.g. ttl=64 
```

* ICMP()

```
type   e.g. type=8(Echo (ping) request)
                 0(Echo (ping) reply)
```

* TCP()

```
sport
dport   e.g. dport=80, [22,23,80]
flags   e.g. flags="S"--SYN
inter
retry
timeout
```

## 0x03 sniff

### params

```
filter
iface       iface="ech0"
prn
```

### demo

```
import scapy_http.http as HTTP
from scapy import *
from scapy.error import

count = 0
def pktTCP(pkt):
    global count
    count += 1
    print count
    if HTTP.HTTPRequest or HTTP.HTTPResponse in pkt:
        src = pkt[IP].src
        srcport = pkt[IP].sport
        dst = pkt[IP].dst
        dport = pkt[IP].dport
        data = pkt[TCP].payload
        if HTTP.HTTPRequest in pkt:
            # do something
            pass
        if HTTP.HTTPResponse in pkt:
            try:
                headers, body = src(data).split("\r\n\r\n", 1)
                print headers
            except Exception as e
                print e

sniff(filter="tcp and port 80", prn=pktTCP, iface='eth0')
```