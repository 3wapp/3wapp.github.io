---
title: "simiki 命令"
date: 2016-01-17 16:41
---

# 基本命令

### 查看 simiki 命令帮助文档

```
$ simiki -h
```

### 生成静态页面到output目录 (需要在站点根目录下执行)

```
$ simiki g
```

### 本地预览模式(开发模式)

```
$ simiki p
```

### 本地预览模式指定绑定IP和端口, 如绑定到所有IP的8888端口

```
$ simiki p --host 0.0.0.0 --port 8888
```

### 本地预览模式监控content目录, 有变更自动更新生成相应静态页面

```
$ simiki p -w
```

### 升级Simiki后检查和更新本地内置的脚本及主题(如fabfile.py, simple主题)

```
$ simiki update
```
