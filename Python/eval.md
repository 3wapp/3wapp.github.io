---
title: "动态执行字符串代码"
date: 2016-06-26 10:19
---

## 0x01 exec

`exec_stmt ::=  "exec" or_expr ["in" expression ["," expression]]`

注意：exec 是一个语法声明，不是一个函数.也就是说和if,for一样. 官方文档对于exec的解释

> This statement supports dynamic execution of Python code.

exec的第一个表达式可以是：

* 代码字符串
* 文件对象
* 代码对象
* tuple

前面三种情况差不多，第四种比较特殊

如果忽略后面的可选表达式,exec后面代码将在当前域执行

```
>>> a=2
>>> exec "a=1"
>>> a
1
>>>
```
 
如果在表达式之后使用in选项指定一个dic，它将作为global和local变量作用域

```
>>> a=10
>>> b=20
>>> g={'a':6,'b':8}
>>> exec "global a;print a,b" in g
6 8
>>>
```

如果in后详指定两个表达式，它们将分别用作global和local变量作用域

```
>>> a=10
>>> b=20
>>> c=20
>>> g={'a':6,'b':8}
>>> l={'b':9,'c':10}
>>> exec "global a;print a,b,c" in g,l
6 9 10
>>>
```

### tuple

如果第一个表达式是tuple

```
exec(expr, globals) #它等效与  exec expr in globals
exec(expr, globals, locals) #它等效与  exec expr in globals,locals
```

## 0x02 eval

eval通常用来执行一个字符串表达式，并返回表达式的值。

`eval(expression[, globals[, locals]])` 有三个参数，表达式字符串，globals变量作用域，locals变量作用域。 其中第二个和第三个参数是可选的。

如果忽略后面两个参数，则eval在当前作用域执行。

```
>>> a=1
>>> eval("a+1")
2
>>>
```

如果指定globals参数

```
>>> a=1
>>> g={'a':10}
>>> eval("a+1",g)
11
>>>
```

如果指定locals参数

```
>>> a=10
>>> b=20
>>> c=20
>>> g={'a':6,'b':8}
>>> l={'b':9,'c':10}
>>> eval("a+b+c",g,l)
25
>>>
```

如果要严格限制 eval 执行，可以设置globals为__builtins__,这样 这个表达式只可以访问 `__builtin__ module`

