## iTerm2

### 通用终端命令

```
ctrl + a 将光标移动到命令行开头
ctrl + e 将光标移动到命令行结尾处
ctrl + u 删除光标前面所有字符
ctrl + k 删除光标后面所有字符
```

### 常用设置

* iTerm2设置为默认终端：`（菜单栏）iTerm -> Make iTerm2 Default Term`
* 在 Keys -> Hotkey 中设置 `optin + space` 快速显示和隐藏iTerm
* 自定义快捷键，在`iTerm->Preferences->Keys`里面设置

## [配色方案](http://iterm2colorschemes.com/)

* [Solarized](http://ethanschoonover.com/solarized) -- [github](https://github.com/altercation/solarized)
* [iTerm2-Color-Schemes](https://github.com/mbadolato/iTerm2-Color-Schemes)

1. 下载完成后依次选择：iTerm->Preferences->Profiles->Colors
2. 然后选择下面的Load Presets->Import，选择下载好的schemes文件夹里面的.itermcolors后缀的文件导入主题即可选择使用。

* 常用的快捷键：
================

**Function** | **Shortcut**
-------- | --------
新建term窗口 | `⌘` + `n`
新建标签页 | `⌘` + `t`
关闭标签页或者窗口 | `⌘` + `w`
分屏显示 |  `⌘` + `d` / `⌘` + `shift` + `d`
tab标签页之间切换 | `⌘` + `数字` / `⌘` + `<-` / `->`
自动补全 | `⌘` + `;`
Move forward a word | `Option` + `f`
Move backward a word | `Option` + `b`
Clear the screen | `⌘` + `k`


Tabs and Windows
================
**Function** | **Shortcut**
-------- | --------
Previous Tab | `⌘`+ `Left Arrow`
Next Tab | `⌘`+ `Right Arrow`
Go to Tab | `⌘` + `Number`
Go to Window | `⌘` + `Option` + `Number`
Go to Split Pane by Direction | `⌘` + `Option` + `Arrow`
Go to Split Pane by Order of Use | `⌘` + `]` , `⌘` + `[`
Split Window Horizontally (same profile) | `⌘` + `D`
Split Window Vertically (same profile) | `⌘` + `d`
Split Window Horizontally (new profile) | `Option` + `⌘` + `H`
Split Window Vertically (new profile) | `Option` + `⌘` + `V`
关闭当前标签页 | `⌘` + 'w'
新的标签页 | `⌘` + 't'
Set Mark | `⌘` + `M`
Jump to Mark | `⌘` + `J`
进入与返回全屏模式 | `⌘` + `enter`
清屏 | `⌘` + `r`

Basic Moves
===========
**Function** | **Shortcut**
-------- | --------
Move back one character | `Ctrl` + `b`
Move forward one character | `Ctrl` + `f`
Delete current character | `Ctrl` + `d`
Delete previous character | `Backspace`
Undo | `Ctrl` + `-`

通用快捷键
=============
**Function** | **Shortcut**
-------- | --------
清空当前行 | `Ctrl` + `u`
移动到行首 | `Ctrl` + `a`
移动到行尾 | `Ctrl` + `e`
向前移动 | `Ctrl` + `f`
向后移动 | `Ctrl` + `b`
上一条命令 | `Ctrl` + `p`
下一条命令 | `Ctrl` + `n`
搜索历史命令 | `Ctrl` + `r`
删除光标之前的字符 | `Ctrl` + `y`
召回最近用命令删除的文字 | `Ctrl` + `h`
删除光标所指的字符 | `Ctrl` + `d`
删除光标之前的单词 | `Ctrl` + `w`
删除从光标到行尾的内容 | `Ctrl` + `k`
交换光标和之前的字符 | `Ctrl` + `t`



Cut and Paste
=============
**Function** | **Shortcut**
-------- | --------
Cut from cursor to the end of line | `Ctrl` + `k`
Cut from cursor to the end of word | `Option` + `d`
Cut from cursor to the start of word | `Option` + `Backspace`
Cut from cursor to previous whitespace | `Ctrl` + `w`
Paste the last cut text | `Ctrl` + `w`
Loop through and paste previously cut text | `Option` + `y`
Loop through and paste the last argument of previous commands | `Option` + `.`

Search the Command History
==========================
**Function** | **Shortcut**
-------- | --------
Search as you type | `Ctrl` + `r` and type the search term; Repeat `Ctrl` + `r` to loop through result
Search the last remembered search term | `Ctrl` + `r` twice
End the search at current history entry  | `Ctrl` + `y`
Cancel the search and restore original line | `Ctrl` + `g`
自动列出剪切板的历史记录 | `⌘` + `shift` + `h`
补全 | `⌘` + ';'

## zsh

install: `brew install zsh`

安装完成后，将zsh设置成系统默认shell，以代替bash。 用编辑器打开/etc/shells，在末尾添加/usr/local/bin/zsh,保存关闭。 在终端中执行以下命令：

chsh -s /usr/local/bin/zsh

[oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh/)

### config

```
# .zsrc
ZSH_THEME = agnoster
```
