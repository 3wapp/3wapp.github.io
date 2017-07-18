# byobu

## install

```
Alpine Linux	apk add byobu
Arch	pacman -Sy byobu
Debian	apt-get install byobu
Fedora	yum install byobu
Gentoo	emerge byobu
Mac OS	brew install byobu
Mint	sudo apt-get install byobu
Ubuntu	sudo apt-get install byobu
```

## cmd


* byobu-select-backend

```
Select the byobu backend:
  1. tmux
  2. screen

Choose 1-2 [1]: 1
```

* byobu

显示所有会话, 或新开一个会话

```
Byobu sessions...

  1. tmux: docker: 1 windows (created Fri Dec  2 15:11:39 2016) [101x53]
  2. tmux: docker1: 1 windows (created Fri Dec  2 15:12:11 2016) [101x53]
  3. tmux: docker2: 1 windows (created Fri Dec  2 15:12:22 2016) [101x53]
  4. Create a new Byobu session (tmux)
  5. Run a shell without Byobu (/bin/zsh)
```

### byobu-tmux

```
byobu new -s session_name
byobu a -t session_name
# 关闭某个会话
byobu kill-session -t session_name
# 关闭所有会话
byobu kill-server
```

## 快捷键

Function | Shortcut
--- | -----
创建新的窗口 | F2
回到先前窗口 | F3
跳到下一个窗口 | F4
重新命名一个窗口 | F8
重新加载文件 | F5
Detach and logout | F6
进入 复制/回滚模式 | F7
启动配置窗口 | F9
生成水平分隔 | shift+F2
生成垂直分隔 | ctrl+F2
生成新会话 | ctrl+shift+F2
在一个窗口的分隔中回到上一个子窗口，可循环 | shift+F3
在一个窗口的分隔中回到下一个子窗口，可循环 | shift+F4
切换当前窗口 | Ctrl+a H/D/J/K
调整当前窗口大小 | Ctrl+a 上/下/左/右

关闭当前窗口: 命令行输入 `exit`

```
F12 -  Lock this terminal



shift-F3 - Shift the focus to the previous split region

shift-F4 - Shift the focus to the next split region

shift-F5 - Join all splits

ctrl-F6 - Remove this split

ctrl-F5 - Reconnect GPG and SSH sockets

shift-F6 - Detach, but do not logout

alt-pgup - Enter scrollback mode

alt-pgdn - Enter scrollback mode

Ctrl-a $ - show detailed status

Ctrl-a R - Reload profile

Ctrl-a ! - Toggle key bindings on and off

Ctrl-a k - Kill the current window

Ctrl-a ~ - Save the current window's scrollback buffer
```
