---
title: "流量监听"
date: 2016-06-06 20:21
---

## 0x01 httpry

HTTP包嗅探工具, 捕获HTTP数据包，并且将HTTP协议层的数据内容以可读形式列举出来. 不能监听https流量

### install

[github httpry][1]

```
git clone https://github.com/jbittel/httpry.git
cd httpry
make
sudo make install
```

### 基本用法

```
httpry [ -dFhpqs ] [ -b file ] [ -f format ] [ -i device ] [ -l threshold ]
       [ -m methods ] [ -n count ] [ -o file ] [ -P file ] [ -r file ]
       [ -S bytes ] [ -t seconds ] [ -u user ] [ 'expression' ]

-b file
Write all processed HTTP packets to a binary pcap dump file. Useful for
further analysis of logged data.

-d
Run the program as a daemon process. All program status output will be sent
to syslog. A pid file is created for the process in /var/run/httpry.pid by
default. Requires an output file specified with -o.

-f format
Provide a comma-delimited string specifying the parsed HTTP data to output.
See the doc/format-string file for further information regarding available
options and syntax.

-F
Disable all output buffering. This may be helpful when piping httpry output
into another program.

-h
Display a brief summary of these options.

-i device
Specify an ethernet interface for the program to listen on. If not specified,
the program will poll the system for a list of interfaces and select the
first one found.

-l threshold
Specify a requests per second rate threshold value when running in rate
statistics mode (-s). Only hosts with a rps value greater than or equal to
this number will be displayed. Defaults to 1.

-m methods
Provide a comma-delimited string that specifies the request methods to parse.
The program defaults to parsing all of the standard RFC2616 method strings if
this option is not set. See the doc/method-string file for more information.

-n count
Parse this number of HTTP packets and then exit. Defaults to 0, which means
loop forever.

-o file
Specify an output file for writing parsed packet data.

-p
Do not put the NIC in promiscuous mode on startup. Note that the NIC could
already be in that mode for another reason.

-P file
Specify a path and filename for creating the PID file in daemon mode.

-q
Suppress non-critical output (startup banner, statistics, etc.).

-r file
Provide an input capture file to read from instead of performing
a live capture. This option does not require root privileges.

-s
Run httpry in an HTTP request per second display mode. This periodically
displays the rate per active host and total rate at a specified interval.

-S
Specify a number of bytes to skip in the ethernet header. This allows for
custom header offsets to be accounted for.

-t seconds
Specify the host statistics display interval in seconds when running in
rate statistics mode (-s). Defaults to 5 seconds.

-u user
Specify an alternate user to take ownership of the process and any output
files. You will need root privileges to do this; it will switch to the new
user after initialization.

'expression'
Specify a bpf-style capture filter, overriding the default. Here are a few
basic examples, starting with the default filter:

 'tcp port 80 or 8080'
 'tcp dst port 80'
 'tcp dst port 80 and src host 192.168.1.1'

These filters will capture all web traffic both directions on two common
ports, capture only requests made to port 80, and capture requests to port
80 by a particular host, respectively. See 'man tcpdump' for further
information on the syntax and available primitives.
```

指定监听设备:`sudo httpry -i <device>`， eg.`sudo httpry -i eth0`.

```
# 二进制文件保存
sudo httpry -i eth0 -o output.dump
# 字符文件保存
sudo httpry -i eth0 -o output.txt
# 读文件
httpry -r output.dump

# 指定 http方法
sudo httpry -i eth0 -m get,post
```

[1]: https://github.com/jbittel/httpry