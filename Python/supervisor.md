

## config

* program

```
; 管理单个进程的配置，可创建多个，下面是所有可能的配置选项
;[program:theprogramname]
;command=/bin/cat              ; 启动进程的命令 使用相对路径，可以加参数
;process_name=%(program_name)s ; 进程名称 表达式 (默认 %(program_name)s)
;numprocs=1                    ; 进程数目 (def 1)
;directory=/tmp                ; 执行命令所在的目录 (def no cwd)
;umask=022                     ; 进程默认权限 (default None)
;priority=999                  ; 进程启动相对优先权 (default 999)
;autostart=true                ; 跟随supervisor启动时启动 (default: true)
;autorestart=unexpected        ; 计划启动 (default: unexpected)
;startsecs=1                   ; 延时启动 (def. 1)
;startretries=3                ; 最多连续启动失败 (default 3)
;exitcodes=0,2                 ; 进程结束代码 (default 0,2)
;stopsignal=QUIT               ; signal used to kill process (default TERM)
;stopwaitsecs=10               ; 最长结束等待时间，否则使用 SIGKILL (default 10)
;stopasgroup=false             ; 是否想UNIX进程组发送结束信号 (default false)
;killasgroup=false             ; SIGKILL UNIX 进程组 (def false)
;user=chrism                   ; 设置启动此程序的用户
;redirect_stderr=true          ; 重定向程序的标准错误到标准输出 (default false)
;stdout_logfile=/a/path        ; 标准输出的日志路径, NONE for none; default AUTO
;stdout_logfile_maxbytes=1MB   ; 日志文件最大值，否则循环写入 (default 50MB)
;stdout_logfile_backups=10     ; 标准输出日志备份数目 (default 10)
;stdout_capture_maxbytes=1MB   ; number of bytes in 'capturemode' (default 0)
;stdout_events_enabled=false   ; emit events on stdout writes (default false)
;stderr_logfile=/a/path        ; 标准错误输出日志路径, NONE for none; default AUTO
;stderr_logfile_maxbytes=1MB   ; 日志文件最大值，否则循环写入 (default 50MB)
;stderr_logfile_backups=10     ; 标准错误日志备份数目 (default 10)
;stderr_capture_maxbytes=1MB   ; number of bytes in 'capturemode' (default 0)
;stderr_events_enabled=false   ; emit events on stderr writes (default false)
;environment=A="1",B="2"       ; 进程附加环境 (def no adds)
;serverurl=AUTO                ; override serverurl computation (childutils)
```