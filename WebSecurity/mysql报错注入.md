# mysql报错注入

## bool盲注结合报错注入

```
select * from users where 1 and 1
```

这里对于and的前后两个条件来说，如果前面的条件为0，它不会执行后面的条件语句了, 只有前面条件为1，才会继续执行。因此可以利用语句执行的特性，and前面的语句的结果控制后面语句的执行，and前面用盲注，后面用报错注入，使SQL语句执行失败, 也可以使用一个不存在的函数使其报错。

常用报错注入函数

* mysql >= 5.1

```
geometrycollection()
multipoint()
polygon()
multipolygon()
linestring()
multilinestring()
```

* mysql >= 5.7

```
ST_LatFromGeoHash()
ST_LongFromGeoHash()
GTID_SUBSET()
GTID_SUBTRACT()
ST_PointFromGeoHash()
```

参考: [0CTF(TCTF)-2017-final Web LuckyGame Writeup](http://www.bendawang.site/article/0CTF-TCTF-2017-final-Web-LuckyGame-Writeup)