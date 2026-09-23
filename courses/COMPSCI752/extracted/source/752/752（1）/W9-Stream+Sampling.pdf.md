# W9-Stream+Sampling.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI752/source/752/752（1）/W9-Stream+Sampling.pdf`
- [打开原文件](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BSampling.pdf)
- 原文件 SHA-256：`4d9b4f13a9c028ade8f8825843f112c6699dcac232825e9978f0e5bcdcaffe72`
- 文件索引：F225；PDF 总页数：17
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BSampling.pdf#page=1)

### 原始文字层

````text
1
Stream Sampling
COMPSCI 752: Big Data Management
University of Auckland
(Credits to Ninh Pham)
Parts of this material are modifications of the lecture slides from
http://mmds.org
Designed for the textbook Mining of Massive Datasets
by Jure Leskovec, Anand Rajaraman, and Jeff Ullman
Auckland, May 2025
抽样
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Stream   Sampling抽样
                                                     CO    MPSC   I   7    52:   Bi  g      Dat a   Man a    ge   me   n t
                                                                          Univers  ity          of Auc  kland
                                                                         (C red  its to Ninh Pham  )
                                                    Par  ts o f th  is mat er ial  are   mo difi  cat io ns o f the  l ect ur e sl ide s from
                                                                                    ht   tp  :/   /mm  ds .o  rg
                                                       D esign ed  for  the t ex tbo ok      Min in g   of Massive Da ta set s
                                                            by    J ur   e Le skovec, A na  n   d  R a  j    ar    a  ma  n   ,  a  n   d  J e   ff    U   ll    ma  n
                                                                             Auck land,         M ay   2025                                                                              1
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Strea m sa*pling
COMPSCI 752 ： Big D ata Management
University of Auckland
(Credits to N inh Pham)
Parts of this material are modifications of the lecture slides from
Designed for the textbook Mining of Massive Datasets
by Jure Leskovec, Anand Rajaraman, and Jeff Ullman
Auckland ， May 202S
````

### 图片文字 OCR（en-US，待对照原页）

````text
Stream sa*pling
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

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BSampling.pdf#page=2)

### 原始文字层

````text
Outline
2
 Sampling from a data stream
 Sampling a fixed proportion
 Sampling a fixed-size (reservoir sampling)
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Outline
Sampling from a data stream
Sampling a fixed proportion
Sampling a fixed-size (reservoir sampling)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BSampling.pdf#page=3)

### 原始文字层

````text
Uniformly sampling from a stream
3
 Motivation:
 Since we cannot store the entire stream, we store a uniform sample of the 
stream to answer queries
 Goal:
 Out of the large number of elements a1, … , am, we choose a small number 
of elements to keep in memory
 Sample from the stream a1, … , am a single element x uniformly at random, 
i.e. the probability of being the sample for each element is the same: 
 Pr [ ai is the sample x] = 1/m
 We draw a uniform sample over the stream, not over the universe U
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Uniformly sampling from a stream
Motivation:
Since we cannot store the entire stream, we store a uniform sample
of the
stream to answer queries
Goal:
Out of the large number of elements al, , m,
. a we choose a small number
of elements to keep in memory
Sample from the stream al, . , am a single element x uniformly at random,
i.e. the probability of being the sample for each element is the same:
Pr [ ai is the sample x] = 1/ m
We draw a uniform sample over the stream, not over the universe u
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BSampling.pdf#page=4)

### 原始文字层

````text
Two different problems
4
 Problem 1 (easy):
 Sample a fixed proportion of elements in the stream (1/10)
 The sample size is m/10 given the stream of m elements
 Problem 2 (hard):
 Maintain a random sample of fixed size over an infinite stream
 The sample size is fixed, i.e. s at any time
 Both problems: Pr [ ai is sampled ] = 1/m
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Two different problems
Problem 1 (easy):
Sample a fixed proporüon of elements in the stream (1 / 10)
The sample size is m/ 10 given the stream of m elements
Problem 2 (hard):
Maintain a random sample of
fixed size
infinite stream
over an
The sample size is fixed, i.e. s at any time
Both problems: Pr [ ai is sampled ] = 1 / m
ooooooooooooooooooooooooooo
oooooooooooooooooo
00000000
ooooooooooooooooo
ooo
oo
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BSampling.pdf#page=5)

### 原始文字层

````text
Sampling a fixed proportion
5
 Scenario:
 Search engine receives a stream of tuples (user, query)
 Question: How many users run the same query?
 Memory:We have enough space to store 1/10 of the stream
 Naïve solution to keep 1/10 stream by:
 Generate a random integer in [0, … , 9] for each query
 Store the query if the integer is 0; otherwise, discard
 Can we approximately answer the query?
 Yes
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Sampling a fixed proportion
e Scenario:
Search engine receives a stream of tuples (user, query)
Question: How many users run the same query?
Memory: We have enough space to store 1 / 10 of the stream
Naive solution to keep 1 / 10 stream by:
Generate a random integer in [O,
' 91 for
each query
Store the
if the integer is O; otherwise, discard
query
Can we approximately answer the query?
Yes
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BSampling.pdf#page=6)

### 原始文字层

````text
Problem with naïve approach
6
 Scenario:
 Search engine receives a stream of tuples (user, query)
 Each user sends x queries once and d queries twice (total of x + 2d)
 Question:What fraction of queries by an average user are duplicates?
 Memory:We have enough space to store 1/10 of the stream
 Solution: d/(x + d)
 Can we approximately answer the query using previous 
approach?
 No
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Problem with naive approach
e Scenario:
Search engine receives a stream of tuples (user, query)
Each user sends x queries once and d queries twice (total of x + 2d)
Question: What fraction of queries by an average user are duplicates?
Memory: We have enough space to store 1 / 10 of the stream
Solution: d/ (x + d)
Can we approximately answer the query using previous
approach?
No
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BSampling.pdf#page=7)

### 原始文字层

````text
Problem with naïve approach
7
 Naïve solution to keep 1/10 stream for each query:
 Sample contains x/10 singleton queries and 2d/10 duplicate queries at 
least once
 Sample contains only d/100 pairs of duplicates
o A query is sampled once with prob. 1/10
o A query is sampled twice with prob. 1/10*1/10 = 1/100
 Of d duplicates, 18d/100 appear exactly once in the sample
o A query is sampled at the first time with prob. 1/10
o A query is not sampled at the second time with prob. 9/10
 Solution: 
𝑑
100
𝑥
10+ 𝑑
100+18𝑑
100
=
𝒅
𝟏𝟎𝒙+𝟏𝟗𝒅
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Problem with naive approach
Naive solution to keep 1 / 10 stream for each query:
Sample contains x/ 10 singleton queries and 2d/ 10 duplicate queries at
least once
Sample contains only d/ 100 pairs of duplicates
A query is sampled once with prob. 1/10
O
A query is sampled twice with prob. 1/10* 1 / 10 = 1/100
o
Of d duplicates, 18d/ 100 appear exactly once in the sample
A query is sampled at the first time with prob. 1 / 10
O
A query is not sampled at the second time with prob. 9/10
O
Solution:
100
x d 18d ¯
10 100 100
d
IOx+19d
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BSampling.pdf#page=8)

### 原始文字层

````text
Fix
8
 Scenario:
 Search engine receives a stream of tuples (user, query)
 Each user sends x queries once and d queries twice (total of x + 2d)
 Question:What fraction of queries by an average user are duplicates?
 Solution:
 Pick 1/10 of users (not queries) and take all their searches in the sample
 Use a hash function to hash the user ID uniformly into 10 buckets and 
pick user IDs on the first bucket
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Fix
e Scenario:
Search engine receives a stream of tuples (user, query)
Each user sends x queries once and d queries twice (total of x + 2d)
Question: What fraction of queries by an average user are duplicates?
e Solution:
Pick 1/10 of
(not queries) and take all their searches in the sample
users
use a hash function
to hash the user ID uniformly into 10 buckets and
pick user IDs on the first bucket
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BSampling.pdf#page=9)

### 原始文字层

````text
 Stream of tuples with keys:
 Key is some subset of each tuple’s components
 E.g. tuple(user, query) with user as a key
 Choice of key depends on application
 To get a sample of a/b fraction of the stream:
 Hash each tuple’s key uniformly into b buckets
 Pick the tuples that hashed into the first a buckets
Generalized solution
9
1 2 a b
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Generalized solution
Stream of tuples with keys:
Key is some subset of each tuple's components
E.g. tuple(user, query) with user as a key
Choice of key depends on application
To get a sample of a/ b fraction of the stream:
Hash each tuple's key uniformly into b buckets
Pick the tuples that hashed into the first a buckets
1
2
a
b
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BSampling.pdf#page=10)

### 原始文字层

````text
Sampling vs. hashing
10
 Sampling:
 Hashing:
Graham Cormode, Marios Hadjieleftheriou, CACM 2009
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Sampling vs. hashing
Sampling:
ooooooooooooooooooooooooooo
oooooooooooooooooo
oooooooo
ooooooooooooooooo
Hashing:
ooo o oooooo o
ooo
Graham Cormode, Marios Hadjieleftheriou, CACM 2009
ooo
oo
10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BSampling.pdf#page=11)

### 原始文字层

````text
Outline
11
 Sampling from a data stream
 Sampling a fixed proportion
 Sampling a fixed-size (reservoir sampling)
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Outline
Sampling from a data stream
Sampling a fixed proportion
Sampling a fixed-size (reservoir sampling)
11
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BSampling.pdf#page=12)

### 原始文字层

````text
Sample a fixed size
12
 Challenge:
 The sample set S has fixed size s regardless the length of the stream
 Uniformly sampling element from the stream
 Reservoir Sampling (s = 1) [Vitter’85]:
 s = a1
 a2 is picked as s with prob. 1/2
 a3 is picked as s with prob. 1/3
 …
 an is picked as s with prob. 1/n
 …
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Sample a fixed size
e Challenge:
The sample set S has fixed size s regardless the length of the stream
Uniformly sampling element from the stream
Reservoir Sampling (s ¯
1) [Vitter' 85]:
a2 is picked as s with prob. 1/2
a3 is picked as s with prob. 1/3
an is picked as s with prob. 1 / n
12
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BSampling.pdf#page=13)

### 原始文字层

````text
Decision tree of reservoir sampling
13
 Reservoir sampling a stream a1, a2, a3, a4
Elena Ikonomovska, Mariano Zelke’13
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Decision tree of reservoir sampling
Reservoir sampling a stream
Take al
as sample s?
Take
to replace s?
Take a3
to replace s?
Take
to replace s?
The final
sample is
Probability
of this path
a3
a2, a3, a 4
a4
a3
Elena Ikonomovska, Mariano Zelke' 1 3
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BSampling.pdf#page=14)

### 原始文字层

````text
Proof
14
 For a stream a1, a2, … , aL, aL+1, … , am, we need to prove 
Pr [ aL is sampled ] = 1/m
 Proof:
 What is the probability that some aL is the final s for 1 ≤ L ≤ m?
 This happens if aL is chosen as s and the rest aL+1, … , am are not
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Proof
For a stream a a
e Proof:
L' LA-I'
is sampled ]
, am, we need to prove
What is the probability that some aL is the final s for 1 L m?
This happens if aL is chosen as s and the rest a
L+l' , am are not
II Pr[ai does not replace ac as s]
Pr[ac is the final s] = Pr[ac is chosen as s] •
1
7
1
7
1
i=C+1
1
11
1—
i
i=C+I
1
11
i
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BSampling.pdf#page=15)

### 原始文字层

````text
Generalized solution
15
 Reservoir Sampling (s > 1) [Vitter’85]:
 Store all the first s elements of the stream to S
 Suppose we have seen m-1 elements, and now the mth element am arrives 
(m > s)
o With prob. s/m, keep am, else discard it
o If we keep am, then am replaces one of the s elements in S, picked 
uniformly at random
 Theorem:
 After m elements, the sample S contains each element seen so far with 
the same probability s/m
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Generalized solution
Reservoir Sampling (s > 1) [Vitter' 85]:
Store all the first s elements of the stream to S
O
Suppose we have seen m-1 elements, and now the mth elementa arrives
With prob. s/ m, keep am, else discard it
o
If we keep am, thena replaces one of the s elements in S, picked
o
uniformly at random
Theorem:
After m elements, the sample S contains each element seen so far with
the same probability s/ m
15
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BSampling.pdf#page=16)

### 原始文字层

````text
Proof by induction
16
 Proof:
 Assume that after m elements: Pr [ aL is sampled ] = s/m, 1 ≤ L ≤ m
 When the (m+1)th element arrives, we need to show 
 Pr [ aL is sampled ] = s/(m+1), 1 ≤ L ≤ m+1
 Base case:
 When we see the first s elements, Pr [ aL is sampled ] = 1, 1 ≤ L ≤ s
 (m+1)th element am+1 arrives:
 Pr [ aL is sampled ] = s/m, 1 ≤ L ≤ m (hypothesis)
 Given aL already in S, the probability that aL is still in S is:
 1 − 𝑠
𝑚+1
+ 𝑠
𝑚+1
𝑠−1
𝑠
=
𝑚
𝑚+1
 Pr [ aL is sampled ] = (s/m)*(m/m+1) = s/(m+1), 1 ≤ L ≤ m
 The new element am+1 is sampled with prob. s/(m+1)
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Proof by induction
e Proof:
Assume that after m elements: Pr [ aL is sampled ] = s/ m, 1 L m
When the (m+ l)th element arrives, we need to show
Pr [ aL is sampled ] = s/(m+l), 1 L m +1
Base case:
When we see the first s elements, Pr [ aL is sampled I
(m+l)th element a
arrives :
Pr [ aL is sampled ] = s/ m, 1 L m (hypothesis)
Given aL already in S, the probability that aL is still in S is :
s s—l
m+l s
m+l
Pr [ aL is sampled ] = = s/(m+l), 1 L m
The new element a
m+l is sampled with prob. s/(m+l)
16
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BSampling.pdf#page=17)

### 原始文字层

````text
Homework
17
 Implement the uniformly sampling algorithms on the dataset from 
Use the KOS blog entries data set from 
https://archive.ics.uci.edu/ml/datasets/Bag+of+Words
 This data set consists of 3430 documents, each represented as a set of 
keywords. The total number of keywords of the corpus is 6960
 Consider each line of data as a streaming transaction in e-commerce
o doc ID is a user ID
o word ID is an item ID
 Queries:
o What is the most frequent items has been bought?
o What is an average number of items bought by a user?
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Homework
Implement the uniformly sampling algorithms on the dataset from
use the
KOS blog entries
data set from
htt s: //archive.ics.uci.edu/ml/datasets/Ba +of+Words
This data set consists of 3430 documents, each represented as a set of
keywords. The total number of keywords of the corpus is 6960
Consider each line of data as a streaming transaction in e-commerce
doc ID is a user ID
O
word ID is an item ID
O
ueries:
What is the most frequent items has been bought?
O
What is an average number of items bought by a user?
O
17
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

