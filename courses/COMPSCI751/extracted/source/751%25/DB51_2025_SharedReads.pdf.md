# DB51_2025_SharedReads.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI751/source/751%25/DB51_2025_SharedReads.pdf`
- [打开原文件](../../../source/751%2525/DB51_2025_SharedReads.pdf)
- 原文件 SHA-256：`88613017e208efd3f11c950bba9669e31273523afe1d716352923a3ee66a5f11`
- 文件索引：F162；PDF 总页数：26
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=1)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 1
351/751
• Shared Read locks
∘ Conflicts
∘ Scheduling based on operations performed
∘ The common scheduler
∘ Shared vs exclusive locks
∘ Upgrade locks
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
351/751
 •  Shared Read locks
      ∘ Conflicts
      ∘ Scheduling based on operations performed
      ∘ T he common scheduler
      ∘ Shared vs exclusive locks
      ∘ Upgrade locks
 35   1/ 7   51              Geral d Weber's TA Management  Slides               1
````

### 图片文字 OCR（en-US，待对照原页）

````text
351/751
Shared Read locks
0 Conflicts
o Scheduling based on operations performed
o The common scheduler
o Shared vs exclusive locks
Upgrade locks
351/751
Gerald Weber's TA Management Slides
1
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=2)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 2
Conflicts in a schedule
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
Confl icts  i n a sc hedul e
• Conflicts are a concept to capture the pairwise relationship
  of operati  ons ( and by extension transactions) accessing the
  same     object i  n a schedule.
• Each operation w  riting an object has one conflict with each
  operation by a different tr ansaction accessing this object.
  We write these conflicts for           object x:
    r1[x], r2[x], c2, w1[x], c1, r3[x], w3[x], c3
• As ordered pairs of operations:
• r2[x], w1[x],    and w1[x],     r3[x], and also w1[x], w3[x],
• r1[x], w3[x],    and r2[x],    w3[x].
• Idea: order in which tr ansactions commit shoul  d be
  compatible with thi  s order.
35   1/ 7   51              Geral d Weber's TA Management  Slides                  2
````

### 图片文字 OCR（en-US，待对照原页）

````text
Conflicts in a schedule
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
2
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=3)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides
Conflict-free Transactions
• A set of transactions is conflict-free, if 
it has no conflicts.
• Note that this is independent of the 
scheduling of the transactions.
• Note also that the transactions can 
still have shared objects and
hence may not be disjoint-access.
• Intuition:
• Shared objects are from the view of 
these transactions constant:
• A set of conflict-free transactions 
should not be delayed either.
k
y
x
z
w2
r1 w1
r2
write access by 1
read access by both
r1
r1
3
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Confl ict-free Transactions
• A set of transactions is conflict-fr ee, if
  it has no confl  icts.
• Note that thi  s i  s i  ndependent of the                 r  k
                                                              2   r1           x
  schedul  ing of the transactions.                                        w2
• Note al  so that the transactions can
  still have shared objects and
  hence may not be disj  oi  nt-access.
• Intui  ti  on:                                                               r1
• Shared objects are from the view of                            r   z       y
                                                                  1            w1
  these transactions constant:
• A set of conflict-free transactions                          write access by 1
  should not be delayed either.                         read access by both
 35   1/ 7   51              Geral d Weber's TA Management  Slides                  3
````

### 图片文字 OCR（en-US，待对照原页）

````text
Conflict-free Transactions
A set of transactions is conflict-free, if
it has no conflicts.
Note that this is independent of the
scheduling of the transactions.
Note also that the transactions can
still have shared objects and
hence may not be disjoint-access.
Intuition:
• Shared objects are from the view of
these transactions constant:
A set of conflict-free transactions
should not be delayed either.
z
write access by 1
read access by both
351/751
Gerald Weber's TA Management Slides
3
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=4)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 4
The simple scheduler is pessimistic
• The simple scheduler expects for every read, that it might 
be followed by a write:
• s: r1[x], r1[y], w1[x], c1,r2[x],w2[x],c2,r3[x],w3[z],c3
• TA1: r1[x], r1[y], w1[x], c1
• TA2: r2[x] _______________, w2[x],c2
• TA3: r3[x]________________________, w3[z], c3
transactions TA2 and TA3 waiting, although no conflict yet.
Oh, good that TA2 was waiting
Transaction TA3 waited, although it was not necessary!
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
The simple scheduler is pessi misti c
• T he simple scheduler expects for every r ead, that it mi  ght
  be foll  ow  ed by a w  rite:
•   s:     r1[x],       r1[y], w1[x], c1,r2[x],w2[x],c2,r3[x],w3[z],c3
• T A1: r1[x],         r1[y], w1[x], c1
• TA2:         r2[x] _______________, w2[x],c2
• TA3:            r3[x]________________________, w3[z], c3
   transact ions  TA2 and T A3  waiting, alt hough no conflic t y et.
                  Oh, good that  TA2 was  waiting
   Transact ion  TA3 wait ed,  although  it w as  not neces sary!
35   1/ 7   51                Geral d Weber's TA Management  Slides                      4
````

### 图片文字 OCR（en-US，待对照原页）

````text
The simple scheduler is pessimistic
The simple scheduler expects for every read, that it might
be followed by a write:
, TAI: rl[x],
, TA2:
, TA3:
W3[z],
transactions TA2 and TA3Waiting, although no conflict yet:
Oh, good that TA2 was waiting
Transaction TA3 waited, although it was not necessary!
351/751
Gerald Weber's TA Management Slides
4
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=5)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 5
Info for transaction scheduling
• Keep a record of which open
transaction accessed (or tried to do so) 
which object with which operation. Tag 
object with:
• The operation performed (r, w)
• The transaction ID (the index)
• Scheduling strategies can be seen as 
deciding access based on the tags on 
x, whether a next operation on x can 
proceed or needs to be blocked in 
order to avoid harm.
• Blocked operations with dotted lines
k
y
z
x
r1
r2
w2
w1
r2
write access by 1
Stack all operations 
on object in temporal
order
r2
w2
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Info for  transaction scheduli ng                       Stack all operations
• Keep a record of which open                            on object in temporal
  transaction accessed (or tried to do so)                         order
  which object wi  th which operation. T ag               r  k
  object w  ith:                                           2         w2   x
r   •  T he operation performed (r, w  )                               r2
2
    •  T he transaction ID   (the i  ndex)
• Scheduling strategi  es can be seen as
  deciding access based on the tags on                      r  z         y
  x, whether a next operati  on on x can                     1             w
                                                               w2            1
  proceed or needs to be blocked in
  order to avoid harm.                                      write access by 1
• Bl  ocked operations w  ith dotted lines
 35   1/ 7   51             Geral d Weber's TA Management  Slides               5
````

### 图片文字 OCR（en-US，待对照原页）

````text
Info for transaction scheduling
Keep a record of which open
transaction accessed (or tried to do so)
which object with which operation. Tag
object with:
The operation performed (r, w)
The transaction ID (the index)
Scheduling strategies can be seen as
deciding access based on the tags on
x, whether a next operation on x can
proceed or needs to be blocked in
order to avoid harm.
Blocked operations with dotted lines
Stack all operations
on object in temporal
order
z
write access by 1
351/751
Gerald Weber's TA Management Slides
5
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=6)

### 原始文字层

````text
k
z y
351/751 Gerald Weber's TA Management Slides 6
r2
r1
w1
r2
Reasoning over open transactions
• Extend definitions to open transactions 
as follows:
• The current set of partially executed 
open transactions:
• All operations from all open transactions 
already executed at this point in time, 
NOT including any currently blocked 
operations.
• Note, if they would all commit at this 
stage they would form a set of 
transactions as we already discussed it.
x
r2
w2
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Reas oning ov er open transacti ons
• Extend definitions to open transactions
  as fol  lows:
• T he current set of partially executed                     r  k
                                                              2          w2   x
  open    tr ansactions:                                                   r2
• Al  l operati  ons from all open transactions
  already executed at this point i  n time,
  NOT  i  ncl  uding any currently blocked
  operations.                                                    r1  z       y
• Note, i  f they woul  d all commi  t at thi  s                  r2           w1
  stage they woul  d      form a set of
  transactions as we already discussed i  t.
 35   1/ 7   51              Geral d Weber's TA Management  Slides                  6
````

### 图片文字 OCR（en-US，待对照原页）

````text
Reasoning over open transactions
Extend definitions to open transactions
as follows:
The current set of partially executed
open transactions:
All operations from all open transactions
already executed at this point in time,
NOT including any currently blocked
operations.
Note, if they would all commit at this
stage they would form a set of
transactions as we already discussed it.
351/751
Gerald Weber's TA Management Slides
6
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=7)

### 原始文字层

````text
k
z y
351/751 Gerald Weber's TA Management Slides 7
r2
r1
w1
r2
Declarative definition of schedulers
• Consider the current set of partially 
executed open transactions for each 
moment in time.
• Simple scheduler: Block any operation 
that would cause this set to be not 
disjoint-access any more.
• New scheduler:
• Common scheduler: Block any 
operation that would cause this set to 
be not conflict-free any more.
x
r2
w2
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Declarativ e defi ni tion of schedul ers
• Consider     the current set of partially
  executed open transactions           for each
  moment in time.                                         r  k
                                                           2         w2   x
• Si m  pl e schedul  er: Block any operation                          r2
  that would cause this set to be not
  disjoint-access any more.
• New schedul  er:
• Comm on schedul  er: Block any                              r1  z      y
  operation    that would cause       this set to              r2          w1
  be not conflict-free any more.
 35   1/ 7   51             Geral d Weber's TA Management  Slides               7
````

### 图片文字 OCR（en-US，待对照原页）

````text
Declarative definition of schedulers
Consider the current set of partially
executed open transactions for each
moment in time.
Simple scheduler: Block any operation
that would cause this set to be not
disjoint-access any more.
New scheduler:
Common scheduler: Block any
operation that would cause this set to
be not conflict-free any more.
351/751
Gerald Weber's TA Management Slides
7
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=8)

### 原始文字层

````text
k
z y
351/751 Gerald Weber's TA Management Slides 8
r2
r1
w1
r2
Declarative definition of schedulers
• Consider the current set of partially 
executed open transactions for 
each moment in time.
• Simple scheduler: Block any operation 
that would cause this set to have a 
shared object.
• Common scheduler: Block any 
operation that would cause this set to 
have a conflict.
• Can all operations on the right pass in 
common scheduler?
x
r2
w2
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Declarativ e defi ni tion of schedul ers
• Consider     the current set of partially
  executed open transactions           for
  each   moment in time.                                  r  k
                                                           2          w2  x
• Si m  pl e schedul  er: Block any operation                           r2
  that would cause this        set to have a
  shar ed object.
• Comm on  schedul  er: Block any
  operation that would cause thi  s set          to           r1  z       y
  have a con flict.                                             r2          w1
• Can all operations on the right pass in
  common scheduler?
 35   1/ 7   51             Geral d Weber's TA Management  Slides                8
````

### 图片文字 OCR（en-US，待对照原页）

````text
Declarative definition of schedulers
Consider the current set of partially
executed open transactions for
each moment in time.
Simple scheduler: Block any operation
that would cause this set to have a
shared object
Common scheduler: Block any
operation that would cause this set to
have a conflict
Can all operations on the right pass in
common scheduler?
351/751
Gerald Weber's TA Management Slides
8
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=9)

### 原始文字层

````text
k
z y
351/751 Gerald Weber's TA Management Slides 9
r2
r1
w1
r2
Declarative definition of schedulers
• Consider the current set of partially 
executed open transactions for 
each moment in time.
• Simple scheduler: Block any operation 
that would cause this set to have a 
shared object.
• Common scheduler: Block any 
operation that would cause this set to 
have a conflict.
• Can all operations on the right pass in 
common scheduler?
x
r2
w2
Only in common
scheduler
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Declarativ e defi ni tion of schedul ers
• Consider     the current set of partially
  executed open transactions           for
  each   moment in time.                                  r  k
                                                           2         w2   x
• Si m  pl e schedul  er: Block any operation                          r2
  that would cause this        set to have a
  shar ed object.
• Comm on  schedul  er: Block any
  operation that would cause thi  s set         to            r1  z      y
  have a con flict.                                            r2          w1
• Can all operations on the right pass in
  common scheduler?                                    Only in common
                                                       schedul  er
 35   1/ 7   51             Geral d Weber's TA Management  Slides               9
````

### 图片文字 OCR（en-US，待对照原页）

````text
Declarative definition of schedulers
Consider the current set of partially
executed open transactions for
each moment in time.
Simple scheduler: Block any operation
that would cause this set to have a
shared object
Common scheduler: Block any
operation that would cause this set to
have a conflict
Can all operations on the right pass in
common scheduler?
Only in common
scheduler
351/751
Gerald Weber's TA Management Slides
9
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=10)

### 原始文字层

````text
k
y
x
z
351/751 Gerald Weber's TA Management Slides 10
r1
r2
r2
r1
w1
r2
Operation tags are natural 
• Schedulers are usually defined directly 
with locks instead of our tags.
• Advantage of declarative definition with 
tags:
• We do not say how and when to place 
and remove locks (imperative)
• We say what should be allowed: all 
operations of ongoing transactions 
(declarative).
• An observable concept
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Operati on tags are natur al
• Schedulers ar e usually          defined directl  y
  with locks instead of our          tags.
• Advantage of        declarative     definition wi  th       r  k
                                                               2        x
  tags:                                                              r2 r
                                                                          1
• We  d o  not say how and w  hen to place
  and remove locks (imperati  ve)
• We say what should be allowed: all
  operations of ongoi  ng transactions                            r1  z       y
  (decl  arative).                                                 r2           w1
• An observable concept
 35   1/ 7   51               Geral d Weber's TA Management  Slides                 10
````

### 图片文字 OCR（en-US，待对照原页）

````text
Operation tags are natural
Schedulers are usually defined directly
with locks instead of our tags.
Advantage of declarative definition with
tags:
We do not
say how and when to place
and remove locks (imperative)
We say what should be allowed: all
operations of ongoing transactions
(declarative).
An observable concept
351/751
Gerald Weber's TA Management Slides
10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=11)

### 原始文字层

````text
k
y
x
z
351/751 Gerald Weber's TA Management Slides 11
r1
r2
r1
r2
Declarative definition of schedulers
• Common scheduler: Block 
any operation that would cause the 
current set of partially executed open 
transactions to have a conflict.
• Example:
• Under this rule: is w2 on the right 
blocked?
w1
w2
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Declarativ e defi ni tion of schedul ers
• Co mm on      schedul  er: Block
  any   operation that would cause           the
  current set of partially executed open                    r  k
                                                             2        x
  transactions      to have a    conflict.                         w2  r
                                                                        1
• Example:
• Under this r ul  e: is w2 on the r ight
  blocked?
                                                                r1   z      y
                                                                  r2          w1
 35   1/ 7   51              Geral d Weber's TA Management  Slides                11
````

### 图片文字 OCR（en-US，待对照原页）

````text
Declarative definition of schedulers
Common scheduler:
Block
any operation that would cause the
current set of partially executed open
transactions to have a conflict
Example:
Under this rule: is on the right
1
blocked?
351/751
Gerald Weber's TA Management Slides
11
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=12)

### 原始文字层

````text
k
y
x
z
351/751 Gerald Weber's TA Management Slides 12
r1
w2
r2
r1
r2
Declarative definition of schedulers
• Common scheduler: Block any 
operation that would cause the current 
set of partially executed 
open transactions to have a conflict.
• Example:
• Under this rule: is w2 on the right 
blocked? Yes!
• (We will depict blocked operations with 
dotted outlines). 
• After a transaction finishes: some 
blocked transactions may continue.
w1
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Declarativ e defi ni tion of schedul ers
• Co mm on       schedul  er: Block any
  operation that would cause            the   current
  set of partiall  y executed                                r  k
                                                              2         x
  open    tr ansactions     to have a    con flict.                 w2  r
                                                                         1
• Example:
• Under this r ul  e: is w2 on the r ight
  blocked?                                  Yes!
• (We will depict blocked operations wi  th                      r1   z      y
  dotted outl  ines).                                              r2           w1
• After a transaction fi  ni  shes: some
  blocked transactions may continue.
 35   1/ 7   51              Geral d Weber's TA Management  Slides                  12
````

### 图片文字 OCR（en-US，待对照原页）

````text
Declarative definition of schedulers
Common scheduler: Block any
operation that would cause the current
set of partially executed
open transactions to have a conflict
Example:
Under this rule: is on the right
-x
1
blocked?
Yes!
(We will depict blocked operations with
dotted outlines).
After a transaction finishes: some
blocked transactions may continue.
351/751
Gerald Weber's TA Management Slides
12
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=13)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 13
The common scheduler with upgrade locks
• Akin to schedulers used in practice.
• uses several kinds of locks:
∘ read locks, also known as shared locks (S locks)
∙ Several transactions can have a read lock on the same object:
∙ an object with read locks can only be read, not written.
∙ Advantage: conflict-free transactions are not delayed.
∘ write locks, also known as exclusive locks (X locks)
∙ If an object has a write lock on x, no other lock can be set on x.
∙ The owner can read and write the object.
∙ A lone read lock on x can be upgraded to a write lock by owner.
∘ upgrade locks (a.k.a. update locks , U locks)
∙ Help in acquiring write locks in certain conditions
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
The c ommon s cheduler with upgrade locks
•  Aki  n to schedulers used in practice.
•  uses several kinds of locks:
     ∘  read locks, also known as shared l  ocks ( S locks)
          ∙  Several transact ions  can have a  read lock  on the s ame objec t:
          ∙  an object  with read lock s c an  only  be read,  not w rit ten.
          ∙  Advantage:      con fl ict -free tran sactio ns are n ot d el ayed         .
     ∘  write locks, also known as exclusive locks (X   l  ocks)
          ∙  If  an object  has  a writ e  lock  on  x,  no  ot her  loc k c an  be  set  on  x.
          ∙  The ow ner c an  read and w rit e the object.
          ∙  A lone read  lock  on  x c an  be      upgraded to  a  write loc k by  owner.
     ∘   upgrade       locks    (a.k.a. update locks             , U locks)
          ∙  Help in  ac quiring w rit e locks  in c ert ain  condit ions
35   1/ 7   51                   Geral d Weber's TA Management  Slides                          13
````

### 图片文字 OCR（en-US，待对照原页）

````text
The common scheduler with upgrade locks
Akin to schedulers used in practice.
uses several kinds of locks:
o read locks, also known as shared locks (S locks)
Several transactions can have a read lock on the same object:
• an object with read locks can only be read, not written.
• Advantage: conflict-free transactions are not delayed.
o write locks, also known as exclusive locks (X locks)
If an object has a write lock on x, no other lock can be set on x.
The owner can read and write the object.
A lone read lock on x can be upgraded to a write lock by owner.
o upgrade locks (a.k.a. update locks , U locks)
351/751
Help in acquiring write locks in certain conditions
Gerald Weber's TA Management Slides
13
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=14)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 14
Scheduling with shared locks
• s: r1[x], r2[x], c2,r1[y], r3[z], w1[y], c1,w3[x], c3
• TA1: r1[x], r1[y], w1[y], c1 
• TA2: r2[x], c2
• TA3: r3[z], w3[x] ___________, c3,
transaction TA2 not waiting any more.
transaction TA3 is waiting, cannot acquire write lock
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Scheduli ng with s hared l ocks
•    s:    r1[x], r2[x], c2,r1[y], r3[z], w1[y],          c1,w3[x], c3
•  T A1: r1[x],             r1[y],          w1[y],          c1
•  T A2:         r2[x], c2
•  T A3:                              r3[z], w3[x] ___________, c3,
transact ion TA2  not  waiting any  more.
                   transact ion TA3  is w ait ing,  cannot ac quire w rit e lock
35   1/ 7   51                    Geral d Weber's TA Management  Slides                           14
````

### 图片文字 OCR（en-US，待对照原页）

````text
Scheduling with shared locks
s: rl[x], r2[x], r3[z], WI
, TAI: rl[x],
TA2:
, TA3:
Cl
r2[x],
r3[z], W3[x]
transaction TA2 not waiting any more.
351/751
transaction TA3 is waiting, cannot acquire write lock
Gerald Weber's TA Management Slides
14
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=15)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 15
Problem with read and write locks:
• As long as several transactions have a read lock on the 
same object, a write lock cannot be acquired. Writing 
transactions have to wait.
• Without further precautions, a writing transaction might 
never be able to acquire the write lock, because new 
transactions continuously start to read: the writing 
transaction would be in a live-lock (a form of starvation):
∘ s: r1[x], r2[x], r3[x], c2, r4[x], r5[x], c3, c4, r6[x],.....
∘ TA1: r1[x], w1[x] _____________________?
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Probl em wi th read and wri te lock s:
• As long as several transacti  ons have a r ead lock on the
  same object, a write lock cannot be acqui  red. Wri  ti  ng
  tr ansactions have to w  ai  t.
• Without further precautions, a writing transaction mi  ght
  never be able to acquire the write l  ock, because new
  tr ansactions continuously start to r ead: the writing
  tr ansaction woul  d be in a          live -lock   (a form of    starvation     ):
    ∘   s:      r1[x], r2[x], r3[x], c2, r4[x], r5[x], c3, c4, r6[x],.....
    ∘  T A1:  r1[x],        w1[x] _____________________?
35   1/ 7   51                Geral d Weber's TA Management  Slides                    15
````

### 图片文字 OCR（en-US，待对照原页）

````text
Problem with read and write locks:
As long as several transactions have a read lock on the
same object, a write lock cannot be acquired. Writing
transactions have to wait.
Without further precautions, a writing transaction might
never be able to acquire the write lock, because new
transactions continuously start to read: the writing
transaction would be in a live-lock (a form of starvation)
rl r2[x], r3[x], r4[x], r5[x], Q, r6[x],.
0 T A1: %
351/751
Gerald Weber's TA Management Slides
15
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=16)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 16
Solution: upgrade locks
• The first writing transaction gets the third type of lock, the 
upgrade lock (U lock):
∘ No new reader can access this object, before the write 
was de-queued and executed.
∘ Once all readers have finished, the writing transaction 
gets the exclusive lock:
∘ s: r1[x], r2[x], r3[x], c2, c3, w1[x], c1,r4[x],.....
∘ TA1: r1[x], w1[x] ____________,c1
∘ TA4: r4[x] _____________, .....
transaction TA4 is waiting, cannot acquire read lock
transaction TA1 waiting, but acquires U lock.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Sol uti on: upgrade lock s
• T he first w  riting transaction gets the third type of lock, the
  upgrade lock (U lock):
    ∘  No new reader can access this obj  ect, before the write
       was de-queued and executed.
    ∘  Once all   readers have finished, the writing transaction
       gets the exclusive l  ock:
    ∘   s:      r1[x], r2[x], r3[x], c2,           c3, w1[x], c1,r4[x],.....
    ∘  TA1:     r1[x],            w1[x] ____________,c1
    ∘  TA4:                                 r4[x] _____________, .....
transact ion TA1  waiting, but  acquires  U  loc k.
                transact ion TA4  is w ait ing,  cannot ac quire read lock
35   1/ 7   51                Geral d Weber's TA Management  Slides                   16
````

### 图片文字 OCR（en-US，待对照原页）

````text
Solution: upgrade locks
The first writing transaction gets the third type of lock, the
upgrade lock (U lock):
o No new reader can access this object, before the write
was de-queued and executed.
o Once all readers have finished, the writing transaction
gets the exclusive lock:
rl r2[x], r3[x],
o TAI: rl[x],
o TA4:
transaction TAI waiting, but acquires U lock.
351/751
transaction TA4 is waiting, cannot acquire read lock
Gerald Weber's TA Management Slides
16
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=17)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 17
Locks can be computed from current ops
• All three locks can be computed 
from the list of operations present 
at the object.
• In principle no locks as separate 
datastructure necessary.
• Still locks can be a helpful way to 
talk about current access to 
objects. 
k
y
x
z
r1
r2
r2
r2
w1
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Loc ks c an be computed from current ops
   •  Al  l three l  ocks can be computed
      fr om the li  st of operations present                      k
      at the object.                                           r2         x
                                                                       r2 r
                                                                           1
   •  In principle no l  ocks as separate
      datastr ucture necessary.
                                                                        z       y
   •  Stil  l locks can be a helpful   w  ay to                      r2           w1
      talk about current access to
      objects.
35   1/ 7   51                Geral d Weber's TA Management  Slides                    17
````

### 图片文字 OCR（en-US，待对照原页）

````text
Locks can be computed from current ops
All three locks can be computed
from the list of operations present
at the object.
In principle no locks as separate
datastructure necessary.
Still locks can be a helpful way to
talk about current access to
objects.
351/751
Gerald Weber's TA Management Slides
17
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 18 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=18)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 18
Locks can be computed from current ops
• All three locks can be computed 
from the list of operations present 
at the object.
• In principle no locks as separate 
datastructure necessary.
• Still locks can be a helpful way to 
talk about current access to 
objects. 
k
y
x
z
r1
r2
r2
r1
r2
w1
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Loc ks c an be computed from current ops
   •  Al  l three l  ocks can be computed
      fr om the li  st of operations present                      k
      at the object.                                           r2         x
                                                                       r2 r
                                                                           1
   •  In principle no l  ocks as separate
      datastr ucture necessary.
                                                                   r1   z       y
   •  Stil  l locks can be a helpful   w  ay to                      r2           w1
      talk about current access to
      objects.
35   1/ 7   51                Geral d Weber's TA Management  Slides                    18
````

### 图片文字 OCR（en-US，待对照原页）

````text
Locks can be computed from current ops
All three locks can be computed
from the list of operations present
at the object.
In principle no locks as separate
datastructure necessary.
Still locks can be a helpful way to
talk about current access to
objects.
351/751
Gerald Weber's TA Management Slides
18
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 19 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=19)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 19
Locks can be computed from current ops
• All three locks can be computed 
from the list of operations present 
at the object.
• In principle no locks as separate 
datastructure necessary.
• Still locks can be a helpful way to 
talk about current access to 
objects. 
k
y
x
z
r1
r2
r2
r1
r2
w1
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Loc ks c an be computed from current ops
   •  Al  l three l  ocks can be computed
      fr om the li  st of operations present                      k
      at the object.                                           r2         x
                                                                       r2 r
                                                                           1
   •  In principle no l  ocks as separate
      datastr ucture necessary.
                                                                   r1   z       y
   •  Stil  l locks can be a helpful   w  ay to                      r2           w1
      talk about current access to
      objects.
35   1/ 7   51                Geral d Weber's TA Management  Slides                    19
````

### 图片文字 OCR（en-US，待对照原页）

````text
Locks can be computed from current ops
All three locks can be computed
from the list of operations present
at the object.
In principle no locks as separate
datastructure necessary.
Still locks can be a helpful way to
talk about current access to
objects.
351/751
Gerald Weber's TA Management Slides
19
````

### 图表辅助说明

右侧数据库对象图把 r1、r2、w1 等操作贴在 k、x、y、z 对象旁：多个读操作可以共存，写操作需要不同的访问状态。该页强调锁状态可由对象当前操作集合计算，不一定要把锁理解为额外独立数据结构。

## PDF 第 20 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=20)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 20
Locks can be computed from current ops
• All three locks can be computed 
from the list of operations present 
at the object.
• In principle no locks as separate 
datastructure necessary.
• Still locks can be a helpful way to 
talk about current access to 
objects. 
k
y
x
z
r1
r2
r2
r1
r2
w2
w1
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Loc ks c an be computed from current ops
   •  Al  l three l  ocks can be computed
      fr om the li  st of operations present                      k
      at the object.                                           r2         x
                                                                       r2 r
                                                                           1
   •  In principle no l  ocks as separate
      datastr ucture necessary.
                                                                     w2
                                                                   r1   z       y
   •  Stil  l locks can be a helpful   w  ay to                      r2           w1
      talk about current access to
      objects.
35   1/ 7   51                Geral d Weber's TA Management  Slides                   20
````

### 图片文字 OCR（en-US，待对照原页）

````text
Locks can be computed from current ops
All three locks can be computed
from the list of operations present
at the object.
In principle no locks as separate
datastructure necessary.
Still locks can be a helpful way to
talk about current access to
objects.
351/751
Gerald Weber's TA Management Slides
20
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 21 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=21)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 21
Locks can be computed from current ops
• All three locks can be computed 
from the list of operations present 
at the object.
• In principle no locks as separate 
datastructure necessary.
• Still locks can be a helpful way to 
talk about current access to 
objects. 
k
y
x
z
r1
r2
r2
r1
r2
w2
w1
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Loc ks c an be computed from current ops
   •  Al  l three l  ocks can be computed
      fr om the li  st of operations present                      k
      at the object.                                           r2         x
                                                                       r2 r
                                                                           1
   •  In principle no l  ocks as separate
      datastr ucture necessary.
                                                                     w2
                                                                   r1   z       y
   •  Stil  l locks can be a helpful   w  ay to                      r2           w1
      talk about current access to
      objects.
35   1/ 7   51                Geral d Weber's TA Management  Slides                   21
````

### 图片文字 OCR（en-US，待对照原页）

````text
Locks can be computed from current ops
All three locks can be computed
from the list of operations present
at the object.
In principle no locks as separate
datastructure necessary.
Still locks can be a helpful way to
talk about current access to
objects.
351/751
Gerald Weber's TA Management Slides
21
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 22 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=22)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 22
Locks can be computed from current ops
• All three locks can be computed 
from the list of operations present 
at the object.
• In principle no locks as separate 
datastructure necessary.
• Still locks can be a helpful way to 
talk about current access to 
objects. 
k
y
x
z
r1
r2
r2
r1
r2
w2
r3
w1
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Loc ks c an be computed from current ops
   •  Al  l three l  ocks can be computed
      fr om the li  st of operations present                      k
      at the object.                                           r2         x
                                                                       r2 r
                                                                           1
   •  In principle no l  ocks as separate
      datastr ucture necessary.                                    r3
                                                                     w2
                                                                   r1   z       y
   •  Stil  l locks can be a helpful   w  ay to                      r2           w1
      talk about current access to
      objects.
35   1/ 7   51                Geral d Weber's TA Management  Slides                    22
````

### 图片文字 OCR（en-US，待对照原页）

````text
Locks can be computed from current ops
All three locks can be computed
from the list of operations present
at the object.
In principle no locks as separate
datastructure necessary.
Still locks can be a helpful way to
talk about current access to
objects.
351/751
Gerald Weber's TA Management Slides
22
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 23 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=23)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 23
Locks can be computed from current ops
• All three locks can be computed 
from the list of operations present 
at the object.
• In principle no locks as separate 
datastructure necessary.
• Still locks can be a helpful way to 
talk about current access to 
objects. 
k
y
x
z
r1
r2
r2
r1
r2
w2
r3
w1
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Loc ks c an be computed from current ops
   •  Al  l three l  ocks can be computed
      fr om the li  st of operations present                      k
      at the object.                                           r2         x
                                                                       r2 r
                                                                           1
   •  In principle no l  ocks as separate
      datastr ucture necessary.                                    r3
                                                                     w2
                                                                   r1   z       y
   •  Stil  l locks can be a helpful   w  ay to                      r2           w1
      talk about current access to
      objects.
35   1/ 7   51                Geral d Weber's TA Management  Slides                    23
````

### 图片文字 OCR（en-US，待对照原页）

````text
Locks can be computed from current ops
All three locks can be computed
from the list of operations present
at the object.
In principle no locks as separate
datastructure necessary.
Still locks can be a helpful way to
talk about current access to
objects.
351/751
Gerald Weber's TA Management Slides
23
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 24 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=24)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 24
Upgrade locks continued
• Only one transaction can acquire an U lock
• Later transactions that try to do so will be 
blocked
• Often expressed in a matrix:
∘ the columns denote the highest lock 
owned by another transaction that is 
already present at this object.
∘ the rows represent the lock that a 
transaction wants to acquire.
∘ Note: the view here is that a write 
requests both and U and X lock.
S U X
S y n n
U y n n
X n n n
y: lock granted and 
 transaction
 not blocked
n: lock not yet
granted
and transaction
blocked
lock requested
highest lock present
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Upgrade l oc ks c ontinued
                                                                        hi ghe st lo ck p resen t
• Only one transaction can acquire an U lock                                  S     U     X
• Later transactions that try to do so will be                           S    y     n     n
  blocked                                                                U    y     n     n
• Often expressed in a m atrix:                                          X    n     n     n
    ∘  the colum ns denote the highest lock
       owned by another transacti  on that                  is           y: l  ock gran  te  d and
       already present at this object.                                        transa cti on
                                                                              no t bl ocked
    ∘  the rows r epresent the l  ock that a
       tr ansaction wants to acquire.                                    n: lock no t yet
                                                                            gra nted
    ∘  Note: the view here is            that a write                       an d tra nsactio n
                                                                            bl ocked
       requests both and            U and X   lock.
35   1/ 7   51                 Geral d Weber's TA Management  Slides                      24
````

### 图片文字 OCR（en-US，待对照原页）

````text
Upgrade locks continued
Only one transaction can acquire an U lock
Later transactions that try to do so will be
blocked
Often expressed in a matrix:
o the columns denote the highest lock
owned by another transaction that is
already present at this object.
o the rows represent the lock that a
transaction wants to acquire.
o Note: the view here is that a write
requests both and U and X lock.
O
351/751
Gerald Weber's TA Management Slides
highest lock present
n
y: lock granted and
transaction
not blocked
n: lock not yet
granted
and transaction
blocked
24
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 25 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=25)

### 原始文字层

````text
351/751 TA management 25
ACID Isolation
• Database operations in a transaction appear isolated from 
database operations of all other transactions
∙ does not apply to non-database operations of scripts
• Isolation is expensive:
• May lead to delays, deadlocks, and/or aborts.
∘ and can therefore be relaxed: isolation levels.
• Highest isolation level:
• Transactions must have same view as with DB-wide MutEx.
• All committed transactions must have the same effect on 
the database as the execution of the transactions with 
Mutual exclusion in some order: Serializability.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
ACID   Isolat ion
• Database operations i n a tr ans actio n appear  iso lated fr om
  database operations o f all o ther  tr ans actio ns
         ∙  does not appl  y to non   -database  operati  ons of sc ripts
• Iso lation is  expensive:
• May lead to delays, deadlo cks , and/or  abo rts.
    ∘  and can ther efor e be rel axed:            is olatio n l evel s .
• Highes t i sol ati on level:
• Transactions must have same vi ew as  wi th DB                     -wide MutEx.
• Al l committed transacti ons must have the same ef fect on
  the database as the executi on of the tr ansacti ons with
  Mutual exclusi on in so me o rder: Seri al izabili ty.
351  /751                              TA man ag ement                                25
````

### 图片文字 OCR（en-US，待对照原页）

````text
ACID Isolation
Database operations in a transaction appear isolated from
database operations of all other transactions
does not apply to non-database operations of scripts
Isolation is expensive:
May lead to delays, deadlocks, and/or aborts.
0 and can therefore be relaxed: isolation /eve/s.
Highest isolation level:
Transactions must have same view as with DB-wide MutEx.
All committed transactions must have the same effect on
the database as the execution of the transactions with
Mutual exclusion in some order: Serializability.
351/751
TA management
25
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 26 页

[查看此页](../../../source/751%2525/DB51_2025_SharedReads.pdf#page=26)

### 原始文字层

````text
Summary
• Conflict-free transactions fulfil ACID isolation.
• The simple scheduler delays conflict-free transactions, is 
pessimistic.
• The common scheduler
∘ plausibly locks less often in practice than 
the simple scheduler
∘ needs a more elaborate locking protocol.
• Locks can be inferred from the operations present; only for 
upgrade locks we need to consider a blocked operation.
351/751 Gerald Weber's TA Management Slides 26
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Summary
• Conflict-free transactions fulfil   A CID isolation.
• T he simple scheduler delays con flict-free               tr ansactions, i  s
  pessimistic.
• T he common scheduler
    ∘  plausibly locks less often in practice than
       the  simple   schedul  er
    ∘  needs a m ore elaborate locking protocol.
• Locks can be inferred from the operations present; only for
  upgrade locks w  e need to consider a bl  ocked operation.
35   1/ 7   51              Geral d Weber's TA Management  Slides                26
````

### 图片文字 OCR（en-US，待对照原页）

````text
Summary
Conflict-free transactions fulfil ACID isolation.
The simple scheduler delays conflict-free transactions, is
pessimistic.
The common scheduler
o plausibly locks less often in practice than
the simple scheduler
o needs a more elaborate locking protocol.
Locks can be inferred from the operations present; only for
upgrade locks we need to consider a blocked operation.
351/751
Gerald Weber's TA Management Slides
26
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

