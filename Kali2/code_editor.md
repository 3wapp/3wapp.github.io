---
title: "Code editor"
date: 2016-01-20 21:38
---

# vscode

## install

```
Download
unzip VSCode-linux-x64.zip -d ~/opt/vscode
sudo ln -s ~/opt/vscode/Code /usr/local/bin/code
code        #to run
```

## 运行python

* press **Ctrl+Shift+B**

It will open a message saying "No task runner configured"

* Press "Configure Task Runner"

It will open/create the file .vscode/tasks.json

* Replace the instructions with

```
// A task runner that calls the Typescript compiler (tsc) and
// Compiles a HelloWorld.ts program

{
    "version": "0.1.0",
    "command": "python",
    "args": ["${fileBasename}"],
    "showOutput": "always"
}
```

this configure also for ** windows 10** to run

4. Go back to your Python file and press Ctrl+Shift+B again

It should run the code with python

## 安装插件

* 方法 1. Ctrl/Cmd+P (或 Ctrl/Cmd + E) 输入 ext install [插件关键字/名称]

* 方法 2. Ctrl/Cmd+Shift+P (或 F1) 输入 Extensions, 选中 Install Extension 然后输入插件名称/关键字.

* 不在插件商店的插件, 则可以放置到用户目录下的 .vscode/extensions 文件夹中~ 重启 VS Code 即可生效.

## 插件

* python

    + Magic Python


# sublime text3

* 官网下载deb包，安装

* 升级，下载新的deb包，直接安装，不会覆盖之前的配置和已安装的插件

* 命令行输入：subl, 即可运行

* 安装包管理

选择：view->Show Console,复制如下内容后回车，稍等片刻后会提示重启即可（需要联网）

```
import urllib.request,os,hashlib; h = '2915d1851351e5ee549c20394736b442' + '8bc59f460fa1548d1514676163dafc88'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
```

## 字体

* 安装文泉驿字体:

```
$sudo apt-get install xfonts-wqy
```
配置Sublime Text 3的Setting User,添加如下内容
```
"font_face": "WenQuanYi Micro Hei Mono"
```

## 输入中文

安装插件 InputHelper，用于输入中文

```
$cd ~/.config/sublime-text-3/Packages
$git clone https://github.com/xgenvn/InputHelper.git
```

到此，按下Ctrl + Shift + Z，输入中文；

## 插件

* Install SublimeREPL

Preferences | Package Control | Package Control: Install Package （enter）
Choose SublimeREPL

* Theme-Flatland
* Package Control
* git
* GitGutter

* Anaconda

```
setting-User:{
    "pep8": false,
    "complete_parameters": true,
    "complete_all_parameters": false,
    "pep8_ignore":
    [
         "E501"
    ],
}
```

* MarkdownPreview

```
setting-User:{
    /* Sets the parser used for building markdown to HTML. */
    "parser": "markdown",

    /* Enable or not mathjax support. */
    "enable_mathjax": true,

    "enable_highlight": true,

}
```

* vi mod 

启用Vintage,Vintage默认禁用

选择Preferences/Settings - Default菜单

编辑ignored_packages配置, 修改:

    "ignored_packages": ["Vintage"]
成:

    "ignored_packages": []

然后保存文件。

Vintage模式则已启用——你可以看到"INSERT MODE"显示在状态栏了。

Vintage默认是插入模式。可以添加:

    "vintage_start_in_command_mode": true

这项配置到User Settings里

## user 配置文件

```
{
	"close_windows_when_empty": false,
	"color_scheme": "Packages/Theme - Flatland/Flatland Monokai.tmTheme",
	"create_window_at_startup": false,
	"ensure_newline_at_eof_on_save": true,
	"font_size": 12,
	"ignored_packages":
	[

	],
	"open_files_in_new_window": false,
	"remember_full_screen": true,
	"show_encoding": true,
	"theme": "Flatland Dark.sublime-theme",
	"translate_tabs_to_spaces": true,
	"trim_trailing_white_space_on_save": true,
	"vintage_start_in_command_mode": true,
}
```

快捷键：Prefernces->Key Bindingd - User
```
[ {"keys":["f5"],
    "caption": "SublimeREPL: Python - RUN current file",
    "command": "run_existing_window_command", "args":
    {
        "id": "repl_python_run",
        "file": "config/Python/Main.sublime-menu"
    }}
]
```

# pycharm

* install

```
download *.tar.gz
解压
cd pytcharm*/bin
./pycharm.sh
```

* license

```
username: SanQ

license:
30796-12042010
000033sWgINzq3OvdRUDrTyy9BCtS4
jmMJIvIZY5FaLP4jDn"Br"YQgh9VKR
mFTbg2svsRmX6ND8DKXcAtaafWxxYl
```

[pycharm 激活码][50]

* run

```
charm
```



# vim


## vunble

```
mkdir ~/.vim
mkdir ~/.vim/bundle
mkdir ~/.vim/bundle/vundle
vim ~/.vimrc

git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/
```

* 函数折叠

命令行模式下， za 组合键折叠当前函数

* vim .vimrc

```
" Use Vim settings, rather then Vi settings. This setting must be as early as
" possible, as it has side effects.
set nocompatible

" Highlight current line
au WinLeave * set nocursorline nocursorcolumn
au WinEnter * set cursorline cursorcolumn
set cursorline cursorcolumn

" Leader
let mapleader = ","

set backspace=2   " Backspace deletes like most programs in insert mode
set nobackup
set nowritebackup
set noswapfile    " http://robots.thoughtbot.com/post/18739402579/global-gitignore#comment-458413287
set history=50
set ruler         " show the cursor position all the time
set showcmd       " display incomplete commands
set incsearch     " do incremental searching
set laststatus=2  " Always display the status line
set autowrite     " Automatically :write before running commands
set confirm       " Need confrimation while exit
set fileencodings=utf-8,gb18030,gbk,big5

" Switch syntax highlighting on, when the terminal has colors
" Also switch on highlighting the last used search pattern.
if (&t_Co > 2 || has("gui_running")) && !exists("syntax_on")
  syntax on
endif

" .vimrc.bundles save configuration of plugin
if filereadable(expand("~/.vimrc.bundles"))
  source ~/.vimrc.bundles
endif

filetype plugin indent on

augroup vimrcEx
  autocmd!

  " When editing a file, always jump to the last known cursor position.
  " Don't do it for commit messages, when the position is invalid, or when
  " inside an event handler (happens when dropping a file on gvim).
  autocmd BufReadPost *
    \ if &ft != 'gitcommit' && line("'\"") > 0 && line("'\"") <= line("$") |
    \   exe "normal g`\"" |
    \ endif

  " Cucumber navigation commands
  autocmd User Rails Rnavcommand step features/step_definitions -glob=**/* -suffix=_steps.rb
  autocmd User Rails Rnavcommand config config -glob=**/* -suffix=.rb -default=routes

  " Set syntax highlighting for specific file types
  autocmd BufRead,BufNewFile Appraisals set filetype=ruby
  autocmd BufRead,BufNewFile *.md set filetype=markdown

  " Enable spellchecking for Markdown
  autocmd FileType markdown setlocal spell

  " Automatically wrap at 80 characters for Markdown
  autocmd BufRead,BufNewFile *.md setlocal textwidth=80
augroup END

" Softtabs, 4 spaces
set tabstop=4
set shiftwidth=2
set shiftround
set expandtab

" Display extra whitespace
set list listchars=tab:»·,trail:·

" Use The Silver Searcher https://github.com/ggreer/the_silver_searcher
if executable('ag')
  " Use Ag over Grep
  set grepprg=ag\ --nogroup\ --nocolor

  " Use ag in CtrlP for listing files. Lightning fast and respects .gitignore
  let g:ctrlp_user_command = 'ag %s -l --nocolor -g ""'

  " ag is fast enough that CtrlP doesn't need to cache
  let g:ctrlp_use_caching = 0
endif

" Color scheme
colorscheme molokai
highlight NonText guibg=#060606
highlight Folded  guibg=#0A0A0A guifg=#9090D0

" Make it obvious where 80 characters is
set textwidth=80
set colorcolumn=+1

" Numbers
set number
set numberwidth=5

" Tab completion
" will insert tab at beginning of line,
" will use completion if not at beginning
set wildmode=list:longest,list:full
function! InsertTabWrapper()
    let col = col('.') - 1
    if !col || getline('.')[col - 1] !~ '\k'
        return "\<tab>"
    else
        return "\<c-p>"
    endif
endfunction
inoremap <Tab> <c-r>=InsertTabWrapper()<cr>
inoremap <S-Tab> <c-n>

" Exclude Javascript files in :Rtags via rails.vim due to warnings when parsing
let g:Tlist_Ctags_Cmd="ctags --exclude='*.js'"

" Index ctags from any project, including those outside Rails
map <Leader>ct :!ctags -R .<CR>

" Switch between the last two files
nnoremap <leader><leader> <c-^>

" Get off my lawn
nnoremap <Left> :echoe "Use h"<CR>
nnoremap <Right> :echoe "Use l"<CR>
nnoremap <Up> :echoe "Use k"<CR>
nnoremap <Down> :echoe "Use j"<CR>

" vim-rspec mappings
nnoremap <Leader>t :call RunCurrentSpecFile()<CR>
nnoremap <Leader>s :call RunNearestSpec()<CR>
nnoremap <Leader>l :call RunLastSpec()<CR>

" Run commands that require an interactive shell
nnoremap <Leader>r :RunInInteractiveShell<space>

" Treat <li> and <p> tags like the block tags they are
let g:html_indent_tags = 'li\|p'

" Open new split panes to right and bottom, which feels more natural
set splitbelow
set splitright

" Quicker window movement
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-h> <C-w>h
nnoremap <C-l> <C-w>l

" configure syntastic syntax checking to check on open as well as save
let g:syntastic_check_on_open=1
let g:syntastic_html_tidy_ignore_errors=[" proprietary attribute \"ng-"]

autocmd Syntax javascript set syntax=jquery " JQuery syntax support

set matchpairs+=<:>
set statusline+=%{fugitive#statusline()} "  Git Hotness

" Nerd Tree
let NERDChristmasTree=0
let NERDTreeWinSize=40
let NERDTreeChDirMode=2
let NERDTreeIgnore=['\~$', '\.pyc$', '\.swp$']
let NERDTreeShowBookmarks=1
let NERDTreeWinPos="left"
autocmd vimenter * if !argc() | NERDTree | endif " Automatically open a NERDTree if no files where specified
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTreeType") && b:NERDTreeType == "primary") | q | endif " Close vim if the only window left open is a NERDTree
nmap <F5> :NERDTreeToggle<cr>

" Tagbar
let g:tagbar_width=35
let g:tagbar_autofocus=1
nmap <F6> :TagbarToggle<CR>

" Emmet
let g:user_emmet_mode='i' " enable for insert mode

" Search results high light
set hlsearch

" nohlsearch shortcut
nmap -hl :nohlsearch<cr>
nmap +hl :set hlsearch<cr>

" Javascript syntax hightlight
syntax enable

" YouCompleteMe
let g:ycm_autoclose_preview_window_after_completion=1
nnoremap <leader>g :YcmCompleter GoToDefinitionElseDeclaration<CR>

" ctrlp
set wildignore+=*/tmp/*,*.so,*.swp,*.zip     " MacOSX/Linux"
let g:ctrlp_custom_ignore = '\v[\/]\.(git|hg|svn)$'

set laststatus=2 " Always display the status line
set statusline+=%{fugitive#statusline()} "  Git Hotness

nnoremap <leader>w :w<CR>
nnoremap <leader>q :q<CR>

" RSpec.vim mappings
map <Leader>t :call RunCurrentSpecFile()<CR>
map <Leader>s :call RunNearestSpec()<CR>
map <Leader>l :call RunLastSpec()<CR>
map <Leader>a :call RunAllSpecs()<CR>

" Vim-instant-markdown doesn't work in zsh
set shell=bash\ -i

" Snippets author
let g:snips_author = 'Yuez'
```

* vim .vimrc.bundles

```
if &compatible
  set nocompatible
end

" support vundle
filetype off
set rtp+=~/.vim/bundle/vundle/
call vundle#rc()

" Let Vundle manage Vundle
Bundle 'gmarik/vundle'

" Define bundles via Github repos
Bundle 'christoomey/vim-run-interactive'
Bundle 'Valloric/YouCompleteMe'
Bundle 'croaky/vim-colors-github'
Bundle 'danro/rename.vim'
Bundle 'majutsushi/tagbar'
Bundle 'kchmck/vim-coffee-script'
Bundle 'kien/ctrlp.vim'
Bundle 'pbrisbin/vim-mkdir'
Bundle 'scrooloose/syntastic'
Bundle 'slim-template/vim-slim'
Bundle 'thoughtbot/vim-rspec'
Bundle 'tpope/vim-bundler'
Bundle 'tpope/vim-endwise'
Bundle 'tpope/vim-fugitive'
Bundle 'tpope/vim-rails'
Bundle 'tpope/vim-surround'
Bundle 'vim-ruby/vim-ruby'
Bundle 'vim-scripts/ctags.vim'
Bundle 'vim-scripts/matchit.zip'
Bundle 'vim-scripts/tComment'
Bundle "mattn/emmet-vim"
Bundle "scrooloose/nerdtree"
Bundle "Lokaltog/vim-powerline"
Bundle "godlygeek/tabular"
Bundle "msanders/snipmate.vim"
Bundle "jelera/vim-javascript-syntax"
Bundle "altercation/vim-colors-solarized"
Bundle "othree/html5.vim"
Bundle "xsbeats/vim-blade"
Bundle "Raimondi/delimitMate"
Bundle "groenewege/vim-less"
Bundle "evanmiller/nginx-vim-syntax"
Bundle "Lokaltog/vim-easymotion"
Bundle "tomasr/molokai"
Bundle "klen/python-mode"
```

```
$vim            #open vim
:BundleInstall  #install plugin
```

* YouCompleteMe error

```
Done! With errors; press l to view log
ycm_client_support.[so|pyd|dll] and ycm_core.[so|pyd|dll] not detected; you need
to compile YCM before using it. Read the docs!
```

solution:

```
cd ~/.vim/bundle/YouComleteMe
git submodule update --init --recursive
sudo apt-get install cmake
python install.py
```
 
* bundle base cmd

```
:BundleInstall
BundleClean
BundleUpdate
```

[50]: http://blog.sina.com.cn/s/blog_83dc494d0102vjyt.html