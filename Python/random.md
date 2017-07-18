---
title: "Random"
date: 2016-04-17 09:20
---

## random 

random模块用于生成随机数

### random.random

random.random()用于生成一个0到1的随机符点数: 0 <= n < 1.0

### random.uniform

> 函数原型为：random.uniform(a, b)

用于生成一个指定范围内的随机浮点数，两个参数其中一个是上限，一个是下限。如果a > b，则生成的随机数n: b <= n <= a。如果 a < b， 则 a <= n <= b。

```
print random.uniform(10, 20)
print random.uniform(20, 10)
#---- 结果（不同机器上的结果不一样）
#18.7356606526
#12.5798298022
```

### random.randint

> 函数原型为：random.randint(a, b)，

用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b

```
print random.randint(12, 20)  #生成的随机数n: 12 <= n <= 20
print random.randint(20, 20)  #结果永远是20
# print random.randint(20, 10)  #该语句是错误的。下限必须小于上限。
```

### random.randrange

> 函数原型为：random.randrange([start], stop[, step])

从指定范围内，按指定基数递增的集合中 获取一个随机数。如：random.randrange(10, 100, 2)，结果相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数。

random.randrange(10, 100, 2)在结果上与 random.choice(range(10, 100, 2) 等效。

### random.choice

> 函数原型为：random.choice(sequence)

random.choice从序列中获取一个随机元素。参数sequence表示一个有序类型。

这里要说明 一下：sequence在python不是一种特定的类型，而是泛指一系列的类型。list, tuple, 字符串都属于sequence。

```
print random.choice("学习Python") 
print random.choice(["JGood", "is", "a", "handsome", "boy"])
print random.choice(("Tuple", "List", "Dict"))
```

### random.shuffle

> 函数原型为：random.shuffle(x[, random])

用于将一个列表中的元素打乱。如:

```
p = ["Python", "is", "powerful", "simple", "and so on..."]
random.shuffle(p)
print p
#---- 结果（不同机器上的结果可能不一样。）
# ['powerful', 'simple', 'is', 'Python', 'and so on...']
```

### random.sample

> 函数原型为：random.sample(sequence, k)

> 从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列。

```
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice = random.sample(list, 5)  #从list中随机获取5个元素，作为一个片断返回
print slice # [4, 9, 6, 10, 5]
print list  # 原有序列并没有改变。
```

## 常用随机化方法

```
def id_generator(size, chars):
    return ''.join(random.choice(chars) for _ in range(size))
    
# 随机生成由大写字母和数字组成的字符串
print id_generator(3, string.ascii_uppercase + string.digits)
>>> 'G5G74W'
```