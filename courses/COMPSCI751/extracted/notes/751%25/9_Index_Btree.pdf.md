# 9_Index_Btree.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI751/notes/original/751%25/9_Index_Btree.pdf`
- [打开原文件](../../../notes/original/751%2525/9_Index_Btree.pdf)
- 原文件 SHA-256：`1d92b0b5b9a74ff855881838e37ec64bb4df22c8f665b97547b39b5808e7b322`
- 文件索引：F151；PDF 总页数：106
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=1)

### 原始文字层

````text
Miao Qiao
The University of Auckland
Index
References: 
-- Section 14, Database System Concepts
-- Chapter 17, Fundamentals of Database Systems
-- Database course, CMU
2weeks
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
lndex
References ：
- Section 14 ， Database System Concepts
- Chapter 17 ， FundamentaIs Of Database Systems
- Database course, CMU
Miao Qiao
The University Of AuckIand
00 TH E UNIVERSITYOF
AUCKLAND
№ Wana.nga 0 Timaki 鬥 《 k r 》 u
N E W Z E A L A N D
````

### 图片文字 OCR（en-US，待对照原页）

````text
Index
-- Section 14, Database System Concepts
-- Chapter 17, Fundamentals of Database Systems
- Database course, CMU
Miao Qiao
The University of Auckland
THE UNIVERSITYOF
AUCKLAND
Te Whare Wananga o Tamaki Makaurau
NEW ZEALAND
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=2)

### 原始文字层

````text
Basic Concepts
▪ Why use indexes?
• To speed up access to desired data.
▪ How to indicate the desired data?
• Search Key - attribute used to look up records in a file.
▪ The basic structure of an index file 
• records (called index entries) of the form
▪ Index Evaluation Metrics
• Access types supported efficiently. E.g., 
▪ Records with a specified value in the attribute
▪ Records with an attribute value falling in a specified range of values.
• Access time, Insertion time, Deletion time, Space overhead
▪ Types of indices:
• Ordered indices: search keys are stored in sorted order
• Hash indices: search keys are distributed uniformly across “buckets”
using a “hash function”. 
search-key pointer
co
efficiency
where xxx
鱻 no
me_
index entries
o­oo
均匀分布
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
． 才 丿 丿
0
TH E UNIVERSIT 丫 OF
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Basic Concepts
Why use indexes?
TO ee up ccess tO desired data.
HOW tO in ℃ a e the desired data?
Search Key - attribute used tO lOOk up records in a file.
The basic structu re Of an index file
records (called index ent ies) Of the form
0
lndex Evaluation Metrics
Access types supported efficiently. E.g.
search-ke
pointer
Records with a specified value in the attribute
Records with an att ri bute value falling in a specified range f values.
Access time, lnsertion time, DeIetion time, Space overhead
Types Of indices.
Ordered indices: search ke ys re stored i sorted order
Hash indices: search ke ys are distributed uniformly across
using a "hash function"
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Basic Concepts
Why use indexes?
To ee up ccess to desired data.
How to in Ica e the desired data?
Search Key - attribute used to look up records in a file.
•
The basic structure of an index file
records (called index ent ies) of the form
Index Evaluation Metrics
Access types supported efficiently. E.g.,
search-ke
Fade*
pointer
Records with a specified value in the attribute
Records with an attribute value falling in a specified range f values.
Access time, Insertion time, Deletion time, Space overhead
Types of indices:
Ordered indices: search keys re stored i sorted order
Hash indices: search keys are distributed uniformly across "buckets"
using a "hash function"
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=3)

### 原始文字层

````text
Ordered Indices
▪ In an ordered index, index entries are stored sorted on the search key value.
▪ Primary index
▪ Clustering index
▪ Secondary index
▪ Dense index
▪ Sparse index
群集
密度
稀疏
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
． 才 丿 丿
0
Ordered lndices
TH E UNIVERSIT 丫 OF
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
0
0
0
0
0
ln an ordered index, index entries are stored SO rted on the search ke y value.
Primary index
Clustering index
Se 0 index
Dense index
Sparse index
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Ordered Indices
•
In an ordered index, index entries are stored sorted on the search key value.
Primary index
Clustering index
Sep ary index
Dense index
Sparse index
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=4)

### 原始文字层

````text
Primary Indexes
▪ In a sequentially ordered file, the index whose search key specifies the 
sequential order of the file.
o
primary key
primary index
primary index tile
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
． 才 丿 丿
0
Primary lndexes
TH E UNIVERSIT 丫 OF
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
。 ln a sequentially ordered file, the index whose search k ey specifies the
sequential order Of the file.
BIO anchor
pnmary key
v 訕 羽
Aaron„ Ed
Adams 」 0 №
AJexander ， Ed
， Troy
Anderson, Zach
炮 巧 ， Mack
Data
Ssn B.trth date 」 ob S
pointer
Name
Aaron, Ed
Abb0t ， Diane
Acosta, Marc
Ad 谑 ， 」 n
Ad 即 ， Robin
Akers ， 」
陶 ex d 釧 Ed
A 皂 d ， BOb
AIÉn, Sam
AIIen, Troy
Anders, K 卣
Anderson, R0b
Anderson ， Zach
An 0
Archer, Sue
ArnoId, Mac:k
ArnOld ，
A 旧 s ， Tlt-nothy
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
• In a sequentially ordered file, the index whose search key specifies the
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Primary Indexes
sequential order of the file.
Data file
k
d)
Name
Aaron, Ed
Abbot, Diane
Acosta, Marc
Adarns, John
Adams, Robin
Akers, Jan
Alexzlder, Ed
Alfred, Bob
Allen, Sam
Allen, Troy
Anders, Keith
Anderson, Rob
Anderson, Zach
An*l, Jce
Archer, Sue
Arnold, Mack
Arnold,
Atkins, Timothy
Ssn Birth date Job S
ked
Index file
enmes)
Block ary±or
prirnary key
value
Aaron, Ed
Adams, John
Alexander, Ed
Alen, Troy
Anderson, Zach
Arnold, Mack
pointer
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=5)

### 原始文字层

````text
Primary Indexes (two-level)
second levelindex
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
Primary lndexes (two-level)
Two-level index
Data
24
29
35
36
39
44
46
52
55
58
66
78
80
82
85
89
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Second (top)
35
55
85
First (base)
level
35
39
44
55
80
85
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Primary Indexes (two-level)
Data file
Prirnary
key field
12
24
29
35
36
39
41
44
46
51
52
55
58
66
71
78
80
82
85
89
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Two-level index
secohd [e
Second (top)
35
55
85
First (base)
level
15
24
I ince
35
39
44
51
55
71
80
85
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=6)

### 原始文字层

````text
Clustering Index
▪ Sequential file ordered on a 
search key, with a clustering 
index on the search key. 聚类 duplicated
point block
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
． 才 丿 丿
0
0
CIus ering lndex
Sequential file ordered on a
search key, with a clustering
index on the search key.
TH E UNIVERSIT 丫 OF
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
Data file
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Custering
field)
| ndex fi
(<K(i) ， P(i)> entries)
Custering
field value
1
2
3
4
5
6
8
Block
pinter
Dept_number Name Ssn 」 0b Birth_date SaIary
1
1
1
2
2
3
3
3
3
3
4
4
5
5
5
5
6
6
6
6
6
8
8
8
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Clus ering Index
Sequential file ordered on a
search key, with a clustering
index on the search key.
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Data file
Custering
field)
Index file
(<K(i), P(i)> entries)
Clustering
field value
2
3
4
5
6
8
Block
pointer
Dept_number Name Ssn Job Birth_date Salary
1
1
1
2
2
3
3
3
3
3
4
4
5
5
5
5
6
6
6
6
6
8
8
8
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=7)

### 原始文字层

````text
Secondary Index
▪ An index whose search key 
specifies an order different 
from the sequential order of 
the file. Also called 
nonclustering index.
非聚类
quality each
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Secondary lndex
An index wh ose search k ey
specifies an order different
from the sequential order Of
the file. Also called
nonclustering index.
lndex fi
(<K(D, P(i)> entries)
lndex
俑 value
10
12
13
14
16
17
18
19
20
22
23
24
引 k
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
Data
吊 四 絎 d
(secondary
key
17
24
20
23
14
12
22
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Secondary Index
An index whose search key
specifies an order different
from the sequential order of
the file. Also called
nonclustering index.
Index file
entries)
Index
field value
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
Block
pointer
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Data file
Indexing field
(secondary
key field)
13
15
17
21
11
16
24
10
20
23
18
14
12
19
22
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=8)

### 原始文字层

````text
Dense index
▪ Index record appears for every search-key value in the file. E.g. index on 
ID attribute of instructor relation 
• Secondary index must be dense ns.O
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Dense index
lndex record appears for every search-key value in the file.
ID attribute Of s uc 厂 relation
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
E.g. index on
Secondary index must be
10101
12121
15151
22222
32343
33456
45565
58583
76543
76766
83821
98345
10101
12121
15151
22222
32343
33456
45565
58583
76543
76766
83821
98345
ense
Srinivasan
Wu
Mozart
Einstein
EI Said
Gold
Katz
Califieri
Singh
Crick
Brandt
Kim
Comp. Sci.
Finance
Music
Physics
History
Physics
Comp. Sci.
History
Finance
Biology
Comp. Sci.
Elec. Eng.
65000
90000
40000
95000
60000
87000
75000
62000
80000
72000
92000
80000
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Dense index
•
Index record appears for every search-key value in the file. E.g. index on
ID attribute of instructor relation
Secondary index must be
10101
12121
15151
22222
32343
33456
45565
58583
76543
76766
83821
98345
10101
12121
15151
22222
32343
33456
45565
58583
76543
76766
83821
98345
ense
Srinivasan
wu
Mozart
Einstein
El Said
Gold
Katz
Califieri
Singh
Crick
Brandt
Kim
Comp. Sci.
Finance
Music
Physics
History
Physics
Comp. Sci.
History
Finance
Biology
Comp. Sci.
Elec. Eng.
65000
90000
40000
95000
60000
87000
75000
62000
80000
72000
92000
80000
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=9)

### 原始文字层

````text
Sparse index
▪ Contains index records for only some search-key values.
• Applicable when records are sequentially 
ordered on search-key
▪ To locate a record with search-key value K we:
• Find index record with largest 
search-key value < K
• Get the pointer
• Sequential read the data file
• Example:
▪ Find 2
▪ Find 5
i
see 2 level
graph
````

### 图片文字 OCR（en-US，待对照原页）

````text
Sparse index
Contains index records for only some search-key values.
Applicable when records are sequentially
ordered on search-key
To locate a record with search-key value K we:
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Data file
(Custering
field)
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
e Salary
Find index record with largest
search-key value < K
Get the pointer
Sequential read the data file
Example:
Find 2
Find 5
Index file
(<K(i), P(i)> entries)
Clustering
field value
2
3
4
5
6
8
Block
pointer
Dept_number Name Ssn Job Birth_
1
1
1
2
2
3
3
3
4
4
5
5
5
5
6
6
6
6
6
8
8
8
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=10)

### 原始文字层

````text
Ordered Indices
▪ In an ordered index, index entries are stored sorted on the search key value. 
▪ Clustering index: in a sequentially ordered file, the index whose search key 
specifies the sequential order of the file.
• Also called primary index
• The search key of a primary index is usually but not necessarily the primary key.
▪ Secondary index: an index whose search key specifies an order different from the 
sequential order of the file. Also called nonclustering index.
▪ Index-sequential file: sequential file ordered on a search key, with a clustering 
index on the search key.
▪ Dense index — Index record appears for every search-key value in the file. E.g. 
index on ID attribute of instructor relation 
▪ Sparse Index: contains index records for only some search-key values.
• Applicable when records are sequentially ordered on search-key
▪ To locate a record with search-key value K we:
• Find index record with largest search-key value < K
• Search file sequentially starting at the record to which the index record points
graph
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Ordered Indices
•
•
In an ordered index, index entries are stored sorted on the search key value.
Clustering index: in a sequentially ordered file, the index whose search key
specifies the sequential order of the file.
Also called primary index
The search key of a primary index is usually but not necessarily the primary key.
Secondary index: an index whose search key specifies an order different from the
sequential order of the file. Also called nonclustering index.
Index-sequential file: sequential file ordered on a search key, with a clustering
index on the search key.
Dense index — Index record appears for every search-key value in the file. E.g.
index on ID attribute of instructor relation
Sparse Index: contains index records for only some search-key values.
Applicable when records are sequentially ordered on search-key
To locate a record with search-key value K we:
Find index record with largest search-key value < K
Search file sequentially starting at the record to which the index record points
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=11)

### 原始文字层

````text
Sparse index – How to update?
ftp 氦
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Sparse index 一
Two-level index
Sec
First (base)
level
24
(top)
35
39
44
85
55
63
80
85
0 一 date?
Data
keyfield
24
29
35
36
39
44
46
52
55
58
66
78
80
82
85
89
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Sparse index —
Two-level index
OW-tO-•u
Data
key field
12
15
21
24
29
35
36
39
41
44
46
52
55
58
66
71
78
80
82
85
89
date?
Sec
85
(top)
First (base)
level
15
24
35
39
44
51
55
63
71
80
85
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=12)

### 原始文字层

````text
7
B-Tree Family
There is a specific data structure called a B-Tree.
People also use the term to generally refer to a class of
balanced tree data structures:
→ B-Tree (1970)
→ B+Tree (1973)
→ B*Tree (1977?)
→ Blink-Tree (1981)
→ B𝛆-Tree (2003)
→ Bw-Tree (2013)
o
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
B-Tree Family
There is a specific data structure called a
People also use the term to generally refer to a class of
b
tree data structures:
1970)
B+ ree 973)
ree 977?)
Blink-Tree (1981 )
BE—Tree (2003)
Bw-Tree (2013)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=13)

### 原始文字层

````text
B+Tree
AB+Tree is a self-balancing, ordered m-way tree for searches,
sequential access, insertions, and deletions in O(logm n) I/Os
where m is the tree fanout, n is the number of keys. 
→ It is perfectly balanced (i.e., every leaf node is at the same depth in the tree)
→ Every node other than the root is at least half-full
m/2-1 ≤ k ≤ m-1, k: # of keys in the node
→ Every inner node with k keys has k+1non-null children.
→ Optimized for reading/writing large data blocks.
Some real-world implementations relax these properties, but
we will ignore that for now…
龇
13
hi hat然
每个节点有 my
ˋ 䪂
-
鬯 _
1
尹
尛 M 4
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
SCIENCE
AUCKLAND
0
DEPARTMENT OF
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
COMPUTER SCIENCE
B+Tree
A B+Tree is se ba 《 ordered for searches,
sequential access, and deletions in O(logm n) I/Os
where m is the tree fanout, n is the number Of ke S ．
乛 lt is perfectly balanced (i.e., eve leaf node
th sam depth in the tree)
乛 Eve node Other than the root is at leas half-ful
m ． 1 k m ． 1 ， k: # 0 keys in the node
乛 Every inner node with k keys h as k+l non-null children.
乛 Optimized fO r reading/writing large data blocks.
Some real-world implementations re 《 ax these properties, but
we will ignore that fO r now. 。
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
SCIENCE
AUCKLAND
DEPARTMENT OF
Wln•ng• o Timüi
COMPUTER SCIENCE
NEW ZEALAND
B+Tree
sawh 90 order
is a self-balåff&Æ, ordered for searches,
sequential access, in—ons, and deletions in O(logm n) VOs
where mis the tree fanout, n is the number of ke s.
It is perfectly balanced (i. e. , every leaf node
th sam depth in the tree)
Every node other than the root is at leas half-ful
m/2-1 k m-1, k: # of keys in the node
Every inner node with k keys has k+l non-null children.
Optimized for reading/writing large data blocks.
Some real-world implementations relax these properties, but
we will ignore that for now...
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=14)

### 原始文字层

````text
B+Tree
10 35
6
20
10 20 31 38 44
M 3
at
ty mode is block
oo
oo
左都小于 右 都大于 2
新 等于1 1
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
． 才 丿 丿
0
TH E UNIVERSIT 丫 OF
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
B+Tree
10
6
先 针 1 、 弓
10
20
20
35
31
38
44
9
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
B+Tree
10
6
I\DJ
10
node i's
20
20
35
31
38
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
lost
44
(19)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=15)

### 原始文字层

````text
10 35
6
RootNode
Inner/ Non-Leaf 
Nodes
Leaf Nodes
20
10 20 31 38 44
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
20
灭 oo No
6
10
10
20
35
31
No $
38 44 LeafNodes
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
20
RootN0de
6
10
10
20
35
31
Inner/ Non-Leaf
Nodes
38 44 LeafN0des
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=16)

### 原始文字层

````text
IndexKey(s) Low→High
10 35
6
RootNode
Inner/ Non-Leaf 
Nodes
Leaf Nodes
20
10 20 31 38 44
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
20
6
10
10
灭 oo No
35
20 31
No $
38 44 LeafNodes
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
20
6
10
10
RootN0de
35
20 31
Inner/ Non-Leaf
Nodes
38 44 LeafN0des
Index Key(s) Low—Migh
````

### 图表辅助说明

B+ 树分三层：根分隔键 20；中间节点示例为 10、35；底部叶节点包含 6、10、20/31、38/44。底部箭头表明索引键从左到右递增，父节点通过分支引导查找。

## PDF 第 17 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=17)

### 原始文字层

````text
IndexKey(s) Low→High
B+TREEEXAMPLE
10 35
6
RootNode
Inner/ Non-Leaf 
Nodes
Leaf Nodes
20
<node*>|<key>|<node*>|…|<key>|<node*>
10 20 31 38 44
_pointer
phlod
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
． 才 丿 丿
0
<node*>l<key>l<node*>l...l<key>l<no e*>
灭 oo No
20
TH E UNIVERSIT 丫 OF
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
6
10
10
35
20 31
No $
38 44 LeafNodes
````

### 图片文字 OCR（en-US，待对照原页）

````text
20
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
intef
RootN0de
block
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
6
10
10
35
20 31
Inner/ Non-Leaf
Nodes
38 44 LeafN0des
Index Key(s) Low—Migh
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 18 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=18)

### 原始文字层

````text
IndexKey(s) Low→High
B+TREEEXAMPLE
10 35
6
RootNode
Inner/ Non-Leaf 
Nodes
Leaf Nodes
20
<node*>|<key>|<node*>|…|<key>|<node*>
10 20 31 38 44
<key>|<value>|<key>|<value>
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
． 才 丿 丿
0
TH E UNIVERSIT 丫 OF
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
<node*>l <key> 《 <node*> 《 … l<key> 《 <node*>
20
6
10
10
灭 oo No
35
20 31
No $
38 44 LeafNodes
< key> 《 <value> 《 < key> 《 <value>
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
I <key> I <node*> I ... I I <node*>
20
6
10
10
RootN0de
35
20 31
Inner/ Non-Leaf
Nodes
38 44 LeafN0des
Index Key(s) Low—Migh
<key> I <value> I <key> I <value>
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 19 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=19)

### 原始文字层

````text
IndexKey(s) Low→High
B+TREEEXAMPLE
10 35
6
Inner/ Non-Leaf 
Nodes
Leaf Nodes
<20
RootNode
≥20
<10 ≥10 <35 ≥35
20
<node*>|<key>|<node*>|…|<key>|<node*>
10 20 31 38 44
<key>|<value>|<key>|<value>
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
． 才 丿 丿
0
TH E UNIVERSIT 丫 OF
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
<node*>l <key> 《 <node*> 《 … l<key> 《 <node*>
20
< 10
6
< 20
10
10
10
灭 oo No
20
35
< 35
20 31
No $
35
38 44 LeafNodes
< key> 《 <value> 《 < key> 《 <value>
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
I <key> I <node*> I ... I I <node*>
20
6
10
210
10
RootN0de
220
35
20 31
Inner/ Non-Leaf
Nodes
235
38 44 LeafN0des
Index Key(s) Low—Migh
<key> I <value> I <key> I <value>
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 20 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=20)

### 原始文字层

````text
IndexKey(s) Low→High
B+TREEEXAMPLE
10 35
6
RootNode
Inner/ Non-Leaf 
Nodes
Leaf Nodes
Sibling Pointers <20 ≥20
<10 ≥10 <35 ≥35
20
<node*>|<key>|<node*>|…|<key>|<node*>
<key>|<value>|<key>|<value>
10 20 31 38 44
<node*>|<key>|<value>|…|<key>|<value>|<node*>
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
I <key> I <node*> I ... I I <node*>
20
RootN0de
220
Sibling Pointers
10
35
6
210
10
20 31
Inner/ Non-Leaf
Nodes
235
38 44 LeafN0des
Index Key(s) Low—Migh
<node*> I <key> I <value> I ... I <key> I <value> I <node*>
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 21 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=21)

### 原始文字层

````text
IndexKey(s) Low→High
6 10 20 31 38 44 Leaf Nodes
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
6
10
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
20 31
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Leaf Nodes
Index Key(s) Low—Migh
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 22 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=22)

### 原始文字层

````text
Nodes
Every B+Tree node is comprised of an array of 
key/value pairs.
→ The keys are derived from the index's target attribute(s).
→ The values will differ based on whether the node is 
classified as an inner node or a leaf node.
The arrays are (usually) kept in sorted key order. 
Store all NULL keys at either first or last leaf nodes.
2
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Nodes
Every B+Tree node is comprised of an array of
key/value pairs.
The keys are derived from the index's target attribute(s).
-+ The values will differ based on whether the node is
classified as an inner node or a leaf node.
The arrays are (usually) kept in sorted key order.
Store all NULL keys at either first or last leaf nodes.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 23 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=23)

### 原始文字层

````text
B+TreeLeaf Node
¤ K1 V1 ••• Kn Vn ¤
Prev Next
B+Tree Leaf Nodes 23
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
B+Tree Leaf Nodes
B + 丑 “ 厂 No
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
B + Tree
Leaf Nodes
B+TreeLeafN0de
Prev
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Next
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 24 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=24)

### 原始文字层

````text
B+TreeLeaf Node
K1 V1 ••• Kn
Prev
¤
Next
PageID Vn ¤ PageID
B+Tree Leaf Nodes 24
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
． 才 丿 丿
0
B+Tree Leaf Nodes
B + 丑 “ 厂 No
TH E UNIVERSIT 丫 OF
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
Next
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
````

### 图片文字 OCR（en-US，待对照原页）

````text
B + Tree
Leaf Nodes
B+TreeLeafN0de
Prev
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Next
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
PagelD
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 25 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=25)

### 原始文字层

````text
B+TreeLeaf Node
Key+Value
¤ K1 V1 ••• Kn Vn ¤
Prev Next
PageID PageID
B+Tree Leaf Nodes 25
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
B+Tree Leaf Nodes
B + 丑 “ 厂 No
````

### 图片文字 OCR（en-US，待对照原页）

````text
B+Tree Leaf Nodes
B+TreeLeafN0de
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Next
PagelD
Prev
KI VI
KO'+Value
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
PagelD
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 26 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=26)

### 原始文字层

````text
B+TreeLeaf Node
Key+Value
V1 ••• Vn
Prev Next
PageID ¤ K1 ¤ Kn ¤ ¤ PageID
B+Tree Leaf Nodes 26
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
B+Tree Leaf Nodes
B + 丑 “ 厂 No
````

### 图片文字 OCR（en-US，待对照原页）

````text
B+Tree Leaf Nodes
B+TreeLeafN0de
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Next
PagelD
Prev
KO'+Value
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
PagelD
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 27 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=27)

### 原始文字层

````text
¤ ¤
Next
# #
B+TreeLeaf Node
Level Slots Prev
27
SortedKey/Value Pairs
K1 ¤ K2 ¤ K3 ¤
K4 ¤ K5 ¤ •••
B+Tree Leaf Nodes
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
B+Tree Leaf Nodes
B + 丑 “ 厂 No
e / S 户
SortedKe “ e 户 “
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
Next
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
B+Tree Leaf Nodes
B+TræLeafN0de
Level Slots
Prev
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Next
Sorted Ke /Value Pairs
KI ÄÆ<2
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 28 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=28)

### 原始文字层

````text
SortedKeys
K1 K2 K3 K4 K5 ••• Kn
¤ ¤
Next
# #
B+TreeLeaf Node
Level Slots Prev
Values
¤ ¤ ¤ ¤ ¤ ••• ¤
B+Tree Leaf Nodes 28
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
B+Tree Leaf Nodes
B + 丑 “ 厂 No
e / S 户
SortedK $
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
Next
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
B + Tree
Leaf Nodes
B+TræLeafN0de
Level Slots Prev
SortedK s
KI K2
v
Next
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 29 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=29)

### 原始文字层

````text
Approach #1: Record IDs
→ A pointer to the location of the tuple to 
which the index entry corresponds.
→ Most common implementation.
Approach #2: Tuple Data
→ Index
-Organized Storage 
→ Primary Key Index: Leaf nodes store the 
contents of the tuple.
→ Secondary Indexes: Leaf nodes store 
tuples' primary key as their values.
Leaf Node Values
1
s￾o
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
L
Node Values
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Microsoft'
Approa #1 : Record IDs
—+ ointer o the location of the tuple to
which t e index entry corresponds.
Most common implementation.
Approach #2: Tuple Data
Index-Organized Storage
PostgreSQL
ndex: Leaf nodes store the
-9 primary
ü\MgSQC
ontent of the tuple.
—5 Secondary Indexes: Leaf nodes store
tuples' primary key as their values.
SQL Server
Microsoft'
SQLServer
ORACLE'
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 30 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=30)

### 原始文字层

````text
B-Tree VS B+Tree 31
• The original B-Tree from 1971 stored keys and values in all nodes in the tree.
• More space-efficient, since each key only appears once in the tree.
• A B+Tree only stores values in leaf nodes. Inner nodes only guide the search 
process. 0 00 0
不存Tape
Bt 内部节点只存pointer 的
优点 能有更多子节点
遍历路更短
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
B-Tree VS B+Tree
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
The original B-Tree from 1971 stO red keys and values in all nodes in the tree.
More space-efficient, since each key only appears once in the tree.
the search
驴 丨 巛 的 “ 儋
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
B-Tree VS B+Tree
The original B-Tree from 1971 stored keys and values in all nodes in the tree.
More space-efficient, since each key only appears once in the tree.
B+ ree only stores alue •n eaf node Inner nodes onl gui
the search
p cess.
134 %
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 31 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=31)

### 原始文字层

````text
Find correct leaf node L.
Insert data entry into L in sorted order.
If L has enough space, done!
Otherwise, split L keys into L and a new node L2
→ Redistribute entries evenly, copy up middle key.
→ Insert index entry pointing to L2 into the parent of L.
To split inner node, redistribute entries evenly, but push 
up middle key.
B+Tree Insert 32
often 有 锏 直接插入
无尘间
c
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
B+Tree lnsert
Find correct leaf node L.
lnsert d ata entry intO L in sorted order.
0
If L has enough space, done!
Otherwise, split L keys int0 L and a new node L2
乛 Redistribute entries evenly, COPY up middle key.Q•e•••-
乛 lnsert index entry pointing tO L2 intO the parent Of Lg-
TO split inner node, redistribute entries evenly, but push
up middle key.
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
32
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
B+Tree Insert
Find correct leaf node L.
Insert data entry into L in sorted order.
If L has enough space, done!
Otherwise, split L keys into L and a new node 1-2
Redistribute entries evenly, copy up middle key.Q•-.-
Insert index entry pointing to 1-2 into the parent of LC
To split inner node, redistribute entries evenly, but push
up middle key.
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
32
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 32 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=32)

### 原始文字层

````text
≥12
1 3 5 9 10 12 13
4 12
33
<4
B+Tree Insert
1 3
4 12
[4,12)
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
B+Tree lnsert
< 4
1
3
4
5
12
圃 12 》
9
12
10
12
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
13
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
B+Tree Insert
[4,12)
212
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 33 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=33)

### 原始文字层

````text
≥12
1 3 5 9 10 12 13
4 12
Insert 6
35
<4 [4,12) ≥12
1 3 5 9 10 12 13
4 12
<
4 12
[4,12)
一
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
35
lnsert
6
1
< 4
3
4
5
12
圃 12 》
9
12
10
12
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
13
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
35
Insert
6
[4,12)
212
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 34 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=34)

### 原始文字层

````text
≥12
1 3 5 9 10 12 13
4 12
Insert 6
36
[4,12)
Node isfull!
<4
4 12
1 3
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
36
lnsert
6
1
< 4
3
4
5
12
圃 12 》
9
12
10
12
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
13
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
36
Insert
6
[4,12)
212
Node isfull!
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 35 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=35)

### 原始文字层

````text
1 3 5 9 10 12 13
4 12
Insert 6
37
<4 [4,12)
4 12
1 3
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
6
< 4
4
12
圃 12 》
12
13
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
6
[4,12)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 36 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=36)

### 原始文字层

````text
1 3 5 9 10 12 13
4 12
Insert 6
38
<4 [4,12)
4 12
1 3
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
6
< 4
4
12
圃 12 》
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
6
[4,12)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 37 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=37)

### 原始文字层

````text
1 3 5 6 12 13
4 12
Insert 6
9 10
39
<4 [4,12)
4 12
1 3
均分 若做不到均分
first node larger
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
． 才 丿 丿
0
TH E UNIVERSIT 丫 OF
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
6
1
4
< 4
3
12
圃 12 》
9 10
12
13
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
6
[4,12)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 38 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=38)

### 原始文字层

````text
1 3 5 6 12 13
4 12
Insert 6
9 10
40
<4 [4,12)
4 12
1 3
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
6
1
4
< 4
3
12
圃 12 》
9
10
12
13
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
6
[4,12)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 39 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=39)

### 原始文字层

````text
1 3 5 6 12 13
4 12
Insert 6
9 10
41
<4 [4,12)
1 3
4 12
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
6
1
4
< 4
3
12
圃 12 》
9
10
12
13
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
6
1
3
5
[4,12)
6
9
10
12
13
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 40 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=40)

### 原始文字层

````text
<4
1 3 5 6 12 13
4 ? 12
Insert 6
9 10
4
[4,12)
1 3 5 6 9 10
tiny
smallest value of
new
block
0
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
0
lnsert
6
1
4
< 4
3
12
0
圃 12 》
9
snßlles+
10
12
13
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
6
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
swlles+ 11/0811
[4,12)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 41 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=41)

### 原始文字层

````text
<4
1 3 5 6 12 13
4 ? 12
Insert 6
9 10
4
[4,12)
1 3 5 6 9 10
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
6
1
< 4
3
0
圃 12 》
9
10
12
13
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
6
[4,12)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 42 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=42)

### 原始文字层

````text
<4
1 3 6 12 13
?
Insert 6
9 10
44
[4,12)
4 9 12
1 3 5 6 9 10
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
6
1
4
9
圃 12 》
< 4
3
12
9
10
12
13
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
6
[4,12)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 43 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=43)

### 原始文字层

````text
<4
1 3 5 6 12 13
?
Insert 6
9 10
4
4 9 12
1 3 5 6 9 10
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
6
1
4
< 4
3
9
12
9
10
12
13
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
6
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 44 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=44)

### 原始文字层

````text
<4
1 3 5 6 12 13
?
Insert 6
9 10
46
4 9 12
[4,9) [9,12) ≥12
1 3 5 6 9 10
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
6
1
4
9
圃 9 ）
12
942 》
< 4
3
9
12
10
12
13
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
6
[4,9)
9,12)
212
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 45 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=45)

### 原始文字层

````text
1 3 12 13
4 9 12
9 10
47
Insert 6
Insert 8
1 3 5 6 9 10
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
lnsert
6
8
1
3
4
5
9
6
12
9
10
12
13
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
Insert
6
8
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 46 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=46)

### 原始文字层

````text
1 3 12 13
4 9 12
9 10
48
Insert 6
Insert 8
1 3 5 6 9 10
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
lnsert
6
8
1
3
4
5
9
6
12
9
10
12
13
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
Insert
6
8
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 47 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=47)

### 原始文字层

````text
1 3 12 13
4 9 12
9 10
49
Insert 6
Insert 8
1 3 5 6 88 9 10
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
lnsert
6
8
1
3
4
5
9
6
12
8
9
10
12
13
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
Insert
6
8
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 48 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=48)

### 原始文字层

````text
18
1 3 5 7 9 11 13 14 15 20 21 23
5 9 13 19
Insert 17
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
13 19
17
5
9
13 14 5
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
20 21 23
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
17
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 49 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=49)

### 原始文字层

````text
18
1 3 5 7 9 11 20 21 23
5 9 13 19
13 14 15 17
Insert 17
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
13 19
13 14 5 17
17
5
9
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
20 21 23
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
17
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 50 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=50)

### 原始文字层

````text
19
1 3 5 7 9 11 13 14 15 17 20 21 23
5 9 13 19
Insert 17
Insert 16
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
lnsert
13 19
13 14 5 17
17
16
5
9
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
20 21 23
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
Insert
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
17
16
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 51 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=51)

### 原始文字层

````text
19
1 3 5 7 9 11 13 14 15 17 20 21 23
5 9 13 19
Nospace in the nodewhere 
the newkey “belongs”.
Insert 17
Insert 16
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
lnsert
13 19
17
16
5
9
13 4 5
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
20 21 23
Nospaæin the “ e
the new ， “
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
Insert
17
16
No in the nMe where
the new key "belongs".
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 52 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=52)

### 原始文字层

````text
19
1 3 5 7 9 11 13 14 15 17 20 21 23
5 9 13 19
Split the node!
Copy themiddle key. 
Pushthe key up.
Insert 17
Insert 16
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
lnsert
13 19
17
16
5
9
13 4 5
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
20 21 23
c 丿 k 莎
乃 the key ·
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
Insert
17
16
Splü the node!
Copy the middle key.
Push the key up.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 53 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=53)

### 原始文字层

````text
20
1 3 5 7 9 11 13 14 15 17 20 21 23
5 9 13 19
Insert 17
Insert 16
NewNode!
Shuffle keysfrom the node 
15 that triggered the split.
team
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
lnsert
13 19
13 14 5 17
17
16
5
9
20 2 23
No 钅 ， No /
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
Insert
17
16
NewN0de!
Shuffle keys from the nMe
that triggered the split.
4
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 54 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=54)

### 原始文字层

````text
20
1 3 5 7 9 11 13 14 15 17 20 21 23
5 9 13 19
Insert 17
Insert 16
NewNode!
Shuffle keysfrom the node 
that triggered the split.
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
lnsert
13 19
17
16
5
9
13
4
5
20 2 23
No 钅 ， No /
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
Insert
17
16
101010101
NewN0de!
Shuffle keys from the nMe
that triggered the split.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 55 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=55)

### 原始文字层

````text
1 3 5 7 9 11 13 14 15 20 21 23
5 9 13 19
16 17
Insert 17
Insert 16
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
lnsert
13 19
17
16
5
9
13 14 5
16
7
20 2 23
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
Insert
17
16
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 56 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=56)

### 原始文字层

````text
21
1 3 5 7 9 11 13 14 15 20 21 23
5 9 13 19
Insert 17
Insert 16
16 17
But this is an“orphan”node! 
Noparent nodepointsto it.
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
lnsert
13 19
17
16
5
9
13 14 5
16 7
20 2 23
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
Insert
17
16
But this is an "aphan"nme!
Noparent nMepoints to it.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 57 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=57)

### 原始文字层

````text
21
1 3 5 7 9 11 13 14 15 20 21 23
5 9 13 19 16
Insert 17
Insert 16
16 17
But this is an“orphan”node! 
Noparent nodepointsto it.
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
lnsert
13 19
17
16
5
9
16
13 14 5
16 7
20 2 23
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
Insert
17
16
But this is an "aphan"nme!
Noparent nMepoints to it.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 58 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=58)

### 原始文字层

````text
21
1 3 5 7 9 11 13 14 15 20 21 23
5 9 13 19 16
Want to create a key, pointer 
pair like this. But cannotinsert it 
in the root node,whichisfull.
16 17
But this is an“orphan”node! 
Noparent nodepointsto it.
Insert 17
Insert 16
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
Insert
17
16
Want to create a key, pointer
pair like this. Bm cannot insert it
in the root nme, which is full.
But this is an "aphan"nme!
Noparent nMepoints to it.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 59 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=59)

### 原始文字层

````text
21
1 3 5 7 9 11 13 14 15 20 21 23
5 9 13 19 16
Want to create a key, pointer 
pair like this. But cannotinsert it 
in the root node,whichisfull.
16 17
But this is an“orphan”node! 
Noparent nodepointsto it.
Split the root. Grow the tree!
Insert 17
Insert 16
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
Insert
17
16
Want to create a key, pointer
pair like this. Bm cannot insert it
in the root nme, which is full.
16 Split the root.
Grow the tree!
But this is an "aphan"nme!
Noparent nMepoints to it.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 60 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=60)

### 原始文字层

````text
1 3 5 7 9 11 13 14 15 20 21 23
5 9 13 19
16 17
16 Split the root. Grow the tree!
Insert 17
Insert 16
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
lnsert
13 19
17
16
5
9
16
Split the root. Grow the tree!
13 14 5
16
7
20 2 23
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
Insert
17
16
16
Split the root. Grow the tree!
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 61 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=61)

### 原始文字层

````text
22
1 3 5 7 9 11 13 14 15 20 21 23
5 9
13
19
16 17
16 Split the root. Grow the tree!
Insert 17
Insert 16
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
lnsert
17
13
16
19
16
Split the root. Grow the tree!
13 14 5
16
7
20 2 23
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
Insert
17
13
16
16
Split the root. Grow the tree!
````

### 图表辅助说明

插入动画中的分裂步骤：红框突出新键 16 与叶节点 16/17，并提示 Split the root, Grow the tree。图展示分裂向上传播的中间状态；完整树结构需连同相邻动画页阅读。

## PDF 第 62 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=62)

### 原始文字层

````text
23
1 3 5 7 9 11 13 14 15 20 21 23
5 9 16 19
16 17
13
Next, need to split the “old”root, then 
point to the split nodesfrom the newroot.
Insert 17
Insert 16
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
lnsert
17
16
5
9
13
16 19
耵 ， “ e the ' ， root, e ”
the 犰 “ 歹 the e ” root.
13 14 5
16 17
20 2 23
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
Insert
17
16
Next, need to split the "ü'root, then
point to the split n&from the new root.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 63 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=63)

### 原始文字层

````text
24
1 3 5 7 9 11 13 14 15 20 21 23
5 9
16 17
13
16 19
Insert 17
Insert 16
卡 1E ka5
z Ek
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
lnsert
17
16
斟 0 旧 圓
13
13 14 5
16 19
16 17
20 2 23
乙
之
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
Insert
17
13
16
16 19
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 64 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=64)

### 原始文字层

````text
24
1 3 5 7 9 11 13 14 15 20 21 23
5 9
16 17
13
16 19
<13 ≥13
Insert 17
Insert 16
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert
lnsert
16 19
16 17
17
16
斟 0 旧 圓
13
< 13
13
13 14 5
20 2 23
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
Insert
17
16
13
213
16 19
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 65 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=65)

### 原始文字层

````text
24
1 3 5 7 9 11 13 14 15 20 21 23
5 9
16 17
13
16 19
<5 [5,9) [9,13) [13,16) [16,19) ≥19
<13 ≥13
Insert 17
Insert 16
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
lnsert
lnsert
16 19
16 17
17
16
斟 0 旧 圓
[ 5
13
< 13
13 ）
13
[ 13,1 司
13 14 5
[ 篁 649 》
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
19
20 2 23
````

### 图片文字 OCR（en-US，待对照原页）

````text
Insert
Insert
17
16
[5,9)
13
[9,13)
213
16 19
[13,16)
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
[16,19)
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
219
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 66 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=66)

### 原始文字层

````text
Exercises
1. If index entries are inserted in sorted order, what will be the occupancy of 
each leaf node in a B+-tree? Explain why.
2. If the fanout of the B+-tree is m and its height is 3, what are:
1. The maximum number of leaf nodes?
2. The minimum number of leaf nodes?
似
4Gj.nu
morethan lyft
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Exercises
half@(
2 ．
If index entries are inserted in sorted order, what will be the occupancy Of
each leaf node in a B+-tree? Explain why.
If the fanout 0f the B+-tree is m nd its height is 3 ， what are:
The maximu m number Of leaf nodes?
2 ．
The minimum number Of leaf nodes?
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Exercises
2.
If index entries are inserted in sorted order, what will be the occupancy of
each leaf node in a B+-tree? Explain why.
L/tatftl(
If the fanout of the B+-tree ism nd its height is 3, what are:
The maximum number of leaf nodes?
2.
The minimum number of leaf nodes?
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 67 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=67)

### 原始文字层

````text
Start at root, find leaf L where entry belongs. Remove the
entry.
If L is at least half-full, done! If L has only
m/2-1 entries (recall that m is the tree fanout),
→ Try to re-distribute, borrowing from sibling (adjacent node with same 
parent as L).
→ If re-distribution fails, merge L and sibling.
If merge occurred, must delete entry (pointing to L or sibling) 
from parent of L.
B+Tree Delete 68
o_o
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
B+Tree Delete
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Start at root, find leaf L where entry belongs. Remove the
entry.
least half-f , done! If L has only
m/2-1 en I s recall tha is the tree fanout),
Try to re-distributel borrowing from si In (adjacent node with same
parent as L).
If re-distribution fails erg
and sibling.
If merge occurred, must delete entry (pointing to L or sibling)
from parent of L.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 68 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=68)

### 原始文字层

````text
26
1 3 5 9 10
4 12
9 10 12
9
6
Delete 6
4 9
1 3 5 6
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
6
1
扈 《 囗 《
3
5
6
9
10
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
2
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
6
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 69 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=69)

### 原始文字层

````text
26
1 3 5 9 10
4 12
9 10 12
9
6
Delete 6
4 9
1 3 5 6
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
6
1
扈 《 囗 《
3
5
6
9
10
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
2
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
6
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 70 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=70)

### 原始文字层

````text
1 3 5 96 10
4 12
9 10 12
9
Delete 6
4 9
1 3
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
6
1
3
扈 《 囗 《
5
9
10
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
2
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
6
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 71 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=71)

### 原始文字层

````text
1 3 5 9 10
4 12
9 12 14
9
Delete 6
4 9
1 3
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
6
1
3
扈 《 囗 《
5
9
12
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
4
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
6
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 72 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=72)

### 原始文字层

````text
27
1 3 5 9 10
4 12
9 12 14
9
Delete 6
Borrowfrom a “rich”sibling node. 
Couldborrowfrom eithersibling.
4 9
1 3
到
KaKEt­了e
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
Delete
6
1
3
扈 《 囗 《
5
． 才 丿 丿
0
9 12 4
一 嫔 弁
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
6
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Borrowfrom a 'WI" sibling node.
Could borrowfrom either sibling.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 73 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=73)

### 原始文字层

````text
27
1 3 5 9 10
4 12
9 12 14
9
Delete 6
Borrowfrom a “rich”sibling node. 
Couldborrowfrom eithersibling.
4 9
1 3
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
6
1
3
扈 《 囗 《
5
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
9 12 4
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
6
Borrowfrom a 'WI" sibling node.
Could borrowfrom either sibling.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 74 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=74)

### 原始文字层

````text
28
1 3 5 9 10
4 9
9 12 14
Delete 6
Need to update parent node!
4 9
1 3 5 9
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
6
1
扈 《 囗 《
3
5
9
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
12 14
Needto 尹 “ e 刊
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
6
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Need to updateparent nMe!
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 75 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=75)

### 原始文字层

````text
28
1 3 5 9 10
4 9
9 12 14
≥9
Delete 6
Need to update parent node!
4 9
1 3 5 9
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
6
1
扈 《 囗 《
3
5
9
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
12 14
Needto 尹 “ e 刊
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
6
29
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Need to updateparent nMe!
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 76 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=76)

### 原始文字层

````text
4 9
28
1 3 5 9 10
9
9 12 14
≥9
Delete 6
Need to update parent node!
1 3 5 9
o
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
6
1
3
5
9
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
14
12
Need
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
6
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Need pdateparent nMe!
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 77 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=77)

### 原始文字层

````text
1 3 5 9 10
4 9
12 14
12
9
≥12
Delete 6
Need to update parent node!
4 12
1 3 5 9
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
6
1
3
4
5
12
9
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
12
12 14
Needto 尹 “ e 刊
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
6
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
212
Need to updateparent nMe!
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 78 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=78)

### 原始文字层

````text
2
1 3 5 7 9 11 13 15 17 19 20 21 23
5 9 17 21
Delete 15 13
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
17 21
13 15
2 篁 23
15
13
7 19 20
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
15
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 79 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=79)

### 原始文字层

````text
13 15
29
1 3 5 7 9 11 15 17 19 20 21 23
5 9 17 21
Delete 15 13
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
17 21
2 篁 23
15
13
7 19 20
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
15
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 80 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=80)

### 原始文字层

````text
13 15
29
1 3 5 7 9 11 15 17 19 20 21 23
5 9 17 21
Delete 15 13
Borrowfrom a “rich”sibling node.
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
17 21
2 篁 23
15
13
7 19 20
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
15
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Borrowfrom a 'WI" sibling node.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 81 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=81)

### 原始文字层

````text
1 3 5 7 9 11 13 15 17 19 20 21 23
5 9 17 21
Delete 15 13
Borrowfrom a “rich”sibling node.
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
17 21
2 篁 23
15
13
7 19 20
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
15
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Borrowfrom a 'WI" sibling node.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 82 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=82)

### 原始文字层

````text
30
1 3 5 7 9 11 13 17 19 20 21 23
5 9 17 21
Delete 15 13
Need to update parent node!
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
17 21
13 17
9 20
15
13
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
2 篁 23
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
15
Need to updateparent nMe!
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 83 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=83)

### 原始文字层

````text
30
1 3 5 7 9 11 13 17 19 20 21 23
5 9 17 21
Delete 15 13
Need to update parent node!
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
17 21
13 17
9 20
15
13
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
2 篁 23
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
15
17 21
Need to updateparent nMe!
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 84 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=84)

### 原始文字层

````text
30
1 3 5 7 9 11 13 17 19 20 21 23
5 9 17
Delete 15 13
19 21
Need to update parent node!
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
19 21
13 17
9 20
15
13
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
2 篁 23
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
15
19 21
Need to updateparent nMe!
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 85 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=85)

### 原始文字层

````text
31
1 3 5 7 9 11 13 17 19 20 21 23
5 9 19 21
Delete 15 13
Delete 19
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
DeIete
Delete
19 21
13 17
9 20
2 篁 23
15
19
13
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
Delete
15
19
19 21
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 86 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=86)

### 原始文字层

````text
31
1 3 5 7 9 11 13 17 19 20 21 23
5 9 19 21
Delete 15 13
Delete 19
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
DeIete
Delete
19 21
13 17
2 篁 23
15
19
13
20
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
Delete
15
19
19 21
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 87 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=87)

### 原始文字层

````text
31
1 3 5 7 9 11 13 17 19
5 9 19 21
Delete 15 13
Delete 19
20
Under-filled!
21 23
No“rich”sibling nodesto borrow. 
Mergewith a sibling
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
DeIete
Delete
15
19
13
13 17
19 21
2
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
21 3
No ' ， 产 $ / ” borrow.
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
Delete
15
19
19 21
Under-filled!
No 'WI" sibling nodes to borrow.
Merge with a sibling
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 88 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=88)

### 原始文字层

````text
31
1 3 5 7 9 11 13 17 19
5 9 19 21
Delete 15 13
Delete 19
20
Under-filled!
21 23
No“rich”sibling nodesto borrow. 
Mergewith a sibling
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
DeIete
Delete
15
19
13
13 17
19 21
2
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
21 3
No ' ， 产 $ / ” borrow.
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
Delete
15
19
19 21
Under-filled!
No 'WI" sibling nodes to borrow.
Merge with a sibling
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 89 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=89)

### 原始文字层

````text
1 3 5 7 9 11 13 17 19
5 9 19 21
Delete 15 13
Delete 19
20
Under-filled!
21 23
No“rich”sibling nodesto borrow. 
Mergewith a sibling
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
DeIete
Delete
15
19
13
13 17
19
2
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
21 3
No ' ， 产 $ / ” borrow.
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
Delete
15
19
Under-filled!
No 'WI" sibling nodes to borrow.
Merge with a sibling
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 90 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=90)

### 原始文字层

````text
32
1 3 5 7 9 11 13 17 20 21 23
5 9 19
13
This node is 
under-filled! 
Pull-down.
Delete 15
Delete 19
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
DeIete
Delete
13 17
15
19
13
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
19
20 21 23
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
nMe
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
Delete
15
19
This nMe is
under-filled!
Pull-down.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 91 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=91)

### 原始文字层

````text
32
1 3 5 7 9 11 13 17 20 21 23
5 9 19
13
This node is 
under-filled! 
Pull-down.
Delete 15
Delete 19
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
DeIete
Delete
13 17
15
19
13
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
19
20 21 23
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
nMe
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
Delete
15
19
This nMe is
under-filled!
Pull-down.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 92 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=92)

### 原始文字层

````text
32
1 3 5 7 9 11 13 17 20 21 23
5 9 13 19
This node is 
under-filled! 
Pull-down.
Delete 15
Delete 19
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
DeIete
15
Delete
19
O 旧 圓
13 17
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
19
20 21 23
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
nMe
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
Delete
15
19
This nMe is
under-filled!
Pull-down.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 93 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=93)

### 原始文字层

````text
32
1 3 5 7 9 11 13 17 20 21 23
5 9 13 19
This node is 
under-filled! 
Pull-down.
Delete 15
Delete 19
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
DeIete
15
Delete
19
O 旧 圓
13 17
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
19
20 21 23
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
nMe
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
Delete
15
19
This nMe is
under-filled!
Pull-down.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 94 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=94)

### 原始文字层

````text
33
1 3 5 7 9 11 13 17 20 21 23
5 9 13 19
The tree hasshrunk in height.
Delete 15
Delete 19
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
DeIete
15
Delete
19
5 9 13 19
13 17
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
20 21 23
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
Delete
15
19
The tree has shrunk in height.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 95 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=95)

### 原始文字层

````text
33
1 3 5 7 9 11 13 17 20 21 23
5 9 13 19
The tree hasshrunk in height.
<5 [5,9) [9,13) [13,19) ≥19
Delete 15
Delete 19
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
DeIete
Delete
13 17
15
19
[ 5
5 9 13 19
[ 9 ， 13 ）
[ 1349 》
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
19
20 21 23
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Delete
Delete
15
19
The tree has shrunk in height.
[5,9)
[9,13)
[13,19)
219
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 96 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=96)

### 原始文字层

````text
Queries on B+-
Trees
▪ If there are n search-key values in the file, the height of the tree is no 
more than logm/2(n).
▪ A node is generally the same size as a disk block, typically 4 kilobytes
• and m is typically around 100 (40 bytes per index entry).
▪ With 1 million search key values and m = 100
• at most log50(1,000,000) = 4 nodes are accessed in a lookup 
traversal from root to leaf.
▪ Contrast this with a balanced binary tree with 1 million search key values 
— around 20 nodes are accessed in a lookup
• above difference is significant since every node access may need a 
disk I/O, costing around 20 milliseconds
h 69凹 n
o
Oqtk B
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
． 才 丿 丿
0
Queries on B+-Trees
TH E UNIVERSIT 丫 OF
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
If there are 冂 search-key values in the file, the eight f the tree i n
more than 自
2 （ ．
A node is generally the same size as a disk IOC typically 4 kllobytes
and m is typically around 100 （ 40 bytes per inde try).
With 1 million search ke y values and m = 100
at most / 0g50 （ 1 ， 000 ， 000 ） = 4 nodes are accessed in a lookup
trave rsal from root to leaf.
Contrast this with a balanced binary tree with 1 million search ke y values
around 20 nodes are accessed in a lOOkup
above difference iS significant since evety node access may need a
disk 《 ℃ ， costing around 20 milliseconds
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Queries on B+-Trees
If there are n search-key values in the file, the eight f the treei n
more than r I
A node is generally the same size as a disk loc , typically 4 kilobytes
and m is typically around 100 (40 bytes per inde try).
With 1 million search key values and m = 100
at most loco(l = 4 nodes are accessed in a lookup
traversal from root to leaf.
Contrast this with a balanced binary tree with 1 million search key values
— around 20 nodes are accessed in a lookup
above difference is significant since every node access may need a
disk 1/0, costing around 20 milliseconds
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 97 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=97)

### 原始文字层

````text
Complexity of Updates
▪ Cost (in terms of number of I/O operations) of insertion and deletion of a 
single entry proportional to height of the tree
• With n entries and maximum fanout of m, worst case complexity of 
insert/delete of an entry is O(logm/2(n))
▪ In practice, number of I/O operations is less:
• Internal nodes tend to be in buffer
• Splits/merges are rare, most insert/delete operations only affect a leaf 
node
▪ Average node occupancy depends on insertion order
• 2/3rds with random, ½ with insertion in sorted order
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Complexity of Updates
•
Cost (in terms of number of 1/0 operations) of insertion and deletion of a
single entry proportional to hei ht of the tree
With n entries and maximum fanout of m, worst case complexity of
insert/delete of an entry is O(logrm/
In practice, number of 1/0 operations i less:
Internal nodes end to be In buffer
Splits/merges are rare, most insert/delete operations only affect a leaf
node
Average node occupancy depends on insertion order
2/3rds with random, 1/2 with insertion in sorted order
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 98 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=98)

### 原始文字层

````text
Bulk Loading and Bottom-Up Build
▪ The fastest way to build a new B+Tree for an existing table is to first sort 
the keys and then build the index from the bottom up.
▪ Keys: 3, 7, 9, 13, 6, 1.
▪ Sorted Keys: 1, 3, 6, 7, 9, 13
Why bulk loading is better than insertion-based B+Tree construction?
6 9
1 3 6 7 9 13
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Bulk Loading and Bottom-Up Build
The fastest way to build a new B+Tree for an existing table is to first sort
the keys and then build the index from the bottom up.
Keys: 3, 7, 9, 13, 6, 1.
Sorted Keys: 1, 3, 6, 7, 9, 13
Why bulk loading is better than insertion-based B+Tree construction?
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 99 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=99)

### 原始文字层

````text
Bulk Loading and Bottom-Up Build
▪ Inserting entries one-at-a-time into a B+-tree requires  1 IO per entry 
• assuming leaf level does not fit in memory
• can be very inefficient for loading a large number of entries at a time 
(bulk loading) 
▪ Efficient alternative 1:
• sort entries first (using efficient external-memory sort algorithms)
• insert in sorted order
▪ a leaf needs to be written out only once
▪ much improved IO performance, but most leaf nodes half full
▪ Efficient alternative 2: Bottom-up B+-tree construction
• As before sort entries
• And then create tree layer-by-layer, starting with leaf level
▪ details as an exercise
• Implemented as part of bulk-load utility by most database systems
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Bulk Loading and ottom-Up Build
• Inserting entries one-at-a-time Into
per entry
Ires
assuming leaf level does not fit in memory
can be vey inefficient for loading a large number of entries at a time
(bulk loading)
Efficient alternative 1 :
sort entries Irst using efficient external-memory sort algorithms)
insert in sorted order
a leaf needs to be written out only once
much improved 10 performance, but most leaf nodes half full
Efficient alternative 2: Bottom-up B+-tree construction
As before sort entries
And then create tree layer-by-layer, starting with leaf level
details as an exercise
Implemented as part of bulk-load utility by most database systems
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 100 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=100)

### 原始文字层

````text
Indexing Strings
▪ Variable length strings as keys
• Variable fanout
• Use space utilization as criterion for splitting, not number of pointers
▪ Prefix compression
• Key values at internal nodes can be prefixes of full key
▪ Keep enough characters to distinguish entries in the subtrees 
separated by the key value
• E.g., “Silas” and “Silberschatz” can be separated by “Silb”
• Keys in leaf node can be compressed by sharing common prefixes
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Indexing Strings
Variable length strings as keys
Variable fanout
Use space utilization as criterion for splitting, not number of pointers
Prefix compression
Key values at internal nodes can be prefixes of full key
Keep enough characters to distinguish entries in the subtrees
separated by the key value
E.g., "Silas" and "Silberschatz" can be separated by "Silb"
Keys in leaf node can be compressed by sharing common prefixes
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 101 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=101)

### 原始文字层

````text
FIN
Any questions?
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
00 THE UNIVERSITYOF
AUCKLAND
Te W № W “ 0 Timaki 孬 k “ r.u
N E W Z E A L A N 0
FIN
Any questions?
SCIENCE
````

### 图片文字 OCR（en-US，待对照原页）

````text
00 THE UNIVERSITYOF
AUCKLAND
Te Whare Wananga o Tamaki Yakaur•u
NEW ZEALAND
FIN
Any questions?
SCIENCE
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 102 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=102)

### 原始文字层

````text
Queries on B+-Trees
function find(v)
1. C=root
2. while (C is not a leaf node)
1. Let i be least number s.t. V  Ki
.
2. if there is no such number i then 
3. Set C = last non-null pointer in C
4. else if (v = C.Ki ) Set C = Pi +1 
5. else set C = C.Pi
3. if for some i, Ki = V then return C.Pi
4. else return null /* no record with search-key value v exists. */
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Queries on B+-Trees
function find(v)
C=root
while (C is not a leaf node)
2.
3.
4.
2.
3.
4.
5.
Let ibe least number s.t. V s Ki.
if there is no such number i then
Set C = last non-null pointer in C
else if c.Ki) Set C = Pl +1
else set C = C.Pi
if for some i, Ki = V then return C.Pi
else return null /* no record with search-key value v exists.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 103 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=103)

### 原始文字层

````text
Insert
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
． 才 丿 丿
0
lnsert
procedure e 0 户 ）
TH E UNIVERSIT 丫 OF
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
if (tree is empty) create an e mptY leaf node 厶 whic h is also the root
else Find the leaf node that should contain key value K
(L h as less than 一 1 key values)
then insert in 」 eaf ， K ， ）
el 跹 begm / * £ h as 烈 一 1 key values already ， split it * /
Create node 尸
Copy L.PI … L.Kn- 1 t0 a block 0f memory 丆 that c an
hold ” (pointer, key-value ） palrs
tnsertån 」 eaf （ 不 & 尹 ）
Set 尸 、 户 = LTn•, Set (Æ) “ 尸
Erase L 户 1 through LK 一 什 om L
Copy through TK from T into L at L.P
/ 2 ]
Copy 丆 肀 同 21 + 1 through TXn 什 om T into 尸 starting at 尸
Let K' be the smallest key-value in 尸
mserun-parent(), ℃ ， 尸 ）
end
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insert
procedure insert(va/ue K, pointer P)
if (tree is empty) create an empty leaf node L, which is also the root
else Find the leaf node L that should contain key value K
if (L has less than n — 1 key values)
then (L, K, P)
else begin / * L has n — I key values already, split it
Create node Lt
Copy L.PI L.Kn_1 to a block of memory T that can
hold n (pointer, key-value) pairs
insert-in-leaf ( T, K, P)
Set L'.Pn = Set -
Erase LYI through L.Kn_1 from L
Copy T Tl through TK from T into L starting at L.PI
In/21
Copy T.PI„/21+1 through T Xn from T into Lt starting at Lt.P1
Let K' be the smallest key-value in L'
insert-in-parent(L, K', L')
end
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 104 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=104)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
． 才 丿 丿
0
proc edure 忉 勖 」 e (node 厶 value K ， 0 r 户 ）
then insert 六 K into just before L.PI
else begm
Let K be the hlgh e st value in L that is less than or equ al to K
TH E UNIVERSIT 丫 OF
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
lnsert P,K 血 t0 L j ust after LX
end
procedure 忉 」 ” “ e N ， e K' ， node ' ）
(N is the root of the tree)
then begin
Create a new node 火 contaltung ， Kt N'
Make 火 the root of th e tree
return
end
（ has less th an pornters)
then insert (K', (') in 户 just after N
else begin 严 SpIit 尹 * /
严 and N' are potnters
Copy to a block of memory T that can hold 尹 and (Kt, N' ）
lnsert (K', N' ） into 丆 just after N
Erase 酣 entries 什 om 产 Create node 尸
Copy 丆 乃 … T 、 户
intO 户
知 + l) / 21
Let Ktt = 丆 、 K
厣 + 1)/21
T 、 + 1 tnto
Copy 丆
区 艹 l) / 21 + 《 ·
inserün-parent(P K" ， 户 ' ）
end
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
procedure insertän alegf (node L, value K, pointer P)
if(K < LXI)
then insert P, K into L just before L.PI
else begin
Let Kj be the highest value in L that is less than or equal to K
Insert P, K into L just after L.Kj
end
procedure insert-in-parent(node N, value K', node N')
if (N is the root of the tree)
then begin
Create a new node R containing N, K t N'
Make R the root of the tree
return
end
Let P — parent (N)
if (P has less than n pointers)
then insert N') in P just after N
else begin / * Split P
/ * N and N' are pointers
Copy P to a block of memory T that can hold P and N')
Insert N') into T just after N
Erase all entries from P; Create node P
copy T?
into P
((n+1)/21
Let K" = TX
into P
copy T?
insert-in-parent(P, K", P')
end
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 105 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=105)

### 原始文字层

````text
cio 9是每个块能存放的
鎏
nnnnnn
e
e Oo
une
了 叶子节计
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
B+Tree Batched Construction
Keys: 3 ， 7 ， 9 ， 13 ， 6 ， 1 ，
Sorted Keys: 1 ， 3 ， 6 ， 7 ， 9 ， 13
Then create tree layer-by-layer
bottom-up
3
Suppose YOIJ have a relation r wit tupie on wh ℃ h a e
is t0 be constructed, Assume each b!ocK hc{d 一
and that 削 levels 0f th e tree above the af are 旧 m,emory,
Give a formula f0 r the cost 0f build:ng the B+tree index by 的 s ？
t a time.
one recor
Give a formula f0 r the cost Of bu:!dng th e B+tree index by
the elation.
````

### 图片文字 OCR（en-US，待对照原页）

````text
B+Tree Batched Construction
Keys: 3, 7, 9, 13, 6, 1.
Sorted Keys: l, 3, 6, 7, 9, 13
Then create tree layer-by-layer
bottom-up
Suppose you have a relation r wit nr tuple on which a secondary B*tree
is to be constructed, Assume each b!ocK hold
and that all levels of the tree above the leaf are in memory.
C Give a formula for the cost of building the B+tree index by insert
t a time.
one recor
Give a formula for the cost of bu the B+tree index by
the elatiOn•
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 106 页

[查看此页](../../../notes/original/751%2525/9_Index_Btree.pdf#page=106)

### 原始文字层

````text
① 假设只有叶子节点在 e 磁盘
0 点
蠭涉放心 - 块数
每一次插入读写 1次工0
y ET
- 上节课排序
结论
有几个记录
M是缓飜放的块数
所以 I 0为 Ri O br 默认缓存无限大 内
部节点全在缓存中
and
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
工 (D C>St
刁 只 入 0 乜
阢 丿
````

### 图片文字 OCR（en-US，待对照原页）

````text
f
$-'/RüÄåWå
OCflp)
cost
O C Job),
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

