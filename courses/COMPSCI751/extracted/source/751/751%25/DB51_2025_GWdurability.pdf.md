# DB51_2025_GWdurability.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI751/source/751/751%25/DB51_2025_GWdurability.pdf`
- [打开原文件](../../../../source/751/751%2525/DB51_2025_GWdurability.pdf)
- 原文件 SHA-256：`f75fa5142958309fd75ca1ec71656ee925490ecde9eb5440716488bdea497d7b`
- 文件索引：F114；PDF 总页数：23
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../source/751/751%2525/DB51_2025_GWdurability.pdf#page=1)

### 原始文字层

````text
ACID durability
• write ahead logging
• buffer management
• steal, no-force strategies
• checkpoints
• media recovery
351/751 Transaction Processing 1
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
ACID durabil ity
  •  write ahead logging
  •  buffer management
  •  steal, no-force strategies
  •  checkpoi  nts
  •  medi  a r ecovery
  35   1/ 7   51                        Tr    ans   act i    on  P   roc   ess   i ng               1
````

### 图片文字 OCR（en-US，待对照原页）

````text
ACID durability
write ahead logging
buffer management
steal, no-force strategies
checkpoints
media recovery
351/751
Transaction Processing
1
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../source/751/751%2525/DB51_2025_GWdurability.pdf#page=2)

### 原始文字层

````text
351/751 Transaction Processing 2
The ACID properties
• requirements that a transaction manager must meet for the 
transactions:
∘ Atomicity: either all the operations of a transaction are 
made durable or none of them are. 
∘ Consistency: after the transaction, the database is in a 
consistent state.
∘ Isolation: operations in a transaction appear isolated 
from all other operations. Transactions have a virtual 
serial view on the system. 
∘ Durability: once the user has been notified of success, 
the transaction will persist, and not be undone.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
The A CID properties
• requirements that a transaction m anager must meet for the
  tr ansactions:
    ∘  Atom icit y    : either all the operations of a transaction are
       m ade durable or none of them  are.
    ∘  Co nsisten cy      : after the transaction, the database is in a
       consistent state.
    ∘  Isolation:  operati  ons in a transacti  on appear isolated
       fr om all other operations. T ransactions have a virtual
       serial view on the system.
    ∘  Du rabilit y: once the user has been notified of success,
       the tr ansaction will   persist, and not be undone.
35   1/ 7   51                    Tr    ans   act i    on  P   roc   ess   i ng       2
````

### 图片文字 OCR（en-US，待对照原页）

````text
The ACID properties
requirements that a transaction manager must meet for the
transactions:
Atomicity: either all the operations of a transaction are
made durable or none of them are.
Consistency: after the transaction, the database is in a
consistent state.
Isolation:
operations in a transaction appear isolated
from all other operations. Transactions have a virtual
serial view on the system.
Qurability: once the user has been notified of success,
the transaction will persist, and not be undone.
351/751
Transaction Processing
2
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../source/751/751%2525/DB51_2025_GWdurability.pdf#page=3)

### 原始文字层

````text
351/751 Transaction Processing 3
ACID durability
• Once the user has been notified of success of transaction t:
a) All writes of t are permanent: must be changed through 
later committed writes, e.g., compensating transactions.
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
ACID  durabil ity
• Once the user has been notified of success of transaction t:
a)   Al  l wri  tes of t are permanent: must be changed through
     later commi  tted writes, e.g., compensating transactions.
b)   T he effect of t is kept in a crash resistant way.
    ∘  minimum r equirement: transacti  on is written to
       persi  stent storage: r esistant against
         ∙  OS crash
         ∙  sy stem  out age
c)   preferred: protection against l  oss of persistent memory:
         1.   Res istance against  pers istent  storage  failure
         2.   resist anc e agains t c at astrophes , geographic  distribution
35   1/ 7   51                     Tr    ans   act i    on  P   roc   ess   i ng          3
````

### 图片文字 OCR（en-US，待对照原页）

````text
ACID durability
Once the user has been notified of success of transaction t:
a) All writes of t are permanent: must be changed through
later committed writes, e.g., compensating transactions.
b) The effect of t is kept in a crash resistant way.
o minimum requirement: transaction is written to
persistent storage: resistant against
OS crash
system outage
c) preferred: protection against loss of persistent memory:
1. Resistance against persistent storage failure
2. resistance against catastrophes, geographic distribution
351/751
Transaction Processing
3
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../source/751/751%2525/DB51_2025_GWdurability.pdf#page=4)

### 原始文字层

````text
351/751 Transaction Processing 4
System architecture
server with
database management system
stable 
database
stable 
Log
log buffer
database
buffer 
transaction
manager
Database
database Clients
clients
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
System architecture
                                     serve  r w  ith                                                           stabl  e
                                     da  ta  base   ma  nag  emen  t system                                  da  ta  base
     Da ta base
        da ta baseCl   ien   ts       transa cti  on                   da ta base
           cli  ents                    man  age  r                      bu  ffer
                                                                      lo   g  buf f er
                                                                                                                 stabl  e
                                                                                                                   Lo   g
35   1/ 7   51                                       Tr    ans   act i    on  P   roc   ess   i ng                                       4
````

### 图片文字 OCR（en-US，待对照原页）

````text
System architecture
database
clients
351/751
server With
database management system
transaction
database
manager
buffer
log buffer
Transaction Processing
stable
database
stable
Log
4
````

### 图表辅助说明

数据库架构图：客户端请求进入事务管理器，再分别进入 database buffer 与 log buffer；两条独立箭头指向 stable database 与 stable log，表示数据页和日志各自有持久存储路径。

## PDF 第 5 页

[查看此页](../../../../source/751/751%2525/DB51_2025_GWdurability.pdf#page=5)

### 原始文字层

````text
351/751 Transaction Processing 5
Structure of the database
• Database buffer and stable database 
content is partitioned into pages.
• Every buffer page has exactly one 
image page on the stable database.
• Complete pages are read from and 
written to the stable database on disk.
∘ must be read when not yet in buffer.
• buffer is fast, stable database is vast.
• Difference in access time: RAM: 1ns, 
disk 1ms; ratio? SSD?
x 78 z 54
y 89
database 
pages 
object name value
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Str  uc ture of the databas e
• Database buffer and stable database                           database
  content is partitioned i  nto pages.                                             pages
• Every buffer page has exactly one
  im age page on the stable database.                              x   78     z  54
• Complete pages are read fr om and
  written to the stable database on di  sk.
    ∘  m ust be read when not yet in buffer.
• buffer is fast, stabl  e database is vast.                             y   89
• Difference in access time: R  AM: 1ns,
  disk 1ms; rati  o? SS D?
                                                            object  name       value
35   1/ 7   51                    Tr    ans   act i    on  P   roc   ess   i ng          5
````

### 图片文字 OCR（en-US，待对照原页）

````text
Structure of the database
Database buffer and stable database
content is partitioned into pages.
Every buffer page has exactly one
image page on the stable database.
Complete pages are read from and
written to the stable database on disk.
o must be read when not yet in buffer.
buffer is fast, stable database is vast.
Difference in access time: RAM: Ins,
disk lms; ratio? SSD?
database
x
78
pages
z 54
Y 89
351/751
object name
Transaction Processing
value
5
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../source/751/751%2525/DB51_2025_GWdurability.pdf#page=6)

### 原始文字层

````text
351/751 Transaction Processing 6
Crash recovery: write ahead logging 1 
• A log has a log buffer in main memory and a stable log on 
persistent storage.
• Semantics of a system crash: At an arbitrary point in time, 
database buffer as well as log buffer are lost.
• Recovery must be based on stable log and stable database 
alone.
• A transaction is conceived as committed only after the 
commit entry of this transaction is written to the persistent 
and reliable log file storage: write ahead logging (WAL).
∘ Crucial part of durability.
• Main policy/semantics of database crash recovery: 
The stable log is authoritative.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Crash rec ov er  y: wr  ite ahead loggi ng 1
• A log has a      log buffer    in mai   n memor y and a        stable l   og on
  persi  stent storage.
• Semanti  cs of a system cr ash: At an arbitrary point in time,
  database buffer as well as log buffer are l  ost.
• Recovery m ust be based on stable log and stabl  e database
  alone.
• A transaction is conceived as committed only after the
  commit entry of this transaction is written to the persistent
  and reliable log fil  e storage: write ahead logging ( WAL).
    ∘  Crucial    part of durability.
• Main policy/semantics of database crash recovery:
  The stable l  og is authoritative.
35   1/ 7   51                   Tr    ans   act i    on  P   roc   ess   i ng       6
````

### 图片文字 OCR（en-US，待对照原页）

````text
Crash recovery: write ahead logging 1
A log has a log buffer in main memory and a stable log on
persistent storage.
Semantics of a system crash: At an arbitrary point in time,
database buffer as well as log buffer are lost.
Recovery must be based on stable log and stable database
alone.
A transaction is conceived as committed only after the
commit entry of this transaction is written to the persistent
and reliable log file storage: write ahead logging (WAL).
o Crucial part of durability.
Main policy/semantics of database crash recovery:
The stable log is authoritative.
351/751
Transaction Processing
6
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../../source/751/751%2525/DB51_2025_GWdurability.pdf#page=7)

### 原始文字层

````text
351/751 Transaction Processing 7
Crash recovery: stable log is authoritative
• The stable log decides about the correct status of 
transactions:
∘ Committed transactions are exactly those that have a 
commit record in the stable log because of write ahead 
logging. They are winners and considered committed: 
crash-durability.
∘ Other transactions (without a commit record in the 
stable log) are losers and considered aborted.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Crash rec ov er  y: stabl e l og is  authori tativ e
• T he stable l  og decides about the correct status of
  tr ansactions:
    ∘  Com mi  tted transactions are exactly those that have a
       com mit record in the stabl  e log because of w  rite ahead
       logging. T hey are         winners      and considered com mitted:
       cr ash   -durabili  ty.
    ∘  Other transactions (without a commit record in the
       stable l  og) are      losers    and considered aborted.
35   1/ 7   51                     Tr    ans   act i    on  P   roc   ess   i ng           7
````

### 图片文字 OCR（en-US，待对照原页）

````text
Crash recovery: stable log is authoritative
The stable log decides about the correct status of
transactions:
o Committed transactions are exactly those that have a
commit record in the stable log because of write ahead
logging. They are winners and considered committed:
crash-durability.
o Other transactions (without a commit record in the
stable log) are losers and considered aborted.
351/751
Transaction Processing
7
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../../source/751/751%2525/DB51_2025_GWdurability.pdf#page=8)

### 原始文字层

````text
351/751 Transaction Processing 8
Goal of crash recovery: clean stable database
• The stable database is clean iff the stable database is 
consistent with the winner/loser decision of the stable log.
• All writes of the winners, and only the writes of the winners 
are reflected in the stable database.
• The log entries of uncommitted transactions must be 
without effect.
• Task of crash recovery: The stable database must be made 
clean based on the stable log.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Goal of c ras h recovery : c lean stabl e database
• T he stable database is            clean    iff the stable database i  s
  consistent with the wi  nner/loser decision of the stable log.
• Al  l wri  tes of the winners, and only the w  rites of the winners
  are r eflected in the stable database.
• T he log entr ies of uncommitted tr ansactions m ust be
  without effect.
• T ask of crash r ecovery: T he stable database m ust be m ade
  clean based on the stable log.
35   1/ 7   51                     Tr    ans   act i    on  P   roc   ess   i ng          8
````

### 图片文字 OCR（en-US，待对照原页）

````text
Goal of crash recovery: clean stable database
The stable database is clean iff the stable database is
consistent with the winner/loser decision of the stable log.
All writes of the winners, and only the writes of the winners
are reflected in the stable database.
The log entries of uncommitted transactions must be
without effect.
Task of crash recovery: The stable database must be made
clean based on the stable log.
351/751
Transaction Processing
8
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../../source/751/751%2525/DB51_2025_GWdurability.pdf#page=9)

### 原始文字层

````text
351/751 Transaction Processing 9
Remark: media recovery
• Addresses a much more severe failure situation, but is 
semantically simple:
• Addresses the situation that the stable database is lost by 
media failure, i.e., Hard disk crash, catastrophes.
• Important semantic specification: The clean stable 
database can be reconstructed at any point in time:
∘ from the complete stable log : Redo all transactions!
∘ from a historic clean stable database copy and the 
stable log from that point in time: media recovery.
• Ergo: For media recovery, log must be independently 
durable on every commit! Backups for stable database!
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Remark: media recovery
• Addresses a m uch m ore severe failure situation, but i  s
  semantically simple:
• Addresses the situation that the stable database is lost by
  m edi  a failure, i.e., Hard disk crash, catastr ophes.
• Im portant sem antic specification: T he clean stable
  database can be reconstructed at any point in time:
    ∘  fr om the complete stable l  og : Redo all transactions!
    ∘  fr om  a hi  storic clean stable database copy and the
       stable l  og from  that point i  n tim e:        m edi  a r ecovery.
• Ergo: F or m edia recovery, log must be independently
  durable on every com m it!  B  ackups for stable database!
35   1/ 7   51                    Tr    ans   act i    on  P   roc   ess   i ng          9
````

### 图片文字 OCR（en-US，待对照原页）

````text
Remark: media recovery
Addresses a much more severe failure situation, but is
semantically simple:
Addresses the situation that the stable database is lost by
media failure, i.e., Hard disk crash, catastrophes.
Important semantic specification: The clean stable
database can be reconstructed at any point in time:
o from the complete stable log : Redo all transactions!
o from a historic clean stable database copy and the
stable log from that point in time: media recovery.
Ergo: For media recovery, log must be independently
durable on every commit! Backups for stable database!
351/751
Transaction Processing
9
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../source/751/751%2525/DB51_2025_GWdurability.pdf#page=10)

### 原始文字层

````text
351/751 Transaction Processing 10
Media recovery contd.
• Media recovery: takes place, if stable database is lost.
∙ Remark: Loss of the log cannot be repaired
∙ highly reliable store is used for log.
• Requires proper archiving:
∘ Log is kept long-term, even after truncation.
∘ All log entries are stored in a log archive.
∘ From time to time, database backups are made from the 
stable database.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Media recovery contd.
•  Medi  a r ecovery: takes place, i  f stable database is lost.
          ∙  Remark:  Loss  of t he  log  cannot  be repaired
          ∙  highly reliable  store is  used for log.
•  Requires proper archiving:
     ∘  Log i  s kept long       -term, even after  truncation.
     ∘  Al  l log entri  es are stored in a           log archive       .
     ∘  F rom  ti  me to time,        database backups              are m ade from the
        stable database.
35   1/ 7   51                       Tr    ans   act i    on  P   roc   ess   i ng             10
````

### 图片文字 OCR（en-US，待对照原页）

````text
Media recovery contd.
Media recovery: takes place, if stable database is lost.
Remark: Loss of the log cannot be repaired
highly reliable store is used for log.
Requires proper archiving:
o Log is kept long-term, even after truncation.
o All log entries are stored in a log archive.
o From time to time, database backups are made from the
stable database.
351/751
Transaction Processing
10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../source/751/751%2525/DB51_2025_GWdurability.pdf#page=11)

### 原始文字层

````text
351/751 Transaction Processing 11
Database buffer management
• The buffer is a write cache: Changes to the data in the 
buffer are not immediately written to the stable database. 
• Database buffer management: 
∘ if a cache miss occurs, load requested pages. This 
means, old pages must be replaced.
∘ Pages with changes need to be written back.
∘ We have to distinguish committed changes and 
uncommitted changes.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Databas e buffer management
• T he buffer is a w  rite cache: Changes to the data in the
  buffer are not immedi  ately written to the stable database.
• Database buffer management:
    ∘  if a cache m iss occurs, load r equested pages. T his
       m eans, old pages must be replaced.
    ∘  Pages with changes need to be written back.
    ∘  We have to distinguish com mitted changes and
       uncomm itted changes.
35   1/ 7   51                   Tr    ans   act i    on  P   roc   ess   i ng      11
````

### 图片文字 OCR（en-US，待对照原页）

````text
Database buffer management
The buffer is a write cache: Changes to the data in the
buffer are not immediately written to the stable database.
Database buffer management:
o if a cache miss occurs, load requested pages. This
means, old pages must be replaced.
o Pages with changes need to be written back.
o We have to distinguish committed changes and
uncommitted changes.
351/751
Transaction Processing
11
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../source/751/751%2525/DB51_2025_GWdurability.pdf#page=12)

### 原始文字层

````text
351/751 Transaction Processing 12
Crash recovery challenges
• Database buffer management can be aligned in different 
ways to transactions. 
• Easiest situation: Stable database is always clean. 
Unfortunately, this will turn out to be not practical.
• Alternative, more complex situations:
∘ The stable database can contain pages with the 
following problems:
1. Old data not reflecting writes by committed 
transactions:
an outdated (stale) page.
2. writes by uncommitted transactions: A steal page.
∘ Both kinds of problems can appear on the same page.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Crash rec ov er y chal lenges
• Database buffer management can be al  igned in different
  ways to tr ansactions.
• Easiest situati  on    : Stable database i  s alw  ays clean.
  Unfortunatel  y, this will   turn out to be not practical.
• Al  ternati  ve, more complex situations:
    ∘  T he stable database can contain pages with the
       following problems:
         1.  Old data not reflecti  ng writes by commi  tted
             transactions:
             an outdated (stal  e) page.
         2.  writes by uncommitted transactions: A steal page.
    ∘  Both kinds of problems can appear on the same page.
35   1/ 7   51                   Tr    ans   act i    on  P   roc   ess   i ng     12
````

### 图片文字 OCR（en-US，待对照原页）

````text
Crash recovery challenges
Database buffer management can be aligned in different
ways to transactions.
Easiest situation: Stable database is always clean.
Unfortunately, this will turn out to be not practical.
Alternative, more complex situations:
o The stable database can contain pages with the
following problems:
1. Old data not reflecting writes by committed
transactions:
an outdated (stale) page.
2. writes by uncommitted transactions: A steal
page.
o Both kinds of problems can appear on the same page.
351/751
Transaction Processing
12
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../../source/751/751%2525/DB51_2025_GWdurability.pdf#page=13)

### 原始文字层

````text
351/751 Transaction Processing 13
Buffer management policy alternatives 
• Policies for buffer pages with committed write.
∘ force: At commit, such pages have to be written to the 
stable database. Leads to performance bottlenecks.
∘ no-force: drops this requirement. Leads to redo.
• Policies for buffer pages with uncommitted write 
∘ no-steal: Such pages must not be written to stable 
database. Can lead to buffer bottlenecks.
∘ steal: drops this requirement. Leads to undo.
• Force, no-steal is easy crash recovery, ensures the stable 
database is always clean: not practical enough.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Buffer management pol ic y al ter nativ es
• Poli  cies for buffer pages w  ith commi  tted write.
    ∘  force: At commit, such pages have to be wri  tten to the
       stable database.  Leads to performance bottl  enecks.
    ∘  no-force: drops thi  s requirement. Leads to redo.
• Poli  cies for buffer pages w  ith uncommitted w  rite
    ∘  no-steal: Such pages must not be written to stable
       database. Can lead to buffer bottlenecks.
    ∘  steal: drops thi  s requirement. Leads to undo.
• F orce, no-steal is easy cr ash r ecovery, ensures the stabl  e
  database is always clean: not practi  cal   enough.
35   1/ 7   51                   Tr    ans   act i    on  P   roc   ess   i ng     13
````

### 图片文字 OCR（en-US，待对照原页）

````text
Buffer management policy alternatives
Policies for buffer pages with committed write.
o force: At commit, such pages have to be written to the
stable database. Leads to performance bottlenecks.
o no-force: drops this requirement. Leads to redo.
Policies for buffer pages with uncommitted write
o no-steal: Such pages must not be written to stable
database. Can lead to buffer bottlenecks.
o steal: drops this requirement. Leads to undo.
Force, no-steal is easy crash recovery, ensures the stable
database is always clean: not practical enough.
351/751
Transaction Processing
13
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../../source/751/751%2525/DB51_2025_GWdurability.pdf#page=14)

### 原始文字层

````text
351/751 Transaction Processing 14
Crash recovery challenges
• The stable database can contain pages with the following 
problems:
1. Old data not reflecting writes by committed 
transactions:
an outdated (stale) page.
-> no-force
2. writes by uncommitted transactions: A steal page.
-> steal
• Note: no-steal requires some kind of page lock: we need to 
get all open transactions off a page to write it back under 
no-steal policy. Page locks are a performance issue.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Crash rec ov er y chal lenges
• T he stable database can contain pages with the following
  problem s:
    1.   Old data not r eflecti  ng writes by commi  tted
         tr ansactions:
         an outdated (stal  e) page.
          ->  no-force
    2.   writes by uncommitted tr ansactions: A steal page.
          ->  steal
• Note: no-steal requires some kind of page lock: we need to
  get all   open transacti  ons off  a page to wri  te it back under
  no-steal poli  cy. P  age locks are a performance issue.
35   1/ 7   51                   Tr    ans   act i    on  P   roc   ess   i ng       14
````

### 图片文字 OCR（en-US，待对照原页）

````text
Crash recovery challenges
The stable database can contain pages with the following
problems:
1. Old data not reflecting writes by committed
transactions:
an outdated (stale) page.
no-force
2. writes by uncommitted transactions: A steal
page.
steal
Note: no-steal requires some kind of page lock: we need to
get all open transactions off a page to write it back under
no-steal policy. Page locks are a performance issue.
351/751
Transaction Processing
14
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../../source/751/751%2525/DB51_2025_GWdurability.pdf#page=15)

### 原始文字层

````text
351/751 Transaction Processing 15
Buffer management: no-force, steal policy
• Algorithms for Recovery and Isolation Exploiting Semantics
(ARIES) [Mohan et al. 1992]
• Is today’s preferred solution: no alignment between buffer 
page swapping and transactions: no-force, steal policy:
∘ A full write cache delivering durability!
• Buffer pages are swapped according to demand.
• Avoids more bottlenecks, more difficult to implement.
• no-force:, some committed writes are not in the stable 
database yet. Makes redo after crash necessary.
• steal: some uncommitted writes are in the stable database: 
undo also after crash.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Buffer management: no                     -force, s teal poli cy
• Al  gorithms for R  ecovery and Isolati  on Exploiting Semantics
  (AR  IE  S) [Mohan et al. 1992]
• Is today’s    preferred solution: no alignment between buffer
  page swapping and transactions: no-for ce, steal p olicy:
    ∘  A f ull writ e cache delivering  du rab ility!
• Buffer pages are swapped according to demand.
• Avoids m ore bottlenecks, more difficult to i  mplement.
• no-force:, some committed writes are not in the stable
  database yet. Makes r edo after cr ash necessary.
• steal: some uncommitted writes are in the stabl  e database:
  undo also after crash.
35   1/ 7   51                  Tr    ans   act i    on  P   roc   ess   i ng   15
````

### 图片文字 OCR（en-US，待对照原页）

````text
Buffer management: no-force, steal policy
Algorithms for Recovery and Isolation Exploiting Semantics
(ARIES) [Mohan et al. 1992]
Is today's preferred solution: no alignment between buffer
page swapping and transactions: no-force, steal policy:
A full write cache delivering durability!
Buffer pages are swapped according to demand.
Avoids more bottlenecks, more difficult to implement.
no-force:, some committed writes are not in the stable
database yet. Makes redo after crash necessary.
steal: some uncommitted writes are in the stable database:
undo also after crash.
351/751
Transaction Processing
15
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../../source/751/751%2525/DB51_2025_GWdurability.pdf#page=16)

### 原始文字层

````text
351/751 Transaction Processing 16
Write ahead logging 2 for steal
• enabling crash recovery for steal policy: 
• stable database pages are changed by loser transactions.
• the information to undo the loser transactions must be in 
the log.
• Therefore, 
∘ before a buffer page is written back to the stable 
database:
∘ all log entries for that page have to be written back to 
the stable log.
• This is another application of write ahead logging.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Wr ite ahead loggi ng 2     for steal
• enabl  ing cr ash recovery for steal pol  icy:
• stable database pages are changed by loser transactions.
• the i  nformation to undo the loser transactions must be in
  the l  og.
• T herefore,
     ∘  before a buffer page is written back to the stable
        database:
     ∘  all log entr ies for that page have to be wri  tten back to
        the stable log.
• T hi  s i  s another appl  icati  on of      write ahead logging           .
35   1/ 7   51                      Tr    ans   act i    on  P   roc   ess   i ng          16
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write ahead logging 2 for steal
enabling crash recovery for steal policy:
stable database pages are changed by loser transactions.
the information to undo the loser transactions must be in
the log.
Therefore,
o before a buffer page is written back to the stable
database:
o all log entries for that page have to be written back to
the stable log.
This is another application of write ahead logging.
351/751
Transaction Processing
16
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../../source/751/751%2525/DB51_2025_GWdurability.pdf#page=17)

### 原始文字层

````text
351/751 Transaction Processing 17
Recovery example, the scenario 
• Example log using implicit 
transaction start, no BOT.
• When was the last time a page 
was written out.
Stable log
[nr: 110, ta: 22, obj: x, b: 91, a: 78]
[nr: 111, ta: 23, obj: z, b: 23, a: 54]
[nr: 112, ta: 22, obj: x, b: 78, a: 53]
[nr: 113, ta: 22, obj: y, b: 89, a: 64]
[nr: 114, ta: 22, commit]
[nr: 116, ta: 23, obj: y, b: 64, a: 85]
[nr: 116, ta: 23, obj: z, b: 54, a: 37]
 log buffer
x 78 z 54
y 89
Stable database 
o
before after
pt
r out.hu
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Recovery example, the scenari o
•   Exam ple log              using       implicit                          Stable database
    tr ansaction          start, no B  OT.                                        x    78       z   54
•   When was the last time a page
    was written out.                                                                      y   89o
                                     before     Stable     log
    [nr:  110,  ta:  22,    obj:  x,  b: 91,  a:  78]after
    [nr:  111,  ta:  23,  obj:  z,  b: 23,  a:  54]                              out.hu
    [nr:  112,  ta:  22,    obj:  x,  b: 78,  a:  53]             r
    [nr:  113,  ta:  22,  obj:  y,  b: 89,  a:  64]pt
    [nr:  114,  ta:  22,    comm it     ]
    [nr:  116,  ta:  23,    obj:  y,  b: 64,  a:  85]
    [nr:  116,  ta:  23,  obj: z,  b:      54,  a: 37]
                                                                                                    log buffer
35   1/ 7   51                               Tr    ans   act i    on  P   roc   ess   i ng                         17
````

### 图片文字 OCR（en-US，待对照原页）

````text
Recovery exarnple, the scenario
111, ta:
Stable database
Example log using implicit
transaction start, no BOT.
• When was the last time a page
was written out.
x 78 z 54
Y 89
[nr: 110, ta:
[nr:
[nr: 112, ta:
[nr: 113, ta:
114,
[nr: 116, ta:
[nr: 116, ta:
351/751
SFPle log
91, a: 78]
22, obj: x, b:
23, obj: z, b: 23, a 54
22, obj: x, b:
a: 53]
22, obj: y, b: 89
a: 64]
22, commit]
23, obj: y, b:
64, a: 85]
23, obj: z, b:
54, a: 37]
log buffer
Transaction Processing
17
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 18 页

[查看此页](../../../../source/751/751%2525/DB51_2025_GWdurability.pdf#page=18)

### 原始文字层

````text
351/751 Transaction Processing 18
Recovery example, the scenario 
• Situation at the time of the crash.
• Database buffer is then lost.
• Writes are shown on top of old 
values.
Stable log
[nr: 110, ta: 22, obj: x, b: 91, a: 78]
[nr: 111, ta: 23, obj: z, b: 23, a: 54]
[nr: 112, ta: 22, obj: x, b: 78, a: 53]
[nr: 113, ta: 22, obj: y, b: 89, a: 64]
[nr: 114, ta: 22, commit]
[nr: 116, ta: 23, obj: y, b: 64, a: 85]
[nr: 116, ta: 23, obj: z, b: 54, a: 37]
 log buffer
x 78 z 54
y 89
Stable database
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Recovery example, the scenari o
•   Si  tuation at the time of the crash.                                     Stable database
•   Database buffer is then lost.                                                    x    78       z    54
•   Writes are show  n on top of ol  d
    values.                                                                                  y   89
                                                  Stable     log
    [nr:  110,  ta:  22,     obj:  x,  b: 91,  a:  78]
    [nr:  111,  ta:  23,  obj:  z,  b: 23,  a:  54]
    [nr:  112,  ta:  22,     obj:  x,  b: 78,  a:  53]
    [nr:  113,  ta:  22,  obj:  y,  b: 89,  a:  64]
    [nr:  114,  ta:  22,     comm it     ]
    [nr:  116,  ta:  23,     obj:  y,  b: 64,  a:  85]
    [nr:  116,  ta:  23,  obj: z,  b:       54,  a: 37]
                                                                                                    log buffer
35   1/ 7   51                                 Tr    ans   act i    on  P   roc   ess   i ng                          18
````

### 图片文字 OCR（en-US，待对照原页）

````text
values.
[nr: 110, ta:
[nr:
[nr: 112, ta:
[nr: 113, ta:
114,
[nr: 116, ta:
[nr: 116, ta:
351/751
Recovery exarnple, the scenario
Stable database
Situation at the time of the crash.
• Database buffer is then lost.
x 78 z 54
Writes are shown on top of old
111, ta:
Y 89
Stable log
91, a: 78]
22, obj: x, b:
23, obj: z, b: 23, a: 54]
22, obj: x, b:
78, a: 53]
22, obj: y, b: 89, a: 64]
22, commit]
23, obj: y, b:
64, a: 85]
23, obj: z, b:
54, a: 37]
log buffer
Transaction Processing
18
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 19 页

[查看此页](../../../../source/751/751%2525/DB51_2025_GWdurability.pdf#page=19)

### 原始文字层

````text
351/751 Transaction Processing 19
Recovery example, the scenario 
• What is the state of the database 
buffer at current time?
x ? z ?
y ?
Stable log
[nr: 110, ta: 22, obj: x, b: 91, a: 78]
[nr: 111, ta: 23, obj: z, b: 23, a: 54]
[nr: 112, ta: 22, obj: x, b: 78, a: 53]
[nr: 113, ta: 22, obj: y, b: 89, a: 64]
[nr: 114, ta: 22, commit]
[nr: 116, ta: 23, obj: y, b: 64, a: 85]
[nr: 116, ta: 23, obj: z, b: 54, a: 37]
 log buffer
x 78 z 54
y 89
Stable database 
Database buffer
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Recovery example, the scenari o
                                                                               Stable database
•   What is the state of the database                                                 x    78        z   54
    buffer at current time?
                                                                                              y    89
                                                  Stable      log             Dat abase  buf fer
    [nr:  110,  ta:  22,      obj:  x,  b: 91,  a:  78]
    [nr:  111,  ta:  23,  obj:  z,  b: 23,  a:  54]
    [nr:  112,  ta:  22,      obj:  x,  b: 78,  a:  53]                               x    ?         z   ?
    [nr:  113,  ta:  22,  obj:  y,  b: 89,  a:  64]
    [nr:  114,  ta:  22,      comm it     ]
    [nr:  116,  ta:  23,      obj:  y,  b: 64,  a:  85]                                       y    ?
    [nr:  116,  ta:  23,  obj: z,  b:        54,  a: 37]
                                                                                                    log buffer
35   1/ 7   51                                 Tr    ans   act i    on  P   roc   ess   i ng                            19
````

### 图片文字 OCR（en-US，待对照原页）

````text
Recovery exarnple, the scenario
111, ta:
• What is the state of the database
buffer at current time?
Stable database
x 78 z 54
Y 89
Database buffer
[nr: 110, ta:
[nr:
[nr: 112, ta:
[nr: 113, ta:
114,
[nr: 116, ta:
[nr: 116, ta:
351/751
Stable log
91, a: 78]
22, obj: x, b:
23, obj: z, b: 23, a: 54]
22, obj: x, b:
78, a: 53]
22, obj: y, b: 89, a: 64]
22, commit]
23, obj: y, b:
64, a: 85]
23, obj: z, b:
54, a: 37]
log buffer
Transaction Processing
19
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 20 页

[查看此页](../../../../source/751/751%2525/DB51_2025_GWdurability.pdf#page=20)

### 原始文字层

````text
351/751 Transaction Processing 20
Recovery example, the scenario 
• Situation at the time of the crash.
• Database buffer is then lost.
• What do we have to do?
x 91 z 23
y 89
Stable log
[nr: 110, ta: 22, obj: x, b: 91, a: 78]
[nr: 111, ta: 23, obj: z, b: 23, a: 54]
[nr: 112, ta: 22, obj: x, b: 78, a: 53]
[nr: 113, ta: 22, obj: y, b: 89, a: 64]
[nr: 114, ta: 22, commit]
[nr: 116, ta: 23, obj: y, b: 64, a: 85]
[nr: 116, ta: 23, obj: z, b: 54, a: 37]
 log buffer
x 78 z 54
y 89
Stable database 
Database buffer
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Recovery example, the scenari o
•   Si  tuation at the time of the crash.                                    Stable database
•   Database buffer is then lost.                                                   x    78       z   54
•   What do we               have to do?
                                                                                            y   89
                                                 Stable     log             Dat abase  buf fer
    [nr:  110,  ta:  22,     obj:  x,  b: 91,  a:  78]
    [nr:  111,  ta:  23,  obj:  z,  b: 23,  a:  54]
    [nr:  112,  ta:  22,     obj:  x,  b: 78,  a:  53]                              x    91       z   23
    [nr:  113,  ta:  22,  obj:  y,  b: 89,  a:  64]
    [nr:  114,  ta:  22,     comm it     ]
    [nr:  116,  ta:  23,     obj:  y,  b: 64,  a:  85]                                     y    89
    [nr:  116,  ta:  23,  obj: z,  b:       54,  a: 37]
                                                                                                    log buffer
35   1/ 7   51                                Tr    ans   act i    on  P   roc   ess   i ng                          20
````

### 图片文字 OCR（en-US，待对照原页）

````text
Recovery exarnple, the scenario
111, ta:
Situation at the time of the crash.
• Database buffer is then lost.
What do we have to do?
[nr: 110, ta:
[nr:
[nr: 112, ta:
[nr: 113, ta:
114,
[nr: 116, ta:
[nr: 116, ta:
351/751
Stable log
91, a: 78]
22, obj: x, b:
23, obj: z, b: 23, a: 54]
22, obj: x, b:
78, a: 53]
22, obj: y, b: 89, a: 64]
22, commit]
23, obj: y, b:
64, a: 85]
23, obj: z, b:
54, a: 37]
log buffer
Transaction Processing
Stable database
x 78 z 54
Y 89
Database buffer
x 91 z 23
Y 89
20
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 21 页

[查看此页](../../../../source/751/751%2525/DB51_2025_GWdurability.pdf#page=21)

### 原始文字层

````text
351/751 Transaction Processing 21
Crash recovery for no-force, steal policy
• has to redo winners and undo losers.
• has to go through the log:
• for redo in positive time direction
∘ Identify, whether the write (or its TA) is committed.
∘ write for each committed operation the after-image.
• for undo in negative time direction
∘ Identify whether write (or its TA) is not committed
∘ write for each uncommitted operation the before-image.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Crash rec ov er y for no                  -force, s teal poli cy
• has to r edo winners and undo losers.
• has to go through the l  og:
• for r edo in positive ti  me direction
    ∘  Identify, whether the write (or its T A) is comm itted.
    ∘  write for each com mitted operati  on the after                  -im age.
• for undo i  n negati  ve time di  rection
    ∘  Identify whether write (or i  ts T A) is not committed
    ∘  write for each uncommitted operation the before                        -im age.
35   1/7   51                      Tr    ans   act i    on  P   roc   ess   i ng         21
````

### 图片文字 OCR（en-US，待对照原页）

````text
Crash recovery for no-force, steal policy
has to redo winners and undo losers.
has to go through the log:
for redo in positive time direction
o Identify, whether the write (or its TA) is committed.
o write for each committed operation the after-image.
for undo in negative time direction
o Identify whether write (or its T A) is not committed
o write for each uncommitted operation the before-image.
351/751
Transaction Processing
21
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 22 页

[查看此页](../../../../source/751/751%2525/DB51_2025_GWdurability.pdf#page=22)

### 原始文字层

````text
351/751 Transaction Processing 22
Recovery example, the scenario 
• Situation at the time of the crash.
• Database buffer is then lost.
• Writes are shown on top of old 
values.
x 91 z 23
y 89
Stable log
[nr: 110, ta: 22, obj: x, b: 91, a: 78]
[nr: 111, ta: 23, obj: z, b: 23, a: 54]
[nr: 112, ta: 22, obj: x, b: 78, a: 53]
[nr: 113, ta: 22, obj: y, b: 89, a: 64]
[nr: 114, ta: 22, commit]
[nr: 116, ta: 23, obj: y, b: 64, a: 85]
[nr: 116, ta: 23, obj: z, b: 54, a: 37]
 log buffer
x 78 z 54
y 89
Stable database 
Database buffer 
64 85
78
53
54 fonmit.­lcrasG.gggindo­.­CO
只提交了22.23没撇
留 䜝
lost
不邀
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Recovery example, the scenari o
   •  Si  tuation at the time of the crash.                                Stable database
   •  Database buffer is then lost.                                              x    78      z    54
   •  Writes are show  n on top of ol  d
      values.                                                                           y    89
                                                Stable     log            Dat abase  buf fer
      [nr:  110,  ta:  22,    obj:  x,  b: 91,  a:  78]                                  53
      [nr:  111,  ta:  23,  obj:  z,  b: 23,  a:  54]                                  78            54
fo                 n                 m                 i                 t[nr:  112,  ta:  22,  .objlcrasG.:  x,  b: 78,  a:  53]gggindx91oz.23CO
      [nr:  113,  ta:  22,  obj:  y,  b: 89,  a:  64]                      没撇
      [nr:  114,  ta:  22,    comm it]              只提交了22.23
      [nr:  11 6,  ta:  23,   obj:  y,  b: 64,  a:  85]                                 y    89   64   85䜝
      [nr:  116,  ta:  23,  obj: z,  b: 54,  a: 37]
                                                                                                      log bufferlost留
                                                                                           不邀
  35   1/ 7   51                              Tr    ans   act i    on  P   roc   ess   i ng                     22
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
[nr
[nr
351 / 751
Recovery example, the scenario
Stable database
． Situation at the time of the crash.
1 10 ， ta ．
。 22 ， obj•
苤 23 ， obj.
。 22 ， obj.
1 13 ， ta ：
。 23 ， obj.
1 16 ， ta ：
Database buffer is then lost.
． Writes a re shown 0 n top 0f 01d
values.
Stable log
： 1 11 ， ta
nr: 112 ， ta ·
114 ， t
： 1 16 ， ta ·
： 2
2 ， obj•
CO
23 ， obj•
到 x ， b: 91 ， a: 78 ]
z, b: 23 ， a: 54 ]
x ， b: 78 ， a 53 ]
· y ， b: 89 ， a 64
y ， b: 64 ， a 85 ]
到 z ， b: 54 ， a ： 37 ]
x 78 z 54
y 89
Database buf er
53
6
log buffer 〔 亳 〕
Transaction Processing
22
````

### 图片文字 OCR（en-US，待对照原页）

````text
Recovery exarnple, the scenario
Stable database
Situation at the time of the crash.
111, ta:
• Database buffer is then lost.
Writes are shown on top of old
values.
22, obj:
23, obj: z,
22, obj:
2, obj:
co
23, obj:
23, obj: z,
x, b: 91, a: 78]
[nr:
351/751
[nr: 110, ta:
nr: 112, ta:
[nr: 113, ta:
114,
[nr: 116, ta:
[nr: 116, ta:
b:
Stable log
23, a: 54]
b: 78, a: 53]
t.
2
x,
y,
89, a 64
64, a: 85]
54, a: 37]
x 78 z 54
Y 89
Database buf er
crash)
53
z
6
log buffer Clos+)
Transaction Processing
VihJo
undo
22
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 23 页

[查看此页](../../../../source/751/751%2525/DB51_2025_GWdurability.pdf#page=23)

### 原始文字层

````text
Summary
• ACID Atomicity and ACID Durability can achieved with 
strategies working with an undo/redo log.
• The stable log and the stable database reside on persistent 
memory (disks, SSD).
• System crash: main memory content is lost.
• write-ahead logging: the stable log is authoritative, can be 
used to reconstruct a clean stable database.
• Different managements of the database buffer are possible, 
with the alternatives force/no-force, steal/no-steal.
• In the steal, no-force strategy, we have to redo winners and 
undo loser transactions.
351/751 Transaction Processing 23
一
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Summary
• AC  ID   A tomicity and A CID Durabili  ty can achi  eved with
  str ategies worki  ng with an undo/redo log.
• T he stable l  og and the stable database reside on persistent
  memory (disks, SS D).
• System crash: main m emory content is lost.
• write-ahead logging: the stable log is authori  tative, can be
  used to r econstr uct a clean stable database.
• Different managements of the database buffer are possible,
  with the alternatives force/no-force, steal  /no-steal.
• In the steal  , no-force strategy, we have to r edo wi  nners and ⼀
  undo loser transacti  ons.
35   1/ 7   51                   Tr    ans   act i    on  P   roc   ess   i ng      23
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Summary
． ACID Atomicity and ACID Durability can achieved with
strategies working with an undo/redo log.
． The stable log and the stable database reside O n persistent
memory (disks, SSD).
System crash: main memory content is lost.
． write-ahead logging: the stable log is authoritative, can be
used to reconstruct a clean stable database.
Different managements 0f the database buffer a re possible,
with the alternatives force/no-force, steal/no-steal.
《 th e steal, no-force strategy, we have tO redO winners and
undO loser transac lOns.
351 / 751
Transaction Processing
23
````

### 图片文字 OCR（en-US，待对照原页）

````text
Summary
ACID Atomicity and ACID Durability can achieved with
strategies working with an undo/redo log.
The stable log and the stable database reside on persistent
memory (disks, SSD).
System crash: main memory content is lost.
write-ahead logging: the stable log is authoritative, can be
used to reconstruct a clean stable database.
Different managements of the database buffer are possible,
with the alternatives force/no-force, steal/no-steal.
I the steal, no-force strategy, we have to redo winners and
undo loser transac Ions.
351/751
Transaction Processing
23
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

