---
title: "Socket"
date: 2016-01-20 05:30
---

## recv

recv函数默认是阻塞的， 也就是说recv会阻塞程序运行，直到它获取到数据，否则它将永远等待，除非服务器断开连接。

* 解决阻塞问题方法1： `socket.settimeout`

```
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# accept can throw socket.timeout
sock.settimeout(5.0)
conn, addr = sock.accept()

# recv can throw socket.timeout
conn.settimeout(5.0)
conn.recv(1024)
```

* 方法2： `select`

```
import select

sock.setblocking(0)

ready = select.select([sock], [], [], timeout_in_seconds)
if ready[0]:
    data = mysocket.recv(1024)
```

* 方法3： `socket.setblocking(0)`

> s.setblocking(0) is equivalent to s.settimeout(0.0)

```
sock.setblocking(0)
sock.recv(1024)
```

* 方法4： `fcntl`

```
import sys
import socket
import fcntl, os
import errno
from time import sleep

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1',9999))
fcntl.fcntl(sock, fcntl.F_SETFL, os.O_NONBLOCK)

while True:
    try:
        msg = s.recv(4096)
    except socket.error as e:
        err = e.args[0]
        if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
            sleep(1)
            print 'No data available'
            continue
        else:
            # a "real" error occurred
            print e
            sys.exit(1)
    else:
        # got a message, do something :)
```

## socket 监听 TCP 端口，获取 password 数据

```python
import socket
import re

host = '0.0.0.0'
port = 8000 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #listen TCP port
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
sock.bind((host, port))  
sock.listen(1)  #start listen

while 1:
    conn, addr = sock.accept()
    print("connected by:{}".format(addr))
    data=conn.recv(1024)  

    pattern = r"password.+?\b"
    pattern = re.compile(pattern)
    match = pattern.findall(data)
    if match:
        for m in match:
            print(m)
    else:
        print('no password match')
```

访问
```
http://127.0.0.1/index.html?password=1000
```

结果
```
connected by:('127.0.0.1', 53678)
password=1000 
```