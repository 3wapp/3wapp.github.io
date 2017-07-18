---
title: "Encode and Decode"
date: 2016-05-11 11:45
---

# JS

## JSFuck

### encode

[jsfuck.com][1]

### decode

chrome(firefox) console input follow

```
alert(/.+(?=\n})/.exec(eval(prompt().slice(0,-2))))
```

or

```
alert(/\n(.+)/.exec(eval(prompt().slice(0,-2)))[1])
```

运行，然后在弹出框中输入 jsfuck 编码的代码，即可得到解码后的代码

解析：

```
alert(
    /\n(.+)/.exec(                 // regex to extract code from inside outer function braces {}
        eval(prompt().slice(0,-2)) // remove the final set of parens () and evaluate the code
                                   // this results in a function, which will be converted to a string as 'exec' expects a string
    )[1]                           // get the first capture group
)
```





[1]: http://www.jsfuck.com/