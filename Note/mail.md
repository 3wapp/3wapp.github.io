
## [mailgun](http://www.mailgun.com)

Mailgun 是一个简便高效的邮件发送云服务，提供丰富的API接口, 广受开发人员喜欢

### 免费版

* 每个月3000封免费邮件发送服务
* 可以绑定域名 或 使用免费的域名

## [mailnesia](http://mailnesia.com)

匿名邮箱, 可以自动激活链接, 无需注册和密码

* 自动激活注册链接
* RSS订阅


## telnet 登录smtp发邮件

telnet 通过smtp服务器发邮件，可以伪造发信地址。现在163做了安全保护，不能伪造发信人地址了，以下仅为示例。

```
# telnet smtp.163.com 25        //登陆 smtp.163.com 端口号为 25
Trying 202.108.44.205...
Connected to smtp.163.com (202.108.44.205).
Escape character is '^]'.
220 163.com Coremail SMTP(Anti Spam) System
HELO localhost                 // 与服务器打招呼，并告知客户端使用的机器名字，可以随便填写
250 OK
AUTH LOGIN                     //使用身份认证登陆指令
334 dXNlcm5hbWU6
cmVkc29zMw==                   //输入已经base64_encode()过的用户名.
334 UGFzc3dvcmQ6
MbM2MDQ3NQ==                   //输入已经base64_encode()过的密码
235 Authentication successful
MAIL FROM:<redsos3@163.com>    //告诉服务器发信人的地址
250 Mail OK
RCPT TO:<yourframe@21cn.com>   //告诉服务器收信人的地址
250 Mail OK
DATA                           //正面开始传输信件的内容，且最后要以只含有 . 的特殊行结束。
354 End data with .
From:redsos3@163.com          // 可伪造发信地址
To:yourframe@21cn.com        
Subject:test mail
test body
．                             //结束传输信件
250 Mail OK queued as smtp14,F0CPBFsuzUOvoDwE.41582S2
QUIT                          //断开连接
221 Bye
Connection closed by foreign host.
```

附录1 | 状态码说明 |
 --- | -----
220  |  服务就绪
250  | 请求邮件动作正确，完成（HELO,MAIL FROM,RCPT TO,QUIT 指令执行成功会返回此信息）
235  | 认证通过
221  | 正在处理
354  | 开始发送数据，结束以 ．（DATA指令执行成功会返回此信息）
500  | 语法错误，命令不能识别
550  | 命令不能执行，邮箱无效
552  | 中断处理 | 用户超出文件空间来自:
