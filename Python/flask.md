---
title: "Flask"
date: 2016-03-02 10:08
---


## 参考资源

* [FLASK使用小结][1]
* [flask api][2]

[1]: http://www.wklken.me/posts/2013/09/09/python-framework-flask.html
[2]: http://flask.pocoo.org/docs/0.10/api/

## 快速入门

Flask依赖两个外部组件：Jinja2 和 Werkzeug路由模块

* 变量规则

给URL添加变量部分，可以将特殊的字段标记为< variable_name >,这个部分将会作为命名参数传递到你的函数。规则可以用 < converter:variable_name > 指定一个可选的转换器

```python
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
```

转换器有下面几种：

```
int	    接受整数
float	同 int ，但是接受浮点数
path	和默认的相似，但也接受斜线
```

注:

> variable_name 不能为空，否则会报错，只输入一个或多个空格是支持的

> 函数参数variable_name默认参数无效，总是从url读取。

> 需要支持url variable_name 为空，和参数 variable_name有默认参数，可以参考如下方式

```
@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return 'hello'+ (name if name else 'None')
``` 

其中，默认参数可以随便设定，没必要必须是None

* url_for

返回的是相对路径

URL 构建会转义特殊字符和 Unicode 数据

## 静态文件

在你的包中或是模块的所在目录中创建一个名为 static 的文件夹，在应用中使用 /static 即可访问。

给静态文件生成 URL ，使用特殊的 'static' 端点名:

```
url_for('static', filename='style.css')
```

这个文件应该存储在文件系统上的 static/style.css

## 渲染模板

render_template()方法可以渲染模板

> 在模板内部可以访问 request, sesion, g对象，以及get_flashed_messages()函数

自动转义默认开启，传入模板的变量包含HTML，将被自动转义，更多特性参考Jinja文档

> 自动转义只为扩展名为 .html, .htm, .xml, xhtml 开启，从字符串载入的模板将关闭自动转义

## 文件上传

用 Flask 处理文件上传，须在 HTML 表单中设置 enctype="multipart/form-data" 属性，不然浏览器不会发送文件。

已上传的文件存储在内存或是文件系统中一个临时的位置。你可以通过请求对象的 files 属性访问它们。每个上传的文件都会存储在这个字典里。它表现近乎为一个标准的 Python file 对象，但它还有一个 save() 方法，这个方法允许你把文件保存到服务器的文件系统上。

把文件按客户端提供的文件名存储在服务器上，可以将它传递给 Werkzeug 提供的 secure_filename() 函数，做文件名的过滤。

```python
from flask import request
from werkzeug import secure_filename

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))
    ...
```

> save 支持相对路径和绝对路径

## 关于响应

视图函数的返回值会被自动转换为一个响应对象。如果返回值是一个字符串， 它被转换为该字符串为主体的、状态码为 `200 OK` 的 、 MIME 类型是 `text/html` 的响应对象。Flask 把返回值转换为响应对象的逻辑是这样：

* 如果返回的是一个合法的响应对象，它会从视图直接返回。
* 如果返回的是一个字符串，响应对象会用字符串数据和默认参数创建。
* 如果返回的是一个元组，且元组中的元素可以提供额外的信息。这样的元组必须是 (response, status, headers) 的形式，且至少包含一个元素。 status 值会覆盖状态代码， headers 可以是一个列表或字典，作为额外的消息标头值。
* 如果上述条件均不满足， Flask 会假设返回值是一个合法的 WSGI 应用程序，并转换为一个请求对象。

如果你想在视图里操纵上述步骤结果的响应对象，可以使用 make_response() 函数。如有这样一个视图:

```python
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404
```

只需要把返回值表达式传递给 make_response() ，获取结果对象并修改，然后再返回它:

```python
@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp
```

## 会话

是在 Cookies 的基础上实现的，并且对 Cookies 进行密钥签名。这意味着用户可以查看你 Cookie 的内容，但却不能修改它，除非用户知道签名的密钥。

要使用会话，需要设置一个密钥

```python
# logout
session.pop('username', None)
```

## 日志

Flask 就已经预置了日志系统

```python
app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')
```

## 整合 WSGI 中间件¶

给应用添加 WSGI 中间件，可以封装内部 WSGI 应用。

例如若是想用 Werkzeug 包中的某个中间件来应付 lighttpd 中的 bugs ，可以这样做:

```python
from werkzeug.contrib.fixers import LighttpdCGIRootFix
app.wsgi_app = LighttpdCGIRootFix(app.wsgi_app)
```

## sqlite


## 路径

app.root_path 属性可以获取应用的路径。配合 os.path 模块使用，轻松可达任意文件

## note

* return a requests response object

```
import requests

@app.route('/')
def index():
    url = 'xxx'
    resp = requests.get(url)
    return (resp.content, resp.status_code, resp.headers.items())
```

* Flask instance

```
app = Flask(__name__)
```

app 的属性或方法会比 Flask 多