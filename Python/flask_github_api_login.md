---
title: "Flask github api login"
date: 2016-03-02 10:08
---

Flask框架中，使用Github api作第三方登录

## github 注册应用

[github connect with third party applications][2]
[github api][3]

* 注册应用

[https://github.com/settings/applications/new][1]注册应用程序

```
Application name
demo

Homepage URL
http://localhost:5000/github


Application description
use github api to login

Authorization callback URL
http://localhost:5000/github/callback
```

Homepage URL 和 Authorization callback URL 根据需求来填，没有严格限制。注册完应用后会生成一个 Client ID 和 Client Secret, 这两个值用来访问Github API.它们应该存储在环境变量中，而不是被硬编码或放在版本控制库中，这样做是不安全的。

## 重定向用户请求到github，获取code信息

向 https://github.com/login/oauth/authorize 发送 get 请求，获取code信息。get请求需要带如下参数：

* client_id [required]

注册应用获取的Client ID

* redirect_url [optional]

从github获取code码之后跳转到的url,

The redirect_uri parameter is optional. If left out, GitHub will redirect users to the callback URL configured in the OAuth Application settings. If provided, the redirect URL's host and port must exactly match the callback URL. The redirect URL's path must reference a subdirectory of the callback URL.

```
CALLBACK: http://example.com/path

GOOD: http://example.com/path
GOOD: http://example.com/path/subdir/other
BAD:  http://example.com/bar
BAD:  http://example.com/
BAD:  http://example.com:8080/path
BAD:  http://oauth.example.com:8080/path
BAD:  http://example.org
```

* scope [optional]

scope 返回你需要调用github哪些信息，可以填写多个，逗号分割，如: scope=user,public_repo

不填写就只读取github公开信息。

* state [oprional]

state 自由设定，用于防止跨站请求伪造攻击

样例:

```
# 访问url
https://github.com/login/oauth/authorize?client_id=da43827a6b636a68e5ad

# github 返回code
http://loacalhost:5000/github/callback?code=8befa63003cbd59b56eb
```

## 通过code获取access_token

获取access_token，需要向 https://github.com/login/oauth/access_token POST请求，参数如下：

* client_id	[Required]

The client ID you received from GitHub when you registered.

* client_secret	[Required]

The client secret you received from GitHub when you registered.

* code [Required]

The code you received as a response

* redirect_uri

The URL in your app where users will be sent after authorization

* state

The unguessable random string you optionally provided

```python
@app.route('/github/callback', methods=['GET'])
def github_callback():
    if request.method == 'GET':
        client = Client()
        code = request.args.get('code')
        url = "https://github.com/login/oauth/access_token"
        payload = {
            'client_id': client.id,
            'client_secret': client.secret,
            'code': code
        }
        r = requests.post(url, data=payload)
        return r.content

# github 返回参数
access_token=18365f14ea0b85beecf17e841af0060e493150d1&scope=&token_type=bearer
```

## 获取用户登录信息

向 https://api.github.com/user?access_token=xxx 发送GET请求，即可获得github信息

```
public_repos: 35
site_admin: False
subscriptions_url: https://api.github.com/users/hxer/subscriptions
gravatar_id:
hireable: None
id: 15061633
followers_url: https://api.github.com/users/hxer/followers
following_url: https://api.github.com/users/hxer/following{/other_user}
blog: None
followers: 0
location: None
type: User
email: None
bio: None
gists_url: https://api.github.com/users/hxer/gists{/gist_id}
company: None
events_url: https://api.github.com/users/hxer/events{/privacy}
html_url: https://github.com/hxer
updated_at: 2016-03-03T01:31:41Z
received_events_url: https://api.github.com/users/hxer/received_events
starred_url: https://api.github.com/users/hxer/starred{/owner}{/repo}
public_gists: 6
name: {{app.__dict__}}
organizations_url: https://api.github.com/users/hxer/orgs
url: https://api.github.com/users/hxer
created_at: 2015-10-10T08:21:08Z
avatar_url: https://avatars.githubusercontent.com/u/15061633?v=3
repos_url: https://api.github.com/users/hxer/repos
following: 0
login: hxer
```


[1]: https://github.com/settings/applications/new
[2]: https://help.github.com/articles/connecting-with-third-party-applications/
[3]: https://developer.github.com/v3/oauth/
