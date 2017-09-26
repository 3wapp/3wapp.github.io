

## 常用命令

| 命令                        | 例子                           | 解释                 |
| ------------------------- | ---------------------------- | ------------------ |
| start                     |                              |                    |
| r/run                     |                              | 运行指定的程序            |
| b/break                   |                              | 在某断代码上增加断点         |
| c/continue                |                              | 运行到下一个断点           |
| n/next                    |                              | 执行下一条语句            |
| p/print <变量名/表达式>         |                              | 查看变量的值/执行表达式       |
| s/step                    |                              | 执行下一条语句（可以进入到方法内部） |
| fin/finish                |                              | 跳出当前方法             |
| clear                     |                              | 清除下一个断点            |
| delete                    |                              | 清除断点               |
| disable                   |                              | 禁用断点               |
| enable                    |                              | 启用断点               |
| info program              |                              | 查看程序状态             |
| info locals               |                              | 列出所有当前上下文变量        |
| Info break/b              |                              | 查看断点信息             |
| info functions <fun_name> | `info functions thread*`     | 查看所有函数/特定函数(支持正则)  |
| list <lineno1, lineno2>   |                              |                    |
| bt                        |                              | 查看调用栈              |
| watch                     | `watch *(data type*)address` | 设置监视点              |
| info watchpoints          |                              |                    |
| rw/rwatch                 |                              | 设置读观察点             |
| whatis                    |                              | 查询变量或函数            |
| where                     |                              |                    |

### 条件断点设置

* `break … if cond`

  ```
  b 10 if i==101


  ```

  ​

### 分割窗口

| 命令           | 解释                   |
| ------------ | -------------------- |
| layout       | 用于分割窗口，可以一边查看代码，一边测试 |
| layout src   | 显示源代码窗口              |
| layout asm   | 显示反汇编窗口              |
| layout regs  | 显示源代码/反汇编和CPU寄存器窗口   |
| layout split | 显示源代码和反汇编窗口          |
| Ctrl + L     | 刷新窗口                 |





- delete
  用法：`delete [breakpoints num][range…]`
  delete可删除单个断点，也可删除一个断点的集合，这个集合用连续的断点号来描述。
  如: `delete 5`, `delete 1-10`

- clear
  用法: `clear` , 删除所在行的多有断点。
  ​         `clear location`, clear 删除所选定的环境中所有的断点
  ​        `clear location location`, 具体的断点

  ```
  clear list_insert         //删除函数的所有断点
  clear list.c:list_delet   //删除文件：函数的所有断点
  clear 12                  //删除行号的所有断点
  clear list.c:12           //删除文件：行号的所有断点
  ```



### 参考

* https://wizardforcel.gitbooks.io/100-gdb-tips/set-step-mode-on.html