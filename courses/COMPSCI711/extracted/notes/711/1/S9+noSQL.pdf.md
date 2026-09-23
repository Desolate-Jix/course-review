# S9+noSQL.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI711/notes/original/711/1/S9+noSQL.pdf`
- [打开原文件](../../../../notes/original/711/1/S9%2BnoSQL.pdf)
- 原文件 SHA-256：`e2043b2e383e87ae5d2a424b2e0683b30dc389bbe8dd338c7cb2690136f644f9`
- 文件索引：F074；PDF 总页数：28
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=1)

### 原始文字层

````text
Consistency and CAP
1
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Consistency and CAP
````

### 图片文字 OCR（en-US，待对照原页）

````text
Consistency and CAP
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=2)

### 原始文字层

````text
Reasons for Replication
• Data replication is a common technique in 
distributed systems. There are two reasons for 
data replication:
– It increases the reliability of a system.
• If one replica is unavailable or crashes, use another
• Protect against corrupted data
– It improves the performance of a system.
• Scale with size of the distributed system (replicated 
Web servers)
• Scale in geographically distributed systems (Web 
proxies)
• The key issue is the need to maintain consistency
of replicated data.
– If one copy is modified, others become inconsistent.
2
mnnunsr 性能
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Reasons for Replication
Data replication iS a COtnmon technique in
distributed systems. There are 忄 WO reasons for
data replication:
工 忄 increases the reliability 0f a system.
． If one replica iS unav 。 able or crashes, uSe another
． Protect against corrupted data
_ 工 忄 improves the performance 0f a system.
． Scale with size of e di rlbuted system (replicated
Web servers)
． ScaIe in geographically distributed systems (Web
proxies)
Th e k ey issue is the need 忄 0 maintain
consistency
of replicated data.
工 f one copy is modified, others become inconsistent.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Reasons for Replication
Data replication is a common technique in
distributed systems. There are two reasons for
data replication:
— It increases the reliability of a system.
If one replica is unav • able or crashes, use another
Protect against corrupted data
It improves the performance of a system.
Scale with size of e di ributed system (replicated
Web servers)
Scale in geographically distributed systems (Web
proxies)
The key issue is the need to maintain consistency
of replicated data.
If one copy is modified, others become inconsistent.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=3)

### 原始文字层

````text
Potential Issue
3
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Potential 工 ssue
9
X = 0
X = 0
9
X = 0
9
````

### 图片文字 OCR（en-US，待对照原页）

````text
Potential Issue
x=o
x=o
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=4)

### 原始文字层

````text
4
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
9
X = 0
9
X = 0
9
X = 0
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=5)

### 原始文字层

````text
5
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
9 一
一 × = 1 宀
X = 0
9
× = 0
9
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=6)

### 原始文字层

````text
6
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
9
9
X = 0
× = 0
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=7)

### 原始文字层

````text
7
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
9
9
X = 0
× = 0
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=8)

### 原始文字层

````text
Consistency model
• A consistency model defines the 
semantics of read operation of a data 
store
• That is, the set of possible values that 
can be returned by the data store.
8
we
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Consistency model
． consistency model defines the
semantics Of read
operation of a data
store
． That is, the set of possible values 忄 h 酣
can be returned by the data s 忄 or 巳
````

### 图片文字 OCR（en-US，待对照原页）

````text
Consistency model
A consistency model defines the
semantics of read operation of a data
store
That is, the set of possible values that
can be returned by the data store.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=9)

### 原始文字层

````text
• Strong Consistency: clients of a data 
storage always see the latest value that 
was written to a data object
• Eventual Consistency: 
– The data returned by a read operation is 
the value of the object at some past point 
in time but not necessarily the latest value.
– The replicated objects converge towards 
identical copies in the absence of updates. 
9
三
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
． Strong Consistency: clients of a data
storage always See the latest valu that
was written 忄 0 a data 0 ject
． EventuaI Consistency:
_ Th e data returned by a read operation is
the value of the object at some past point
in time but no 忄 necessarily the 忄 es 忄 value.
_ Th e replicated objects
towards
converge
identical copies in the absence 0f updates.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Strong Consistency: clients of a data
storage always see the latest valu that
was written to a data o ject
Eventual Consistency:
— The data returned by a read operation is
the value of the object at some past point
in time but not necessarily the latest value.
— The replicated objects converge
towards
identical copies in the absence of updates.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=10)

### 原始文字层

````text
10
Enforcing Strong Consistency 
(Quorum algorithm)
• Two weights are given. 
– One is for the write operation ww
– The other is for the read operation rw. 
– Each replication site has one token that carries 
some weight (normally 1). 
• In order to carry out a read/write operation, 
a client needs to collect enough weight (i.e. 
tokens). 
– A read operation can be carried out if the weight 
collected by the client is greater or equal than rw; 
– A write operation can be carried out if the weight 
collected by the client is greater or equal to ww. 
10
6 wait wait
5 read wait
令牌
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Enforcing Strong Consistency
(Quorum algorithm)
Tw 0 weights are given.
_ One is for the write operatio
“ tead 七
_ Th e other is for the read operatio
_ Each replication site h as one toke
that carries
some weight (normally 1 〗
工 n order 忄 0 carry ou 忄 a read/write operation,
a client needs 忄 0 collect enough weight (i.e.
tokens).
_ read operation can be carried ou 忄 if the weight
collected by the client is greater 0 r equal than rw;
_ write operation can be carried ou 忄 if the weight
collected by the client is greater 0 r equal 忄 0
10
````

### 图片文字 OCR（en-US，待对照原页）

````text
Enforcing Strong Consistency
(Quorum algorithm)
' Two weights are given.
vhtte
nbww
One is for the write operatio
frw. tud
The other is for the read operatio
Each replication site has one toke
that carries
some weight (normally 1).
In order to carry out a read/write operation,
a client needs to collect enough weight (i.e.
tokens).
— A read operation can be carried out if the weight
collected by the client is greater or equal than rw;
— A write operation can be carried out if the weight
collected by the client is greater or equal to ww.
10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=11)

### 原始文字层

````text
11
• rw and ww have to satisfy the following: 
– ww > ns/2
• ensure that the write operations are exclusive 
– (rw + ww) > ns
• ensure that read and writes excludes each 
other 
• a read operation will never read a value which is 
out-of-date 
– ns is the number of tokens in the system, 
and each token carries weight 1 
no
unicorn
need5 to read but only4remain
rwiocfttd
number of token
read and write an
not happen
the 㗊
允许 同时 读
不许同时读鸟 鸟鸟
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
红 丝 （ 丿 hf 呼
e 认
司 er 寸
r ： 占
． rw “ have 忄 0 satisfy the following:
． ensure that the write operations are exclusive
_ (r + 丿 > nS
． ensure that read and writes excludes eac
other
． a read operation will never read a value which iS
out-of-date
一 nS is the number of 忄 0 nS in the system,
and each token carries weight 1
````

### 图片文字 OCR（en-US，待对照原页）

````text
urq/cg
need < pad / buf on/ 4
rernøt.öh
rw and w have to satisfy the following:
ww
ensure that the write operations are exclusive
read 001 d
— (rw + ww) > ns
ensure that read and writes excludes eac
other
Camg
a read operation will never read a value which is
out-of-date
— ns is the number of to ns in the system,
and each token carries weight 1
fid {$15)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=12)

### 原始文字层

````text
Enforcing Eventual Consistency
• Enforcing eventual consistency relies on 
two properties: 
– total propagation: updates can reach all the 
sites
– consistent ordering: updates are processed 
by all the sites in consistent order
12
mnnnznn
````

### 图片文字 OCR（en-US，待对照原页）

````text
Enforcing Eventual Consistency
Enforcing eventual consistency relies on
two properties:
— total propagation
sites
— consistent orderin
u dates are processed
by all the sites in consisten o er
12
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=13)

### 原始文字层

````text
13
X=1 X=1
increase 10 increase 20
Order is not always important
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Order is not always important
increase 10
× = 1
increase 20
× = 1
13
````

### 图片文字 OCR（en-US，待对照原页）

````text
Order is not always important
increase 10
increase 20
13
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=14)

### 原始文字层

````text
Issues with Strong and Eventual 
Consistency 
• Strong consistency generally results in lower 
performance and reduced availability for reads or writes or both. 
• Eventual consistency can confuse users and 
applications
– A user may write a value to a data item and then 
later reads an older value.
– A user may update some data item based on 
reading some other data, while others read the 
updated item without seeing the data on which it is 
based.
– These issues can appear even when only a single 
user or application is making data modifications.
14
臼
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
工 ssues with Strong and Eventual
Consistency
Strong consistency generally results in
lower
performance
and reduced availability for reads
0 r writes 0 r both.
1
Eventual consistency ca
confuse users and
applications
_ user m ay write a value 忄 0 a data item and then
later reads an older value.
_ user m ay update some data item based on
reading some other data, while others read the
updated item without seeing the data on which it is
based.
_ Th eSe issues can appear even when only a single
user 0 r application is making data modifications.
14
````

### 图片文字 OCR（en-US，待对照原页）

````text
Issues with Strong and Eventual
Consistency
Strong consistency generally results in lower
performance and reduced availability for reads
or writes or both.
' Eventual consistency ca
confuse users and
applications
— A user may write a value to a data item and then
later reads an older value.
— A user may update some data item based on
reading some other data, while others read the
updated item without seeing the data on which it is
based.
These issues can appear even when only a single
user or application is making data modifications.
14
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=15)

### 原始文字层

````text
Consistency models in industry
• Microsoft Azure: strong consistency 
• Amazon S3: eventual consistency 
• Many others: between strong and 
eventual 
15
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Consistency models in industry
． Microsoft Azure: strong consistency
． Amazon S3: eventual consistency
． Many others: between strong and
eventual
15
````

### 图片文字 OCR（en-US，待对照原页）

````text
Consistency models in industry
Microsoft Azure: strong consistency
Amazon 53: eventual consistency
Many others: between strong and
eventual
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=16)

### 原始文字层

````text
CAP Theorem for distributed 
systems • Cloud providers normally replicate data at 
different locations.
– For availability and reliability
• To maintain the consistency of the replicated 
data, the operations on the replicated data 
need to be synchronised. 
• The CAP theorem states that any networked 
shared-data system can have at most two of 
three desirable properties:
– consistency (C) equivalent to having a single up-to- date copy of the data;
– high availability (A) of that data (for updates); 
– tolerance to network partitions (P).
16
T_T
evenif crashed can providesame
same
系统分开 依 有
Ii
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
CAP Theorem for distributed
． CIoud providers 00 羔 aTly
S S ems
replicate data 酣
different locations.
_ For availability and reliability
To maintain the consistency of the re licated
data, the operations on the 00ph0 酣 0 扌 d 酣 0
need 忄 0 be synchronised.
Th e CAP theorem states 忄 h 酣 a
ed
shared-data S stem can have at most tw of
three desirablYe properties:
（ equivalent 忄 0 having a single up-to-
_ consistency
date copy of 忄 e dat
） 。 忄 h 磊 忆 (for upd tes);
_ high 口 b 洧 t /
_ tolerance 忄 0 network partitions
16
````

### 图片文字 OCR（en-US，待对照原页）

````text
CAP Theorem for distributed
systems
Cloud providers notha ly replicate data at
different locations.
For availability and reliability
To maintain the consistency of the replicated
data, the operations on the replicated data
need to be synchronised.
The CAP theorem states that a
ed
shared-data system can have at most tw of
three desirable properties:
— consistency (C) equivalent to having a single up-to-
date copy of the dat
caq hvide
(A) o thaCftåata (for upd tes);
high availability
— tolerance to network partitions
16
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=17)

### 原始文字层

````text
Consistency
• Consistency means the multiple copies 
need to be kept perfectly synchronised.
– To require perfect consistency, 
communication between data centers
hosting the copies is paramount. 
– The overall performance of such a system 
could drop as the number of replica 
required goes up.
17
__
````

### 图片文字 OCR（en-US，待对照原页）

````text
Consistency
Consistency means the m Itiple co ies
need to be kept perfect y synchronised
— To require perfect consistency,
communic tion between data centers
h s ingt e opies is paramount.
— The overall performance of such a system
could drop as the number of replica
required goes up.
17
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 18 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=18)

### 原始文字层

````text
Availability 
• Although having a single copy of a data item 
ensures perfect consistency, such an 
arrangement does not provide high availability.
– The copy becomes unavailable when the site 
hosting the copy goes down
• The only solution to the availability issue is 
through replicating the data.
• Increasing the number of sites with copies of 
the data directly increases the availability of 
the system.
• Replicas also help in load balancing concurrent 
read operations. 
18
一
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Availability
Although having a single COPY of a data item
ensures perfect conSIStency, such an
arrangement does not provide high availability.
_ Th e copy becomes unavailable when the site
hosting the COPY goes down
Th e only solution 忄 0 the availability issue is
through re licating
the data.
er of sites with cop ies 0f
lncreasin 忄 e n
the data 000 刊 y increases the availabllity of
the system.
Replicas also help in load balancing concurrent
read operations.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Availability
Although having a single copy of a data item
ensures perfect consistency, such an
arrangement does not provide high availability.
The copy becomes unavailable when the site
hosting the copy goes down
The only solution to the availability issue is
through replicating the data.
Increasinq t e n er of sites with copies of
the data directly increases the availability of
the system.
Replicas also help in load balancing concurrent
read operations.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 19 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=19)

### 原始文字层

````text
Partition Tolerance
• We get Availability by replicating data on 
different data centers.
• If the network connectivity between two data 
centers is lost, both data centers are incapable 
of synchronizing state with each other.
– If we allow read/write operations on these two 
data centers , it can be shown that the data in the 
two data centers won’t be consistent anymore.
– If we decide consistency is important, and disable 
write operations during the network outage, we will 
loose “availability” as no update operations can be 
carried out.
19
````

### 图片文字 OCR（en-US，待对照原页）

````text
Partition Tolerance
We get Availability by
replicating data on
different data centers.
If the network connectivity between two data
centers is lost, both data centers are incapable
of synchronizing state with each other.
If we allow read/write operations on these two
data centers , it can be shown that the data in the
two data centers won't be consistent anymore.
If we decide consistency is important, and disable
operations during the network outage, we will
write
loose "availability" as no update operations can be
carried out.
19
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 20 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=20)

### 原始文字层

````text
• Many applications require high availability and good performance.
• According to the CAP theorem, there is a trade-off
between consistency and availability.
• In the presence of partition, many systems choose 
availability at the expense of consistency (temporarily).
– The consistency will be restored after the partition is 
repaired.
– Eventual consistency
• The NoSQL movement is about creating choices that focus on availability first and consistency 
second.
• NoSQL systems use BASE (basically available, soft state, eventually consistent).
20
Cott not only SQL
````

### 图片文字 OCR（en-US，待对照原页）

````text
Many applications require high availability and good
performance
According to the CAP theorem, there is a trade-off
between consistency and availability.
• In the presence of partition, many systems
choose
availability at the expense of consistency
(temporarily).
The consistency will be restored after the partition is
repaired.
— Eventual consistency
wt SQL
movement is about 'heating choices
The
OS
that ocus on availability first and consistency
second.
BASE
basically available, soft
• NoSQL systems use
state, eventually consistent .
20
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 21 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=21)

### 原始文字层

````text
Basically available
• The system supports data availability in a 
partial system failure.
– there will be a response to any request. 
– some responses might fail to obtain the 
requested data or the data may be in an 
inconsistent state
• For example, if data are partitioned across 
several servers, BASE design encourages 
crafting operations in such a way that a 
server failure impacts only the operations accessing the data on the failed server. 
21
````

### 图片文字 OCR（en-US，待对照原页）

````text
Basically available
The system supports data availability
ina
partial system failure.
— there will be a
response to any request.
— some responses might
to obtain the
requested data or the data may be in an
inconsistent state
For example, if data are partitioned across
several servers, BASE design encourages
craftinq operations in such a way that a
server failure impacts only the operations
accessing the data on the failed server.
21
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 22 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=22)

### 原始文字层

````text
Soft State
• For many operations, it takes some time for the 
states of the system to settle.
– Transfer money between two accounts
– After deducting an amount from one user, the amount 
to be credited to the other user is placed in a 
message queue waiting to be executed
– There is a lag between the start and the end of the 
transfer when the money is in the message queue and 
does not appear in neither users’ accounts
• For many applications, this time lag is acceptable.
• Accepting the state of the system is constantly 
changing means accepting the fact that sometimes 
the data returns from the system might not be 
accurate.
22
````

### 图片文字 OCR（en-US，待对照原页）

````text
Soft State
For many operations, it takes some time for the
states of the system to settle.
Transfer money between two accounts
After deducting an amount from one user, the amount
to be credited to the other user is placed in a
message queue waiting to be executed
There is a lag between the start and the end of the
transfer when the money is in the message queue and
does not appear in neither users' accounts
For many applications, this time lag is acceptable
Accepting the state of the system is constantly
chanqing means accepting the fact that sometimes
the data returns from the system might
not be
accurate
22
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 23 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=23)

### 原始文字层

````text
Eventually Consistent
• The system will eventually become 
consistent once it stops receiving input.
– Updates will be propagated to every site 
eventually
23
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Eventually Consistent
． The system will eventually
become
consistent once it StopS receiving input.
_ Updates will be propagated 忄 0 every site
eventually
23
````

### 图片文字 OCR（en-US，待对照原页）

````text
Eventually Consistent
The system will eventually become
consistent once it stops receiving input.
Updates will be propagated to every site
eventually
23
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 24 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=24)

### 原始文字层

````text
Begin transaction
Insert into sell_record(id, seller_id, buyer_id, amount);
Queue message “update user(“seller”, seller_id, amount)”;
Queue message “update user(“buyer”, buyer_id, amount)”;
End transaction
To implement BASE, many systems rely on 
transaction and some sort of message queue to 
persistently store and route data to various 
storage services that perform the actual 
database operations.
24
reaiable­.ruSha
send
message
local machine
net i
ensure send
to remote
machine
````

### 图片文字 OCR（en-US，待对照原页）

````text
To implement BASE, many systems rely on ble
transaction and some sort of messa e queue
persistently store and route ata to various
fbl
storage services that perform the actual
database operations,
Begin transaction
Insert into sell
Queue message
End transaction
(Ocal
_record(i4, s Iler_id,
up a e seller",
Queue message "update user("buyer", buyer_id, amount)";
Lok's e
buyer_id, amount);
seller_id, amount)"
gend
remgte
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 25 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=25)

### 原始文字层

````text
• In BASE conforming systems, concurrent 
and possible inconsistent updates might 
occur.
– Concurrent updating the same calendar entry 
while the system is partitioned.
• Partially ordered timestamps and event 
logging should be used for the events in a 
BASE conforming system. 
– Identifying and resolving conflicting and 
inconsistent updates.
25
````

### 图片文字 OCR（en-US，待对照原页）

````text
In BASE conforming systems, concurrent
and possible
updates might
inconsistent
occur.
— Concurrent updating the same calendar entry
while the system is partitioned.
Partially ordered timestamps and event
logging should be used for the events in a
BASE conforming system.
— Identifying and resolving conflicting and
inconsistent updates.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 26 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=26)

### 原始文字层

````text
reviews
• Understand strong consistency and eventual 
consistency.
• How to ensure strong consistency?
• What are the issues with strong consistency and 
eventual consistency?
• Understand the CAP theorem for distributed 
systems. 
• Assume you are developing a banking and a shopping 
cart applicant. Discuss how the CAP theorem and 
the operating environment might affect your 
development.
• What are the advantages of a system that prefers 
CP? What are the challenges facing the system?
• What are the advantages of a system that prefers 
AP? What are the challenges facing the system?
26
````

### 图片文字 OCR（en-US，待对照原页）

````text
reviews
• Understand strong consistency and eventual
consistency.
How to ensure strong consistency?
What are the issues with strong consistency and
eventual consistency?
• Understand the CAP theorem for distributed
systems.
Assume you are developing a bankinq and a shopping
cart applicant. Discuss how the CAT theorem and
the operating environment might affect your
development.
• What are the advantaaes of a system that prefers
CP? What are the challenges facing the system?
• What are the advantaqes of a system that prefers
AP? What are the challenges facing the system?
26
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 27 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=27)

### 原始文字层

````text
reviews
• Understand the BASE properties.
• Why do many systems conform to the BASE 
properties.
• In BASE, how does a system ensure that an 
operation can be carried out in the presence of 
a system failure? [Note: a failure could be a 
crash failure of a site or a system partition]
• If you design a system conforming to the BASE 
properties, what issues do you need to address 
in the presence of system partition?
27
````

### 图片文字 OCR（en-US，待对照原页）

````text
reviews
Understand the BASE properties.
Why do many systems conform to the BASE
properties.
In BASE, how does a system ensure that an
operation can be carried out in the presence of
a system failure? [Note: a failure could be a
crash failure of a site or a system partition]
If you design a system conforming to the BASE
properties, what issues do you need to address
in the presence of system partition?
27
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 28 页

[查看此页](../../../../notes/original/711/1/S9%2BnoSQL.pdf#page=28)

### 原始文字层

````text
Further readings
• Douglas B. Terry, Alan J. Demers, Karin Petersen, 
Mike Spreitzer, Marvin Theimer, and Brent W. 
Welch. 1994. Session Guarantees for Weakly 
Consistent Replicated Data. In Proceedings of the Third International Conference on Parallel and 
Distributed Information Systems (PDIS '94). IEEE Computer Society, Washington, DC, USA, 140-149.
• Eric Brewer, "CAP Twelve Years Later: How the 
"Rules" Have Changed," Computer, vol. 45, no. 2, pp. 23-29, Feb. 2012
• Dan Pritchett. 2008. BASE: An Acid 
Alternative. Queue 6, 3 (May 2008), 48-55.
28
````

### 图片文字 OCR（en-US，待对照原页）

````text
Further readings
Douglas B. Terry, Alan J. Demers, Karin Petersen,
Mike Spreitzer, Marvin Theimer, and Brent W.
Welch. 1994. Session Guarantees for Weakly
Consistent Replicated Data. In Proceedings of the
Third International Conference on Parallel and
Distributed Information Systems (PDIS '94). IEEE
Computer Society, Washington, DC, USA, 140-149.
' Eric Brewer, "CAP Twelve Years Later: How the
"Rules" Have Changed," Computer, vol. 45, no. 2, pp.
23-29, Feb. 2012
Dan Pritchett. 2008. BASE: An Acid
Alternative. Queue 6, 3 (May 2008), 48-55.
28
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

