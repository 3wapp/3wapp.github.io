## 更改pypi国内源

`vi ~/.pip/pip.conf`

```
[global]
timeout =6000
index-url = http://pypi.douban.com/simple/

[install]
use-mirrors =true
mirrors = http://pypi.douban.com/simple/
trusted-host =pypi.douban.com
```

```
[global]
timeout =6000
index-url = http://mirrors.aliyun.com/pypi/simple

[install]
use-mirrors =true
mirrors = http://mirrors.aliyun.com/pypi/simple/
trusted-host = mirrors.aliyun.com
```
