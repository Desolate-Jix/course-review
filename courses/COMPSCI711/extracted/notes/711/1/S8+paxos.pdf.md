# S8+paxos.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI711/notes/original/711/1/S8+paxos.pdf`
- [打开原文件](../../../../notes/original/711/1/S8%2Bpaxos.pdf)
- 原文件 SHA-256：`77b12c0c4870d987b54df83782f54693f30ec7dea39870966b6ff3e7aa8fa00e`
- 文件索引：F072；PDF 总页数：49
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=1)

### 原始文字层

````text
The consensus problem in 
distributed systems
1
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Th e consensus problem in
distributed systems
````

### 图片文字 OCR（en-US，待对照原页）

````text
The consensus problem in
distributed systems
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=2)

### 原始文字层

````text
The consensus problem 
• There are N nodes in the system
• Each node starts with input {0,1}
• The network is asynchronous but reliable
– Messages can take arbitrarily long to be delivered
• Nodes operate at arbitrary speed, may fail by 
stopping (crash failure), and may restart.
• At most 1 node fails 
• Goal: all nodes decide same value v, where v was 
an input
2
藻
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Th e consensus problem
There are N nodes in the system
Each node starts wi input {
Th e network is asyn ronous but reliable
_ Messages can take
arbitcarily long
忄 0 be delivered
Nodes 0 些 r 酣 e 酣 arbi+r%ary speed, m ay
stopping (crash failure), and m ay
restart
忄 most 1 node fails
Goal: nodes decide
same value V
where V waS
an input
````

### 图片文字 OCR（en-US，待对照原页）

````text
The consensus problem
There are N nodes in the system
Each node starts wi input (C) 1
The network is asyn ronous but reliable
— Messages can take
arbitcarily long
to be delivered
Nodes operate at arbi+r%ary speed, may
fgiLby
stopping (crash failure), and may
restart
At most 1 node fails
Goal: all nodes decide same value v
where v was
an input
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=3)

### 原始文字层

````text
Fault-tolerant consensus protocol
• Collect votes from all N nodes
• Wait for the majority of nodes to 
respond, and tell everyone the outcome 
(choose value for the output)
• Nodes “decide” (i.e. they accept the 
outcome)
• There is a problem if a message is 
delayed or a node restarts after a 
failure.
3
协 收
-
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Fault-toIerant consensus protocol
． Co c 忄 votes from N nodes
． Wait for the ma'ority of nodes 忄 0
respond, and te everyone the outcome
(choose value for the output)
． Nodes "decide" (i.e. they accept the
outcome)
problem
． There iS a
if a message iS
delayed 0 r a node restarts after a
failure.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Fault-tolerant consensus protocol
Collect votes from all N nodes
Wait for the ma'ority of nodes to
respond, and te everyone the outcome
(choose value for the output)
Nodes
decide
(i.e. they accept the
outcome)
There is a problem if a message is
delayed or a node restarts after a
failure.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=4)

### 原始文字层

````text
4
A
B
C
````

> OCR 未识别出可靠文字；本页可能以图形、手写公式或空白为主。

### 图表辅助说明

一致性示例的初始布局：A 位于上方，B、C 位于下方，尚未画出请求或回复箭头。

## PDF 第 5 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=5)

### 原始文字层

````text
5
A
B C
10 10
````

### 图片文字 OCR（en-US，待对照原页）

````text
10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=6)

### 原始文字层

````text
6
A
B C
OK OK
````

> OCR 未识别出可靠文字；本页可能以图形、手写公式或空白为主。

### 图表辅助说明

B 和 C 各向 A 发送一条标记为 OK 的回复，箭头指向上方的 A。

## PDF 第 7 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=7)

### 原始文字层

````text
7
A
B C
Use 10 Use 10 takestime
not
get reply
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Use 10
Use 10
丶
丶
乛 况
````

### 图片文字 OCR（en-US，待对照原页）

````text
Use 10
Use 10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=8)

### 原始文字层

````text
8
A
B C
Use 10 Use 10
20 àssu me
There A crash
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Use ℃
20
丶
Use 10
````

### 图片文字 OCR（en-US，待对照原页）

````text
Use 10
Use 10
20
A clash
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=9)

### 原始文字层

````text
9
A
B C
Use 10 Use 10
OK
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Use 10
OK
Use 10
````

### 图片文字 OCR（en-US，待对照原页）

````text
Use 10
0K
Use 10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=10)

### 原始文字层

````text
10
A
B C
Use 10 Use 10
Use 20
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Use 10
Use 20
Use 10
10
````

### 图片文字 OCR（en-US，待对照原页）

````text
Use 10
Use 20
Use 10
10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=11)

### 原始文字层

````text
11
A
B C
Use 10 Use 10
Use 10
Use 20 Use 20 0
0
0
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Us
Use ℃
Use 2
1
Use 10
Use
0
````

### 图片文字 OCR（en-US，待对照原页）

````text
1
Use 10
Use 2
Use 10
Use
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=12)

### 原始文字层

````text
FLP Impossibility of Consensus
• A surprising result
– In an asynchronous model where only one node 
might crash, there is no fault-tolerant 
distributed algorithm that solves the 
consensus problem.
• They prove that no consensus algorithm is 
guaranteed to terminate in the presence 
of crash faults
– This is true even if no crash actually occurs
– Proof constructs infinite non-terminating runs
12
0
````

### 图片文字 OCR（en-US，待对照原页）

````text
FLP Impossibility of Consensus
A surprising result
model where only one ode
— In an as nchro
s
might rash there is no fault-toleran
distributed algorithm that solves the
consensus problem.
They prove that no consensus algorithm
is
guaranteed to terminate
in the presence
of crash faults
— This is true even if no crash actually occurs
— Proof constructs infinite non-terminating runs
12
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=13)

### 原始文字层

````text
Intuition of FLP
1. A system tries to agree on which command to execute next
2. Node p’s messages are delayed during the transmission
– p is regarded as failed
3. Since the system is fault-tolerant, if p crashes, the system should adapt and move on to reach a 
decision
4. Before the decision is finally reached, p’s 
messages arrive. So, p has to be included in decision making. 
5. We are back to the beginning (step 1).
• This takes time and no real progress occurs between 1 
and 4.
13
von Lee
O
_
o ra­re
start delay 一
器
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
1 ·
2 ·
3 ·
5 ·
工 ntuition of FLP
system tries 忄 0 agree 0 n which command 忄 0
execute neXt
delayed during the
NOde p'S messages are
transfttiSsion
P is regarded as failed
Since the system is fault-tolerant, if p crashes,
the system should adapt
and move on 忄 0 reach a
deciston
efor he decision is finally reached, p's
· So, p has 忄 0 be included in
back 忄 0 the b eg
s ep 1 〗
We are
ThiS ta eS 《 me and no real progress occurS between 1
and 4 ·
````

### 图片文字 OCR（en-US，待对照原页）

````text
1.
2.
3.
4.
5.
Intuition of FLP
A system tries to agree on which command to
execute next
Node p's messages are delayed during the
transmiSsion
— p is regarded as failed
Since the system is fault-tolerant, if p crashes,
the system should adapt and move on to reach a
deciston
efor he decision is finally reached, p's
So, p has to be included in
arrive
m ages
decision
We are back to the beg
s ep 1).
This ta es tme and no real progress occurs between 1
and 4.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=14)

### 原始文字层

````text
The meaning of “impossibility”
• In formal proofs, an algorithm is totally correct
if
– It is safe.
– It always terminates.
• FLP proves that any fault-tolerant algorithm 
solving consensus has runs that never terminate
– These runs are extremely unlikely (“probability is 
close to zero”)
• These runs mean that a totally correct solution 
for the consensus problem is impossible.
• It means consensus is not always possible.
14
co
Still use chance 愿
机率
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
The meaning of "impossibility"
ln formal proofs, an algorithm is 忄 0 忆
correct
_ 工 忄 is afe
_ 工 忄 always termina e ·
FLP proves 忄 h 酣 any fault-tolerant algorithm
SOlVing consensus haS runs that
never terminat
_ Th eSe runs are extremely
unlikel
("probability is
ClOSe 忄 0 zero")
Th es e runs mean 忄 h 酣 a totally correct solutio
for the consensus problem iS
impossible
no 忄 always possible.
工 忄 means consensus iS
14
````

### 图片文字 OCR（en-US，待对照原页）

````text
The meaning of "impossibility"
In formal proofs, an algorithm is totally
correct
It is afe
It always termina e .
FLP proves that any fault-tolerant algorithm
solving consensus has runs that
never terminat
These runs are extremely unlikely ("probability is
soll (Age, chmz/ØJ
close to zero")
These runs mean that a totally correct
for the consensus problem is impossible
not always possible.
It means consensus is
14
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=15)

### 原始文字层

````text
Paxos Algorithm
• Distributed consensus algorithm
• Key Assumptions:
– There are n nodes. The set of node is known a￾priori.
– Nodes suffer crash failures, nodes can restart
after a failure
– Network might be very slow
• Guarantees safety
– Only a single value is chosen 
– Only a proposed value can be chosen 
– Once a value is chosen, it remains the only chosen 
value.
• Cannot guarantee liveness.
15
o
````

### 图片文字 OCR（en-US，待对照原页）

````text
Paxos Algorithm
Distributed consensus algorithm
Key Assumptions:
There are n nodes. The set of node is known a-
priori.
Nodes suffer crash failures, nodes can restart
after a failure
Network might be very slow
Guarantees safety
Only a
value is chosen
Only a proposed value can be chosen
— Once a value is chosen, it remains the only chosen
value
Cannot guarantee liveness
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=16)

### 原始文字层

````text
Details of Paxos
• 3 roles
– proposer
– acceptor
– learner
• 3 phases
– Phase 1: prepare
– Phase 2 (if get positive replies from a majority 
of the nodes): propose
– Phase 3: (if get positive replies from a 
majority of the nodes): finalise
16
If u value
TǗÜ
````

### 图片文字 OCR（en-US，待对照原页）

````text
Details o
tell learner
axos
Vallie,
3 roles
— proposer
— acceptor
— learner
3 phases
— Phase 1: prepare
— Phase 2 (if get positive replies from a majority
of the nodes): propose
— Phase 3: (if get positive replies from a
majority of the nodes): finalise
16
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=17)

### 原始文字层

````text
Phase 1: (prepare request)
• A proposer chooses a new proposal version 
number n , and sends a prepare request 
(“prepare”,n) to a majority of acceptors:
– Can I make a proposal with version number n ?
– If yes, do you suggest a value for my proposal?
17
A3
P
A1
A2
wu
_
O fffff.­co
````

### 图片文字 OCR（en-US，待对照原页）

````text
Phase 1: (prepare request)
Ver5110in vluunPr
a new proposal version
A ropos choo
num er n , an sends a
repare request
re are"
to a majority o acce tors:
— Can I make a proposal with ersion numb
— If yes, do you suggest a value for my proposal?
p
17
````

### 图表辅助说明

消息时序图中时间从左向右，P 向 A1、A2、A3 发出 prepare 请求，版本号为 n。横线表示进程，斜向箭头表示跨进程消息。

## PDF 第 18 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=18)

### 原始文字层

````text
• When an acceptor receives a prepare request 
(“prepare”, n) where n is greater than the version 
number of any prepare request the acceptor t has 
already responded, the acceptor sends out (“ack”, 
n, n’, v’) or (“ack”, n, - , -)
– A respond is a promises not to accept any proposal with version number less than n.
– A respond suggests the value v’ of the highest-number proposal that the acceptor has accepted if any, else –
– If the acceptor receives a prepare request with a 
larger version number, the acceptor abandons the 
engagement with the proposer with a smaller version 
number and engages the proposer with a larger version 
number.
18
A3
P
A1
A2
Ccheek
o no
杅之
t ET 前
repy­nc.nl awe
COL 毗 版本 融 放弃 小
版本的
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
When an acceptor receives a repare request
C prepare", n) where n is
a e han the version
number Of a ny prepare re
e acceptor 忄 ha
alread reS onded, the acceptor sends ou 忄 (' 、 ack"
respond is a promtses no 忄 忄 0 accept a ny pr 0Sal with
version number leSS than n.
hiqhest-number(
工 f the accepto receives a prepare request with a
larger
n ber, the acceptor abandons
the
engagement with e roposer with a smaller version
number and engages
number.
roposer with a larger version
AI
````

### 图片文字 OCR（en-US，待对照原页）

````text
• When an acceptor receives a repare request
("prepare", n) where n is
a e han the version
number of any prepare re
e acceptor t ha
already responded, the acceptor sends out ("ack",
n, n', v') or ("ack", n,
respond is a promises not to accept any pr osal with
version number less than n.
highest-number?
— A respond suggests the value v of the
the acceptor has accepted If any, else -
proposa
If the accepto receives a prepare request with a
larger
n ber, the acceptor abandons the
engagement with e roposer with a smaller version
number and engages
number.
p
roposer with a larger version
18
````

### 图表辅助说明

在 prepare 消息之后，acceptor 的回复箭头返回 proposer。回复承诺不再接受更低版本，并携带已接受提案中最高版本及其值（如果存在）；红色手写文字解释版本检查。

## PDF 第 19 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=19)

### 原始文字层

````text
Phase 2: (accept request)
• If the proposer receives responses from a 
majority of the acceptors, it can issue a 
proposal for value (i.e. an accept request) 
(“accept”, n , v) with version number n and 
value v:
– n is the number that appears in the prepare 
request.
– v is the value of the highest version number 
proposal among the responses (if any)
19
P
A1
A2
A3
Phase 1
value v?
o
some acceptor may ten
with
prepare
messy
用最大
版本号和
l­itnotre
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Phase 2 ： (accept request)
the roposer receives responses from a
f the acceptors, it can iSSue a
maJOrI
or value i.e. an accept request)
（ 、 、 accept", n ， v) wit version number n and
value v:
is the number that appears i the pre r
request.
is the value of the highest version numbe
proposal among the responses ()f any)
value V?
AI
Phase 1
19
````

### 图片文字 OCR（en-US，待对照原页）

````text
Phase 2: (accept request)
the roposer receives responses from a
f the acceptors, it can issue a
maJorl
or value (i.e. an accept request)
("accept", n , v) with version number n and
q CC +01/1
value v:
n is the number that appears i the
request.
v is the value of the highest version numbe
proposal among the responses (if any)
value v?
p
Phase 1
19
````

### 图表辅助说明

黄色区域是已完成的 Phase 1；随后 proposer 发送 Phase 2 accept 请求。选值依据 Phase 1 返回的最高已接受版本，而不是简单任意挑选。

## PDF 第 20 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=20)

### 原始文字层

````text
• If the acceptor receives an accept request 
(“accept”, n , v), it accepts the proposal unless 
it has already responded to a prepare request 
having a version number greater than n.
– The acceptor logs v on disk and sends ack to the 
proposer
• If a majority of the acceptors have logged v on 
their disk, the value is chosen.
20
P
A1
A2
A3
Phase 1
value v
H n I
re­ceive
use
𡁻
record came send reply in disk
majority
agree­d
made 此照
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
If the acc 忄 or receives an accept request
("accept"
， v), it accepts the proposal unless
it has already responded 忄 0 a prepare reques
having a version number greater than n.
owb
_ Th e acceptor logs v on disk and sends ack 忄 0 the
proposer
If a majority of the acceptors have logged v on
their IS
e value iS chosen.
AI
A3
Phase 1
````

### 图片文字 OCR（en-US，待对照原页）

````text
CefiÆ
If the acc tor receives an accept request
("accept"
v), it accepts the proposal unless
it has already responded to a prepare reques
having a version number greater than n.
The acceptor logs v on disk and sends ack to the
proposer
If a majority of the acceptors have logged v on
their IS
e value is chosen.
value v
p
a rec,
Phase 1
ade decisl.b
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 21 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=21)

### 原始文字层

````text
Phase 3 (finalise)
• If the proposer gets acknowledgments 
from a majority of the acceptors, it 
tells everyone about the chosen value.
• The acceptors can tell all the learners 
about the chosen value.
21
P
A1
A2
A3
Phase 1
value v
Phase 2
decision made
The­o
𠱃 tell 𢜔
````

### 图片文字 OCR（en-US，待对照原页）

````text
Phase 3 (finalise)
If the proposer gets acknowledgments
from a ma ort of the acceptors, it
tells everyone about the chosen value.
The acceptors can tell all th lea ner
about the chosen value.
value v
p
Phase 1
Phase 2
decision made
21
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 22 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=22)

### 原始文字层

````text
• If the acceptor receives a prepare request with a 
larger version number, the acceptor abandons the 
engagement with the proposer with a smaller 
version number and engages the proposer with a 
larger version number.
– why
22
discussions
P1
A1
A2
A3
P2
wrenches
ㄧ
o
位 version number P
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
discussions
If the acceptor receives a prepare re
with a
on-numbecg the acceptor
andons he
r
ngagement with the proposer with a sma er
verston number and engages the proposer with a
version number.
_ why
AI
22
1
````

### 图片文字 OCR（en-US，待对照原页）

````text
discussions
If the acceptor receives a prepare re
with a
lgqger--vec$ion_numbecg the acceptor andons he
with the proposer with a sma er
verston number and engages the proposer with a
la
version number.
why
22
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 23 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=23)

### 原始文字层

````text
23
P1
A1
A2
A3
P2
crash
12 version number 1
中 not abandons
if wait fr pi reply
it in crash
waìtfnucnnnn
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
沪 宛 迁 a 怊
甲 “ 忙 for 胃
crash
AI
A3
23
````

### 图片文字 OCR（en-US，待对照原页）

````text
t? not
nit for p
crash
repla
23
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 24 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=24)

### 原始文字层

````text
• When an acceptor receives a prepare 
request (“prepare”, n) where n is 
greater than the version number of any 
prepare request the acceptor t has 
already responded, the acceptor sends 
out (“ack”, n, n’, v’) or (“ack”, n, - , -)
– What are n’ and v’?
24
P
A1
A2
A3
discussions
````

### 图片文字 OCR（en-US，待对照原页）

````text
discussions
When an acceptor receives a prepare
request ("prepare", n) where n is
greater than the version number of any
prepare request the acceptor t has
already responded, the acceptor sends
out ("ack", n, n', v') or ("ack", n,
— What are n' and v'?
24
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 25 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=25)

### 原始文字层

````text
25
P1
A1
A2
A3
Phase 1
value v’
P1
A1
A2
A3
Phase 1
value v’
P2
(“ack”, n, n’, v’)
o
继
浆
䉱
的
值
ft
ps Pl
version
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
/ åe 尸
ase
ase 丿
````

### 图片文字 OCR（en-US，待对照原页）

````text
l/a/ue v'
l/a/u
tack"
````

### 图表辅助说明

上下两组时序图对照：上图 P1 已把 v′ 发给 acceptor；下图 P2 发起另一轮 Phase 1，从相交的 acceptor 集合获知先前的 n′、v′，以保持选值一致。

## PDF 第 26 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=26)

### 原始文字层

````text
• If a majority of the acceptors have logs 
v on their disk, the value is chosen.
– Why?
26
P
A1
A2
A3
Phase 1
value v
discussions
version
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
discussions
． 工 f a majority of the acceptors have logs
v on their disk, the value is chosen.
_ Why?
value V
AI
A3
Phase 1
26
````

### 图片文字 OCR（en-US，待对照原页）

````text
discussions
If a majority of the acceptors have logs
v on their disk, the value is chosen.
Why?
value v
p
Phase 1
26
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 27 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=27)

### 原始文字层

````text
27
P
A1
A2
A3
Phase 1
value v’
Phase 2
P1
A1
A2
A3
Phase 1
value v’
P2
(“ack”, n, n’, v’)
P2 must receive the ack from one of A2 and A3 to move to phase 2.
当
i
i
ǐ
going
nor
ii
Chain
lick n.nu
ospone­cinck.mn v
I
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
AI
A2
A3
Phase 1
AI
A3
Phase 1
value
Phase 2
value V
（ "a c k"
P2 must receive the ack from 0 n e 0f A2 and A3 t0 move t0 phase 2 ·
27
````

### 图片文字 OCR（en-US，待对照原页）

````text
A1
Phase 1
Phase 1
value v'
Phase 2
value v'
P2 must receive the ack from one of A2 and A3 to move to phase 2.
("ack", n, n', v')
27
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 28 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=28)

### 原始文字层

````text
28
P
A1
A2
A3
Phase 1
value v’
Phase 2
P
A1
A2
A3
Phase 1
value v’
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
value
AI
A3
Phase 1
value
AI
A3
Phase 1
Phase 2
28
````

### 图片文字 OCR（en-US，待对照原页）

````text
value v'
p
A1
Phase 1
value v'
p
Phase 1
Phase 2
28
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 29 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=29)

### 原始文字层

````text
• After an acceptor receives the accept 
request of a proposer, can the acceptor 
ignore the prepare request from other 
proposers?
– Why?
29
P
A1
A2
A3
Phase 1
value v
discussions
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
discussions
After an acceptor receives the accept
request 0f a proposer, can the acce 忄 or
ignore the prepare request from 0 忄 er
proposers?
_ Why?
value V
AI
A3
Phase 1
29
````

### 图片文字 OCR（en-US，待对照原页）

````text
discussions
After an acceptor receives the accept
request of a proposer, can the acceptor
ignore the prepare request from other
proposers?
Why?
value v
p
Phase 1
29
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 30 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=30)

### 原始文字层

````text
30
P
A1
A2
A3
Phase 1
value v
crash
s
wait
to
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
AI
A3
Phase 1
value V
crash
30
````

### 图片文字 OCR（en-US，待对照原页）

````text
p
Phase 1
value v
crash
30
````

### 图表辅助说明

P 在完成黄色 Phase 1 并发出 Phase 2 消息后崩溃，黄色星形 crash 标在 proposer 的时间线上。图用于讨论 proposer 故障后协议的进展问题。

## PDF 第 31 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=31)

### 原始文字层

````text
discussions
• In the response to the prepare request 
message, is it possible for the proposer 
to receive two (“ack”, n, n’, v’) and (“ack”, 
n, n’’, v’’) such that v’ and v’’ are not the 
same?
31
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
discussions
． 工 n the response 忄 0 the prepare request
message, is it possible for the proposer
忄 0 receive 忄 wo (' 、 ack", n, n', v' ） and ("ack"
n, n", (") such that v' and v" are no 忄 the
same?
````

### 图片文字 OCR（en-US，待对照原页）

````text
discussions
In the response to the prepare request
message, is it possible for the proposer
to receive two ("ack", n, n', v') and ("ack",
n, n", v") such that v' and v" are not the
same?
31
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 32 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=32)

### 原始文字层

````text
• P1 sends prepare request to A1, A2 and A3, and 
gets ack from all. 
– At phase 2, A1 receives v1, but A2 and A2 have not 
receive v1 yet.
• P2 sends prepare request to A1, A2, and A3. P2 
receives A2’s and A3’s responds. But, not A1’s 
response.
– P2 starts phase 2 and send v2 to A1, A2 and A3. A2 and 
A3 receive v2. A1 has not received v2 yet.
• P3 sends prepare request to A1, A2 and A3. A1 
response with v1 and A2 and A3 response with v2.
• Which value will P3 use in its accept request?
• Which value is the agreed value?
32
in
````

### 图片文字 OCR（en-US，待对照原页）

````text
Pl sends prepare request to A1, A2 and A3, and
gets ack from all.
At phase 2,
but A2 and A2 have not
A1 receives vl
receive vl yet.
• P2 sends prepare request to A1, A2, and A3. P2
receives A2's and A3's responds
But, not A1's
response
P2 starts phase 2 and send v2 to A1, A2 and A3. A2 and
A3 receive v2 A1 has not received v2
yet.
P3 sends prepare request to A1, A2 and A3.
response with vl and A2 and A3 response with v2
• Which value will P3 use in its accept request?
• Which value is the agreed value?
Irv
32
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 33 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=33)

### 原始文字层

````text
• P1 sends prepare request to A1, A2 and A3, and 
gets ack from all. 
– At phase 2, A1 receives v1, but A2 and A2 have not 
receive v1 yet.
• P2 sends prepare request to A1, A2, and A3. P2 
receives A2’s and A3’s responds. But, not A1’s 
response.
– P2 starts phase 2 and send v2 to A1, A2 and A3. A2 and 
A3 receive v2. A1 has not received v2 yet.
• P3 sends prepare request to A1, A2 and A3. A1 
response with v1 and A2 and A3 response with v2.
• Which value will P3 use in its accept request?
• Which value is the agreed value?
32 solution log value i
````

### 图片文字 OCR（en-US，待对照原页）

````text
• Which value will P3 use in its accept request?
• Which value is the agreed value?
(o value
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 34 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=34)

### 原始文字层

````text
discussions
• The scheme can be optimised to reduce 
the number of messages
– Have a single acceptor
33
g
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
discussions
． The scheme can be optimised 忄 0 reduce
the number of messages
_ Have a single acceptor
33
````

### 图片文字 OCR（en-US，待对照原页）

````text
discussions
The scheme can be optimised to reduce
the number of messages
— Have a single acceptor
33
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 35 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=35)

### 原始文字层

````text
Safeness
• As a value is chosen when a majority of the 
acceptors log v sent by the proposer in 
phase 2, if v in proposal (v, n) is chosen, 
the value in all accepted proposals (v’, n’) 
where n’>n must satisfy v = v’
– In the respond to the prepare request, at least 
one acceptor informs the proposer of the value 
that the majority acceptors have accepted.
– The proposer uses accepted value with the 
largest version number as its own proposed 
value in the accept request.
34
````

### 图片文字 OCR（en-US，待对照原页）

````text
Safeness
As a value is chosen when a majority
of the
acceptors log v sent by the proposer in
phase 2, if v in proposal (v, n) is chosen,
the value in all accepted proposals (v', n')
where n'>n must satisfy v = v'
— In the respond to the prepare request at least
one acceptor informs the proposer of the value
that the majority acceptors have accepted.
— The proposer uses accepted value with the
largest version number as its own proposed
value in the accept request.
34
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 36 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=36)

### 原始文字层

````text
Liveness
• Per FLP, Paxos cannot guarantee liveness.
• Proposer p completes phase 1 for a proposal number n1. 
• Another proposer q then completes phase 1 for a proposal number n2 > n1. 
• Proposer p’s phase 2 accept requests for a proposal numbered n1 are ignored because the 
acceptors have all promised not to accept any 
new proposal numbered less than n2. 
• Proposer p then begins phase 1 for a new proposal number n3 > n2, causing the second phase 2 accept requests of proposer q to be 
ignored. 
• And so on.
35
in 中次
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Liveness
Per FLP, Paxos cannot guarantee liveness.
Proposer completes phase 1 for a proposal
rwmber
Another proposer q then completes phase 1 for
a proposal number n2 > nl.
proposal num
acceptors have all promise no 忄 忄 0 accept any
new proposal numbered less than n2.
Proposer p then be ins hase 1 for a new
proposal number causing the second
phase 2 accept requests of proposer q 忄 0 be
tgnored.
And so on.
35
````

### 图片文字 OCR（en-US，待对照原页）

````text
Liveness
Per FLP, Paxos cannot guarantee liveness.
Proposer p completes phase 1 for a proposal
number nl.
Another proposer q then completes phase 1 for
a proposal number n2 > nl.
Proposer p's phase 2 accept requests for a
proposal numbered nl are iqnored because the
acceptors have all promised not to accept any
new proposal numbered less than n2.
Proposer p then beqins phase 1 for a new
proposal number nS> n2, causing the second
phase 2 accept requests of proposer q to be
Ignored.
And so on.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 37 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=37)

### 原始文字层

````text
36
P
A1
A2
1
Q
A3
不停的 情况
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
AI
36
````

### 图片文字 OCR（en-US，待对照原页）

````text
A1
36
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 38 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=38)

### 原始文字层

````text
37
P
A1
A2
1
Q
A3
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
37
````

### 图片文字 OCR（en-US，待对照原页）

````text
37
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 39 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=39)

### 原始文字层

````text
38
P
A1
A2
1
Q
A3
2
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
38
````

### 图片文字 OCR（en-US，待对照原页）

````text
38
````

### 图表辅助说明

两个 proposer P、Q 竞争：P 先发版本 1，Q 随后发送版本 2 的 prepare。箭头跨过相同的三个 acceptor，展示更高版本请求如何打断较低版本的进展；这是连续动画中的一个中间状态。

## PDF 第 40 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=40)

### 原始文字层

````text
39
P
A1
A2
1
Q
A3
2
Cfs
ignored
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
AI
39
````

### 图片文字 OCR（en-US，待对照原页）

````text
39
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 41 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=41)

### 原始文字层

````text
40
P
A1
A2
1
Q
A3
2
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
AI
40
````

### 图片文字 OCR（en-US，待对照原页）

````text
40
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 42 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=42)

### 原始文字层

````text
41
P
A1
A2
1
Q
A3
2
9
3山兰 larger version
numbers
Üg
not terminal
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
1
AI
2
0
41
````

### 图片文字 OCR（en-US，待对照原页）

````text
-v. C (ader
LAvtberJ
41
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 43 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=43)

### 原始文字层

````text
Paxos vs Virtual Synchrony
• Ordering
– Paxos enforces a strict global execution order of commands,
– Virtual Synchrony only ensures agreement on the set of 
messages received within a view, without imposing an order.
• Failure Handling
– Virtual Synchrony ensures messages received by at least one 
process are propagated to all surviving processes during a view 
change.
– Paxos maintains a consistent log through quorum-based decision-making. 
• Once a decision is made, it is recorded by a majority of nodes, 
ensuring that after a failure, at least one surviving node will inform the leader of the decision, allowing the system to continue making progress without losing previously agreed-upon values.
42
www.­m
````

### 图片文字 OCR（en-US，待对照原页）

````text
Paxos vs Virtual Synchrony
Ordering
Paxos enforces a strict global execution order of commands,
Virtual Synchrony only ensures agreement on the set of
messages received within a view, without imposing an rder.
Failure Handling
Virtual Synchrony ensures messages received by at least one
process are propagated to all surviving processes during a view
chan e.
axo maintains a onsistent Io through quorum-based
ects:on-makin
• Once a ecisio is made, it is recorded by a a•orit o node
ensurinq t at a ter a failure at least one surviving no e w: Inform
the leader of the decision, allowing the system to continue making
progress without losing previously agreed-upon values.
42
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 44 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=44)

### 原始文字层

````text
Paxos in real life
• The replication services of some modern 
file systems uses Paxos
– Google BigTable
– Apache ZooKeeper, Yahoo
– Many MS products, e.g. SQL server 
clusters
43
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Paxos in real life
． The replication services Of some modern
file systems uses Paxos
_ Goog BigTable
_ Apache ZooKeeper, Yahoo
_ Many MS products, e.g. SQL server
clusters
43
````

### 图片文字 OCR（en-US，待对照原页）

````text
Paxos in real life
The replication services of some modern
file systems uses Paxos
Google BigTable
— Apache ZooKeeper, Yahoo
— Many MS products, e.g. SQL server
clusters
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 45 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=45)

### 原始文字层

````text
reviews
• Understand how FLP impossibility theorem affect real 
system design.
• Give a scenario in which the Paxos algorithm cannot 
terminate.
• What are the safety conditions of the Paxos algorithm?
• Paxos uses version numbers to help the acceptors to 
decide whether they should respond to a received prepare 
request message. Use an example to explain why version 
numbers are important.
– hint: Without a version number, an acceptor needs to 
response to any prepare message. Consider whether you can 
find a scenario in which if two proposers send their prepare 
messages at the same time, none of them can get 
acknowledgement from a majority of the acceptors.
44
````

### 图片文字 OCR（en-US，待对照原页）

````text
reviews
Understand how FLP impossibility theorem affect real
system design.
• Give a scenario in which the Paxos algorithm cannot
terminate.
What are the safety conditions of the Paxos algorithm?
• Paxos uses version numbers to help the acceptors to
decide whether they should respond to a received prepare
request message. Use an example to explain why version
numbers are important.
hint: Without a version number, an acceptor needs to
response to any prepare message. Consider whether you can
find a scenario in which if two proposers send their prepare
messages at the same time, none of them can get
acknowledgement from a majority of the acceptors.
44
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 46 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=46)

### 原始文字层

````text
reviews
• In Paxos, what are the pros and cons of having 
a single acceptor?
• How does the Paxos algorithm guarantee that 
only the consensus value is propagated?
– Hint: A decision is made when a majority of the 
acceptors have recorded the proposed value in the 
2nd phase.
• Assume that a membership service that 
implements virtual synchrony is available and 
only one node can crash. Explain how the 
implementation of the Paxos algorithm can use 
the membership service to ensure the 
termination of the consensus algorithm.
– Hint: Consider making the membership service to 
choose an unique proposer for each view.
45
````

### 图片文字 OCR（en-US，待对照原页）

````text
reviews
In Paxos, what are the pros and cons of having
a single acceptor?
How does the Paxos algorithm guarantee that
only the consensus value is propagated?
Hint: A decision is made when a majority of the
acceptors have recorded the proposed value in the
2nd phase.
Assume that a membership service that
implements virtual synchrony is available and
only one node can crash. Explain how the
implementation of the Paxos algorithm can use
the membership service to ensure the
termination of the consensus algorithm.
Hint: Consider making the membership service to
choose an unique proposer for each view.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 47 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=47)

### 原始文字层

````text
Further readings
• Michael J. Fischer, Nancy A. Lynch, and Michael 
S. Paterson. 1985. Impossibility of distributed 
consensus with one faulty process. J. ACM 32, 
2 (April 1985), 374-382.
• Leslie Lamport. 1998. The part-time parliament. 
ACM Trans. Comput. Syst. 16, 2 (May 1998), 
133-169.
• Lamport, Leslie (2001). Paxos Made Simple ACM 
SIGACT News (Distributed Computing Column) 
32, 4 (Whole Number 121, December 2001) 51-
58
46
````

### 图片文字 OCR（en-US，待对照原页）

````text
Further readings
Michael J. Fischer, Nancy A. Lynch, and Michael
S. Paterson. 1985. Impossibility of distributed
consensus with one faulty process. J. ACM 32,
2 (April 1985), 374-382.
Leslie Lamport. 1998. The part-time parliament.
ACM Trans. Compute syst. 16, 2 (May 1998),
133-169.
Lamport, Leslie (2001). Paxos Made Simple ACM
SIGACT News (Distributed Computing Column)
32, 4 (Whole Number 121, December 2001) 51-
58
46
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 48 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=48)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
工 n the following discussion, assume that the version
numbers of the three proposers, PI, P2 and P3, satisfy ：
P3s > P2's > P1's
PI sends prepare request 忄 0 AI, A2 and A3, and gets ack
from ·
十 hase 2 ， AI receives vl, but 2 and A2 have not receive
P2 sends prepare request to AI, 燕 2 ， and A3. P2 receives
2 ' s and 引 s responds. But, A 1 has not received the
忄 message.
P2 starts hase 2 and send v2 忄 0 燕 1 ， 2 and A3. A2 and A3
receive v2P 1 has no 忄 received v2 yet.
P3 sends prepare request 忄 0 1 ， 2 and 燕 3 · 1 responses
with vl and 2 and 3 response with v2.
Which value will P3 use in its accept request?
Which value is the agreed value?
````

### 图片文字 OCR（en-US，待对照原页）

````text
In the following discussion, assume that the version
numbers of the three proposers, Pl, P2 and P3, satisfy:
P3's > P2's > Pl's
Pl sends prepare request to A1, A2 and A3, and gets ack
from all.
At hase 2, A1 receives VI, but A2 and A2 have not receive
• P2 sends prepare request to A1, A2, and A3. P2 receives
A2's and A3s responds. But, A1 has not received the
requzst message.
P2 starts Dhase 2 and send v2 to A1, A2 and A3. A2 and A3
receive vZ. A1 has not received v2 yet.
P3 sends prepare request to A1, A2 and A3. A1 responses
with vl and A2 and A3 response with v2.
Which value will P3 use in its accept request?
Which value is the agreed value?
33
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 49 页

[查看此页](../../../../notes/original/711/1/S8%2Bpaxos.pdf#page=49)

> 本页无可提取文字层；见 OCR 或图示说明。

> OCR 未识别出可靠文字；本页可能以图形、手写公式或空白为主。

### 图表辅助说明

低对比度白板照片：多条横线标记 P1、A1、A2、A3、P2、P3，并用斜箭头画出 proposer 与 acceptor 的消息交错。具体消息编号与部分手写值无法可靠辨认，不能据此补造完整执行序列。

