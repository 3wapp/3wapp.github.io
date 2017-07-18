---
title: "Pyenv"
date: 2016-03-06 08:34
---

## pyenv 快速入门

* install 

```
$ curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
```

install requirements

```
$ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm
```

* add PATH

add follow to the end of file .bashrc

```
export PATH="/home/hx/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

* 利用virtualenv 创建虚拟python环境

现在我们已经安装了多个python版本，要求系统环境足够干净的，这时候我们可以使用virtualenv来创建虚拟python环境

virtualenv本是一个独立的工具，官网在这里：https://pypi.python.org/pypi/virtualenv

如果你是安装我们前面的方式安装pyenv的，那它已经帮我们以plugin的形式安装好了virtualenv, 我们只要使用就好了

* 安装特定版本

```
pyenv install 3.5.1
```

* 首先我们创建一个2.7.1的虚拟环境

```
$:pyenv virtualenv 3.5.1 env351
```

这条命令在本机上创建了一个名为env271的python虚拟环境，这个环境的真实目录位于：~/.pyenv/versions/

> 命令中的 ‘3.5.1’ 必须是一个安装前面步骤已经安装好的python版本， 否则会出错。

* 进入虚拟环境

```
# change to python 3.4.3 virtual environment, "deactivate" logout
pyenv activate env351
```

> pyenv 创建版本存放路径: /home/haoxi/.pyenv

然后我们可以继续通过 ‘pyenv versions’ 命令来查看当前的虚拟环境


* 删除这个虚拟环境

只要直接删除它所在的目录就好：

```
rm -rf ~/.pyenv/versions/env271/
```



## Command Reference

Like git, the pyenv command delegates to subcommands based on its first argument.

The most common subcommands are:

```
pyenv commands
pyenv local
pyenv global
pyenv shell
pyenv install
pyenv uninstall
pyenv rehash
pyenv version
pyenv versions
pyenv which
pyenv whence
pyenv commands
```

Lists all available pyenv commands.

* pyenv local

Sets a local application-specific Python version by writing the version name to a .python-version file in the current directory. This version overrides the global version, and can be overridden itself by setting the PYENV_VERSIONenvironment variable or with the pyenv shell command.

$ pyenv local 2.7.6

When run without a version number, pyenv local reports the currently configured local version. You can also unset the local version:

$ pyenv local --unset

Previous versions of pyenv stored local version specifications in a file named .pyenv-version. For backwards compatibility, pyenv will read a local version specified in an .pyenv-version file, but a .python-version file in the same directory will take precedence.

* pyenv local (advanced)

You can specify multiple versions as local Python at once.

Let's say if you have two versions of 2.7.6 and 3.3.3. If you prefer 2.7.6 over 3.3.3,

```
$ pyenv local 2.7.6 3.3.3
$ pyenv versions
  system
* 2.7.6 (set by /Users/yyuu/path/to/project/.python-version)
* 3.3.3 (set by /Users/yyuu/path/to/project/.python-version)
$ python --version
Python 2.7.6
$ python2.7 --version
Python 2.7.6
$ python3.3 --version
Python 3.3.3
```
or, if you prefer 3.3.3 over 2.7.6,

```
$ pyenv local 3.3.3 2.7.6
$ pyenv versions
  system
* 2.7.6 (set by /Users/yyuu/path/to/project/.python-version)
* 3.3.3 (set by /Users/yyuu/path/to/project/.python-version)
  venv27
$ python --version
Python 3.3.3
$ python2.7 --version
Python 2.7.6
$ python3.3 --version
Python 3.3.3
```

* pyenv global

Sets the global version of Python to be used in all shells by writing the version name to the ~/.pyenv/version file. This version can be overridden by an application-specific .python-version file, or by setting the PYENV_VERSIONenvironment variable.

```
$ pyenv global 2.7.6
```

The special version name system tells pyenv to use the system Python (detected by searching your $PATH).

When run without a version number, pyenv global reports the currently configured global version.

pyenv global (advanced)

You can specify multiple versions as global Python at once.

Let's say if you have two versions of 2.7.6 and 3.3.3. If you prefer 2.7.6 over 3.3.3,

```
$ pyenv global 2.7.6 3.3.3
$ pyenv versions
  system
* 2.7.6 (set by /Users/yyuu/.pyenv/version)
* 3.3.3 (set by /Users/yyuu/.pyenv/version)
$ python --version
Python 2.7.6
$ python2.7 --version
Python 2.7.6
$ python3.3 --version
Python 3.3.3
```

or, if you prefer 3.3.3 over 2.7.6,

```
$ pyenv global 3.3.3 2.7.6
$ pyenv versions
  system
* 2.7.6 (set by /Users/yyuu/.pyenv/version)
* 3.3.3 (set by /Users/yyuu/.pyenv/version)
  venv27
$ python --version
Python 3.3.3
$ python2.7 --version
Python 2.7.6
$ python3.3 --version
Python 3.3.3
```

* pyenv shell

Sets a shell-specific Python version by setting the PYENV_VERSION environment variable in your shell. This version overrides application-specific versions and the global version.


$ pyenv shell pypy-2.2.1

When run without a version number, pyenv shell reports the current value of PYENV_VERSION. You can also unset the shell version:

$ pyenv shell --unset

Note that you'll need pyenv's shell integration enabled (step 3 of the installation instructions) in order to use this command. If you prefer not to use shell integration, you may simply set the PYENV_VERSION variable yourself:

$ export PYENV_VERSION=pypy-2.2.1

pyenv shell (advanced)

You can specify multiple versions via PYENV_VERSION at once.

Let's say if you have two versions of 2.7.6 and 3.3.3. If you prefer 2.7.6 over 3.3.3,

```
$ pyenv shell 2.7.6 3.3.3
$ pyenv versions
  system
* 2.7.6 (set by PYENV_VERSION environment variable)
* 3.3.3 (set by PYENV_VERSION environment variable)
$ python --version
Python 2.7.6
$ python2.7 --version
Python 2.7.6
$ python3.3 --version
Python 3.3.3
```

or, if you prefer 3.3.3 over 2.7.6,

```
$ pyenv shell 3.3.3 2.7.6
$ pyenv versions
  system
* 2.7.6 (set by PYENV_VERSION environment variable)
* 3.3.3 (set by PYENV_VERSION environment variable)
  venv27
$ python --version
Python 3.3.3
$ python2.7 --version
Python 2.7.6
$ python3.3 --version
Python 3.3.3
```

* pyenv install

Install a Python version (using python-build).

```
Usage: pyenv install [-f] [-kvp] <version>
       pyenv install [-f] [-kvp] <definition-file>
       pyenv install -l|--list

  -l/--list        List all available versions
  -f/--force       Install even if the version appears to be installed already

  python-build options:

  -k/--keep        Keep source tree in $PYENV_BUILD_ROOT after installation
                   (defaults to $PYENV_ROOT/sources)
  -v/--verbose     Verbose mode: print compilation status to stdout
  -p/--patch       Apply a patch from stdin before building
  -g/--debug       Build a debug version
```

* pyenv uninstall

Uninstall a specific Python version.

```
Usage: pyenv uninstall [-f|--force] <version>

   -f  Attempt to remove the specified version without prompting
       for confirmation. If the version does not exist, do not
       display an error message.
```

* pyenv rehash

Installs shims for all Python binaries known to pyenv (i.e., ~/.pyenv/versions/*/bin/*). Run this command after you install a new version of Python, or install a package that provides binaries.

$ pyenv rehash

* pyenv version

Displays the currently active Python version, along with information on how it was set.

* pyenv versions

Lists all Python versions known to pyenv, and shows an asterisk next to the currently active version.

```
$ pyenv versions
* 2.7.6 (set by /home/yyuu/.pyenv/version)
  3.3.3
  jython-2.5.3
  pypy-2.2.1
```

* pyenv which

Displays the full path to the executable that pyenv will invoke when you run the given command.

```
$ pyenv which python3.3
/home/yyuu/.pyenv/versions/3.3.3/bin/python3.3
```

* pyenv whence

Lists all Python versions with the given command installed.

```
$ pyenv whence 2to3
2.6.8
2.7.6
3.3.3
```
* pyenv install

Part of Python-build, this installs versions of python

```
$ pyenv install 2.7.6
$ pyenv install 2.6.8
$ pyenv versions
  system
  2.6.8
* 2.7.6 (set by /home/yyuu/.pyenv/version)
```

* pyenv install --list

List available remote versions of Python, including Anaconda, Jython, pypy, and stackless

$ pyenv install --list