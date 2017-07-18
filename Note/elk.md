---
title: "ELK"
date: 2016-04-11 21:08
---

## 简介

[ELK 中文指南][8]

ELK 是 Elasticsearch、Logstash、Kibana 三个开源软件的组合

### ElasticSearch

Elasticsearch是一个基于Apache Lucene(TM)的开源的实时分布式搜索和分析引擎,可以快速处理大数据，用于全文搜索、结构化搜索、分析以及将这三者混合使用。

[Elasticsearch download][1]

[Elasticsearch install and running][2]

```
$ cd elasticsearch-2.3.1
$ bin/elasticsearch

# browser http://locaolhost:9200

# get the following output
{
  "name" : "X-23",
  "cluster_name" : "elasticsearch",
  "version" : {
    "number" : "2.3.1",
    "build_hash" : "bd980929010aef404e7cb0843e61d0665269fc39",
    "build_timestamp" : "2016-04-04T12:25:05Z",
    "build_snapshot" : false,
    "lucene_version" : "5.5.0"
  },
  "tagline" : "You Know, for Search"
}
```

### Logstash

[logstash download][6]

[logstash document][7]

run:

```
../logstash-2.3.1$ bin/logstash -e 'input{stdin{}}output{stdout{codec=>rubydebug}}'
Settings: Default pipeline workers: 4
Pipeline main started
hello world
{
       "message" => "hello world",
      "@version" => "1",
    "@timestamp" => "2016-04-13T03:37:00.404Z",
          "host" => "kali"
}
```

终端输入 Hello World，回车，然后看看会返回结果, 如上所示

### Kibana

[kibana download][4]

[kibana install and running][5]

download tar.gz and extract

```
cd kibana-4.5.0-linux-x64/bin
./kibana 

# browser
http://localhost:5601
```

install and run app sense

```
cd kibana-4.5.0-linux-x64/bin
./kibana plugin --install elastic/sense
./bin/kibana
```

Open Sense your web browser by going to http://localhost:5601/app/sense

### ELK

```
### Elasticsearch ###
cd elasticsearch-2.3.1
bin/elasticsearch


### logstash ###
cd logstash-2.3.1
mkdir conf 
mkdir /var/opt/logs
echo "hello" > /var/opt/logs/test.log
vim conf/logstash-indexer.conf

input{                                                                          
    file {
        path => ["/var/opt/logs/test.log"]
    }                                                                    
}                                                                               
                                                                                
output {                                                                        
    elasticsearch {                                                             
        hosts => ["localhost:9200"]                                             
    }                                                                           
                                                                                
    stdout {                                                                    
        codec => rubydebug                                                      
    }                                                                           
} 

bin/logstash -f conf/logstash-indexer.conf


### Kibana ###
cd kibana-4.5.0-linux-x64/
vim config/kibana.yml

## 更改如下 ##
# The Elasticsearch instance to use for all your queries.                  
  15 elasticsearch.url: "http://localhost:9200"

bin/kibana


### browser ### 
http://localhost:5601  
  
```

```
# Elasticseatch 后台进程运行
nohup ./elasticsearch & 
```

新建索引配置文件logstash-indexer.conf，input{file{...}}部分指定的是日志文件的位置（可以多个文件）。output部分则是表示将日志文件的内容保存到elasticsearch，这里hosts对应的是一个数组，可以设置多个elasticsearch主机，相当于一份日志文件的内容，可以保存到多个elasticsearch中。stdout中 codec => rubydebug ，方便部署时验证是否正常运行，验证通过后，可以去掉。


[1]: https://www.elastic.co/downloads/elasticsearch
[2]: https://www.elastic.co/guide/en/elasticsearch/reference/current/_installation.html

[4]: https://www.elastic.co/downloads/kibana
[5]: https://www.elastic.co/guide/en/kibana/current/setup.html

[6]: https://www.elastic.co/downloads/logstash
[7]: https://www.elastic.co/guide/en/logstash/current/index.html

[8]: http://kibana.logstash.es/content/