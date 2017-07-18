---
title: "Pythonic"
date: 2016-06-08 12:45
---

[PythonSpeedPerformanceTips][1]

## 0x01 字符串

### 列表转字符串

避免使用如下方式

```python
s = ""
for substring in list:
    s += substring
```
尽量使用 `s = "".join(list)` 这种方式

### 格式化字符串

避免使用 `out = "<html>" + head + prologue + query + tail + "</html>"`    
应该使用 `out = "<html>%s%s%s%s</html>" % (head, prologue, query, tail)`    
或者可读性更好的方式 `out = "<html>%(head)s%(prologue)s%(query)s%(tail)s</html>" % locals()`

## 0x02 字典

### 减少循环中 if 判断

使用字典做词频统计

```
wdict = {}
for word in words:
    if word not in wdict:
        wdict[word] = 0
    wdict[word] += 1
```

使用 `try` 替代 `if` 判断

```
wdict = {}
for word in words:
    try:
        wdict[word] += 1
    except KeyError:
        wdict[word] = 1
```     

使用 get 方式

```
wdict = {}
get = wdict.get
for word in words:
    wdict[word] = get(word, 0) + 1
```

使用 defaultdict

```
from collections import defaultdict

wdict = defaultdict(int)

for word in words:
    wdict[word] += 1
```

## 0x03 循环

避免使用

```
newlist = []
for word in oldlist:
    newlist.append(word.upper())
```

map 方式：  `newlist = map(str.upper, oldlist)`    
列表生成器： `newlist = [s.upper() for s in oldlist]`    
迭代器：    `iterator = (s.upper() for s in oldlist)`

不能使用以上方式的情况下，避免`点号`， 减少循环中函数引用带来的开销，但这也会降低程序的可读性

```
upper = str.upper
newlist = []
append = newlist.append
for word in oldlist:
    append(upper(word))
```

尽可能使用 `local variable`, 而不是 `global variable`

```
def func():
    upper = str.upper
    newlist = []
    append = newlist.append
    for word in oldlist:
        append(upper(word))
    return newlist
```



### 集合 A，B 交集判断

```
any(_ in A for _ in B)  => True(have) or False(no)
```

### hashlib

```
import hashlib

clipher = hashlib.new("md5", "plain").hexdigest()
```


[1]: https://wiki.python.org/moin/PythonSpeed/PerformanceTips