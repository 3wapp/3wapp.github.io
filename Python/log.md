---
title: "Log"
date: 2016-02-25 00:25
---

# logging

* logging.getLogger([name])

返回一个logger实例，如果没有指定name，返回root logger。

> 只要name相同，返回的logger实例都是同一个而且只有一个，即name和logger实例是一一对应的。这意味着，无需把logger实例在各个模块中传递。只要知道name，就能得到同一个logger实例

* Logger.setLevel(lv)

设置logger的level， level有以下几个级别： `NOTSET` < `DEBUG` < `INFO` < `WARNING` < `ERROR` < `CRITICAL`

常用示例：

```
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
log = logging.getLogger(__name__)

logging.basicConfig(filename="xx.log",
    level=logging.DEBUG,
    format='%(asctime)s|%(filename)s|%(funcName)s|line:%(lineno)d%(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M'
)

# stdout print, other module import logger
import logging
import sys

   
# 创建一个logger 
logger = logging.getLogger('mylogger') 
logger.setLevel(logging.DEBUG) 

# 创建一个handler，用于写入日志文件 
fh = logging.FileHandler('test.log') 
fh.setLevel(logging.DEBUG) 
   
# 再创建一个handler，用于输出到控制台 
ch = logging.StreamHandler(sys.stdout) 
ch.setLevel(logging.DEBUG) 
   
# 定义handler的输出格式 
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 
# FORMATTER = logging.Formatter("\r[%(asctime)s] [%(levelname)s] %(message)s", "%H:%M:%S")
fh.setFormatter(formatter) 
ch.setFormatter(formatter) 
   
# 给logger添加handler 
logger.addHandler(fh) 
logger.addHandler(ch) 

   
# 记录一条日志 
logger.info('foorbar')
```