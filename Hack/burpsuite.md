---
title: "BurpSuite"
date: 2016-05-19 14:58
---

[乌云 Brup使用介绍][1]

## Intruder

### attack type

四种模式`sniper, battering ram, pitchfork, cluster bomb`

* sniper(狙击手) 

使用一套单一的payloads。它的目标依次在每个有效载荷的位置，并把每个有效载荷送入依次那个位置。

攻击中生成的请求的总数是位置的数目和在有效载荷中设定的有效载荷的数量的乘积。

* Battering ram(撞击物) 

使用一组payload。通过迭代的有效载荷方式，并将相同的payloads再一次填充到所有已定义的有效载荷。当其中一个攻击需要相同的输入将被插入在多个地方在请求中,对这种攻击类型是非常有用的。例如生成一组数字1-9，则就是1-1 ，2-2，3-3这种形式

在攻击中生成的请求的总数是有效载荷的有效载荷中设定的数目

* Pitchfork(相交叉) 

使用多个payloads集。对每个定义的位置（最多20个）赋予不同的有效载荷。通过设置所有有效载荷的攻击迭代的方式，并将一个有效载荷传到所定义的位置。例如设置多个payload，每个payload设置一个字典，则就是1-1-1，2-2-2，3-3-3这种形式

在攻击中生成的请求的总数是有效载荷中的最小有效载荷组的数目。

* Cluster bomb(集束炸弹)

使用多个Payload sets。对每个定义的Positions（最多20个）设置不同的payload set。通过每个有效载荷的攻击迭代依次设置，使有效载荷组合的所有排列进行测试。例如设置三个字典都是10个数，则总共有1000总匹配的模式

在攻击中生成的请求的总数是在所有定义的有效载荷的有效载荷集的数目的乘积

### Payloads Types

Burp Intruder包含以下几种attack type:

|名词         | 解释 |
|-------------|-------| 
|Simple list | 简单字典 |
|Runtime file|运行文件|
|Custom iterator|自定义迭代器|
|Character substitution|字符替换|
|Case modification| |
|Recursive grep|递归grep|
|Illegal Unicode|非法的Unicode|
|Character blocks|字符块|
|Numbers|数字|
|Dates|日期|
|Brute forcer|暴力|
|Null payloads|空的有效负载|
|haracter frobber| |
|Bit flipper|位翻转|
|Username generator|用户名生成器|
|ECB block shuffler| |
|Extension-generated|使用安装的扩展|
|Copy other payload|复制其它有效负载|

* Character substitution

配置一个字符串列表，并应用各种字符替换到每个项目。** 在密码猜测攻击非常有用 **，用来产生在字典中的单词常见的变化。 用户界面允许您配置了一些字符替换。当执行攻击，有效载荷类型工程通过逐一配置的列表项。对于每个项目，它产生一个数的有效载荷，根据所定义的取代基包括取代的字符的所有排列。例如，默认替换规则（其中包括e>3且t>7），该项目“peter”将产生以下的有效载荷：

```
peter
p3ter
pe7er
p37er
pet3r
p3t3r
pe73r
p373r
```

* Case modification

配置一个字符串列表，并应用各种情况下修改每个项目。** 密码猜测攻击非常有用 **，用来产生在字典中的单词的情况下的变化。 可以选择以下的情况下修改规则：

```
No change - 这个项目可以用不被修改。 
To lower case- 在该项目的所有字母转换为小写。 
To upper case - 在该项目的所有字母转换为大写。 
To Propername - 在该项目的第一个字母转换为大写，以及随后的字母转换为小写。 
To ProperName - 在该项目的第一个字母转换为大写，以及随后的字母都不会改变。
```

例如：

```
Peter Wiener
peter wiener
PETER WIENER
Peter wiener
```

### Payload Processing

使用各种有效载荷的处理规则和编码，操纵配置的有效载荷。 在使用有效载荷之前， 可以定义多种规则处理每个有效载荷，定义的规则按顺序执行。

Payload Processing Rules：

```
Add prefix - 添加一个文字前缀
Add suffix - 添加一个文字后缀
Match/replace - 将替换匹配特定正则表达式的有效载荷的任何部位，用一个文字字符串表示。
Substring - 提取的有效载荷的子部分中，从指定的偏移量（0-索引）和至所指定的长度开始。
Reverse substring - 对于子规则来说，最终的偏移量指定的有效载荷的末尾向后计数，并且长度从端部向后偏移计数。
Modify case - 这个修改了的有效载荷的情况下，如果适用的话。同样的选项作为的情况下修改有效载荷类型。
Encode - URL，HTML，Base64的，ASCII码或十六进制字符串构建各种平台：采用不同的计划，该编码的有效载荷。
Hash - hash
Add raw payload - 这之前或之后，在当前处理的值增加了原始负载值。它可以是有用的，例如，如果你需要提交相同的有效载荷在raw和哈希表。
Skip raw payload - 将检查是否当前处理的值匹配指定的正则表达式，如果是这样，跳过有效载荷和移动到下一个。这可能是有用的，例如，如果知道一个参数值必须有一个最小长度和要跳过的一个列表，比这更短的长度的任何值。
Invoke Burp extension - 调用一个Burp exxtension(扩展)来处理负载。扩展名必须已注册入侵者有效载荷处理器。您可以从已注册的当前加载的扩展可用的处理器列表中选择所需的处理器。
```

### Options

* Request Headers

控制在攻击Intruder(入侵者)是否更新配置请求头。

Update Content-length header(更新Content-Length头) - 此选项使Intruder(入侵者)添加或更新的Content-Length头的每个请求，与该特定请求的HTTP体的长度正确的值。此功能通常用于该插入可变长度的有效载荷送入模板的HTTP请求的主体的攻击至关重要。如果未指定正确的值，则目标服务器可能会返回一个错误，可能不完全响应请求，或者可能无限期地等待在请求继续接收数据。

Set Connection:close(设置连接：关闭) - 此选项使Intruder(入侵者)添加或更新连接头的值为“close(关闭)” 。在某些情况下（当服务器本身并不返回一个有效的Content-Length或Transfer-Encoding头） ，这个选项可以让攻击更快速地执行。

* Request Engine

设置控制用于发出HTTP请求中的Intruder(入侵者)攻击的Engine(引擎)。下列选项可用：

```
Number of threads(执行进程数) - [专业版]该选项控制并发请求数的攻击。
Number of retries on network failure(网络故障的重试次数) - 如果出现连接错误或其他网络问题，Burp会放弃和移动之前重试的请求指定的次数。测试时间歇性网络故障是常见的，所以最好是在发生故障时重试该请求了好几次。
Pause before retry(重试前暂停) - 当重试失败的请求，Burp会等待指定的时间（以毫秒为单位） ，然后重试失败以下。如果服务器被宕机，繁忙，或间歇性的问题发生，最好是等待很短的时间，然后重试。
Throttle between requests(请求之间的节流) - Burp可以在每次请求之前等待一个指定的延迟（以毫秒为单位） 。此选项很有用，以避免超载应用程序，或者是更隐蔽。或者，您可以配置一个可变延迟（与给定的初始值和增量） 。这个选项可以是有用的测试应用程序执行的会话超时时间间隔。
Start time(开始时间) - 此选项允许您配置攻击立即启动，或在指定的延迟后，或开始处于暂停状态。如果攻击被配置，将在未来的某个时刻以供将来使用被执行，或保存这些替代品可能是有用的。
```

* Attack Results

```
Store requests/responses(存储请求/响应) - 这些选项确定攻击是否会保存单个请求和响应的内容。保存请求和响应占用磁盘空间，在你的临时目录中，但可以让您在攻击期间在众目睽睽这些，如果有必要重复单个请求，并将其发送到其他Burp工具。
Make unmodified baseline request(未修改的基本请求) - 如果选择此选项，那么除了配置的攻击请求，Burp会发出模板请求设置为基值，所有有效载荷的位置。此请求将在结果表显示为项目＃ 0 。使用此选项很有用，提供一个用来比较的攻击响应基地的响应。
Use denial-of-service mode(使用拒绝服务的模式) - 如果选择此选项，那么攻击会发出请求，如正常，但不会等待处理从服务器收到任何答复。只要发出的每个请求， TCP连接将被关闭。这个功能可以被用来执行拒绝服务的应用层对脆弱的应用程序的攻击，通过重复发送该启动高负荷任务的服务器上，同时避免通过举办开放套接字等待服务器响应锁定了本地资源的请求。
Store full payloads(保存完整的有效载荷) - 如果选择此选项，Burp将存储全部有效载荷值的结果。此选项会占用额外的内存，但如果你想在运行时执行某些操作，如修改payload grep setting(有效负载值设置)，或重新发出请求与修改请求模板可能需要。
```

* Grep-Match

设置可用于包含在响应中指定的表达式标志结果的项目。对于配置列表中的每个项目，Burp会添加一个包含一个复选框，指出项目是否被发现在每个响应的新成果列。然后，您可以到组排序此列（通过单击列标题）匹配的结果相加。

除了表达式匹配的列表，下列选项可用：

```
Match(匹配类型) - 指定的表达式是否是简单的字符串或regular expressions(正则表达式)。
Case sensitive match(区分大小写的匹配) - 指定检查表达式是否应区分大小写。
Exclude HTTP headers(不包括HTTP头) - 指定的HTTP响应头是否应被排除在检查。
```

* Grep-Extrack

从攻击列表中提取有用信息

## 0x02 Extender

### 001 python environment note

1. [burp extender document][2]  
2. [burp extender api][5]  
3. [burp app store][3]  
4. [burp configuration file][4]
5. [burpextendercallback Constant Field Values][6]

Because of the way in which Jython dynamically generates Java classes, you may encounter memory problems if you load several different Python extensions, or if you unload and reload a Python extension multiple times. If this happens, you will see an error like:
java.lang.OutOfMemoryError: PermGen space 

You can avoid this problem by configuring Java to allocate more PermGen storage, by adding a `-XX:MaxPermSize` option to the command line when starting Burp. For example: `java -XX:MaxPermSize=1G -jar burp.jar`

### 002 Bapp store

Bapp store里的扩展安装之后默认是在burpsuite同目录下的`bapps`的文件夹内

### 003 interface

interface IBurpExtender: 这个接口所有的扩展都需要实现.

Interface IBurpExtenderCallbacks: 这个接口几乎是必备的。在编写扩展的过程中会经常用到。

Interface IExtensionHelpers: 这个接口是新加的。提供了编写扩展中常用的一些通用函数，比如编解码、构造请求等。这样就不需要重复造轮子了。

Interface IHttpRequestResponse: 这个接口包含了每个请求和响应的细节。在Brupsuite中的每个请求或者响应都是IHttpRequestResponse实例

### 004 插件开发

最好的方式就是在原有插件的基础上修改，这样能省很多精力。从头开发，步骤如下：

1. 包含burp的接口文件

2. 创建一个包名为burp，在里面创建BurpExtender类，实现IBurpExtender接口，这个BurpExtender类是所有接口的心脏，注意这里涉及到名字都不能改动，burp插件就这么规定的。

3. 实现唯一的接口函数

```
public void registerExtenderCallbacks(final IBurpExtenderCallbacks callbacks) {
this. callbacks = callbacks ;
}
```

通过callbacks获取核心基础库能力,像日志，请求，返回值修改等。

4. 日志接口

```
PrintWriter stdout = new PrintWriter(callbacks.getStdout(), true);
PrintWriter stderr = new PrintWriter(callbacks.getStderr(), true);
//输出到插件的output
stdout.println("Hello output");
// 输出到alerts tab
callbacks.issueAlert("Hello alerts");
//打印调用栈
e.printStackTrace(stderr)
```

有了这些日志接口就能比较好的调试代码了，如果要很好的跟踪请求的，可以在BApp Store中添加”Custom Logger”这个插件，能够记录所有的请求和返回信息


### 005 Demo

```python
"""
python extension
function: simple fuzz
"""

from burp import IBurpExtender
from burp import IIntruderPayloadGeneratorFactory
from burp import IIntruderPayloadGenerator

#from java.util import List
#from java.util import ArrayList

import random


class BurpExtender(IBurpExtender, IIntruderPayloadGeneratorFactory):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()

        callbacks.registerIntruderPayloadGeneratorFactory(self)

        return

    def getGeneratorName(self):
        return "BHP payload Generator"

    def createNewInstance(self, attack):
        return BHPFuzzer(self, attack)


class BHPFuzzer(IIntruderPayloadGenerator):
    def __init__(self, extender, attack):
        self._extender = extender
        self.__helpers = extender._helpers
        self.__attack = attack
        self.max_payloads = 10
        self.num_iterations = 0

        return

    def hasMorePayloads(self):
        if self.num_iterations == self.max_payloads:
            return False
        else:
            return True

    def getNextPayload(self, current_payload):
        """
        params:
            current_payload[list]: 列表对象，存储payload 每个字符的 ascii 码数值
        """
        # convert to string
        payload = "".join(chr(x) for x in current_payload)

        # fuzz post requesta
        payload = self.mutate_payload(payload)

        self.num_iterations += 1

        return payload

    def reset(self):
        self.num_iterations = 0
        return

    def mutate_payload(self, original_payload):
        """
        params:
            original_payload[str]:
        """
        # generate random int
        picker = random.randint(1, 3)

        # 在载荷中选取一个随机的偏移量去变形
        offset  = random.randint(0, len(original_payload)-1)
        payload = original_payload[:offset]

        # 在随机偏移位置插入sql 注入尝试
        if picker == 1:
            payload += "'"
        # xss
        elif picker == 2:
            payload += "<script>alert('BHP');</script>"
        # random repeat
        else:
            chunk_length = random.randint(len(payload[offset:]), len(payload))
            repeater = random.randint(1, 10)
            for i in range(repeater):
                payload += original_payload[offset:offset+chunk_length]

        # add remain
        payload += original_payload[offset:]

        return payload
```


## 0x06 Extender Interface

### 001 IHttpListener

`IBurpExtenderCallbacks.registerHttpListener()` to register an HTTP listener. 

监听器可以接受和修改任何 burp 工具(如: proxy, repeater)产生的 HTTP 请求和响应。

* methods

```
void processHttpMessage(int toolFlag,
                      boolean messageIsRequest,
                      IHttpRequestResponse messageInfo)
This method is invoked when an HTTP request is about to be issued, and when an HTTP response has been received.
Parameters:
toolFlag - A flag indicating the Burp tool that issued the request. Burp tool flags are defined in the IBurpExtenderCallbacks interface.
messageIsRequest - Flags whether the method is being invoked for a request or response.        
messageInfo - Details of the request / response to be processed. Extensions can call the setter methods on this object to update the current message and so modify Burp's behavior. 
```

**toolFlag [int]**

`IBurpExtenderCallbacks.getToolName(toolFlag)` 返回 burp tool 的名称， 如: Repeater, Proxy

**messageIsRequest [boolean]**  

布尔值，True is request, Flase is response

**messageInfo [IHttpRequestResponse]**

`jpython`: methods on this object 

```
c:bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.

class -> java.lang.Class
comment:
equals:None
getClass:None
getComment:None
getHighlight:None
getHost() -> unicode
getHttpService() -> burp.j7f
getPort() -> int
getProtocol() -> unicode : eg. http
getRequest():None
getResponse():None
getStatusCode() -> int
getUrl() -> java.net.URL class
hashCode:None
highlight:

host:unicode(object='') -> unicode object
unicode(string[, encoding[, errors]]) -> unicode object

Create a new Unicode object from the given encoded string.
encoding defaults to the current default string encoding.
errors can be 'strict', 'replace' or 'ignore' and defaults to 'strict'.

httpService:The most base type
notify:None
notifyAll:None

port:int(x[, base]) -> integer

Convert a string or number to an integer, if possible.  A floating point
argument will be truncated towards zero (this does not include a string
representation of a floating point number!)  When converting a string, use
the optional base.  It is an error to supply a base when converting a
non-string.  If base is zero, the proper base is guessed based on the
string content.  If the argument is outside the integer range a
long object will be returned instead.

protocol:unicode(object='') -> unicode object
unicode(string[, encoding[, errors]]) -> unicode object

Create a new Unicode object from the given encoded string.
encoding defaults to the current default string encoding.
errors can be 'strict', 'replace' or 'ignore' and defaults to 'strict'.

request:None
response:
setComment:None
setHighlight:None
setHost:None
setHttpService:None
setPort:None
setProtocol:None
setRequest:None
setResponse:None

statusCode:int(x[, base]) -> integer

Convert a string or number to an integer, if possible.  A floating point
argument will be truncated towards zero (this does not include a string
representation of a floating point number!)  When converting a string, use
the optional base.  It is an error to supply a base when converting a
non-string.  If base is zero, the proper base is guessed based on the
string content.  If the argument is outside the integer range a
long object will be returned instead.

toString() -> unicode 
url:The most base type. type(messageInfo.url) is java.net.URL,
wait:None
```

### 002 IHttpRequestResponse

This interface is used to retrieve and update details about HTTP messages. Note: The setter methods generally can only be used before the message has been processed, and not in read-only contexts. The getter methods relating to response details can only be used after the request has been issued.

**method**

* `byte[]	getRequest()`

This method is used to retrieve the request message.

* `byte[]	getResponse()`

This method is used to retrieve the response message.

* `void	setRequest(byte[] message)`

This method is used to update the request message.

* `void	setResponse(byte[] message)`

This method is used to update the response message.

### 003 IHttpService

### 004 IBurpExtenderCallbacks

**Field**

```
TOOL_COMPARER
TOOL_DECODER
TOOL_EXTENDER
TOOL_INTRUDER
TOOL_PROXY
TOOL_REPEATER
TOOL_SCANNER
TOOL_SEQUENCER
TOOL_SPIDER
TOOL_SUITE
TOOL_TARGET
```

**method**

* `java.util.List<ICookie>	getCookieJarContents()`

This method is used to retrieve the contents of Burp's session handling cookie jar

* `java.lang.String	getToolName(int toolFlag)`

This method is used to obtain the descriptive name for the Burp tool identified by the tool flag provided.

* `IHttpRequestResponse	makeHttpRequest(IHttpService httpService, byte[] request)`

This method can be used to issue HTTP requests and retrieve their responses.

* `byte[]	makeHttpRequest(java.lang.String host, int port, boolean useHttps, byte[] request)`

This method can be used to issue HTTP requests and retrieve their responses.

* `IHttpRequestResponsePersisted saveBuffersToTempFiles(IHttpRequestResponse httpRequestResponse)`

This method is used to save the request and response of an IHttpRequestResponse object to temporary files, so that they are no longer held in memory.

* `void	updateCookieJar(ICookie cookie)`

This method is used to update the contents of Burp's session handling cookie jar.


### 005 IExtensionHelpers

**method**

* `IParameter buildParameter(java.lang.String name, java.lang.String value, byte type)`

This method constructs an IParameter object based on the details provided. 
根据提供的参数，生成 IParamter 对象

* `IParameter	getRequestParameter(byte[] request, java.lang.String parameterName)`

> Returns: An IParameter object that can be queried to obtain details about the parameter, or null if the parameter was not found

This method can be used to retrieve details of a specified parameter within an HTTP request.

* `byte[]	removeParameter(byte[] request, IParameter parameter)`

This method removes a parameter from an HTTP request, and if appropriate updates the Content-Length header.

* `byte[]	updateParameter(byte[] request, IParameter parameter)`

> Returns:  A new HTTP request with the parameter updated

This method updates the value of a parameter within an HTTP request, and if appropriate updates the Content-Length header.



### 006 IParameters

**Field**

```
PARAM_BODY
PARAM_COOKIE
PARAM_JSON
PARAM_MULTIPART_ATTR
PARAM_URL
PARAM_XML
PARAM_XML_ATTR
```

**method**

* `java.lang.String	getName()`

This method is used to retrieve the parameter name.

* `byte	getType()`

This method is used to retrieve the parameter type.

* `java.lang.String	getValue()`

This method is used to retrieve the parameter value.

### 007 IRequestInfo

**method** 

* `java.util.List<IParameter>	getParameters()`

This method is used to obtain the parameters contained in the request.  
返回请求参数对象的列表， IParameter 可以是 URL，COOKIE，BODY等的参数，通过 Iparamter.getType() 确定参数类型

### 008 IResponseInfo



[1]: http://drops.wooyun.org/tools/1548
[2]: https://portswigger.net/burp/help/extender.html
[3]: https://portswigger.net/bappstore/
[4]: https://portswigger.net/burp/help/suite_burp_projects.html#configfiles
[5]: https://portswigger.net/burp/extender/api/index.html
[6]: https://portswigger.net/burp/extender/api/constant-values.html#burp.IBurpExtenderCallbacks