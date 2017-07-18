
## install

```
pip install virtualenv
pip install virtualenvwrapper

# vim .bashrc add follow
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/workspace
source /usr/local/bin/virtualenvwrapper.sh


source .bashrc
```

* [virtualenv install](https://virtualenv.pypa.io/en/stable/installation/)
* [virtualenvwrapper install](http://virtualenvwrapper.readthedocs.io/en/latest/install.html)

## virtualenvwrapper

cmd | description
 --- | -----
mkvirtualenv ENV | 创建运行环境ENV
rmvirtualenv ENV | 删除运行环境ENV
mkproject mic | 创建mic项目和运行环境mic
mktmpenv | 创建临时运行环境
workon ENV | 工作在ENV运行环境
lsvirtualenv | 列出可用的运行环境
lssitepackages | 列出当前环境安装了的包

## 打包

* 1.复制整个环境

```
# env test
cd ~/.virtualenvs/test
# 装换为相对路径
virtualenv --relocatable ./

# copy
cp -r * /xxx/venv/
```
