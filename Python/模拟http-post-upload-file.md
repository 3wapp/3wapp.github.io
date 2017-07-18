---
title: "模拟HTTP POST upload file"
date: 2016-02-26 14:21
---

目前仅测试php解析的服务端

> PHP: 要确保上传表单的属性是 enctype=”multipart/form-data，必须用POST


## socket

```python
import socket

boundary = '---------------------------11008921013555437861019615112'
file_content = "hello"
host = '127.0.0.1'
port = 80
file_name = 'file.txt'
file_type = 'text/plain'

req_data = '--{b}\r\n'.format(b=boundary)
req_data += 'Content-Disposition: form-data; name="file"; filename={fn}\r\n'.format(fn=file_name)
req_data += 'Content-Type: {ft}\r\n'.format(ft=file_type)
req_data += '\r\n'
req_data += '{file_content}\r\n'.format(file_content=file_content)
req_data += '--{b}--'.format(b=boundary)

req = 'POST /upload.php HTTP/1.1\r\n'
req += 'Host: {host}\r\n'.format(host=host)
req += 'Content-Type: multipart/form-data; boundary={b}\r\n'.format(b=boundary)
req += 'Content-Length: {l}\r\n'.format(l=len(req_data))
req += 'Connection: close\r\n'
req += '\r\n'
req += '{data}'.format(data=req_data)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))
s.sendall(req)

data = ""
while True:
    rcv_data = s.recv(4096)

    data += rcv_data
    if rcv_data == "":
        break

    # detect the final chunk
    if rcv_data.endswith("0\r\n\r\n"):
        break

s.close()
```

## urllib

```python
import urllib2

boundary = '%s' % hex(int(time.time() * 1))
fr=open(r'/var/qr/b.png','rb')
file_name = 'file.txt'
file_type = 'text/plain'
data = []

data.append('--%s' % boundary)

data.append('Content-Disposition: form-data; name="file"; filename="%s"' % file_name)
data.append('Content-Type: %s' % file_type)
data.append('--%s--' % boundary)

data.append(fr.read())
fr.close()


http_url='http://127.0.0.1/upload.php'
http_body='\r\n'.join(data)
try:
    #buld http request
    req=urllib2.Request(http_url, data=http_body)
    
    #header
    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
    req.add_header('Host', '127.0.0.1')
    
    #post data to server
    resp = urllib2.urlopen(req, timeout=5)
    
    #get response
    qrcont=resp.read()
    
    print qrcont
    
except Exception as e:
    print '{e}'.format(e=e)
```

## requests

```python
import requests
host = '127.0.0.1'
url = 'http://{ip}/upload.php'.format(ip=host)
file_ = '/var/www/file.txt'

response = requests.post(url, files={"name": open(file_, 'rb')})

print(response.text)
```