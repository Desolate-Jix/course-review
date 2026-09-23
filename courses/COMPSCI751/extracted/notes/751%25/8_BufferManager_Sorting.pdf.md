# 8_BufferManager_Sorting.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI751/notes/original/751%25/8_BufferManager_Sorting.pdf`
- [打开原文件](../../../notes/original/751%2525/8_BufferManager_Sorting.pdf)
- 原文件 SHA-256：`f52d11fdc7bdce72976617fad05fc034f82fc7b4ea06500017fdf764ffbefb24`
- 文件索引：F149；PDF 总页数：20
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../notes/original/751%2525/8_BufferManager_Sorting.pdf#page=1)

### 原始文字层

````text
Miao Qiao
The University of Auckland
Buffer Manager and Sorting
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Buffer Manager and Sorting
Miao Qiao
The University Of AuckIand
00 TH E UNIVERSITYOF
AUCKLAND
№ Wana.nga 0 Timaki 鬥 《 k r 》 u
N E W Z E A L A N D
````

### 图片文字 OCR（en-US，待对照原页）

````text
Buffer Manager and Sorting
Miao Qiao
The University of Auckland
THE UNIVERSITYOF
AUCKLAND
Te Whare Wananga o Tamaki Makaurau
NEW ZEALAND
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../notes/original/751%2525/8_BufferManager_Sorting.pdf#page=2)

### 原始文字层

````text
Recap: Storage Hierarchy
Volatile 
Random Access
Byte Addressable
Non-volatile 
Sequential Access 
Block-Addressable
Faster, 
Smaller, 
Expensive.
Slower, 
Larger, 
Cheaper.
▪ Data is transfered between the main memory and the disk in blocks.
易变的
光盘
磁带
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
Recap ： Storage Hierarchy
Volatile
Random Access
Byte AddressabIe
Non-volatile
Sequential Access
Block-Addressable
cache
maln memory
flash memory
magnetic d isk
optica 1 d isk
magneåc tapes
Faste r,
Smaller,
Expensive.
Slower,
Larger,
Cheaper.
Data is transfered between the main memory and the disk i n blocks.
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Recap: Storage Hierarchy
Volatile
Random Access
Byte Addressable
Non-volatile
Sequential Access
Block-Addressable
cache
main memory
flash memory
magnetic disk
optical disk
magnetic tapes
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Faster,
Smaller,
Expensive.
Slower,
Larger,
Cheaper.
Data is transfered between the main memory and the disk in blocks.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../notes/original/751%2525/8_BufferManager_Sorting.pdf#page=3)

### 原始文字层

````text
Storge
• Buffer Pool: available main memory used for storing copies of disk blocks.
• Buffer Manager: a DBMS subsystem that manages the buffer pool, aiming at 
minimizing I/O – the number of blocks transfered between the memory and the 
disk.
冲 nor
replace policy
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
． 才 丿 丿
0
Storge
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Buffer P00 壮 available main memory used for storing copies Of disk blocks.
Buffer Manager. a DBMS subsystem that manages the buffer POOI, aiming at
minimizinq I(O _ the number Of blocks transfered between the memory and the
B 自 0
自 0000
TH E UNIVERSIT 丫 OF
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
disk.
Memory n
Get page # 2
P0inter t0 page # 2
Execution
Engine
Pages
Disk
0
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Storge
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Buffer Pool: available main memory used for storing copies of disk blocks.
Buffer Manager: a DBMS subsystem that manages the buffer pool, aiming at
minimizinq '(O — the number of blocks transfered between the memory and the
disk.
O
Memory n
Disk
Directory
Header
2
Get page
Pointer to page #2
Execution
Engine
Pages
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../notes/original/751%2525/8_BufferManager_Sorting.pdf#page=4)

### 原始文字层

````text
Buffer Manager
• The buffer pool is an array of frames, the 
size of a frame is the size of a page.
• When the DBMS requests a page, a copy is 
placed in a frame.
• The page table maps the IDs of the pages 
that are currently in the buffer pool to the 
corresponding frames, and maintains the 
meta-data for each page
• Dirty flag: a binary state. The page is dirty if 
the page is updated since loaded from the 
disk.
• Pin: an integer, representing the number of 
threads that is using the page.
• The page is unpinned if pin = 0. Page Table VS Page Directory 
Page directory: non-volatile mapping 
from Page IDs to Page locations.
三
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Buffer Manager
The buffer POOI is a n array Of
frames
， the
size Of a fra me iS the size Of a page.
When the DBMS requests a page, a COPY is
placed i n a frame.
The page table maps the IDs of the pages
that are currently in the buffer POOI tO the
corresponding frames, and maintains the
meta-data fO r each page
Dirty flag• a binary state ． The page is
dirty
the page is updated since loaded fro m the
disk.
Pin. a n integer, representing the number Of
threads that is usin the pa e ．
The page is u pnned i pin = 0 ．
． 才 丿 丿
0
Page
TabIe
pagel
page3
TH E UNIVERSIT 丫 OF
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
B 凵 什 e 「
PooI
pagel
page3
frame3
frame4
pagel
page2
page3
page4
On-Disk F i 丨 e
Page TabIe VS Page Directory
Page directory: non-volatile mapping
from Page IDs tO Page locations.
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Buffer Manager
The buffer pool is an array of frames, the
size of a frame is the size of a page.
When the DBMS requests a page, a copy is
placed in a frame.
The
page table maps the IDs of the pages
that are currently in the buffer pool to the
corresponding frames, and maintains the
meta-data for each page
Dirty flag
a binary state. The page is dirty if
the page is updated since loaded from the
disk.
an integer, representing the number of
Pin•
threads that is usin the pa e.
The page is u pinned i pin = 0.
page
Table
pagel
page3
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Buffer
Pool
pagel
page3
frame3
f rame4
pagel
page2
page3
page4
On-Disk File
Page Table VS Page Directory
Page directory: non-volatile mapping
from Page IDs to Page locations.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../notes/original/751%2525/8_BufferManager_Sorting.pdf#page=5)

### 原始文字层

````text
Buffer Manager - Read
Read request: a page ID X .
Buffer manager, upon receiving a read request
□ Check the page table, if the page is not in the buffer pool,
□ if the buffer pool is full, perform buffer replacement to get 
an empty frame
load X to the buffer and update the page table.
□ Return the the content of the page from the 
corresponding frame.
Buffer replacement: Choose, among all the unpinned 
pages, one page Y based on a replacement policy
□ If Page Y is dirty, write back Y to the disk, then kick the 
page out of the buffer pool. Write back: either overwrite 
the original block, or write to a 
new location and then mark 
the original block as invalid.
replace secret new
o
````

### 图片文字 OCR（en-US，待对照原页）

````text
Buffer Manager -
Read request: a page ID X.
Read
Buffer manager, upon receiving a read request
Check the page table, if the page is not in the buffer pool,
o if the buffer pool is full, perform buffer replacement to get
C repboe @ crat new.
an empty frame
load Xto the buffer and update he page table.
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
page
Table
pagel
page3
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Buffer
Pool
pagel
page3
frame3
frame4
Return the the content of the page from the
corresponding frame.
Buffer replacement: Choose, among all the unpinned
pages, one page Y based on a replacement policy
I Pa e Yis dirty, write back Y to the disk, then kick the
page out of the bulfér-øoof
pagel
page2
page3
page4
On-Disk File
Write back: either ovemrite
the original block, or write to a
new location and then mark
the original block as invalid.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../notes/original/751%2525/8_BufferManager_Sorting.pdf#page=6)

### 原始文字层

````text
Buffer Manager - Replacement Policy
Buffer replacement policy. When the DBMS needs to free up a frame to make 
room for a new page, it must decide which page to evict from the buffer pool.
□ Goal: Increase the “hit rate” — the proportion of read requests whose page is in 
the buffer pool without triggering an I/O.
Policy 1: Least Recently Used (LRU).
□ Maintain a single timestamp of when each page was last accessed.
□ Select the one with the oldest timestamp to be evicted.
Heuristic: The page that is used more recently is more likely to be used later.
7
一
瘫
herne
tis
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
B 冚 fe r Manager - Rep lacement P01icy
． 才 丿 丿
0
TH E UNIVERSIT 丫 OF
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Buffer replacement policy. When the DBMS needs tO free up a frame tO make
room fO r a new page ， it must decide which page tO evict
from the buffer po 酰
囗 Goal: lncrease the "hit rate
the proportion Of read requests whose page is in
the buffer POOI without triggering an 《 ℃ ．
PoIicy 1 ： yeast RecentIy Used (LRU).
Maintain a Slngle timestamp Of when each page was last accessed.
囗
囗 Select the one with the oldest timestamp tO be evicted.
Heuristic: The page that is used more recently is more likely tO be used later.
7
````

### 图片文字 OCR（en-US，待对照原页）

````text
Buffer Manager - Replacement Policy
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Buffer replacement policy. When the DBMS needs to free up a frame to make
room for a new page, it must decide which page to
from the buffer pool.
evict
0 Goal: Increase the "hit rate" — the proportion of read requests whose page is in
O Idest
the buffer pool without triggering an 1/0.
Time
Policy 1 : yeast Recently Used (LRU).
Maintain a Single timestamp of when each page was last accessed.
Select the one with the oldest timestamp to be evicted.
Heuristic: The page that is used more recently is more likely to be used later.
7
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../notes/original/751%2525/8_BufferManager_Sorting.pdf#page=7)

### 原始文字层

````text
Buffer Manager - Replacement Policy
Buffer replacement policy. When the DBMS needs to free up a frame to make 
room for a new page, it must decide which page to evict from the buffer pool.
□ Goal: Increase the “hit rate” — the proportion of read requests whose page is in 
the buffer pool without triggering an I/O.
Policy 2: Clock.
□ Maintain a binary bit for each page, when access the page, set the bit to 1.
□ Reset to bit to 0 using a “sweeping clock hand”, in particular,
□ When the clock hand reaches a page and the bit of the page is 0 – the page 
has not been accessed for the past whole circle, evict the page; otherwise, set 
the bit to 0.
8 Heuristic: Approximate LRU without keeping a timestamp per page.
expensive 6bits
䬔
o
T­o
use only 1 韭
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
0
B uffe r Manager “ Rep lacement POIicy
TH E UNIVERSIT 丫 OF
AUCKLAND
reWh•r• 、 能 隧 《 0 Tim•ki •k 》 “ “
N E W 7 E A L A N D
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Buffer replacement policy. When the DBMS needs tO free up a frame tO make
room fO r a new page, it must decide which page tO evict
from the buffer pool.
the proportion Of read requests whose pag
oa lncrease t e 'hit rate"
the buffer pool without triggering an 《 ℃ ．
PoIicy 2 ： lock
Maintain a binary bit for each page, when acce the page ， set th bi tO 1 ．
囗
Reset tO bit tO 0 using a "sweeping clock hand", in particular,
囗
When the clock hand reaches a page and the bit O e page is 0 一 the page
囗
has not been accessed fO r the past whole circle, evict he page; otherwise, set
the bit to 0 ．
Heuristic: Approximate LRU without keeping a timestamp per page.
8
2
````

### 图片文字 OCR（en-US，待对照原页）

````text
Buffer Manager - Replacement Policy
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Buffer replacement policy. When the DBMS needs to free up a frame to make
room for a new page, it must decide which page to
evict
from the buffer pool.
oa Increase t e "hit rate" — the proportion of read requests whose pag
the buffer pool without triggering an 1/0.
Policy 2: lock
1
Maintain a binary bit for each page, when acce the page, set th bi to 1.
Reset to bit to 0 using a "sweeping clock hand", in particular,
When the clock hand reaches a page and the bito e page is 0 — the page
has not been accessed for the past whole circle, evict he page; otherwise, set
the bit to 0.
Heuristic: Approximate LRU without keeping a timestamp per page.
8
l/tSe on l}
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../notes/original/751%2525/8_BufferManager_Sorting.pdf#page=8)

### 原始文字层

````text
Buffer Manager - Replacement Policy
▪ Sequential flooding of Policies 1-2.
 A query performs a sequential scan that reads every page.
 This pollutes the buffer pool with pages that are read once and then never again.
▪ Example:
▪ Q1: SELECT AVG(VAL) FROM A
▪ Q2: SELECT ∗ FROM A WHERE VAL = 100
▪ Both queries are executed by sequentially scanning the blocks of relation A.
▪ Policy 3: Mose Recently Used (MRU).
 Maintain a single timestamp of when each page was last accessed.
 Select the one with the youngest timestamp to be evicted.
▪ Heuristic: The page that is used more recently is less likely to be used later.
顺序扫描
we
drawback scan 𨨶留在poor
再Scan 设个用例上
褓
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
AUCKLAND
Buffer Manager “ Rep lacement PoIicy
《 7 E A L A N D
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
SScan 7
Sequential ℃ ding Of PoIicies 1 ． 2 ．
A query performs a sequential scan that read s every page.
O
This pollutes the buffer POOI with pages that a re read once and then never again.
O
ExampIe
QI ： SELECT AVG ()A L) FROM A
Q2: SELECT * FROM A WHERE VA L = 100
BOth queries a re executed by sequentially scanning the blocks Of relation
POIicy 3 ： Mose Recently Used (MRU).
Maintain a single timestamp Of when each page wa S last accessed ．
O
SeIect the one with the youngest timestamp tO be evicted ．
O
Heuristic: The page that is used more recently is less likely tO be used later.
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Buffer Manager - Replacement Policy
nv Wln•ng• o Timüi
ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
San —D pr
drawback
sscan -a
Sequential lo ding of Policies 1-2.
A query performs a sequential scan that reads every page.
O
This pollutes the buffer pool with pages that are read once and then never again.
O
Example:
QI : SELECT AVG(VAL) FROM A
Q2: SELECT * FROM A WHERE VAL = 100
Both queries are executed by sequentially scanning the blocks of relation A.
Policy 3: Mose Recently Used (MRU).
Maintain a single timestamp of when each page was last accessed.
O
Select the one with the youngest timestamp to be evicted.
O
Heuristic: The page that is used more recently is less likely to be used later.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../notes/original/751%2525/8_BufferManager_Sorting.pdf#page=9)

### 原始文字层

````text
Buffer Manager
Other heuristics in improving the buffer management.
□ Run-time statistics and query execution algorithms can be analyzed to predict which 
page is less likely to be used in future.
□ Replacing a dirty page is slower than replacing a clean page.
□ Background writing: the DBMS can periodically walk through the page table, write 
dirty pages back to the disk and reset the dirty flag.
□ Engaging multiple buffer pools with different replacement policies
- Per-database buffer pool,
- Per-page buffer pool,
- Sorting and join buffers,
- Log buffers,
- Query caches
worn
定期置制脏阿比写回
磁盘
排序 -
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
B u ffe r Manager
Other h e u risti cs i n improving the b uffer management.
． 才 丿 丿
0
TH E UNIVERSIT 丫 OF
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Run-time statistics and query execution a g
s ca n be analyzed tO p red i ct which
囗
page is 《 s likely tO be used in futu re
RepIacing a d i rty page is slower than replacing a dean page.
囗
Background writing: the DBMS ca n penodically walk through t e pa e table, w ri te
囗
d i rty pages back tO the disk and reset the d i rty flag.
Engaging multiple buffer POOIS with different replaæment policies
囗
- Per-database buffer pool,
- Per-page buffer pool,
and jOin buffers,
- Log buffers,
- Query cach es
````

### 图片文字 OCR（en-US，待对照原页）

````text
Buffer Manager
Other heuristics in improving the buffer management.
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Run-time statistics and query execution a g
s can be analyzed to predict which
page is less likely to be in future
Replacing a dirty page is slower than replacing a dean page.
Background writing: the DBMS can periodically walk through t epa e table, write
dirty pages back to the disk and reset the dirty flag.
Engaging multiple buffer pools with different replaæment policies
241)
- Per-database buffer pool,
- Per-page buffer pool,
Sorting
and join buffers,
- Log buffers,
- Query caches
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../notes/original/751%2525/8_BufferManager_Sorting.pdf#page=10)

### 原始文字层

````text
Sorting
▪ We may build an index on the relation, and then use the index to read 
the relation in sorted order. May lead to one disk block access for each 
tuple.
▪ For relations that fit in memory, techniques like quicksort can be used. 
• For relations that don’t fit in memory, external sort-merge is a 
good choice.
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
Sorting
We may build an index on the relation, and then use the index to read
the relation in sorted order. May lead to one disk block access for each
tuple.
For relations that fit in memory, techniques like quicksort can be used.
For relations that don' t fit in memory, external sort-merge is a
good choice.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../notes/original/751%2525/8_BufferManager_Sorting.pdf#page=11)

### 原始文字层

````text
Example: External Sorting Using Sort-Merge
g
a 
d 31
c 33
b 14
e 16
r 16
d 21
m 3
p 2
d 7
a 14
a 14
a 19
b 14
c 33
d 7
d 21
d 31
e 16
g 24
m 3
p 2
r 16
a 19
b 14
c 33
d 31
e 16
g 24
a 14
d 7
d 21
m 3
p 2
r 16
a 19
d 31
g 24
b 14
c 33
e 16
d 21
m 3
r 16
a 14
d 7
p 2 initial
relation
create
runs
merge
pass–1
merge
pass–2
runs runs
sorted
output
24
19 lfiiftbuter­3 br
2 input 0 1 output
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
Example: External SortbngrUsing Sort-Merge
haer
19
d
r
d
m
24
19
31
33
14
16
16
21
3
a
d
C
e
d
m
r
19
31
14
33
1
21
3
16
14
7
C
d
e
d
m
r
14
33
3
1
14
7
21
3
16
a
d
d
e
m
r
14
19
14
33
7
21
31
16
24
3
16
0 Iltpr€
a 14
initial
relation
runs
create
runs
runs
merge
pass—I
sorted
output
merge
pass—2
````

### 图表辅助说明

外部归并排序从左到右：初始未排序关系先切为四个 runs；merge pass 1 两两合并成两个较长 runs；merge pass 2 合并成最终有序输出。蓝色批注圈出两个输入缓冲和一个输出缓冲，共 3 个 buffer。

## PDF 第 12 页

[查看此页](../../../notes/original/751%2525/8_BufferManager_Sorting.pdf#page=12)

### 原始文字层

````text
Create runs (chunks)
一 个缓存 数
熊赟
〇
〇 䵋有序块
数
读取坎 趴 一 帧 磁盘 北 操作
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
Create runs (chunks)
input file R:
Dis
M buffer
hunk 1
S ort
Disk Soned
M blocks
M buffer
chunk 2
Sort
Sorted
M bl ock s
M buffer
Sorted
< = M bl ocks
# disk I/Os = 2 B(R)
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Create runs (chunks)
input file R:
Dis
M buffer
hunk 1
Sort
Disk Sorted
M blocks
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
M buffer
M buffer
chunk 2
Sort
Sorted
M blocks
chunk(S å$fh*
Sort
Sorted
M blocks
# disk I/Os = 2 B(R)
1/0 t*5P,
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../notes/original/751%2525/8_BufferManager_Sorting.pdf#page=13)

### 原始文字层

````text
Merge: Pass 1 (1 run = 1 chunk)
 br blocks of data
 M is the # of frames in the buffer pool
 K = br / M
 M-1 way merge 
08濉
舆 区内一定是比剩下的
tnnnnybhocky
im
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
Merge ： Pass 1 （ 1 run = 1 chunk)
Disk
chunk 1
M blocks
ne
1 buffer
# disk 《 / 0 s = B(R)
chunk 2
chunk K
M blocks
< = M b 《 k s
So
Soned
read 1 block at a time
1 buffer
mov r 0 rd with
smalle son
1 ou 鬣 put buffer
br blocks 0 data
M is the # 0 frame in the buffer p00 《
K = br / M
M-I waY@9.!-q
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
Merge: Pass 1 (1 run 1 chunk)
Disk
chunk 1
M blocks
ne
1 buffer
# disk I/Os = B(R)
chunk 2
chunk K
M blocks
Sorted
Soned
read 1 block at a time
1 buffer
Jk k Oldll¯
mov record with
7æk
smalle son
1 output buffer
br blocks of data
M is the # of frame in the buffer pool
K=br/M
M-1 way merq
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../notes/original/751%2525/8_BufferManager_Sorting.pdf#page=14)

### 原始文字层

````text
Merge: Pass 2
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TH E UNIVERSIT 丫 OF
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
Merge ： Pass 2
M 一 1 chunks,•
Disk
． 才 丿 丿
0
> M—I chunks
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
M bl ks · 。 M blks
M 一 1 buffer
1 output buffer
、 M 一 1 chunks
1 output buffer
Disk
M—I M bl ks
# disk I/Os
Disk
= 2 B(R)
M—I M bl ks
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Merge:
Disk
Pass 2
M-1 chunks:'
> M-1 chunks
M blks •e M blks
read block at time
Disk
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
chunks
M blks M blks
read block at time
M-1 buffer
1 output buffer
M-1 buffer
1 output buffer
Disk
M-1 M blks
# disk I/Os =
Disk
M-1 M blks
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../notes/original/751%2525/8_BufferManager_Sorting.pdf#page=15)

### 原始文字层

````text
External Sort-Merge
1. Create sorted runs. Let i be 0 initially. 
 Repeatedly do the following till the end of the relation:
 (a) Read M blocks of relation into memory
 (b) Sort the in-memory blocks
 (c) Write sorted data to run Ri
; increment i.
Let the final value of i be N
2. Merge the runs (N-way merge). We assume (for now) that N < M. 
1. Use N blocks of memory to buffer input runs, and 1 block to buffer output. 
Read the first block of each run into its buffer page
2. repeat
1. Select the first record (in sort order) among all buffer pages
2. Write the record to the output buffer. If the output buffer is full write it to disk.
3. Delete the record from its input buffer page.
If the buffer page becomes empty then
 read the next block (if any) of the run into the buffer. 
3. until all input buffer pages are empty:
Let M denote memory size (in pages).
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
1.
External Sort-Merge
Let M denote memory size (in pages).
Create sorted runs. Let ibe 0 initially.
Repeatedly do the following till the end of the relation:
(a) Read M blocks of relation into memory
(b) Sort the in-memory blocks
(c) Write sorted data to run R; increment i.
Let the final value of ibe N
2. Merge the runs (N-way merge). We assume (for now) that N< M.
Use N blocks of memory to buffer input runs, and 1 block to buffer output.
2.
3.
Read the first block of each run into its buffer page
repeat
Select the first record (in sort order) among all buffer pages
2.
3.
Write the record to the output buffer. If the output buffer is full write it to disk.
Delete the record from its input buffer page.
If the buffer page becomes empty then
read the next block (if any) of the run into the buffer.
until all input buffer pages are empty:
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../notes/original/751%2525/8_BufferManager_Sorting.pdf#page=16)

### 原始文字层

````text
External Sort-Merge (Cont.)
▪ If N  M, several merge passes are required.
• In each pass, contiguous groups of M - 1 runs are merged. 
• A pass reduces the number of runs by a factor of M -1, and creates runs 
longer by the same factor. 
▪ E.g. If M=11, and there are 90 runs, one pass reduces the number of 
runs to 9, each 10 times the size of the initial runs
• Repeated passes are performed till all runs have been merged into one.
q logmt 县
m 咚 哭
mum br
b
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
． 才 丿 丿
0
External Sort-Merge (Cont.)
If N M, several merge passes are required.
ln each pass, contiguous gr01-lPS Of M ． 1 runs are merged.
TH E UNIVERSIT 丫 OF
AUCKLAND
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
A pass reduces the number Of runs by a factO r Of M-I ， and creates runs
longer by the same factO r ．
E.g. If M=11 ， and there are 90 ru ns ， one pass reduces the number Of
runs tO 9 ， each 1 0 times the size Of the initial runs
Repeated passes are performed till runs have been merged intO one.
9
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
External Sort-Merge (Cont.)
If N2 M, several merge passes are required.
In each pass, contiguous groups of M- 1 runs are merged.
A pass reduces the number of runs by a factor of M -1 , and creates runs
longer by the same factor.
E.g. If M=11, and there are 90 runs, one pass reduces the number of
runs to 9, each 10 times the size of the initial runs
Repeated passes are performed till all runs have been merged into one.
q
n 1/11-1)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../notes/original/751%2525/8_BufferManager_Sorting.pdf#page=17)

### 原始文字层

````text
External Merge Sort (Cont.)
▪ Cost analysis for a relation with br blocks of tuples:
• Total number of merge passes required: log M–1(br
/M).
• Block transfers for initial run creation as well as in each pass is 2br
▪ for final pass, we don’t count write cost 
• we ignore final write cost for all operations since the output of 
an operation may be sent to the parent operation without 
being written to disk
▪ Thus, the total number of I/Os for external sorting:
br ( 2 log M–1 (br / M) + 1) 
int 1
年归所需
轮数a Yin
O
第一次分会区块
nrnnn CO ru
不算
2
brignim 上
最后一
次 1 br
第一次排序 this 以 1
次并 吼 不算最后圾
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
乪 一 到
Exte rna 》 Merge Sort (Cont.)
COSt analysis for a relation with br blocks Of tuples.
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Ot 《 n mber Of e g passes required. 「 ℃ g 1 （ b / M, 月
BI ck transfers fO r initial run creation as well as in each pass is 2 br
or inal pass ， we don t ount write st
《 O pe ra 丨 ns since the output Of
we ignore lnal write
an operation may be se nt tO the parent operation without
being written tO disk
Thus, the tOtal number Of l/Os fO r external sorting.
br(2Flog - (br/M)1 + 1 ）
次 着 禰 丿
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
External Merge Sort (Cont.)
Cost analysis for a relation with br blocks of tuples:
ot In mber of e g passes required: log
Bl ck transfers for initial run creation as well as in each pass is 2br
or inal pass, we don't ount write st
opera I ns since the output of
we ignore Inal write
an operation may be sent to the parent operation without
being written to disk
Thus, the total number of I/Os for external sorting:
(br/M)1+ 1)
cb/n)-J
'k I)3L
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 18 页

[查看此页](../../../notes/original/751%2525/8_BufferManager_Sorting.pdf#page=18)

### 原始文字层

````text
Exercise: EM Sort
▪ Suppose you need to sort a relation of 40 gigabytes, with 8-kilobyte blocks, 
using a memory size of 40 megabytes. Suppose the cost of a seek is 5 
milliseconds, while the disk transfer rate is 40 megabytes per second.
1. What is the time of transferring one block of data (without seeking)?
2. Suppose a flash storage device is used instead of a disk, and it has a 
latency of 20 microsecond and a transfer rate of 400 megabytes per 
second. What is the time of transferring one block of data (without 
seeking)?
3. How many merge passes are required?
4. Find the cost of sorting the relation, in the number of I/Os.
5. [After class exercise] 
What is the largest file size that can be sorted in at most 2 passes?
MB KB GB
-
hntotfnnggg 和 叱
一
一 块大小 8143
8000
器 0
br是
总块数O 㼏 微 乐 㔋 鷗 㣈
Brlzhgcmnl制十门 313r 3 5州
县 有4
q 2
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
《 kB ／ 裼
Exercise ： EM Sort
TH E UNIVERSIT 丫 OF
． 才 丿 丿
AUCKLAND
0
reWh•r• 、 能 隧 《 0 T1müi 》 “ “
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
一 休 小 8
Suppose ou n ed t SO r lation Of 40 gga ytes, with ßzki.l@yte blocks,
ab es ． Suppose the CO st Of a seek is 5
I-ISIng a emory SIze 0
m• seco n s ， while the dis tr nsfer rat is 40 megab es pe r second ．
What is the time Of transferring one block
wlthout seeking)?
2 ．
3 ．
4
5
Suppose a flash stO ra g e device is used instead Of a disk, and it h as a
latency Of 20 microsecond and a transfer rate Of 400 megabytes pe r
second. Wh at is the time ransferring one block
seeking)?
HOW many merg as es are req
0
Find the CO st Of sorting the relation, in the number Of /Os.
[Afte r class exercise]
What is the largest file size that can be SO rted in at most 2 passes?
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Exercise: EM Sort
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
-Rich
Suppose ou n ed t sort r lation of 40 g ga ytes, withßzkil@yte blocks,
ab es. Suppose the cost of a seek is 5
using a emory size o
m' •secon s, while the dis tr nsfer rat is 40 megab es per second.
What is the time of transferring one block
without seeking)?
2.
3.
4
5
Suppose a flash storage device is used instead of a disk, and it has a
latency of 20 microsecond and a transfer rate of 400 megabytes per
w t -.Bklå
second. What is the timent ransferring one block
seeking)?
How many merg as es are req
Find the cost of sorting the relation, in the number of /Os.
[After class exercise]
What is the largest file size that can be sorted in at most 2 passes?
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 19 页

[查看此页](../../../notes/original/751%2525/8_BufferManager_Sorting.pdf#page=19)

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

## PDF 第 20 页

[查看此页](../../../notes/original/751%2525/8_BufferManager_Sorting.pdf#page=20)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
在 0 助
8
000
兯 7
````

### 图片文字 OCR（en-US，待对照原页）

````text
2.0 D0ic.@
S KIO
ooo
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

