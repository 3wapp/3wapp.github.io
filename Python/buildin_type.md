---
title: "常用内置对象操作"
date: 2016-01-28 11:18
---

## 0x01 string

### 编码

```
# unicode
chinese = '\u4e2d\u6587'
>>> print chinese.decode('unicode-escape')
中文
```

### 基本操作

```python
>>> "a" + "b"
'ab'
>>> "a" * 3
'aaa'
>>> ",".join(["a", "b", "c"])           # 合并多个字符串
'a,b,c'
>>> "a,b,c".split(",")                  # 按指定字符分割
['a', 'b', 'c']
>>> "a\nb\r\nc".splitlines()            # 按行分割
['a', 'b', 'c']
>>> "a\nb\r\nc".splitlines(True)        # 分割后,保留换行行符。
['a\n', 'b\r\n', 'c']
>>> "abc".startswith("ab"), "abc".endswith("bc")!       # 判断是否以特定子子串开始或结束。
True, True
>>> "abc".upper(), "Abc".lower()        # 大大小小写转换。
'ABC', 'abc'
>>> "abcabc".find("bc"), "abcabc".find("bc", 2)         # 可指定查找起始结束位置。
1, 4
>>> " abc".lstrip(), "abc ".rstrip(), " abc ".strip()   # 剔除前后空格。
'abc', 'abc', 'abc'
>>> "abc".strip("ac")                   # 可删除指定的前后缀字符。
'b'
>>> "abcabc".replace("bc", "BC")        # 可指定替换次数。
'aBCaBC'
>>> "a\tbc".expandtabs(4)               # 将 tab 替换成空格。
'a    bc'
>>> "123".ljust(5, '0'), "456".rjust(5, '0'), "abc".center(10, '*')     # 填充
'12300', '00456', '***abc****'
>>> "123".zfill(6), "123456".zfill(4)   # 数字填充
'000123', '123456'
```

### 格式化

Python 提供了两种字符串格式化方方法

1. `%[(key)][flags][width][.precision]typecode`

标记: - 左对齐, + 数字符号, # 进制前缀, 或者用用空格、0 填充。

```python
>>> "%(key)s=%(value)d" % dict(key = "a", value = 10)       # key
'a=10'
>>> "[%-10s]" % "a"         # 左对齐
'[a         ]'
>>> "%+d, %+d" % (-10, 10)  # 数字符号
'-10, +10'
>>> "%010d" % 3             # 填充
'0000000003'
>>> "%.2f" % 0.1234         # 小小数位
'0.12'
>>> "%#x, %#X" % (100, 200) # 十十六进制、前缀、大大小小写
'0x64, 0XC8'
>>> "%s, %r" % (m, m)       # s: str(); r: repr()
'test..., <__main__.M object at 0x103c4aa10>'
```

2. format 方方法支支持更多的数据类型,包括列表、字典、对象成员等

`{field!convertflag:formatspec}`

格式化规范: formatspec: `[[fill]align][sign][#][0][width][.precision][typecode]`

```
>>> "{key}={value}".format(key="a", value=10)   # 使用用命名参数
'a=10'
>>> "{0},{1},{0}".format(1, 2)                  # field 可多次使用用
'1,2,1'
>>> "{0:,}".format(1234567)                     # 千分位符号 
'1,234,567'
>>> "{0:,.2f}".format(12345.6789)               # 千分位,带小小数位。
'12,345.68'
>>> "[{0:<10}], [{0:^10}], [{0:*>10}]".format("a")! # 左中右对齐,可指定填充字符。
'[a       ], [    a     ], [*********a]'
>>> import sys
>>> "{0.platform}".format(sys)          # 成员
'linux2'
>>> "{0[a]}".format(dict(a=10, b=20))   # 字典
'10'
>>> "{0[5]}".format(range(10))          # 列表
'5'
```

另有 string.Template 模板可供使用用。该模块还定义了各种常见的字符序列。

```
>>> from string import letters, digits, Template
>>> letters`        # 字母母表
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> digits          # 数字表
'0123456789'
>>> Template("$name, $age").substitute(name = "User1", age = 20)    # 模板替换。
'User1, 20'
>>> Template("${name}, $age").safe_substitute(name = "User1")       # 没找到值,不会抛出异常。
'User1, $age'
```

## 0x02 字符串数字转换

二进制：    ‘0b’ 开头
八进制：    ‘0o’ 开头
十六进制：  ‘0x’ 开头

* 整数 <==> 字符串

```
# 十六进制
hex()       hex(number) -> string
> hex(10) ==> '0xa'

# 十进制
int()       int(x, base=10) -> int or long
> int('0b100', 0) ==> 4
> int('0b100', 2) ==> 4
> int('0x10', 16) ==> 16
> int('10', 16)   ==> 16

# 二进制
bin()       bin(number) -> string
> bin(4) ==> '0b100'

# 八进制
oct()       oct(number) -> string
> oct(17) ==> '021'

"{0:b}".format(4) ==> '100'
```

* 整数 <==> 字节串

short:2字节， long：4字节

```
import struct

struct.unpack('<HH', bytes(b'\x01\x00\x00\x00')) ==> (1,0)
struct.unpack('<L', bytes(b'\x01\x00\x00\x00'))  ==> (1,)

struct.pack('<HH', 1,2)    ==> '\x01\x00\x02\x00'
struct.pack('<LL', 1,2)    ==> '\x01\x00\x00\x00\x02\x00\x00\x00'
```
* 16进制串 <==> 字符串

```
'abc'.encode('hex')     ==> '616263'
binascii.b2a_hex('abc') ==> '616263'
binascii.hexlify('abc') ==> '616263'

'616263'.decode('hex')      ==> 'abc'
binascii.a2b_hex('616263')  ==> 'abc'
binascii.unhexlify('616263')==> 'abc'
```

* 字符串 <==> 字节串

```

```

* unicode
    
\\u 后面是十六进制的Unicode码

    + prefix u
    
    u‘中文’ ==> u'\u4e2d\u6587'
    
    + unicode 强制转换
    
    要求 python文件中指定了对应的编码类型；并且对应的python文件的确是以该编码方式保存的

```
# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

s = unicode('中文')

>>> u'\u4e2d\u6587'
```

* unicode <==> string

unicode ==> string : encode

string  ==> unicode: decode




## 0x03 编码

Python 2.x 默认采用用 ASCII 编码。为了完成编码转换,必须和操作系统字符编码统一一起来。

```
>>> import sys, locale
>>> sys.getdefaultencoding()            # Python 默认编码。
'ascii'
>>> c = locale.getdefaultlocale(); c    # 获取当前系统编码。
('zh_CN', 'UTF-8')
>>> reload(sys)                         # setdefaultencoding 在被初始化时被 site.py 删掉了。
<module 'sys' (built-in)>
>>> sys.setdefaultencoding(c[1])        # 重新设置默认编码。
```

str、unicode 都提供了 encode 和 decode 编码转换方方法。

* encode: 将默认编码转换为其他编码。
* decode: 将默认或者指定编码字符串转换为 unicode

标准库 codecs 模块用用来处理更复杂的编码转换

### base64

* characters set

```
ABCDEFGHIJKLMNOP
QRSTUVWXYZabcdef
ghijklmnopqrstuv
wxyz0123456789+/
```

## 0x04 list

### 基本操作

```python
>>> []                          # 空列表
>>> ['a', 'b'] * 3   
['a', 'b', 'a', 'b', 'a', 'b']
>>> ['a', 'b'] + ['c', 'd']     # 连接多个列表
['a', 'b', 'c', 'd']
>>> list("abcd")                # 将序列类型或迭代器转换为列表
['a', 'b', 'c', 'd']
>>> [x for x in range(3)]       # 生生成器表达式
[0, 1, 2]

>>>l = list("abcbc")
>>>l[1:-1]                      # 切片
['b', 'c', 'b']
>>> l.count('b')                # 统计元素项
2
>>> l.index('b', 2)             # 从指定位置查找项，返回序号
3
>>> l.append('d')               # 追加元素
>>> l
['a', 'b', 'c', 'b', 'c', 'd']
>>> l.insert(1, 5)              # 指定位置插入元素
>>> l
['a', 5, 'b', 'c', 'b', 'c', 'd']
>>> l.extend(range(2))          # 合并列表
>>> l
['a', 5, 'b', 'c', 'b', 'c', 'd', 0, 1]
>>> l.remove('b')               # 移除第一个指定元素
>>> l
['a', 5, 'c', 'b', 'c', 'd', 0, 1]
>>> l.pop(0)                    # 弹出指定位置的元素(默认最后项)
'a'
>>> l
[5, 'c', 'b', 'c', 'd', 0, 1]
```

### bisect 向有序列表中插入入元素

```
>>> import bisect
>>> l = ["a", "d", "c", "e"]
>>> l.sort()
>>> l
['a', 'c', 'd', 'e']
>>> bisect.insort(l, "b")
>>> l
['a', 'b', 'c', 'd', 'e']
>>> bisect.insort(l, "d")
>>> l
['a', 'b', 'c', 'd', 'd', 'e']
```

### array

某些时候,可以考虑用用数组代替列表。 和列表存储对象指针不同,数组直接内嵌数据,既省了创建
对象的内存开销,又又提升了读写效率。

```
>>> import array
>>> a = array.array("l", range(10))     # 用用其他序列类型初始化数组。
>>> a
array('l', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> a.tolist()                          # 转换为列表。
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a = array.array("c")                # 创建特定类型数组。
>>> a.fromstring("abc")                 # 从字符串添加元素。
>>> a
array('c', 'abc')
>>> a.fromlist(list("def"))             # 从列表添加元素。
>>> a
array('c', 'abcdef')
>>> a.extend(array.array("c", "xyz"))   # 合并列表或数组。
>>> a
array('c', 'abcdefxyz')
```

## 0x05 tuple

* 只读对象,元组和元素指针数组内存是一一次性连续分配的
* 虚拟机缓存 n 个元素数量小小于 20 的元组复用用对象

在编码中,应该尽可能用用元组代替列表。除内存复用用更高高效外,其只读特征更利于并行行开发

### 基本操作:

```
>>> a = (4)             # 少了逗号,就成了普通的括号运算符了
>>> type(a)
<type 'int'>
>>> a = (4,)            # 这才是元组
>>> type(a)
<type 'tuple'>
>>> s = tuple("abcadef")! ! ! # 将其他序列类型转换成元组。
>>> s
('a', 'b', 'c', 'a', 'd', 'e', 'f')
>>> s.count("a")        # 元素统计。
2
>>> s.index("d")        # 查找元素,返回序号
4
```

### 标准库 namedtuple

可用用名字访问元素项。

```
>>> from collections import namedtuple
>>> User = namedtuple("User", "name age")       # 空格分隔字段名,或使用用迭代器。
>>> u = User("user1", 10)
>>> u.name, u.age
('user1', 10)
```

其实 namedtuple 并不是元组,而而是利用用模板动态创建的自自定义类型

## 0x06 dict

字典 (dict) 采用用开放地址法的哈希表实现

* 自自带元素容量为 8 的 smalltable,只有 "超出" 时才到堆上额外分配元素表内存。
* 虚拟机缓存 80 个字典复用用对象,但在堆上分配的元素表内存会被释放。
* 按需动态调整容量。扩容或收缩操作都将重新分配内存,重新哈希
* 删除元素操作不会立立即收缩内存

### 创建字典

```
>>> {}              # 空字典
>>> {"a":1, "b":2}  # 普通构造方方式
>>> dict(a = 1, b = 2)          # 构造
{'a': 1, 'b': 2}
>>> dict((["a", 1], ["b", 2]))  # 用两个序列类型构造字典
{'a': 1, 'b': 2}
>>> dict(zip("ab", range(2)))   # 同上
{'a': 0, 'b': 1}
>>> dict(map(None, "abc", range(2)))    #同上
{'a': 0, 'c': None, 'b': 1}
>>> dict.fromkeys("abc", 1)     # 用序列作 key， 并提供默认的 value
{'a': 1, 'c': 1, 'b': 1}
>>> {k:v for k, v in zip("abc", range(3))}      # 使用用生生成表达式构造字典。
{'a': 0, 'c': 2, 'b': 1}
```

### 基本操作

```
>>> d = {"a":1, "b":2}
>>> "b" in d            # 判断是否包含 key
True
>>> d = {"a":1, "b":2}  # 删除 k/v
>>> del d["b"]
>>> d
{'a': 1}
>>> d = {"a":1}
>>> d.update({"c": 3})  # 合并
>>> d
{'a': 1, 'c': 3}
>>> d = {"a":1, "b":2}
>>> d.pop("b")          # 弹出
>>> d
(2, {'a': 1})
>>> d = {"a":1, "b":2}
>>> d.popitem()         # 弹出 (key, value)
('a', 1)

# 默认返回值
>>> d = {"a":1, "b":2}
>>> d.get("c")              # 如果没有对应 key, 返回 None
None
>>> d.get("d", 123)         # 如果没有对应 key,返回缺省值。
>>> d.setdefault("a", 100)  # key 存在,直接返回 value。
1
>>> d.setdefault("c", 200)  # key 不存在,先设置,后返回。
200
>>> d
{'a': 1, 'c': 200, 'b': 2}
```

### 迭代器操作

```
>>> d = {"a":1, "b":2}
>>> d.keys()
['a', 'b']
>>> d.values()
[1, 2]
>>> d.items()
[('a', 1), ('b', 2)]
>>> for k in d: print k, d[k]
a 1
b 2
>>> for k, v in d.items(): print k, v
a 1
b 2
```

对于大大字典,调用用 keys()、values()、items() 会构造同样巨大大的列表。建议用用迭代器替代,以减
少内存开销

```
>>> d = {"a":1, "b":2}
>>> d.iterkeys()
<dictionary-keyiterator object at 0x10de82cb0>
>>> d.itervalues()
<dictionary-valueiterator object at 0x10de82d08>
>>> d.iteritems()
<dictionary-itemiterator object at 0x10de82d60>
>>> for k, v in d.iteritems():
...    print k, v
a 1
b 2
```

### 视图

要判断两个字典间的差异,使用用视图是最简便的做法。

```
>>> d1 = dict(a = 1, b = 2)
>>> d2 = dict(b = 2, c = 3)
>>> d1 & d2                 # 字典不支支持该操作。
TypeError: unsupported operand type(s) for &: 'dict' and 'dict'
>>> v1 = d1.viewitems()
>>> v2 = d2.viewitems()
>>> v1 & v2                 # 交集
set([('b', 2)]) 
>>> v1 | v2                 # 并集
set([('a', 1), ('b', 2), ('c', 3)])
>>> v1 - v2                 # 差集 (仅 v1 有,v2 没有的)
set([('a', 1)])
>>> v1 ^ v2                 # 对称差集 (不会同时出现在 v1 和 v2 中)
set([('a', 1), ('c', 3)])
>>> ('a', 1) in v1          # 判断
True

# 更新字典内容
>>> a = dict(x=1)
>>> b = dict(x=10, y=20)
39>>> a.update({k:b[k] for k in a.viewkeys() & b.viewkeys()})
>>> a
{'x': 10}
```

视图会和字典同步变更

```
>>> d = {"a": 1}
>>> v = d.viewitems()
>>> v
dict_items([('a', 1)])
>>> d["b"] = 2
>>> v
dict_items([('a', 1), ('b', 2)])
>>> del d["a"]
>>> v
dict_items([('b', 2)])
```

### 扩展

当访问的 key 不存在时, defaultdict 自自动调用用 factory 对象创建所需键值对。factory 可以是任何无无参数函数或 callable 对象

```
>>> from collections import defaultdict
>>> d = defaultdict(list)       # key "a" 不存在,直接用用 list() 函数创建一一个空列表作为 value。
>>> d["a"].append(1)

>>> d["a"].append(2)
>>> d["a"]
[1, 2]
```

字典是哈希表,默认迭代是无无序的。如果希望按照元素添加顺序输出结果,可以用用 OrderedDict。

```
>>> from collections import OrderedDict
>>> d = dict()
>>> d["a"] = 1
>>> d["b"] = 2
>>> d["c"] = 3
>>> for k, v in d.items(): print k, v           # 并非非按添加顺序输出。
a 1
c 3
b 2
>>> od = OrderedDict()
>>> od["a"] = 1
>>> od["b"] = 2
>>> od["c"] = 3
>>> for k, v in od.items(): print k, v          # 按添加顺序输出。
a 1
b 2
c 3
>>> od.popitem()                                # 按 LIFO 顺序弹出。
('c', 3)
>>> od.popitem()
('b', 2)
>>> od.popitem()
('a', 1)
```

## 0x07 set

集合 (set) 用用来存储无无序不重复对象。所谓不重复对象,除了不是同一一对象外,还包括 "值" 不能相同。集合只能存储可哈希对象,一一样有只读版本 frozenset。

判重公式: `(a is b) or (hash(a) == hash(b) and eq(a, b))`

在内部实现上,集合和字典非非常相似,除了 Entry 没有 value 字段。集合不是序列类型,不能像列表那样按序号访问,也不能做切片片操作

```
>>> s = set("abc")              # 通过序列类型初始化。
set(['a', 'c', 'b'])
>>> {v for v in "abc"}          # 通过构造表达式创建
set(['a', 'c', 'b'])
>>> "b" in s                    # 判断元素是否在集合中
True
>>> s.add("d")                  # 添加元素
>>> s
set(['a', 'c', 'b', 'd'])
>>> s.remove("b")               # 移除元素
>>> s
set(['a', 'c', 'd'])
>>> s.discard("a")              # 如果存在,就移除
>>> s
set(['c', 'd'])
>>> s.update(set("abcd"))       # 合并集合
>>> s
set(['a', 'c', 'b', 'd'])
>>> s.pop()                     # 弹出元素
'a'
>>> s
set(['c', 'b', 'd'])
```

### 集合运算

```
>>> "c" in set("abcd")          # 判断集合中是否有特定元素
>>> set("abc") is set("abc")
False
>>> set("abc") == set("abc")    # 相等判断
True
>>> set("abc") != set("abc")    # 不等判断
False
>>> set("abcd") >= set("ab")    # 超集判断 (issuperset)
True
>>> set("bc") < set("abcd")     # 子集判断 (issubset)
True
>>> set("abcd") | set("cdef")   # 并集 (union)
set(['a', 'c', 'b', 'e', 'd', 'f'])
>>> set("abcd") & set("abx")    # 交集 (intersection)
set(['a', 'b'])
>>> set("abcd") - set("ab")     # 差集 (difference), 仅左边有,右边没有的
set(['c', 'd'])
>>> set("abx") ^ set("aby")     # 对称差集 (symmetric_difference)
set(['y', 'x'])                 # 不会同时出现在两个集合当中的元素
>>> set("abcd").isdisjoint("ab")    # 判断是否没有交集
False
```

### 更新操作

```
>>> s = set("abcd")
>>> s |= set("cdef")        # 并集 (update)
>>> s
set(['a', 'c', 'b', 'e', 'd', 'f'])
>>> s = set("abcd")
>>> s &= set("cdef")        # 交集 (intersection_update)
>>> s
set(['c', 'd'])
>>> s = set("abx")
>>> s -= set("abcdy")       # 差集 (difference_update)
>>> s
set(['x'])
>>> s = set("abx")
>>> s ^= set("aby")         # 对称差集 (symmetric_difference_update)
>>> s
set(['y', 'x'])
```

集合和字典主键都必须是可哈希类型对象,但常用用的 list、dict、set、defaultdict、OrderedDict 都是不可哈希的,仅有 tuple、frozenset 可用用

```
>>> hash([])
TypeError: unhashable type: 'list'
>>> hash({})
TypeError: unhashable type: 'dict'
>>> hash(set())
TypeError: unhashable type: 'set'
>>> hash(tuple()), hash(frozenset())
(3527539, 133156838395276)
```

如果想把自自定义类型放入入集合,需要保证 hash 和 equal 的结果都相同才能去重

```
>>> class User(object):
...     def __init__(self, name):
...         self.name = name
>>> hash(User("tom"))           # 每次的哈希结果都不同
279218517
>>> hash(User("tom"))
279218521
>>> class User(object):
...    def __init__(self, name):
...        self.name = name
...    def __hash__(self):
...        return hash(self.name)
...    def __eq__(self, o):
...        if not o or not isinstance(o, User): return False
...        return self.name == o.name
>>> s = set()
>>> s.add(User("tom"))
>>> s.add(User("tom"))
>>> s
set([<__main__.User object at 0x10a48d150>])
```
