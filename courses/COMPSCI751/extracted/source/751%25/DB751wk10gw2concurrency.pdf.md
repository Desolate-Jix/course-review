# DB751wk10gw2concurrency.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI751/source/751%25/DB751wk10gw2concurrency.pdf`
- [打开原文件](../../../source/751%2525/DB751wk10gw2concurrency.pdf)
- 原文件 SHA-256：`ed8c72e59a8c4000896a3fafe39284a5bf999387f4990fefba219b86f1a4b649`
- 文件索引：F169；PDF 总页数：17
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../source/751%2525/DB751wk10gw2concurrency.pdf#page=1)

### 原始文字层

````text
351/751
Gerald Weber
Transaction Processing
How to perform composite updates safely for a 
remotely and concurrently accessed system.
Concurrency, ACID properties
351/751 TA management 1
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
35  1/7  51
                                      Gerald  Weber
                   Tran sac ti  on  Proc es sing
      Ho  w  to   p e rfor m com  po  si te   upd a te s  s afe ly   for  a
          r em  ote l y  a nd   concur re ntl y  a cce ss e d  s ys te m.
    C oncurr ency ,        AC ID p rop e rt ie s
 351  /751                              TA man ag ement                                    1
````

### 图片文字 OCR（en-US，待对照原页）

````text
351/751
Gerald Weber
Transaction Processing
How to perform composite updates safely for a
remotely and concurrently accessed system.
Concurrency, ACID properties
351/751
TA management
1
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../source/751%2525/DB751wk10gw2concurrency.pdf#page=2)

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

[查看此页](../../../source/751%2525/DB751wk10gw2concurrency.pdf#page=3)

### 原始文字层

````text
This just in….
DB 51 CS 351, CS 751 TA management Slide Set 1 3
````

### 图片文字 OCR（en-US，待对照原页）

````text
This just in....
QTY
TICKET TYPE
Allocated Seating
Floor Standing
Loyalty Meet & Greet Pac...
Damn. Early Entry Package
Sorry, no results match your search.
Try changing ticket type.
Find Resale Tickets
tekeiller
@tekeiller
iSi
md me
oms
how are GA @kendricklamar sold out 22 secs after tickets go on
sale @Tlcketmaster NZO!
1211 PM - Apr 30, 2018
0 4 g See tekeillers other Tweets
DB 51
TA management Slide Set 1
3
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../source/751%2525/DB751wk10gw2concurrency.pdf#page=4)

### 原始文字层

````text
• Simple Solution proposal for Concurrency Problem:
• DB-wide Mutual exclusion (MutEx) :
User orders are executed one at a time.
• System again needs to know when user order ends: commit.
• Must know when the next user’s order can start.
• Needs again transaction demarcation!
Transaction: A sequence of operations that form a logical unit; 
sequence of operations delimited by TA demarcation.
• In mutual exclusion, Transactions can get delayed.
351/751 TA management 4
Solution Proposal
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Solution Proposal
• Simple So l ut  io n pro po sal fo r Co ncur rency Pr oblem:
    •  DB-w ide  Mu tu al  exclus ion             (MutEx) :
       User  or der s are executed o ne at a ti me.
• System again needs  to  kno w when user o rder ends: commit.
• Must kno w when the next us er ’s or der  can s tar t.
• Needs agai n tr ans actio n demarcation!
         Tr  a ns a cti on:  A sequenc e of operations that f orm a  logic al unit;
         sequenc e of  operations  del  imited by  TA demarcati  on.
• In mutual exclusi on, Tr ans actio ns  can get delayed.
  351  /751                              TA man ag ement                                 4
````

### 图片文字 OCR（en-US，待对照原页）

````text
Solution Proposal
Simple Solution proposal for Concurrency Problem:
DB-wide Mutual exclusion (MutEx)
User orders are executed one at a time.
System again needs to know when user order ends: commit.
Must know when the next user's order can start.
Needs again transaction demarcation!
Transaction: A sequence of operations that form a logical unit;
sequence of operations delimited by TA demarcation.
In mutual exclusion, Transactions can get delayed.
351/751
TA management
4
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../source/751%2525/DB751wk10gw2concurrency.pdf#page=5)

### 原始文字层

````text
• Scalability limits: DB-wide Mutual exclusion for user orders 
puts a strict limit on the throughput of the system: 
• DB-wide MutEx serializes all transactions.
• transaction script needs all parameters beforehand, does 
not talk to human operator.
• Assume for sake of argument: each transaction takes on 
average 0.04 seconds to process on current hardware:
• Average number of transactions per second for MutEx: ?
351/751 TA management 5
Analysis of Solution Proposal
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Analysis of Solution  Pro posa l
• Scalabi lity li mits: DB-wide Mutual excl usio n f  or us er  or der s
  puts  a s tr ict limi t o n the throughput of  the sys tem:
    •  DB-wide MutEx se r ia li  ze s all  tr ans actio ns.
    •  transaction scr ipt      needs  al l parameter s  bef  orehand, does
       not tal k to  human operator .
    •  As sume f  or s ake o f argument: each tr ans actio n takes o n
       average 0.04  seconds to process  on curr ent hardwar e:
    •  Aver age number o f transacti ons per s eco nd fo r                 MutEx:  ?
  351  /751                              TA man ag ement                                 5
````

### 图片文字 OCR（en-US，待对照原页）

````text
Analysis of Solution Proposal
Scalability limits: DB-wide Mutual exclusion for user orders
puts a strict limit on the throughput of the system:
DB-wide MutEx serializes all transactions.
transaction script needs all parameters beforehand, does
not talk to human operator.
Assume for sake of argument: each transaction takes on
average 0.04 seconds to process on current hardware:
Average number of transactions per second for MutEx: ?
351/751
TA management
5
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../source/751%2525/DB751wk10gw2concurrency.pdf#page=6)

### 原始文字层

````text
351/751 TA management
Case against DB-wide MutEx: disjoint-access TAs
• Shared object: a data object accessed 
by more than one transaction in a set.
• A set of transactions is disjoint-access, 
if it has no shared object.
• thought experiment: If concurrent 
transactions access random data in a 
huge database,
• then often they are disjoint-access.
• Also, if transactions are concerned with 
unrelated matters:
• they are probably disjoint-access.
6
k
y
x
z
w2
r1 w1
r2
write access by 1
read access by 2
complete content of
database
r1 r2
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Case  agai nst  DB-wide MutEx: disjoint-access TAs
 • Shared object: a data object accessed
   by more than one transaction in a set.
 • A set of transactions is disjoint-access,                r k
                                                             2               x
   if it has no shared object.                                            w2
 • thought experiment: If concurrent                         co mplete co ntent of
   transactions access random data in a                            database
   huge database,                                                r2           r
                                                                               1
     •  then often they are disjoint-access.                    r   z      y
                                                                 1           w1
 • Al  so, if transactions are concerned with
   unrelated matters:                                         write access by 1
     •  they are probabl  y disj  oi  nt-access.            read access by 2
  35   1/ 7   51                      TA     m  ana   gem  ent                    6
````

### 图片文字 OCR（en-US，待对照原页）

````text
Case against DB-wide MutEx: disjoint-access TAs
Shared object
a data object accessed
by more than one transaction in a set.
A set of transactions is disjoint-access,
if it has no shared object.
thought experiment: If concurrent
transactions access random data in a
huge database,
then often they are disjoint-access.
Also, if transactions are concerned with
unrelated matters:
they are probably disjoint-access.
351/751
TA management
omplete content of
database
r2
z
write access by 1
read access by 2
6
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../source/751%2525/DB751wk10gw2concurrency.pdf#page=7)

### 原始文字层

````text
Read/Write Model (abstract Key/Value Store):
• DB storing a single current value per key: A Map.
• Keys are initialized with a null value.
• Two operations:
• Read r[x] y=db.get(x) : get value for key x
• Write w[x] db.put(x,y) : replace val. for key x with y
• In Java: db.put(key, val); y=get(key);
• What is the value of y?
DB 51 CS 351, CS 751 TA management Slide Set 1 7
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Read/Wri te Model (abs trac t Key/Value Store) :
  •  DB stor ing a single curr ent  value per key: A M  ap.
  •  Keys ar e init iali zed wi th a null  val ue.
  •  Two operati ons:
  •  Read r[x]   y=db.get(x) :   g  et   v  a  lu  e   fo  r   k  ey   x
  •  Wr ite    w[ x]   db.put(x,y) :   re  p  la  c  e   v  al   . f  o  r k  e  y   x   w it  h   y
       •  In     Ja  v  a  : db.put(key, val); y=get(key);
       •  Wh a t  is  th e  v a lu e  o f  y?
DB    51CS 351,  CS 751                TA     m  ana   gem  ent      Sl i    de       Set      1 7
````

### 图片文字 OCR（en-US，待对照原页）

````text
Read/Write Model (abstract Key/Value Store):
DB storing a single current value per key: A Map.
Keys are initialized with a null value.
Two operations:
y=db.get(x) . get value for key x
Read r[x]
db.put(x,y)
replace val. for key x with y
Write
In Java: db.put(key, val); y=get(key);
What is the value of y?
DB 51
TA management Slide Set 1
7
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../source/751%2525/DB751wk10gw2concurrency.pdf#page=8)

### 原始文字层

````text
Read/Write Model (abstract Key/Value Store):
• We focus on read/write[object] for eg a 
transaction TA1, r1[x], w1[x]
• Read r1[x] y=db.get(x) : get value for key x
• Write w1[x] db.put(x,y) : repl. val. for key x with y
• Commit c1
• Abort a1
DB 51 CS 351, CS 751 TA management Slide Set 1 8
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Read/Wri te Model (abs trac t Key/Value Store) :
       •   We  f o cu s  o n  r ea d /wr it e[ o bj  e ct ] f or  eg a
           tr  a  n  sa  c  tio  n   T  A 1  , r1[x], w1[x]
  •  Read r1[x]   y=db.get(x) :   g et   v  a lu e  fo r   k  ey   x
  •  Wr ite      w1[x]  db.put(x,y) :   re  p  l.   v  al   . f  o  r k  e  y   x   w it  h   y
  •  Commi t c1
  •  Abort a1
DB    51CS 351,  CS 751                   TA     m  ana   gem  ent      Sl i    de       Set      1     8
````

### 图片文字 OCR（en-US，待对照原页）

````text
Read/Write Model (abstract Key/Value Store):
We focus on read/write[object] for eg a
transaction TAI , rl[x], Wl[x]
get value for key x
y=db.get(x)
Read
db.put(x,y)
repl. val. for key x with y
Write
Commit
Abort
DB 51
TA management Slide Set 1
8
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../source/751%2525/DB751wk10gw2concurrency.pdf#page=9)

### 原始文字层

````text
351/751 TA management 9
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
35   1/ 7   51                                 TA     m  ana   gem  ent                                  9
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
9
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../source/751%2525/DB751wk10gw2concurrency.pdf#page=10)

### 原始文字层

````text
351/751 TA management
DB-wide MutEx bad for disjoint-access TAs
• Shared object: a data object accessed by 
more than one transaction in a set.
• A set of transactions T is disjoint-access, if it 
has no shared object.
• Principle: disjoint-access transactions 
do not interfere.
• Hence should not be delayed
• But DB-wide MutEx does delay them:
• DB-wide MutEx is too blunt a tool:
• So: how to detect whether 
transactions are disjoint-access?
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
10
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
DB-wide MutE x bad for  di sjoi nt-access  TAs
• Shared object : a data  object  acc es sed by
  more than one transact ion  in a set .
• A s et  of  trans actions  T is  disjoint-acc es s,  if it   r  k
  has no shared objec t.                                        2                x
                                                                             w2
• Principle: disjoint-access transacti  ons
  do not i  nterfere.
• Hence should not be del  ayed
• But DB-wide MutEx does delay them:                                              r1
                                                                   r   z       y
• DB-wide MutEx is too blunt a tool:                                1            w1
• So: how to detect whether
  transactions are disjoint-access?                              write access by 1
                                                               read access by 2
 35   1/ 7   51                        TA     m  ana   gem  ent                       10
````

### 图片文字 OCR（en-US，待对照原页）

````text
DB-wide MutEx bad for disjoint-access TAs
Shared object: a data object accessed by
more than one transaction in a set.
A set of transactions T is disjoint-access, if it
has no shared object.
Principle: disjoint-access transactions
do not interfere.
Hence should not be delayed
But DB-wide MutEx does delay them:
DB-wide MutEx is too blunt a tool:
So: how to detect whether
transactions are disjoint-access?
351/751
TA management
z
write access by 1
read access by 2
10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../source/751%2525/DB751wk10gw2concurrency.pdf#page=11)

### 原始文字层

````text
• Scalability limits: DB-wide Mutual exclusion user order puts a 
strict limit on the throughput of the system:
• Challenge: Design a solution that offers clients mostly the 
same interface as for MutEx, but does not unnecessary delay 
transactions, 
• does not delay disjoint-access transactions
351/751 TA management 11
Challenge Transaction processing:
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Challenge Transaction pro cessing:
• Scalabi lity li mits: DB-wide Mutual excl usio n us er  or der  puts a
  str ict l imit on the throughput of  the sys tem:
• Chall enge: Design a sol utio n that offer s clients mos tl y the
  same interface as for  MutEx, but do es not unnecessar y del ay
  transactions,
    •  does not delay di sjoi nt-acces s transactions
  351  /751                            TA man ag ement                             11
````

### 图片文字 OCR（en-US，待对照原页）

````text
Challenge Transaction processing:
Scalability limits: DB-wide Mutual exclusion user order puts a
strict limit on the throughput of the system:
Challenge: Design a solution that offers clients mostly the
same interface as for MutEx, but does not unnecessary delay
transactions,
does not delay disjoint-access transactions
351/751
TA management
11
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../source/751%2525/DB751wk10gw2concurrency.pdf#page=12)

### 原始文字层

````text
351/751 TA management 12
The ACID properties
• Widely accepted requirements that a transaction manager 
must meet for the transactions [Gray et al, 1974, 1983]:
∘ Atomicity: either all of the operations of a transaction 
are made durable or none of them are. 
∘ Consistency: after the transaction, the database is in 
a consistent state.
∘ Isolation: operations in a transaction appear isolated 
from all other operations. Transactions have a virtual 
serial view on the system. 
∘ Durability: once the user has been notified of success, 
the transaction will persist, and not be undone.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
The  ACID pro perties
• Widely accepted r equir ements that a transaction manager
  must meet for  the transactions  [Gr ay et al, 19 74 , 19 83 ]:
    ∘  Ato m  ic i ty: ei ther al l of the operations o f a tr ansacti on
       are made durable or  none of them ar e.
    ∘  Cons isten cy      : after the tr ansacti on, the databas e i s in
       a consi stent state.
    ∘  Isolation:  o per ati ons in a transaction appear i sol ated
       fr om all o ther  oper ati ons. Transacti ons have a virtual
       ser ial vi ew o n the system.
    ∘  Durability: o nce the us er has been notif ied o f success,
       the tr ans actio n wi ll pers ist, and not be undone.
351  /751                             TA man ag ement                              12
````

### 图片文字 OCR（en-US，待对照原页）

````text
The ACID properties
Widely accepted requirements that a transaction manager
must meet for the transactions [Gray et al, 1974, 1983]:
Atomicity: either all of the operations of a transaction
are made durable or none of them are.
Consistency: after the transaction, the database is in
a consistent state.
Isolation:
operations in a transaction appear isolated
from all other operations. Transactions have a virtual
serial view on the system.
Durability: once the user has been notified of success,
the transaction will persist, and not be undone.
351/751
TA management
12
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../source/751%2525/DB751wk10gw2concurrency.pdf#page=13)

### 原始文字层

````text
351/751 TA management 13
ACID atomicity
1. Only if the client has requested commit, write operations 
in the transaction may become durable.
Atomicity protects against client failures that lead to 
incomplete transaction processing:
Hence: Database must take care of the rollback in 
case of abort.
1. b. client can request abort as a programming feature.
2. Either all writes of the transaction, or none become 
durable: If any write becomes durable, all must become 
durable.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
ACID   at omicity
1.  Only if the client has  reques ted commit, wr ite o per ati ons
    in the tr ans actio n may become dur able.
    Atomici ty pro tects agai nst cl ient f  ai lures  that lead to
    incomplete tr ans actio n pr ocessi ng:
    Hence: Dat abas e m us t t ake care  of  th e rollback  in
    cas e of ab  ort .
1.  b. cl ient can reques t abor t as  a pr ogramming f  eature.
2.  Either all  writes o f the transaction, or  no ne become
    durable: If any wri te beco mes  dur abl e, all  mus t become
    durable.
351  /751                            TA man ag ement                              13
````

### 图片文字 OCR（en-US，待对照原页）

````text
ACID atomicity
1.
1.
2.
Only if the client has requested commit, write operations
in the transaction may become durable.
Atomicity protects against client failures that lead to
incomplete transaction processing:
Hence: Database must take care of the rollback in
case of abort.
b. client can request abort as a programming feature.
Either all writes of the transaction, or none become
durable: If any write becomes durable, all must become
durable.
351/751
TA management
13
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../source/751%2525/DB751wk10gw2concurrency.pdf#page=14)

### 原始文字层

````text
351/751 TA management 14
ACID consistency (high-level)
a) Is referring to additional high-level features of the DB 
(and is not part of the basic transaction model we will 
use) Declarative integrity constraints, such as referential 
integrity, must hold between transactions.
b) During the transaction, certain integrity constraints might 
be violated, but on commit, they must be fulfilled
∘ by explicit operations in the transaction,
∘ by automatic mechanisms (ON DELETE CASCADE),
∘ by user-defined triggers.
Any transaction still violating constraints will be aborted.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
ACID  co nsist ency   (high                -lev el)
a)  Is r eferr ing to  additional hi gh-level f eatures o f the DB
    (and is no t part of the bas ic tr ansacti on model  we wi ll
    use) Decl arative integr ity co nstraints, such as  refer ential
    integr ity, mus t hol d between transacti ons.
b)  During the transaction, certain integr ity co nstraints might
    be viol ated, but o n co mmi t, they must be fulfil led
    ∘  by expli cit oper ati ons i n the tr ansacti on,
    ∘  by automatic mechanis ms  (ON DELETE C  ASCADE),
    ∘  by user-defined tr igger s.
    Any transaction stil l vio lating co ns tr aints will  be abor ted.
351  /751                             TA man ag ement                              14
````

### 图片文字 OCR（en-US，待对照原页）

````text
ACID consistency (high-level)
a) Is referring to additional high-level features of the DB
(and is not part of the basic transaction model we will
use) Declarative integrity constraints, such as referential
integrity, must hold between transactions.
b) During the transaction, certain integrity constraints might
be violated, but on commit, they must be fulfilled
by explicit operations in the transaction,
by automatic mechanisms (ON DELETE CASCADE),
by user-defined triggers.
Any transaction still violating constraints will be aborted.
351/751
TA management
14
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../source/751%2525/DB751wk10gw2concurrency.pdf#page=15)

### 原始文字层

````text
351/751 TA management 15
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
351  /751                              TA man ag ement                                15
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
15
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../source/751%2525/DB751wk10gw2concurrency.pdf#page=16)

### 原始文字层

````text
351/751 TA management 16
ACID durability
• Once the user has been notified of success of transaction t:
a) All writes of t are permanent: must be changed through 
later committed writes, e.g. compensating transactions.
b) The effect of t is kept in a crash resistant way.
∘ minimum requirement: transaction is written to 
persistent storage: resistant against 
∙ OS crash
∙ system outage
c) preferred: protection against loss of persistent memory:
1. Resistance against persistent storage failure
2. resistance against catastrophes, geographic distribution
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
ACID   durabilit y
• Once the us er has been notif  ied o f success o f tr ansacti on t:
a)  Al l wri tes o f t ar e per manent: must be changed thr ough
    later committed wr ites , e.g. compensati ng transactions .
b)  The eff  ect of t is  kept in a crash r esis tant way.
    ∘  minimum requir ement: transacti on is  wr itten to
       persi stent stor age:  resi stant agai ns t
         ∙  OS crash
         ∙  system  outage
c)  prefer red: protecti on agai ns t l oss  of pers istent memor y:
         1.   Resi  stanc e against  persistent storage f ailure
         2.   resistanc e against catastrophes, geographic  di  stribution
351  /751                              TA man ag ement                                16
````

### 图片文字 OCR（en-US，待对照原页）

````text
ACID durability
Once the user has been notified of success of transaction t:
a) All writes of t are permanent: must be changed through
later committed writes, e.g. compensating transactions.
b) The effect of t is kept in a crash resistant way.
0 minimum requirement: transaction is written to
persistent storage: resistant against
OS crash
system outage
c) preferred: protection against loss of persistent memory:
1. Resistance against persistent storage failure
2. resistance against catastrophes, geographic distribution
351/751
TA management
16
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../source/751%2525/DB751wk10gw2concurrency.pdf#page=17)

### 原始文字层

````text
Summary
1. we need transaction demarcation: for Mutex, but also for 
atomicity: for both remote and concurrent access.
2. Transaction: A sequence of operations that form a logical 
unit; the client has to request commit.
3. The database needs to roll back failed transactions.
4. DB-wide Mutex delays disjoint-access transaction, does not 
scale. We need to find a more scalable solution with the 
same interface as DB-wide Mutex.
5. The ACID Properties (Atomicity, Consistency, Isolation, 
Durability) are the requirements of transaction processing.
351/751 TA management 17
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Summa ry
1.  we need transacti on demar catio n:  for  Mutex, but al so fo r
    atomicity: fo r both remot e and concu rren t acces s.
2.  Transaction: A s  equence o f operations that f  orm a lo gi cal
    unit; the cl ient has to r equest commit.
3.  The database needs  to  rol l back fail ed transactions .
4.  DB-wide Mutex delays   di sjoi nt-acces s transaction, do es not
    scale. We need to fi nd a mor e scalabl e sol utio n wi th the
    same interface as DB-wide Mutex.
5.  The A CID Pr oper ties (A to mi city, Co nsis tency, Is olatio n,
    Durabili ty)  ar e the r equir ements of  tr ans actio n pr ocessi ng.
 351  /751                          TA man ag ement                                17
````

### 图片文字 OCR（en-US，待对照原页）

````text
Summary
1.
2.
3.
4.
5.
we need transaction demarcation: for Mutex, but also for
atomicity: for both remote and concurrent access.
Transaction: A sequence of operations that form a logical
unit; the client has to request commit.
The database needs to roll back failed transactions.
DB-wide Mutex delays disjoint-access transaction, does not
scale. We need to find a more scalable solution with the
same interface as DB-wide Mutex.
The ACID Properties (Atomicity, Consistency, Isolation,
Durability) are the requirements of transaction processing.
351/751
TA management
17
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

