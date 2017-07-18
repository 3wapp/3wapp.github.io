---
title: "PNG"
date: 2016-05-18 15:16
---

## png image type
 
png支持三种图像类型：索引彩色图像(index-color)，灰度图像(grayscale)，真彩色图像(true-color)

### Palette-Based

Palette-based images, also known as colormapped or index-color images, use the PLTE chunk and are supported in four pixel depths: 1, 2, 4, and 8 bits, corresponding to a maximum of 2, 4, 16, or 256 palette entries

## png 文件结构 

标准的png文件结构如下

```
png signature | png chunk | png chunk | ... | png chunk
```

## png signature

png signature 8 bytes.

```
89 50 4E 47 OD 0A 1A 0A
```

## chunk

PNG定义了两种类型的数据块，一种是称为关键数据块(critical chunk)，标准的数据块; 另一种叫做辅助数据块(ancillary chunks)，可选的数据块。关键数据块定义了3个标准数据块，每个PNG文件都必须包含它们。3个标准数据块为: IHDR， IDAT， IEND.

* PNG文件格式中的数据块

| 数据块符号 | 数据块名称  | 多数据块 | 可选否 | 位置限制 |
| --------- | ---------- | :-----: | :---: | ------- |
| IHDR	    | 文件头数据块 |	否	  |  否	 | 第一块   |
| cHRM	    | 基色和白色点数据块 | 否 |	是  | 在PLTE和IDAT之前 |
| gAMA	    | 图像γ数据块     |	否  | 是	  | 在PLTE和IDAT之前 |
| sBIT	    | 样本有效位数据块 | 否  |	是	| 在PLTE和IDAT之前 |
| PLTE	    | 调色板数据块 |	否	  | 是	 | 在IDAT之前 |
| bKGD	    | 背景颜色数据块	| 否	 | 是 |	在PLTE之后IDAT之前 |
| hIST	    | 图像直方图数据块 | 否	 | 是 |	在PLTE之后IDAT之前 |
| tRNS	    | 图像透明数据块	| 否	  | 是 |	在PLTE之后IDAT之前 |
| oFFs	    | (专用公共数据块)	| 否	  | 是 |	在IDAT之前 |
| pHYs	    | 物理像素尺寸数据块	| 否	 | 是 |	在IDAT之前 |
| sCAL	    | (专用公共数据块) |	否 |	 是  | 在IDAT之前 |
| IDAT	    | 图像数据块	     |   是 |  否  |	与其他IDAT连续 |
| tIME	    | 图像最后修改时间数据块 |	否 | 是 |	无限制  |
| tEXt	    | 文本信息数据块	| 是	  |  是	| 无限制   |
| zTXt	    | 压缩文本数据块	| 是	   | 是	| 无限制   |  
| fRAc	    | (专用公共数据块)	| 是	   | 是	| 无限制   |
| gIFg	    | (专用公共数据块) |	是  | 是	| 无限制   |
| gIFt	    | (专用公共数据块)	| 是	   | 是	| 无限制   |
| gIFx	    | (专用公共数据块) |	是  | 是	| 无限制   |
| IEND	    | 图像结束数据 |	否	    | 否 | 最后一个数据块 |

* 数据块结构

PNG文件中，每个数据块由4个部分组成

```
length | type(name) | data | CRC

length: 4 bytes， just length of the data, not include type and CRC  
type: 4 bytes, ASCII letters([A-Z,a-z])
CRC: 4bytes
```

CRC(cyclic redundancy check)域中的值是对Chunk Type Code域和Chunk Data域中的数据进行计算得到的。CRC具体算法定义在ISO 3309和ITU-T V.42中，其值按下面的CRC码生成多项式进行计算： x<sup>32</sup>+x<sup>26</sup>+x<sup>23</sup>+x<sup>22</sup>+x<sup>16</sup>+x<sup>12</sup>+x<sup>11</sup>+x<sup>10</sup>+x<sup>8</sup>+x<sup>7</sup>+x<sup>5</sup>+x<sup>4</sup>+x<sup>2</sup>+x+1

### IHDR

文件头数据块IHDR(header chunk)：它包含有PNG文件中存储的图像数据的基本信息，并要作为第一个数据块出现在PNG数据流中，而且一个PNG数据流中只能有一个文件头数据块。

文件头数据块由13字节组成，它的如下所示

| 域的名称 | 字节数 |  说明 |
| ------- | :----: | ---- |
| Width	  | 4 bytes | 图像宽度，以像素为单位 |
| Height  |	4 bytes | 图像高度，以像素为单位 |
| Bit depth	| 1 byte | 	图像深度.</br> 索引彩色图像： 1，2，4或8 </br> 灰度图像： 1，2，4，8或16 </br> 真彩色图像： 8或16 |
| ColorType | 1 byte |	颜色类型. </br> 0：灰度图像, 1，2，4，8或16 </br> 2：真彩色图像，8或16 </br> 3：索引彩色图像，1，2，4或8 </br> 4：带α通道数据的灰度图像，8或16 </br> 6：带α通道数据的真彩色图像，8或16 |
| Compression method |	1 byte	| 压缩方法(LZ77派生算法) |
| Filter method	| 1 byte |	滤波器方法 |
| Interlace method | 1 byte	| 隔行扫描方法. </br> 0：非隔行扫描 </br> 1： Adam7(由Adam M. Costello开发的7遍隔行扫描方法) |

### PLTE

调色板数据块PLTE(palette chunk)包含有与索引彩色图像(indexed-color image)相关的彩色变换数据，它仅与索引彩色图像有关，而且要放在图像数据块(image data chunk)之前。

PLTE数据块是定义图像的调色板信息，PLTE可以包含1~256个调色板信息，每一个调色板信息由3个字节组成：

| 颜色  | 字节 | 意义 |
| ---- | :---: | ---- |
| Red  | 1 byte | 0 = 黑色, 255 = 红 |
| Green | 1 byte | 0 = 黑色, 255 = 绿色 | 
| Blue | 1 byte | 0 = 黑色, 255 = 蓝色 |

因此，调色板的长度应该是3的倍数，否则，这将是一个非法的调色板。

** 颜色数 = length/3 **

对于索引图像，调色板信息是必须的，调色板的颜色索引从0开始编号，然后是1、2……，调色板的颜色数不能超过色深中规定的颜色数（如图像色深为4的时候，调色板中的颜色数不可以超过2^4=16），否则，这将导致PNG图像不合法。

真彩色图像和带α通道数据的真彩色图像也可以有调色板数据块，目的是便于非真彩色显示程序用它来量化图像数据，从而显示该图像。

### IDAT

图像数据块IDAT(image data chunk)：它存储实际的数据，在数据流中可包含多个连续顺序的图像数据块。

IDAT存放着图像真正的数据信息

### IEND

图像结束数据IEND(image trailer chunk)：它用来标记PNG文件或者数据流已经结束，并且必须要放在文件的尾部。

PNG文件的结尾12个字符应该是这样的：

```
00 00 00 00 49 45 4E 44 AE 42 60 82
```

由于数据块结构的定义，IEND数据块的长度总是0（00 00 00 00，除非人为加入信息），数据标识总是IEND（49 45 4E 44），因此，CRC码也总是AE 42 60 82


