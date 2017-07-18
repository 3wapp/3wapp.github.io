# PHP 代码审计

## 工具

### 静态代码审计

* [RISP]()

## 基础函数

* get_defined_vars(void)

此函数返回一个包含当前可用的变量列表的多维数组，这些变量包括环境变量、服务器变量和用户定义的变量.在函数中使用此函数可以调试函数中的变量，而不会返回其他的变量

* get_defined_functions(void)

获取所有已经定义的函数,包含内部函数和用户定义的函数。

```php
# 输出用户定义的函数方法为：
$funcs = get_defined_functions();
var_dump($funcs['user']);
```

* get_defined_constants(void)

返回所有可用的常量，包含系统常量和用户定义的常量

* get_declared_classes(void)

返回所有可用的类，包含系统类和用户定义的类。

* get_included_files()

返回所有的包含的文件路径的数组，included 和 required 的包含文件

## 弱类型比较

### 类型转换


* int vs string

```
>>> 0 == "abc"
=> true
>>> 0 == "1abc"
=> false
>>> 0 == "0abc"
=> true
```

* int vs float

```
>>> 1.000000000000001 == 1
=> false
>>> 1.0000000000000001 == 1
=> true
```

### 字符串比较

* `\d+0e\d+`

比较运算时, 遇到 `\d+e\d+` 类型字符串会将其解析为科学计数法

```php
>>> "0e1234" == "0e7654321"
=> true
>>> "0e1234" == "0e1234abc"
=> false
>>> "0e1234" == "0"
=> true
>>> "0e1234" == "0e"
=> false
>>> "0e1234" == "0e1"
=> true

# md5
>>> md5('240610708')
=> "0e462097431906509019562988736854"
>>> md5('QNKCDZO')
=> "0e830400451993494058024219903391"
>>> md5('240610708') == md5('QNKCDZO')
=> true

>>> "1e2" == "100"
=> true
```

* 0x

比较运算时, 字符串以 `0x` 开头, php会尝试将字符串转换为十进制然后再比较

```
>>> "0xf" == "15"
=> true
>>> "0xf" == 0xf
=> true
>>> "0xf" == 15
=> true
```

## 类型转换

### intval

intval()转换的时候，会将从字符串的开始处进行转换，直到遇到一个非数字的字符。即使出现无法转换的字符串，intval()不会报错而是返回0

```
>>> intval("3")
=> 3
>>> intval("3abc")
=> 3
>>> intval("abc")
=> 0
```

## 内置函数参数的松散性

### md5

> string md5 ( string $str [, bool $raw_output = false ] )

md5 需要是一个string类型的参数， 你传递一个array时，md5()不会报错，只是会无法正确地求出 array 的md5值， 导致任意2个array的md5值都会相等。

### strcmp

strcmp函数比较字符串的本质是将两个变量转换为ascii，然后进行减法运算，然后根据运算结果来决定返回值。

### in_array

> bool in_array ( mixed $needle , array $haystack [, bool $strict = FALSE ] )

如果strict参数没有提供，那么in_array就会使用`松散比较`来判断$needle是否在$haystack中。当strince的值为true时，in_array()会比较`needls的类型`和`haystack中的类型`是否相同。

```
>>> $arr = [0, 1, 2, '3']
=> [
     0,
     1,
     2,
     "3",
   ]
>>> in_array('abc', $arr)       # 'abc' 转换为 0
=> true
>>> in_array('1abc', $arr)      # '1abc' 转换为 1
=> true
```

seem to `array_search()`

## 序列化

### unserialize

unserialize 函数反序列化不成功会返回`false`, 函数会从第一个字符开始解析，解析完`完整的反序列化字符串`就会返回，而不再解析之后的可能存在的字符串，如下所示：

```php
$tmp = 's:3:"123";';
var_dump(unserialize($tmp));
=>string '123' (length=3)

$tmp = 's:3:"123";s:2:"34";';
=>string '123' (length=3)

$tmp = 's:3:"123";xxx';
=>string '123' (length=3)

$tmp = ' s:3:"123";';
=>boolean false
```

## 变量覆盖

很多应用会有这个逻辑，就是在全局覆盖变量前，检查`$_REQUEST`变量，如果`$_REQUEST`中含有一些不允许覆盖的变量时就报错；如果不含有非法变量，再依次将`$_GET` `$_POST` `$_COOKIE`三者覆盖到全局变量。

这在php5.3以前都是比较安全的，但php5.3以后** `$_REQUEST`变量中不再包含`$_COOKIE` ** ，所以第一步检查的时候也就不会检查`$_COOKIE`中的变量，但第二步又是包含了`$_COOKIE`的。这种情景不光在变量覆盖中存在，比如一些WAF也可能会因为php5.3而漏掉检查`$_COOKIE`。

php 5.3以后`$_REQUEST`变量中不再包含`$_COOKIE`, 这是php5.3.0以后`$_REQUEST`是受php.ini中的`request_order`影响的，关于 `request_order` 这个配置选项，是php的5.3.0版本中新增加的, `request_order`默认值为GP，也就是说默认配置下`$_REQUEST`只包含`$_GET`和`$_POST`而不包括`$_COOKIE`。通过 COOKIE就可以提交GLOBALS变量。

 从而绕过了大多开源程序中的全局变量防御。因此要将次选项更改为 `request_order = "CGP"`

* [2015通达oa-从前台注入到后台getshell](http://www.cnblogs.com/iamstudy/articles/tongdaoa_2015_sql_getshell.html)
