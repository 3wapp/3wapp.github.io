---
title: "微信公众号开发"
date: 2016-04-19 11:12
---

## wechat-sdk

### 开发者认证配置

[接入指南, 成为开发者][3]

开发者通过检验signature对请求进行校验。若确认此次GET请求来自微信服务器，请原样返回echostr参数内容，则接入生效，成为开发者成功，否则接入失败。

```
加密/校验流程如下：
1. 将token、timestamp、nonce三个参数进行字典序排序
2. 将三个参数字符串拼接成一个字符串进行sha1加密
3. 开发者获得加密后的字符串可与signature对比，标识该请求来源于微信
```

```python
from flask import Flask
from flask import request

from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic

conf = WechatConf(
    token='',
    appid='',
    appsecret='',
    encrypt_mode='safe',
    encoding_aes_key='',
)

wechat = WechatBasic(conf=conf)

app = Flask(__name__)

@app.route('/weixin', methods=['GET'])
def check():
    args = request.args
    signature = args.get('signature')
    timestamp = args.get('timestamp')
    nonce = args.get('nonce')
    echostr = args.get('echostr')
    if all([signature, timestamp, nonce, echostr]) and wechat.check_signature(signature, timestamp, nonce):
        return echostr
    else:
        return 'error'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
```

## 微信请求

### 格式

```
POST /weixin?signature=92db6dae514eaec009a55926df68734815d450e9&timestamp=1461049146&nonce=12030128&encrypt_type=aes&msg_signature=20b4e1f1a0e59d4cb670bc082ad2256157cad3d3

<xml><ToUserName><![CDATA[gh_e712ef998048]]></ToUserName>
<FromUserName><![CDATA[ojNiswfpvDLPxYinSkmqI3T0vDdA]]></FromUserName>
<CreateTime>1461049145</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[hi]]></Content>
<MsgId>6275158296027149334</MsgId>
</xml>
```

### 解析请求

[wechat sdk 消息管理接口][4]

```python
err_msg = 'error'
args = request.args
if request.method == 'POST':
    data = request.data
    print args
    print data
    if not parse_request(args, data):
        return err_msg

def parse_request(args, data):
    msg_signature = args.get('msg_signature')
    timestamp = args['timestamp']
    nonce = args['nonce']
    try:
        wechat.parse_data(data, msg_signature, timestamp, nonce)
    except Parse_Error:
        print 'Parse Error'
        return False
    return True

```

### 被动回复消息 -- 文本消息

将文字信息组装为符合微信服务器要求的响应数据

```
调用方法：.response_text(content, escape=False)

参数说明：

content: 回复文字
escape: 是否转义该文本内容 (默认不转义)
```



[3]: http://mp.weixin.qq.com/wiki/8/f9a0b8382e0b77d87b3bcc1ce6fbc104.html
[4]: http://wechat-python-sdk.com/official/message/