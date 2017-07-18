
## celery

## celeryconfig

[4.0.0 configuration](http://docs.celeryproject.org/en/master/userguide/configuration.html)

* params

```
# Broker settings
BROKER_URL = 'redis://localhost:6379/1'

# backend, Result store settings.
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'

REDIS_CONNECT_RETRY = True

# List of modules to import when celery starts.
CELERY_IMPORTS = (
    "data_dump.tasks",
    )

# Worker settings
# If you're doing mostly I/O you can have more processes,
# but if mostly spending CPU, try to keep it close to the
# number of CPUs on your machine. If not set, the number of CPUs/cores
# available will be used.
CELERYD_CONCURRENCY = 10
# CELERYD_LOG_FILE = "celeryd.log"
# CELERYD_LOG_LEVEL = "INFO"

# Where to chdir at start.
CELERYD_CHDIR="/xxx/aaa"

# Extra arguments to celeryd
# CELERYD_OPTS="--time-limit=300 --concurrency=1"
CELERYD_OPTS="--time-limit=14000 -S -E -B"  # load celerymon, celerybeat, celeryevent

# create log and daemon process
#CELERYD_LOG_FILE="/tmp/celery.log"
#CELERYD_PID_FILE="/tmp/celery.pid"

# 默认所有格式为 json
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']

# 某个程序中出现的队列，在broker中不存在，则立刻创建它  
CELERY_CREATE_MISSING_QUEUES = True  

# 每个worker最多执行万100个任务就会被销毁，可防止内存泄露  
CELERYD_MAX_TASKS_PER_CHILD = 100

# 单个任务的运行时间不超过此值，否则会被SIGKILL 信号杀死   
CELERYD_TASK_TIME_LIMIT = 60    

# 任务发出后，经过一段时间还未收到acknowledge , 就将任务重新交给其他worker执行 
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 90}


# 定时任务  
CELERYBEAT_SCHEDULE = {  
    'msg_notify': {  
        'task': 'async_task.notify.msg_notify',  
        'schedule': timedelta(seconds=10),  
        #'args': (redis_db),  
        'options' : {'queue':'my_period_task'}  
    },  
    'report_result': {  
        'task': 'async_task.tasks.report_result',  
        'schedule': timedelta(seconds=10),  
      #'args': (redis_db),  
        'options' : {'queue':'my_period_task'}  
    },  
    #'report_retry': {  
    #    'task': 'async_task.tasks.report_retry',  
    #    'schedule': timedelta(seconds=60),  
    #    'options' : {'queue':'my_period_task'}  
    #},  
  
}  
```

* sample

```
import os
import sys

from kombu import Exchange, Queue
from datetime import timedelta
from config import cfg

import log

log.initLog(cfg.log)

sys.path.append(os.path.dirname(os.path.basename(__file__)))


_redis = cfg.redis
_email = cfg.email

REDIS_SERVER = "redis://:%s@%s:%d/%d" %(_redis['password'],_redis['host'],\
                                                    _redis['port'],_redis['db'])

BROKER_URL = REDIS_SERVER

BROKER_POOL_LIMIT = 200

BROKER_CONNECTION_TIMEOUT = 5
BROKER_CONNECTION_RETRY = True
BROKER_CONNECTION_MAX_RETRIES = 100

BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600*12} # 12 hour

# BROKER_HEARTBEAT
# BROKER_HEARTBEAT_CHECKRATE


# Only AMQP broker support using ssl  
BROKER_USE_SSL = False 


CELERY_RESULT_BACKEND = REDIS_SERVER

CELERY_TIMEZONE = "Asia/Shanghai"

CELERY_TASK_RESULT_EXPIRES = 3600*24  # 1 day

CELERYD_CONCURRENCY = 6

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERY_CACHE_BACKEND = "memory"

CELERY_TASK_PUBLISH_RETRY = True
CELERY_TASK_PUBLISH_RETRY_POLICY = {
    'max_retries': 3,
    'interval_start': 0,        # wait between retries
    'interval_step': 30,
    'interval_max': 60,
}


CELERYD_POOL = "processes"


CELERY_IMPORTS = (
    'tasks',
    'urlscan.tasks',
    'codescan.tasks',
    'webscan.tasks'
)


#################################################
#: Queue and Route related configuration
#################################################

CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'

CELERY_QUEUES = (
        Queue('errorhandler',Exchange('errorhandler'),routing_key='errorhandler'),
        Queue('urlscan.log',Exchange('urlscan.log'),routing_key='urlscan.log'),
        Queue('urlscan.spider',Exchange('urlscan.spider'),routing_key='urlscan.spider'),
        Queue('webscan',Exchange('webscan'),routing_key='webscan'),
        Queue('codescan',Exchange('codescan'),routing_key='codescan'),

    )



CELERY_ROUTES = ({
    'webscan.errorhandler': {
        'queue':'errorhandler',
        'routing_key':'errorhandler'
    }},

    {
    'webscan.urlscan.spider': {
        'queue': 'urlscan.spider',
        'routing_key': 'urlscan.spider'
    }},

    {
    'webscan.urlscan.logextract': {
        'queue': 'urlscan.log',
        'routing_key': 'urlscan.log'
    }},

    {
    'webscan.codescan': {
        'queue': 'codescan',
        'routing_key': 'codescan'
    }},

    {
    'webscan.webscan': {
        'queue': 'webscan',
        'routing_key': 'webscan'
    }},
)



#################################################
#: Events configuration, Event can be used for monitor by flower
#################################################
CELERY_SEND_EVENTS = True
CELERY_SEND_TASK_SENT_EVENT = True



#################################################
#: Log configuration
#################################################
CELERYD_HIJACK_ROOT_LOGGER = True
CELERYD_LOG_COLOR = True
CELERYD_LOG_FORMAT = "[%(asctime)s <%(processName)s>] %(levelname)s: %(message)s"
CELERYD_TASK_LOG_FORMAT = "[%(asctime)s <%(task_name)s %(task_id)s>] %(levelname)s: %(message)s"
CELERY_REDIRECT_STDOUTS = True


#################################################
#: E-mail configuration, Send mail to admin when task failed.
#################################################
CELERY_SEND_TASK_ERROR_EMAILS = True

ADMINS = (
    ("kenshin", "kenshin.acs@gmail.com"),
)

SERVER_EMAIL = _email['SERVER_EMAIL']

EMAIL_HOST = _email['EMAIL_HOST']
EMAIL_PORT = _email['EMAIL_PORT']
EMAIL_HOST_USER = _email['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = _email['EMAIL_HOST_PASSWORD']
```