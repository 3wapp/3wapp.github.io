---
title: "Google Hacking"
date: 2016-03-08 20:00
---

## 常用搜索技巧

* site

search specific site

> can not search port

```
site:github.com
```

* inurl

search url

> can search the whole URL, including port and filetype

```
inurl:admin
inurl:admin.php
```

* filetype

search secific files

> only search file extension

```
filetype:php
```

* intext

```
# scan port
inurl:8000 -intext:8000
```

* intitle

* link

* author

* daterange

* numrange


## special characters

* +

force inclusion of something common

* -

exclude a search term

* "

use quotes around search phrases

* .

a single-character wildcard

* *

any word

* |

boolean 'OR'

## digging SQL

* password

```
filetype:inc intext:mysql_connect
filetype:inc intext:password
filetype:sql +"IDENTIFIED BY" -cvs
filetype:sql +"IDENTIFIED BY" ("Grant * on *" | "create user")
```

* sql dump detction

```
# php-nuke or postnuke CMS dumps
inurl:nuke filetype:sql

# SQL database dumps or batched SQL
filetype:sql password

# SQL database dumps or batched SQL commands, focus on "IDENTIFIED BY", which can locate passwords
filetype:sql +"IDENTIFIED BY" -cvs

# SQL database dumps
"mysql dump" filetype:sql
"# Dumping data for table(username|user|users|password)"
"# Dumping data for table"
"# phpMyAdmin MySQL-Dump" filetype:txt
"# phpMyAdmin MySQL-Dump" "INSERT INTO" -"the"
```

* database detection

```
# ColdFusion source code
filetype:cfm "cfapplication name" password

# Microsoft Access
filetype:mdb inurl:user.mdb
inurl:email filetype:mdb
inurl:backup filetype:mdb
inurl:forum filetype:mdb
inurl:profiles filetype:mdb
allinurl:admin.mdb
# ASP
inurl:/db/main.mdb
```

## Web File Browser

* "Web File Browser" "Use regular experssion"

## VNC

* intitle:"VNC viewer for Java"

## WebCam

```
"Active Webcam page" inurl:8080
```

## Network cameras

```
intitle:"toshiba network camera-User Login"
```