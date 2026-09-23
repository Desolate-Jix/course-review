# 10_Index_Hashing.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI751/notes/original/751%25/10_Index_Hashing.pdf`
- [打开原文件](../../../notes/original/751%2525/10_Index_Hashing.pdf)
- 原文件 SHA-256：`877a27e7dfd3a7fdde42741b1e8732c7044a89bea0a314898bbc1334687df061`
- 文件索引：F133；PDF 总页数：42
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=1)

### 原始文字层

````text
Miao Qiao
The University of Auckland
Index
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
lndex
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
Miao Qiao
The University of Auckland
THE UNIVERSITYOF
AUCKLAND
Te Whare Wananga o Tamaki Makaurau
NEW ZEALAND
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=2)

### 原始文字层

````text
Outline
▪ Basic Concepts
▪ Ordered Indices 
▪ B+-Tree Index Files
▪ B-Tree Index Files
▪ Hashing
▪ Write-optimized indices
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
Outline
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
0
0
0
0
0
0
Basic Concepts
Ordered lndices
B+-Tree lndex Files
B-Tree lndex Files
Hashing
Write-optimized indices
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Outline
Basic Concepts
Ordered Indices
B+-Tree Index Files
B-Tree Index Files
Hashing
Write-optimized indices
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=3)

### 原始文字层

````text
Hashing
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
Hashing
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Hashing
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=4)

### 原始文字层

````text
Example of Hash Index
hash index on instructor, on attribute ID
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
ExampIe 0f Hash lndex
bucket 0
76766
bucket 1
45565
76543
bucket 2
22222
bucket 3
10101
bu cket 4
bu cket 5
15151
33456
bucket 6
83821
bucket 7
12121
32343
58583
98345
76766
10101
45565
83821
98345
12121
76543
32343
58583
15151
22222
33465
hash
Crick
Srinivasan
Katz
Brandt
Kim
Wu
Singh
EI Said
Califieri
Mozart
Einstein
Gold
Biology
Comp. Sci.
Comp. Sci.
Comp · Sci.
Elec. Eng.
Finance
Finance
Hi story
Hi story
Music
Physics
Physics
index on S 亇 IJC
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
72000
65000
75000
92000
80000
90000
80000
60000
62000
40000
95000
87000
on attribute ID
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Example of Hash Index
bucket 0
76766
bucket 1
45565
76543
bucket 2
22222
bucket 3
10101
bucket 4
bucket 5
15151
33456
bucket 6
83821
bucket 7
12121
32343
58583
98345
76766
10101
45565
83821
98345
12121
76543
32343
58583
15151
22222
33465
Crick
Srinivasan
Katz
Brandt
Kim
wu
Singh
El Said
Califieri
Mozart
Einstein
Gold
Biology
Comp. Sci.
Comp. Sci.
Comp. Sci.
Elec. Eng.
Finance
Finance
History
History
Music
Physics
Physics
hash index on instructor,
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
72000
65000
75000
92000
80000
90000
80000
60000
62000
40000
95000
87000
on attribute ID
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=5)

### 原始文字层

````text
Static Hashing
▪ A bucket is a unit of storage containing one or more entries (a bucket 
is typically a disk block). 
• we obtain the bucket of an entry from its search-key value using a 
hash function
▪ Hash function h is a function from the set of all search-key values K to 
the set of all bucket addresses B.
▪ Hash function is used to locate entries for access, insertion as well as 
deletion.
▪ Entries with different search-key values may be mapped to the same 
bucket; thus entire bucket has to be searched sequentially to locate an 
entry. 
▪ In a hash index, buckets store entries with pointers to records
▪ In a hash file-organization buckets store records
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
Static Hashing
•
•
A bucket is a unit of storage containing one or more entries (a bucket
is typically a disk block).
we obtain the bucket of an entry from its search-key value using a
hash function
Hash function h is a function from the set of all search-key values K to
the set of all bucket addresses B.
Hash function is used to locate entries for access, insertion as well as
deletion.
Entries with different search-key values may be mapped to the same
bucket; thus entire bucket has to be searched sequentially to locate an
entry •
In a hash index, buckets store entries with pointers to records
In a hash file-organization buckets store records
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=6)

### 原始文字层

````text
Handling of Bucket Overflows
▪ Bucket overflow can occur because of 
• Insufficient buckets 
• Skew in distribution of records. This can occur due to two reasons:
▪ multiple records have same search-key value
▪ chosen hash function produces non-uniform distribution of key 
values
▪ Although the probability of bucket overflow can be reduced, it cannot be 
eliminated; it is handled by using overflow buckets.
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
Handling of Bucket Overflows
Bucket overflow can occur because of
Insufficient buckets
Skew in distribution of records. This can occur due to two reasons:
multiple records have same search-key value
chosen hash function produces non-uniform distribution of key
values
Although the probability of bucket overflow can be reduced, it cannot be
eliminated; it is handled by using overflow buckets.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=7)

### 原始文字层

````text
Handling of Bucket Overflows (Cont.)
▪ Overflow chaining – the overflow buckets of a given bucket are chained 
together in a linked list.
▪ Above scheme is called closed addressing (also called closed hashing 
or open hashing depending on the book you use) 
• An alternative, called 
open addressing 
(also called 
open hashing or
closed hashing 
depending on the 
book you use) which 
does not use over￾flow buckets, is not 
suitable for database 
applications.
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Overflow chaining — the overflow buckets of a given bucket are chained
together in a linked list.
Above scheme is called closed addressing (also called closed hashing
or open hashing depending on the book you use)
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
An alternative, called
open addressing
(also called
open hashing or
closed hashing
depending on the
book you use) which
does not use over-
flow buckets, is not
suitable for database
applications.
bucket 0
bucket 1
bucket 2
bucket 3
overflow buckets for bucket 1
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=8)

### 原始文字层

````text
Example of Hash File Organization 
Hash file organization of instructor file, using dept_name as key.
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
Examp le 0f Hash File Organization
Hash file organization Of s 亇 uc 厂 file, using dept_name as key.
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
bucket 0
bucket 1
bucket 2
32343 EI Said
58583 Califieri
bucket 3
22222 Einstein
33456 Gold
98345 Kim
bucket 4
12121 Wu
76543 Sin h
bucket 5
bucket 6
Finance
Finance
90000
80000
History
History
Ph sics
Physics
Elec. Eng.
80000
60000
95000
87000
80000
10101 Srinivasan Comp. Sci. 65000
Com ． Sci. 75000
45565 Katz
83821 Brandt Comp ． Sci. 92000
bucket 7
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Example of Hash File Organization
Hash file organization of instructor file, using dept_name as key.
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
bucket 0
bucket 1
15151 Mozart
bucket 2
32343 El Said
58583 Califieri
bucket 3
22222 Einstein
33456 Gold
98345 Kim
Music
History
History
Ph sics
Physics
Elec. Eng.
40000
80000
60000
95000
87000
80000
bucket 4
12121 wu
76543 Sin h
bucket 5
76766 Crick
bucket 6
Finance
Finance
Biolo
90000
80000
72000
10101 Srinivasan Comp. Sci. 65000
Com . Sci. 75000
45565 Katz
83821 Brandt Comp. Sci. 92000
bucket 7
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=9)

### 原始文字层

````text
Deficiencies of Static Hashing
▪ In static hashing, function h maps search-key values to a fixed set of B of 
bucket addresses. Databases grow or shrink with time. 
• If initial number of buckets is too small, and file grows, performance 
will degrade due to too much overflows.
• If space is allocated for anticipated growth, a significant amount of 
space will be wasted initially (and buckets will be underfull).
• If database shrinks, again space will be wasted.
▪ One solution: periodic re-organization of the file with a new hash function
• Expensive, disrupts normal operations
▪ Better solution: allow the number of buckets to be modified dynamically.
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
Deficiencies of Static Hashing
• In static hashing, function h maps search-key values to a fixed set of Bof
bucket addresses. Databases grow or shrink with time.
If initial number of buckets is too small, and file grows, performance
will degrade due to too much overflows.
If space is allocated for anticipated growth, a significant amount of
space will be wasted initially (and buckets will be underfull).
If database shrinks, again space will be wasted.
One solution: periodic re-organization of the file with a new hash function
Expensive, disrupts normal operations
Better solution: allow the number of buckets to be modified dynamically.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=10)

### 原始文字层

````text
Dynamic Hashing
▪ Periodic rehashing
• If number of entries in a hash table becomes (say) 1.5 times size of 
hash table, 
▪ create new hash table of size (say) 2 times the size of the 
previous hash table
▪ Rehash all entries to new table
▪ Linear Hashing
• Do rehashing in an incremental manner
▪ Extendable Hashing
• Tailored to disk based hashing, with buckets shared by multiple hash 
values
• Doubling of # of entries in hash table, without doubling # of buckets
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
Dynamic Hashing
Periodic rehashing
If number of entries in a hash table becomes (say) 1.5 times size of
hash table,
create new hash table of size (say) 2 times the size of the
previous hash table
Rehash all entries to new table
Linear Hashing
Do rehashing in an incremental manner
Extendable Hashing
Tailored to disk based hashing, with buckets shared by multiple hash
values
Doubling of # of entries in hash table, without doubling # of buckets
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=11)

### 原始文字层

````text
Extendable Hashing
▪ Extendable hashing – one form of dynamic hashing 
• Hash function generates values over a large range — typically b-bit 
integers, with b = 32.
• At any time use only a prefix of the hash function to index into a table 
of bucket addresses. 
• Let the length of the prefix be i bits, 0  i  32. 
▪ Bucket address table size = 2i. Initially i = 0
▪ Value of i grows and shrinks as the size of the database grows 
and shrinks.
• Multiple entries in the bucket address table may point to a bucket 
(why?)
• Thus, actual number of buckets is < 2i
▪ The number of buckets also changes dynamically due to 
coalescing and splitting of buckets.
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
Extendable Hashing
• Extendable hashing — one form of dynamic hashing
Hash function generates values over a large range — typically b-bit
integers, with b = 32.
At any time use only a prefix of the hash function to index into a table
of bucket addresses.
Let the length of the prefix be i bits, 0 < is 32.
Bucket address table size = 21• Initially i = 0
Value of i grows and shrinks as the size of the database grows
and shrinks.
Multiple entries in the bucket address table may point to a bucket
(why?)
Thus, actual number of buckets is < 21
The number of buckets also changes dynamically due to
coalescing and splitting of buckets.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=12)

### 原始文字层

````text
General Extendable Hash Structure 
In this structure, i2 = i3 = i, whereas i1 = i – 1 (see next slide for details)
i i1
i2
i3
bucket 1
bucket 2
bucket 3
00..
01..
10..
11..
bucket address table
hash prefix
…
…
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
General Extendable Hash Structure
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
hash prefix
00..
01..
10..
11..
bucket address table
In this structure, i2 = i3 = i, whereas
13
bucket 1
bucket 2
bucket 3
1 (see next slide for details)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=13)

### 原始文字层

````text
Use of Extendable Hash Structure
▪ Each bucket j stores a value ij
• All the entries that point to the same bucket have the same values on 
the first ij bits.
▪ To locate the bucket containing search-key Kj
:
1. Compute h(Kj
) = X
2. Use the first i high order bits of X as a displacement into bucket 
address table, and follow the pointer to appropriate bucket
▪ To insert a record with search-key value Kj
• follow same procedure as look-up and locate the bucket, say j. 
• If there is room in the bucket j insert record in the bucket. 
• Else the bucket must be split and insertion re-attempted (next slide.)
▪ Overflow buckets used instead in some cases (will see shortly)
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
Use of Extendable Hash Structure
Each bucket j stores a value ij
All the entries that point to the same bucket have the same values on
the first ij bits.
To locate the bucket containing search-key Kj:
Compute h(Kj) = X
Use the first i high order bits of Xas a displacement into bucket
2.
address table, and follow the pointer to appropriate bucket
To insert a record with search-key value Kj
follow same procedure as look-up and locate the bucket, say j.
If there is room in the bucket j insert record in the bucket.
Else the bucket must be split and insertion re-attempted (next slide.)
Overflow buckets used instead in some cases (will see shortly)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=14)

### 原始文字层

````text
Insertion in Extendable Hash Structure (Cont.) 
▪ If i > ij (more than one pointer to bucket j)
• allocate a new bucket z, and set ij = iz = (ij + 1)
• Update the second half of the bucket address table entries originally 
pointing to j, to point to z
• remove each record in bucket j and reinsert (in j or z)
• recompute new bucket for Kj and insert record in the bucket (further 
splitting is required if the bucket is still full)
▪ If i = ij (only one pointer to bucket j)
• If i reaches some limit b, or too many splits have happened in this 
insertion, create an overflow bucket 
• Else
▪ increment i and double the size of the bucket address table.
▪ replace each entry in the table by two entries that point to the same 
bucket.
▪ recompute new bucket address table entry for Kj
Now i > i
j
 so use the first case above. 
To split a bucket j when inserting record with search-key value Kj
:
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
Insertion in Extendable Hash Structure (Cont.)
To split a bucket j when inserting record with search-key value Kj:
If i > ij (more than one pointer to bucket J)
allocate a new bucket z, and set 0 = iz-
Update the second half of the bucket address table entries originally
pointing to j, to point to z
remove each record in bucket j and reinsert (in jor z)
recompute new bucket for Kj and insert record in the bucket (further
splitting is required if the bucket is still full)
If 1 = ij (only one pointer to bucket J)
If i reaches some limit b, or too many splits have happened in this
insertion, create an overflow bucket
Else
• increment i and double the size of the bucket address table.
replace each entry in the table by two entries that point to the same
bucket.
recompute new bucket address table entry for Kj
Now i > ij so use the first case above.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=15)

### 原始文字层

````text
Deletion in Extendable Hash Structure
▪ To delete a key value, 
• locate it in its bucket and remove it. 
• The bucket itself can be removed if it becomes empty (with appropriate 
updates to the bucket address table). 
• Coalescing of buckets can be done (can coalesce only with a “buddy”
bucket having same value of ij and same ij –1 prefix, if it is present) 
• Decreasing bucket address table size is also possible
▪ Note: decreasing bucket address table size is an expensive 
operation and should be done only if number of buckets becomes 
much smaller than the size of the table
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Deletion in Extendable Hash Structure
TO delete a key value,
locate it in its bucket and remove it.
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
The bucket itself can be removed if it becomes empty (with appropriate
updates to the bucket address table).
Coalescing of buckets can be done (can coalesce only with a "buddy/'
bucket having same value of ij and same ij—l prefix, if it is present)
Decreasing bucket address table size is also possible
Note: decreasing bucket address table size is an expensive
operation and should be done only if number of buckets becomes
much smaller than the size of the table
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=16)

### 原始文字层

````text
Use of Extendable Hash Structure: Example
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
Use of Exte ndab le Hash Strueture ： Example
叩 t_name
Biology
Comp. Sci.
Elec. Eng.
Finance
History
Music
Physics
h(dept—name)
0010 1101 1111 1011 0010 1100 0011 0000
1111 0001 0010 0100 1001 0011 0110 1101
0100 0011 1010 1100 1100 0110 1101 1111
1010 0011 1010 0000 1100 0110 1001 1111
1100 0111 1110 1101 1011 1111 0011 1010
0011 0101 1010 0110 1100 1001 1110 1011
1001 1000 0011 1111 1001 1100 0000 0001
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
Use of Extendable Hash Structure:
Example
dept_name
Biology
Comp. Sci.
Elec. Eng.
Finance
History
Music
Physics
h(dept_name)
0011 0101 1010 0110 1100 1001 1110 1011
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=17)

### 原始文字层

````text
Example (Cont.)
▪ Initial hash structure; bucket size = 2
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Exam p le (Cont.)
。 lnitial hash structure; bucket size = 2
hash prefix
0
bucket address table
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
0
bucket 1
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Example (Cont.)
• Initial hash structure; bucket size = 2
hash prefix
bucket address table
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
bucket 1
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 18 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=18)

### 原始文字层

````text
Example (Cont.)
▪ Hash structure after insertion of “Mozart”
, 
“Srinivasan”, and “Wu” records
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
0
Exam p le (Cont.)
Hash structure afte r insertion Of
hash prefix
bucket address table
Mozart"
Srinivasan
10101
12121 Wu
， and
' ' records
15151 Mozart
MLISic
40000
Sriniva san Comp. Sci. 90000
F inance
90000
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
Example (Cont.)
Hash structure after insertion of "Mozart", "Srinivasan'
and "Wu" records
hash prefix
bucket address table
15151
Mozart
10101
12121 wu
Music
40000
Srinivasan Comp. Sci. 90000
Finance
90000
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 19 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=19)

### 原始文字层

````text
Example (Cont.)
▪ Hash structure after insertion of Einstein record
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Exam p le (Cont.)
。 Hash structu re afte r insertion Of Einstein reco rd
hash prefix
bucket address table
15151 Mozart
12121 Wu
22222 Einstein
Music
Finance
Ph sics
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
40000
90000
95000
10101 Srinivasan Com
· Sci. 65000
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
Example (Cont.)
• Hash structure after insertion of Einstein record
hash prefix
bucket address table
15151 Mozart
12121 WU
22222 Einstein
Music
Finance
Ph sics
40000
90000
95000
10101 Srinivasan Com
. Sci. 65000
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 20 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=20)

### 原始文字层

````text
Example (Cont.)
▪ Hash structure after insertion of Gold and El Said records
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
Exam p le (Cont.)
Hash structu re afte r insertion of Gold and 曰 Said records
0
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
hash prefix
3
bu cke t address table
15151
22222
33456
12121
10101
32343
Mozart
Einstein
G01d
Wu
MLISic
Physics
Physi cs
F inance
Srinivasan · SCi.
EI Said History
40000
95000
87000
90000
65000
60000
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Example (Cont.)
Hash structure after insertion of Gold and El Said records
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
hash prefix
3
bucket address table
15151
22222
33456
12121
10101
32343
Mozart
Einstein
Gold
wu
Music
Physics
Physics
Finance
Srinivasan Com . Sci.
El Said History
40000
95000
87000
90000
65000
60000
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 21 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=21)

### 原始文字层

````text
Example (Cont.)
▪ Hash structure after insertion of Katz record
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Exam p le (Cont.)
Hash structure afte r insertion of Katz reco rd
0
hash prefix
3
bu cket address table
15151
22222
33456
12121
32343
10101
45565
Mozart
Einstein
Gold
Wu
EI Said
Music
Physics
Physics
F inance
History
Srinivasan Comp ． SCi.
Katz
Comp. Sci.
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
40000
95000
87000
90000
60000
65000
75000
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Example (Cont.)
Hash structure after insertion of Katz record
hash prefix
3
bucket address table
15151
22222
33456
12121
32343
10101
45565
Mozart
Einstein
Gold
wu
El Said
Music
Physics
Physics
Finance
History
Srinivasan Comp. Sci.
Katz
Comp. Sci.
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
40000
95000
87000
90000
60000
65000
75000
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 22 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=22)

### 原始文字层

````text
Example (Cont.)
And after insertion of 
eleven records
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Exam p le (Cont.)
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
And afte r insertion Of
eleven records
hash prefix
3
bucket address table
15151
76766
22222
33456
12121
76543
32343
58583
10101
45565
Mozart
Crick
Einstein
Gold
Wu
Singh
EI Said
Califieri
Music
Biology
Physics
Physics
Finance
F inance
History
History
Srinivasan Comp.
Sci.
Sci.
40000
72000
95000
87000
90000
80000
60000
62000
65000
75000
83821
Brandt
Com
· Sci.
92000
Katz
Comp.
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Example (Cont.)
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
And after insertion of
eleven recordS
hash prefix
3
bucket address table
15151
76766
22222
33456
12121
76543
32343
58583
10101
45565
Mozart
Crick
Einstein
Gold
wu
Singh
El Said
Califieri
Music
Biology
Physics
Physics
Finance
Finance
History
History
Srinivasan Comp.
Sci.
Sci.
40000
72000
95000
87000
90000
80000
60000
62000
65000
75000
83821
Brandt
Com
. Sci.
92000
Katz
Comp.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 23 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=23)

### 原始文字层

````text
Example (Cont.)
And after insertion of 
Kim record in previous 
hash structure
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Examp le
hash prefix
3
bucket address table
2 nt.
15151
76766
98345
22222
33456
12121
76543
32343
58583
10101
45565
Mozart
Crick
Kim
Einstein
Gold
Wu
Singh
EI Said
Califieri
MLISic
Biolog
Elec. En
Physics
Physics
Finance
Finance
History
History
40000
72000
80000
95000
87000
90000
80000
60000
62000
65000
75000
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
And afte r insertion Of
Kim record in previous
hash structu re
Srinivasan Comp.
Sci.
Sci.
83821
Brandt
Com
· Sci ·
92000
Katz
Comp.
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Example
hash prefix
3
bucket address table
15151
76766
98345
22222
33456
12121
76543
32343
58583
10101
45565
Mozart
Crick
Kim
Einstein
Gold
wu
Singh
El Said
Califieri
Music
Biolog
Elec. En
Physics
Physics
Finance
Finance
History
History
40000
72000
80000
95000
87000
90000
80000
60000
62000
65000
75000
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
And after insertion of
Kim record in previous
hash structure
Srinivasan Comp.
Sci.
Sci.
83821
Brandt
Com
. Sci.
92000
Katz
Comp.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 24 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=24)

### 原始文字层

````text
Extendable Hashing vs. Other Schemes
▪ Benefits of extendable hashing: 
• Hash performance does not degrade with growth of file
• Minimal space overhead
▪ Disadvantages of extendable hashing
• Extra level of indirection to find desired record
• Bucket address table may itself become very big (larger than memory)
▪ Cannot allocate very large contiguous areas on disk either
▪ Solution: B+-tree structure to locate desired record in bucket 
address table
• Changing size of bucket address table is an expensive operation
▪ Linear hashing is an alternative mechanism 
• Allows incremental growth of its directory (equivalent to bucket 
address table)
• At the cost of more bucket overflows
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Extendable Hashing vs. Other Schemes
Benefits of extendable hashing:
Hash performance does not degrade with growth of file
Minimal space overhead
Disadvantages of extendable hashing
Extra level of indirection to find desired record
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Bucket address table may itself become very big (larger than memory)
Cannot allocate very large contiguous areas on disk either
Solution: B+-tree structure to locate desired record in bucket
address table
Changing size of bucket address table is an expensive operation
Linear hashing is an alternative mechanism
Allows incremental growth of its directory (equivalent to bucket
address table)
At the cost of more bucket overflows
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 25 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=25)

### 原始文字层

````text
Comparison of Ordered Indexing and Hashing
▪ Cost of periodic re-organization
▪ Relative frequency of insertions and deletions
▪ Is it desirable to optimize average access time at the expense of worst￾case access time?
▪ Expected type of queries:
• Hashing is generally better at retrieving records having a specified 
value of the key.
• If range queries are common, ordered indices are to be preferred
▪ In practice:
• PostgreSQL supports hash indices, but discourages use due to poor 
performance
• Oracle supports static hash organization, but not hash indices
• SQLServer supports only B+-trees
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Comparison of Ordered Indexing and Hashing
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
•
•
Cost of periodic re-organization
Relative frequency of insertions and deletions
Is it desirable to optimize average access time at the expense of worst-
case access time?
Expected type of queries:
Hashing is generally better at retrieving records having a specified
value of the key.
If range queries are common, ordered indices are to be preferred
In practice:
PostgreSQL supports hash indices, but discourages use due to poor
performance
Oracle supports static hash organization, but not hash indices
SQLServer supports only B+-trees
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 26 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=26)

### 原始文字层

````text
Multiple-Key Access
▪ Use multiple indices for certain types of queries.
▪ Example: 
select ID
from instructor
where dept_name = 
“Finance” and salary = 80000
▪ Possible strategies for processing query using indices on single attributes:
1. Use index on dept_name to find instructors with department name 
Finance; test salary = 80000 
2. Use index on salary to find instructors with a salary of $80000; test
dept_name = “Finance”.
3. Use dept_name index to find pointers to all records pertaining to the 
“Finance” department. Similarly use index on salary. Take 
intersection of both sets of pointers obtained.
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
Multiple-Key Access
Use multiple indices for certain types of queries.
Example:
select ID
from instructor
where dept_name = "Finance" and salary = 80000
Possible strategies for processing query using indices on single attributes:
1. Use index on dept_name to find instructors with department name
Finance; test salary = 80000
2. Use index on salatyto find instructors with a salary of $80000; test
dept_name = "Finance' .
3. Use dept_name index to find pointers to all records pertaining to the
"Finance" department. Similarly use index on salary. Take
intersection of both sets of pointers obtained.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 27 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=27)

### 原始文字层

````text
Indices on Multiple Keys
▪ Composite search keys are search keys containing more than one 
attribute
• E.g., (dept_name, salary)
▪ Lexicographic ordering: (a1, a2) < (b1, b2) if either 
• a1 < b1, or 
• a1=b1 and a2 < b2
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
Indices on Multiple Keys
•
Composite search keys are search keys containing more than one
attribute
E.g., (dept_name, salary)
Lexicographic ordering: (al, a) < (bl, b2) if either
al < bl, or
al=bl and a2 < b2
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 28 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=28)

### 原始文字层

````text
Indices on Multiple Attributes
▪ With the where clause
 where dept_name = “Finance” and salary = 80000
the index on (dept_name, salary) can be used to fetch only records that 
satisfy both conditions.
• Using separate indices in less efficient — we may fetch many 
records (or pointers) that satisfy only one of the conditions.
▪ Can also efficiently handle 
 where dept_name = 
“Finance” and salary < 80000
▪ But cannot efficiently handle
 where dept_name < 
“Finance” and balance = 80000
• May fetch many records that satisfy the first but not the second 
condition
Suppose we have an index on combined search-key
(dept_name, salary).
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
Indices on Multiple Attributes
Suppose we have an index on combined search-key
(dept_name, salary).
With the where clause
where dept_name = "Finance" and salary = 80000
the index on (dept_name, salary) can be used to fetch only records that
satisfy both conditions.
Using separate indices in less efficient — we may fetch many
records (or pointers) that satisfy only one of the conditions.
Can also efficiently handle
where dept_name = "Finance" and salary< 80000
But cannot efficiently handle
where dept_name < "Finance" and balance = 80000
May fetch many records that satisfy the first but not the second
condition
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 29 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=29)

### 原始文字层

````text
Other Features
▪ Covering indices
• Add extra attributes to index so (some) queries can avoid fetching the 
actual records
• Store extra attributes only at leaf
▪ Why?
▪ Particularly useful for secondary indices 
• Why?
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
Other Features
•
Covering indices
Add extra attributes to index so (some) queries can avoid fetching the
actual records
Store extra attributes only at leaf
Why?
Particularly useful for secondary indices
Why?
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 30 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=30)

### 原始文字层

````text
Creation of Indices
▪ Example
 create index takes_pk on takes (ID,course_ID, year, semester, section)
 drop index takes_pk
▪ Most database systems allow specification of type of index, and 
clustering.
▪ Indices on primary key created automatically by all databases
• Why?
▪ Some database also create indices on foreign key attributes
• Why might such an index be useful for this query:
▪ takes ⨝ σname='Shankar' (student)
▪ Indices can greatly speed up lookups, but impose cost on updates
• Index tuning assistants/wizards supported on several databases to 
help choose indices, based on query and update workload
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
Creation of Indices
Example
•
•
create index takes_pkon takes (ID,course_lD, year, semester, section)
drop index takes_pk
Most database systems allow specification of type of index, and
clustering.
Indices on primary key created automatically by all databases
Some database also create indices on foreign key attributes
Why might such an index be useful for this query:
takes o
name—Shankar' (Student)
Indices can greatly speed up lookups, but impose cost on updates
Index tuning assistants/wizards supported on several databases to
help choose indices, based on query and update workload
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 31 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=31)

### 原始文字层

````text
Index Definition in SQL
▪ Create an index
create index <index-name> on <relation-name>
(<attribute-list>)
E.g.,: create index b-index on branch(branch_name)
▪ Use create unique index to indirectly specify and enforce the condition 
that the search key is a candidate key is a candidate key.
• Not really required if SQL unique integrity constraint is supported
▪ To drop an index 
drop index <index-name>
▪ Most database systems allow specification of type of index, and 
clustering.
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
Index Definition in SQL
Create an index
create index <index-name> on <relation-name>
(<attribute-list>)
E.g.,: create index b-index on branch(branch_name)
Use create unique index to indirectly specify and enforce the condition
that the search key is a candidate key is a candidate key.
Not really required if SQL unique integrity constraint is supported
To drop an index
drop index <index-name>
Most database systems allow specification of type of index, and
clustering.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 32 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=32)

### 原始文字层

````text
Write Optimized Indices
▪ Performance of B+-trees can be poor for write-intensive workloads
• One I/O per leaf, assuming all internal nodes are in memory
• With magnetic disks, < 100 inserts per second per disk
• With flash memory, one page overwrite per insert
▪ Two approaches to reducing cost of writes
• Log-structured merge tree
• Buffer tree
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
Write Optimized Indices
Performance of B+-trees can be poor for write-intensive workloads
One 1/0 per leaf, assuming all internal nodes are in memory
With magnetic disks, < 100 inserts per second per disk
With flash memory, one page overwrite per insert
•
Two approaches to reducing cost of writes
Log-structured merge tree
Buffer tree
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 33 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=33)

### 原始文字层

````text
Bloom Filters
▪ A bloom filter is a probabilistic data structure used to check membership 
of a value in a set
• May return true (with low probability) even if an element is not present
• But never returns false if an element is present
• Used to filter out irrelevant sets
▪ Key data structure is a single bitmap
• For a set with n elements, typical bitmap size is 10n
▪ Uses multiple independent hash functions
▪ With a single hash function h() with range=number of bits in bitmap:
• For each element s in set S compute h(s) and set bit h(s)
• To query an element v compute h(v), and check if bit h(v) is set
▪ Problem with single hash function: significant chance of false positive due 
to hash collision
• 10% chance with 10n bits
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
Bloom Filters
A bloom filter is a probabilistic data structure used to check membership
of a value in a set
May return true (with low probability) even if an element is not present
But never returns false if an element is present
Used to filter out irrelevant sets
Key data structure is a single bitmap
For a set with n elements, typical bitmap size is 10n
Uses multiple independent hash functions
With a single hash function h() with range=number of bits in bitmap:
For each element s in set S compute h(s) and set bit h(s)
To query an element v compute h(v), and check if bit h(v) is set
Problem with single hash function: significant chance of false positive due
to hash collision
10% chance with 1 On bits
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 34 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=34)

### 原始文字层

````text
Bloom Filters (Cont.)
▪ Key idea of Bloom filter: reduce false positives by use multiple hash 
functions hi
() for i = 1..k
• For each element s in set S for each i compute hi
(s) and set bit hi
(s)
• To query an element v for each i compute hi
(v), and check if bit hi
(v) is 
set
▪ If bit hi
(v) is set for every i then report v as present in set
▪ Else report v as absent
• With 10n bits, and k = 7, false positive rate reduces to 1% instead of 
10% with k = 1
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
Bloom Filters (Cont.)
Key idea of Bloom filter: reduce false positives by use multiple hash
functions hi() for k
For each element s in set S for each i compute hi(s) and set bit hi(s)
To query an element v for each i compute hi(v), and check if bit hi(v) is
set
• If bit hi(v) is set for every i then report v as present in set
Else report vas absent
With 10n bits, and k= 7, false positive rate reduces to 1% instead of
10% with k = 1
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 35 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=35)

### 原始文字层

````text
Log Structured Merge (LSM) Tree
▪ Consider only inserts/queries for 
now
▪ Records inserted first into in￾memory tree (L0 tree)
▪ When in-memory tree is full, 
records moved to disk (L1 tree)
• B+-tree constructed using 
bottom-up build by merging 
existing L1 tree with records 
from L0 tree
▪ When L1 tree exceeds some 
threshold, merge into L2 tree
• And so on for more levels
• Size threshold for Li+1 tree 
is k times size threshold for 
Li tree
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Log Structured Merge (LSM) Tree
Consider only inserts/queries for
now
Records inserted first into in-
memory tree (Lo tree)
When in-memory tree is full,
records moved to disk (Ll tree)
B+-tree constructed using
bottom-up build by merging
existing Ll tree with records
from 1-0 tree
When Ll tree exceeds some
threshold, merge into 1-2 tree
And so on for more levels
Size threshold for Li+l tree
is k times size threshold for
Li tree
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Memory
Disk
102
````

### 图表辅助说明

LSM 层级图：L0 位于 Memory，其下 L1、L2、L3 位于 Disk，三角形逐层变大。内存层满后与磁盘层合并，超过层阈值后继续向下一层合并；图旁说明层容量阈值按 k 倍增长。

## PDF 第 36 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=36)

### 原始文字层

````text
LSM Trees (Cont.)
▪ Deletion handled by adding special “delete” entries
• Lookups will find both original entry and the delete entry, and must 
return only those entries that do not have matching delete entry
• When trees are merged, if we find a delete entry matching an original 
entry, both are dropped.
▪ Update handled using insert+delete
▪ LSM trees were introduced for disk-based indices
• But useful to minimize erases with flash-based indices
• The stepped-merge variant of LSM trees is used in many BigData
storage systems
▪ Google BigTable, Apache Cassandra, MongoDB
▪ And more recently in SQLite4, LevelDB, and MyRocks storage 
engine of MySQL
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
LSM Trees (Cont.)
Deletion handled by adding special "delete" entries
Lookups will find both original entry and the delete entry, and must
return only those entries that do not have matching delete entry
When trees are merged, if we find a delete entry matching an original
entry, both are dropped.
Update handled using insert+delete
LSM trees were introduced for disk-based indices
But useful to minimize erases with flash-based indices
The stepped-merge variant of LSM trees is used in many BigData
storage systems
Google BigTable, Apache Cassandra, MongoDB
And more recently in SQLite4, LevelDB, and MyRocks storage
engine of MySQL
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 37 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=37)

### 原始文字层

````text
LSM Tree (Cont.)
▪ Benefits of LSM approach
• Inserts are done using only sequential I/O operations
• Leaves are full, avoiding space wastage
• Reduced number of I/O operations per record inserted as compared to 
normal B+-tree (up to some size)
▪ If each leaf has m entries, m/k entries merged in using 1 IO
▪ Total I/O operations: k/m logk(I/M) where I = total number of 
entries, and M is the size of L0 tree.
▪ Drawback of LSM approach
• Queries have to search multiple trees
• Entire content of each level copied multiple times
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
LSM Tree (Cont.)
Benefits of LSM approach
Inserts are done using only sequential 1/0 operations
Leaves are full, avoiding space wastage
Reduced number of 1/0 operations per record inserted as compared to
normal B+-tree (up to some size)
• If each leaf has m entries, m/kentries merged in using 1 10
Total 1/0 operations: Wm logk(l/M) where total number of
entries, and Mis the size of Lo tree.
Drawback of LSM approach
Queries have to search multiple trees
Entire content of each level copied multiple times
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 38 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=38)

### 原始文字层

````text
▪ Rolling merge
▪ LSM/Stepped Merge often implemented on a partitioned relation
• Each partition size set to some max, split if over-sized 
• Spread partitions over multiple machines
Optimizations of LSM
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
Optimizations of LSM
•
Rolling merge
LSM/Stepped Merge often implemented on a partitioned relation
Each partition size set to some max, split if over-sized
Spread partitions over multiple machines
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 39 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=39)

### 原始文字层

````text
Stepped Merge Index
▪ Stepped-merge index: variant of 
LSM tree with k trees at each 
level on disk
• When all k indices exist at a 
level, merge them into one 
index of next level. 
• Reduces write cost 
compared to LSM tree
▪ But queries are even more 
expensive since many trees need 
to be queries
▪ Optimization for point lookups
• Compute Bloom filter for 
each tree and store in￾memory
• Query a tree only if Bloom 
filter returns a positive result
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Stepped Merge Index
Stepped-merge index: variant of
LSM tree with k trees at each
level on disk
When all k indices exist at a
level, merge thern into one
Llo
index of next level.
Reduces write cost
Lil
compared to LSM tree
But queries are even more
expensive since many trees need
to be queries
Optimization for point lookups
Compute Bloom filter for
each tree and store in-
memory
Query a tree only if Bloom
filter returns a positive result
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Memory
Disk
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 40 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=40)

### 原始文字层

````text
LSM Trees (Cont.)
▪ Deletion handled by adding special “delete” entries
• Lookups will find both original entry and the delete entry, and must 
return only those entries that do not have matching delete entry
• When trees are merged, if we find a delete entry matching an original 
entry, both are dropped.
▪ Update handled using insert + delete
▪ LSM trees were introduced for disk-based indices
• But useful to minimize erases with flash-based indices
• The stepped-merge variant of LSM trees is used in many BigData
storage systems
▪ Google BigTable, Apache Cassandra, MongoDB
▪ And more recently in SQLite4, LevelDB, and MyRocks storage 
engine of MySQL
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
LSM Trees (Cont.)
Deletion handled by adding special "delete" entries
Lookups will find both original entry and the delete entry, and must
return only those entries that do not have matching delete entry
When trees are merged, if we find a delete entry matching an original
entry, both are dropped.
Update handled using insert + delete
LSM trees were introduced for disk-based indices
But useful to minimize erases with flash-based indices
The stepped-merge variant of LSM trees is used in many BigData
storage systems
Google BigTable, Apache Cassandra, MongoDB
And more recently in SQLite4, LevelDB, and MyRocks storage
engine of MySQL
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 41 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=41)

### 原始文字层

````text
Buffer Tree
▪ Alternative to LSM tree
▪ Key idea: each internal node of B+-tree has a buffer to store inserts
• Inserts are moved to lower levels when buffer is full
• With a large buffer, many records are moved to lower level each time
• Per record I/O decreases correspondingly 
▪ Benefits
• Less overhead on queries
• Can be used with any tree index structure
• Used in PostgreSQL Generalized Search Tree (GiST) indices
▪ Drawback: more random I/O than LSM tree
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
Buffer Tree
Alternative to LSM tree
Key idea: each internal node of B+-tree has a buffer to store inserts
Inserts are moved to lower levels when buffer is full
With a large buffer, many records are moved to lower level each time
Per record 1/0 decreases correspondingly
Benefits
Less overhead on queries
Can be used with any tree index structure
Used in PostgreSQL Generalized Search Tree (GiST) indices
Drawback: more random 1/0 than LSM tree
Internal node
Pl
Buffer
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 42 页

[查看此页](../../../notes/original/751%2525/10_Index_Hashing.pdf#page=42)

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

