---
title: "Django 1.8.7"
date: 2016-01-25 00:22
---


## 参考

* [Django快速建网站][1]

[1]: http://zozoz.github.io/myblog/2015/08/28/django%E5%BF%AB%E9%80%9F%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AA%E7%BD%91%E7%AB%99/

### 基本命令

* django-admin startproject project_name

* django-admin startapp app_name

* python manage.py makemigrations

* python manage.py migrate

* python manage.py runserver

* python manage.py collectstatic

> 需要先配置 STATIC_ROOT

### 国际化和本地化

#### 本地化配置

* 根目录下面创建一个locale文件夹，
* 配置setting.py

```python
from django.utils.translation import ugettext_lazy as _

LANGUAGES = [
    ('zh-hans', _('Simplified Chinese')),  # zh-cn is deprecated
    ('en', _('English')),
]

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale/'),)  #[must be tuple]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
)

TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'django.template.context_processors.i18n',
            ],
        },
    },
]
```

> if no translation is found. leave the default: LANGUAGE_CODE = 'en-us'

> LocaleMiddleware 指定语言偏好。中间件的顺序是有影响的，最好按照依照以下要求：
> 保证它是第一批安装的中间件类。
> 因为 LocalMiddleware 要用到session数据，所以需要放在 SessionMiddleware 之后。
> 如果你使用CacheMiddleware,把LocaleMiddleware放在它后面。
>
> LocaleMiddleware 按照如下算法确定用户的语言:
> 首先，在当前用户的 session 的中查找django_language键；
> 如未找到，它会找寻一个cookie
> 还找不到的话，它会在 HTTP 请求头部里查找Accept‐Language，
> 该头部是你的浏览器发送的，并且按优先顺序告诉服务器你的语言偏好。
> Django会尝试头部中的每一个语种直到它发现一个可用的翻译。
> 以上都失败了的话, 就使用全局的 LANGUAGE_CODE 设定值。
> 中文 -> LANGUAGE_CODE = 'zh-hans'

> Django寻找项目中的翻译
> 首先，Django在该视图所在的应用程序文件夹中寻找 locale 目录。
> 若找到所选语言的翻译，则加载该翻译。
> 第二步，Django在项目目录中寻找 locale 目录。 若找到翻译，则加载该翻译。
> 最后，Django使用 django/conf/locale 目录中的基本翻译。

#### 命令创建文件

* 然后使用命令创建国际化文件：

```python
 django-admin.py makemessages -l zh_Hans
```

> zh_Hans 必须与setting.py 中 LANGUAGES 配置相同, 而且不能是 **zh-hans**, '-' 与'_' 有区别; 必须是 **zh_Hans**, zh_hans都是错的

执行完后，locale 文件夹下面创建  zh_hans/LC_MESSAGES/django.po 写好了所有的翻译后执行：

```python
 django-admin.py compilemessages
```

生成文件 zh_hans/LC_MESSAGES/django.mo ，最终的目标文件

* 如果我们在代码或模板中增加或删除了相关的国际化代码,需要从新运行 **makemessages**  和  **compilemessages**

* 如果只是改了django.po中的翻译,只需 **compilemessages** 就行了

## debug 模式

`debug=False` 的情况下，不处理静态文件，交给服务器处理，若需要在没有服务器的情况下，可以使用 `python manage.py runserver 0.0.0.0:80 --insecure`

### 模板

* 1.基本

```
# [S]: 
{% tag %}

#[D]: 
{% tag %} ... {% endtag %}
```

* entends[S]

> 告诉模板引擎，这个模板继承了另一个模板, 必须放在子模版的第一行

* load[S]

> 读入一个自定义的模板库

* include[S]

> 允许在模板中包含其它的模板的内容

* block[D]

> 告诉模板引擎，子模板可以重载这些部分

* 2. 翻译

* trans[S] 

To enable it, set USE_I18N to True, then load it with 

```
{% load i18n %}
```

> 标记需要翻译的字符串

不允许使用模板中的变量，只能使用单引号或双引号中的字符串

* blocktrans[S]

> 标记需要翻译的字符串

可以使用模板中的变量

* 3.安全

* csrf_token[S]

> 跨站请求伪造保护标签，在提交表单中需要添加

### 注释

> {# add some comment #}

### 备注

国际化 -- Internationalization，i 和 n 之间有 18 个字母，简称 I18N,。
本地化 -- localization， l 和 n 之间有 10 个字母，简称 L10N

### some examples

* 1.block.supper

```html
# Template: A.html

<html>
    <head></head>
    <body>
        {% block hello %}
            HELLO
        {% endblock %}
    </body>
</html>

# Template B.html
{% extends "A.html" %}
{% block hello %}
World
{% endblock %}

# Rendered Template B
<html>
    <head></head>
    <body>
World
    </body>
</html>

# Template C
{% extends "A.html" %}
{% block hello %}
{{ block.super }} World
{% endblock %}

# Rendered Template C
<html>
    <head></head>
    <body>
Hello World
    </body>
</html>
```

### note

* login redirect

    django登录后默认的跳转页面是 "/account/profile/",可以在 settings.py 文件中设置，改变重定向，如

    > LOGIN_REDIRECT_URL = '/'

* 自定义的 app 名称避免与内建名称相同

* models field

-  OneToOneField vs ForeignKey

OneToOneField, A one-to-one relationship. Conceptually, this is similar to a ForeignKey with unique=True, but the "reverse" side of the relation will directly return a single object.

In contrast to the OneToOneField "reverse" relation, a ForeignKey "reverse" relation returns a QuerySet

参考: [What's the difference between django OneToOneField and ForeignKey][10]


[10]: http://stackoverflow.com/questions/5870537/whats-the-difference-between-django-onetoonefield-and-foreignkey

* windows 运行 django

- "python manage.py runserver", cmd 需要管理员权限执行
- 小心端口占用，酷狗音乐使用了 8000 端口

* settings

- "from django.conf import settings" is better than "from yourprojectname import settings", for better portability

- STATIC_ROOT = 'staticfiles'

> relative path, when run "python manage.py collectstatic", collect static files to this directory

- django查找静态文件的范围

    + yourapp/static/yourapp/staticfiles

    + STATICFILES_DIRS

    + STATIC_ROOT

- MEDIA_ROOT --must absolute path

- use "MEDIA_URL" in template
    must add "django.core.context_processors.media" in settings.py->TEMPLATES->OPTIONS->context_processors

* request

    + request.path    除域名以外的请求路径，以正斜杠开头   "/hello/"
    + request.get_host()  主机名（比如，通常所说的域名） "127.0.0.1:8000" or "www.example.com"
    + request.get_full_path() 请求路径，可能包含查询字符串  "/hello/?print=true"
    + request.is_secure() HTTPS访问，返回True，否则返回False   True 或者 False

    + request.META 是一个Python字典，包含了所有本次HTTP请求的Header信息

        * HTTP_REFERER，进站前链接网页
        * HTTP_USER_AGENT，用户浏览器的user-agent字符串
        * REMOTE_ADDR 客户端IP，(如果申请是经过代理服务器的话，那么它可能是以逗号分割的多个IP地址，如："12.345.67.89,23.456.78.90" 。)

    > request.META 是一个普通的Python字典，访问一个不存在的键时，会触发一个KeyError异常

    +  request.GET 和 request.POST --类字典对象

* form

is_valid()方法：验证它的数据是否合法。

errors属性：提供了一个字段与错误消息相映射的字典表

cleaned_data属性：在数据合法的情况下，它包含干净的提交数据的字典

Django的form系统自动寻找匹配的函数方法，该方法名称以clean_开头，并以字段名称结束。 如果有这样的方法，它将在校验时被调用;自定义的clean_func()方法将在指定字段的默认校验逻辑执行之后被调用
