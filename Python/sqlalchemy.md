## SQLAlchemy

install: `pip install sqlalchemy`

## 引擎

> sqlalchemy.create_engine(*args, **kwargs)

`create_engine` 通常用一个url字符串作为第一个参数, 表示连接信息,   
格式为: `dialect[+driver]://user:password@host/dbname[?key=value..]`   
即 `数据库类型[+数据库驱动名称]://用户名:口令@机器地址:端口号/数据库名[?查询参数]`


* sqlite

```python
from sqlalchemy import create_engine
from sqlalchemy import MetaData

engine = create_engine('sqlite:///test.db', echo=True)
metadata = MetaData(engine)
```

test.db是相对路径, 也可写成：`sqlite:///./test.db`, 创建MetaData时绑定了引擎：`metadata = MetaData(engine)`, 后续调用 (如 MetaData.create_all()，Table.create()，等等) 就不用指定引擎了 