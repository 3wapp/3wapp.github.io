---
title: "Function"
date: 2016-04-22 23:49
---

## file

### is_file

> bool is_file ( string $filename )

判断给定文件名是否为一个正常的文件。

```
参数 

filename: 文件的路径
```

* 测试环境

```
路径
/var/www/
    123/
        test.php
        45/
            robot.txt
```

test.php 

```
// test.php
<?php
$file = $_GET['file'];

if (is_file($file)){
    echo "exist";
}else{
    echo "not exist";
}
?>
```

```
http://localhost/123/test.php?file=test.php --> exitst

/123/test.php --> not exitst
/test.php --> not exitst
./test.php --> exitst
45/../test.php --> exitst
46/../test.php --> not exist
```

从上面结果可以猜测出， is_file 判断文件是否存在时，文件路径为 该php文件的路径 + 带路径的参数$filename，并且当某个目录不存在时，返回false

```
# 跟路径 /var/www/

test.php -> 123/ + test.php = 123/test.php --> exist
/123/test.php -> 123/123/test.php --> not exitst
/test.php 123//test.php --> not exitst
./test.php 123/./test.php --> exitst
45/../test.php -> 123/45/../test.php --> exitst
46/../test.php -> 123/46/../test.php --> not exist
```

当 46 文件夹不存在时, is_file返回的是false, 这个特性可以用作 ** php 文件的过滤绕过 **

另外， is_file存在缓存机制，第一次调用is_file函数的时候，PHP会把文件的属性（file stat）保存下来，当再次调用is_file的时候，如果文件名更第一次的一样，那么就会直接返回缓存，即使文件已经删除了。


## is_numeric  理解 

简单翻看is_numeric实现代码，is_numeric对输入的参数，先做了样式判断如果是整型、浮点型就直接返回true，如果是字符串则进入is_numeric_string函数进行判断
 
```
switch (Z_TYPE_P(arg)) { 
        case IS_LONG: 
        case IS_DOUBLE: 
            RETURN_TRUE; 
            break; 
        case IS_STRING: 
            if (is_numeric_string(Z_STRVAL_P(arg), Z_STRLEN_P(arg), NULL, NULL, 0)) { 
                RETURN_TRUE; 
            } else { 
                RETURN_FALSE; 
            } 
            break; 
        default: 
            RETURN_FALSE; 
            break;
```

经过查找，找到真正的处理函数_is_numeric_string_ex,省略一些代码，我们只用知道哪些字符能够出现在is_numeric的参数中，很明显可以看出， 
空格、\t、\n、\r、\v、\f、+、-能够出现在参数开头，“点”能够在参数任何位置，E、e只能出现在参数中间。 

```
ZEND_API zend_uchar ZEND_FASTCALL _is_numeric_string_ex(......) /* {{{ */ 
{   
    ...... 
    /* Skip any whitespace 
     * This is much faster than the isspace() function */ 
    while (*str == ' ' || *str == '\t' || *str == '\n' || *str == '\r' || *str == '\v' || *str == '\f') { 
        str++; 
        length--; 
    } 
    ptr = str; 
    if (*ptr == '-') { 
        neg = 1; 
        ptr++; 
    } else if (*ptr == '+') { 
        ptr++; 
    } 
    if (ZEND_IS_DIGIT(*ptr)) { 
        /* Skip any leading 0s */ 
        while (*ptr == '0') { 
            ptr++; 
        } 
.... 
        for (type = IS_LONG; !(digits >= MAX_LENGTH_OF_LONG && (dval || allow_errors == 1)); digits++, ptr++) { 
check_digits: 
            if (ZEND_IS_DIGIT(*ptr)) { 
                tmp_lval = tmp_lval * 10 + (*ptr) - '0'; 
                continue; 
            } else if (*ptr == '.' && dp_or_e < 1) { 
                goto process_double; 
            } else if ((*ptr == 'e' || *ptr == 'E') && dp_or_e < 2) { 
                const char *e = ptr + 1; 
                if (*e == '-' || *e == '+') { 
                    ptr = e++; 
                } 
                if (ZEND_IS_DIGIT(*e)) { 
                    goto process_double; 
                } 
            } 
            break; 
        } 
...... 
    } 
}
```

## php字符过滤


* htmlspecialchars

> 将与、单双引号、大于和小于号化成HTML格式

```
&   转成 
"   转成 
'   转成 
<   转成 
```

* htmlentities()

> 所有字符都转成HTML格式, 除上面htmlspecialchars字符外，还包括双字节字符显示成编码等。

* addslashes

> 单双引号、反斜线及NULL加上反斜线转义

被改的字符包括单引号(')、双引号(")、反斜线backslash (\) 以及空字符NULL。

* stripslashes

> 去掉反斜线字符

去掉字符串中的反斜线字符。若是连续二个反斜线，则去掉一个，留下一个。若只有一个反斜线，就直接去掉。
 
* quotemeta

> 加入引用符号

将字符串中含有. \\ + * ? [ ^ ] ( $ ) 等字符的前面加入反斜线"\" 符号。

* strip_tags

> 去掉HTML及PHP标记

去掉字符串中任何HTML标记和PHP标记，包括标记封堵之间的内容。注意如果字符串HTML及PHP标签存在错误，也会返回错误。

* mysql_real_escape_string

> 转义SQL字符串中的特殊字符

转义\x00 \n \r 空格 \ ' " \x1a，针对多字节字符处理很有效。mysql_real_escape_string会判断字符集，mysql_escape_string则不用考虑。
