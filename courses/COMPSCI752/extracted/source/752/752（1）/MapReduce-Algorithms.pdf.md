# MapReduce-Algorithms.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI752/source/752/752（1）/MapReduce-Algorithms.pdf`
- [打开原文件](../../../../source/752/752%EF%BC%881%EF%BC%89/MapReduce-Algorithms.pdf)
- 原文件 SHA-256：`23488af0cc442f0ac50ca49dce847d83b9a42c088f82752035e19e62963fb19c`
- 文件索引：F217；PDF 总页数：20
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/MapReduce-Algorithms.pdf#page=1)

### 原始文字层

````text
1
MapReduce
COMPCSI 752: Big Data Management
University of Auckland
Credits to Ninh Pham for the Slides
Slides are collected and edited from http://webdam.inria.fr/Jorge/index9213.html
and https://homepages.cwi.nl/~boncz/bads/mapreduce.shtml
Auckland, May 2025
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Map Reduc e
                            C OMPC SI  7 5 2: B ig   Data  Ma nag  ement
                                            Un iver   sity   o f Auc  kland
                                   C red it  s to  Ni  nh   Pham f  or   the Sl id es
       Sl ides are c  oll ec  ted   and   ed  ited   fro  m http  :/ /webdam.inr  ia.fr/ Jorge/ index921  3.html
                    and http  s://homepages.cwi.nl/ ~bo  ncz/bads/ map  red  uce.s html
                                                 Auck land, M ay   2025                                                1
````

### 图片文字 OCR（en-US，待对照原页）

````text
MapReduce
COMPCSI 752: Big Data Management
University of Auckland
Credits to Ninh Pham for the Slides
Slides are collected and edited from
http : / /webdam.inria. fr/ Jorge / index921 3. html
and ht s: / / home a es.cwi.nl/ —boncz/bads/ma reduce.shtml
Auckland, May 2025
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/MapReduce-Algorithms.pdf#page=2)

### 原始文字层

````text
Outline
2
 The MapReduce framework
 MapReduce
 HDFS
 Apache Hadoop
 Apache Spark
 MapReduce algorithms: 
 PageRank
 Similarity join
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Outline
The MapReduce framework
MapReduce
HDFS
Apache Hadoop
Apache Spark
MapReduce algorithms:
PageRank
Similarity join
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/MapReduce-Algorithms.pdf#page=3)

### 原始文字层

````text
PageRank computation
3
 PageRank: importance score for nodes in a graph, used for 
ranking query results of Web search engines:
 Compute M.
 Let v0 be the uniform vector of sum 1, v = v0
 Repeat N times:
o Set v := Mv
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
PageRank computation
PageRank importance score for nodes in a graph, used for
ranking query results of Web search engines:
Compute M.
Let vo be the uniform vector of sum 1, v = vo
Repeat N times:
Set v := Mv
O
Exercise
Express PageRank computation as a MapReduce problem. Main program? map and reduce
functions? combiner function?
Illustrate on this graph.
4
2
3
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/MapReduce-Algorithms.pdf#page=4)

### 原始文字层

````text
PageRank exercise
4
 Setup:
 M = 
0 0 0 1
2
1
2
0 0 0
1
2
1 0 1
2
0 0 1 0
, v0 =
1/4
1/4
1/4
1/4
 Results of the first and second rounds:
v1 = Mv0
=
1/8
1/8
1/2
1/4
, v2 = Mv1
=
2/16
1/16
5/16
8/16
,
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
PageRank exercise
Setup:
M
0
2
1
0
1
1/4
Results of the first and second rounds:
1/8
1/8
1/2
MVI -
2/16
1/16
5/16
8/16
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/MapReduce-Algorithms.pdf#page=5)

### 原始文字层

````text
PageRank exercise
5
 Setup:
 Mv0 = 
0 0 0 1
2
1
2
0 0 0
1
2
1 0 1
2
0 0 1 0
1/4
1/4
1/4
1/4
=
1/8
1/8
1/2
1/4
 New set up:
Mv0
=
0
1/2
1/2
0
¼ + 
0
0
1
0
¼ + 
0
0
0
1
¼ + 
1/2
0
1/2
0
¼ 
Node A Node B Node C Node D
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
PageRank exercise
14 +
Setup:
0
1
New set up:
1/2
1/2
Node A
0
1
1/4
1/8
1/8
1/2
1/2
Node B Node C
1/2
Node D
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/MapReduce-Algorithms.pdf#page=6)

### 原始文字层

````text
MapReduce: PageRank
6
 We emit both pagerank contributions and the outlink_list
since we will use the outlink_list for the next map-reduce
Node
Node
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
MapReduce: PageRank
4
Node
2
3
Algorithm 1 map key: [url, pagerank], value: outlink-list)
1: for each outlink in outlink-list do
emit(key: outlink, value: pagerank/size(outlink-list))
2:
3: end for
Node
4: emit (key: url, value: outlink-list)
We emit both
pagerank contributions and the outlink_list
since we will use the outlink_list for the next map-reduce
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/MapReduce-Algorithms.pdf#page=7)

### 原始文字层

````text
Map: Example 
7
 Assume that we have 1 mapper for each url
 Map inputs:
 Node 1: (key = [1, 1/4], value = [2, 3])
 Node 2: (key = [2, 1/4], value = [3])
 Node 3: (key = [3, 1/4], value = [4])
 Node 4: (key = [4, 1/4], value = [1, 3])
 Map outputs:
 Node 1: (2, 1/8), (3, 1/8), (1, [2, 3])
 Node 2: (3, 1/4), (2, [3])
 Node 3: (4, 1/4), (3, [4])
 Node 4: (1, 1/8), (3, 1/8), (4, [1, 3])
I
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Map: Example
4
Assume that we have 1 mapper for each url
2
3
Map inputs:
Node 1: (key = [1, 1/4], value
Node 2: (key = [2, 1/4], value
Node 3: (key = [3, 1/4], value
Node 4: (key = [4, 1/4], value
e Map outputs:
Node 1: (2,
Node 2: (3,
Node 3: (4,
Node 4: (1,
1/4
1/4
1/8), (3
1/8), (1
[31)
[41)
1/8), (4
= [41)
l)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/MapReduce-Algorithms.pdf#page=8)

### 原始文字层

````text
MapReduce: PageRank
8
Check urls or pagerank
• urls is a list of nodes
• pagerank is a real value
Node
I
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Map  Red uce : P ageR ank
                                         Node
                                                                I
                                                             C hec  k u rls o r p ag  eran k
                                                             •   u rls is   a l ist   o f n od es
                                                             •   p ag  eran k is   a real   va l ue
                                                                                              8
````

### 图片文字 OCR（en-US，待对照原页）

````text
MapReduce: PageRank
Algorithm 2 reduce(key: url, value: list-pageran
2
3
1:
2:
3:
4:
5:
6:
8:
9:
10:
11:
outlink-list=[ ]
Node
pagerank 0
for each pagerank-or-urls in list-pagerank-or-url
or-urls)
do
if is-list (pagerank-or-urls) then
outlink-list pagerank-or-urls
else
pagerank pagerank-or-urls
Check rls or pagerank
urls s a list of nodes
pag rank is a real value
end if
end for
pagerank
emit (key:
d * pagerank + (1 - d)/n
[url, pagerank], value: outlink-list)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/MapReduce-Algorithms.pdf#page=9)

### 原始文字层

````text
Reduce: Example
9
 Assume that we have 1 reducer for each url, d = 1
 Reduce inputs:
 Node 1: (1, [1/8, [2, 3]])
 Node 2: (2, [1/8, [3]])
 Node 3: (3, [1/8, 1/4, 1/8, [4]])
 Node 4: (4, [1/4, [1, 3]])
 Reduce outputs:
 Node 1: ([1, 1/8], [2, 3])
 Node 2: ([2, 1/8], [3])
 Node 3: ([3, 1/2], [4])
 Node 4: ([4, 1/4], [1, 3])
I
按关键词分类
_
have
㬗
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Reduce: Example
Assume that we have 1 reducer for each url, d = 1
． Reduce inputs ：
． Node 1 ： （ 1 ，
． Node 2 ： （ 2 ，
卩 / 8 ， [311)
． Node 3 ： （ 3 ，
卩 / 8 ， 1 / 4 ， 1 / 8 ， [4]])
． Node 4 ： （ 4 ，
卩 / 4 ， 卩 ， 311)
． Reduce outputs ：
． Node 1 ： （ 卩 ， 1 / 8 ] ，
31)
． Node 2 ： ([2, 1 / 8 ] ，
． Node 3 ： （ 卩 ， 1 / 2 ] ，
． Node 4 ： ([4, 1 / 4 ] ，
4
3
````

### 图片文字 OCR（en-US，待对照原页）

````text
Reduce: Example
Assume that we have 1 reducer for each url, d =
Reduce inputs:
Node 1: (1,
Node 2: (2, [1/8, [311
Node 3: (3,
[1/8, 1/4, 1/8,
Node 4: (4,
[1 /4, [1, 311)
Reduce outputs:
Node l: 1/81, p, 31)
Node 2: (P, 1/81,
[31)
Node 3: 1/2],
Node 4: ( [4, 1 / 41,
2
3
4
1
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/MapReduce-Algorithms.pdf#page=10)

### 原始文字层

````text
PageRank example 
10
 Reduce outputs:
 Node 1: ([1, 1/8], [2, 3])
 Node 2: ([2, 1/8], [3])
 Node 3: ([3, 1/2], [4])
 Node 4: ([4, 1/4], [1, 3])
 Verifications:
v1 = Mv0
=
1/8
1/8
1/2
1/4
, v2 = Mv1
=
2/16
1/16
5/16
8/16
, …
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
PageRank example
Reduce outputs:
Node 1: 1/81, p, 31)
Node 2: (P, 1/81,
[31)
Node 3: 1/2],
[41)
Node 4: ( [4, 1 / 41,
l)
e Verifications:
4
1/8
1/8
1/2
MVI
2/16
1/16
5/16
8/16
2
3
10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/MapReduce-Algorithms.pdf#page=11)

### 原始文字层

````text
Outline
11
 The MapReduce framework
 MapReduce
 HDFS
 Apache Hadoop
 Apache Spark
 Applications: 
 PageRank
 Similarity join
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Outline
The MapReduce framework
MapReduce
HDFS
Apache Hadoop
Apache Spark
Applications :
PageRank
Similarity join
11
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/MapReduce-Algorithms.pdf#page=12)

### 原始文字层

````text
Inverted index solution
12
family (d1, .13), (d3, .13), (d6, .08), (d5, .07)
football (d4, .47)
jaguar (d1, .04), (d2, .04), (d3, .04), (d4,.04), (d6, .04), (d5, .02)
new (d2, .24), (d1, .20), (d5, .10)
rule (d6, .28)
us (d4, .30), (d5, .15)
world (d1, .47)
…
Term Documents
family:(d1, d3), (d1, d6), (d1, d5), (d3, d6), (d3, d5), (d6, d5)
…
new: (d2, d1), (d2, d5), (d1, d5)
…
Candidate 
pairs
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Inve r    te d   index  s ol  ution
 Ter   m                                               Do cu ments
fa mily        (d1,   .1 3), (d3 , .1 3 ), (d6, .  08 ), (d5 , .0 7 )
fo  o  tba  l  l   (d4,   .4 7)
ja  gu  a  r   (d1,   .0 4), (d2 , .0 4 ), (d3, .  04 ), (d4 ,.0 4 ), (d6, .  04 ), (d5 , .0 2 )
new            (d2,   .2 4), (d1 , .2 0 ), (d5, .  10 )
rule           (d6,   .2 8)
us             (d4,   .3 0), (d5 , .1 5 )
wo rl d        (d1,   .4 7)
…
     family: (d1, d3 ), (d1, d 6), (d1 , d5), (d 3, d6), (d 3, d5), (d6, d5 )                      Candi  date
     …                                                                                                 pa ir    s
     new: (d2, d1 ), (d2, d 5), (d1 , d5)                                                                   12
     …
````

### 图片文字 OCR（en-US，待对照原页）

````text
Term
famil
football
ja ar
new
rule
us
world
family:
Inverted index solution
(d6, .28)
dl, .13 , d3,
.47)
.04), (d2,
.24), (d 1,
.30), (ds, .15)
.47)
.13 , d6,
.04), (d3,
.20), (ds, . 10)
Documents
.08 , ds, .07
.04), ((14,.04), (d6,
(d2, dl), (d2, ds), (dl, ds)
new:
.04), (d5, .02)
Candidate
pairs
12
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/MapReduce-Algorithms.pdf#page=13)

### 原始文字层

````text
MapReduce: Index construction
13
 Map input (i, di
): 
 For each document i, we have a list di consisting of terms t and its weight 
di
[t]
 Map output (t, [i, di
[t]]): 
 For each term t in document i, we output key = t, value = [i, di
[t]] as a 
pair of document ID and the weight of the term t
 Reduce: do nothing
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
MapReduce: Index construction
Map input di
For each document i, we have a list di consisting of terms t and its weight
di[tl
(t,
[i, di[t]]
Map output
For each term t in document i, we output key = t, value ¯
pair of document ID and the weight of the term t
Reduce
• do nothing
[i, di[t]]
as a
Map
Reduce
(i, di) —+ (i, dt[t])) ld
13
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/MapReduce-Algorithms.pdf#page=14)

### 原始文字层

````text
MapReduce: Similarity join
14
 Map input (t, [(i, di
[t]), (j, dj
[t]), …]): 
 For each term t, we have a posting list of document ID consisting of t and 
its weight
 Map output ((i, j), [di
[t] * dj
[t]]): 
 For each pair of documents (i, j) where i < j, we compute the product 
di
[t] * dj
[t] as the contribution of the term t to their inner product
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
MapReduce: Similarity join
(t,
di[t]), (j, dj[t]),
Map input
For each term t, we have a posting list of document ID consisting of t and
its weight
Map output ( (i, j)'
For each pair of documents (i, j) where i < j, we compute the product
as the contribution of the term t to their inner product
Map
Reduce
w = (It [t] • dj[t]) I i < j]
, Wlwl])
a(dt, dj) Ewe
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/MapReduce-Algorithms.pdf#page=15)

### 原始文字层

````text
MapReduce: Similarity join
15
 Reduce input ((i, j), [w0, w1, …, w|W|]): 
 For each pair of documents (i, j) where i < j, we have a list of values, 
each corresponding to the contribution of the common term t
 Reduce output ((i, j), σ(i, j) = w0+w1+…+w|W|]): 
 For each pair of documents (i, j) where i < j, we compute the inner 
product σ by the sum of all term contributions and decide the matching
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
MapReduce: Similarity join
Reduce input ( (i, j)'
For each pair of documents (i, j) where i < j, we have a list of values,
each corresponding to the contribution of the common term t
Reduce output
For each pair of documents (i, j) where i < j, we compute the inner
product O by the sum of all term contributions and decide the matching
Map
Reduce
w = (It [t] • dj[t]) I i < j]
, Wlwl])
a(dt, dj) Ewe
15
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/MapReduce-Algorithms.pdf#page=16)

### 原始文字层

````text
Prefix-filtering solution
16
 Observation:
 We do not want to index all documents for each term
 Do not want to compute σ(x, y) if
 σ(x, y) = x1y1 + x2y2 + … + xkyk + xk+1yk+1 +… + xdyd < thres
 Define vector m containing the maximum value for each 
dimension
 x1m1 + x2m2 + … + xkmk + xk+1mk+1 + … + xdmd
< thres
≥ thres
Maximum contribution 
from dimensions 1 to k
If no intersection between 
x and y on dimensions k+1 to 
d then sim(x, y) < thres
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Prefix-fi Itering sol ution
Observation:
We do not want to index all documents for each term
Do not want to compute O(x, y) if
O(X, y) = XIYI + X2Y2 + + XkYk + Xk+lYk+l
+ + XdYd < thres
Define vector m containing the
maximum value for each
dimension
+ + ... + Xkmk
x m + + X dmd
< thres
2 thres
Maximum contribution
from dimensions 1 to k
If no intersection between
x and y on dimensions k +1 to
d then sim(x, y) < thres
16
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/MapReduce-Algorithms.pdf#page=17)

### 原始文字层

````text
Prefix-filtering solution
17
 bi (bj
) is the maximum position of di (dj
) s.t. the maximum
of partial sum from dimensions 1 to bi (bj
) is still smaller 
than thres
 We only index the signatures of di and dj
< thres
< thres
Signatures
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Prefix-fi Itering sol ution
bi (bj) is the
position of di (d.) s.t. the
maximum
maximum
of partial sum from dimensions 1 to bi (b.) is still smaller
than thres
We only index the signatures
of di and dj
< thres bi
Pruned
d
b
Indéxed
ICI
Indexed
Pruhed
< thres
Signatures
17
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 18 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/MapReduce-Algorithms.pdf#page=18)

### 原始文字层

````text
MapReduce: Prefix-filtering
18
 Map input (i, di
): 
 For each document i, we keep a list di consisting of terms t and its weight 
di
[t]
 Map output (t, di
) for each term t in the signature S(di
):
 For each term t in the signature, we output the list di (whole document)
≥ thres
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
MapReduce: Prefix-filtering
Map input di
For each document i, we keep a list di consisting of terms t and its weight
di[tl
Map output t, di) for each term t in the signature S(di):
For each term t in the signature, we output the list d (whole document)
Map
Reduce
•••,dIDI])—
j), a(dt, dj)
di,dj e D A a(di, dj) thres
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 19 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/MapReduce-Algorithms.pdf#page=19)

### 原始文字层

````text
MapReduce: Prefix-filtering
19
 Reduce input (t, [di
, dj
, …]): 
 For each term t, we have a list of list di of the document i which contains 
t in their signature
 Reduce output ((i, j), σ(di
, dj
)) if σ(di
, dj
) ≥ thres: 
 For each pair of documents (i, j) where i < j, we compute their inner 
product σ using di and dj and decide the matching
≥ thres
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
MapReduce: Prefix-filtering
Reduce input t [di, dj, ...l
For each term t, we have a list of list di of the document i which contains
t in their signature
o(di, dj)) o(di, dj)
Reduce output
For each pair of documents (i, j) where i < j, we compute their inner
product O using di and d. and decide the matching
Map
Reduce
•••,dIDI])—
j), a(dt, dj)
di,dj e D A a(di, dj) thres
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 20 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/MapReduce-Algorithms.pdf#page=20)

### 原始文字层

````text
Homework
20
 Writing the Hadoop MapReduce programs to compute 
PageRank and Similarity Join (both versions)
 Input of PageRank is the same as the PageRank lecture’s homework
 Input of Similarity Join is the same as the Data Cleaning lecture’s 
homework
 Verify the accuracy of the results between the MapReduce 
version and the non-MapReduce version
 Challenges: Can we adapt these solutions for other similarity 
measures, e.g. Jaccard similarity, containment similarity?
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Homework
Writing the Hadoop MapReduce programs to compute
PageRank and Similarity Join (both versions)
Input of PageRank is the same as the PageRank lecture's homework
Input of Similarity Join is the same as the Data Cleaning lecture's
homework
Verify the accuracy of the results between the MapReduce
version and the non-MapReduce version
Challenges: Can we adapt these solutions for other similarity
measures, e.g. Jaccard similarity, containment similarity?
20
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

