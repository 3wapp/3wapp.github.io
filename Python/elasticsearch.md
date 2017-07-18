# Elasticsearch python api

* [elasticsearch-py 2.4.0](http://elasticsearch-py.readthedocs.io/en/2.4.0/api.html)

    Official Python low-level client for Elasticsearch

* [elasticsearch-dsl-py](http://elasticsearch-dsl.readthedocs.io/en/latest/)

    High level Python client for Elasticsearch

* [ES权威指南--翻译](http://es.xiaoleilu.com/)

## Elasticsearch 

### 索引

在Elasticsearch中存储数据的行为就叫做索引(indexing)，不过在索引之前，我们需要明确数据应该存储在哪里。

在Elasticsearch中，文档归属于一种类型(type),而这些类型存在于索引(index)中，我们可以画一些简单的对比图来类比传统关系型数据库：

* `Relational DB -> Databases -> Tables -> Rows -> Columns`
* `Elasticsearch -> Indices   -> Types  -> Documents -> Fields`


Elasticsearch集群可以包含多个索引(indices)（数据库），每一个索引可以包含多个类型(types)（表），每一个类型包含多个文档(documents)（行），然后每个文档包含多个字段(Fields)（列）

## 特征

* 转化基础的python数据结构到json数据结构，或者把json的数据结构转化成python的数据结构(由于性能的原因，datetimes类型并没有转化)
* 自动发现集群结点可配置
* 持久连接
* 从可知的结点中负载均衡（通过pluggable selection strategy）
* 连接失败处罚(基于时间，也就是说连接失败了不会再次尝试连接直到timeout)
* 线程安全
* pluggable architecture

## install

pypi: `pip install elasticsearch`,  `pip install elasticsearch-dsl`

## elasticsearch-py usage

### 建立ES连接

```python
es = Elasticsearch()

es = Elasticsearch([{'host':'10.10.13.12', 'port':9200}])
```

### 增

* index

> index(*args, **kwargs)

创建或更新`一条`JSON文档类型的索引

|parameters| note|
| ---- | ---- |
|index | The name of the index |
|doc_type | The type of the document, 数据类型 |
|body | The document, 具体的数据 |
|id | Document ID |
|consistency | Explicit write consistency setting for the operation, valid choices are: ‘one’, ‘quorum’, ‘all’ |
|op_type | Explicit operation type, default ‘index’, valid choices are: ‘index’, ‘create’ |
|parent | ID of the parent document |
|refresh | Refresh the index after performing the operation |
|routing | Specific routing value |
|timeout | Explicit operation timeout |
|timestamp | Explicit timestamp for the document |
|ttl | Expiration time for the document |
|version | Explicit version number for concurrency control |
|version_type | Specific version type, valid choices are: ‘internal’, ‘external’, ‘external_gte’, ‘force’|

```
建议index设置为时间或时间的组合体，如log_2015_11_29
数据类型即当前索引下数据的分类名称，可以把当前的数据按照不同的类型分类，同时也方便了查询，查询时可以很方便的过滤需要的类型
```

* create

创建`一条`JSON文档类型的索引, 调用`index(..., op_type=’create’)`

### 查

* search

> search(*args, **kwargs)

| parameters | note |
| --- | ---- |
|index|索引名 |
|q|查询指定匹配 使用Lucene查询语法 |
|from_|查询起始点  默认0 |
|doc_type|文档类型 |
|size|指定查询条数 默认10 |
|field|指定字段 逗号分隔 |
|sort|排序  字段：asc/desc |
|body|使用 Query DSL |
|scroll|滚动查询 |


## Query DSL


### range 过滤器查询范围

gt: > 大于

lt: < 小于

gte: >= 大于或等于

lte: <= 小于或等于

```python
"range":{
    "money":{
        "gt":20,
        "lt":40
    }
}
```

### bool 组合过滤器

must：所有分句都必须匹配，与 AND 相同。

must_not：所有分句都必须不匹配，与 NOT 相同。

should：至少有一个分句匹配，与 OR 相同。

```python
{
    "bool":{
      "must":[],
      "should":[],
      "must_not":[],
    }
}
```

### term 过滤器

term单过滤

```python
{
    "terms":{
      "money":20
    }
}
```

terms复数版本，允许多个匹配条件

```python
{
    "terms":{
      "money": [20,30]
    }
}
```

### match查询

match 精确匹配

```python
{
    "match":{
      "email":"123456@qq.com"
    }
}
```

multi_match 多字段搜索

```python
{
    "multi_match":{
      "query":"11",
      "fields":["Tr","Tq"]
    }
}
```

### demo

* 获取最近一小时的数据

```python
{'query':
    {'filtered':
        {'filter':
            {'range':
                {'@timestamp':{'gt':'now-1h'}}
            }
        }
    }
}
```

* 条件过滤查询

```python
{
    "query":{
        "filtered":{
            "query":{"match":{"http_status_code":500}},
            "filter":{"term":{"server_name":"vip03"}}
        }
    }
}
```

* Terms Facet 单字段统计

```python
{'facets':
  {'stat':
    {'terms':
      {'field':'http_status_code',
        'order':'count',
    'size':50}
    }
  },
  'size':0
}
```

* 一次统计多个字段

```python
{'facets':
  {'cip':
    {'terms':
      {'fields':['client_ip']}},
        'status_facets':{'terms':{'fields':['http_status_code'],
        'order':'term',
        'size':50}}},
    'query':{'query_string':{'query':'*'}},
  'size':0
}
```

* 多个字段一起统计

```python
{'facets':
  {'tag':
    {'terms':
      {'fields':['http_status_code','client_ip'],
        'size':10
       }
    }
  },
  'query':
    {'match_all':{}},
  'size':0
}
```
