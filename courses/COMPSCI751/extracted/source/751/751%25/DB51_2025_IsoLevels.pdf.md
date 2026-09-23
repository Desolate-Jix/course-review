# DB51_2025_IsoLevels.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI751/source/751/751%25/DB51_2025_IsoLevels.pdf`
- [打开原文件](../../../../source/751/751%2525/DB51_2025_IsoLevels.pdf)
- 原文件 SHA-256：`aa3e04080f6ee46a1e1227f9b15cbfeb97cd09059d80dc9d03c7c459d50d19ed`
- 文件索引：F115；PDF 总页数：17
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../source/751/751%2525/DB51_2025_IsoLevels.pdf#page=1)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 1
Relaxed Isolation, Isolation Levels
• Transaction Management for high throughput:
• Relaxed transaction isolation
• ANSI Isolation Levels
• Phenomena
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Relaxed Isol ati on, Is ol ati on Lev el s
  •  T ransaction M anagem ent for high throughput:
  •  Relaxed transacti  on isolation
  •  AN  SI Isolation Levels
  •  Ph e n o me n a
  35   1/ 7   51                Geral  d Webe r's  TA Ma nag ement   Slid es                     1
````

### 图片文字 OCR（en-US，待对照原页）

````text
Relaxed Isolation, Isolation Levels
Transaction Management for high throughput:
Relaxed transaction isolation
ANSI Isolation Levels
Phenomena
351/751
Gerald Weber's TA Management Slides
1
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../source/751/751%2525/DB51_2025_IsoLevels.pdf#page=2)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 2
ACID Isolation
• Database operations in a transaction appear isolated from 
database operations of all other transactions
∙ does not apply to non-database operations of client programs
• One crucial property of high isolation: Repeatable Read:
∘ if a transaction reads a data field in the DB twice, and 
does not change it in between, it must receive the same 
value.
• Isolation with Repeatable Read is expensive: 
∘ leads to delays, deadlocks, and/or aborts.
∘ and can be relaxed: isolation levels.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
ACID  Isolation
• Database operations in a transaction appear isolated from
  database operations of all other transacti  ons
         ∙  does not  apply  to non   -database operat ions  of c lient  programs
• One crucial property of high isolation:                 Repeatable Read           :
    ∘  if a transacti  on r eads a data field in the DB twice, and
       does not change it in between, it must r eceive the same
       value.
• Isolation wi  th Repeatable Read i  s expensive:
    ∘  leads to delays, deadlocks, and/or aborts.
    ∘  and can be relaxed:           isolation level  s    .
35   1/ 7   51              Geral  d Webe r's  TA Ma nag ement   Slid es                 2
````

### 图片文字 OCR（en-US，待对照原页）

````text
ACID Isolation
Database operations in a transaction appear isolated from
database operations of all other transactions
does not apply to non-database operations of client programs
One crucial property of high isolation: Repeatable Read:
if a transaction reads a data field in the DB twice, and
does not change it in between, it must receive the same
value.
Isolation with Repeatable Read is expensive:
o leads to delays, deadlocks, and/or aborts.
o and can be relaxed: isolation levels.
351/751
Gerald Weber's TA Management Slides
2
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../source/751/751%2525/DB51_2025_IsoLevels.pdf#page=3)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 3
Repeatable Read:
• One crucial property: Repeatable Read:
∘ if a transaction reads a data field in the DB twice, does not 
change it in between, it must receive the same value.
• Pseudocode: val=r1[x]; wait(t); assert(val==r1[x]);
• C++ -like language: 
 val=DB.read(x); wait(t); assert(val== DB.read(x));
• Isolation with Repeatable Read is expensive, can be relaxed. 
• But always: w1[x](val); wait(t); assert(val==r1[x]); 
 DB.write(x, val); wait(t); assert(val== DB.read(x)); 
∘ Writes observe the exclusive lock of other writes!
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Repeatable Read:
• One cr ucial proper ty: Repeatable Read:
    ∘  if a transacti  on r eads a data field in the DB twice, does not
       change it in between, it m ust receive the sam e value.
• Pseudocode:              val =r1[x]; wait( t); assert(val==r1[x]);
• C++ -like language:
        val=DB .read(x); wait( t); assert(val== DB .read(x));
• Isolation wi  th Repeatable Read i  s expensive, can be relaxed.
• But always:       w1[x](val); wait( t); assert(val==r1[x]);
                  DB .w  rite(x, val); wait( t); assert(val== DB  .r ead(x));
    ∘  Writes observe the exclusive l  ock of other wri  tes!
35   1/ 7   51              Geral  d Webe r's  TA Ma nag ement   Slid es                3
````

### 图片文字 OCR（en-US，待对照原页）

````text
Repeatable Read:
One crucial property: Repeatable Read:
if a transaction reads a data field in the DB twice, does not
change it in between, it must receive the same value.
val=rl [x]; wait(t); [x]);
Pseudocode:
, C++ -like language:
val=DB.read(x); wait(t); assert(val== DB.read(x));
Isolation with Repeatable Read is expensive, can be relaxed.
WI wait(t); [x]);
But always:
DB.write(x, val); wait(t); assert(val== DB.read(x));
Writes observe the exclusive lock of other writes!
351/751
Gerald Weber's TA Management Slides
3
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../source/751/751%2525/DB51_2025_IsoLevels.pdf#page=4)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 4
Fuzzy read
• non-repeatable read: transaction gets two different values
• val1=DB.read(x); wait(t); val2=DB.read(x)); 
• val1 is not equal to val2.
• We want to call a violation of isolation that we can observe 
a phenomenon. 
• Transaction TA1 encounters a fuzzy read phenomenon if 
it reads two or more different committed values for x.
∘ scheduling example: r1[x], w2[x], c2, r1[x]
• Fuzzy read situations can lead to a more serious situation: 
lost updates.
fuzzy read
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Fuzzy  read
• non-repeatable read: transaction gets two different values
• val1=DB .read(x); wait( t); val2=DB .read(x));
•   val1 is not equal   to val2.
• We want to call a violati  on of isolati  on that we can observe
  a phenomenon.
• T ransaction T A1  encounters a fuzzy read  phenomenon if
  it reads two or m ore different committed values for x.
    ∘  schedul  ing exampl  e:   r1[x], w2[x], c2, r1[x]              fuzzy read
• F uzzy r ead situations can lead to a more serious situation:
  lost updates.
35   1/ 7   51            Geral  d Webe r's  TA Ma nag ement   Slid es              4
````

### 图片文字 OCR（en-US，待对照原页）

````text
Fuzzy read
non-repeatable read: transaction gets two different values
vall =DB.read(x); wait(t); va12=DB.read(x));
vall is not equal to va12.
We want to call a violation of isolation that we can observe
a phenomenon.
Transaction TAI encounters a fuzzy read phenomenon if
it reads two or more different committed values for x.
o scheduling example: G W2[x], c2, G [x]
fuzzy read
Fuzzy read situations can lead to a more serious situation:
lost updates.
351/751
Gerald Weber's TA Management Slides
4
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../../source/751/751%2525/DB51_2025_IsoLevels.pdf#page=5)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 5
Fuzzy read
• A type of non-repeatable read is a fuzzy read.
• Transaction TA1 encounters a fuzzy read phenomenon if it 
reads two or more different committed values for x.
∘ scheduling example: r1[x], w2[x], c2, r1[x]
• Fuzzy reads can happen, if
∘ TA2 does not observe the read-lock of transaction TA1.
∘ But TA1 observes the write lock on TA2.
• Fuzzy read situations can lead to a more serious situation 
(lost updates) in a rather counterfactual way:
∘ If the second read does not happen or is not acted 
upon: coming soon
fuzzy read
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Fuzzy  read
• A type of non      -repeatable read i  s a fuzzy read.
• T ransaction T A1        encounters a fuzzy read phenomenon if i  t
  reads two or m ore different com m itted values for x.
    ∘  schedul  ing exampl  e:        r1[x], w  2[x], c 2, r1[x]       fuzzy read
• F uzzy r eads can happen, i  f
    ∘  T A2 does not observe the read-lock of tr ansaction TA 1.
    ∘  But TA 1 observes the wri  te lock on T A2.
• F uzzy r ead situations can lead to a more serious situation
  (lost updates) in a rather counterfactual way:
    ∘  If the second r ead does not happen or is not acted
       upon: coming soon
35   1/ 7   51            Geral  d Webe r's  TA Ma nag ement   Slid es               5
````

### 图片文字 OCR（en-US，待对照原页）

````text
Fuzzy read
A type of non-repeatable read is a fuzzy read.
Transaction TAI encounters a fuzzy read phenomenon if it
reads two or more different committed values for x.
scheduling example: % [x], W2[x], c2, q [x]
fuzzy read
Fuzzy reads can happen, if
o TA2 does not observe the read-lock of transaction TAI .
o But TAI observes the write lock on TA2.
Fuzzy read situations can lead to a more serious situation
(lost updates) in a rather counterfactual way:
o If the second read does not happen or is not acted
upon: coming soon
351/751
Gerald Weber's TA Management Slides
5
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../source/751/751%2525/DB51_2025_IsoLevels.pdf#page=6)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 6
ANSI/ISO transaction isolation levels
• Isolation levels are defined with respect to three different 
phenomena (results of reduced isolation):
∘ Dirty read: reading an uncommitted value for x.
∘ Fuzzy read: reading different, committed values for x
∘ Phantom: reading a new committed inserted row.
• ANSI/ISO SQL-92 defines four isolation levels: 
Isolation Level Dirty read Fuzzy read Phantom
READ UNCOMMITTED Possible Possible Possible
READ COMMITTED Not Possible Possible Possible
REPEATABLE READ Not Possible Not Possible Possible
SERIALIZABLE Not Possible Not Possible Not Possible
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
ANSI/ISO trans ac ti on i solation l ev el s
 • Isolation levels are defined wi  th r espect to three different
   phenom ena ( results of reduced isolation):
     ∘  Dirty read: reading an uncommitted value for x.
     ∘  F uzzy read: reading different, com mi  tted values for x
     ∘  Phantom: reading a new com mitted inserted row.
 • AN  SI/IS  O S  QL    -92 defines four isolation levels:
Is olat ion  Lev el             Dirt y read        Fuz zy  read         Phant om
READ  UNC OM MITT ED            Possible           Possible             Possible
READ  COMMIT TED                No t  Possible     Possible             Possible
REPEATABLE  READ                No   t Possible    No   t Possible      Possible
SERIALIZ ABLE                   No   t Possible    No t Possible        No t Possible
 35   1/ 7   51              Geral  d Webe r's  TA Ma nag ement   Slid es                  6
````

### 图片文字 OCR（en-US，待对照原页）

````text
ANSI/ISO transaction isolation levels
Isolation levels are defined with respect to three different
phenomena (results of reduced isolation):
o Dirty read: reading an uncommitted value for x.
o Fuzzy read: reading different, committed values for x
o Phantom: reading a new committed inserted row.
ANSI/ISO SQL-92 defines four isolation levels:
Isolation Level
Dirty read
READ UNCOMMITTED Possible
READ COMMITTED
REPEATABLE READ
SERIALIZABLE
351/751
Not Possible
Not Possible
Not Possible
Fuzzy read
Possible
Possible
Not Possible
Not Possible
Gerald Weber's TA Management Slides
Phantom
Possible
Possible
Possible
Not Possible
6
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../../source/751/751%2525/DB51_2025_IsoLevels.pdf#page=7)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 7
Fuzzy read continued: lost updates
• a serious consequence of not using REPEATABLE READ: 
a committed transaction might miss an update: lost update
r1[x], r2[x], w2[x], c2, w1[x], c1
∘ example: 
∙ a123 is $99.
∙ TA1 withdraws $17, TA2 withdraws $23 
∘ r1[x] : d1 := 99
∘ r2[x] : d2 := 99
∘ w2[x] : a123 := 76 ( == d2-23)
∘ w1[x] : a123 := 82 (== d1-17)
here is the fuzzy read 
“zone”
r1[x], 
lost update
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Fuzzy  read conti nued: lost updates
• a serious consequence of not using REP EAT ABLE  R  EAD:
  a committed transaction mi  ght miss an update:                      lost up date
         r1[x], r 2[x], w2[x], c2,             w1[x], c1
    ∘  example:                        r1[x],
                                                    here is the fuzzy r ead
         ∙  a123  is $99.                           “zone”
         ∙  TA1 wit hdraws  $17,   TA   2 wit hdraws  $23
    ∘  r1[x]   : d 1 := 99
    ∘  r2[x]  : d2 :=  99
    ∘  w2[x] : a123 := 76 ( == d2-23)                       lost update
    ∘  w1[x] : a123 := 82  (== d1-17)
35   1/ 7   51             Geral  d Webe r's  TA Ma nag ement   Slid es                 7
````

### 图片文字 OCR（en-US，待对照原页）

````text
Fuzzy read continued: lost updates
, a serious consequence of not using REPEATABLE READ:
a committed transaction might miss an update: lost update
rl r2[x], W2[xl,
rl [x],
example:
here is the fuzzy read
, a123 is $99.
"zone"
TAI withdraws $17,
TA2 withdraws $23
o rl[x] : dl
= 99
o r2[x] : d2 99
d2-23) lost update
o : a123 76 (
Wl[x] : a123 82 dl-17)
351/751
Gerald Weber's TA Management Slides
7
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../../source/751/751%2525/DB51_2025_IsoLevels.pdf#page=8)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 8
Preventing lost update in READ COMMITTED
 Explicitly getting a write lock with SELECT FOR UPDATE can 
prevent lost updates even in READ COMMITTED level.
Current situation:
• s: r1[x], r2[x], w1[x], c1, w2[x], c2
• TA1: r1[x], w1[x], c1
• TA2: r2[x], w2[x] ______, c2
• Second read is now SELECT FOR UPDATE
• s: R1[x], w1[x], c1, R2[x], w2[x], c2
• TA1: R1[x], w1[x], c1
• TA2: R2[x] ____________, w2[x], c2
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
P rev enting lost update in REA D COMMITTE D
Expli  citly getting a write lock with S ELECT  FOR UP DAT E can
  prevent lost updates even in R  EAD COMMIT TE D level.
Current situation:
• s:      r1[x], r2[x], w1[x],      c1, w2[x], c2
• T A1: r1[x],         w1[x],       c1
• T A2:          r2[x],       w2[x] ______, c2
• Second read is now S ELECT  FOR UPD  ATE
• s:      R1[x],       w1[x],      c1, R2[x], w2[x], c2
• T A1: R1[x],         w1[x],     c1
• T A2:             R2[x] ____________, w2[x], c2
35   1/ 7   51             Geral  d Webe r's  TA Ma nag ement   Slid es                8
````

### 图片文字 OCR（en-US，待对照原页）

````text
Preventing lost update in READ COMMITTED
Explicitly getting a write lock with SELECT FOR UPDATE can
prevent lost updates even in READ COMMITTED level.
Current situation:
rl r2[x], WI
, TAI: rl[x],
Cl, W2[x],
, TA2:
r2[x], W2[x]
, Second read is now SELECT FOR UPDATE
, s: Rl[x],
, T A1: RI
, TA2:
351/751
Cl, R2[x], W2[x],
, W2[x],
Gerald Weber's TA Management Slides
8
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../../source/751/751%2525/DB51_2025_IsoLevels.pdf#page=9)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 9
Preventing lost update in READ COMMITTED
 Explicitly getting a write lock with SELECT FOR UPDATE can 
prevent lost updates even in READ COMMITTED level.
Current situation:
• s: r1[x], r2[x], w1[x], c1, w2[x], c2
• TA1: r1[x], w1[x], c1
• TA2: r2[x], w2[x] ______, c2
• Both reads are now SELECT FOR UPDATE
• s: R1[x], w1[x], c1, R2[x], w2[x], c2
• TA1: R1[x], w1[x], c1
• TA2: R2[x] ____________, w2[x], c2
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
P rev enting lost update in REA D COMMITTE D
Expli  citly getting a write lock with S ELECT  FOR UP DAT E can
  prevent lost updates even in R  EAD COMMIT TE D level.
Current situation:
• s:      r1[x], r2[x], w1[x],      c1, w2[x], c2
• T A1: r1[x],         w1[x],       c1
• T A2:          r2[x],       w2[x] ______, c2
• Both reads       are now SE LE CT F OR UPDA TE
• s:      R1[x],       w1[x],      c1, R2[x], w2[x], c2
• T A1: R1[x],         w1[x],     c1
• T A2:             R2[x] ____________, w2[x], c2
35   1/ 7   51             Geral  d Webe r's  TA Ma nag ement   Slid es                9
````

### 图片文字 OCR（en-US，待对照原页）

````text
Preventing lost update in READ COMMITTED
Explicitly getting a write lock with SELECT FOR UPDATE can
prevent lost updates even in READ COMMITTED level.
Current situation:
Cl, W2[x],
, TAI:
, TA2:
, TAI:
, TA2:
351/751
rl r2[x], WI
r2[x], W2[x]
, Both reads are now SELECT FOR UPDATE
Cl, R2[x], W2[x],
, W2[x],
Gerald Weber's TA Management Slides
9
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../source/751/751%2525/DB51_2025_IsoLevels.pdf#page=10)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 10
Recap: Only one transaction uses R[ ]
• Can the following transactions run into a deadlock ?
∙ TA1: r1[x], w1[x], c1
∙ TA2: R2[x], w2[x], c2
• No.
 Note: this was Isolation level REPEATABLE READ
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
Recap:                  Only  one transaction us es  R[  ]
•   Can the following transactions r un i  nto a deadlock                                                           ?
              ∙   TA1:   r     1[x   ],          w1[x   ],    c1
              ∙   TA2:   R      2[x   ],      w2[x   ],    c2
•   No .
         Note: this was Isolati  on level                                  RE PEA TAB LE REA D
•   F irst    s1:    r1[x   ],                                  w1[x   ],    c1, R2[x   ] ,               w2[x   ],    c2
              ∙   TA1:   r     1[x   ],                                  w1[x   ],    c1
              ∙   TA2:               R     2[x ]______________ ,        w                    2[x   ],    c2
      2nd   s2:                R2[x   ] ,                           w2[x   ],    c2, r1[x   ],           w1[x   ],      c1
              ∙   TA1:                   r   1[x ]______________,    w                    1[x   ],      c1
              ∙   TA2:    R       2[x   ] ,                           w2[x   ],    c2
 35   1/ 7   51                            Geral  d Webe r's  TA Ma nag ement   Slid es                                               10
````

### 图片文字 OCR（en-US，待对照原页）

````text
Recap: Only one transaction uses RI ]
Can the following transactions run into a deadlock ?
, TAI: rl[x],
, TA2: R2[x], W2[x],
, No.
Note: this was Isolation level
REPEATABLE READ
, First
2nd
351/751
sl:
, TAI:
, TA2:
s2:
, TAI:
TA2:
rl[X],
Wl[x], Cl
WI [x], Cl
R2[x] ,
R2[x]
R2[x] ,
R2[x]
W2[x],
Wl[x], Cl
WI [x], Cl
Gerald Weber's TA Management Slides
10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../source/751/751%2525/DB51_2025_IsoLevels.pdf#page=11)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 11
On Isolation Level READ COMMITTED
• Can the following transactions run into a deadlock ?
∙ TA1: r1[x], w1[x], c1
∙ TA2: R2[x], w2[x], c2
• How do the schedules look for the two timings we have 
discussed before?
• First relevant timing: 
∙ TA1: r1[x], w1[x], c1
∙ TA2: R2[x] , w2[x], c2
• Second relevant timing: 
∙ TA1: r1[x], w1[x], c1
∙ TA2: R2[x] , w2[x], c2
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
On Isolation Level READ COMMITTED
•  Can the following transactions r un i  nto a deadlock                                               ?
            ∙   TA1:   r   1[x   ],          w1[x   ],    c1
            ∙   TA2:   R     2[x   ],      w2[x   ],    c2
•  How do the schedules look for the two timings we have
   discussed before?
•  F irst relevant timing:
            ∙   TA1:   r   1[x   ],                                  w1[x   ],    c1
            ∙   TA2:               R  2[x   ] ,               w2[x   ],    c2
•  Second r elevant tim ing                     :
            ∙   TA1:                   r1[x   ],      w1[x   ],      c1
            ∙   TA2:    R     2[x   ] ,                           w2[x   ],    c2
 35   1/ 7   51                       Geral  d Webe r's  TA Ma nag ement   Slid es                                    11
````

### 图片文字 OCR（en-US，待对照原页）

````text
On Isolation Level READ COMMITTED
Can the following transactions run into a deadlock ?
, TAI: rl[x],
, TA2: R2[x], W2[x],
How do the schedules look for the two timings we have
discussed before?
First relevant timing:
, TAI: rl[x],
, TA2:
WI [x], Cl
R2[x], W2[x],
Second relevant timing:
, TAI:
, TA2: R2[x]
351/751
G [X], Wl[x], Cl
Gerald Weber's TA Management Slides
11
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../source/751/751%2525/DB51_2025_IsoLevels.pdf#page=12)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 12
On Isolation Level READ COMMITTED
• Can the following transactions run into a deadlock ?
∙ TA1: r1[x], w1[x], c1
∙ TA2: R2[x], w2[x], c2
• Still No. But different timing for alternative 1 on
isolation level READ COMMITTED
• First s1: r1[x], R2[x], w2[x], c2, w1[x], c1
∙ TA1: r1[x], w1[x] ________, c1
∙ TA2: R2[x], w2[x], c2
 2nd s2: R2[x] , w2[x], c2, r1[x], w1[x], c1
∙ TA1: r1[x]______________, w1[x], c1
∙ TA2: R2[x] , w2[x], c2
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
On Isolation Level READ COMMITTED
•   Can the following transactions r un i  nto a deadlock                                                     ?
             ∙   TA1:   r    1[x   ],          w1[x   ],    c1
             ∙   TA2:   R      2[x   ],      w2[x   ],    c2
•   Still N  o.       But different timing for alternative 1 on
    isolation level   R  EAD COM MIT TE D
•   F irst    s1:            r1[x   ], R2[x   ],    w2[x   ],    c2, w1[ x],     c1
             ∙   TA1:   r1[x   ],                                  w1[x ] ________,  c1
             ∙   TA2:               R   2[x   ],     w2[x   ],    c2
      2nd   s2:              R2[x   ] ,                           w2[x   ],    c2, r1[x   ],           w1[x   ],      c1
             ∙   TA1:                   r 1[x ]______________,    w                  1[x   ],      c1
             ∙   TA2:    R      2[x   ] ,                           w2[x   ],    c2
 35   1/ 7   51                          Geral  d Webe r's  TA Ma nag ement   Slid es                                         12
````

### 图片文字 OCR（en-US，待对照原页）

````text
On Isolation Level READ COMMITTED
Can the following transactions run into a deadlock ?
, TAI: rl[x],
, TA2: R2[x], W2[x],
Still No. But different timing for alternative 1 on
isolation level READ COMMITTED
, First
2nd
351/751
sl:
, TAI:
, TA2:
s2:
, TAI:
TA2:
rl[x], R2[x], W2[x], cl
rl[X],
R2[x], W2[x],
R2[x] ,
R2[x]
Wl[x],
Wl[x],
Gerald Weber's TA Management Slides
12
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../../source/751/751%2525/DB51_2025_IsoLevels.pdf#page=13)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 13
On Isolation Level READ COMMITTED
• Can the following transactions run into a deadlock ?
∙ TA1: r1[x], w1[x], c1
∙ TA2: R2[x], w2[x], c2
• Still No. But different timing for alternative 1 on
isolation level READ COMMITTED
• First s1: r1[x], R2[x], w2[x], c2, w1[x], c1 lost update!
∙ TA1: r1[x], w1[x] ________, c1
∙ TA2: R2[x], w2[x], c2
 2nd s2: R2[x] , w2[x], c2, r1[x], w1[x], c1
∙ TA1: r1[x]______________, w1[x], c1
∙ TA2: R2[x] , w2[x], c2
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
On Isolation Level READ COMMITTED
•   Can the following transactions r un i  nto a deadlock                                                    ?
             ∙   TA1:   r    1[x   ],          w1[x   ],    c1
             ∙   TA2:   R     2[x   ],      w2[x   ],    c2
•   Still N  o.       But different timing for alternative 1 on
    isolation level   R  EAD COM MIT TE D
•   F irst    s1:            r1[x   ], R2[x   ], w2[x], c2, w1[ x],     c1       lost  updat e!
             ∙   TA1:   r    1[x   ],                                  w1[x ] ________,  c1
             ∙   TA2:               R   2[x   ],     w2[x   ],    c2
      2nd   s2:              R2[x   ] ,                           w2[x   ],    c2, r1[x   ],           w1[x   ],      c1
             ∙   TA1:                   r 1[x ]______________,    w                 1[x   ],      c1
             ∙   TA2:    R     2[x   ] ,                           w2[x   ],    c2
 35   1/ 7   51                         Geral  d Webe r's  TA Ma nag ement   Slid es                                         13
````

### 图片文字 OCR（en-US，待对照原页）

````text
On Isolation Level READ COMMITTED
Can the following transactions run into a deadlock ?
, TAI: rl[x],
, TA2: R2[x], W2[x],
Still No. But different timing for alternative 1 on
isolation level READ COMMITTED
, First
2nd
351/751
sl:
, TAI:
, TA2:
s2:
, TAI:
TA2:
WAX], WI [X], cl
rl[x], R2[x],
lost update!
rl[X],
R2[x], W2[x],
R2[x] ,
R2[x]
Wl[x],
Wl[x],
Gerald Weber's TA Management Slides
13
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../../source/751/751%2525/DB51_2025_IsoLevels.pdf#page=14)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 14
Phenomenon: Dirty read
• Transaction TA2 performs a dirty read if it reads an 
uncommitted write result of TA1
∘ scheduling example: ........ w1[x], r2[x], 
• Dirty reads can happen, if transaction TA2 does not react to 
a write-lock on x. 
• Dirty reads might be no problem for: 
∘ transactions that gather overview data
∘ transactions that investigate options for later transactions
• But they are dangerous for other transactions
∘ might lead to inconsistent results.
• Isolation level READ UNCOMMITTED allows dirty reads, but 
the transactions have to be read-only.
dirty read
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Phenomenon: Dir ty  read
• T ransaction T A2  per form s a dirty read if it r eads an
  uncomm itted write result of T A1
    ∘  schedul  ing exam pl  e:  ........ w  1[x], r2[x],               dirty read
• Dir ty reads can happen, if transaction T A2 does not r eact to
  a write   -lock on x.
• Dir ty reads mi  ght be no problem  for :
    ∘  tr ansactions that gather overview data
    ∘  tr ansactions that investi  gate options for later transactions
• But they ar e dangerous for  other  transactions
    ∘  m ight lead to inconsistent r esults.
• Isolation level RE AD UNCOM M IT TE  D allows dirty r eads, but
  the tr ansactions have to be r ead              -only.
35   1/ 7   51               Geral  d Webe r's  TA Ma nag ement   Slid es                14
````

### 图片文字 OCR（en-US，待对照原页）

````text
Phenomenon: Dirty read
• Transaction TA2 performs a dirty read if it reads an
uncommitted write result of TAI
o scheduling example:
dirty read
WI [x], r2[x],
• Dirty reads can happen, if transaction TA2 does not react to
a write-lock on x.
• Dirty reads might be no problem for:
o transactions that gather overview data
o transactions that investigate options for later transactions
• But they are dangerous for other transactions
o might lead to inconsistent results.
Isolation level READ UNCOMMITTED allows dirty reads, but
the transactions have to be read-only.
351/751
Gerald Weber's TA Management Slides
14
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../../source/751/751%2525/DB51_2025_IsoLevels.pdf#page=15)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 15
Dirty read on second read is not a fuzzy read
• a case, where a transaction reads two different values for 
x, but one of them is a dirty value:
r1[x], r2[x], w2[x], r1[x], w2[y], c1
• This is a dirty read and not a fuzzy read.
• The new value is not committed, so it is really no fuzzy 
read: Remember the definition:
• Transaction TA1 encounters a fuzzy read phenomenon if 
it reads two or more different committed values for x.
New, dirty value of x
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Dir ty  read on second read is  not a fuzzy  r ead
• a case, where a transaction reads two different val  ues for
  x, but one of them is a di  rty value:
         r1[x], r 2[x], w  2[x], r1[x], w  2[y], c 1
                                                   New, dirty value of x
• T hi  s i  s a dirty read and not a fuzzy r ead.
• T he new value is not committed, so it i  s really no fuzzy
  read: Remember the definition:
• T ransaction T A1  encounters a               fuzzy read       phenom enon if
  it reads two or m ore         different    committed       values for  x.
35   1/ 7   51              Geral  d Webe r's  TA Ma nag ement   Slid es                15
````

### 图片文字 OCR（en-US，待对照原页）

````text
Dirty read on second read is not a fuzzy read
a case, where a transaction reads two different values for
x, but one of them is a dirty value:
rl r2[x], WAX], rl WAY],
New, dirty value of x
This is a dirty read and not a fuzzy read.
The new value is not committed, so it is really no fuzzy
read: Remember the definition:
Transaction TAI encounters a fuzzy read phenomenon if
it reads two or more different committed values for x.
351/751
Gerald Weber's TA Management Slides
15
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../../source/751/751%2525/DB51_2025_IsoLevels.pdf#page=16)

### 原始文字层

````text
351/751 Gerald Weber's TA Management Slides 16
phantom
• A phantom (row) is a phenomenon possible in the relational 
data model, but goes beyond the basic read/write model.
• Are caused by relational inserts, not by updates.
• The following situation describes a phantom row:
∘ TA1 performs: SELECT * FROM mytabl 
∙ gets a result set res1.
∘ TA2 : inserts a row r into mytabl and commits.
∘ TA1 performs again SELECT * FROM mytabl
∙ gets a different result set res2 = res1 ∪ {r} 
∘ the row r is the phantom for TA1
• Considered less serious and hard to avoid with locks.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
phantom
• A phantom (row) is a phenomenon possible in the r el  ational
  data m odel  , but goes beyond the basic r ead/write model.
• Are caused by relational inserts, not by updates.
• T he following situation describes a phantom r ow:
    ∘  T A1 perform s: SELEC  T * F ROM m ytabl
         ∙  gets  a result s et res1.
    ∘  T A2 : inserts a r ow r into mytabl and com mits.
    ∘  T A1 performs again SE  LECT  *  FROM  mytabl
         ∙  gets  a different result  set  res 2 =  res 1  ∪  {r}
    ∘  the row r i  s the phantom for T A1
• Considered less serious and hard to avoi  d wi  th locks.
35   1/ 7   51              Geral  d Webe r's  TA Ma nag ement   Slid es                 16
````

### 图片文字 OCR（en-US，待对照原页）

````text
phantom
A phantom (row) is a phenomenon possible in the relational
data model, but goes beyond the basic read/write model.
Are caused by relational inserts, not by updates.
The following situation describes a phantom row:
o TAI performs: SELECT * FROM mytabl
gets a result set resl.
o TA2 : inserts a row r into mytabl and commits.
o TAI performs again SELECT * FROM mytabl
gets a different result set res2 = resl u {r}
o the row r is the phantom for TAI
Considered less serious and hard to avoid with locks.
351/751
Gerald Weber's TA Management Slides
16
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../../source/751/751%2525/DB51_2025_IsoLevels.pdf#page=17)

### 原始文字层

````text
Summary 
• We have seen the following bad phenomena of reduced 
isolation: phantom, fuzzy read, lost update, dirty read.
• They are increasingly serious.
• The ANSI phenomena appear in increasingly relaxed 
isolation levels: SERIALIZABLE, REPEATABLE READ, 
READ COMMITTED, READ UNCOMMITTED.
• The first level SERIALIZABLE allows no phenomenon, the 
last level READ UNCOMMITTED allows dirty read, fuzzy 
read and phantom phenomena.
• DB start on level REPEATABLE READ, on level READ 
COMMITTED, lost updates can be prevented with R[ ].
351/751 Gerald Weber's TA Management Slides 17
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Summary
• We have seen the following bad phenomena of reduced
  isolation: phantom, fuzzy r ead, lost update, dirty read.
• T hey are increasingl  y serious.
• T he AN  SI phenomena appear i  n increasingl  y relaxed
  isolation level  s: S  ERIALIZA BLE, REP EAT AB LE  READ  ,
  RE AD COMMIT TED  , RE AD UNC  OMMITT ED.
• T he first l  evel S  ERIALIZA BLE allows no phenomenon, the
  last level READ   U  NCOMMITT ED allows dirty read, fuzzy
  read and phantom phenomena.
• DB  start on level REP EAT ABLE  R  EAD, on level   R  EAD
  COM MIT TE D, l  ost updates can be prevented wi  th R[ ].
35   1/ 7   51           Geral  d Webe r's  TA Ma nag ement   Slid es           17
````

### 图片文字 OCR（en-US，待对照原页）

````text
Summary
We have seen the following bad phenomena of reduced
isolation: phantom, fuzzy read, lost update, dirty read.
They are increasingly serious.
The ANSI phenomena appear in increasingly relaxed
isolation levels: SERIALIZABLE, REPEATABLE READ,
READ COMMITTED, READ UNCOMMITTED.
The first level SERIALIZABLE allows no phenomenon, the
last level READ UNCOMMITTED allows dirty read, fuzzy
read and phantom phenomena.
, DB start on level REPEATABLE READ, on level READ
COMMITTED, lost updates can be prevented with RI l.
351/751
Gerald Weber's TA Management Slides
17
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

