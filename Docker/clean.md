## 镜像清理

```
# 删除所有未打 dangling 标签的镜像
docker rmi $(docker images -q -f dangling=true)

# 删除所有镜像
docker rmi $(docker images -q)
```

## 容器清理

```
# 杀死所有正在运行的容器
docker kill $(docker ps -a -q)

# 删除所有已经停止的容器
docker rm $(docker ps -a -q)
```

## volume

```
# 移除无用的挂载目录
docker volume rm $(docker volume ls -qf dangling=true)
```