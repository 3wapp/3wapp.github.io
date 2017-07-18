# requests

## requests proxy

* socks proxy

install: `pip install -U requests[socks]`

usage:

```python
import requests

resp = requests.get('http://go.to',
                    proxies=dict(http='socks5://user:pass@host:port',
                                 https='socks5://user:pass@host:port'))

resp = requests.get('http://go.to',
                    proxies=dict(http='socks4://user:pass@host:port',
                                 https='socks4://user:pass@host:port'))
```

### `requests proxy` vs `pysocks proxy`

[pysocks](https://github.com/Anorov/PySocks)

* http proxy

pysocks 进行 http 代理时， 使用的是 HTTP CONNECT 方式， 对于不支持 `CONNECT` 方式的代理服务器，比如BurpSuite, 就无效

requests 进行 http 代理，不使用 HTTP CONNECT 方式， 兼容性更好

## error

* 常见报错解析

```
[Errno 8] Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known',))
[Errno -5] No address associated with hostname
[Errno -2] Name or service not known
-- DNS lookup of the host name you're trying to access failed
```

### 自动跳转

通过配置`allow_redirects`参数，可以设置requests自动跳转，默认允许

* 禁止自动跳转

`requests.get(url, allow_redirects=False)`

### 手动添加cookie

通过requests.utils.add_dict_to_cookiejar对session对象设置cookie，之后所有的请求都会自动加上自定义的cookie内容。

也可以通过requests.utils.cookiejar_from_dict 生成一个cookiejar对象，再赋值给session.cookies。

```python
import requests
import time

mycookie = { "PHPSESSID":"56v9clgo1kdfo3q5q8ck0aaaaa" }
s = requests.session()
requests.utils.add_dict_to_cookiejar(x.cookies,{"PHPSESSID":"07et4ol1g7ttb0bnjmbiqjhp43"})
s.get("http://127.0.0.1:80",cookies = mycookie)
time.sleep(5)
s.get("http://127.0.0.1:80")
```
