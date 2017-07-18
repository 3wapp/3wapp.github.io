## mac 快捷键

**Shortcut** | **Function**
------------- | ----------
`Ctrl` + `space` | 输入法切换
Ctrl + Shift + Power | 关闭屏幕
Cmd + Opt + Power | 睡眠 (sleep)
Cmd + Ctrl + Power | 重启 (restart)
Cmd + Ctrl + Opt + Power | 关机 (shutdown)
fn + delete | 向光标后删除
cmd + 方向左 | home
cmd + 方向右 | end
crtl+cmd+f | 全屏某个应用
cmd+w | 关闭应用
cmd+m | 最小化应用
alt+cmd+esc | 任务管理器
cmd+shift+3 | 截全屏
cmd+shift+4 | 选择截屏
cmd+delete | 删除
cmd+alt+c | 复制当前路径(finder下)

在finder下选中一个目录按空格 可以查看目录大小

### Finder 显示路径

命令行输入:

```
defaults write com.apple.finder _FXShowPosixPathInTitle -bool YES
```

## 信息查看

### 进程

```
lsof -i tcp:8000 查看某个端口对应进程
```

## software

software | note
--- | ----
Amphetamine | 防止系统休眠 Better than Caffeine

* sougouinput

install `brew cask install sougouinput`

then `open /usr/local/Caskroom/sogouinput/{versions}/安装搜狗输入法.app`

## proxychains-ng

### conf

`vim /usr/local/Cellar/proxychains-ng/4.11/etc/proxychains.conf`

```
socks5 127.0.0.1 1080
# or
http 127.0.0.1 8080
```

* proxychains4.12_1

'/usr/local/etc/proxychains.conf'

## lxml

```
brew install libxml2 --with-python
pip install lxml
```
