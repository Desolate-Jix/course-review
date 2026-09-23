# Caches.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI711/source/711/1/Caches.pdf`
- [打开原文件](../../../../source/711/1/Caches.pdf)
- 原文件 SHA-256：`384072f2d1e3eb4ae9d3d3198501a9fb4fae07497a706bf7b008e5717e4a19af`
- 文件索引：F051；PDF 总页数：29
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../source/711/1/Caches.pdf#page=1)

### 原始文字层

````text
Caches
mano@cs.auckland.ac.nz
````

### 图片文字 OCR（en-US，待对照原页）

````text
Caches
mano@cs.auckland.ac.nz
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../source/711/1/Caches.pdf#page=2)

### 原始文字层

````text
Caches
• A cache is a small local memory holding items of interest
• Items of interest include items we used in the recent past and items we may 
use in the future.
• Example: a browser cache that holds the web content you looked at recently
• Why is such a cache useful?
• Avoiding re-fetching items over a (slow) network
• Processors are a lot faster than memory
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Caches
• A cache is a small local memory holding  items of interest
    • Items of interest include items we used in the recent past and items we may
      use in the future.
    • Example: a browser cache that holds the web content you looked at recently
• Why is such  a cache useful?
    • Avoiding re-fetching items over a (slow) network
    • Processors are a lot faster than memory
````

### 图片文字 OCR（en-US，待对照原页）

````text
Caches
' A cache is a small local memory holding items of interest
• Items of interest include items we used in the recent past and items we may
use in the future.
• Example: a browser cache that holds the web content you looked at recently
• Why is such a cache useful?
• Avoiding re-fetching items over a (slow) network
• Processors are a lot faster than memory
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../source/711/1/Caches.pdf#page=3)

### 原始文字层

````text
Caches
• Assume 5 slots where you can keep numbered (i.e. addressable) 
items.
• Items can be anything so long as they have a unique sequence number (i.e. 
address) with which they can be identified. Example: customer name that is 
identified through a customer id.
• We pick items using their ids (e.g. pick a customer using the customer id). 
• You want to keep in the 5 slots some items that have been used in the 
recent past.
• These 5 slots make up our cache.
• What process should we follow to make our cache work?
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Caches
• Assume  5 slots where you can keep numbered  (i.e. addressable)
  items.
    • Items can be anything so long as they have a unique sequence number (i.e.
      address) with which they can be identified. Example: customer name that is
      identified through a customer id.
    • We pick items using their ids (e.g. pick a customer using the customer id).
• You want to keep in the 5 slots some items that have been used  in the
  recent past.
    • These 5 slots make up our cache.
• What process should  we follow to make our cache work?
````

### 图片文字 OCR（en-US，待对照原页）

````text
Caches
' Assume 5 slots where you can keep numbered (i.e. addressable)
items.
• Items can be anything so long as they have a unique sequence number (i.e.
address) with which they can be identified. Example: customer name that is
identified through a customer id.
• We pick items using their ids (e.g. pick a customer using the customer id).
' You want to keep in the 5 slots some items that have been used in the
recent past.
• These 5 slots make up our cache.
' What process should we follow to make our cache work?
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../source/711/1/Caches.pdf#page=4)

### 原始文字层

````text
Example
Id Item
Cache
Id Item
0 Geoff
1 Joe
2 Nora
3 Allan
4 Rick
5 Gary
6 Ben
7 Chris
8 Mitch
9 Dan
10 Sue
11 Fred
List of Items
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Example
              Id              Item                         Id               Item
                                                           0                Geoff
                                                           1                Joe
                                                           2                Nora
                                                           3                Allan
                                                           4                Rick
                                                           5                Gary
                               Cache                       6                Ben
                                                           7                Chris
                                                           8                Mitch
                                                           9                Dan
                                                           10               Sue
                                                           11               Fred
                                                                         List of Items
````

### 图片文字 OCR（en-US，待对照原页）

````text
Example
Item
Cache
1
2
3
4
5
6
7
8
9
10
11
Item
Geoff
Joe
Nora
Allan
Rick
Gary
Ben
Chris
Mitch
Dan
Sue
Fred
List of Items
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../../source/711/1/Caches.pdf#page=5)

### 原始文字层

````text
Example
Id Item
10 Sue
3 Allan
7 Chris
6 Ben
8 Mitch
Id Item
0 Geoff
1 Joe
2 Nora
3 Allan
4 Rick
5 Gary
6 Ben
7 Chris
8 Mitch
9 Dan
10 Sue
11 Fred
Cache
List of Items
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Example
              Id              Item                          Id               Item
              10              Sue                           0                Geoff
              3               Allan                         1                Joe
              7               Chris                         2                Nora
              6               Ben                           3                Allan
              8               Mitch                         4                Rick
                                                            5                Gary
                               Cache                        6                Ben
                                                            7                Chris
                                                            8                Mitch
                                                            9                Dan
                                                            10               Sue
                                                            11               Fred
                                                                          List of Items
````

### 图片文字 OCR（en-US，待对照原页）

````text
Example
10
3
7
6
8
Item
Sue
Allan
Chris
Ben
Mitch
Cache
1
2
3
4
5
6
7
8
9
10
11
Item
Geoff
Joe
Nora
Allan
Rick
Gary
Ben
Chris
Mitch
Dan
Sue
Fred
List of Items
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../source/711/1/Caches.pdf#page=6)

### 原始文字层

````text
Issues with our Cache
• Searching through the cache for a given id is expensive.
• What is the time complexity of the search, in terms of the size of the cache?
• How do we do the search in hardware? What is the space complexity?
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Issues with our Cache
• Searching through the cache for a given id is expensive.
    • What is the time complexity of the search, in terms of the size of the cache?
    • How do we do the search in hardware? What is the space complexity?
````

### 图片文字 OCR（en-US，待对照原页）

````text
Issues with our Cache
' Searching through the cache for a given id is expensive.
• What is the time complexity of the search, in terms of the size of the cache?
• How do we do the search in hardware? What is the space complexity?
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../../source/711/1/Caches.pdf#page=7)

### 原始文字层

````text
Hardware Complexity
==
==
==
==
==
OR
myId
slot[0].id
slot[3].id
slot[2].id
slot[1].id
slot[4].id
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Hardware Complexity
                                      myId
                                         ==
                  slot[0].id
                  slot[1].id             ==
                  slot[2].id             ==                 OR
                  slot[3].id             ==
                  slot[4].id             ==
````

### 图片文字 OCR（en-US，待对照原页）

````text
Hardware Complexity
myld
slot[0J.id
slot[l].id
slot[2J.id
OR
slot[3].id
slot[4].id
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../../source/711/1/Caches.pdf#page=8)

### 原始文字层

````text
Issues with our Cache
• Is there a way to reduce the complexity (i.e. speed up the search)?
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Issues with our Cache
•Is there a way to reduce the complexity (i.e. speed up the search)?
````

### 图片文字 OCR（en-US，待对照原页）

````text
Issues with our Cache
' Is there a way to reduce the complexity (i.e. speed up the search)?
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../../source/711/1/Caches.pdf#page=9)

### 原始文字层

````text
Direct-Mapped Caches
• In our first attempt, any id from the list can go to any slot in the cache 
– thus there was a need to search every slot in the cache, when we 
looked for an id.
• Now, we have a variant of the cache where an id can go to just one 
predefined slot in the cache.
• Id 0 will go to slot 0 (and only slot 0); id 1 will go to slot 1 (and only slot 1); 
etc; 
• Id 5 will go to slot 0 (and only slot 0); id 6 will go to slot 1 (and only slot 1); 
etc; 
• This is called a direct-mapped cache. In contrast, our first cache is called a 
fully-associative cache (where an id can go to any slot).
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Direct-Mapped Caches
• In our first attempt, any id from the list can go to any slot in the cache
  – thus  there was a need to search every slot in the cache, when we
  looked for an id.
• Now, we have a variant of the cache where an id can go to just one
  predefined  slot in the cache.
    • Id 0 will go to slot 0 (and only slot 0); id 1 will go to slot 1 (and only slot 1);
      etc;
    • Id 5 will go to slot 0 (and only slot 0); id 6 will go to slot 1 (and only slot 1);
      etc;
    • This is called a direct-mapped cache. In contrast, our first cache is called a
      fully-associative cache (where an id can go to any slot).
````

### 图片文字 OCR（en-US，待对照原页）

````text
Direct-Mapped Caches
' In our first attempt, any id from the list can go to any slot in the cache
— thus there was a need to search every slot in the cache, when we
looked for an id.
• Now, we have a variant of the cache where an id can go to just one
predefined slot in the cache.
• ld O will go to slot O (and only slot 0); id 1 will go to slot 1 (and only slot 1);
etc;
• ld 5 will go to slot O (and only slot 0); id 6 will go to slot 1 (and only slot 1);
etc;
• This is called a direct-mapped cache. In contrast, our first cache is called a
fully-associative cache (where an id can go to any slot).
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../source/711/1/Caches.pdf#page=10)

### 原始文字层

````text
Direct-Mapped Caches
Id Item
Cache
Id Item
0 Geoff
1 Joe
2 Nora
3 Allan
4 Rick
5 Gary
6 Ben
7 Chris
8 Mitch
9 Dan
10 Sue
11 Fred
List of Items
Which slot in the cache each id of 
the data will go to?
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Direct-Mapped Caches
             Id              Item                         Id              Item
                                                          0               Geoff
                                                          1               Joe
                                                          2               Nora
                                                          3               Allan
                                                          4               Rick
                                                          5               Gary
                              Cache                       6               Ben
                                                          7               Chris
                                                          8               Mitch
                 Which slot in the cache each id of       9               Dan
                 the data will go to?                     10              Sue
                                                          11              Fred
                                                                       List of Items
````

### 图片文字 OCR（en-US，待对照原页）

````text
Direct-Mapped Caches
Item
Cache
Which slot in the cache each id of
the data will go to?
1
2
3
4
73
6
7
8
9
10
11
Item
Geoff
Joe
Nora
Allan
Rick
Gary
Ben
Chris
Mitch
Dan
Sue
Fred
List of Items
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../source/711/1/Caches.pdf#page=11)

### 原始文字层

````text
Direct-Mapped Cache
• There is now only one slot where a particular id can be. We don’t 
therefore need to search every slot.
• We improve the complexity. 
• Well, do we?
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Direct-Mapped Cache
•There is now only one slot where a particular id can be. We don’t
 therefore need to search every slot.
•We improve the complexity.
   • Well, do we?
````

### 图片文字 OCR（en-US，待对照原页）

````text
Direct-Mapped Cache
' There is now only one slot where a particular id can be. We don't
therefore need to search every slot.
' We improve the complexity.
• Well, do we?
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../source/711/1/Caches.pdf#page=12)

### 原始文字层

````text
Direct-Mapped Cache
• There are two problems with our direct-mapped cache.
• What price is this: 
int where2look = myId % CacheSize
• How do we do this mod better?
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Direct-Mapped Cache
•There are two problems  with our direct-mapped   cache.
•What price is this:
   int where2look = myId % CacheSize
•How do we do this mod better?
````

### 图片文字 OCR（en-US，待对照原页）

````text
Direct-Mapped Cache
' There are two problems with our direct-mapped cache.
• What price is this:
int where2100k = myld % CacheSize
' How do we do this mod better?
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../../source/711/1/Caches.pdf#page=13)

### 原始文字层

````text
Direct-mapped Caches
• In hardware, we can replace the mod operation by a mask operation 
provided that the denominator is a power of 2.
• 11011010 AND 00000011
• Direct-mapped caches in computers therefore have number of entries that is always a power of 2.
• There are very many other things that are powers of 2 when it comes to computing 
hardware. Can you think of some others?
• What is magical about 2?
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Direct-mapped Caches
• In hardware, we can replace the mod operation by a mask operation
  provided that the denominator is a power of 2.
• 11011010  AND 00000011
• Direct-mapped caches in computers therefore have number of entries that
  is always a power of 2.
    • There are very many other things that are powers of 2 when it comes  to computing
      hardware. Can you think of some others?
    • What is magical about 2?
````

### 图片文字 OCR（en-US，待对照原页）

````text
Direct-mapped Caches
' In hardware, we can replace the mod operation by a mask operation
provided that the denominator is a power of 2.
11011010 AND 00000011
' Direct-mapped caches in computers therefore have number of entries that
is always a power of 2.
• There are very many other things that are powers of 2 when it comes to computing
hardware. Can you think of some others?
• What is magical about 2?
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../../source/711/1/Caches.pdf#page=14)

### 原始文字层

````text
Direct-mapped Caches
• Suppose we have a direct-mapped cache of size 4 (i.e. with 4 slots).
• Ids 0, 4, 8, 12, … map to slot 0; ids 1, 5, 9, 13, … map to slot 1; ids 2, 6, 10, 
14, … map to slot 2; and ids 3, 7, 11, 15, … map to slot 3.
• Exercise: Imagine the cache has no valid entries to start with (i.e. cold 
start). Work out if the following accesses are hits or misses in the cache.
• 1, 2, 3, 4, 2, 3, 1, 4, 5
• 1, 4, 1, 4, 1, 4, 1, 4, 1
• 1, 5, 1, 5, 1, 5, 1, 5, 1 
ns
0hit 5 replace 1
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Direct-mapped Caches
• Suppose we have a direct-mapped cache of size 4 (i.e. with 4 slots).
• Ids 0, 4, 8, 12, … map to slot 0; ids 1, 5, 9, 13, … map to slot 1; ids 2, 6, 10,
  14, … map to slot 2; and ids 3, 7, 11, 15, … map to slot 3.
• Exercise: Imagine the cache has no valid entries to start with (i.e. cold
  start). Work out if the following accesses are hits or misses in the cache.
    • 1, 2, 3, 4, 2, 3, 1, 4, 5
    • 1, 4, 1, 4, 1, 4, 1, 4, 1
    • 1, 5, 1, 5, 1, 5, 1, 5, 1      0hit                  5                      1
                  ns                                             re   p   l   a   c   e
````

### 图片文字 OCR（en-US，待对照原页）

````text
Direct-mapped Caches
' Suppose we have a direct-mapped cache of size 4 (i.e. with 4 slots).
' Ids O, 4, 8, 12, ... map to slot O; ids 1, 5, 9, 13, ... map to slot 1; ids 2, 6, 10,
14, ... map to slot 2; and ids 3, 7, 11, 15, ... map to slot 3.
Exercise: Imagine the cache has no valid entries to start with (i.e. cold
start). Work out if the following accesses are hits or misses in the cache.
S replace
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../../source/711/1/Caches.pdf#page=15)

### 原始文字层

````text
Direct-Mapped Caches
Id Item
0
1
2
3
Cache
ids 0, 4, 8, 12, … map to slot 0; 
ids 1, 5, 9, 13, … map to slot 1; 
ids 2, 6, 10, 14, … map to slot 2; 
ids 3, 7, 11, 15, … map to slot 3.
Exercise: Imagine the cache has no valid entries to start with (i.e. cold start). Work 
out if the following accesses are hits or misses in the cache.
1, 2, 3, 4, 2, 3, 1, 4, 5
1, 4, 1, 4, 1, 4, 1, 4, 1
1, 5, 1, 5, 1, 5, 1, 5, 1
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Direct-Mapped Caches
     Id            Item                             ids 0, 4, 8, 12, … map to slot 0;
0                                                   ids 1, 5, 9, 13, … map to slot 1;
                                                    ids 2, 6, 10, 14, … map to slot 2;
1                                                   ids 3, 7, 11, 15, … map to slot 3.
2
3
                   Cache
  Exercise: Imagine the cache has no valid entries to start with (i.e. cold start). Work
  out if the following accesses are hits or misses in the cache.
       1, 2, 3, 4, 2, 3, 1, 4, 5
       1, 4, 1, 4, 1, 4, 1, 4, 1
       1, 5, 1, 5, 1, 5, 1, 5, 1
````

### 图片文字 OCR（en-US，待对照原页）

````text
Direct-Mapped Caches
ids O, 4, 8, 12, .
map to slot 0;
ids 1, 5, 9, 13, ..
map to slot 1;
ids 2, 6, 10, 14, .
. map to slot 2;
ids 3, 7, 11, 15, ...
map to slot 3.
1
2
3
Item
Cache
Exercise: Imagine the cache has no valid entries to start with (i.e. cold start). Work
out if the following accesses are hits or misses in the cache.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../../source/711/1/Caches.pdf#page=16)

### 原始文字层

````text
Direct-mapped Caches
• Direct-mapped caches can lead to thrashing: two items go in and out 
all the time even though there is plenty of space available.
• A cache miss resulting from thrashing is a conflict miss.
• Is there a way to reduce thrashing?
• Is there a way to get rid of thrashing?
• Fully-associative cache – our first cache where an id can go to any slot
• Is there a way to reduce thrashing?
_
抖动 一时釉找回
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Direct-mapped Caches                                              釉    找回
•Direct-mapped  caches can lead to thrashing:  two items go in and out 抖动⼀时
 all the time even though there is plenty of space available._
   • A cache miss resulting from thrashing is a conflict miss.
•Is there a way to reduce thrashing?
•Is there a way to get rid of thrashing?
   • Fully-associative cache – our first cache where an id can go to any slot
•Is there a way to reduce thrashing?
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Direct-mapped Caches
． Direct-mapped caches can lead tO thrashln ： tWO items go in and out
all the time even though there is P enty 0 space available.
． A cache miss resulting from thrashing is a conflict miss.
． ls there a way tO reduce thrashing?
． ls there a way t0 get rid 0f thrashing?
． Fully-associative cache 一 O u r fi rst cache where a n id can go tO a ny slOt
． ls there a way tO reduce thrashing?
````

### 图片文字 OCR（en-US，待对照原页）

````text
Direct-mapped Caches
4vp
' Direct-mapped caches can lead to thrashin : two items go in and out
all the time even though there is p entyo space available.
• A cache miss resulting from thrashing is a conflict miss.
• Is there a way to reduce thrashing?
• Is there a way to get rid of thrashing?
• Fully-associative cache — our first cache where an id can go to any slot
' Is there a way to reduce thrashing?
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../../source/711/1/Caches.pdf#page=17)

### 原始文字层

````text
Direct-Mapped Caches
Id Item
Cache
Which slot in the cache each id of 
the data will go to?
Id Item
0 Geoff
1 Joe
2 Nora
3 Allan
4 Rick
5 Gary
6 Ben
7 Chris
8 Mitch
9 Dan
10 Sue
11 Fred
List of Items
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Direct-Mapped Caches
 Id    Item                               Id              Item
                                          0               Geoff
                                          1               Joe
                                          2               Nora
                                          3               Allan
                                          4               Rick
    Cache                                 5               Gary
                                          6               Ben
Which slot in the cache each id of        7               Chris
the data will go to?                      8               Mitch
                                          9               Dan
                                          10              Sue
                                          11              Fred
                                                    List of Items
````

### 图片文字 OCR（en-US，待对照原页）

````text
Direct-Mapped Caches
Item
Cache
Which slot in the cache each id of
the data will go to?
0
1
2
3
4
5
6
7
8
9
10
11
Geoff
Joe
Nora
Allan
Rick
Gary
Ben
Chris
Mitch
Dan
Sue
Fred
List of Items
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 18 页

[查看此页](../../../../source/711/1/Caches.pdf#page=18)

### 原始文字层

````text
Set-Associative Caches
Id Item
Cache
Id Item
0 Geoff
1 Joe
2 Nora
3 Allan
4 Rick
5 Gary
6 Ben
7 Chris
8 Mitch
9 Dan
10 Sue
11 Fred
List of Items
We have two half-size direct￾mapped caches side-by-side.
Which slot in the cache each id 
of the data will go to?
Id Item
一
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Set-Associative Caches⼀
 Id    Item       Id    Item                Id               Item
                                            0                Geoff
                                            1                Joe
             Cache                          2                Nora
                                            3                Allan
                                            4                Rick
                                            5                Gary
                                            6                Ben
We have two half-size direct-               7                Chris
mapped caches side-by-side.                 8                Mitch
Which  slot in the cache each id            9                Dan
of the data will go to?
                                            10               Sue
                                            11               Fred
                                                       List of Items
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
et-Associative Caches
ltem
Cache
ltem
We have two half-size direct-
mapped caches side-by-side.
Which slot i n the cache each id
of the data will go tO?
0
1
2
3
4
5
6
7
8
9
10
11
ltem
Geoff
」 oe
Nora
Allan
Rick
Gary
Ben
Chris
M itch
Dan
Sue
Fred
List Of ltems
````

### 图片文字 OCR（en-US，待对照原页）

````text
et-Associative Caches
Item
Item
Cache
We have two half-size direct-
mapped caches side-by-side.
Which slot in the cache each id
of the data will go to?
ld
0
1
2
3
4
5
6
7
8
9
10
11
Item
Geoff
Joe
Nora
Allan
Rick
Gary
Ben
Chris
Mitch
Dan
Sue
Fred
List of Items
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 19 页

[查看此页](../../../../source/711/1/Caches.pdf#page=19)

### 原始文字层

````text
Set-Associative Caches
Id Item
Cache
Id Item
0 Geoff
1 Joe
2 Nora
3 Allan
4 Rick
5 Gary
6 Ben
7 Chris
8 Mitch
9 Dan
10 Sue
11 Fred
List of Items
We have 2 slots where each 
data id can go to. This reduces 
thrashing (does it?) but does 
not prevent it.
Id Item
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Set-Associative Caches
 Id    Item       Id    Item                Id               Item
                                            0                Geoff
                                            1                Joe
             Cache                          2                Nora
                                            3                Allan
                                            4                Rick
                                            5                Gary
                                            6                Ben
We have 2 slots where each                  7                Chris
data id can go to. This reduces             8                Mitch
thrashing (does it?) but does               9                Dan
not prevent it.
                                            10               Sue
                                            11               Fred
                                                       List of Items
````

### 图片文字 OCR（en-US，待对照原页）

````text
Set-Associative Caches
Item
Item
Cache
We have 2 slots where each
data id can go to. This reduces
thrashing (does it?) but does
not prevent it.
ld
0
1
2
3
4
5
6
7
8
9
10
11
Item
Geoff
Joe
Nora
Allan
Rick
Gary
Ben
Chris
Mitch
Dan
Sue
Fred
List of Items
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 20 页

[查看此页](../../../../source/711/1/Caches.pdf#page=20)

### 原始文字层

````text
Fully Associative Caches
Id Item
10 Sue
3 Allan
7 Chris
6 Ben
8 Mitch
Cache
Id Item
0 Geoff
1 Joe
2 Nora
3 Allan
4 Rick
5 Gary
6 Ben
7 Chris
8 Mitch
9 Dan
10 Sue
11 Fred
List of Items
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Fully Associative Caches
 Id   Item                            Id             Item
 10   Sue                             0              Geoff
 3    Allan                           1              Joe
 7    Chris                           2              Nora
 6    Ben                             3              Allan
 8    Mitch                           4              Rick
          Cache                       5              Gary
                                      6              Ben
                                      7              Chris
                                      8              Mitch
                                      9              Dan
                                      10             Sue
                                      11             Fred
                                                List of Items
````

### 图片文字 OCR（en-US，待对照原页）

````text
Fully Associative Caches
10
3
7
6
8
Item
1
Sue
Allan
Chris
Ben
Mitch
Cache
ld
0
1
2
3
4
5
6
7
8
9
10
11
Item
Geoff
Joe
Nora
Allan
Rick
Gary
Ben
Chris
Mitch
Dan
Sue
Fred
List of Items
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 21 页

[查看此页](../../../../source/711/1/Caches.pdf#page=21)

### 原始文字层

````text
Fully Associative Caches
• Which of the items to throw out when we need to make room for a 
new item?
• A replacement policy determines this.
• The most commonly used policy is LRU (least-recently-used): every 
slot has a counter; every time a slot is accessed, a global counter is 
incremented and the value stored in the slot counter; the slot with 
the lowest counter value is chosen for replacement.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Fully Associative Caches
•Which  of the items to throw out when we need to make room for a
 new item?
•A replacement policy determines this.
•The most commonly used policy is LRU (least-recently-used):   every
 slot has a counter; every time a slot is accessed, a global counter is
 incremented and the value stored in the slot counter; the slot with
 the lowest counter value is chosen for replacement.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Fully Associative Caches
' Which of the items to throw out when we need to make room for a
new item?
• A replacement policy determines this.
• The most commonly used policy is LRU (least-recently-used): every
slot has a counter; every time a slot is accessed, a global counter is
incremented and the value stored in the slot counter; the slot with
the lowest counter value is chosen for replacement.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 22 页

[查看此页](../../../../source/711/1/Caches.pdf#page=22)

### 原始文字层

````text
Fully-Associative Caches: Exercise
• Suppose we have a fully-associative cache of size 4 (i.e. with 4 slots).
• Exercise: Imagine the cache has no valid entries to start with (i.e. cold 
start). Work out if the following accesses are hits or misses in the 
cache.
• 1, 2, 3, 4, 2, 3, 1, 4, 5
• 1, 4, 1, 4, 1, 4, 1, 4, 1
• 1, 5, 1, 5, 1, 5, 1, 5, 1
• 2, 5, 1, 3, 4, 2, 5, 1, 3
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Fully-Associative Caches: Exercise
• Suppose  we have a fully-associative cache of size 4 (i.e. with 4 slots).
• Exercise: Imagine the cache has no valid entries to start with (i.e. cold
  start). Work out if the following accesses are hits or misses  in the
  cache.
    • 1, 2, 3, 4, 2, 3, 1, 4, 5
    • 1, 4, 1, 4, 1, 4, 1, 4, 1
    • 1, 5, 1, 5, 1, 5, 1, 5, 1
    • 2, 5, 1, 3, 4, 2, 5, 1, 3
````

### 图片文字 OCR（en-US，待对照原页）

````text
Fully-Associative Caches: Exercise
' Suppose we have a fully-associative cache of size 4 (i.e. with 4 slots).
• Exercise: Imagine the cache has no valid entries to start with (i.e. cold
start). Work out if the following accesses are hits or misses in the
cache.
2,
4,
5,
5,
3,
1,
1,
1,
4,
5,
3,
1,
1,
4,
4,
5,
2,
1,
1,
1,
5,
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 23 页

[查看此页](../../../../source/711/1/Caches.pdf#page=23)

### 原始文字层

````text
Further Exercises
• https://cws.auckland.ac.nz/CW/Core/Coursework?cid=Caches
````

### 图片文字 OCR（en-US，待对照原页）

````text
Further Exercises
https://cws.auckland.ac.nz/CW/Core/Coursework?cid=Caches
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 24 页

[查看此页](../../../../source/711/1/Caches.pdf#page=24)

### 原始文字层

````text
Array Layout in Memory
`
Layout is row by row.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Array Layout in Memory
Layout is row by row.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 25 页

[查看此页](../../../../source/711/1/Caches.pdf#page=25)

### 原始文字层

````text
Two ways to sum a 2-D array
const int MAXX = 5;
const int MAXY = 4;
int array[MAXX][MAXY]; // init
int sum = 0;
for ( int i = 0; i < MAXX; ++i )
{
for ( int j = 0; j < MAXY; ++j )
{
sum += array[i][j];
}
}
const int MAXX = 5;
const int MAXY = 4;
int array[MAXX][MAXY]; // init
int sum = 0;
for ( int j = 0; j < MAXY; ++j )
{
for ( int i = 0; i < MAXX; ++i )
{
sum += array[i][j];
}
}
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Two ways to sum a 2-D array
                 const  int MAXX = 5;                               const int MAXX = 5;
                 const  int MAXY = 4;                               const int MAXY = 4;
                 int array[MAXX][MAXY]; // init                     intarray[MAXX][MAXY]; // init
                 int sum = 0;                                       intsum = 0;
                 for ( int i = 0; i < MAXX; ++i )                   for ( intj = 0; j < MAXY; ++j )
                 {                                                  {
                   for ( int j = 0; j < MAXY; ++j )                   for ( inti = 0; i < MAXX; ++i )
                   {                                                  {
                     sum += array[i][j];                               sum += array[i][j];
                   }                                                  }
                 }                                                  }
````

### 图片文字 OCR（en-US，待对照原页）

````text
Two ways to sum a 2-D array
const int MAXX = 5;
const int MAXX = 5;
const int MAXY = 4;
const int MAXY = 4;
int array[MAXX][MAXY]; // init
int array[MAXX][MAXY]; // init
int sum = 0;
int sum = O;
for ( int i = 0; i < MAXX; ++i )
for ( intj = 0; j < MAXY; ++j )
for ( intj = 0; j < MAXY; ++j )
for ( int i = 0; i < MAXX; ++i )
sum +=
sum +=
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 26 页

[查看此页](../../../../source/711/1/Caches.pdf#page=26)

### 原始文字层

````text
Two ways to sum a 2-D array
const int MAXX = 5;
const int MAXY = 4;
int array[MAXX][MAXY]; // init
int sum = 0;
for ( int i = 0; i < MAXX; ++i )
{
for ( int j = 0; j < MAXY; ++j )
{
sum += array[i][j];
}
}
const int MAXX = 5;
const int MAXY = 4;
int array[MAXX][MAXY]; // init
int sum = 0;
for ( int j = 0; j < MAXY; ++j )
{
for ( int i = 0; i < MAXX; ++i )
{
sum += array[i][j];
}
}
a(0,0), a(0,1), a(0,2), a(0,3), 
a(1,0), a(1,1), a(1,2), a(1,3),, 
a(2,0), a(2,1), ... 
Access order = memory layout order
a(0,0), a(1,0), a(2,0), a(3,0), a(4,0), 
a(0,1), a(1,1), a(2,1), a(3,1), a(4,1), 
a(0,2), a(1,2), ...
Access order != memory layout order
舆
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Two ways to sum a 2-D array
                   const  int MAXX = 5;                                  const   int MAXX = 5;
                   const  int MAXY = 4;                                  const   int MAXY = 4;
                   int array[MAXX][MAXY]; // init                        int  array[MAXX][MAXY]; // init
                   int sum = 0;                                          int  sum = 0;
                   for ( int i = 0; i < MAXX; ++i )                      for ( int j = 0; j < MAXY; ++j )
                   {                                                     {
                     for ( int j = 0; j < MAXY; ++j )                       for ( int i = 0; i < MAXX; ++i )
                     {                                                      {
                       sum += array[i][j];                                    sum += array[i][j];
                     }                                                      }
                   }                                                     }
                 a(0,0),  a(0,1),  a(0,2),  a(0,3),                       a(0,0),  a(1,0),  a(2,0),  a(3,0),  a(4,0),
                 a(1,0),  a(1,1),  a(1,2),  a(1,3),,                      a(0,1),  a(1,1),  a(2,1),  a(3,1),  a(4,1),
                 a(2,0),  a(2,1),   ...                                   a(0,2),  a(1,2),  ...
                 Access order     = memory layout order                   Access order     != memory layout order
                           舆
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TWO ways tO S u m a 2-D array
const int M AXX = 5 ；
const int MAXX = 5 ；
const int M AXY = 4 ；
const int M AXY = 4 ；
int array[MAXX] [MAXY]; / / init
int array[MAXX] [MAXY]; / / init
int S u m = 0 ；
int sum = 0 ；
for （ int i = 0 ； i < MAXX; ++i ）
for （ intj = 0 ； j < M AXY; ++j ）
for （ intj = 0 ； j < M AXY; ++j ）
for （ int i = 0 ； i < MAXX; ++i ）
sum + = array[ 刂 [j];
sum + = array[i][j];
Access order = memory layout order
Access order ！ = memory layout order
````

### 图片文字 OCR（en-US，待对照原页）

````text
Two ways to sum a 2-D array
const int MAXX = 5;
const int MAXX = 5;
const int MAXY = 4;
const int MAXY = 4;
int array[MAXX][MAXY]; // init
int array[MAXX][MAXY]; // init
int sum = 0;
int sum = O;
for ( int i = 0; i < MAXX; ++i )
for ( intj = 0; j < MAXY; ++j )
for ( intj = 0; j < MAXY; ++j )
for ( int i = 0; i < MAXX; ++i )
sum +=
sum +=
Access order = memory layout order
Access order != memory layout order
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 27 页

[查看此页](../../../../source/711/1/Caches.pdf#page=27)

### 原始文字层

````text
Access Sequence #1
Array
a(0,0) a(0,1) a(0,2) a(0,3)
a(1,0) a(1,1) a(1,2) a1,3)
a(2,0) a(2,1) a2,2) a(2,3)
a(3,0) a(3,1) a(3,2) a(3,3)
a(4,0) a(4,1) a(4,2) a(4,3)
a(9,0) a(9,1) a(9,2) a(9,3)
a(0,0)
a(0,1)
a(0,2)
a(0,3)
a(1,0)
a(1,1)
a(1,2)
a(1,3)
a(2,0)
a(2,1)
a(2,2)
a(2,3)
a(3,0)
Memory
a(0,0), a(0,1), a(0,2), a(0,3), 
a(1,0), a(1,1), a(1,2), a(1,3),, 
a(2,0), a(2,1), ... 
Access order = memory layout order
Work out the cache hits/misses for the memory 
accesses.
Cache
`
no one
空间盥 品鸣
邀
this
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
no               one
Access Sequence #1                                                          空间盥                                                      鸣
                                                                                                    a(0,0)                   品
                                Array                                                  Memory                                            邀
                                                                                                    a(0,1)
                  a(0,0)   a(0,1)  a(0,2)   a(0,3)
                                                                                                    a(0,2)
                  a(1,0)   a(1,1)  a(1,2)   a1,3)
                                                                                                    a(0,3)
                  a(2,0)   a(2,1)  a2,2)    a(2,3)
                                                                    Cache                           a(1,0)
                  a(3,0)   a(3,1)  a(3,2)   a(3,3)
                                                           `                                        a(1,1)
                  a(4,0)   a(4,1)  a(4,2)   a(4,3)
                                                                                                    a(1,2)
                                                                                                    a(1,3)
                                                                                                    a(2,0)
                  a(9,0)   a(9,1)  a(9,2)   a(9,3)
                                                                                                    a(2,1)
                                a(0,0),  a(0,1),  a(0,2),  a(0,3),                                  a(2,2)
                                a(1,0),  a(1,1),  a(1,2),  a(1,3),,                                 a(2,3)
                                a(2,0),  a(2,1),   ...                                              a(3,0)
                        thisAccess order         = memory layout order
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Access Sequence # 1
Array
匚 彐 氕 兑
a00 ）
a （ 1
a （ 乙 0 ）
a 0 ）
a@0 ）
a01 ）
a （ 1 ， 1
a （ 乙 1 ）
a 1 ）
a （ 生 1 ）
a02 ）
a （ 1 ， 2
a2 ， 2 ）
a02 ）
a （ 生 2 ）
a （ 2 ， 0 ）
a03 ）
al ， 3
a （ 2 ， 3 ）
Cache
a03 ）
a （ 4 ， 3 ）
Memory
a01 ）
a02 ）
a （ 0 司
a(1,0)
a （ 1
a （ 1
a （ 1 司
a （ 乙 0 ）
a （ 乙 1 ）
a （ 乙 2 ）
a （ 乙 3 ）
a 0 ）
0
0
0
0
0
0
0
0
0
s order = memory layout order
````

### 图片文字 OCR（en-US，待对照原页）

````text
one
Access Sequence #1
Array
al,3
a2,2)
a
Memory
Cache
o
o
0
06
s order = memory layout order
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 28 页

[查看此页](../../../../source/711/1/Caches.pdf#page=28)

### 原始文字层

````text
Access Sequence #2
Array
a(0,0) a(0,1) a(0,2) a(0,3)
a(1,0) a(1,1) a(1,2) a1,3)
a(2,0) a(2,1) a2,2) a(2,3)
a(3,0) a(3,1) a(3,2) a(3,3)
a(4,0) a(4,1) a(4,2) a(4,3)
a(9,0) a(9,1) a(9,2) a(9,3)
a(0,0)
a(0,1)
a(0,2)
a(0,3)
a(1,0)
a(1,1)
a(1,2)
a(1,3)
a(2,0)
a(2,1)
a(2,2)
a(2,3)
a(3,0)
Cache
`
Memory
a(0,0), a(1,0), a(2,0), a(3,0), a(4,0), 
a(0,1), a(1,1), a(2,1), a(3,1), a(4,1), 
a(0,2), a(1,2), ...
Access order != memory layout order
Work out the cache hits/misses for the memory 
accesses.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Access Sequence #2
                                                                                                                           a(0,0)
                                       Array                                                               Memory
                                                                                                                           a(0,1)
                       a(0,0)    a(0,1)     a(0,2)    a(0,3)
                                                                                                                           a(0,2)
                       a(1,0)    a(1,1)     a(1,2)    a1,3)
                                                                                                                           a(0,3)
                       a(2,0)    a(2,1)     a2,2)     a(2,3)
                                                                                    Cache                                  a(1,0)
                       a(3,0)    a(3,1)     a(3,2)    a(3,3)
                                                                         `                                                 a(1,1)
                       a(4,0)    a(4,1)     a(4,2)    a(4,3)
                                                                                                                           a(1,2)
                                                                                                                           a(1,3)
                                                                                                                           a(2,0)
                       a(9,0)    a(9,1)     a(9,2)    a(9,3)
                                                                                                                           a(2,1)
                                               a(0,0),  a(1,0),  a(2,0),  a(3,0),  a(4,0),                                 a(2,2)
                                               a(0,1),  a(1,1),  a(2,1),  a(3,1),  a(4,1),                                 a(2,3)
                                               a(0,2),  a(1,2),  ...                                                       a(3,0)
                                               Access order          != memory layout order
````

### 图片文字 OCR（en-US，待对照原页）

````text
Access Sequence #2
Array
al,3
a2,2)
Memory
Cache
Access order != memory layout order
o
o
0
06
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 29 页

[查看此页](../../../../source/711/1/Caches.pdf#page=29)

### 原始文字层

````text
¿?
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

> OCR 未识别出可靠文字；本页可能以图形、手写公式或空白为主。

### 图表辅助说明

本页中央仅有“¿?”提问／结束标记，没有课件正文。

