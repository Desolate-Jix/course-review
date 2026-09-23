# DB51_2025_Deadlocks.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI751/source/751%25/DB51_2025_Deadlocks.pdf`
- [打开原文件](../../../source/751%2525/DB51_2025_Deadlocks.pdf)
- 原文件 SHA-256：`ce32bb2c5093334407c0a904d4adbf9e97995bd8f67edafb244ef9b7a5e38215`
- 文件索引：F159；PDF 总页数：17
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../source/751%2525/DB51_2025_Deadlocks.pdf#page=1)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 1
Deadlocks
• Precedence Graph
• Deadlock while Lock Upgrade
• Read for Update
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Deadlock s
  •  Precedence Graph
  •  Deadlock while Lock Upgrade
  •  Read for Update
  35   1/ 7   51               Geral  d Webe r's  TA Ma nag ement   Slid es                     1
````

### 图片文字 OCR（en-US，待对照原页）

````text
Deadlocks
Precedence Graph
Deadlock while Lock Upgrade
Read for Update
351/751
Gerald Weber's TA Management Slides
1
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../source/751%2525/DB51_2025_Deadlocks.pdf#page=2)

### 原始文字层

````text
From Wikipedia
351/751 TA Management 2
````

### 图片文字 OCR（en-US，待对照原页）

````text
From Wikipedia
EDIA
vclopedia
tent
kipedia
re
dia
ortal
Jes
351/751
Transactional Synchronization
Extensions
From Wikipedia, the free encyclopedia
Transactional Synchronization Extensions (TSX-NI) is an extension to
the x86 instruction set architecture (ISA) that adds hardware transactional
memory support, speeding up execution of multi-threaded software through
lock elision. According to different benchmarks, TSX can provide around
40% faster applications execution in specific workloads, and 4—5 times
more database transactions per second
TSX was documented by Intel in February 2012, and debuted in June 2013
on selected Intel microprocessors based on the Haswell microarchitecture.
Haswell processors below 45xx as well as R-series and K-series
(with unlocked multiplier) SKUs do not support TSX.[8] In August 2014, Intel
announced a bug in the TSX implementation on current steppings of
Haswell- Haswell-F- Haswell-FP and earlv Broadwell CPUs- which resulted
TA Management
2
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../source/751%2525/DB51_2025_Deadlocks.pdf#page=3)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 3
Recap: Conflicts in a schedule
• Conflicts are a concept to capture the pairwise relationship 
of operations (and by extension transactions) accessing the 
same object in a schedule.
• Each operation writing an object has one conflict with each 
operation by a different transaction accessing this object. 
We write these conflicts for object x:
r1[x], r2[x], c2, w1[x], c1, r3[x], w3[x], c3
• As ordered pairs of operations:
• r2[x], w1[x], and w1[x], r3[x], and also w1[x], w3[x],
• r1[x], w3[x], and r2[x], w3[x].
• Idea: order in which transactions commit should be 
compatible with this order.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Recap: Confli cts i n a schedul e
• Conflicts are a concept to capture the pairwise relationship
  of operati  ons ( and by extension transactions) accessing the
  same     object i  n a schedule.
• Each operation w  riting an object has one conflict with each
  operation by a different tr ansaction accessing this object.
  We write these conflicts for           object x:
    r1[x], r2[x], c2, w1[x], c1, r3[x], w3[x], c3
• As ordered pairs of operations:
• r2[x], w1[x],   and w1[x],      r3[x], and also w1[x], w3[x],
• r1[x], w3[x],   and r2[x],    w3[x].
• Idea: order in which tr ansactions commit shoul  d be
  compatible with thi  s order.
35   1/ 7   51              Geral d Weber's TA Management  Slides                 3
````

### 图片文字 OCR（en-US，待对照原页）

````text
Recap: Conflicts in a schedule
Conflicts are a concept to capture the pairwise relationship
of operations (and by extension transactions) accessing the
same object in a schedule.
Each operation writing an object has one conflict with each
operation by a different transaction accessing this object.
We write these conflicts for object x:
WI [x] Cl, rdx],
W3[x], 3
As ordered pairs of operations:
and WI [x], r3[x], and also WI [x], W3[x],
W3[x],
and r2[x],
W3[x]
Idea: order in which transactions commit should be
compatible with this order.
351/751
Gerald Weber's TA Management Slides
3
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../source/751%2525/DB51_2025_Deadlocks.pdf#page=4)

### 原始文字层

````text
TA3
351/751 Gerald Weber's TA Management Slides
Precedence graph 
• We interpret the conflicts as directed edges, 
which we see as going from the transaction of 
the earlier operation in the conflict to the 
transaction of the later operation. 
• The resulting directed graph we call the 
precedence graph, of that schedule.
• Idea still: order in which transactions commit 
should be compatible with this order.
• Definition: A schedule is conflict-serializable 
iff the precedence graph is free of cycles.
• r1[x], r2[x], c2, w1[x], c1, r3[x], w3[x], c3
TA1
TA2
4
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Prec edenc e graph
• We interpret the conflicts as directed edges,
  which we see as going from the tr ansaction of
  the earlier operation in the conflict to the
  tr ansaction of the l  ater operati  on.                                          TA           3
• T he r esul  ti  ng directed graph we cal  l the
  precedence graph, of that schedule.                               TA           1
• Idea still  : order in which transacti  ons commit                              TA           2
  should be compatible with this order.
• Definition: A  schedule is confli  ct-serializable
  iff  the precedence graph is free of cycles.
• r1[x], r2[x], c2, w1[x], c1, r3[x], w3[x], c3
35   1/ 7   51                Geral d Weber's TA Management  Slides                     4
````

### 图片文字 OCR（en-US，待对照原页）

````text
Precedence graph
We interpret the conflicts as directed edges,
which we see as going from the transaction of
the earlier operation in the conflict to the
transaction of the later operation.
The resulting directed graph we call the
precedence graph, of that schedule.
Idea still: order in which transactions commit
should be compatible with this order.
Definition: A schedule is conflict-serializable
iff the precedence graph is free of cycles.
rl[x], r2[x], WI Cl, r3[x], W3[x],
TAI
351/751
Gerald Weber's TA Management Slides
, TA3
TA2
4
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../source/751%2525/DB51_2025_Deadlocks.pdf#page=5)

### 原始文字层

````text
TA3
351/751 Gerald Weber's TA Management Slides
Precedence graph 
• We interpret the conflicts as directed edges, 
which we see as going from the transaction of 
the earlier operation in the conflict to the 
transaction of the later operation. 
• The resulting directed graph we call the 
precedence graph, of that schedule.
• Idea still: order in which transactions commit 
should be compatible with this order.
• Only if the precedence graph is free of cycles 
the schedule is serializable.
• r1[x], r2[x], c2, w1[x], c1, r3[x], w3[x], c3
TA1
TA2
5
x
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Prec edenc e graph
• We interpret the conflicts as directed edges,
  which we see as going from the tr ansaction of
  the earlier operation in the conflict to the
  tr ansaction of the l  ater operati  on.                                         TA           3
• T he r esul  ti  ng directed graph we cal  l the
  precedence graph, of that schedule.                              TA           1x
• Idea still  : order in which transacti  ons commit                              TA           2
  should be compatible with this order.
• Only if the precedence graph is free of cycles
  the schedule is serializable.
• r1[x], r2[x], c2, w1[x], c1, r3[x], w3[x], c3
35   1/ 7   51                Geral d Weber's TA Management  Slides                     5
````

### 图片文字 OCR（en-US，待对照原页）

````text
Precedence graph
We interpret the conflicts as directed edges,
which we see as going from the transaction of
the earlier operation in the conflict to the
transaction of the later operation.
The resulting directed graph we call the
precedence graph, of that schedule.
Idea still: order in which transactions commit
should be compatible with this order.
TAI
Only if the precedence graph is free of cycles
the schedule is serializable.
rl[x], r2[x], WI Cl, r3[x], W3[x],
351/751
Gerald Weber's TA Management Slides
, TA3
x
TA2
5
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../source/751%2525/DB51_2025_Deadlocks.pdf#page=6)

### 原始文字层

````text
TA3
351/751 Gerald Weber's TA Management Slides
Precedence graph 
• We interpret the conflicts as directed edges, 
which we see as going from the transaction of 
the earlier operation in the conflict to the 
transaction of the later operation. 
• The resulting directed graph we call the 
precedence graph, of that schedule.
• Idea still: order in which transactions commit 
should be compatible with this order.
• Only if the precedence graph is free of cycles 
the schedule is serializable.
• r1[x], r2[x], c2, w1[x], c1, r3[x], w3[x], c3
TA1
TA2
6
x
x
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Prec edenc e graph
• We interpret the conflicts as directed edges,
  which we see as going from the tr ansaction of
  the earlier operation in the conflict to the
  tr ansaction of the l  ater operati  on.                                         TA           3
• T he r esul  ti  ng directed graph we cal  l the                           x
  precedence graph, of that schedule.                              TA           1x
• Idea still  : order in which transacti  ons commit                              TA           2
  should be compatible with this order.
• Only if the precedence graph is free of cycles
  the schedule is serializable.
• r1[x], r2[x], c2, w1[x], c1, r3[x], w3[x], c3
35   1/ 7   51                Geral d Weber's TA Management  Slides                     6
````

### 图片文字 OCR（en-US，待对照原页）

````text
Precedence graph
We interpret the conflicts as directed edges,
which we see as going from the transaction of
the earlier operation in the conflict to the
transaction of the later operation.
The resulting directed graph we call the
precedence graph, of that schedule.
Idea still: order in which transactions commit
should be compatible with this order.
TAI
Only if the precedence graph is free of cycles
the schedule is serializable.
rl[x], r2[x], WI Cl, r3[x], W3[x],
351/751
Gerald Weber's TA Management Slides
TA3
x
x
TA2
6
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../source/751%2525/DB51_2025_Deadlocks.pdf#page=7)

### 原始文字层

````text
TA3
351/751 Gerald Weber's TA Management Slides
Precedence graph 
• We interpret the conflicts as directed edges, 
which we see as going from the transaction of 
the earlier operation in the conflict to the 
transaction of the later operation. 
• The resulting directed graph we call the 
precedence graph, of that schedule.
• Idea still: order in which transactions commit 
should be compatible with this order.
• Only if the precedence graph is free of cycles 
the schedule is serializable.
• r1[x], r2[x], c2, w1[x], c1, r3[x], w3[x], c3
TA1
TA2
7
x
x x
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Prec edenc e graph
• We interpret the conflicts as directed edges,
  which we see as going from the tr ansaction of
  the earlier operation in the conflict to the
  tr ansaction of the l  ater operati  on.                                         TA           3
• T he r esul  ti  ng directed graph we cal  l the                           x         x
  precedence graph, of that schedule.                              TA           1x
• Idea still  : order in which transacti  ons commit                              TA           2
  should be compatible with this order.
• Only if the precedence graph is free of cycles
  the schedule is serializable.
• r1[x], r2[x], c2, w1[x], c1, r3[x], w3[x], c3
35   1/ 7   51                Geral d Weber's TA Management  Slides                     7
````

### 图片文字 OCR（en-US，待对照原页）

````text
Precedence graph
We interpret the conflicts as directed edges,
which we see as going from the transaction of
the earlier operation in the conflict to the
transaction of the later operation.
The resulting directed graph we call the
precedence graph, of that schedule.
Idea still: order in which transactions commit
should be compatible with this order.
x
TAI
Only if the precedence graph is free of cycles
the schedule is serializable.
rl[x], r2[x], WI Cl, r3[x], W3[x],
351/751
Gerald Weber's TA Management Slides
TA3
x
x
TA2
7
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../source/751%2525/DB51_2025_Deadlocks.pdf#page=8)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides
Deadlock: cycle in precedence graph 
• Deadlock:
• The precedence graph including the operations blocked and 
not yet executed at a point t in time contains a cycle: 
• s: r2[x], w3[y] 
• TA1: w1[x] _____________? 
• TA2: r2[x], r2[y] ________? 
• TA3: w3[y], w3[x]______? 
t
8
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Deadlock : c ycl e i n precedence gr aph
•  Deadlock:
•  T he precedence graph including the operations bl  ocked and
   not yet executed at a point t in time contai  ns a cycle:
•    s:      r2[x],     w3[y]
•  TA1:         w1[x] __ ___ ___ ___ __?
•  TA2:   r2[x],             r2[y] __ ___ ___ ?
•  TA3:               w3[y],      w3[x]_ ___ __?
                                      t
35   1/ 7   51                   Geral d Weber's TA Management  Slides                          8
````

### 图片文字 OCR（en-US，待对照原页）

````text
Deadlock: cycle in precedence graph
Deadlock:
The precedence graph including the operations blocked and
not yet executed at a point t in time contains a cycle:
s:
, TAI:
, TA2:
, TA3:
351/751
W3[y], W3[x]
t
Gerald Weber's TA Management Slides
8
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../source/751%2525/DB51_2025_Deadlocks.pdf#page=9)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides
Deadlock: cycle in precedence graph 
• Deadlock:
• The precedence graph including the operations 
blocked and not yet executed at a point t in time 
contains a cycle: 
• s: r2[x], w3[y] 
• TA1: w1[x] _____________? 
• TA2: r2[x], r2[y] ________? 
• TA3: w3[y], w3[x]______? 
t
9
At time t:
TA3
TA1
TA2
x
x y
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Deadlock : c ycl e i n precedence gr aph
•  Deadlock:
•  T he precedence graph including the operations
   blocked and not yet executed at a point t in time
   contai  ns a cycle:
•    s:      r2[x],     w3[y]
•  TA1:         w1[x] __ ___ ___ ___ __?
•  TA2:   r2[x],             r2[y] __ ___ ___ ?                                               TA           3
•  TA3:               w [y],      w[x]_ ___ __?               At  time  t:             x         y
                       3          3
                                                                                            x
                                                                           TA           1   TA           2
                                        t
35   1/ 7   51                    Geral d Weber's TA Management  Slides                              9
````

### 图片文字 OCR（en-US，待对照原页）

````text
Deadlock: cycle in precedence graph
Deadlock:
The precedence graph including the operations
blocked and not yet executed at a point t in time
contains a cycle:
s:
TAI:
TA2:
, TA3:
351/751
r2[x], W3[y]
W3[y], W3[x]
TA3
At time t:
x
TAI
t
Gerald Weber's TA Management Slides
x
TA2
9
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../source/751%2525/DB51_2025_Deadlocks.pdf#page=10)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slide Set 10
Deadlocks while attempting lock upgrade
• Transactions mostly read x before they write x. 
• On the common scheduler, this results in a lock upgrade: 
the transaction first has a read lock on x, then upgrades 
this to a write lock on x. 
• This process can result in a deadlock: 
∙ s: r1[x], r2[x], ..................... ?
∙ TA1: r1[x], w1[x] _____________?
∙ TA2: r2[x], w2[x] _______?
• This is bound to happen eventually, if transactions take 
some finite amount of time.
• Solution: Clients declare intention to write….
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Deadlock s whi le attempting lock upgrade
•  T ransactions m ostly read x before they w  rite x.
•  On the comm on scheduler, this r esults in a lock upgrade:
   the tr ansaction first has a read l  ock on x, then upgrades
   this to a write l  ock on x.
•  T hi  s process can r esult in a               deadl   ock     :
           ∙   s:               r1[x   ],    r2[x   ],    ...   ...   ...   ...   ...   ...   ...         ?
           ∙  TA1:   r  1[x   ],                  w1[x ] _____________?
           ∙  TA2:              r2[x   ],                       w2[x ] _______?
•  T hi  s i  s bound to happen eventually, if  tr ansactions take
   som e finite amount of time.
•  Solution: Clients declare  intention to write….
35   1/ 7   51                   Geral d Weber's TA Management  Slide Set                             10
````

### 图片文字 OCR（en-US，待对照原页）

````text
Deadlocks while attempting lock upgrade
Transactions mostly read x before they write x.
On the common scheduler, this results in a lock upgrade:
the transaction first has a read lock on x, then upgrades
this to a write lock on x.
This process can result in a deadlock:
r2[x], .
TAI: rl[x],
TA2:
This is bound to happen eventually, if transactions take
some finite amount of time.
Solution: Clients declare intention to write....
351/751
Gerald Weber's TA Management Slide Set
10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../source/751%2525/DB51_2025_Deadlocks.pdf#page=11)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 11
Early declaration of intention to upgrade
• The aforementioned deadlock:
∙ s: r1[x], r2[x], ..................... ?
∙ TA1: r1[x], w1[x] _____________?
∙ TA2: r2[x], w2[x] _______?
• Solution: Use “SELECT ... FOR UPDATE”
• This is a read operation that expresses intent to write.
• We indicate this operation with capital R[ ] in the schedule 
(this is an extension of the basic transaction model):
• Implementation is left to database, we use:
• R[ ] is, with regard to locking, treated like a write:
∘ requires X lock (and U lock) before even reading.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Earl y dec laration of intention to upgrade
•  T he aforementioned                  deadl   ock    :
           ∙   s:               r1[x   ],    r2[x   ],    ...   ...   ...   ...   ...   ...   ...         ?
           ∙  TA1:   r  1[x   ],                  w1[x ] _____________?
           ∙  TA2:              r2[x   ],                       w2[x ] _______?
•  Solution: Use “SE LECT  ... FOR UP DAT E”
•  T hi  s i  s a r ead operation that expresses intent to write.
•  We indicate this operation w  ith capital R[ ] in the schedule
   (thi  s i  s an extension of the basi  c tr ansaction m odel):
•  Im pl  em entation is left to database, w  e use:
•  R[ ] is, wit h r egard  to  locking , t reated like a writ e:
     ∘   requires X lock (and U lock) before even r eadi  ng.
35   1/ 7   51                  Geral  d Webe r's  TA Ma nag ement   Slid es                           11
````

### 图片文字 OCR（en-US，待对照原页）

````text
Early declaration of intention to upgrade
The aforementioned deadlock:
rl r2[x], .
s:
, TAI: rl[x],
, TA2:
, Solution: Use "SELECT ... FOR UPDATE"
This is a read operation that expresses intent to write.
We indicate this operation with capital ] in the schedule
(this is an extension of the basic transaction model):
Implementation is left to database, we use:
RI ] is, with regard to locking, treated like a write:
o requires X lock (and U lock) before even reading.
351/751
Gerald Weber's TA Management Slides
11
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../source/751%2525/DB51_2025_Deadlocks.pdf#page=12)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slide Set 3 12
Early declaration of intention to upgrade
• The aforementioned deadlock:
∙ s: r1[x], r2[x], ..................... ?
∙ TA1: r1[x], w1[x] _____________?
∙ TA2: r2[x], w2[x] _______?
• Alternative using R (“SELECT ... FOR UPDATE”)
∙ s: R1[x], w1[x], c1 R2[x], w2[x], c2
∙ TA1: R1[x], w1[x], c1
∙ TA2: R2[x] ____________, w2[x], c2
• the simple scheduler: all reads are “FOR UPDATE”
transaction TA2 is waiting, because TA1 has the exclusive lock on x
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Earl y dec laration of intention to upgrade
•   T he aforementioned                        deadl   ock        :
             ∙    s:               r1[x   ],    r2[x   ],    ...   ...   ...   ...   ...   ...   ...         ?
             ∙   TA1:   r    1[x   ],                  w1[x ] _____________?
             ∙   TA2:              r 2[x   ],                       w2[x ] _______?
•   Al  ternati  ve using R (“SE LECT  ... FOR UP DAT E”)
             ∙   s:                R1[x   ],                  w1[x   ],    c1 R2[x   ],     w2[x   ],    c2
             ∙   TA1:   R     1[x   ],                  w1[x   ],    c1
             ∙   TA2:              R  2[x ] ____________,  w               2[x   ],    c2
  transact ion  TA2 is  waiting,  bec aus e  TA1 has t he  exclusiv e lock  on  x
•   the si  mple scheduler: al  l reads are “F OR UPDA TE ”
35   1/ 7   51                         Geral d Weber's TA Management  Slide Set 3                                         12
````

### 图片文字 OCR（en-US，待对照原页）

````text
Early declaration of intention to upgrade
The aforementioned deadlock:
rl[x], r2[x], .
s:
, TAI: rl[x],
, TA2:
Alternative using R ("SELECT ... FOR UPDATE")
Wl[x], R2[x],
TAI: Rl[x],
, TA2:
R2[X]
, W2[x], C2
transaction TA2 is waiting, because TAI has the exclusive lock on x
, the simple scheduler: all reads are "FOR UPDATE"
351/751
Gerald Weber's TA Management Slide Set 3
12
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../source/751%2525/DB51_2025_Deadlocks.pdf#page=13)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 13
Only one transaction uses R[ ]
• Can the following transactions run into a deadlock ?
∙ TA1: r1[x], w1[x], c1
∙ TA2: R2[x], w2[x], c2
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Only  one transaction us es  R[  ]
•  Can the following transactions r un i  nto a deadlock                                          ?
            ∙   TA1:   r  1[x   ],          w1[x   ],    c1
            ∙   TA2:   R   2[x   ],      w2[x   ],    c2
 35   1/ 7   51                     Geral  d Webe r's  TA Ma nag ement   Slid es                                 13
````

### 图片文字 OCR（en-US，待对照原页）

````text
Only one transaction uses RI ]
Can the following transactions run into a deadlock ?
, TAI: rl[x],
, TA2: R2[x], WAX],
351/751
Gerald Weber's TA Management Slides
13
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../source/751%2525/DB51_2025_Deadlocks.pdf#page=14)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 14
Only one transaction uses R[ ]
• Can the following transactions run into a deadlock ?
∙ TA1: r1[x], w1[x], c1
∙ TA2: R2[x], w2[x], c2
• We have to address all possible timings (either by 
individual testing or by argument)
• First timing
∙ TA1: r1[x], w1[x], c1
∙ TA2: R2[x] , w2[x], c2
• second timing
∙ TA1: r1[x], w1[x], c1
∙ TA2: R2[x] , w2[x], c2
• And so on…..
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Only  one transaction us es  R[  ]
•   Can the following transactions r un i  nto a deadlock                                                    ?
             ∙   TA1:   r    1[x   ],          w1[x   ],    c1
             ∙   TA2:   R     2[x   ],      w2[x   ],    c2
•   We have to address al  l possible timings (either by
    individual testing or by argument)
•   F irst timing
             ∙   TA1:   r    1[x   ],                                               w1[x   ],    c1
             ∙   TA2:              R   2[x   ] ,    w2[x   ],    c2
•   second timing
             ∙   TA1:   r    1[x   ],                       w1[x   ],                              c1
             ∙   TA2:              R   2[x   ] ,                       w2[x   ],    c2
•   And so on…..
 35   1/ 7   51                         Geral  d Webe r's  TA Ma nag ement   Slid es                                         14
````

### 图片文字 OCR（en-US，待对照原页）

````text
Only one transaction uses RI ]
Can the following transactions run into a deadlock ?
, TAI: rl[x],
, TA2: R2[x], W2[x],
We have to address all possible timings (either by
individual testing or by argument)
First timing
, TAI: rl[x],
, TA2:
second timing
, TAI: rl[x],
TA2:
And so on.....
351/751
W2[x] C
2
R2[x] ,
Gerald Weber's TA Management Slides
14
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../source/751%2525/DB51_2025_Deadlocks.pdf#page=15)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 15
Only one transaction uses R[ ]
• Can the following transactions run into a deadlock ?
∙ TA1: r1[x], w1[x], c1
∙ TA2: R2[x], w2[x], c2
• No. We have to address all possible timings (either by 
individual testing or by argument)
• First relevant timing: TA2 can only access x after c1
∙ TA1: r1[x], w1[x], c1
∙ TA2: R2[x] , w2[x], c2
• Second relevant timing: TA1 can only access x after c2
∙ TA1: r1[x], w1[x], c1
∙ TA2: R2[x] , w2[x], c2
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Only  one transaction us es  R[  ]
•  Can the following transactions r un i  nto a deadlock                                              ?
            ∙   TA1:   r   1[x   ],          w1[x   ],    c1
            ∙   TA2:   R    2[x   ],      w2[x   ],    c2
•  No . We have to addr ess al  l possible timings ( either by
   individual testing or by argument)
•  F irst relevant timing: T A2 can only access x after c                                           1
            ∙   TA1:   r   1[x   ],                                  w1[x   ],    c1
            ∙   TA2:               R 2[x   ] ,               w2[x   ],    c2
•  Second r elevant tim ing: T A1 can only access x after                                               c2
            ∙   TA1:                   r1[x   ],      w1[x   ],      c1
            ∙   TA2:    R    2[x   ] ,                           w2[x   ],    c2
 35   1/ 7   51                       Geral  d Webe r's  TA Ma nag ement   Slid es                                   15
````

### 图片文字 OCR（en-US，待对照原页）

````text
Only one transaction uses RI ]
Can the following transactions run into a deadlock ?
, TAI: rl[x],
, TA2: R2[x], W2[x],
No. We have to address all possible timings (either by
individual testing or by argument)
First relevant timing: TA2 can only access x after Cl
, TAI: rl[x],
, TA2:
WI [x], Cl
R2[x], W2[x],
Second relevant timing: TAI can only access x after
, TAI:
, TA2: R2[x]
351/751
G [X], Wl[x], Cl
Gerald Weber's TA Management Slides
15
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../source/751%2525/DB51_2025_Deadlocks.pdf#page=16)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 16
Only one transaction uses R[ ]
• Can the following transactions run into a deadlock ?
∙ TA1: r1[x], w1[x], c1
∙ TA2: R2[x], w2[x], c2
• No. We have to address all possible timings (either by 
individual testing or by argument)
• First s1: r1[x], w1[x], c1, R2[x] , w2[x], c2
∙ TA1: r1[x], w1[x], c1
∙ TA2: R2[x]______________ , w2[x], c2
 2nd s2: R2[x] , w2[x], c2, r1[x], w1[x], c1
∙ TA1: r1[x]______________, w1[x], c1
∙ TA2: R2[x] , w2[x], c2
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Only  one transaction us es  R[  ]
•   Can the following transactions r un i  nto a deadlock                                                           ?
              ∙   TA1:   r     1[x   ],          w1[x   ],    c1
              ∙   TA2:   R      2[x   ],      w2[x   ],    c2
•   No . We have to addr ess al  l possible timings ( either by
    individual testing or by argument)
•   F irst    s1:              r1[x   ],                                  w1[x   ],    c1, R2[x   ] ,               w2[x   ],    c2
              ∙   TA1:   r     1[x   ],                                  w1[x   ],    c1
              ∙   TA2:               R     2[x ]______________ ,        w                   2[x   ],    c2
      2nd   s2:                R2[x   ] ,                           w2[x   ],    c2, r1[x   ],           w1[x   ],      c1
              ∙   TA1:                   r  1[x ]______________,    w                     1[x   ],      c1
              ∙   TA2:    R      2[x   ] ,                           w2[x   ],    c2
 35   1/ 7   51                            Geral  d Webe r's  TA Ma nag ement   Slid es                                              16
````

### 图片文字 OCR（en-US，待对照原页）

````text
Only one transaction uses RI ]
Can the following transactions run into a deadlock ?
, TAI: rl[x],
, TA2: R2[x], W2[x],
No. We have to address all possible timings (either by
individual testing or by argument)
, First
2nd
351/751
sl:
, TAI:
, TA2:
s2:
, TAI:
TA2:
Wl[x], Cl
WI [x], Cl
R2[x] ,
rl[X],
R2[x]
R2[x] ,
R2[x]
W2[x],
Wl[x], Cl
WI [x], Cl
Gerald Weber's TA Management Slides
16
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../source/751%2525/DB51_2025_Deadlocks.pdf#page=17)

### 原始文字层

````text
Summary 
• Conflicts lead to the precedence graph: 
• conflicts seen as directed edges between transactions.
• Circles in the precedence graph including blocked 
operations express deadlocks
• Shared reads are prone to deadlocks wtithouy precautions.
• Certain deadlocks can be prevented with R[ ].
351/751 Gerald Weber's TA Management Slides 17
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Summary
• Conflicts lead to the precedence graph:
• conflicts seen as di  rected edges between transacti  ons.
• Circles in the precedence graph including                 blocked
  operations express deadlocks
• Shared r eads are prone to deadlocks wtithouy precautions.
• Certai  n  deadl  ocks can be prevented with R  [ ].
35   1/ 7   51            Geral  d Webe r's  TA Ma nag ement   Slid es            17
````

### 图片文字 OCR（en-US，待对照原页）

````text
Summary
Conflicts lead to the precedence graph:
conflicts seen as directed edges between transactions.
Circles in the precedence graph including blocked
operations express deadlocks
Shared reads are prone to deadlocks wtithouy precautions.
Certain deadlocks can be prevented with R[ ].
351/751
Gerald Weber's TA Management Slides
17
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

