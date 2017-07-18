---
title: "W3af"
date: 2016-05-24 09:49
---

## 0x00 简介

[w3af document][1]

[w3af plugins][2]

## 0x01 plugins

```
# 查看 sqli 的详细信息
w3af/plugins>>>audit desc sqli

# 查看配置
w3af/plugins>>>audit config xss
w3af/plugins/config:xss>>>view 
```

### plugin type

main plugins type: `crawl`(漏洞挖掘), `audit`(漏洞分析) and `attack`(漏洞攻击)

### output

## 0x02 http-settings

* headers_file

w3af 从文件中解析 header, 不过会修改 User-agent 为 w3af 设置的值, 如下所示

```
path: w3af/core/data/url/opener_settings.py

def set_headers_file(self, headers_file):
    ...
    f = open(headers_file, 'r')      # support ralative path and absolute path ================
    ...
    for line in f:
        header_name = line.split(':')[0]
        header_value = ':'.join(line.split(':')[1:])    # line without ":" will raise error ===
        header_value = header_value.strip()
        header_list.append((header_name, header_value))
    ...

def set_user_agent(self, user_agent):
        self.header_list = [i for i in self.header_list if i[0].lower()
                            != USER_AGENT_HEADER]
        self.header_list.append((USER_AGENT_HEADER, user_agent))
        cfg.save('user_agent', user_agent)
```

从源码分析可知， headers_file 文件中设置的 user-agent 并不会生效，`set user_agent x` 才是有效的; 读 headers_file 文件支持相对路径和绝对路径; 文件中每行必须用 `":"` 分隔 `key: value`, 并且文件中不能出现空行， 否则导致解析出错， console 报错如下：

```
The following error was detected and could not be resolved:
The remote web server is not answering our HTTP requests, multiple errors have been found while trying to GET a response from the server.
```

### proxy_address

通过 `set proxy_address 127.0.0.1`, 可以使用 burpsuite 等代理软件监听 w3af 请求 

## 0x03 profiles



[1]: http://docs.w3af.org/en/latest/
[2]: http://w3af.org/plugins