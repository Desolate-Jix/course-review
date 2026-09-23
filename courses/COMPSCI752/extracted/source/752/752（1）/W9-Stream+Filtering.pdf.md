# W9-Stream+Filtering.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI752/source/752/752（1）/W9-Stream+Filtering.pdf`
- [打开原文件](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BFiltering.pdf)
- 原文件 SHA-256：`dfb9dcde6284dc509301df703a05a7d0dd930d9ca09004ce81152af2e33e2f01`
- 文件索引：F222；PDF 总页数：17
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BFiltering.pdf#page=1)

### 原始文字层

````text
1
Bloom Filter
COMPCSI 752: Big Data Management
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
Bloom F ilter
                                                        CO    MPC   SI   7    52:   Bi  g      Dat a   Man a    ge   me   n t
                                                                              Univers  ity of Auc  kland
                                                                             (C red  its to Ninh Pham  )
                                                       Par  ts o f th  is mat er ial  are   mo difi  cat io ns o f the  l ect ur e sl ide s from
                                                                                         ht   tp  :/   /mm  ds .o  rg
                                                           D esign ed  for  the t ex tbo ok        Min in g   of Massive Da ta set s
                                                               by    J ur   e Le skovec , A na  n   d  R a  j    ar    a  ma  n   ,  a  n   d  J e   ff    U   ll    ma  n
                                                                                 Auck land,   May   2025                                                                                            1
````

### 图片文字 OCR（en-US，待对照原页）

````text
Bloom Filter
COMPCSI 752: Big Data Management
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

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BFiltering.pdf#page=2)

### 原始文字层

````text
Basic definitions
2
 Let U be a universe of size n, i.e. U = {1, 2, 3, … , n}
 Cash register model stream:
 Sequence of m elements a1,…, am where ai ∈ U
 Elements of U may or may not occur once or several times in the stream
 Example: A sequence of email addresses, a sequence of IP addresses,…
 Filtering a data stream (today’s lecture):
 Select elements with property x from the stream
鏶
o
胶鞋ㄏ 懒
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Basic definitions
Let u be a universe of size n, i.e. u = { 1 ， 2 ， 3
． Cash register model stream ：
Sequence Ofm elements al ， ·
a where ai
Elements Of may or may not O ccur once or several time S in the stream
Example ： A sequence of email addresses, a sequence of IP addresses, ·
． Filtering a data stream (today's lecture
Select elements with
from the stream
property x
````

### 图片文字 OCR（en-US，待对照原页）

````text
Basic definitions
Let u be a universe of size n, i.e. u = {1 2 3
Cash register model stream:
Sequence of m elements al, ... , am where ai e u
Elements of u may or may not occur once or several times in the stream
Example: A sequence of email addresses, a sequence of IP addresses, ...
Filtering a data stream (today's lecture):
Select elements with
from the stream
property x
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BFiltering.pdf#page=3)

### 原始文字层

````text
Filtering data stream
3
 Given a list of elements S, determine which stream elements 
are in S
 Obvious solution: Hash table
 We do not have enough memory to store all S in a hash table
 We might process millions of filters on the same stream, i.e. we have 
millions of different sets S
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Filtering data stream
Given a list of elements S, determine which stream elements
are in S
Obvious solution: Hash table
We do not have enough memory to store all S in a hash table
We might process
millions of filters on the same stream, i.e. we have
millions of different sets S
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BFiltering.pdf#page=4)

### 原始文字层

````text
Applications
4
 Email spam filtering:
 We know approximately 1 billion “good” email addresses
 If an email comes from one of these, it is NOT spam
http://www.junkemailfilter.com
前屏
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Applications
． Email sp am filtering:
We know approximately 1 billion good" email addresses
If an email comes from one of these, it is NOT spam
MaiI/Spam/Viruses
Our Spam FiIter
TRASHED ！
VIRUSES/SPAMS
0
htt ： / / www. •unkemailfilter.com
Good Email
````

### 图片文字 OCR（en-US，待对照原页）

````text
Applications
Email spam filtering:
We know approximately 1 billion "good" email addresses
If an email comes from one of these, it is NOT spam
Mail/Spam/Viruses
Our Spam Filter
TRASHED!
VIRUSES/SPAMS
htt : / / www. •unkemailfilter.com
Good Email
Low Spam
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BFiltering.pdf#page=5)

### 原始文字层

````text
Applications
5
 Publish-subscribe systems:
 You are collecting a lots of message (new articles)
 People express interest in certain sets of keywords
 Determine whether each message matches user’s interest
https://docs.oracle.com
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Applications
Publish-subscribe systems:
You are collecting a lots of message (new articles)
People express interest in certain sets of keywords
Determine whether each message matches user's interest
MyTPublisher1
Msgl
MyTPublisher2
Msg2
Msg3
MyTPublisher3
Broker
Topicl
htt s: / /docs.oracle.com
sgl
MyTSubscriber1
sg2
Msg3
Msgl
Msg3
MyTSubscriber2
Msg2
MyTSubscriber3
Msgl
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BFiltering.pdf#page=6)

### 原始文字层

````text
First cut solution
6
 Given a set of keys S
 Create a bit array B of n bits, initially at 0s
 Choose a hash function h with range [1, n]
 Hash each member s ∈ S to one of n buckets, and set that bit 
to 1, i.e. B[h(s)] = 1
 Hash each element a of the stream and output only those that 
hash to bit that was set to 1
 Output a if B[h(a)] = 1
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
First cut solution
Given a set of keys S
Create a bit array B of n bits, initially at Os
Choose a hash function h with range [1, n
Hash each member s E S to one of n buckets, and set that bit
to 1, i.e.
Hash each element a of the stream and output only those that
hash to bit that was set to 1
Output a if
—1
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BFiltering.pdf#page=7)

### 原始文字层

````text
7
 Create false positives but no false negatives:
 If the item is in S, we surely output it (no false negatives)
 If not, we may still output it (false positives)
Item
0010001011000
Output the item since it may be in S
Item hashes to a bucket that at least 
one of the items in S hashed to
Hash 
func h
Drop the item
It hashes to a bucket set 
to 0 so it is surely not in S
Bit array B
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Output the item since it may be in S
Item hashes to a bucket that at least
one of the items in S hashed to
Filter
Item
Hash
func h
0010001011000 Bit array B
Drop the item
It hashes to a bucket set
to O so it is surely not in S
Create false positives but no false negatives:
If the item is in S, we surely output it (no false negatives)
If not, we may still output it (false positives)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BFiltering.pdf#page=8)

### 原始文字层

````text
Parameter settings
8
 |S| = 1 billion email addresses
 |B| = 1 GB = 8 billion bits
 If the email is in S, then it hash to bucket that set to 1. It 
always gets through (no false negatives)
 Approximately 1/8 of the bit are set to 1. So about 1/8 of 
the email addresses not in S get through to the output (false 
positives)
 Often, less than 1/8, since we might have collisions, i.e. more than one 
email address hash to the same position
Broom 大 比r
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Parameter settings
1 billion email addresses
《 B 《 = 1 GB = 8 billion bits
If the email is in S, then it hash to bucket that set to 1 · lt
always gets through ()o false negatives)
Approximately 1 / 8 of the bit are set to 1 · So about 1 / 8 of
the email addresses not in S get through to the output (false
positives
Often, less than 1 / 8 ， sinc e we might have collisions, i.e. more than one
email address hash tO the same po sition
````

### 图片文字 OCR（en-US，待对照原页）

````text
Pa rameter settings
= 1 billion email addresses
IBI = 1 GB = 8 billion bits
If the email is in S, then it hash to bucket that set to 1. It
always gets through (no false negatives)
Approximately 1/8 of the bit are set to 1. So about 1/8 of
the email addresses not in S get through to the output (false
positives)
Often, less than 1/8, since we might have collisions, i.e. more than one
email address hash to the same position
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BFiltering.pdf#page=9)

### 原始文字层

````text
Analysis: Balls and bins model
9
 We want to analyze the number of false positives
 General problem: If we randomly throw m balls into n bins, 
what is the probability that a bin get at least one ball?
 Our case:
 Balls = elements of S
 Bins = buckets
 Randomly throwing = hashing
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Analysis: Balls and bins model
We want to analyze the number of false positives
General problem: If we randomly throw m balls into n bins,
what is the probability that a bin get at least one ball?
Our case:
Balls = elements of S
Bins = buckets
Randomly throwing = hashing
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BFiltering.pdf#page=10)

### 原始文字层

````text
Analysis: Balls and bins model
10
 We have m balls, n bins
 Prob. that a bin does not have any ball: (1-1/n)m
 Prob. that a bin has at least one ball: 1-(1-1/n)m
 Since (1-1/n)m ~ e-m/n, the prob. that a bin gets at least one 
ball is: 1 - e-m/n
 Fraction of 1s in the array B = prob. of false positives 
= 1 - e-m/n
 Example: m = 1 billions, n = 8 billion bits = 1GB, the 
fraction of 1s in B is 0.1175 (~1/8 = 0.125)
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Analysis: Balls and bins model
We have m balls, n bins
Prob. that a bin does not have any ball: (1-1 /n)m
Prob. that a bin has at least one ball: 1-(1-1 /n)m
e-m/n the prob. that a bin gets at least one
Since (1-1 /n)m
1 — e-m/n
ball is:
Fraction of Is in the array B
prob. of false positives
1 — e-m/n
Example: m = 1 billions, n = 8 billion bits = IGB, the
fraction of Is in B is 0.1175 (
-1/8 = 0.125)
10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BFiltering.pdf#page=11)

### 原始文字层

````text
Bloom filter
11
 |S| = m, |B| = n
 Use k independent hash function h1, … , hk with range [1, n]
 Construct Bloom filter:
 Set B to all 0s
 Hash each member s ∈ S to one of n buckets using k hash functions, and set 
B[hi
(s)] = 1 for i = 1, … , k
 Filtering:
 When a stream element a arrives,
o If B[hi
(a)] = 1 for all i = 1, … , k, then declare a ∈ S
o Otherwise, discard the element a
Onna
k个 hash 一起用
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Bloom filter
us indep endent hash function h
． Construct Bloom filter ：
Set B to all Os
< 1 5h 一 孕 甲
hk with range 卩 n
Hash each member s S to one of n buckets using k hash functions ， and set
1 for i
． Filtering ：
a stream element a arrives ，
1 for all i
k, then declare a S
Otherwise ， discard the element a
````

### 图片文字 OCR（en-US，待对照原页）

````text
Bloom filter
ISI = m, IBl = n
us independent hash function hl,
Construct Bloom filter:
Set B to all Os
hash
, hk with range [1, n
Hash each member s E S to one of n buckets using k hash functions, and set
= 1 for i =
Filtering:
When a stream element a arrives,
If
= 1 for all i = 1
k, then declare a E S
o
Otherwise, discard the element a
o
11
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BFiltering.pdf#page=12)

### 原始文字层

````text
Bloom filter
12
 Example:
 |S| = 3, |B| = 18
 S = {x, y, z}
 k = 3
 Discard w since all B[h(w)] are not all 1s
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Bloom filter
Example:
3, IBI = 18
Discard w since all are not all
Is
o
1
o
1
1
1
0
o
0
o
o
1
o
1
o
o
1
o
12
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BFiltering.pdf#page=13)

### 原始文字层

````text
Bloom filter analysis
13
 What fraction of the bit vector B are 1s?
 Randomly throw km balls into n bins
 So fraction of 1s is 1 - e-km/n
 Prob. that 1 position of a is 1s: 1 - e-km/n
 Prob. that all k positions of a is 1s: (1 - e-km/n)k
 So, false positive probability is: (1 - e-km/n)k
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Bloom filter analysis
What fraction of the bit vector B are Is?
Randomly throw km balls into n bins
So fracüon of Is is
-km/n
Prob. that 1 position of a is Is:
-km/n k
Prob. that all k positions ofa is Is: (1 - e
-km/n k
So, false positive probability is:
13
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BFiltering.pdf#page=14)

### 原始文字层

````text
Parameter settings
14
 |S| = 1 billion, n = 8 billion
 k = 1: (1 – e-1/8) = 0.1175
 k = 2: (1 – e-1/4)2 = 0.0493
 Can we increase k to ∞?
 No ☺
 Optimal value of k:
 k = nln(2)/m
 Our case, optimal k = 8ln(2) ~ 6
 Error at k = 6: (1 – e-3/4)6 = 0.0216
0 2 4 6 8 10 12 14 16 18 20
0.02
0.04
0.06
0.08
0.1
0.12
0.14
0.16
0.18
0.2
Number of hash functions, k
False positive prob.
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Pa rameter settings
= 1 billion, n = 8 billion
-1/8
= 0.1175
-1/4 2—
0.0493
Can we increase k to T?
Optimal value of k:
'D k = nln(2)/m
Our case, optimal k = 81n(2) 6
-3/4 6 = 0.0216
Error at k = 6: (1 — e
0.2
0.18
0.16
0.14
O
o. 12
0.1
O
0.04
6
8
10
12
14
16
18 20
Number of hash functions, k
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BFiltering.pdf#page=15)

### 原始文字层

````text
Storage system
15
 Bloom filter speeds 
up answers in a 
key-value storage 
system
 Values are stored 
on a disk which has 
slow access times 
while bloom filter 
decisions are much 
faster
Source: Wikipedia
o
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Storage system
Bloom filter speeds
up answers in a
key-value storage
system
Values are stored
on a disk which has
slow access times
while bloom filter
decisions are much
faster
Do you have 'keyl'?
No
Do you have tkey2'?
Yes: here is key2
Do you have tkey3'?
No
FILTER
Filter:
No
Filter:
Yes
False Positive
Filter:
Yes
necessary
disk access
Yes: here is key2
unnecessary
disk access
No
Source : Wikipedia
STORAGE
Storage:
No
Storage:
Yes
S torage:
No
15
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BFiltering.pdf#page=16)

### 原始文字层

````text
Bloom filter: Summary 
16
 Bloom filters guarantee no false negatives and use limited 
memory, which is suitable for processing data stream
 Great for pre-processing before more expensive check
 Very suitable for hardware implementation
 Hash function computation can be parallelized
nunnery
lowmey
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Bloom filter: Summary
Bloom filters guarante no a se negatives nd use limited
memory, which is suitab e or processing data stream
Great for pre-processing before more expensive check
Very suitable for hardware implementation
Hash function computation can be parallelized
low
16
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BFiltering.pdf#page=17)

### 原始文字层

````text
Homework
17
 Implement the Bloom filter algorithm on the dataset from 
https://archive.ics.uci.edu/ml/datasets/bag+of+words, 
using word tokens from vocal.kos.text:
 Description: Consider that word tokens in the file as “good” words and 
words not mentioned in the file as “bad” words
 Goal: Implement an add-on for Gmail to help users filter out “bad” words 
efficiently while writing an email
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Homework
Implement the Bloom filter algorithm on the dataset from
https://archive.ics.uci.edu/ml/datasets/bag + of + words
using word tokens from vocal.kos.text:
Description: Consider that word tokens in the file as "good" words and
words not mentioned in the file as "bad" words
Goal :
Implement an add-on for Gmail to help users filter out "bad" words
efficiently while writing an email
17
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

