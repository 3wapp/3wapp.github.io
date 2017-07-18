---
title: "XPATH"
date: 2016-05-09 20:24
---

## 简介

xpath, 选择XML文件中节点的方法， 节点是XML文件最小构成单位，分为7种

```
element   （元素节点）
attribute （属性节点）
text      （文本节点）
namespace （名称空间节点）
processing-instruction （处理命令节点）
comment   （注释节点）
root      （根节点）
```

[firefox 插件, 在线编辑展示xpath][1]

## 路径表达式 path expression

xpath通过"路径表达式"（Path Expression）来选择节点

```
斜杠（/）作为路径内部的分割符。

绝对路径（absolute path） 必须用"/"起首，后面紧跟根节点，比如/step/step/...

相对路径（relative path）则是除了绝对路径以外的其他写法，比如 step/step，也就是不使用"/"起首。

"."表示当前节点。

".."表示当前节点的父节点
```

## 选择节点的基本规则

```
- nodename（节点名称）：表示选择该节点的所有子节点

- "/"：表示选择根节点

- "//"：表示选择任意位置的某个节点

- "@"： 表示选择某个属性
```

* XML实例

```
<?xml version="1.0" encoding="ISO-8859-1"?>
<bookstore>
  <book>
    <title lang="eng">Harry Potter</title>
    <price>29.99</price>
  </book>
  <book>
    <title lang="eng">Learning XML</title>
    <price>39.95</price>
  </book>
</bookstore>
```

* e.g.

```
bookstore ：选取 bookstore 元素的所有子节点。

/bookstore ：选取根节点bookstore，这是绝对路径写法。

bookstore/book ：选取所有属于 bookstore 的子元素的 book元素，这是相对路径写法。

//book ：选择所有 book 子元素，而不管它们在文档中的位置。

bookstore//book ：选择所有属于 bookstore 元素的后代的 book 元素，而不管它们位于 bookstore 之下的什么位置。

//@lang ：选取所有名为 lang 的属性
```

## 通配符

```
# "*" 表示匹配任何元素节点。
# "@*" 表示匹配任何属性值。
# node() 表示匹配任何类型的节点
```

* e.g.

```
//* ：选择文档中的所有元素节点。

/*/* ：表示选择所有第二层的元素节点

//title[@*] ：表示选择所有带有属性的title元素
```

## xpath的谓语条件（Predicate）

所谓"谓语条件"，就是对路径表达式的附加条件

所有的条件，都写在方括号"[]"中，表示对节点进行进一步的筛选。

```
/bookstore/book[1] ：表示选择bookstore的第一个book子元素。

/bookstore/book[last()] ：表示选择bookstore的最后一个book子元素。

/bookstore/book[last()-1] ：表示选择bookstore的倒数第二个book子元素。

/bookstore/book[position()<3] ：表示选择bookstore的前两个book子元素。

//title[@lang] ：表示选择所有具有lang属性的title节点。

//title[@lang='eng'] ：表示选择所有lang属性的值等于"eng"的title节点。

/bookstore/book[price] ：表示选择bookstore的book子元素，且被选中的book元素必须带有price子元素。

/bookstore/book[price>35.00] ：表示选择bookstore的book子元素，且被选中的book元素的price子元素值必须大于35。

/bookstore/book[price>35.00]/title ：表示在例14结果集中，选择title子元素。

/bookstore/book/price[.>35.00] ：表示选择值大于35的"/bookstore/book"的price子元素
```

## 选择多个路径

用"|"选择多个并列的路径。

```
//book/title | //book/price ：表示同时选择book元素的title子元素和price子元素
```

## XPath 轴（Axes）

轴可定义相对于当前节点的节点集。

```
ancestor	选取当前节点的所有先辈（父、祖父等）。
ancestor-or-self	选取当前节点的所有先辈（父、祖父等）以及当前节点本身。
attribute	选取当前节点的所有属性。
child	    选取当前节点的所有子元素。
descendant	选取当前节点的所有后代元素（子、孙等）。
descendant-or-self	选取当前节点的所有后代元素（子、孙等）以及当前节点本身。
following	选取文档中当前节点的结束标签之后的所有节点。
namespace	选取当前节点的所有命名空间节点。
parent	    选取当前节点的父节点。
preceding	选取文档中当前节点的开始标签之前的所有节点。
preceding-sibling	选取当前节点之前的所有同级节点。
self	    选取当前节点。
```

* e.g.

```
child::*  选取当前节点的所有子元素。
attribute::*  选取当前节点的所有属性。
child::text()  选取当前节点的所有文本子节点。
child::node()  选取当前节点的所有子节点。
```

## 运算符	

```
|	计算两个节点集	   //book | //cd --> 返回所有拥有 book 和 cd 元素的节点集
+	加法	6 + 4 --> 10
-	减法	6 - 4 --> 2
*	乘法	6 * 4 --> 24
div	除法	8 div 4 -->	2
mod	计算除法的余数	5 mod 2 -->	1

=	等于	price=9.80 --> 如果 price 是 9.80，则返回 true, 否则false
!=	不等于	
<	小于	 
<=	小于或等于		
>	大于		
>=	大于或等于		

or	或		
and	与	
not() 逻辑非

:   命名空间分隔符，将命名空间前缀与元素名或属性名分隔 
```

> = 比较是弱类型比较， 1 = ”1“ --> true

## function

[XPATH function document][3]

常用函数：

```
<bookstore>
    <book>
        <title lang="eng">Harry Potter</title>
        <price>29.99</price>
    </book>

    <book>
        <title lang="eng">Learn XML</title>
        <price>39.95</price>
    </book>

    <test>
      <item>Apple</item>
      <item>Banana</item>
      <item>Orange</item>
    </test>
</bookstore>

name([node-set])  返回节点的名字(string)

count(node-set)  返回参数node-set中的节点个数
    count(//test/child::node())，将会返回和test处于兄弟节点的全部子节点的总数 --> 7

string([object])  返回对象转换的字符串
    string(1) --> "1"
    string(//test/item) --> "Apple"
    string(//test) --> 43字符的字符串 ...

string-length(string)  取字符串的长度，如果参数被省略则计算上下文节点的string-value值的长度
    string-length(//book[position()=1]/title)，将会返回user的第一个节点包含的一个字符串的长度 --> 12

substring(string, start [,length])  取子字符串，注意字符串的位置从1开始
    substring((//book[position()=1]/title), 1, 1)，将会返回book的第一个节点（title）的第1个字母 --> H

translate(string, string, string) 返回第一个字符串， 第一个字符串中出现第二个参数字符串中的字符的位置，替换为第三个参数字符串中对应位置的字符
    translate("bar", "abc", "ABC") --> BAr
     
concat(string, string [, string]*)  返回参数的串联， 如果参数不是字符串类型，将先使用string()函数转换为字符串，然后计算转换的结果
    concat("ab", 3, "ef", "g") --> "ab3efg"
    
contains(string1, string2)  返回 true, 当第一个参数字符串包含第二个参数字符串， 否则返回 false
    contains(//test, "Banana") --> true
```

[1]: https://addons.mozilla.org/en-US/firefox/addon/xpath-checker/

[3]: https://developer.mozilla.org/en-US/docs/Web/XPath/Functions