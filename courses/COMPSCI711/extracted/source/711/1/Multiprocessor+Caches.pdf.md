# Multiprocessor+Caches.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI711/source/711/1/Multiprocessor+Caches.pdf`
- [打开原文件](../../../../source/711/1/Multiprocessor%2BCaches.pdf)
- 原文件 SHA-256：`0d7bc1cedf22a66335d1e7a8cba4e5ece4552becf3e4d399ffa7d782d0d70402`
- 文件索引：F054；PDF 总页数：74
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=1)

### 原始文字层

````text
Multiprocessor Caches
mano@auckland.ac.nz
````

### 图片文字 OCR（en-US，待对照原页）

````text
Multiprocessor Caches
mano@auckland.ac.nz
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=2)

### 原始文字层

````text
Caches
• Caches bridge the speed gap between the processor and the main 
memory. 
• Small fast memory holding data that is likely to be accessed in the 
near future.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Caches
•Caches bridge the speed gap between the processor  and the main
 memory.
•Small fast memory holding data that is likely to be accessed in the
 near future.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Caches
' Caches bridge the speed gap between the processor and the main
memory.
• Small fast memory holding data that is likely to be accessed in the
near future.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=3)

### 原始文字层

````text
Hardware Architecture
• A single-processor machine has: a CPU, memory, cache (primary & 
secondary), disk, and other peripheral devices.
Memory
L2Cache
L1Cache
CPU
Recapitulate:
Locality
Cache lines
Hit/miss/miss penalty
Write through/write back
Direct mapped
Set associative
Replacement policies
局限性 level2
level1
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Hardware Architecture
• A single-processor  machine has: a CPU, memory, cache (primary &
  secondary), disk,  and other peripheral  devices.
            Memory                      Recapitulate:
                                        Locality  局限性
        level2L2Cache                   Cache lines
                                        Hit/miss/miss penalty
       level1L1Cache                    Write through/write back
                                        Direct mapped
                 CPU                    Set associative
                                        Replacement policies
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Hardware Architecture
． A single-processor machine has: a CPU, memory, cache (primary &
secondary), disk, and other peripheral devices.
Memory
L2Cache
LICache
CPU
RecapituIate:
Loca | ity
Cache lines
Hit/miss/miss penalty
Write through/write back
Direct mapped
Set associative
Replacement policies
````

### 图片文字 OCR（en-US，待对照原页）

````text
Hardware Architecture
' A single-processor machine has: a CPU, memory, cache (primary &
secondary), disk, and other peripheral devices.
Memory
L2Cache
LICache
CPU
Recapitulate:
Locality
Cache lines
Hit/miss/miss penalty
Write through/write back
Direct mapped
Set associative
Replacement policies
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=4)

### 原始文字层

````text
Locality
• Caches rely on two properties of the access patterns of most 
programs: 
• temporal locality - if a memory location is accessed once, it is likely to be 
accessed again soon
• spatial locality - if one memory location is accessed then nearby memory 
locations are also likely to be accessed. 
时间局限性
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Locality
• Caches rely on two properties of the access patterns of most
  programs: 时间局限性
    • temporal locality - if a memory location is accessed once, it is likely to be
      accessed again soon
    • spatial locality - if one memory location is accessed then nearby memory
      locations are also likely to be accessed.
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Locality
． Caches rely O n tWO properties Of the access patterns Of most
programs:
． temporal loca ity - if a memory location is accessed once, it is likely tO be
accessed again soon
． spatial locality 一 if O n e memory location is accessed then nearby memory
locations a re also likely tO be accessed.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Locality
' Caches rely on two properties of the access patterns of most
programs:
• temporal Ioca ity - if a memory location is accessed once, it is likely to be
accessed again soon
• spatial locality - if one memory location is accessed then nearby memory
locations are also likely to be accessed.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=5)

### 原始文字层

````text
Cache Lines
• In order to exploit spatial locality, caches operate on several words at 
a time, called a cache line or a cache block. 
• Main memory reads and writes are whole cache lines. 
• This takes advantage of the principle of spatial locality of reference: if one 
location is read then nearby locations (particularly following locations) are 
likely to be read soon afterwards.
malt words
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Cache Lines
• In order to exploit spatial locality, caches operate on several words at
  a time, called a cache line or a cache block.
    • Main memory reads and writes are whole cache lines.
    • This takes advantage of the principle of spatial locality of reference: if one
      location is read then nearby locations (particularly following locations) are
      likely to be read soon afterwards.
                                                             malt         wo rd s
````

### 图片文字 OCR（en-US，待对照原页）

````text
Cache Lines
' In order to exploit spatial locality, caches operate on several words at
a time, called a cache line or a cache block.
• Main memory reads and writes are whole cache lines.
• This takes advantage of the principle of spatial locality of reference: if one
location is read then nearby locations (particularly following locations) are
likely to be read soon afterwards.
word"
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=6)

### 原始文字层

````text
Hits, Misses and Miss Penalty
• If the data being accessed is in the cache, then we have a cache hit.
• If the data is not cached (a cache miss) then it is fetched from main 
memory and also saved in the cache. 
• The time it takes to service a memory request under a cache miss is 
called a miss penalty.
处罚
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Hits, Misses and Miss Penalty处罚
•If the data being accessed is in the cache, then we have a cache hit.
•If the data is not cached (a cache miss) then it is fetched from main
 memory and also saved in the cache.
•The time it takes to service a memory request  under  a cache miss is
 called a miss penalty.
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Hits, Misses and Miss Pen lty
． If the data being accessed is in the cache, then we have a cach e hit.
． If the data is not cached (a cach e miss) then it is fetched from main
memory and alSO saved in the cache.
． The time it takes tO service a memory request under a cache miSS iS
called a m 5 pe 冂 0 / ·
````

### 图片文字 OCR（en-US，待对照原页）

````text
Hits, Misses and Miss Pen Ity
' If the data being accessed is in the cache, then we have a cache hit.
• If the data is not cached (a cache miss) then it is fetched from main
memory and also saved in the cache.
' The time it takes to service a memory request under a cache miss is
called a miss penalty.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=7)

### 原始文字层

````text
Write through and write back
• When writing, a write-through policy updates both cache and main 
memory
• A write-back policy only updates the cache, and written to the main 
memory only when required. 
o
O
mon
only value require
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Write through and write back
•When writing , a write-through policy updates both cache and main o
 memoryO
•A write-back policy only updates the cache, and written to the main mon
 memory only when required.
                           only        va l u e     re   q   u   i   re
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write through and write back
' When writing, a write-through policy updates both ach and main
memo
• A write-back policy only updates t e cache, and written to the main
memory only when required.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=8)

### 原始文字层

````text
Direct-Mapped Caches
000
001
010
011
100
101
110
111
4, 5, 6, 7
1c, 1d, 1e, 1f
0, 1, 2, 3
24, 25, 26, 27
20, 21, 22, 23
3c, 3d, 3e, 3f
01 1101 11 1101
Tag Line index Word offset
Word address
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Direct-Mapped Caches
   0, 1, 2, 3                  000                                     20, 21, 22, 23
   4, 5, 6, 7                  001                                     24, 25, 26, 27
                               010
                               011
                               100
        01 1101                101                                    11 1101
                               110
 1c, 1d, 1e, 1f                111                                    3c, 3d, 3e, 3f
                                                                           W ord address
                                                                Tag                     Line index    W ord offset
````

### 图片文字 OCR（en-US，待对照原页）

````text
Direct-Mapped Caches
01 1101
lc, ld, le, If
ooo
001
010
011
100
101
110
111
Tag
20, 21, 22, 23
24, 25, 26, 27
11 1101
3c, 3d, 3e, 3f
Word address
Line index
Word offset
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=9)

### 原始文字层

````text
Categorizing cache misses
• Compulsory miss: First ever reference to a cache line.
• Capacity miss: Miss due to the cache not being big enough to hold 
the current data set. If the number of active lines is more than the 
cache can contain, capacity misses take place.
can be reduced
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Categorizing cache misses
•Compulsory miss: First ever reference to a cache line.              can   be     re  d  u  c  e  d
•Capacity  miss: Miss  due to the cache not being big enough to hold
 the current data set.  If the number  of active lines is more than the
 cache can contain, capacity misses take place.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Categorizing cache misses
be reduced ,
' Compulsory miss: First ever reference to a cache line.
• Capacity miss: Miss due to the cache not being big enough to hold
the current data set. If the number of active lines is more than the
cache can contain, capacity misses take place.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=10)

### 原始文字层

````text
Categorizing cache misses
• Conflict miss: The required line was previously there in the cache, but 
was replaced by another line which happened to map to the same 
cache location.
• Conflict misses take place because of limited or zero associativity when lines 
must be discarded in order to accommodate new lines which are mapped to 
the same line in the cache. 
• A miss occurs when the replaced line needs to be accessed again.
ˇ
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Categorizing cache misses
ˇ  • Conflict  miss: The required line was previously  there in the cache, but
     was replaced by another line which happened  to map to the same
     cache location.
       • Conflict misses take place because of limited or zero associativity when lines
         must be discarded in order to accommodate new lines which are mapped to
         the same line in the cache.
       • A miss occurs when the replaced line needs to be accessed again.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Categorizing cache misses
' Conflict miss: The required line was previously there in the cache, but
was replaced by another line which happened to map to the same
cache location.
• Conflict misses take place because of limited or zero associativity when lines
must be discarded in order to accommodate new lines which are mapped to
the same line in the cache.
• A miss occurs when the replaced line needs to be accessed again.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=11)

### 原始文字层

````text
Shared-memory multiprocessors
• Processors and memory modules are connected by an 
interconnection network – typically a shared bus.
Memory Memory
Cache Cache
CPU CPU
Interconnection Network
……
……
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Shared-memory multiprocessors
•Processors  and memory modules are connected by an
 interconnection  network – typically a shared bus.
                Memory             ……               Memory
                         Interconnection Network
                 Cache             ……               Cache
                  CPU                                CPU
````

### 图片文字 OCR（en-US，待对照原页）

````text
Shared-memory multiprocessors
' Processors and memory modules are connected by an
interconnection network — typically a shared bus.
Memory
Cache
CPU
Interconnection Network
Memory
Cache
CPU
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=12)

### 原始文字层

````text
Distributed-memory Systems
• A distributed system 
• Has a network of computers; independent failures; no global clock
• Communicates and coordinates only by passing messages
• Can mean both hardware and software
Memory Memory
Cache Cache
CPU CPU
Interconnection Network
……
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Distributed-memory Systems
•A distributed  system
   • Has a network of computers; independent failures; no global clock
   • Communicates and coordinates only by passing messages
   • Can mean both hardware and software
                               Interconnection Network
                    Memory                                 Memory
                     Cache                ……                 Cache
                      CPU                                     CPU
````

### 图片文字 OCR（en-US，待对照原页）

````text
Distributed-memory Systems
' A distributed system
• Has a network of computers; independent failures; no global clock
• Communicates and coordinates only by passing messages
• Can mean both hardware and software
Interconnection Network
Memory
Cache
CPU
Memory
Cache
CPU
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=13)

### 原始文字层

````text
Cache coherency
• Caching of data in multiprocessors results in the existence of multiple 
copies of the same memory location in the system.
• Cache coherence allows the programmer to see the whole system as 
one single memory.
• When a processor modifies its local copy of the data, data 
inconsistency may result. 
• This is known as the cache coherence problem.
• Multiprocessors with local caches need hardware and/or software 
support to enforce data consistency.
一致性
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Cache coherency                   ⼀致性
•Caching of data in multiprocessors   results in the existence of multiple
 copies of the same memory location in the system.
•Cache coherence allows the programmer to see the whole system as
 one single memory.
•When a processor  modifies its local copy of the data, data
 inconsistency  may result.
•This is known as the cache coherence problem.
•Multiprocessors   with local caches need hardware and/or software
 support  to enforce data consistency.
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Cache coherency
． Caching Of data in multiprocessors results in the existence Of multiple
copies Of the sa m e memory location in the syste m ·
． Cache coherence allows the programmer tO see the whole syste m a S
O n e single memory.
． When a processor modifies its local COPY 0f the data, data
inconsistency may result.
． This is known a S the cache coherence problem.
． Multiprocessors with local caches need hardware and/or software
SUPport tO enforce data consistency.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Cache coherency
' Caching of data in multiprocessors results in the existence of multiple
copies of the same memory location in the system.
• Cache coherence allows the programmer to see the whole system as
one single memory.
' When a processor modifies its local copy of the data, data
inconsistency may result.
• This is known as the cache coherence problem.
' Multiprocessors with local caches need hardware and/or software
support to enforce data consistency.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=14)

### 原始文字层

````text
Solving the Cache Coherence Problem
• Don’t use caches at all. 
• Single cache (L1 cache) shared by all processors.
• Have private caches but 
• Write-through to the memory.
• Write to an item invalidates all other copies of the item.
• Write to an item updates all other copies of the item.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Solving the Cache Coherence Problem
•Don’t use caches at all.
•Single cache (L1 cache) shared by all processors.
•Have private caches but
   • Write-through to the memory.
   • Write to an item invalidates all other copies of the item.
   • Write to an item updates all other copies of the item.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Solving the Cache Coherence Problem
• Don't use caches at all.
• Single cache (Ll cache) shared by all processors.
• ave private caches but
to the memory.
• Write to an item invalidates all other copies of the item.
• Write to an item updates all other copies of the item.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=15)

### 原始文字层

````text
Cache coherency protocols
• Cache coherency protocols ensure that any changes made to a data 
item in one cache are consistently reflected across all other caches 
that store copies of the same data.
• When a processor writes to a memory location, the coherency 
scheme must guarantee the consistency of the copies.
协议
一一
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Cache coherency protocols协议
                                       ⼀⼀
•Cache coherency protocols ensure that any changes made to a data
 item in one cache are consistently  reflected across all other caches
 that store copies of the same data.
•When a processor  writes to a memory location, the coherency
 scheme must  guarantee the consistency  of the copies.
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Cache coherency protocols
． Cache coherency protocols e n S u re that any changes made tO a data
item in O n e cache a re consistently reflected across a ll other caches
that stO re copies Of the sa m e data.
． When a processor writes tO a memory location, the coherency
scheme must guarantee the consistency Of the copies.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Cache coherency protocols
' Cache coherency protocols ensure that any changes made to a data
item in one cache are consistently reflected across all other caches
that store copies of the same data.
• When a processor writes to a memory location, the coherency
scheme must guarantee the consistency of the copies.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=16)

### 原始文字层

````text
Cache coherency protocols
• Two broad classifications
• Write-update protocols
• Write-invalidate protocols
• Further classifications depending on the availability of global state 
information
• Snoopy protocols
• Directory-based protocols
二十 0比 啊
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Cache coherency protocols
•Two broad  classifications⼆⼗
   • Write-update protocols          0 ⽐     啊
   • Write-invalidate protocols
•Further classifications  depending  on the availability of global state
 information
   • Snoopy protocols
   • Directory-based protocols
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Cache coherency protocols
． Two broad clas
《 O n
． Write-update protocols
． Write-inv date protocols
． Further classi
information
． Snoopy protocols
depending 0 n the availability 0f global state
． Directory-based protocols
````

### 图片文字 OCR（en-US，待对照原页）

````text
Cache coherency protocols
• Two broad clas
Ion
• Write-update protocols
• Write-inv date protocols
Odw c.ffä
• Further classi •
information
• Snoopy protocols
depending on the availability of global state
• Directory-based protocols
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=17)

### 原始文字层

````text
Snoopy protocols
• A snoopy cache protocol relies on the hardware to monitor all writes 
to the memory. If a write is seen by a cache, it needs to either update 
or invalidate the copies that may exist elsewhere in other caches. 
• Snoopy protocols can be efficiently implemented if all the processors 
are connected to the same shared bus, so that each cache can 
monitor the other caches' activity and broadcast invalidates or 
updates. 
• In the absence of a shared bus, communication costs involved in 
broadcasting the write modifications become prohibitively expensive.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Snoopy protocols
•A snoopy cache protocol relies on the hardware to monitor all writes
 to the memory. If a write is seen by a cache, it needs to either update
 or invalidate the copies that may exist elsewhere in other caches.
•Snoopy protocols can be efficiently implemented  if all the processors
 are connected to the same shared bus,  so that each cache can
 monitor the other caches' activity and broadcast  invalidates or
 updates.
•In the absence of a shared bus,  communication  costs involved in
 broadcasting  the write modifications  become prohibitively  expensive.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Snoopy protocols
' A snoopy cache protocol relies on the hardware to monitor all writes
to the memory. If a write is seen by a cache, it needs to either update
or invalidate the copies that may exist elsewhere in other caches.
• Snoopy protocols can be efficiently implemented if all the processors
are connected to the same shared bus, so that each cache can
monitor the other caches' activity and broadcast invalidates or
updates.
• In the absence of a shared bus, communication costs involved in
broadcasting the write modifications become prohibitively expensive.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 18 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=18)

### 原始文字层

````text
Directory-based protocols
• When there is no shared bus, it is more efficient to multicast the write 
modifications to those caches that require them. 
• To do this requires storing information about which caches have 
copies of all cached blocks. 
• A directory-based protocol takes this approach.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Directory-based protocols
•When there is no shared bus,  it is more efficient to multicast  the write
 modifications  to those caches that require them.
•To do this requires storing  information about which caches have
 copies of all cached blocks.
•A directory-based  protocol takes this approach.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Directory-based protocols
' When there is no shared bus, it is more efficient to multicast the write
modifications to those caches that require them.
• To do this requires storing information about which caches have
copies of all cached blocks.
' A directory-based protocol takes this approach.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 19 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=19)

### 原始文字层

````text
Categorizing cache misses
• Coherency miss: The required line was previously there in the cache, 
but was invalidated by another processor. There are two types:
• True-sharing miss
• False-sharing miss
Someone invalidate you copy
m
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Categorizing cache misses
•Coherency  miss: The required line was previously  there in the cache,
 but was invalidated by another processor.  There are two types:
   • True-sharing miss
   • False-sharing miss
            Someone        invalidate        yo  u   copy
                                         m
````

### 图片文字 OCR（en-US，待对照原页）

````text
Categorizing cache misses
' Coherency miss: The required line was previously there in the cache,
but was invalidated by another processor. There are two types:
• True-sharing miss
• False-sharing miss
rnva dovi
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 20 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=20)

### 原始文字层

````text
Snoopy Protocols
````

### 图片文字 OCR（en-US，待对照原页）

````text
Snoopy Protocols
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 21 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=21)

### 原始文字层

````text
Write-invalidate protocols
Memory bus
x System memory
P1 P2
x
P3 P4
clean
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write-invalidate protocols
x
clean
x
emory bus
System memory
````

### 图表辅助说明

总线结构图：P1–P4 各有私有缓存，通过 Memory bus 连接 System memory。当前 x 从主存进入 P2 的缓存，缓存副本标为 clean；这是后续 write-invalidate 动画的初始状态。

## PDF 第 22 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=22)

### 原始文字层

````text
Write-invalidate protocols
Memory bus
x System memory
P1
x
P2
x
P3 P4
x
shared shared shared
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Write-invalidate protocols
                 P1            P2            P3           P4
                 x              x                          x
               shared         shared                     shared
                                Memory bus
                      x       System memory
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write-invalidate protocols
x
shared
x
shared
Memory bus
System memory
x
shared
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 23 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=23)

### 原始文字层

````text
Write-invalidate protocols
Memory bus
x System memory
P1
x
P2
x
P3 P4
x’
invalid invalid modified
Note that P4 is copy is more recent than what the memory has, and this has to be written back to the memory at 
some point.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Write-invalidate protocols
                         P1                   P2                 P3                P4
                          x                    x                                    x’
                        invalid             invalid                             modified
                                              Memory bus
                                 x          System memory
Note that P4 is copy is more recent than what the memory has, and this has to be written back to the memory at
some point.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write-invalidate protocols
x
invalid
x
invalid
Memory bus
System memory
x'
modified
Note that P4 is copy is more recent than what the memory has, and this has to be written back to the memory at
some point.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 24 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=24)

### 原始文字层

````text
Write-invalidate protocols
Memory bus
x’ System memory
P1
x
P2
x’
P3 P4
x’
invalid shared shared
What happens if x’ is not written through to the memory?
znlftnyh
bus
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Write-invalidate protocols
                  P1              P2             P3            P4                bus
                   x              x’      zn l f t n y hx’
                 invalid         shared                       shared
                                   Memory bus
                         x’      System memory
               What happens if x’ is not written through to the memory?
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write-invalidate protocols
p
ared
invalid
x'
shared
System memory
What happens if x' is not written through to the memory?
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 25 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=25)

### 原始文字层

````text
Write-invalidate protocols
Memory bus
x’ System memory
P1
x
P2
x’
P3 P4
x’
invalid shared shared
What happens if x’ is not written through to the memory? Answer: The state is no longer 
“modified”, so if it x’ is not written now, it will never be.
ro's consistent
with memory
need update men
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Write-invalidate protocols
                       P1                 P2                 P3               P4
                        x                  x’                                  x’
                     invalid            shared                               shared
                                           Memory bus                          ro      '      sconsistent
                                                                                       with     memory
                               x’        System memory                              need       update   men
  What happens if x’ is not written through to the memory? Answer: The state is no longer
                     “modified”, so if it x’ is not written now, it will never be.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write-invalidate protocols
invalid
x'
x'
shared
System memory
x'
are
(L17h
need "e
What happens if x' is not written through to the memory? Answer: The state is no longer
"modified", so if it x' is not written now, it will never be.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 26 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=26)

### 原始文字层

````text
Write-invalidate protocols
• The basic write-invalidate protocol is known as the MSI protocol. 
• The name comes from the status bits kept with each cache block to 
maintain coherence.
• In case of MSI: M: Modified, S: Shared, and I: Invalid.
• The MOSI protocol adds another status bit – O: Owned – to MSI
• The MESI protocol adds another status bit – E: Exclusive – to MSI
• The MOESI protocol combines both MOSI and MESI.
More on these protocols later.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Write-invalidate protocols
•The basic write-invalidate protocol is known  as the MSI protocol.
•The name comes from the status  bits kept with each cache block  to
 maintain coherence.
   • In case of MSI: M: Modified, S: Shared, and I: Invalid.
•The MOSI protocol adds  another status bit – O: Owned – to MSI
•The MESI protocol adds another status bit – E: Exclusive – to MSI
•The MOESI protocol combines both MOSI and MESI.
                                More on these protocols later.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write-invalidate protocols
' The basic write-invalidate protocol is known as the MSI protocol.
• The name comes from the status bits kept with each cache block to
maintain coherence.
• In case of MSI: M: Modified, S: Shared, and l: Invalid.
• The MOSI protocol adds another status bit — O: Owned — to MSI
• The MESI protocol adds another status bit — E: Exclusive — to MSI
• The MOESI protocol combines both MOSI and MESI.
More on these protocols later.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 27 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=27)

### 原始文字层

````text
False Sharing
• False sharing occurs when two items that happen to map to the same 
cache line are used by two different processors concurrently, thus 
resulting in a number of cache invalidation operations. 
• Example: Item A and item B map to the same cache line. Item A is written by 
processor core 1 while B is written by processor core 2. Even though 
processor cores 1 and 2 do not share A or B, there will still be invalidation 
operations just because A and B map to the same cache line.
A B
↑ ↑
Core 1 Core 2
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
False Sharing
• False sharing occurs when two items that happen  to map to the same
  cache line are used  by two different processors  concurrently,  thus
  resulting  in a number  of cache invalidation operations.
    • Example: Item A and item B map to the same cache line.  Item A is written by
      processor core 1 while B is written by processor core 2. Even though
      processor cores 1 and 2 do not share A or B, there will still be invalidation
      operations just because A and B map to the same cache line.
             A            B
             ↑            ↑
           Core 1       Core 2
````

### 图片文字 OCR（en-US，待对照原页）

````text
False Sharing
' False sharing occurs when two items that happen to map to the same
cache line are used by two different processors concurrently, thus
resulting in a number of cache invalidation operations.
• Example: Item A and item B map to the same cache line. Item A is written by
processor core 1 while B is written by processor core 2. Even though
processor cores 1 and 2 do not share A or B, there will still be invalidation
operations just because A and B map to the same cache line.
Core 1
Core 2
````

### 图表辅助说明

A 与 B 位于同一个 cache line，Core 1 操作 A、Core 2 操作 B。尽管逻辑变量不同，两核仍会因缓存行共享而互相触发失效，展示 false sharing。

## PDF 第 28 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=28)

### 原始文字层

````text
Exercise
Consider the following code fragment: 
01 double t [8]; double a[1024][8]; // t: total
02 int i, j;
03 ....
04
05 for ( int i = 0; i < 8; ++i ) {
06 for ( int j = 0; j < 1024; ++j ) {
07 t[i] += a[j][i];
08 }
09 }
This code is to be executed in parallel on 
an 8 core system by assigning each of 
the outer loop iteration to a separate core. 
Assuming that sizeof(double) is 8 and 
the cache line size is 64 bytes, what 
performance problems the parallel 
execution may face? How can you fix 
these problems? Re-write the code 
fragment with the problems fixed.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Exercise
 Consider the following code fragment:                                  This code is to be executed in parallel on
 01      double t [8]; double a[1024][8];    // t: total                an 8 core system by assigning each of
 02      int i, j;                                                      the outer loop iteration to a separate core.
 03      ....                                                           Assuming that sizeof(double) is 8 and
 04                                                                     the cache line size is 64 bytes, what
 05      for ( int i = 0; i < 8; ++i ) {                                performance problems the parallel
 06          for ( int j = 0; j < 1024; ++j ) {                         execution may face? How can you fix
 07              t[i] += a[j][i];                                       these problems? Re-write the code
 08          }                                                          fragment with the problems fixed.
 09      }
````

### 图片文字 OCR（en-US，待对照原页）

````text
Exercise
Consider the following code fragment:
01
02
03
04
05
06
08
09
double t double all
int i, j;
for ( int i = 0; i < 8; ++i ) {
for ( intj = 0; j < 1024; ++j ) {
total
This code is to be executed in parallel on
an 8 core system by assigning each of
the outer loop iteration to a separate core.
Assuming that sizeof(double) is 8 and
the cache line size is 64 bytes, what
performance problems the parallel
execution may face? How can you fix
these problems? Re-write the code
fragment with the problems fixed.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 29 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=29)

### 原始文字层

````text
Exercise
t0 t1 t2 t3 t4 t5 t6 t7
a0,0 a0,1 a0,2 a0,3 a0,4 a0,5 a0,6 a0,7
a1,0 a1,1 a1,2 a1,3 a1,4 a1,5 a1,6 a1,7
a2,0 a2,1 a2,2 a2,3 a2,4 a2,5 a2,6 a2,7
... ... ... ... ... ... ... ...
Memory organized as cache lines.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Exercise
                   t0      t1      t2     t3      t4      t5     t6      t7
                   a0,0    a0,1    a0,2   a0,3    a0,4    a0,5   a0,6    a0,7
                   a1,0    a1,1    a1,2   a1,3    a1,4    a1,5   a1,6    a1,7
                   a2,0    a2,1    a2,2   a2,3    a2,4    a2,5   a2,6    a2,7
                     ...    ...     ...     ...     ...    ...     ...     ...
                          Memory organized as cache lines.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Exercise
00
10
a20
01
11
02
12
03
13
a23
04
14
05
15
a25
06
16
a26
07
17
Memory organized as cache lines.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 30 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=30)

### 原始文字层

````text
Exercise
t0 t1 t2 t3 t4 t5 t6 t7
a0,0 a0,1 a0,2 a0,3 a0,4 a0,5 a0,6 a0,7
a1,0 a1,1 a1,2 a1,3 a1,4 a1,5 a1,6 a1,7
a2,0 a2,1 a2,2 a2,3 a2,4 a2,5 a2,6 a2,7
... ... ... ... ... ... ... ...
Memory organized as cache lines.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Exercise
                   t0      t1      t2     t3      t4      t5     t6      t7
                   a0,0    a0,1    a0,2   a0,3    a0,4    a0,5   a0,6    a0,7
                   a1,0    a1,1    a1,2   a1,3    a1,4    a1,5   a1,6    a1,7
                   a2,0    a2,1    a2,2   a2,3    a2,4    a2,5   a2,6    a2,7
                     ...    ...     ...     ...     ...    ...     ...     ...
                          Memory organized as cache lines.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Exercise
00
10
a20
02
12
04
14
06
16
a26
Memory organized as cache lines.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 31 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=31)

### 原始文字层

````text
Reducing False Sharing
• Use local (e.g., register) variables. Write to the memory just at the 
end. 
• Reduce the cache line size. In one extreme where a cache line is no 
bigger than the size of the object, there won't be any false sharing. 
The problem is that this throws away the principle of spatial locality. 
This leads to a drastic increase in compulsory misses.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Reducing False Sharing
•Use local (e. g., register) variables. Write to the memory just at the
 end.
•Reduce the cache line size. In one extreme where a cache line is no
 bigger than the size of the object, there won't be any false sharing.
 The problem  is that this throws away the principle  of spatial locality.
 This leads to a drastic increase in compulsory  misses.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Reducing False Sharing
' Use local (e.g., register) variables. Write to the memory just at the
end.
• Reduce the cache line size. In one extreme where a cache line is no
bigger than the size of the object, there won't be any false sharing.
The problem is that this throws away the principle of spatial locality.
This leads to a drastic increase in compulsory misses.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 32 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=32)

### 原始文字层

````text
Reducing False Sharing
• Use padding to separate out objects into different cache lines. This 
requires analysis and identification of the false sharing, and 
knowledge of the size of the cache line. If the code is to be run on a 
different system with a different cache line size, code needs re-tuning. 
There is wasted memory/cache space. Padding also leads to an 
increase in capacity misses.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Reducing False Sharing
•Use padding  to separate out objects  into different cache lines. This
 requires analysis and identification  of the false sharing , and
 knowledge of the size of the cache line. If the code is to be run on a
 different system with a different cache line size, code needs re-tuning.
 There is wasted memory/cache space. Padding  also leads to an
 increase in capacity misses.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Reducing False Sharing
' Use padding to separate out objects into different cache lines. This
requires analysis and identification of the false sharing, and
knowledge of the size of the cache line. If the code is to be run on a
different system with a different cache line size, code needs re-tuning.
There is wasted memory/cache space. Padding also leads to an
increase in capacity misses.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 33 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=33)

### 原始文字层

````text
Reducing False Sharing
• With some effort, the program could be re-structured to minimize 
false sharing. This approach is program-specific.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Reducing False Sharing
•With some effort, the program could be re-structured   to minimize
 false sharing.  This approach is program-specific.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Reducing False Sharing
' With some effort, the program could be re-structured to minimize
false sharing. This approach is program-specific.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 34 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=34)

### 原始文字层

````text
Write-update protocols
Memory bus
x System memory
P1 P2
x
P3 P4
clean
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write-update protocols
x
clean
x
emory bus
System memory
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 35 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=35)

### 原始文字层

````text
Write-update protocols
Memory bus
x System memory
P1
x
P2
x
P3 P4
x
shared shared shared
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Write-update protocols
                 P1            P2            P3           P4
                 x              x                          x
               shared         shared                     shared
                                Memory bus
                      x       System memory
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write-update protocols
x
shared
x
shared
Memory bus
System memory
x
shared
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 36 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=36)

### 原始文字层

````text
Write-update protocols
Memory bus
x' System memory
P1
x'
P2
x'
P3 P4
x’
shared shared shared
All cached copies are updated as well as the memory.
O change x
to x
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Write-update protocols
                   P                P                P              P     change        x
                     1                2               3           O4
                    x'               x'                             x’           to     x
                  shared           shared                         shared
                                     Memory bus
                          x'       System memory
                      All cached copies are updated as well as the memory.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write-update protocols
x'
shared
x'
x'
shared
System memory
x'
ared
do
All cached copies are updated as well as the memory.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 37 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=37)

### 原始文字层

````text
Write-update protocols
Memory bus
x' System memory
P1 P2 P3 P4
x'
clean
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write-update protocols
Memory bus
System memory
x'
clean
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 38 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=38)

### 原始文字层

````text
Write-update protocols
Memory bus
x' System memory
P1 P2 P3 P4
x'’
modified
No other caches contain a copy, so P4 holds a “modified” block (which is not written through to the memory).
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Write-update protocols
                         P1                  P2                 P3               P4
                                                                                  x'’
                                                                               modified
                                             Memory bus
                                 x'        System memory
No other caches contain a copy, so P4 holds a “modified” block (which  is not written through to the memory).
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write-update protocols
Memory bus
System memory
x"
modified
No other caches contain a copy, so P4 holds a "modified" block (which is not written through to the memory).
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 39 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=39)

### 原始文字层

````text
Write-update protocols
Memory bus
x’’ System memory
P1 P2
x’’
P3 P4
x’’
shared shared
What happens if x’’ is not written through to the memory?
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Write-update protocols
                    P1               P2               P3             P4
                                     x’’                             x’’
                                   shared                          shared
                                      Memory bus
                           x’’      System memory
                 What happens if x’’ is not written through to the memory?
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write-update protocols
shared
System memory
ared
What happens if x" is not written through to the memory?
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 40 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=40)

### 原始文字层

````text
Write-update protocols
Memory bus
x’’ System memory
P1 P2
x’’
P3 P4
x’’
shared shared
What happens if x’’ is not written through to the memory? Answer: The state is no longer 
“modified”, so if it x’’ is not written now, it will never be.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Write-update protocols
                       P1                 P2                 P3               P4
                                          x’’                                  x’’
                                        shared                               shared
                                           Memory bus
                               x’’       System memory
  What happens if x’’ is not written through to the memory? Answer: The state is no longer
                     “modified”, so if it x’’ is not written now, it will never be.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write-update protocols
shared
System memory
ared
What happens if x" is not written through to the memory? Answer: The state is no longer
"modified", so if it x" is not written now, it will never be.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 41 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=41)

### 原始文字层

````text
Write-update protocols
• We look at an example of a write-update protocol example (used by 
DEC Firefly)
• A cache can detect when another cache shares a particular location. The bus 
contains a signal, MSh, which is asserted during a bus operation if another 
cache contains the requested location. 
• Each cache line contains 2 state bits: shared and dirty. There is no valid bit. 
• A write to a shared location is write-through. 
• A write to a non-shared location is write nnn -back
write to memory
only update cash
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Write-update protocols
• We look at an example of a write-update protocol example (used  by
  DEC Firefly)
    • A cache can detect when another cache shares a particular location. The bus
      contains a signal, MSh, which is asserted during a bus operation if another
      cache contains the requested location.
    • Each cache line contains 2 state bits: shared and dirty. There is no valid bit.
    • A write to a shared location is write-through.             write      to     memory
    • A write to a non-shared location is writennn  -back                   update        cash
                                                                 only
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write-update protocols
' We look at an example of a write-update protocol example (used by
DEC Firefly)
A cache can detect when another cache shares a particular location. The bus
contains a signal, MSh, which is asserted during a bus operation if another
cache contains the requested location.
Each cache line contains 2 state bits: shared and dirty. There is no valid bit.
A write to a shared location is write-through.
A write toa on-shared location is write-back
-fro nnemaa
onto wpbte cg5ht
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 42 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=42)

### 原始文字层

````text
Write-update protocols
• There are four states (from status bits shared and dirty). State 
transitions occur at these events:
• PRead: The processor to which the cache belongs reads the location 
corresponding to the cache line. 
• PWrite: The processor to which the cache belongs writes to the location 
corresponding to the cache line. 
• MRead: A processor to which the cache does not belong reads the location 
corresponding to the cache line. 
• MWrite: The processor to which the cache does not belong writes to the 
location corresponding to the cache line. 
• Transitions may depend on whether the bus signal MSh is active or 
not.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Write-update protocols
• There are four states (from status bits shared and dirty). State
  transitions  occur at these events:
    • PRead: The processor to which the cache belongs reads the location
      corresponding to the cache line.
    • PWrite: The processor to which the cache belongs writes to the location
      corresponding to the cache line.
    • MRead: A processor to which the cache does not belong reads the location
      corresponding to the cache line.
    • MWrite: The processor to which the cache does not belong writes to the
      location corresponding to the cache line.
• Transitions  may depend  on whether the bus  signal MSh is active or
  not.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write-update protocols
• There are four states (from status bits shared and dirty). State
transitions occur at these events:
• PRead: The processor to which the cache belongs reads the location
corresponding to the cache line.
• PWrite: The processor to which the cache belongs writes to the location
corresponding to the cache line.
• MRead: A processor to which the cache does not belong reads the location
corresponding to the cache line.
• MWrite: The processor to which the cache does not belong writes to the
location corresponding to the cache line.
' Transitions may depend on whether the bus signal MSh is active or
not.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 43 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=43)

### 原始文字层

````text
Write-update protocols
~Shared
~Dirty
~Shared
Dirty
Shared
~Dirty
Shared
Dirty
PRead PRead, PWrite
PRead, MRead
PRead, MRead,
MWrite, PWrite(MSh)
PMiss (MSh)
PMiss (~MSh)
PWrite
MWrite,
PWrite (MSh)
PWrite (~MSh)
MWrite
MRead, MWrite
A write to a 
shared location is 
write-through. 
A write to a non￾shared location is 
write-back.
if cnet.rs
memory
upda­t­e
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Write-update protocols
                 PRead                                             PRead, PWrite               A write to a
                                                                                               shared location is
                      if~Shared            PWrite             ~Shared                          write-through.
 PMiss (~MSh)           ~Dirty                                  Dirty                       cnet.rsA write to a non-
                                                                                    memory     shared location is
                                                MWrite                                         write-back.
                                                                    update
                                               PWrite (~MSh)
   PMiss (MSh)          Shared                                 Shared
                        ~Dirty             MWrite,              Dirty
                                         PWrite (MSh)
                          PRead, MRead,
                       MWrite, PWrite(MSh)                                PRead, MRead
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write-update protocols
PRead, PWrite
PMiss (NMSh)
PMiss (MSh)
Read
hared
'"Dirty
2
Shared
'"Dirty
Read, MRead,
PWrite
rite
Shared
Dirty
A write to a
shared location is
write-through.
shared location is
write-back.
not Shared
P rite (N
Shared
MWrite,
Dirty
PWrite (MSh)
PRead, MRead
MWrite, PWrite(MSh)
````

### 图表辅助说明

状态图把 Shared 与 Dirty 两个布尔状态组合成四个节点；箭头以处理器读写及总线读写事件标注。旁注强调共享位置的写采用 write-through，非共享位置的写采用 write-back。手写颜色与箭头属于原笔记批注。

## PDF 第 44 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=44)

### 原始文字层

````text
Write-update protocols
• During bootstrapping the caches are placed in a miss mode and are 
pre-filled with data consistent with memory. During normal 
operation, a line can be replaced by other lines, but is never 
invalidated. Having no invalidation facility poses these problems: 
• Pre-filling is a must. 
• Starting a process on a processor which had been executing some other 
process will incur unnecessary coherency operations on the bus. 
• Process migration (when time-sliced, etc.) will result in unnecessary 
coherency operations on the bus.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Write-update protocols
• During  bootstrapping   the caches are placed in a miss mode and are
  pre-filled with data consistent with memory.  During normal
  operation, a line can be replaced by other lines, but is never
  invalidated. Having no invalidation facility poses these problems:
    • Pre-filling is a must.
    • Starting a process on a processor which had been executing some other
      process will incur unnecessary coherency operations on the bus.
    • Process migration (when time-sliced, etc.) will result in unnecessary
      coherency operations on the bus.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write-update protocols
' During bootstrapping the caches are placed in a miss mode and are
pre-filled with data consistent with memory. During normal
operation, a line can be replaced by other lines, but is never
invalidated. Having no invalidation facility poses these problems:
• Pre-filling is a must.
• Starting a process on a processor which had been executing some other
process will incur unnecessary coherency operations on the bus.
• Process migration (when time-sliced, etc.) will result in unnecessary
coherency operations on the bus.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 45 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=45)

### 原始文字层

````text
Write-update protocols
• The savings however are minimal: no need to check for the validity of 
a line (since a line is always valid), and a bit per cache line is saved. 
• If the line is always valid, there will not be any false-sharing misses.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Write-update protocols
•The savings however are minimal:  no need to check for the validity of
 a line (since  a line is always valid), and a bit per cache line is saved.
•If the line is always valid, there will not be any false-sharing  misses.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write-update protocols
' The savings however are minimal: no need to check for the validity of
a line (since a line is always valid), and a bit per cache line is saved.
• If the line is always valid, there will not be any false-sharing misses.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 46 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=46)

### 原始文字层

````text
Write-invalidate protocols
• The basic write-invalidate protocol is known as the MSI protocol. 
• The name comes from the status bits kept with each cache block to 
maintain coherence.
• In case of MSI: M: Modified, S: Shared, and I: Invalid.
• The MOSI protocol adds another status bit – O: Owned – to MSI
• The MESI protocol adds another status bit – E: Exclusive – to MSI
• The MOESI protocol combines both MOSI and MESI.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Write-invalidate protocols
•The basic write-invalidate protocol is known  as the MSI protocol.
•The name comes from the status  bits kept with each cache block  to
 maintain coherence.
   • In case of MSI: M: Modified, S: Shared, and I: Invalid.
•The MOSI protocol adds  another status bit – O: Owned – to MSI
•The MESI protocol adds another status bit – E: Exclusive – to MSI
•The MOESI protocol combines both MOSI and MESI.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write-invalidate protocols
' The basic write-invalidate protocol is known as the MSI protocol.
• The name comes from the status bits kept with each cache block to
maintain coherence.
• In case of MSI: M: Modified, S: Shared, and l: Invalid.
• The MOSI protocol adds another status bit — O: Owned — to MSI
• The MESI protocol adds another status bit — E: Exclusive — to MSI
• The MOESI protocol combines both MOSI and MESI.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 47 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=47)

### 原始文字层

````text
The MSI Protocol
• The MSI protocol is a basic cache coherence protocol used in 
multiprocessor systems to ensure that the multiple caches maintain a 
consistent view of the shared memory. 
• The protocol uses three distinct states to manage the status of cache 
lines across different caches. 
• These states are: Modified (M), Shared (S), and Invalid (I).
• The Invalid state means a cache block is either not valid or not present. 
• Each state indicates a particular status of a cache line in relation to 
the actions that can be performed on it and how it interacts with 
other caches in the system.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
The MSI Protocol
• The MSI protocol is a basic cache coherence protocol used  in
  multiprocessor  systems to ensure that the multiple caches maintain a
  consistent  view of the shared memory.
• The protocol uses three distinct  states to manage the status  of cache
  lines across different caches.
    • These states are: Modified (M), Shared (S), and Invalid (I).
    • The Invalid state means a cache block is either not valid or not present.
• Each state indicates a particular status of a cache line in relation to
  the actions that can be performed on it and how it interacts with
  other caches in the system.
````

### 图片文字 OCR（en-US，待对照原页）

````text
The MSI Protocol
' The MSI protocol is a basic cache coherence protocol used in
multiprocessor systems to ensure that the multiple caches maintain a
consistent view of the shared memory.
• The protocol uses three distinct states to manage the status of cache
lines across different caches.
• These states are: Modified (M), Shared (S), and Invalid (l).
• The Invalid state means a cache block is either not valid or not present.
• Each state indicates a particular status of a cache line in relation to
the actions that can be performed on it and how it interacts with
other caches in the system.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 48 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=48)

### 原始文字层

````text
The M State
• The cache line is only in this cache, and it has been changed from 
what is in the main memory.
• This means the cache line is both exclusive to this cache and dirty (it 
contains data that has not been written back to memory). 一
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
The M State
•The cache line is only in this cache, and it has been changed from
 what is in the main memory.
•This means the cache line is both exclusive to this cache and dirty (it
 contains data that has not been written back to memory).
                                                 ⼀
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
The M State
． The cache line is only in this cache, and it has been changed fro m
what iS in the main memory.
． This m e a n S the cache line is bOth exclusive tO this cache and d i rty (it
contains data that has not been written back tO memory).
````

### 图片文字 OCR（en-US，待对照原页）

````text
The M State
' The cache line is only in this cache, and it has been changed from
what is in the main memory.
• This means the cache line is both exclusive to this cache and dirty (it
contains data that has not been written back to memory).
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 49 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=49)

### 原始文字层

````text
The M State
• Any write operation by this cache does not need to interact with 
other caches or main memory.
• However, if another cache attempts to read or write this data, the 
current cache must write the modified data back to the main memory
and change its state to Shared on a read attempt or Invalid on a write 
attempt.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
The M State
•Any write operation by this cache does not need to interact with
 other caches or main memory.
•However, if another cache attempts to read or write this data, the
 current cache must  write the modified data back to the main memory
 and change its state to Shared       on a read attempt or Invalid       on a write
 attempt.
````

### 图片文字 OCR（en-US，待对照原页）

````text
The M State
' Any write operation by this cache does not need to interact with
other caches or main memory.
• However, if aryther cache attempts to read or write this data, the
current cachevmust write the modified data back to the main memory
and change its state to Shared on a read attempt or Invalid on a write
attempt.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 50 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=50)

### 原始文字层

````text
The S State
• The cache line may be stored in multiple caches simultaneously and is 
consistent with the main memory.
• This state indicates that the data has not been modified in any of the 
caches.
not necessary
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
The S State
•The cache line may be stored in multiple caches simultaneously   and is notnecessary
 consistent  with the main memory.
•This state indicates that the data has not been modified in any of the
 caches.
````

### 图片文字 OCR（en-US，待对照原页）

````text
The S State
hct
' The cache line may be stored in multiple caches simultaneously and is
consistent with the main memory.
• This state indicates that the data has not been modified in any of the
caches.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 51 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=51)

### 原始文字层

````text
The S State
• A cache can read from a cache line in the Shared state without any 
coherence action.
• A Shared cache block is clean (i.e., has the same content in the memory).
• If any cache wants to write to a cache line in the Shared state, all 
other caches that have that line in the Shared state must invalidate 
their copies.
• This ensures that the writing cache can safely change the state of the line to 
Modified without causing incoherence.
一
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
The S State
• A cache can read from a cache line in the Shared                 state without  any
  coherence action.
    • A Shared   cache block is clean (i.e., has the same content in the memory).
• If any cache wants to write to a cache line in the Shared                 state, all
  other caches that have that line in the Shared               state must  invalidate ⼀
  their copies.
    • This ensures that the writing cache can safely change the state of the line to
      Modified   without causing incoherence.
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
The S State
． A cache can read fro m a cache line in the 5h0 化 d state without any
coherence action.
． A Shared cache block is clean (i.e., has the same content i n the memory).
． If any cache wants tO write tO a cache line in the 5h0 化 d state, a ll
other caches that have that line in the Shared state must invalidate
their copies.
． This ensures that the writing cache ca n safely change the state Of the line tO
Modified without causing incoherence.
````

### 图片文字 OCR（en-US，待对照原页）

````text
The S State
' A cache can read from a cache line in the Shared state without any
coherence action.
• A Shared cache block is clean (i.e., has the same content in the memory).
' If any cache wants to write to a cache line in the Shared state, all
other caches that have that line in the Shared state must invalidate
their copies.
• This ensures that the writing cache can safely change the state of the line to
Modified without causing incoherence.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 52 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=52)

### 原始文字层

````text
The I State
• The cache line is not valid for use; it might be stale (out of date) or 
initially empty.
• This state is used to denote that the cache line either needs to be 
fetched from memory or that it has been invalidated due to updates 
from other caches.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
The I State
• The cache line is not valid for use; it might be stale (out of date) or
  initially empty.
• This state is used  to denote that the cache line either needs to be
  fetched from memory or that it has been invalidated due to updates
  from other caches.
````

### 图片文字 OCR（en-US，待对照原页）

````text
The I State
' The cache line is not valid for use; it might be stale (out of date) or
initially empty.
• This state is used to denote that the cache line either needs to be
fetched from memory or that it has been invalidated due to updates
from other caches.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 53 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=53)

### 原始文字层

````text
The I State
• Any attempt to read or write to a cache line in this state necessitates 
a coherence action:
• Read: fetching the data from the main memory and setting the state to 
Shared.
• Write: ensuring all other caches invalidate their copies, and setting the state 
to Modified.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
The I State
• Any attempt to read or write to a cache line in this state necessitates
  a coherence action:
    • Read: fetching the data from the main memory and setting the state to
      Shared.
    • Write: ensuring all other caches invalidate their copies, and setting the state
      to Modified.
````

### 图片文字 OCR（en-US，待对照原页）

````text
The I State
' Any attempt to read or write to a cache line in this state necessitates
a coherence action:
• Read: fetching the data from the main memory and setting the state to
Shared.
• Write: ensuring all other caches invalidate their copies, and setting the state
to Modified.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 54 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=54)

### 原始文字层

````text
Read Hit
• If a processor reads a cache line and it is either in the Modified or 
Shared state, it can directly read the data from the cache.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Read Hit
•If a processor  reads a cache line and it is either in the Modified             or
 Shared    state, it can directly read the data from the cache.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Read Hit
' If a processor reads a cache line and it is either in the Modified or
Shared state, it can directly read the data from the cache.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 55 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=55)

### 原始文字层

````text
Read Miss
• If the cache line is Invalid, the cache must fetch the data from main 
memory or another cache.
• The cache line is set to Shared.
• If fetched from another cache where the line was Modified, the other 
cache must handle the write-back first.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Read Miss
•If the cache line is Invalid, the cache must  fetch the data from main
 memory      or another cache.
•The cache line is set to Shared.
•If fetched from another cache where the line was Modified, the other
 cache must  handle the write-back first.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Read Miss
' If the cache line is Invalid, the cache must fetch the data from main
memory or another cache.
• The cache line is set to Shared.
' If fetched from another cache where the line was Modified, the other
cache must handle the write-back first.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 56 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=56)

### 原始文字层

````text
Write Hit
• If the processor writes to a cache line that is in the Modified state, it 
proceeds with no additional coherence actions.
• If in the Shared state, other caches are signaled to invalidate their 
copies, and the state is changed to Modified.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Write Hit
• If the processor  writes to a cache line that is in the Modified            state, it
  proceeds with no additional coherence actions.
• If in the Shared    state, other caches are signaled to invalidate their
  copies, and the state is changed to Modified.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write Hit
' If the processor writes to a cache line that is in the Modified state, it
proceeds with no additional coherence actions.
• If in the Shared state, other caches are signaled to invalidate their
copies, and the state is changed to Modified.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 57 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=57)

### 原始文字层

````text
Write Miss
• If the line is Invalid, the cache must signal other caches to invalidate if 
they have the line in Shared or Modified, fetch the data, and then set 
the line to Modified.
becauseǕy modified
u
fetch 口 口 15212
dug 么
write back 口 口 国 1212
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Write Miss
•If the line is Invalid, the cache must  signal other caches to invalidate if
 they have the line in Shared     or Modified, fetch the data, and then set
 the line to Modified.
                                         because
                                                                      modified
                                                   Ǖy    u       15212
                                         fe         t      c         h⼝⼝
                                                                    么
                                                    dug
                                    write       back         ⼝    ⼝    国     1212
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Write Miss
． If the line is 仂 va / 冠 ， the cache must signal other caches t0 invalidate if
they have the line in Shared 0 r Modified, fetch the data, and then set
the line to M0dified.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write Miss
' If the line is Invalid, the cache must signal other caches to invalidate if
they have the line in Shared or Modified, fetch the data, and then set
the line to Modified.
locall
@fch O b p b
need u ft
W rP{e I azl< a (2 > p.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 58 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=58)

### 原始文字层

````text
MSI Protocol: Permitted States
M S I
M ✘ ✘ ✓
S ✘ ✓ ✓
I ✓ ✓ ✓
````

### 图片文字 OCR（en-US，待对照原页）

````text
MSI Protocol: Permitted States
````

### 图表辅助说明

MSI 合法状态组合表：两缓存同一块的 (M,M)、(M,S)、(S,M) 不合法；(S,S) 合法；任一方为 I 时表中均允许。行列依次为 M、S、I。

## PDF 第 59 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=59)

### 原始文字层

````text
The MOSI Protocol
• This adds another state, Owned (O), to the MSI protocol.
• The Modified and Invalid states of the MOSI protocol are as in the MSI 
protocol.
• The Shared state means the cache block is valid and shared by 
multiple caches (as in MSI) but the block may be more recent than 
the memory copy. 
• The Owned state is a special case of the Shared state, where when 
the cache sees a Read request on the bus, it provides to the requester 
the requested data without updating memory. Also if the block needs 
replacement, then it needs to be written back to memory.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
The MOSI Protocol
•This adds another state, Owned (O), to the MSI protocol.
•The Modified and Invalid states of the MOSI protocol are as in the MSI
 protocol.
•The Shared state means the cache block is valid and shared by
 multiple  caches (as in MSI) but the block may be more recent than
 the memory copy.
•The Owned state is a special case of the Shared state, where when
 the cache sees a Read request  on the bus,  it provides  to the requester
 the requested data without updating  memory. Also if the block needs
 replacement, then it needs to be written back to memory.
````

### 图片文字 OCR（en-US，待对照原页）

````text
The MOSI Protocol
' This adds another state, Owned (O), to the MSI protocol.
• The Modified and Invalid states of the MOSI protocol are as in the MSI
protocol.
' The Shared state means the cache block is valid and shared by
multiple caches (as in MSI) but the block may be more recent than
the memor co
• The Owned state is a special case of the Shared state, where when
the cache sees a Read request on the bus, it provides to the requester
the re uested data without u datin memor . Also if the block needs
replacement, then it needs to be written back to memory.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 60 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=60)

### 原始文字层

````text
The MOSI Protocol
• The Modified state means that this cache block exists only in this 
cache and is dirty.
• The Owned state means that this cache block may exist in multiple 
caches and may be dirty.
• A read miss request (from another processor) for a block in the M state in MSI 
will need a write-back to memory and change state to S. 
• In MOSI, we change from M to O, supply data the requester, but retain the 
dirty block – there is no need to write-back to memory right away.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
The MOSI Protocol
• The Modified state means that this cache block exists  only in this
  cache and is dirty.
• The Owned state means that this cache block may exist in multiple
  caches and may be dirty.
    • A read miss request (from another processor) for a block in the M state in MSI
      will need a write-back to memory and change state to S.
    • In MOSI, we change from M to O, supply data the requester, but retain the
      dirty block – there is no need to write-back to memory right away.
````

### 图片文字 OCR（en-US，待对照原页）

````text
The MOSI Protocol
' The Modified state means that this cache block exists only in this
cache and is dirty.
• The Owned state means that this cache block may exist in multiple
caches and may be dirty.
• A read miss request (from another processor) for a block in the M state in MSI
will need a write-back to memory and change state to S.
• In MOSI, we change from M to O, supply data the requester, but retain the
dirty block — there is no need to write-back to memory right away.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 61 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=61)

### 原始文字层

````text
The MOSI Protocol
• We go to the Owned state only from the Modified state when we 
have invalidated all other copies elsewhere. 
• At this point we know we are the owner of a dirty copy, and will supply this 
dirty copies to other caches when the attempt to read (upon which those 
caches will have the S status).
• When we have a cache line in the Owned state, any copies we have 
elsewhere in a Shared state will be dirty. 
• This is because the Owned cache line would have supplied this data to the 
caches.
• When we don’t have a cache line in a Owned state, all copies in the 
Shared state will be clean.
回
_
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
The MOSI Protocol回
• We go to the Owned state only from the Modified state when we
  have invalidated all other copies elsewhere.
    • At this point we know we are the owner of a dirty copy, and will supply this
      dirty copies to other caches when the attempt to read (upon which those
      caches will have the S status).
• When we have a cache line in the Owned state, any copies we have
  elsewhere in a Shared state will be dirty_         .
    • This is because the Owned cache line would have supplied this data to the
      caches.
• When we don’t  have a cache line in a Owned state, all copies in the
  Shared state will be clean.
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
The MOSI Protocol
． We go t0 the Owned state only from the Modified state when we
have invalidated all other copies elsewhere.
． At this point we know we a re the 0 w n e r 0f a d irty COPY, and will SUPPIY this
di rty copies tO other caches when the attempt tO read (upon which those
caches will have the S status).
． When we have a cache line in the 0 澎 冂 ed state, any copies we have
elsewhere in a Shared state wi 《 be d i rty.
． This is because the Owned cache ine would have supplied this data t0 the
caches.
． When we don't have a cache line i n a 0 澎 冂 ed state, all copies i n the
Shared state will be clean.
````

### 图片文字 OCR（en-US，待对照原页）

````text
The MOSI Protocol
• We go to the Owned state only from the Modified state when we
have invalidated all other copies elsewhere.
• At this point we know we are the owner of a dirty copy, and will supply this
dirty copies to other caches when the attempt to read (upon which those
caches will have the S status).
• When we have a cache line in the Owned state, any copies we have
elsewhere in a Shared state wi I be dirty.
• This is because the Owned cache ine would have supplied this data to the
caches.
' When we don't have a cache line in a Owned state, all copies in the
Shared state will be clean.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 62 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=62)

### 原始文字层

````text
MOSI Protocol: Permitted States
M O S I
M ✘ ✘ ✘ ✓
O ✘ ✘ ✓ ✓
S ✘ ✓ ✓ ✓
I ✓ ✓ ✓ ✓
````

### 图片文字 OCR（en-US，待对照原页）

````text
MOSI Protocol: Permitted States
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 63 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=63)

### 原始文字层

````text
The MESI Protocol
• This adds another state, Exclusive (E), to the MSI protocol.
• The Modified, Shared and Invalid states of the MESI protocol are as in 
the MSI protocol.
• The Shared state has a clean cache block matching the memory, unlike MOSI 
which may have a dirty block. 
• The Exclusive state means only the current cache has this block.
• If this cache attempts to write this block, the state changes to Modified, and 
no invalidation requests are sent since no-one else has a copy.
• If another cache attempts to read this block, the state changes to Shared.
exclusive 不用invalide
other
copy
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
The MESI Protocol                               exc l u s i ve                不⽤       invalide
• This adds another state, Exclusive (E), to the MSI protocol.                         other
• The Modified, Shared and Invalid states of the MESI protocol are as in copy
  the MSI protocol.
    • The Shared state has a clean cache block matching the memory, unlike MOSI
      which may have a dirty block.
• The Exclusive state means only the current cache has this block.
    • If this cache attempts to write this block, the state changes to Modified, and
      no invalidation requests are sent since no-one else has a copy.
    • If another cache attempts to read this block, the state changes to Shared.
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
The MESI Protocol
一 闺 同
． This adds another state, ExcIusive (E), to the MSI protocol.
． The M0dified, Shared and 忉 va / 冠 states of the MESI protocol a re a s in
the MSI protocol.
． The Shared state has a clean cache block matching the memory, unlike MOSI
which may have a d i rty block.
． The Exclusive state m e a n s only the current cache has this block.
． If this cache attempts tO write this block, the state changes tO Modified, and
no invalidation requests a re sent since no-one else has a COPY.
． If another cache attempts t0 read this block, the state changes t0 Shared.
````

### 图片文字 OCR（en-US，待对照原页）

````text
The MESI Protocol
8)$1
erc(u51vc
' This adds another state, Exclusive (E), to the MSI protocol.
• The Modified, Shared and Invalid states of the MESI protocol are as in
the MSI protocol.
• The Shared state has a clean cache block matching the memory, unlike MOSI
which may have a dirty block.
' The Exclusive state means only the current cache has this block.
• If this cache attempts to write this block, the state changes to Modified, and
no invalidation requests are sent since no-one else has a copy.
• If another cache attempts to read this block, the state changes to Shared.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 64 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=64)

### 原始文字层

````text
MESI Protocol: Permitted States
M E S I
M ✘ ✘ ✘ ✓
E ✘ ✘ ✘ ✓
S ✘ ✘ ✓ ✓
I ✓ ✓ ✓ ✓
````

### 图片文字 OCR（en-US，待对照原页）

````text
MESI Protocol: Permitted States
````

### 图表辅助说明

MESI 合法状态表的行列为 M、E、S、I。M 或 E 只能与另一缓存的 I 共存；S 可与 S 或 I 共存；I 可与所有状态共存。

## PDF 第 65 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=65)

### 原始文字层

````text
MOSI vs. MESI.
• MOSI can be more efficient in scenarios with frequent shared 
modifications, as the Owned state reduces the need for frequent 
memory write-backs.
• MESI is more efficient in scenarios where cache lines are not 
frequently shared between caches, as it reduces unnecessary 
invalidations.
• MESI requires shared data to be clean, while MOSI does not.
• The owner (O) in MOSI is responsible for writing back to the memory when 
the block is evicted.
__
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
MOSI vs. MESI.
•MOSI can be more efficient in scenarios with frequent shared
 modifications,  as the Owned        state reduces the need for frequent
 memory write-backs.
•MESI is more efficient in scenarios where cache lines are not
 frequently shared      between caches, as it reduces unnecessary __
 invalidations.
•MESI requires shared data to be clean, while MOSI does not.
   • The owner (O) in MOSI is responsible for writing back to the memory when
     the block is evicted.
````

### 图片文字 OCR（en-US，待对照原页）

````text
MOSI vs. MESI.
' MOSI can be more efficient in scenarios with frequent shared
modifications, as the Owned state reduces t
need for fre uent
memor write-backs.
• MESI is more efficient in scenarios where cache lines are not
frequently shared between caches, as it reduces unnecessar
invalidations.
• MESI requires shared data to be clean, while MOSI does not.
• The owner (O) in MOSI is responsible for writing back to the memory when
the block is evicted.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 66 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=66)

### 原始文字层

````text
MOSI plus MESI
• The MOESI protocols combines both MOSI and MESI.
• Like MOSI, the Shared state may be dirty (i.e., may have a more 
recent copy of data than memory).
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
MOSI plus MESI
•The MOESI protocols combines  both MOSI and MESI.
•Like MOSI, the Shared state may be dirty (i.e., may have a more
 recent copy of data than memory).
````

### 图片文字 OCR（en-US，待对照原页）

````text
MOSI plus MESI
' The MOESI protocols combines both MOSI and MESI.
• Like MOSI, the Shared state may be dirty (i.e., may have a more
recent copy of data than memory).
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 67 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=67)

### 原始文字层

````text
MOESI Protocol: Permitted States
M O E S I
M ✘ ✘ ✘ ✘ ✓
O ✘ ✘ ✘ ✓ ✓
E ✘ ✘ ✘ ✘ ✓
S ✘ ✓ ✘ ✓ ✓
I ✓ ✓ ✓ ✓ ✓
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
MOESI Protocol: Permitted States
                     M  O   E   S  I
                 M   ✘  ✘   ✘  ✘   ✓
                 O   ✘  ✘   ✘   ✓  ✓
                 E   ✘  ✘   ✘  ✘   ✓
                 S   ✘  ✓   ✘   ✓  ✓
                 I   ✓  ✓   ✓   ✓  ✓
````

### 图片文字 OCR（en-US，待对照原页）

````text
MOESI Protocol:
M
X
X
X
Permitted States
o
X
X
X
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 68 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=68)

### 原始文字层

````text
The Forward (F) State
• In the MESI protocol, when there is a read request to a cache block 
that exists in the Shared state in multiple caches, the read request 
could be serviced by:
• The memory (slow), or
• All the caches that hold the block in the Shared state (too many responses 
sent to the requester)
• The Forward state is a special Shared state that is responsible for 
servicing read requests, eliminating the need for multiple caches to 
respond to read requests.
• Note that Forward is a clean state (as opposed to Owned which is dirty).
t.it rrnnT īns
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
The Forward (F) State
• In the MESI protocol, when there is a read request  to a cache block
  that exists in the Shared state in multiple  caches, the read request
  could be serviced by:
    • The memory (slow), or
    • All the caches that hold the block in the Shared state (too many responses
      sent to the requester)
• The Forward state is a special SharednT state that is responsible  for īns
  servicing read requests,  eliminating  the need for multiple caches to rrn
  respond  to read requests.t.it
    • Note that Forward is a clean state (as opposed to Owned which is dirty).
````

### 图片文字 OCR（en-US，待对照原页）

````text
The Forward (F) State
' In the MESI protocol, when there is a read request to a cache block
that exists in the Shared state in multiple caches, the read request
could be serviced by:
• The memory (slow), or
• All the caches that hold the block in the Shared state (too many responses
sent to the requester)
• The Forward state is a special Shared state that i responsib for
servicing read requests, e Iminatingt e need for multip e caches to
• Note that Forward is a clean state (as opposed to Owned which is dirty).
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 69 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=69)

### 原始文字层

````text
Snoopy protocols
• A snoopy cache protocol relies on the hardware to monitor all writes 
to the memory. If a write is seen by a cache, it needs to either update 
or invalidate the copies that may exist elsewhere in other caches. 
• Snoopy protocols can be efficiently implemented if all the processors 
are connected to the same shared bus, so that each cache can 
monitor the other caches' activity and broadcast invalidates or 
updates. 
• In the absence of a shared bus, communication costs involved in 
broadcasting the write modifications become prohibitively expensive.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Snoopy protocols
•A snoopy cache protocol relies on the hardware to monitor all writes
 to the memory. If a write is seen by a cache, it needs to either update
 or invalidate the copies that may exist elsewhere in other caches.
•Snoopy protocols can be efficiently implemented  if all the processors
 are connected to the same shared bus,  so that each cache can
 monitor the other caches' activity and broadcast  invalidates or
 updates.
•In the absence of a shared bus,  communication  costs involved in
 broadcasting  the write modifications  become prohibitively  expensive.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Snoopy protocols
' A snoopy cache protocol relies on the hardware to monitor all writes
to the memory. If a write is seen by a cache, it needs to either update
or invalidate the copies that may exist elsewhere in other caches.
• Snoopy protocols can be efficiently implemented if all the processors
are connected to the same shared bus, so that each cache can
monitor the other caches' activity and broadcast invalidates or
updates.
• In the absence of a shared bus, communication costs involved in
broadcasting the write modifications become prohibitively expensive.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 70 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=70)

### 原始文字层

````text
Directory-based protocols
• When there is no shared bus, it is more efficient to multicast the write 
modifications to those caches that require them. 
• To do this requires storing information about which caches have 
copies of all cached blocks. 
• A directory-based protocol takes this approach.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Directory-based protocols
•When there is no shared bus,  it is more efficient to multicast  the write
 modifications  to those caches that require them.
•To do this requires storing  information about which caches have
 copies of all cached blocks.
•A directory-based  protocol takes this approach.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Directory-based protocols
' When there is no shared bus, it is more efficient to multicast the write
modifications to those caches that require them.
• To do this requires storing information about which caches have
copies of all cached blocks.
' A directory-based protocol takes this approach.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 71 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=71)

### 原始文字层

````text
Directory-based protocols
• A directory keeps the status of all cache lines. Cache operations 
consult this directory as required. 
• The directory can be centrally kept, or can be distributed. 
• A central directory scheme is easy to implement but it may become a 
bottleneck. A distributed directory is therefore a better choice.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Directory-based protocols
•A directory keeps the status  of all cache lines. Cache operations
 consult  this directory as required.
•The directory can be centrally kept, or can be distributed.
•A central directory scheme is easy to implement  but it may become a
 bottleneck. A distributed  directory is therefore a better choice.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Directory-based protocols
' A directory keeps the status of all cache lines. Cache operations
consult this directory as required.
• The directory can be centrally kept, or can be distributed.
' A central directory scheme is easy to implement but it may become a
bottleneck. A distributed directory is therefore a better choice.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 72 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=72)

### 原始文字层

````text
Directory-based protocols
• Directory-based protocols need to keep quite a lot of state 
information and thus require a fair amount of storage. 
• Yet, these protocols are more scalable than snoopy protocols.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Directory-based protocols
•Directory-based  protocols need to keep quite a lot of state
 information and thus  require a fair amount of storage.
•Yet, these protocols are more scalable than snoopy protocols.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Directory-based protocols
' Directory-based protocols need to keep quite a lot of state
information and thus require a fair amount of storage.
• Yet, these protocols are more scalable than snoopy protocols.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 73 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=73)

### 原始文字层

````text
Directory
• Each cache block has an entry in the directory
• The entry has information about which caches have the 
corresponding cache block and whether or not the block might be 
dirty in some of the caches.
• 1 bit per cache to denote which caches contain the block
• 1 dirty bit
• Cache states are the same, but instead of snooping on a shared bus, 
we are using a directory to ensure coherence.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Directory
• Each cache block  has an entry in the directory
• The entry has information about which caches have the
  corresponding  cache block and whether or not the block might be
  dirty in some of the caches.
    • 1 bit per cache to denote which caches contain the block
    • 1 dirty bit
• Cache states are the same, but instead of snooping  on a shared bus,
  we are using a directory to ensure coherence.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Directory
' Each cache block has an entry in the directory
• The entry has information about which caches have the
corresponding cache block and whether or not the block might be
dirty in some of the caches.
• 1 bit per cache to denote which caches contain the block
• 1 dirty bit
' Cache states are the same, but instead of snooping on a shared bus,
we are using a directory to ensure coherence.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 74 页

[查看此页](../../../../source/711/1/Multiprocessor%2BCaches.pdf#page=74)

### 原始文字层

````text
¿?
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

> OCR 未识别出可靠文字；本页可能以图形、手写公式或空白为主。

### 图表辅助说明

本页中央仅有“¿?”提问／结束标记，没有课件正文。

