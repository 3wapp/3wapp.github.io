# MAC搭建PHP调试环境

> mac 不推荐使用这种方式，更好的是使用docker的方式来搭建调试环境。

使用Docker搭建php调试环境，支持gdb, xdebug, vld等工具调试php。



## 源码安装

### 获取源码

```
git clone https://github.com/php/php-src.git
cd php-src
```

切换到想构建的分支:

* PHP 5.3: git checkout PHP-5.3
* PHP 5.4: git checkout PHP-5.4
* PHP 5.5: git checkout PHP-5.5
* PHP 5.6: git checkout PHP-5.6
* PHP 7.0: git checkout PHP-7.0
* PHP HEAD: git checkout master

```
# 生成编译所需的 configure 文件
./buildconf
```

### configure and make

* `./configure --disable-all --enable-debug --prefix=/Users/js/php/usr`

```
1. 
checking for bison version... invalid
configure: WARNING: This bison version is not supported for regeneration of the Zend/PHP parsers

2.
/php-src/Zend/zend_language_parser.y:50.1-5: invalid directive: `%code’
/php-src/Zend/zend_language_parser.y:50.7-14: syntax error, unexpected identifier
make: *** [/freemouse/php-src/Zend/zend_language_parser.c] 错误 1
```

Refer: https://bugs.php.net/bug.php?id=71343

`brew install bison27`

* `YACC=/usr/local/opt/bison@2.7/bin/bison ./configure --disable-all --enable-debug --prefix=/Users/js/php/usr`
* `make && make install`

### 配置编译的php作为系统默认

* vim ~/.zshrc

```
# choose compile php as default
export PATH="/Users/js/php/usr/bin:$PATH"
```



## vld(Vulcan Logic Dumper)扩展

### 安装

Ref:

*  [PHP 内核分析经验谈：工具篇](http://www.liuhaihua.cn/archives/471421.html)

```
git clone https://github.com/derickr/vld.git
cd vld  
phpize  
./configure
make && make install

vim php.ini
[vld]
extension=vld.so
```

### 使用 VLD 查看 OPCODE

```
php -dvld.active=1 path/xxx.php
```

### vld 参数列表

```
-dvld.active: 是否在执行PHP时激活VLD挂钩
    1) 默认为0: 表示禁用
    2) 使用-dvld.active=1启用
 
-dvld.verbosity: 是否显示更详细的信息
    1) 默认为1
    2) 其值可以为0,1,2,3 其实比0小的也可以，只是效果和0一样，比如0.1之类，但是负数除外，负数和效果和3的效果一样 比3大的值也是可以的，只是效果和3一样，3代表最详细

-dvld.execute: 是否执行这段PHP脚本
    1) 默认值为1，表示执行
    2) 使用-dvld.execute=0，表示只显示中间代码，不执行生成的中间代码 

-dvld.skip_prepend: 是否跳过php.ini配置文件中auto_prepend_file指定的文件
    1) 默认为0，即不跳过包含的文件，显示这些包含的文件中的代码所生成的中间代码。此参数生效有一个前提条件：-dvld.execute=0


-dvld.format: 是否以自定义的格式显示
    1) 默认为0，表示否
    2) 使用-dvld.format=1，表示以自己定义的格式显示。这里自定义的格式输出是以-dvld.col_sep指定的参数间隔

-dvld.col_sep: 在-dvld.format参数启用时此函数才会有效，默认为 "t"

-dvld.save_dir: 指定文件输出的路径，默认路径为/tmp 

-dvld.save_paths: 控制是否输出文件，默认为0，表示不输出文件

-dvld.dump_paths: 控制输出的内容，现在只有0和1两种情况，默认为1,输出内容
```



## gdb调试

### 安装

```
brew install gdb
```

由于macos 10.12.4的安全更新，使用gdb会报错: `During startup program terminated with signal ?, Unknown signal.`.

**解决:**

`brew info gdb`:

```
On 10.12 (Sierra) or later with SIP, you need to run this:

  echo "set startup-with-shell off" >> ~/.gdbinit
```

`sudo -E gdb --args /Users/js/php/usr/bin/php test/index.php`