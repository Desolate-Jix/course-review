# DB51wk10gw3IsolationSimple.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI751/source/751%25/DB51wk10gw3IsolationSimple.pdf`
- [打开原文件](../../../source/751%2525/DB51wk10gw3IsolationSimple.pdf)
- 原文件 SHA-256：`1ba1fa280f08fc3a56f9263d2e76aed5612bdfe4132f8ceff6a3c14544f87531`
- 文件索引：F166；PDF 总页数：17
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../source/751%2525/DB51wk10gw3IsolationSimple.pdf#page=1)

### 原始文字层

````text
351/751
Gerald Weber
Transaction Processing
Motivation: isolation concepts for concurrency
351/751 TA management 1
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
35  1/7  51
                                       Gerald  Weber
                   Tran sac ti  on  Proc es sing
       M ot iv a ti on: is ol at io  n  co  nc  ep ts   for  co  nc  ur re ncy
 351  /751                              TA man ag ement                                     1
````

### 图片文字 OCR（en-US，待对照原页）

````text
351/751
Gerald Weber
Transaction Processing
Motivation: isolation concepts for concurrency
351/751
TA management
1
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../source/751%2525/DB51wk10gw3IsolationSimple.pdf#page=2)

### 原始文字层

````text
• An online multi-leg flight booking system (web or app).
• Users submit their orders and expect them to be:
• Processed as quickly as possible, also meaning that the 
user gets quick feedback on success/no success.
• Exactly as requested, in particularly complete:
• Book all legs of the flight, or do nothing.
• Problem Concurrency: different clients might interfere
• System checked that all legs were available
• but while booking: first flight ok, last flight is full.
 351/751 TA management 2
Example: Flight booking: Concurrency
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Exa mple:         Flight book ing: Concurrency
• An onl ine mul ti-leg fli ght booki ng sys tem (web or  app).
• User s submit their  or der s and expect them to be:
    •  Pro ces sed as  quickl y as  po ssi bl e, als o meani ng that the
       user  gets quick feedback on succes s/no s uccess .
    •  Exactl y as  reques ted, in par ti cul arly co mplete:
         •  Book al  l legs of the  flight, or  do nothi  ng.
• Problem Con currency: dif ferent cl ients  mi ght interfer e
         •  System checked that al l legs were available
         •  but whil e boo king: fir st fli ght ok, last fl ight is  full.
351  /751                             TA man ag ement                                2
````

### 图片文字 OCR（en-US，待对照原页）

````text
Example: Flight booking: Concurrency
An online multi-leg flight booking system (web or app).
Users submit their orders and expect them to be:
Processed as quickly as possible, also meaning that the
user gets quick feedback on success/no success.
Exactly as requested, in particularly complete:
Book all legs of the flight, or do nothing.
Problem Concurrency: different clients might interfere
System checked that all legs were available
but while booking: first flight 0k, last flight is full.
351/751
TA management
2
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../source/751%2525/DB51wk10gw3IsolationSimple.pdf#page=3)

### 原始文字层

````text
351/751 TA management 3
Disjoint-access parallelism (DAP) [e.g. Israeli et al 1994]
• Shared object: a data object accessed 
by more than one transaction in a set.
• A set of transactions is disjoint￾access, if it has no shared object.
• Disjoint-access transactions should 
not delay each other, ideal:
 Disjoint-access parallelism (DAP)
A. Israeli and L. Rappoport. Disjoint-access-parallel 
Implementations of Strong Shared Memory Primitives.In
PODC, pages 151–160, 1994.
k
y
x
z
w2
r1 w1
r2
write access by 1
read access by 2
r1
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Dis joint       -access  parall el is m (DAP                              )  [e.g. Israe  li et al 19   94]
•  Shared object: a data object accessed
   by more than one transaction in a set.
•  A set of transactions is disjoint                   -                   r   k
                                                                            2                     x
   access, i  f it has no shared object.                                                     w2
•  Disj  oi  nt -access       tr ansactions         should
   not delay each other, ideal:
        Disj  oi  nt -access parallelism (D  AP)                                                   r1
                                                                                 r    z        y
                                                                                  1               w1
    A. Israeli  and L.  Rappoport.  Disjoint-ac   ces   s-pa   ral l    el
    Im ple  men  tati   ons   of S tro  ng S ha  red    Mem ory   Primi tives.In
    PODC, pages 151–16   0,   1   994   .                                     write access by 1
                                                                           read access by 2
35   1/ 7   51                                 TA     m  ana   gem  ent                                  3
````

### 图片文字 OCR（en-US，待对照原页）

````text
Disjoint-access parallelism (DAP) [e.g. Israeli 1994]
Shared object: a data object accessed
by more than one transaction in a set.
A set of transactions is disjoint-
access, if it has no shared object.
Disjoint-access transactions should
not delay each other, ideal:
Disjoint-access parallelism (DAP)
A. Israeli and L. Rappoport. Disjoint-access-parallel
Implementations of Strong Shared Memory Primitives.ln
PODC, pages 151-160, 1994.
351/751
TA management
z
write access by 1
read access by 2
3
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../source/751%2525/DB51wk10gw3IsolationSimple.pdf#page=4)

### 原始文字层

````text
351/751 TA management 4
First Solution: simple scheduler [e.g. Ullmann 1980]
• Idea: 
• The simple scheduler uses MutEx per data object, aka one 
exclusive lock per object.
• When to set lock? 
• Scheduler knows only at the first access of x by TA1;
• So TA1 gets excl. lock on x with its first operation on x: 
• latest time allowed, first time possible (implicit OLTP).
• Release all locks held by one transaction at end of 
transaction (commit/abort time)
• If transactions wait in a cycle for each other to release locks: 
deadlock, abort one transaction in the cycle.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Fi rst Solution: s impl e s cheduler                        [e  .g. U llm ann   19  80]
• Idea:
• The simple scheduler uses MutEx per data object, aka one
  exclusive lock per obj  ect.
• When to set lock?
    •  Scheduler knows only at the first access of x by T A1;
• So T A1 gets excl. lock on x with its first operation on x:
    •  latest time allowed, first ti  me possible (implicit OLTP).
• Release al  l locks held by one transaction at end of
  tr ansaction (commi  t/abort time)
• If transacti  ons wait in a cycl  e for each other to r elease locks:
  deadl  ock, abort one transaction in the cycle.
35   1/ 7   51                      TA     m  ana   gem  ent                         4
````

### 图片文字 OCR（en-US，待对照原页）

````text
First Solution: simple scheduler [e.g. 1980]
Idea:
, The
simple scheduler
MutEx per data object
aka one
uses
exclusive lock per object.
When to set lock?
Scheduler knows only at the first access of x by TAI ;
So TAI gets excl. lock on x with its first operation on x:
latest time allowed, first time possible (implicit OLTP).
Release all locks held by one transaction at end of
transaction (commit/abort time)
If transactions wait in a cycle for each other to release locks:
deadlock, abort one transaction in the cycle.
351/751
TA management
4
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../source/751%2525/DB51wk10gw3IsolationSimple.pdf#page=5)

### 原始文字层

````text
351/751 TA management 5
Transactions wait for locks
For a scheduler:
• If a transaction TA1 makes any access to a locked object x 
and gets blocked: 
• The scheduler does not answer to TA1 for now:
• From the perspective of TA1, the call to access x simply 
takes long 
• TA1 does not have to care about scheduling
• best of all possible worlds, solve problem by doing 
nothing ☺
• Transaction scripts are typically strictly sequential: TA1, 
while blocked, cannot execute any other operation.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Transactions wai t for lock s
F or a scheduler:
• If a transaction TA  1 m akes any access to a                locked    object x
  and gets     blocked    :
• T he schedul  er does not answer to T A1 for now:
• F rom the perspective of T A1, the call to access x simply
  takes l  ong
    •  T A1 does not have to care about scheduling
    •  best of all possible w  orlds, solve problem by doi  ng
       nothi  ng ☺
• T ransaction scr ipts are typi  cal  ly strictly sequential: TA 1,
  while blocked, cannot execute any other operati  on.
35   1/ 7   51                     TA     m  ana   gem  ent                         5
````

### 图片文字 OCR（en-US，待对照原页）

````text
Transactions wait for locks
For a scheduler:
If a transaction TAI makes any access to a locked object x
and gets blocked:
The scheduler does not answer to TAI for now:
From the perspective of TAI , the call to access x simply
takes long
TAI does not have to care about scheduling
best of all possible worlds, solve problem by doing
nothing O
Transaction scripts are typically strictly sequential: TAI ,
while blocked, cannot execute any other operation.
351/751
TA management
5
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../source/751%2525/DB51wk10gw3IsolationSimple.pdf#page=6)

### 原始文字层

````text
351/751 TA management 6
Rigorous two-phase locking (R2PL)
• The simple scheduler as described uses:
• Rigorous two-phase locking (R2PL):
• transactions acquire locks during their 
lifetime (first phase).
• When should one transaction release 
any lock?
• We do not want to require further 
info from clients (implicit TP);
• we have only agreed on transaction demarcation:
• So release all locks at end of transaction.
Phase
 1
time
Phase 2
number
of
locks
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Rigorous           two-phase            l oc king (R2PL)
• T he simple scheduler  as descri  bed uses:                                        nu mber
• Rigor ous two       -phase locking ( R2PL):                           Pha  se      of
                                                                            1        lo  cks
• tr ansactions acquir e locks dur ing their
  lifetime ( first phase).
• When should one tr ansaction release                                 Pha se 2
  any lock?
                                                                   time
• We do not want to requir e fur ther
  info fr om cl  ients ( impl  icit TP) ;
• we have only agreed on tr ansaction dem arcation:
• So r elease all locks at end of tr ansaction.
 35   1/ 7   51                        TA     m  ana   gem  ent                            6
````

### 图片文字 OCR（en-US，待对照原页）

````text
Rigorous two-phase locking (R2PL)
The simple scheduler as described uses:
Rigorous two-phase locking (R2PL):
transactions acquire locks during their
lifetime (first phase).
When should one transaction release
any lock?
We do not want to require further
info from clients (implicit T P);
Phase
1
Phase 2
time
we have only agreed on transaction demarcation:
• So release all locks at end of transaction.
351/751
TA management
number
of
locks
6
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../source/751%2525/DB51wk10gw3IsolationSimple.pdf#page=7)

### 原始文字层

````text
351/751 TA management 7
Rigorous two-phase locking (R2PL)
• The simple scheduler as described uses:
• Rigorous two-phase locking (R2PL):
• transactions acquire locks during their 
lifetime (first phase).
• They release all locks immediately after 
commit/abort, but not earlier 
(second phase).
• R2PL used by most lock-based schedulers:
• No explicit lock commands necessary (only commit): no break 
of abstraction for the programmers writing transactions.
• R2PL avoids cascading aborts in case of errors.
Phase
 1
time
Phase 2
number
of
locks
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Rigorous           two-phase            l oc king (R2PL)
• T he simple scheduler  as descri  bed uses:                                       nu mber
• Rigor ous two       -phase locking ( R2PL):                          Pha  se      of
                                                                           1        lo  cks
• tr ansactions acquir e locks dur ing their
  lifetime ( first phase).
• T hey r elease all locks im mediately after                         Pha se 2
  com mit/abort, but not ear lier                                  time
  ( second phase) .
• R2PL used by m ost lock             -based schedulers:
• No explicit lock commands necessar y ( only commi  t) : no br eak
  of abstr acti  on for the pr ogrammer s writing tr ansactions.
• R2PL      avoids cascading abor ts in case of er r or s.
 35   1/ 7   51                        TA     m  ana   gem  ent                           7
````

### 图片文字 OCR（en-US，待对照原页）

````text
Rigorous two-phase locking (R2PL)
The simple scheduler as described uses:
Rigorous two-phase locking (R2PL):
transactions acquire locks during their
lifetime (first phase).
They release all locks immediately after
commit/abort, but not earlier
(second phase).
R2PL used by most lock-based schedulers:
number
of
locks
Phase
1
Phase 2
time
No explicit lock commands necessary (only commit): no break
of abstraction for the programmers writing transactions.
R2PL avoids cascading aborts in case of errors.
351/751
TA management
7
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../source/751%2525/DB51wk10gw3IsolationSimple.pdf#page=8)

### 原始文字层

````text
351/751 TA management 8
The current basic transaction model
∙ allows precise reasoning on transaction scheduling.
∙ elementary operations in transaction s:
∘ read on a data object: rs[x] - client gets the content
∘ write on a data object: ws[x] - client provides new 
content
∙ transaction demarcation:. 
∘ Begin of Transaction (BOTs) -
∙ mostly implicit: first operation starts transaction
∘ Commit: cs - successful end of transaction
∘ Abort: as - unsuccessful end of transaction
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
The c urr  ent basi c trans ac ti on model
∙ allows preci  se r easoning on tr ansaction scheduli  ng.
∙ elem entary operations in transaction s:
    ∘  read on a data object: rs[x]  - client gets the content
    ∘  write on a data object: ws[x] -  client provides new
       content
∙ tr ansaction demarcation:.
    ∘  Begin of T ransaction (B OTs) -
         ∙  most ly im plic it:  first  operation s tarts  transaction
    ∘  Commi  t: cs - successful   end of transaction
    ∘  Abort: as - unsuccessful end of transaction
35   1/ 7   51                       TA     m  ana   gem  ent                          8
````

### 图片文字 OCR（en-US，待对照原页）

````text
The current basic transaction model
allows precise reasoning on transaction scheduling.
elementary operations in transaction s:
read
on a data object: rs[x] - client gets the content
write on a data object: ws[x] - client provides new
content
transaction demarcation:.
o Begin of Transaction (BOTs) -
mostly implicit: first operation starts transaction
o Commit: cs - successful end of transaction
o Abort: as - unsuccessful end of transaction
351/751
TA management
8
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../source/751%2525/DB51wk10gw3IsolationSimple.pdf#page=9)

### 原始文字层

````text
CS 351, CS 751 TA management Slide Set 1 9
Linear schedules
∙ A (linear) schedule orders operations of a set of 
transactions in time. Good for discussing isolation issues.
∙ Example:
∘ Schedule 
s : r1[x], r2[x], r1[y], w1[x], r3[y], c3, w2[x], a2, c1
∘ Transaction 
TA1: r1[x], r1[y], w1[x], c1 (*)
∘ Lines do not cross: the schedule respects the local 
order in the transaction. (*) is called the local schedule 
of TA1.
∙ A transaction is a schedule.
(serializability)
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Linear s chedules
∙  A ( linear) schedule orders operations of a                     set of
   tr ansactions in time.  Good for discussing isolation i  ssues.
∙  Example:                                                       (serializability)
     ∘  Schedule
                    s : r1[x], r2[x], r1[y], w1[x], r3[y], c3, w2[x], a2, c1
     ∘  T ransaction
               T A1:   r1[x], r1[y], w1[x], c1                                      (*)
     ∘  Lines do not cross: the schedule r espects the local
        order in the transaction. ( *) is called the local schedule
        of TA1.
∙  A transaction is a schedule.
CS 351,  CS 751                   TA     m  ana   gem  ent      Sl i    de       Set      1  9
````

### 图片文字 OCR（en-US，待对照原页）

````text
Linear schedules
A (linear) schedule orders operations of a set of
transactions in time. Good for discussing isolation issues.
Example:
0 Schedule
(serializability)
S : rl [X], r2[x], rl [y], WI [X], r3[y], Q, W2[x], a2, Cl
0 Transaction
T A1: G r 1 WI Cl
o Lines do not cross: the schedule respects the local
order in the transaction. ( * ) is called the local schedule
of TAI .
A transaction is a schedule.
cs 351, cs 751
TA management Slide
Set 1
9
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../source/751%2525/DB51wk10gw3IsolationSimple.pdf#page=10)

### 原始文字层

````text
CS 351, CS 751 TA management Slide Set 1 10
Schedulers produce schedules
• Since schedulers cannot execute operations before they 
are issued by the clients, schedulers delay operations.
 s: r1[x], r1[y], r3[z], w1[x], c1, w2[x], c2,r3[x], c3
TA1: r1[x], r1[y], w1[x], c1 
TA2: w2[x] _______________________, c2
TA3: r3[z], r3[x] __________________, c3,
• The scheduling happens by waiting
• Local transactions are merged into a single schedule
transaction TA2 is waiting (aka blocked), w2[x] not yet executed
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Schedulers produce schedul es
• Si  nce schedul  ers cannot execute operations before they
  are issued by the clients, schedulers delay operati  ons.
      s:    r1[x], r1[y], r3[z], w1[x],            c1, w2[x], c2,r3[x], c3
    TA1: r1[x], r1[y],          w1[x],           c1
    TA2:      w2[x] _______________________, c2
    TA3:                  r3[z],    r3[x] __________________, c3,
    transact ion TA2  is w ait ing  (ak a blocked), w2[x ] not  yet  ex ecuted
• T he schedul  ing happens by waiting
• Local transacti  ons are m erged into a single schedul  e
CS 351,  CS 751                  TA     m  ana   gem  ent      Sl i    de       Set      110
````

### 图片文字 OCR（en-US，待对照原页）

````text
Schedulers produce schedules
Since schedulers cannot execute operations before they
are issued by the clients, schedulers delay operations.
s: q [x], q [y], r3[z], WI [x],
TAI : rl
Cl, W2[x],
TA2:
TA3:
W2[x]
r3[z],
2
transaction TA2 is waiting (aka blocked), W2[x] not yet executed
The scheduling happens by waiting
Local transactions are merged into a single schedule
cs 351, cs 751
TA management Slide Set 1
10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../source/751%2525/DB51wk10gw3IsolationSimple.pdf#page=11)

### 原始文字层

````text
CS 351, CS 751 TA management Slide Set 1 11
Schedulers produce schedules
• Since schedulers cannot execute operations before they 
are issued by the clients, schedulers delay operations.
 s: r1[x], r1[y], r3[z], w1[x], c1, w2[x], c2,r3[x], c3
TA1: r1[x], r1[y], w1[x], c1 
TA2: w2[x] _______________________, c2
TA3: r3[z], r3[x] __________________, c3,
• The scheduling happens by waiting
• Local transactions are merged into a single schedule
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Schedulers produce schedul es
• Si  nce schedul  ers cannot execute operations before they
  are issued by the clients, schedulers delay operati  ons.
      s:    r1[x], r1[y], r3[z], w1[x],            c1, w2[x], c2,r3[x], c3
    TA1: r1[x], r1[y],          w1[x],           c1
    TA2:      w2[x] _______________________, c2
    TA3:                  r3[z],    r3[x] __________________, c3,
• T he schedul  ing happens by waiting
• Local transacti  ons are m erged into a single schedul  e
CS 351,  CS 751                 TA     m  ana   gem  ent      Sl i    de       Set      111
````

### 图片文字 OCR（en-US，待对照原页）

````text
Schedulers produce schedules
Since schedulers cannot execute operations before they
are issued by the clients, schedulers delay operations.
s: q [x], q [y], r3[z], WI [x],
TAI : rl
Cl, W2[x],
TA2:
TA3:
W2[x]
r3[z],
The scheduling happens by waiting
Local transactions are merged into a single schedule
cs 351, cs 751
TA management Slide Set 1
11
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../source/751%2525/DB51wk10gw3IsolationSimple.pdf#page=12)

### 原始文字层

````text
351/751 TA management 12
simple scheduler and disjoint-access TAs
• The simple scheduler does not delay disjoint-access TAs
Theorem: For the simple scheduler:
• If a transaction T is disjoint-access with all other 
transactions open during its lifetime (from Begin of 
Transaction of T to its commit/abort)
• then the simple scheduler does not delay this transaction.
Proof:
• The transaction does not encounter any lock by another 
transaction.
Result: The simple scheduler is much better than DB-wide 
mutual exclusion.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
si mpl e sc hedul er and di sjoi nt                 -access  TAs
• T he simple scheduler does not delay di  sjoint             -access TAs
Theorem: For the simple scheduler:
• If a transaction T  is di  sjoint-access with all   other
  tr ansactions open during its lifetime (from Begin of
  T ransaction of      T  to its commit/abort)
• then the simple schedul  er does not delay this transaction.
Pr  oo  f:
• T he transaction does not encounter any lock by another
  tr ansaction.
Result: The simple schedul  er is          much better than DB-wide
mutual exclusion.
35   1/ 7   51                     TA     m  ana   gem  ent                      12
````

### 图片文字 OCR（en-US，待对照原页）

````text
simple scheduler and disjoint-access TAs
The simple scheduler does not delay disjoint-access TAs
Theorem: For the simple scheduler:
If a transaction T is disjoint-access with all other
transactions open during its lifetime (from Begin of
Transaction of T to its commit/abort)
then the simple scheduler does not delay this transaction.
Proof:
The transaction does not encounter any lock by another
transaction.
Result: The simple scheduler is much better than DB-wide
mutual exclusion.
351/751
TA management
12
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../source/751%2525/DB51wk10gw3IsolationSimple.pdf#page=13)

### 原始文字层

````text
CS 351, CS 751 TA management Slide Set 1 13
Example Deadlock for the simple scheduler
∙ Consider
∙ s: r1[x], w1[x], r2[y], w2[y], ????
∙ TA1: r1[x], w1[x], r1[y], _______???
∙ TA2: r2[y], w2[y], r2[x] _____???
∙ A deadlock is a cyclical wait-relation between transactions 
in a scheduler.
∙ Deadlocks are detected by the scheduler (several 
approaches, e.g. graph-based detecting cycles in a waits￾for graph).
Cyclical waiting cannot be resolved: deadlock
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Example Deadlock for the si mple schedul er
∙ Consider
∙   s:    r1[x], w1[x], r2[y], w2[y], ????
∙ TA1:     r1[x], w1[x],                     r1[y], _______???
∙ TA2:                      r2[y], w2[y],           r2[x] _____???
           Cy clical  waiting cannot be resolv ed:  deadlock
∙ A deadlock i  s a cyclical wait-relati  on between transactions
  in a scheduler.
∙ Deadlocks are detected by the scheduler ( several
  approaches, e.g. graph-based detecti  ng cycles in a waits-
  for graph).
CS 351,  CS 751                TA     m  ana   gem  ent      Sl i    de       Set      113
````

### 图片文字 OCR（en-US，待对照原页）

````text
Example Deadlock for the simple scheduler
Consider
s: r 1 WI r2[Y], W2[Y],
, TAI: rl[x], WI
TA2:
Cyclical waiting cannot be resolved: deadlock
A deadlock is a cyclical wait-relation between transactions
in a scheduler.
Deadlocks are detected by the scheduler (several
approaches, e.g. graph-based detecting cycles in a waits-
for graph).
cs 351, cs 751
TA management Slide Set 1
13
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../source/751%2525/DB51wk10gw3IsolationSimple.pdf#page=14)

### 原始文字层

````text
351/751 TA management 14
Abort in non- DB-wide mutual exclusion
Problem: Implicit instant-online transaction management that 
do not block data disjoint transactions must sometimes abort 
transactions.
• Example: The request sequence: 
w1[x], w2[y], w1[y], w2[x] requires abort of one transaction.
• The prefix request schedule w1[x], w2[y] cannot be blocked 
because it may be develop into data disjoint transactions. 
After this prefix has been executed, both transactions have 
done operations that are incompatible with any guaranteed 
correct completion.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Abort in non         - DB-wide mutual exc lusi on
Pr ob lem: Implici  t instant-online transacti  on m anagement that
  do not block data disjoint transactions must sometimes abort
  transactions.
• Example: T he request sequence:
  w1[x], w2[y], w1[y], w2[x] requires abort of one transaction.
• T he prefix r equest schedule w1[x], w2[y] cannot be blocked
  because it may be develop into data di  sjoint transactions.
  After this prefix has been executed, both transactions have
  done operations that are incompatible with any guaranteed
  correct completion.
35   1/ 7   51                    TA     m  ana   gem  ent                     14
````

### 图片文字 OCR（en-US，待对照原页）

````text
Abort in non- DB-wide mutual exclusion
Problem: Implicit instant-online transaction management that
do not block data disjoint transactions must sometimes abort
transactions.
Example: The request sequence:
WI [X], W2[y], WI [y], W2[x] requires abort of one transaction.
The prefix request schedule WI [x], W2[y] cannot be blocked
because it may be develop into data disjoint transactions.
After this prefix has been executed, both transactions have
done operations that are incompatible with any guaranteed
correct completion.
351/751
TA management
14
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../source/751%2525/DB51wk10gw3IsolationSimple.pdf#page=15)

### 原始文字层

````text
351/751 TA management 15
Deadlock resolution
• If transactions wait in a cycle on each other (deadlock), 
abort one transaction in the cycle.
• We make use of the rollback mechanism that we already 
have defined. 
• The transaction under rollback keeps the locks until the 
rollback is completed.
• The transaction to pick for abort may have to be chosen 
judiciously: we need to prevent starvation: that one 
transaction script always gets its transactions aborted.
• Deadlocks can be reduced by following patterns, e.g. 
naming a preferred order to access objects: if everyone 
follows the order, then no deadlocks appear!
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Deadlock  res ol uti on
• If transacti  ons wait in a cycl  e on each other ( deadlock),
  abort one transaction in the cycle.
• We m ake use of the rollback mechanism that we already
  have defined.
• T he transaction under rollback           keeps the locks until the
  rollback i  s completed.
• T he transaction to pick for abort may have to be chosen
  judiciously: we need to prevent starvation: that one
  tr ansaction script always gets its transactions aborted.
• Deadlocks can be reduced by following patterns, e.g.
  nami  ng a preferred order to access objects: i  f everyone
  follows the order, then no deadlocks appear!
35   1/ 7   51                     TA     m  ana   gem  ent                      15
````

### 图片文字 OCR（en-US，待对照原页）

````text
Deadlock resolution
If transactions wait in a cycle on each other (deadlock),
abort one transaction in the cycle.
We make use of the rollback mechanism that we already
have defined.
The transaction under rollback keeps the locks until the
rollback is completed.
The transaction to pick for abort may have to be chosen
judiciously: we need to prevent starvation: that one
transaction script always gets its transactions aborted.
Deadlocks can be reduced by following patterns, e.g.
naming a preferred order to access objects: if everyone
follows the order, then no deadlocks appear!
351/751
TA management
15
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../source/751%2525/DB51wk10gw3IsolationSimple.pdf#page=16)

### 原始文字层

````text
Summary
1. Transaction: A sequence of operations that form a logical 
unit; the client has to request commit.
2. The simple scheduler (exclusive locks) does not delay 
disjoint-access transactions, 
3. Works with one exclusive lock per object.
4. Locks are released at end of transaction
5. No explicit lock commands are needed.
6. Deadlocks can happen, require abort of a transaction.
351/751 TA management 16
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Summa ry
1.  Transaction: A s  equence o f operations that f  orm a lo gi cal
    unit; the cl ient has to r equest commit.
2.  The s imple scheduler  (exclusive l ocks) does  no tdelay
    disjo int-acces s transactions,
3.  Wor ks with one excl us ive lo ck per o bject.
4.  Locks  ar e released at end of transaction
5.  No  expli cit lock commands  ar e needed.
6.  Deadlo cks can happen, require abor t o f a tr ans actio n.
 351  /751                          TA man ag ement                               16
````

### 图片文字 OCR（en-US，待对照原页）

````text
Summary
1.
2.
3.
4.
5.
6.
Transaction: A sequence of operations that form a logical
unit; the client has to request commit.
The simple scheduler (exclusive locks) does not delay
disjoint-access transactions,
Works with one exclusive lock per object.
Locks are released at end of transaction
No explicit lock commands are needed.
Deadlocks can happen, require abort of a transaction.
351/751
TA management
16
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../source/751%2525/DB51wk10gw3IsolationSimple.pdf#page=17)

### 原始文字层

````text
351/751 TA management 17
Retry loop for transaction script
• In best practice for transactional programming, the 
transaction script must always be embedded in a retry loop:
do{
result = transactionScript(requestForm);
} while(result.isRolledBack());
• All info for correct request answering must be collected 
beforehand as parameter for the request:
• Script has to be careful with communication outside DB.
• The loop can be implicitly given e.g. by certain containers for 
scripts, or messaging systems that do the retry, but we have 
to make sure that it happens somewhere.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Retr y loop for tr ansacti on scr ipt
• In best practice for tr ansactional pr ogramming, the
  tr ansaction script must always be embedded in a                       r etr y loop  :
    do{
       re   su  lt    = tr  an  sac  tionScr  ipt(re    ques  tF  orm);
    } while(re   su  lt   .isRolledBack());
• Al  l info for correct request answering must be collected
  beforehand as parameter for the request:
• Scr ipt has to be careful wi  th communication outside DB.
• T he loop can be impli  citly gi  ven e.g. by certain containers for
  scripts, or messaging systems that do the retry, but we have
  to make sure that it happens somewhere.
35   1/ 7   51                        TA     m  ana   gem  ent                         17
````

### 图片文字 OCR（en-US，待对照原页）

````text
Retry loop for transaction script
In best practice for transactional programming, the
transaction script must always be embedded in a
retry loop:
do{
result = transactionScript(requestForm);
} while(result.isRoIledBack());
All info for correct request answering must be collected
beforehand as parameter for the request:
Script has to be careful with communication outside DB.
The loop can be implicitly given e.g. by certain containers for
scripts, or messaging systems that do the retry, but we have
to make sure that it happens somewhere.
351/751
TA management
17
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

