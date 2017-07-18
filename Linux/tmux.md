---
title: "Tmux"
date: 2016-03-30 23:58
---

## 简介

Tmux 是一个工具，用于在一个终端窗口中运行多个终端会话。不仅如此，你还可以通过 Tmux 使终端会话运行于后台或是按需接入、断开会话

[tmux 配置][1]

tmux是典型的c/s架构。有如下几个概念。

* session

session是一个特定的终端组合。输入tmux就可以打开一个新的session。

* window

window 为session中的终端。

* pane 

pane为一个window分隔出来的各个间隔，即window中的终端。

## install

```
apt-get install tmux
```

### cmd 

```
# 关闭所有会话
tmux kill-server
# 关闭某个会话
tmux kill-session -t session_name

息查询:

tmux list-keys 列出所有可以的快捷键和其运行的 tmux 命令
tmux list-commands 列出所有的 tmux 命令及其参数
tmux info 流出所有的 session, window, pane, 运行的进程号，等。
会话控制:

tmux new -s session_name 创建一个叫做 session_name 的 tmux session
tmux attach -t session_name 重新开启叫做 session_name 的 tmux session
tmux switch -t session_name 转换到叫做 session_name 的 tmux session
tmux list-sessions / tmux ls 列出现有的所有 session
tmux detach 离开当前开启的 session
tmux kill-server 关闭所有 session
窗口控制:

tmux new-window 创建一个新的 window
tmux list-windows 列出所有的 window
tmux select-window -t :0-9 根据索引转到该 window
tmux rename-window 重命名当前 window
窗格控制:

tmux split-window 将 window 垂直划分为两个 pane
tmux split-window -h 将 window 水平划分为两个 pane
tmux swap-pane -[UDLR] 在指定的方向交换 pane
tmux select-pane -[UDLR] 在指定的方向选择下一个 pane
```

## 基本用法

tmux的所有操作必须先使用一个前缀键进入命令模式，或者说进入控制台，就像vi中的esc。默认的前缀为<c-b>,比较难按，很多人会改为screen中的<c-a>，来保持一致性。

进入命令模式，输入**?**显示所有的bind-key,按 q 退出。

Tmux 的配置文件 ~/.tmux.conf

系统默认 bind-key, 省略了前缀键:

* 复制粘贴

```
[   : 进入复制模式。
]   : 粘贴
```

进入复制模式后，按下sapce就可以选择文本。回车键进行复制

* session操作

```
s   : 列出当前 Tmux 中的会话
d   : deattch当前session。输入tmux attach [-t sessionname]重新进入该session。
$   : 重命名当前session

<c-z> : 挂起当前session
```

* window操作

```
c   : 创建一个新的window
b   : 重命名当前window
&   : 关闭当前window
n   : 移动到下一个窗口
p   : 移动到前一个窗口
l   : 切换到上一个窗口
w   : 列出所有窗口编号,并进行选择切换编号,移动到指定编号的窗口。
.   : 修改窗口编号，相当于排序。
f   : 搜索所有的窗
```

若要切换窗口，只需要先按下Ctrl-b，然后再按下想切换的窗口所对应的数字，该数字会紧挨着窗口的名字显示

* pane操作

```
"   : 横向分割
# 配置文件将 % 改为了 | 作为纵向分割
%   : 纵向分割
方向键 : 在pane直接移动
o   : 到下一个pane
opt+方向键 : 调整pane大小
{ / } : 左右pane交换
空格 : 横竖切换
q   : 显示pane的编号
x   : 关闭当前pane
```

## 自定义配置文件

* reload conf

```
# bind a reload key r
bind r source-file ~/.tmux.conf ; display-message "Config reloaded.."
```

* vim

```
set -g status-keys vi
setw -g mode-keys vi
```

* 复制粘贴

```
# Copy and paste like in vim
unbind [
unbind ]
bind Escape copy-mode
unbind p
bind p paste-buffer
bind -t vi-copy 'v' begin-selection
bind -t vi-copy 'y' copy-selection
```

设置 Tmux esc进入复制模式，使用 v 键选择文本，用 y 键复制文本

所有的复制都会被记录到缓冲区，输入#或者 tmux list-buffers查看缓冲区,同时也进入了复制模式。也可以使用”=”来选择并粘贴缓冲区内容

在默认情况下，当从 Tmux 中复制文本时，复制下来的文本只能粘贴到同一个 Tmux 会话中。若要使复制下来的文本可以粘贴到任何位置，就需要让 Tmux 将文本复制到系统的剪贴板

使用 xclip 同样键入y复制buffer中最新的内容到系统剪贴板，配置如下

```
bind y run-shell "tmux show-buffer | xclip -sel clip -i" \; display-message "Copied tmux buffer to system clipboard"
```


* 状态栏

```
# 状态栏
  
# 颜色
  set -g status-bg black
  set -g status-fg white
 
# 对齐方式
  set-option -g status-justify centre
   
# 左下角
  set-option -g status-left '#[bg=black,fg=green][#[fg=cyan]#S#[fg=green]]'
  set-option -g status-left-length 20
   
# 窗口列表
  setw -g automatic-rename on
  set-window-option -g window-status-format '#[dim]#I:#[default]#W#[fg=grey,dim]'
  set-window-option -g window-status-current-format '#[fg=cyan,bold]#I#[fg=blue]:#[fg=cyan]#W#[fg=dim]'
   
# 右下角
  set -g status-right '#[fg=green][#[fg=cyan]%Y-%m-%d#[fg=green]]'
```

## tmux命令

```
$tmux --h
usage: tmux [-2CluvV] [-c shell-command] [-f file] [-L socket-name]
            [-S socket-path] [command [flags]]
```   

* 会话

```
tmux new -s session
tmux new -s session -d #在后台建立会话
tmux ls #列出会话
tmux attach -t session #进入某个会话
```

tmux中创建一个新的会话，只需要按下 Ctrl-b : ，然后输入如下的命令：

```
new -s <name-of-my-new-session>
```

## 配置

~/.tmux.conf

```

#-- base settings --#
set -g default-terminal "screen-256color"
set -g display-time 3000
set -g escape-time 0
set -g history-limit 65535
set -g base-index 1
set -g pane-base-index 1

# vi mode
set -g status-keys vi
setw -g mode-keys vi

# 开启status-bar uft-8支持
set -g status-utf8 on

set -g status-interval 1

set -g visual-activity on
setw -g monitor-activity on

# 状态栏

# 颜色
  set -g status-bg black
  set -g status-fg white

# 对齐方式
  set-option -g status-justify centre

# 左下角
  # set-option -g status-left '#[bg=black,fg=green][#[fg=cyan]#S#[fg=green]]'
  set-option -g status-left "#[fg=green]s#S:w#I.p#P#[default]"
  set-option -g status-left-length 20

# 窗口列表
  setw -g automatic-rename on
  set-window-option -g window-status-format '#[dim]#I:#[default]#W#[fg=grey,dim]'
  set-window-option -g window-status-current-format '#[fg=cyan,bold]#I#[fg=blue]:#[fg=cyan]#W#[fg=dim]'

# 右下角
  set -g status-right '#[fg=green][#[fg=cyan]%Y-%m-%d#[fg=green]]'



# prefix C-x
unbind C-b
set -g prefix C-x

# Copy and paste like in vim
unbind [
unbind ]
bind Escape copy-mode
unbind p
bind p paste-buffer
bind -t vi-copy 'v' begin-selection
bind -t vi-copy 'y' copy-selection

bind y run-shell "tmux show-buffer | xclip -sel clip -i" \; display-message "Copied tmux buffer to system clipboard"


unbind %
bind | splitw -h # horizontal split (prefix |)

# bind a reload key r
bind r source-file ~/.tmux.conf ; display-message "Config reloaded.."

# 同一个窗口中的面板操作--------------
#up
bind-key k select-pane -U
#down
bind-key j select-pane -D
#left
bind-key h select-pane -L
#right
bind-key l select-pane -R

# swap panes
bind ^u swapp -U
bind ^d swapp -D


# window --------------------------

#select last window
bind-key C-l select-window -l

bind-key D source-file ~/.tmux/layout

```         

键入 Ctrl + x D (D是大写)，即会自动执行layout脚本

~/.tmux/layout

```
selectp -t 1     #选中第0个窗格
splitw -h -p 50  #将其分成左右两个
selectp -t 2     #选中第一个，也就是右边那个
splitw -v -p 50  #将其分成上下两个，这样就变成了图中的布局了
selectp -t 1     #选回第一个
```

[1]: http://mingxinglai.com/cn/2012/09/tmux/