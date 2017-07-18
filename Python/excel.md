---
title: "Excel"
date: 2016-07-01 21:36
---


## 0x00 简介

Python第三方库操作Excel

* xlrd (Excel Reader): 读

支持Python 2.x和3.x，支持XLS和XLSX文件读取。

* xlwt (Excel Writer): 写

仅支持Python 2.x，仅支持写XLS。

* xlutils: 更多高级操作，依赖前2个库

仅支持Python 2.x

## 0x01 xlrd

[xlrd documet][1]

```
# 导入模块
import xlrd

# 打开Excel文件读取数据

rb = xlrd.open_workbook('excelFile.xls')

# 获取一个工作表
sheet = rb.sheets()[0]               #通过索引顺序获取
sheet = rb.sheet_by_index(0)         #通过索引顺序获取
sheet = rb.sheet_by_name(u'Sheet1')  #通过名称获取
 
# 获取整行和整列的值（数组）
sheet.row_values(i)
sheet.col_values(i)

# 工作表名字 
sheet.name

#获取行数和列数
nrows = sheet.nrows
ncols = sheet.ncols
       
# 循环行列表数据
for i in range(nrows ):
    print sheet.row_values(i)
 
# 单元格
cell_A1 = sheet.cell(0,0).value
cell_C4 = sheet.cell(2,3).value
 
# 使用行列索引
cell_A1 = sheet.row(0)[0].value
cell_A2 = sheet.col(1)[0].value

# 返回行单元格类型列表，0：None，1：string，2：Number，3：date，4：bool，5：error
ws.row_types(int)  
```

## 0x02 xlwt

[xlwt document][2]

```
import xlwt
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('sheet 1')

这样表单就被创建了,写入数据也很简单：
# indexing is zero based, row then column
sheet.write(0, 1, 'test text')
wbk.save('demo.xls')

# 根据序号激活工作表
ws = wb.get_sheet(int)

# 写入并且合并单元格，(x，y)是开始单元格，(m,n)是结束单元格
ws.write_merge(x, m, y, n, value/Formula[, sytle]) 
```

## 0x03 xlutils

[xlutils document][3]

[修改Excel文件][4]

```
# xlutils.copy.copy 这个模块是用来在xlrd和xlwt之间嫁接桥梁的，可以说是依赖xlrd的，因为必须要初始化xlrd的Book类才能复制。 
wb = xlutils.copy.copy(rwb)   
ws.write(row,col,value)  
wb.save('WorkBookName') 
```

[1]: http://xlrd.readthedocs.io/en/latest/
[2]: http://xlwt.readthedocs.io/en/latest/
[3]: http://xlutils.readthedocs.io/en/latest/
[4]: http://blog.csdn.net/tianzhu123/article/details/7225809