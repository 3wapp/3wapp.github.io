# [Homebrew](http://brew.sh/index_zh-cn.html)

## install

`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

## brew usage

| 命令 | 说明 |
| --- | ---- |
|brew update |	更新 brew |
|brew search FORMULA |	查找软件包，可使用正则表达式|
|brew info FORMULA |	显示软件的信息|
|brew deps FORMULA |	显示包依赖|
|brew install FORMULA |	安装软件包|
|brew uninstall FORMULA|卸载软件包|
|brew list	|列出已安装的软件包，可指定 FORMULA|
|brew outdated|	列出可升级的软件包|
|brew upgrade	|更新已安装的软件包，可指定 FORMULA|
|brew doctor|	诊断 homebrew 环境|
|brew prune	|删除 /usr/local 下的无效链接(remove broken symlinks)|

## [Homebrew-cask](https://caskroom.github.io/)

install: `brew install caskroom/cask/brew-cask`

### 特别注意

homebrew-cask 是将应用程序放置在/opt/homebrew-cask/Caskroom/下，会在你的家目录中的「应用程序」文件夹中创建一个类似快捷方式的替身。在Finder的偏好设置中，第三个侧边栏勾选上你的家目录，这样找应用会方便一些。

## 更换镜像源

```
# homebrew
# remote origin
#nurl = https://github.com/Homebrew/brew
cd "$(brew --repo)"
git remote set-url origin git://mirrors.ustc.edu.cn/brew.git

# homebrew-core
# origin 
# url = https://github.com/Homebrew/homebrew-core
cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
git remote set-url origin git://mirrors.ustc.edu.cn/homebrew-core.git


# homebrew-cask
cd "$(brew --repo)/Library/Taps/caskroom/homebrew-cask"
git remote set-url origin git://mirrors.ustc.edu.cn/homebrew-cask.git/
```