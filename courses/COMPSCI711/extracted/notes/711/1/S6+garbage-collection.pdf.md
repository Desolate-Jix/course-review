# S6+garbage-collection.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI711/notes/original/711/1/S6+garbage-collection.pdf`
- [打开原文件](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf)
- 原文件 SHA-256：`28f9cd4e8250a56574807fb65d1a5c6b16491b6b1b0b0e3cab8889b69ac022a9`
- 文件索引：F066；PDF 总页数：36
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=1)

### 原始文字层

````text
1
Garbage Collection
 Modern programming languages provide garbage 
collection mechanisms for reclaiming the memory 
locations that are no longer used by programs
 One of the commonly used technique in centralised 
system is reference counting 
 each object keeps a reference count
 when the reference to an object is copied, the reference 
count of the object is incremented
 when the reference to an object is deleted, the 
reference count of the object is decremented
 when the reference count becomes 0, the object can be garbage collected
一
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Garbage Collection
Modern programming languages provide garbage
囗
collection mechanisms for reclaiming the memory
locations that are no longer used by programs
One of the commonly used technique in centralised
囗
system iS reference counting
each object eeps a
reference count
0
when the reference 忄 0 an ObJect is copied
the reference
0
count of the object is incremented
when the reference 忄 0 an 0bJect is deleted the
0
reference count Of the Object is decremented
hen the reference count becomes 0
the object can be
0
garbage collected
1
````

### 图片文字 OCR（en-US，待对照原页）

````text
Garbage Collection
Modern programming languages provide garbage
collection mechanisms for reclaiming the memory
locations that are no longer used by programs
One of the commonly used technique in centralised
system is reference counting
o each object eeps a reference count
when the reference to an object is copied
the reference
O
count of the object is incremented
when the reference to an object is deleted
the
O
reference count of the object is decremented
hen the reference count becomes O
the object can be
garbage collected
1
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=2)

### 原始文字层

````text
2
2 3
2
I­t
reena count
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
cD 讠 ·
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=3)

### 原始文字层

````text
3
3 2
mi
reference
复制
````

### 图片文字 OCR（en-US，待对照原页）

````text
one
more
reference,
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=4)

### 原始文字层

````text
4
2 0
release
````

> OCR 未识别出可靠文字；本页可能以图形、手写公式或空白为主。

### 图表辅助说明

引用计数图左侧对象仍有两个入引用，计数 2；右侧对象计数 0，旁有 release 批注，表示不再被引用时可释放。

## PDF 第 5 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=5)

### 原始文字层

````text
5
 problems with reference counting when applied in 
a distributed system
 object might be garbage collected prematurely
 The problem is due to the messages for incrementing and 
decrementing count are received out of order
过年
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
problems with reference counting when applied in
囗
a distributed system
0 object might be garbage collected premat rely
Th e problem is due 忄 0 the messa eS for incrementing and
0
decrementing count are receive
0 酣 of order
5
````

### 图片文字 OCR（en-US，待对照原页）

````text
problems with reference counting when applied in
a distributed system
object might be garbage collected premat rely
O
The problem is due to the messaqes for incrementing and
O
decrementing count are received out of order
5
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=6)

### 原始文字层

````text
6
1
M3
M1 M2
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
M2
M3
````

### 图片文字 OCR（en-US，待对照原页）

````text
MI
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=7)

### 原始文字层

````text
7
1
M3
M1 M2
cloned
+1
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
M2
cloned
M3
````

### 图片文字 OCR（en-US，待对照原页）

````text
MI
cloned
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=8)

### 原始文字层

````text
8
1
M3
M1 M2
cloned
+1
deleted
-1 needtime
not arrive
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
M2
cloned
deleted
M3
1
8
````

### 图片文字 OCR（en-US，待对照原页）

````text
MI
deleted
cloned
1
hoed the
not Qthive ,
8
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=9)

### 原始文字层

````text
9
1
M3
M1 M2
cloned
+1
-1
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
M2
cloned
M3
````

### 图片文字 OCR（en-US，待对照原页）

````text
MI
cloned
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=10)

### 原始文字层

````text
10
0
M3
M1 M2
cloned
+1
-1
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
M2
cloned
M3
````

### 图片文字 OCR（en-US，待对照原页）

````text
MI
cloned
10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=11)

### 原始文字层

````text
11
M3
M1 M2
cloned
+1
object has been debt
too late
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
M2
cloned
M3
````

### 图片文字 OCR（en-US，待对照原页）

````text
MI
cloned
11
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=12)

### 原始文字层

````text
12
weighted reference counting 
 An object has a weight
 assign weight to each pointer
 object weight = sum of the pointers’ weight
 when the pointer is copied, evenly distribute the 
weight
 When a pointer is deleted, the weight of the 
pointer is subtracted from the weight of the 
object
 An object is garbage collected when its weight 
becomes to 0
一
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
weighted reference counting
h aS a
weight
囗 An object
weight 忄 0 each pointer
囗
asstgn
囗 object weight = Sum of the ointers' wei ht
w en the potnter is copied, evenly distribute the
weight
When a pointer is deleted the weight 0f the
囗
pointer is subtracted from the weight of the
object
An object is garbage collected when its weight
囗
becomes 忄 0
0
````

### 图片文字 OCR（en-US，待对照原页）

````text
weighted reference counting
o An object has a weight
assign weight to each pointer
object weight = sum of the ointers' wei ht
w en the pointer is copied, evenly distribute the
weight
When a pointer is deleted
the weight of the
pointer is subtracted from the weight of the
object
An object is garbage collected when its weight
becomes to
12
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=13)

### 原始文字层

````text
13
10
5
5
10
5
2
3
deleted
10
5
5
5
5
copied
cos
猤
多
蔬a
only decrease the
weight
no increase
the weight
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
copied
deleted
````

### 图片文字 OCR（en-US，待对照原页）

````text
teru
copied
10
10
only oJec[roe
deleted
10
tA}Q lb)) -e
ho
13
````

### 图表辅助说明

加权引用计数上下对照：复制引用时将一条权重 5 拆成 2 与 3，总对象权重仍为 10；删除一条权重 5 的引用后，对象权重从 10 减为 5。复制不增加对象端总权重，是该图强调的区别。

## PDF 第 14 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=14)

### 原始文字层

````text
14
10
M3
M1 M2
10
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
M2
M3
````

### 图片文字 OCR（en-US，待对照原页）

````text
MI
10
14
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=15)

### 原始文字层

````text
15
10
M3
M1 M2
cloned
5
5
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
M2
cloned
M3
````

### 图片文字 OCR（en-US，待对照原页）

````text
MI
cloned
10
15
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=16)

### 原始文字层

````text
16
10
M3
M1 M2
cloned
deleted
5
-5
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
M2
cloned
deleted
M3
````

### 图片文字 OCR（en-US，待对照原页）

````text
MI
deleted
cloned
10
16
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=17)

### 原始文字层

````text
17
5
M3
M1 M2
cloned
5
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
M2
cloned
M3
````

### 图片文字 OCR（en-US，待对照原页）

````text
MI
cloned
17
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 18 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=18)

### 原始文字层

````text
18
 The weight in an object only decreases
 It won’t have the problem as the reference 
counting scheme
 What if the weight of an object cannot be 
split?
 Create an indirection object
E
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
囗 Th e weight in an object only ecr ases
0 工 忄 won't have the problem aS the e erence
counting scheme
What if the weight of an object cannot be
囗
split?
0 Create an indirection object
````

### 图片文字 OCR（en-US，待对照原页）

````text
The weight in an object only ecr ases
o It won't have the problem as the e erence
counting scheme
What if the weight of an object cannot be
split?
Create an indirection object
O
18
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 19 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=19)

### 原始文字层

````text
19
1
1
````

### 图片文字 OCR（en-US，待对照原页）

````text
19
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 20 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=20)

### 原始文字层

````text
20
1
1
1
10
1
5 5
indirection
object
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
20
````

### 图片文字 OCR（en-US，待对照原页）

````text
20
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 21 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=21)

### 原始文字层

````text
21
 It cannot handle cyclic garbage
1 1 1 1 1
1
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
工 忄 cannot andle cyclic garbage
````

### 图片文字 OCR（en-US，待对照原页）

````text
o It cannot andle cyclic garbage
21
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 22 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=22)

### 原始文字层

````text
22
Collecting cyclic garbage
 This works as a complement of other 
garbage collection algorithms, e.g., 
weighted reference counting)
 If an object, say A, has a reference to 
another object, say B, then A is the 
predecessor of B, and B is A's successor. 
 Let (a) O represent a set of objects, and 
(b) P be the set of the predecessors of 
the objects in O. It is easy to see that, if 
all the objects in O form a cyclic 
structure, P must be a subset of O.
箭头方向
-
一 一
㡭䨊
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
ColIecting cyclic garbage
囗 This works aS a com lement of other
garbage collection a gorithms, e.g.,
weighted reference counting)
囗 If an object, s ay 在 has a reference
another object, sa
e n-A-is-the
and B iS 月 'S SucceS 0
predecessor
囗 Let (a) 0 represent a set of objects, and
(b) P be the set of the predecessors of
the objects in 0 · 工 忄 is eaSy 忄 0 See that, if
the objects in 0 form a cyclic
structure, P must be a subset of 0 ·
22
````

### 图片文字 OCR（en-US，待对照原页）

````text
Collecting cyclic garbage
This works as a complement of other
garbage collection algorithms, e.g.,
weighted reference counting)
If an object, say A, has a reference
another object, sa
en-A-is-the
and B is A 's succes o
predecessor
0 Let (a) O represent a set of objects, and
(b) P be the set of the predecessors of
the objects in O. It is easy to see that, if
all the objects in O form a cyclic
structure, P must be a subset of O.
22
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 23 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=23)

### 原始文字层

````text
23
A
B C
O = {A, B, C}
o
P = {C, A, B}
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
23
````

### 图片文字 OCR（en-US，待对照原页）

````text
23
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 24 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=24)

### 原始文字层

````text
24
A
B C D
O = {A, B, C, D}
P = {C, A, B}
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
24
````

### 图片文字 OCR（en-US，待对照原页）

````text
24
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 25 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=25)

### 原始文字层

````text
25
The Algorithm
 A root object is an operating system object
 Let O be a set of objects which does not include any root
object, and P be the set containing all the predecessors of 
the objects in O. If P O, then objects in O are garbage.
A
B C D E
root

Of A B L
DI­PS
a
有指出
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Th e Algorithm
object is an operating system object
囗 r00 忄
Let 0 be a set of objects which does
include any root
no 忄
囗
object, and P be the set containing the predecessors of
the objects in 0 工 f P 匚 0 then objects in 0 are garbage.
厂 。 0
root
25
````

### 图片文字 OCR（en-US，待对照原页）

````text
The Algorithm
object is an operating system object
o A root
Let O be a set of objects which does not include any root
object, and P be the set containing all the predecessors of
the objects in O. If
GO, then objects in O are garbage.
ft-58
root
25
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 26 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=26)

### 原始文字层

````text
26
A
B C D E
root
O = {A, B, C, D}
P = {C, A, B}
garbage
include garbage
can be
ran
by root fr­ee
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
root
26
````

### 图片文字 OCR（en-US，待对照原页）

````text
lye
root
OJ*e
26
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 27 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=27)

### 原始文字层

````text
27
 The algorithm is going to pass some probes to discover the 
predecessor relationship
A
B C D E
root l
a
有 比 姚
一 A weight
A 二 时 0
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Th e algorithm is going 忄 0 paSS some probes 忄 0 discover the
predecessor relationship
root
27
````

### 图片文字 OCR（en-US，待对照原页）

````text
The algorithm is going to pass some probes to discover the
predecessor relationship
root
27
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 28 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=28)

### 原始文字层

````text
28
 The probes will be sent back to the initiator of 
the algorithm
 How do we know whether we have received all the probes 
so that we can start looking for cyclic structures?
 Each probe carries some weight. When a probe p
is split into n probes, p1, p2, ..., pn, 
 all the (object, predecessor) pairs in p are copied to p1, 
 p.w = p1.w + p2.w + ... + pn.w, 
 ∑ pi.initiator = p.initiator where 1 ≤ i ≤ n.
 How do we know whether we have found all the 
predecessors of a node?
 Compare the weight of the node and the sum of the 
weight of the references to the node (assume the 
weighted reference counting is used)
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
The probes will be sent back to the initiator of
the algorithm
How do we know whether we have received all the probes
O
so that we can start looking for cyclic structures?
Each probe carries some weight. When a probe p
is split into n probes, pl, p2
pn,
all the (object, predecessor) pairs in p are copied to pl,
O
p.w = pl.w + p2.w +
O
+ pn.W,
pi.initiator= p.initiator where 1 < i < n.
O
o How do we know whether we have found all the
predecessors of a node?
Compare the weight of the node and th su of the
O
weight of th r erences to the node (assume the
weighted reference counting is used)
28
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 29 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=29)

### 原始文字层

````text
29
A B
C
D
E F
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
29
````

### 图片文字 OCR（en-US，待对照原页）

````text
29
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 30 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=30)

### 原始文字层

````text
30
A B
C
D
E
w = 10
A  B
rw = 0
F
eturn weight
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
w = 1 0
A 兮 B
rw = 0
fi 砌 仂 比
30
````

### 图片文字 OCR（en-US，待对照原页）

````text
w = 10
rw=0
we;oh€
30
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 31 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=31)

### 原始文字层

````text
31
A B
C
D
E
w = 5
A  B, B  D
rw = 0
F
只有 一 个继承前面的信息
o
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
A 兮 B 兮 D
````

### 图片文字 OCR（en-US，待对照原页）

````text
rw=0
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 32 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=32)

### 原始文字层

````text
32
A B
C
D
E
rw = 0
w = 2
B  C, C  E
F
w = 3
C  F
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
rw = 0
w = 2
B 兮 C, C 兮 E
C 兮 F
32
````

### 图片文字 OCR（en-US，待对照原页）

````text
32
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 33 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=33)

### 原始文字层

````text
33
A B
C
D
E
rw = 8
F
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
33
````

### 图片文字 OCR（en-US，待对照原页）

````text
rw=8
33
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 34 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=34)

### 原始文字层

````text
34
A B
C
D
E
rw = 10
F
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
rw = 1 0
34
````

### 图片文字 OCR（en-US，待对照原页）

````text
rw=10
34
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 35 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=35)

### 原始文字层

````text
35
review
 What problem does the reference counting garbage collection 
algorithm might have in a distributed system?
 Describe how the weighted reference counting garbage collection 
algorithm works.
 Why does the weighted reference counting garbage collection 
algorithm not have the problem encountered by the reference 
counting garbage collection algorithm?
 Understand how the algorithm for detecting cyclic garbage works.
 In the algorithm for collecting cyclic garbage, how do we know 
whether the probes have reached an object through all the 
predecessors of the object? [hint: the algorithm works as a 
complement of other garbage collection algorithms, e.g., weighted 
reference counting ]
 Use the principles of the weighted reference counting to develop 
an algorithm that finds a set of nodes in a wait-for graph such 
that the outgoing edges from the nodes in this set always end on 
nodes in this set. (it would be possible to detect deadlock in the 
OR deadlock model using this algorithm)
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
review
What problem does the reference counting garbage collection
algorithm might have in a distributed system?
Describe how the weighted reference counting garbage collection
algorithm works.
Why does the weighted reference counting garbage collection
algorithm not have the problem encountered by the reference
counting garbage collection algorithm?
Understand how the algorithm for detecting cyclic garbage works.
In the algorithm for collecting cyclic garbage, how do we know
whether the probes have reached an object through all the
predecessors of the object? [hint: the algorithm works as a
complement of other garbage collection algorithms, e.g., weighted
reference counting ]
Use the principles of the weighted reference counting to develop
an algorithm that finds a set of nodes in a wait-for graph such
that the outgoing edges from the nodes in this set always end on
nodes in this set. (it would be possible to detect deadlock in the
OR deadlock model using this algorithm)
35
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 36 页

[查看此页](../../../../notes/original/711/1/S6%2Bgarbage-collection.pdf#page=36)

### 原始文字层

````text
36
Further reading
 P.Watson and I.Watson. An efficient 
garbage collection scheme for parallel 
computer architectures.PARLE'87, LNCS 
259:432-443, Springer Verlag, 1987 
(weighted reference counting)
 X.Ye , J. Keane, Collecting Cyclic Garbage 
in Distributed Systems, Proceedings of the 
1997 International Symposium on Parallel 
Architectures, Algorithms and Networks
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Further reading
P.Watson and I.Watson. An efficient
garbage collection scheme for parallel
computer architectures.PARLEI 87, LNCS
259:432-443, Springer Verlag, 1987
(weighted reference counting)
X. Ye , J. Keane, Collecting Cyclic Garbage
in Distributed Systems, Proceedings of the
1997 International Symposium on Parallel
Architectures, Algorithms and Networks
36
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

