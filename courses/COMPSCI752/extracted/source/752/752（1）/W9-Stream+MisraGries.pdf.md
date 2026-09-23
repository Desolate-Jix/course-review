# W9-Stream+MisraGries.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI752/source/752/752（1）/W9-Stream+MisraGries.pdf`
- [打开原文件](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BMisraGries.pdf)
- 原文件 SHA-256：`9bd716c23be85db3522f6c90ba6c8d0da4c0e12e96c652798409e3c623357514`
- 文件索引：F223；PDF 总页数：23
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BMisraGries.pdf#page=1)

### 原始文字层

````text
1
Misra-Gries Summary: 
Finding Heavy Hitters in Data Stream
COMPSCI 752: Big Data Management
University of Auckland
(Credits to Ninh Pham)
Parts of this material are modifications of the lecture slides from
http://mmds.org
Designed for the textbook Mining of Massive Datasets
by Jure Leskovec, Anand Rajaraman, and Jeff Ullman
Auckland, May 2025
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Misra-Gries Sum  mar   y:
               Finding  Heav y Hitters   in Data S  trea m
                                              CO    MPSC   I   7    52:   Bi  g      Dat a   Man a    ge   me   n t
                                                                Univers  ity of Auc  kland
                                                               (C red  its to Ninh Pham  )
                                            Par  ts o f th  is mat er ial  are   mo difi  cat io ns o f the  l ect ur e sl ide s from
                                                                         ht   tp  :/   /mm  ds .o  rg
                                                D esign ed  for  the t ex tbo ok   Min in g   of Massive Da ta set s
                                                   by    J ur   e Le skovec, A na  n   d  R a  j    ar    a  ma  n   ,  a  n   d  J e   ff    U   ll    ma  n
                                                                  Auck land,   May   2025                                                                      1
````

### 图片文字 OCR（en-US，待对照原页）

````text
Misra-Gries Summary:
Finding Heavy Hitters in Data Stream
COMPSCI 752: Big Data Management
University of Auckland
(Credits to Ninh Pham)
Parts of this material are modifications of the lecture slides from
h
Designed for the textbook Mining of Massive Datasets
by Jure Leskovec, Anand Rajaraman, and Jeff Ullman
Auckland, May 2025
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BMisraGries.pdf#page=2)

### 原始文字层

````text
Basic definitions
2
 Let U be a universe of size n, i.e. U = {1, 2, 3, … , n}
 Cash register model stream:
 Sequence of m elements a1, … , am where ai ∈ U
 Elements of U may or may not occur once or several times in the stream
 Finding heavy hitters in data stream (today’s lecture):
 Given a stream, finding frequent items
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Basic definitions
Let u be a universe of size n, i.e. u = {1,2 3
Cash register model stream:
Sequence of m elements al, , am where ai E u
Elements of u may or may not occur once or several times in the stream
Finding heavy hitters in data stream (today's lecture):
Given a stream, finding frequent items
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BMisraGries.pdf#page=3)

### 原始文字层

````text
Frequent items
3
 Each element of data stream is a tuple
 Given a stream of m elements a1, … , am where ai ∈ U, 
finding the most/top-k frequent items
 Example: 
 {1, 2, 1, 3, 4, 5} → f = {2, 1, 1, 1, 1}
 {1, 2, 1, 3, 1, 2, 4, 5, 2, 3} → f = {3, 3, 2, 1, 1}
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Frequent items
Each element of data stream is a tuple
Given a stream of m elements al, ...
a where ai E u,
finding the most/ top-k frequent items
Example:
1,2
1
4,
1
1}
1,
3
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BMisraGries.pdf#page=4)

### 原始文字层

````text
Applications
4
 Networking:
 Tracking the most popular source, destinations, or source-destination 
pairs (those with the highest amount of traffic)
 Web analytics:
 Tracking the most popular queries to a search engine, or the most 
popular pieces of content in a large content host
 Facts:
 Typical frequency distribution are highly skewed
 Top 10% elements have 90% of total occurrences (active rating users, 
most rated movies in Netflix)
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Applications
Networking:
Tracking the most popular source, destinations, or source-destination
pairs (those with the highest amount of traffic)
Web analytics:
Tracking the most popular queries to a search engine, or the most
popular pieces of content in a large content host
e Facts:
Typical frequency distribution are highly skewed
Top 10% elements have 90% of total occurrences (active rating users,
most rated movies in Netflix)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BMisraGries.pdf#page=5)

### 原始文字层

````text
Skewed distribution
5
 Rating distribution for 
Netflix (solid line) and 
Movielens (dashed line) 
 Items are ordered 
according to popularity 
(most popular at the 
bottom)
Cremonesi et al. RecSys’10
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Skewed distribution
Rating distribution for
Netflix (solid line) and
Movielens (dashed line)
o
o
Items are ordered
o
according to popularity
(most popular at the
bottom)
1000/0
1%
— Netflix
•Movielens
Short-head
(popular)
o
Cremonesi et al.
200/0
RecSys '
Long-tail
(unpopular)
400/0
600/0
% of ratings
800/0
1000/0
10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BMisraGries.pdf#page=6)

### 原始文字层

````text
Exact solution
6
 Create a counter for each distinct element on its first 
occurrence
 When processing an element, increase its counter
 Example:
 Stream: {1, 2, 3, 1, 4, 2, 1, 4, 2}
 Problem:
 Maintain (unknown) n counters ?
 How about maintaining k << n counters
1 2 3 4
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Exact solution
Create a counter for each distinct element on its first
occurrence
When processing an element, increase its counter
1,2
Example:
Stream :
O
Problem:
3
1
4
1
4
2
1
O
O
O
2
O
O
O
3
O
4
O
O
Maintain (unknown) n counters ?
How about maintaining k << n counters
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BMisraGries.pdf#page=7)

### 原始文字层

````text
Sampling solution
7
 Reservoir sampling:
 Reservoir sampling of size k to maintain k elements so far and the size of 
stream m
 Estimate frequency based on the reservoir summary
 As the frequency distribution are highly skewed, what occurs if some 
elements have frequency >> m/k?
 Example:
 Stream: {2, 2, 2, 4, 3, 4, 1, 1, 1, 1, 1, 1}
 Reservoir sampling with k = 3
1 2 3 4
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Sampling solution
Reservoir sampling:
Reservoir sampling of size k to maintain k elements so far and the size of
stream m
Estimate frequency based on the reservoir summary
As the frequency distribution are highly skewed, what occurs if some
elements have frequency >> m/ k?
1
O
O
O
4
3
2
Example:
Stream :
222
Reservoir sampling with k ¯
O
O
O
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BMisraGries.pdf#page=8)

### 原始文字层

````text
Misra Gries’82
8
 Process an element a:
 If we already have a counter for a, increment it
 Else, if there is no counter for a, but fewer k counters, create a counter 
for a initialized to 1
 Else, decrease all counters by 1. Remove 0 counters (key step)
 Example: {1, 2, 3, 1, 4, 2, 1, 4, 5, 2, 6}, n=6, k=3, m=11
 {1}
1
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Misra Gries'82
Process an element a:
If we already have a counter for a, increment it
Else, if there is no counter for a, but fewer k counters, create a counter
for a initialized to 1
Else, decrease all counters by 1. Remove 0 counters (key step)
Example: 1
n=6, k=3, m=11
2,
6
5,
1
O
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BMisraGries.pdf#page=9)

### 原始文字层

````text
Misra Gries’82
9
 Process an element a:
 If we already have a counter for a, increment it
 Else, if there is no counter for a, but fewer k counters, create a counter 
for a initialized to 1
 Else, decrease all counters by 1. Remove 0 counters (key step)
 Example: {1, 2, 3, 1, 4, 2, 1, 4, 5, 2, 6}, n=6, k=3, m=11
 {1, 2}
1 2
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Misra Gries'82
Process an element a:
If we already have a counter for a, increment it
Else, if there is no counter for a, but fewer k counters, create a counter
for a initialized to 1
Else, decrease all counters by 1 . Remove 0 counters (key step)
Example: 1
n=6, k=3, m=11
2,
6
5,
1
2
1
O
2
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BMisraGries.pdf#page=10)

### 原始文字层

````text
Misra Gries’82
10
 Process an element a:
 If we already have a counter for a, increment it
 Else, if there is no counter for a, but fewer k counters, create a counter 
for a initialized to 1
 Else, decrease all counters by 1. Remove 0 counters (key step)
 Example: {1, 2, 3, 1, 4, 2, 1, 4, 5, 2, 6}, n=6, k=3, m=11
 {1, 2, 3}
1 2 3
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Misra Gries'82
Process an element a:
If we already have a counter for a, increment it
Else, if there is no counter for a, but fewer k counters, create a counter
for a initialized to 1
Else, decrease all counters by 1 . Remove 0 counters (key step)
Example: 1
n=6, k=3, m=11
2,
6
5,
1
23
1
O
2
O
3
O
10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BMisraGries.pdf#page=11)

### 原始文字层

````text
Misra Gries’82
11
 Process an element a:
 If we already have a counter for a, increment it
 Else, if there is no counter for a, but fewer k counters, create a counter 
for a initialized to 1
 Else, decrease all counters by 1. Remove 0 counters (key step)
 Example: {1, 2, 3, 1, 4, 2, 1, 4, 5, 2, 6}, n=6, k=3, m=11
 {1, 2, 3, 1}
1 2 3
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Misra Gries'82
Process an element a:
If we already have a counter for a, increment it
Else, if there is no counter for a, but fewer k counters, create a counter
for a initialized to 1
Else, decrease all counters by 1 . Remove 0 counters (key step)
Example: 1
n=6, k=3, m=11
2,
6
5,
1
23
1
1
O
O
2
O
3
O
11
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BMisraGries.pdf#page=12)

### 原始文字层

````text
Misra Gries’82
12
 Process an element a:
 If we already have a counter for a, increment it
 Else, if there is no counter for a, but fewer k counters, create a counter 
for a initialized to 1
 Else, decrease all counters by 1. Remove 0 counters (key step)
 Example: {1, 2, 3, 1, 4, 2, 1, 4, 5, 2, 6}, n=6, k=3, m=11
 {1, 2, 3, 1, 4}
1 2 3
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Misra Gries'82
Process an element a:
If we already have a counter for a, increment it
Else, if there is no counter for a, but fewer k counters, create a counter
for a initialized to 1
Else, decrease all counters by 1 . Remove 0 counters (key step)
Example: 1
2
1
0
n=6, k=3, m=11
2,
6
5,
12
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BMisraGries.pdf#page=13)

### 原始文字层

````text
Misra Gries’82
13
 Process an element a:
 If we already have a counter for a, increment it
 Else, if there is no counter for a, but fewer k counters, create a counter 
for a initialized to 1
 Else, decrease all counters by 1. Remove 0 counters (key step)
 Example: {1, 2, 3, 1, 4, 2, 1, 4, 5, 2, 6}, n=6, k=3, m=11
 {1, 2, 3, 1, 4, 2}
1 2 3 2
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Misra Gries'82
Process an element a:
If we already have a counter for a, increment it
Else, if there is no counter for a, but fewer k counters, create a counter
for a initialized to 1
Else, decrease all counters by 1 . Remove 0 counters (key step)
Example: 1
2
1
0
S
n=6, k=3, m=11
2,
6
5,
2
2
O
13
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BMisraGries.pdf#page=14)

### 原始文字层

````text
Misra Gries’82
14
 Process an element a:
 If we already have a counter for a, increment it
 Else, if there is no counter for a, but fewer k counters, create a counter 
for a initialized to 1
 Else, decrease all counters by 1. Remove 0 counters (key step)
 Example: {1, 2, 3, 1, 4, 2, 1, 4, 5, 2, 6}, n=6, k=3, m=11
 {1, 2, 3, 1, 4, 2, 1}
1 2 3 2
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Misra Gries'82
Process an element a:
If we already have a counter for a, increment it
Else, if there is no counter for a, but fewer k counters, create a counter
for a initialized to 1
Else, decrease all counters by 1 . Remove 0 counters (key step)
Example: 1
2
1
0
O
n=6, k=3, m=11
2,
6
5,
2
2
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BMisraGries.pdf#page=15)

### 原始文字层

````text
Misra Gries’82
15
 Process an element a:
 If we already have a counter for a, increment it
 Else, if there is no counter for a, but fewer k counters, create a counter 
for a initialized to 1
 Else, decrease all counters by 1. Remove 0 counters (key step)
 Example: {1, 2, 3, 1, 4, 2, 1, 4, 5, 2, 6}, n=6, k=3, m=11
 {1, 2, 3, 1, 4, 2, 1, 4}
1 2 3 2 4
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Misra Gries'82
Process an element a:
If we already have a counter for a, increment it
Else, if there is no counter for a, but fewer k counters, create a counter
for a initialized to 1
Else, decrease all counters by 1 . Remove 0 counters (key step)
Example: 1
2
1
2
0
O
1
1
4
O
n=6, k=3, m=11
4
2,
6
5,
4
15
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BMisraGries.pdf#page=16)

### 原始文字层

````text
Misra Gries’82
16
 Process an element a:
 If we already have a counter for a, increment it
 Else, if there is no counter for a, but fewer k counters, create a counter 
for a initialized to 1
 Else, decrease all counters by 1. Remove 0 counters (key step)
 Example: {1, 2, 3, 1, 4, 2, 1, 4, 5, 2, 6}, n=6, k=3, m=11
 {1, 2, 3, 1, 4, 2, 1, 4, 5}
1 2 3 2 4
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Misra Gries'82
Process an element a:
If we already have a counter for a, increment it
Else, if there is no counter for a, but fewer k counters, create a counter
for a initialized to 1
Else, decrease all counters by 1 . Remove 0 counters (key step)
Example: 1
2
1
2
0
4
4
n=6, k=3, m=11
2,
6
5,
5}
16
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BMisraGries.pdf#page=17)

### 原始文字层

````text
Misra Gries’82
17
 Process an element a:
 If we already have a counter for a, increment it
 Else, if there is no counter for a, but fewer k counters, create a counter 
for a initialized to 1
 Else, decrease all counters by 1. Remove 0 counters (key step)
 Example: {1, 2 ,3, 1, 4, 2, 1, 4, 5, 2, 6}, n=6, k=3, m=11
 {1, 2, 3, 1, 4, 2, 1, 4, 5, 2}
1 2 3 2 4 2
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Misra Gries'82
Process an element a:
If we already have a counter for a, increment it
Else, if there is no counter for a, but fewer k counters, create a counter
for a initialized to 1
Else, decrease all counters by 1 . Remove 0 counters (key step)
Example: 1
1
2
0
2
n=6, k=3, m=11
6
42 1 , 4
2
17
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 18 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BMisraGries.pdf#page=18)

### 原始文字层

````text
Misra Gries’82
18
 Process an element a:
 If we already have a counter for a, increment it
 Else, if there is no counter for a, but fewer k counters, create a counter 
for a initialized to 1
 Else, decrease all counters by 1. Remove 0 counters (key step)
 Example: {1, 2 ,3, 1, 4, 2, 1, 4, 5, 2, 6}, n=6, k=3, m=11
 {1, 2, 3, 1, 4, 2, 1, 4, 5, 2 , 6}
1 2 3 2 4 2 6
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Misra Gries'82
Process an element a:
If we already have a counter for a, increment it
Else, if there is no counter for a, but fewer k counters, create a counter
for a initialized to 1
Else, decrease all counters by 1 . Remove 0 counters (key step)
Example: 1
1
2
0
2
n=6, k=3, m=11
6
42 1 , 4
2
6
5,
6
18
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 19 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BMisraGries.pdf#page=19)

### 原始文字层

````text
Misra Gries’82
19
 Process an element a:
 If we already have a counter for a, increment it
 Else, if there is no counter for a, but fewer k counters, create a counter 
for a initialized to 1
 Else, decrease all counters by 1. Remove 0 counters (key step)
 Query: How many times the element a occurred?
 If we have a counter for a, return its value
 Else, return 0
 Observation:We always under-estimate the frequency!
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Misra Gries'82
Process an element a:
If we already have a counter for a, increment it
Else, if there is no counter for a, but fewer k counters, create a counter
for a initialized to 1
Else, decrease all counters by 1. Remove 0 counters (key step)
Query: How many times the element a occurred?
If
we have a counter for a, return its value
Else, return O
Observation: We always under-estimate the frequency!
19
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 20 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BMisraGries.pdf#page=20)

### 原始文字层

````text
Why it works?
20
 Question:
 How many decrements to a particular a can we have?
 How many decrement step can we have?
 Answer:
 The number of elements in stream: m
 The number of elements in the summary: m’
 Given a does not occur in the summary, one decrement step takes out k
items and not count a. That is k + 1 “uncounted” occurrences
 There is (m – m’) / (k + 1) decrement steps
 Estimate is smaller than exact count by at most 𝒎 – 𝒎’
𝒌 + 𝟏
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Why it works?
Question:
How many decrements to a particular a can we have?
How many decrement step can we have?
Answer:
The number of elements in stream: m
The number of elements in the summary: m'
Given a does not occur in the summary, one decrement step takes out k
items and not count a. That is k + 1 "uncounted" occurrences
There is (m — m') / (k + 1) decrement steps
Estimate is smaller than exact count by at most
20
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 21 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BMisraGries.pdf#page=21)

### 原始文字层

````text
Why it works?
21
 Estimate is smaller than exact count by at most 𝒎 – 𝒎’
𝒌 + 𝟏
 We can find the most frequent items if their frequencies > 𝒎 – 𝒎’
𝒌 + 𝟏
 We get good estimate for a if its frequency >> 𝒎 – 𝒎’
𝒌 + 𝟏
 Error bound:
 Inversely proportional to k, hence larger k gives better accuracy
 Can be computed by knowing k and m’, and tracking m
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Why it works?
Estimate is smaller than exact count by at most
We can find the most frequent items if their frequencies >
We get good estimate for a if its frequency >>
Error bound:
Inversely proportional to k, hence larger k gives better accuracy
Can be computed by knowing k and m' and tracking m
21
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 22 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BMisraGries.pdf#page=22)

### 原始文字层

````text
Why it works?
22
 Misra Gries works because typical frequency distributions 
have few very popular elements “Zipf law”
Carl Colglazier
GitHub
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Why it works?
Misra Gries works because typical frequency distributions
have few very popular elements "Zipf law"
YouTube views per video through 2014.
Actual video views Expected views under Zipf's law
25000 -
20000 -
15000 -
0)
10000 -
5000 -
Carl Colglazier
GitHub
o-
10
20
Rank (by views)
30
22
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 23 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BMisraGries.pdf#page=23)

### 原始文字层

````text
Homework
23
 Implement the Misra-Gries algorithm on the dataset from 
https://archive.ics.uci.edu/ml/datasets/bag+of+words, 
using word tokens from vocal.kos.text:
 Description: Each line (doc ID, word ID, freq.) as a stream tuple
 Query: What are the top-1 and top-10 frequent word ID?
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Homework
Implement the Misra-Gries algorithm on the dataset from
https://archive.ics.uci.edu/ml/datasets/bag + of + words
using word tokens from vocal.kos.text:
Description: Each line (doc ID, word ID, freq.) as a stream tuple
Query: What are the top-I and top-10 frequent word ID?
23
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

