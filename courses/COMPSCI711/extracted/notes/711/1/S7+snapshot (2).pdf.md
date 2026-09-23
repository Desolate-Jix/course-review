# S7+snapshot (2).pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI711/notes/original/711/1/S7+snapshot (2).pdf`
- [打开原文件](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf)
- 原文件 SHA-256：`c567d56f20ac1d1e0e391c2843fd1e60038fe184681ffd8a35a26561f7319718`
- 文件索引：F068；PDF 总页数：26
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=1)

### 原始文字层

````text
1
Global state and snapshot
 A distributed system consists of processes that 
communicate asynchronously with each other 
through message passing
 Each process has a local state and states for each 
of its communication channels
 The local state of a process is the state of the 
process’ local memory
 The state of a communication channel is the set of 
messages sent over the channel less the messages that have been received and processed by the 
receiver along the channel
 The global state of a distributed system is a collection of the local states of the processes and the states of the communication channels of all 
the processes
- 异步通信
Crttcoo 发出 一
收到
ooo
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
引 oba 《 state and snapshot
distributed system consists of processes
that
囗
communicategiynchcgogysJ.y with each other
步 笾 宿
through message paSSl ng
Each process has a local state and states for each
囗
Of itS communicatioF-cfifiETs
ocess is the state of the
囗 The
囗 Th state f a
communicatio channe
is th
Sent over the chann
the messages
me
忄 h 酣 have been received and processed by the
receiver 0
channel
囗 The
》 oba 》 s 忄 酣
ibuted system is a
collec 《 on
0 th ocal s te of the processes and
the states of the
ca i C anne Of
the processes
1
````

### 图片文字 OCR（en-US，待对照原页）

````text
Global state and snapshot
A distributed system consists of processes
that
communicate asynchronously with each other
through message passtng
Each process has a local state and states for each
of its communication-cfifiETs
ocess is the state of the
o The
te o
oc
process' local
emory
Th state f a communicatio channe
is th
sent over the chann
the messages
me
that have been received and processed by the
receiver alo
channel
o The
lobal stat
ibuted system is a
collec ton o th ocals te of the processes and
the states of the
•cai c anne of all
the processes
1
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=2)

### 原始文字层

````text
2
c
rece.ie
i
GLOlocal State
````

### 图片文字 OCR（en-US，待对照原页）

````text
ecot
nov 1
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=3)

### 原始文字层

````text
3
snapshot
 Recording a snapshot of a distributed 
system is important for many applications
 Failure recovery
 Debugging a distributed system
 Due to the lack of a global clock, obtaining 
a consistent global snapshot of a 
distributed system is not trivial
 Example: transfer money between two accounts 
located at two different sites
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
snapshot
0 Recording a snapshot of a distributed
system is important for many applications
Failure recovery
o
Debugging a distributed system
O
o Due to the lack of a global clock
obtaining
a consistent global snapshot of a
distributed system is not trivial
Example: transfer money between two accounts
O
located at two different sites
3
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=4)

### 原始文字层

````text
4
T1 A1 = 500 A2 = 600
an k system
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
AI = 500
A2 = 600
4
````

### 图片文字 OCR（en-US，待对照原页）

````text
bank 9ysfem.
A2 = 600
A1 = 500
4
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=5)

### 原始文字层

````text
5
T1 A1 = 500 A2 = 600
T2 A1 = 500
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
A2 = 600
AI = 500
T2
AI = 500
5
````

### 图片文字 OCR（en-US，待对照原页）

````text
A2 = 600
A1 = 500
A1 = 500
5
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=6)

### 原始文字层

````text
6
T1 A1 = 500 A2 = 600
T2 A1 = 500
T3 A1 = 450
A2 = 600
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
A2 = 600
AI = 500
T2
AI = 500
T3
AI = 450
A2 = 600
6
````

### 图片文字 OCR（en-US，待对照原页）

````text
A2 = 600
A1 = 500
A1 = 500
A1 = 450
A2 = 600
6
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=7)

### 原始文字层

````text
7
T1 A1 = 500 A2 = 600
T2 A1 = 500
T3 A1 = 450
A2 = 600
T4 Execute credit A2 50 A2 = 650
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
A2 = 600
AI = 500
T2
AI = 500
T3
AI = 450
A2 = 600
A2 = 650
Execute credit A2 50
````

### 图片文字 OCR（en-US，待对照原页）

````text
A2 = 600
A1 = 500
A1 = 500
A1 = 450
A2 = 600
A2 = 650
Execute credit A2 50
````

### 图表辅助说明

转账时序：A1 原为 500、A2 原为 600；A1 扣除 50 后向 A2 发出加款消息，A2 最后变为 650。黄色标记却分别选中旧 A1=500 与新 A2=650，展示在不一致时刻记录余额会得到错误总量。

## PDF 第 8 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=8)

### 原始文字层

````text
8
T1 A1 = 500 A2 = 600
T2 A1 = 500
T3 A1 = 450
A2 = 600
T4 A2 = 650
T5
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
A2 = 600
AI = 500
T2
AI = 500
T3
AI = 450
A2 = 600
A2 = 650
T5
8
````

### 图片文字 OCR（en-US，待对照原页）

````text
A2 = 600
A1 = 500
A1 = 500
A1 = 450
A2 = 600
A2 = 650
8
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=9)

### 原始文字层

````text
9
T1 A1 = 500 A2 = 600
T2 A1 = 500
T3 A1 = 450
A2 = 600
T4
T5
T6 restored A1 = 500
A2 = 650
restore A2 = 650
_cheekpoint
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
A2 = 600
AI = 500
T2
AI = 50
T3
AI = 450
A2 = 600
A2 = 650
T5
T6
restored AI = 500
restore A2 = 650
9
````

### 图片文字 OCR（en-US，待对照原页）

````text
A2 = 600
A1 = 500
FC he-dc pojn+
A1 =
A1 = 450
A2 = 600
A2 = 650
restored A1 = 500
restore A2 = 650
9
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=10)

### 原始文字层

````text
10
Consistent global state
 A global state of a distributed system is 
consistent if the two conditions below are 
satisfied:
 C1: If the sending of a message is recorded in 
the state of the sender, the receiving of the 
message must be recorded in the state (i.e., 
local state or channel states) of the receiver 
 C2: Messages that have not been recorded by 
the senders should not be recorded by the 
receivers
一
保证发出 和接收
状态 数
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Consistent global state
囗 global state of a distributed system is
consistent if the 忄 wo conditions below are
satisfied:
0 CI: If the sending
Of a message iS recorded
fthesender, the receiving of the
the state 0
message must be recorded in the state (i.e.,
《 oca 》 state 0 r channel states) of the receiver
0 C2: Messages 忄 h 酣 have
no 忄 been recorded
the senders
should not be recorded by the
recetvers
````

### 图片文字 OCR（en-US，待对照原页）

````text
Consistent global state
A global state of a distributed system is
consistent if the two conditions below are
satisfied:
Cl: If the sending of a message is recorded in
o
*thesender, the receiving of the
the state o
message must be recorded in the state (i.e.,
local state or channel states) of the receiver
C2: Messages that have
not been recorded by
O
the senders should not be recorded by the
receivers
10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=11)

### 原始文字层

````text
11
Issues in recording a global state
 How to distinguish between the messages to be 
recorded in the snapshot from those not to be 
recorded.
 Any message that is sent by a process before recording 
its snapshot, must be recorded in the global snapshot 
(from C1).
 Any message that is sent by a process after recording its 
snapshot, must not be recorded in the global snapshot 
(from C2).
 How to determine the instant when a process 
takes its snapshot.
 A process pj must record its snapshot before processing 
a message mij that was sent by process pi after recording 
its snapshot.
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Issues in recording a global state
How to distinguish between the messages to be
recorded in the snapshot from those not to be
recorded.
Any message that is sent by a process before recording
O
its snapshot, must be recorded in the global snapshot
(from Cl).
Any message that is sent by a process after recording
its
O
snapshot, must not be recorded in the global snapshot
(from C2).
o How to determine the instant when a process
takes its snapshot.
A process PJ must record its snapshot before processing
O
a message that was sent by process Pl
after recording
its snapshot.
11
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=12)

### 原始文字层

````text
12
T1 A1 = 500 A2 = 600
T2 A1 = 500
T3 A1 = 450
A2 = 600
T4
T5
T6 restored A1 = 500
A2 = 650
restore A2 = 650
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
A2 = 600
AI = 500
T2
AI = 500
T3
AI = 450
A2 = 600
A2 = 650
T5
T6
restored AI = 500
restore A2 = 650 1
````

### 图片文字 OCR（en-US，待对照原页）

````text
A2 = 600
A1 = 500
A1 = 500
A1 = 450
A2 = 600
A2 = 650
restored A1 = 500
restore A2 = 650
12
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=13)

### 原始文字层

````text
13
Snapshot algorithm for FIFO channels
 The Chandy-Lamport algorithm uses a control 
message, called a marker to separate messages in 
the channels.
 After a site has recorded its snapshot, it sends a 
marker, along all of its outgoing channels before 
sending out any more messages.
 A marker separates the messages in the channel 
into those to be included in the snapshot from 
those not to be recorded in the snapshot.
 A process should record its snapshot when it 
receives the first marker on any of its incoming 
channels.
marker 所有的 Process收到mark
message
record再向所有
发出markermessg
水管堤 pattern o
Check 是否在发出 雕一做
not rein
收到marl­er
䘵 快照
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
囗 The Chandy-Lamp r algorithm use a co 酣
message, called a
ark
忄 0 separate message in
the channels.
囗 After a site has recorded its snapshot, it sends a
marker, along of its outgoing channels before
sending ou 忄 a ny more messages.
marker
separates the messages in the channel
囗
into those 忄 0 be included in the snapshot from
those not 忄 0 be recorded in the snapshot.
囗 process should
record
its snapshot when 汁
receives the first marker on any Of itS incoming
channels.
````

### 图片文字 OCR（en-US，待对照原页）

````text
léYJ
Snapshot algorithn!tprpfIFO
The Chandy-Lamp r algorithm use a cont
message, called a
n hct tard
the channels.
h#ÉeuDh4
o After a site has recorded its snapshot
it sends a
marker, along all of its outgoing channels before
sending out any more messages.
A marker separates the messages in the channel
into those to be included in the snapshot from
those not to be recorded in the snapshot.
1k?l)
A process should record its snapshot when it
receives the first marker on any of its incoming
channels.
13
````

### 图表辅助说明

手写示意把进程 P1、P2 以通道连接，并用 marker 划分快照前后的消息。正文规则是记录本地状态后先在出通道发送 marker；首次收到 marker 时记录本地状态，其他入通道则记录边界内的在途消息。

## PDF 第 14 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=14)

### 原始文字层

````text
14
A
BC
````

> OCR 未识别出可靠文字；本页可能以图形、手写公式或空白为主。

### 图表辅助说明

Chandy–Lamport 快照动画：初始 A、B、C 均未着色，红色小块是各通道中的普通消息。 黑色箭头为有向通道，红色表示普通消息、蓝色表示 marker。

## PDF 第 15 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=15)

### 原始文字层

````text
15
A B
C
queue for record
i
````

### 图片文字 OCR（en-US，待对照原页）

````text
quae fir buord.
15
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=16)

### 原始文字层

````text
16
A
BC
````

> OCR 未识别出可靠文字；本页可能以图形、手写公式或空白为主。

### 图表辅助说明

Chandy–Lamport 快照动画：A 已记录本地状态变绿，并发出蓝色 marker；粉色框表示正在记录的入通道状态。 黑色箭头为有向通道，红色表示普通消息、蓝色表示 marker。

## PDF 第 17 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=17)

### 原始文字层

````text
17
A B
C
O都在 marker前
chunalstat­.­co
g
B Send marker to A.c
record all the message
dtneincomecham en.no 因为 在 泼出mark
之后 需要记录
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
亠
0
0
0
````

### 图片文字 OCR（en-US，待对照原页）

````text
B
@ B Send
nll
17
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 18 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=18)

### 原始文字层

````text
18
A
BC
it
C
````

> OCR 未识别出可靠文字；本页可能以图形、手写公式或空白为主。

### 图表辅助说明

Chandy–Lamport 快照动画：A、B 均已变绿，B 也发送 marker；A 的粉色框已累积在途消息，C 尚未记录本地状态。 黑色箭头为有向通道，红色表示普通消息、蓝色表示 marker。

## PDF 第 19 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=19)

### 原始文字层

````text
19
A
BC
````

> OCR 未识别出可靠文字；本页可能以图形、手写公式或空白为主。

### 图表辅助说明

Chandy–Lamport 快照动画：A、B 已记录状态，普通消息继续到达尚未变绿的 C；蓝色 marker 仍在通道中。 黑色箭头为有向通道，红色表示普通消息、蓝色表示 marker。

## PDF 第 20 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=20)

### 原始文字层

````text
20
A
BC
````

> OCR 未识别出可靠文字；本页可能以图形、手写公式或空白为主。

### 图表辅助说明

Chandy–Lamport 快照动画：C 也变绿并发送 marker，三个进程的本地状态均已记录；部分通道上的 marker 尚未到达，通道记录过程仍要继续。 黑色箭头为有向通道，红色表示普通消息、蓝色表示 marker。

## PDF 第 21 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=21)

### 原始文字层

````text
21
A
BC
A
BC
o
````

### 图片文字 OCR（en-US，待对照原页）

````text
21
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 22 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=22)

### 原始文字层

````text
22
 The algorithm can be initiated by any process by 
executing the “Marker Sending Rule” by which it 
records its local state and sends a marker on each 
outgoing channel.
 A process executes the “Marker Receiving Rule” on 
receiving a marker. If the process has not yet 
recorded its local state, it records the state of 
the channel on which the marker is received as 
empty and executes the “Marker Sending Rule” to 
record its local state.
 The algorithm terminates after each process has 
received a marker on all of its incoming channels.
 All the local snapshots get disseminated to all 
other processes and all the processes can 
determine the global state.
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
The algorithm can be initiated by any process by
executing the "Marker Sending Rule" by which it
records its local state and sends a marker on each
outgoing channel.
A process executes the "Marker Receiving Rule" on
receiving a marker. If the process has not yet
recorded its local state, it records the state of
the channel on which the marker is received as
empty and executes the "Marker Sending Rule" to
record its local state.
The algorithm terminates after each process has
received a marker on all of its incoming channels.
All the local snapshots get disseminated to all
other processes and all the processes can
determine the global state.
22
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 23 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=23)

### 原始文字层

````text
23
Marker Sending Rule for process i
 Process i records its state.
 For each outgoing channel C on which a marker has 
not been sent, i sends a marker along C
Marker Receiving Rule for process j
On receiving a marker along channel C:
 if j has not recorded its state then
Record the state of C as the empty set
Follow the “Marker Sending Rule”
 else
Record the state of C as the set of messages 
received along C after j ’s state was recorded 
and before j received the marker along C
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Marker Sending Rule for process i
Process i records its state.
For each outgoing channel C on which a marker has
not been sent, i sends a marker along C
Marker Receiving Rule for process j
On receiving a marker along channel C:
o if j has not recorded its state then
Record the state of C as the empty set
Follow the "Marker Sending Rule"
o else
Record the state of C as the set of messages
received along C after j 's state was recorded
and before j received the marker along C
23
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 24 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=24)

### 原始文字层

````text
24
Correctness
 Due to FIFO property of channels, it follows that 
no message sent after the marker on that channel 
is recorded in the channel state. Thus, condition 
C2 is satisfied.
 When a process pj receives message mij that 
precedes the marker on channel Cij , it acts as 
follows: 
 If process pj has not taken its snapshot yet, then it 
includes mij in its recorded snapshot. 
 Otherwise, it records mij in the state of the channel Cij . 
 Thus, condition C1 is satisfied.
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Correctness
Due to FIFO property of channels, it follows that
no message sent after the marker on that channel
is recorded in the channel state. Thus, condition
C2 is satisfied.
When a process p. receives message mij that
precedes the marker on channel Cij , it acts as
follows:
If process PJ has not taken its snapshot yet, then it
O
includes rniJ in its recorded snapshot.
Otherwise, it records
t•nIJ in the state of the channel CIJ
O
Thus, condition Cl is satisfied.
O
24
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 25 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=25)

### 原始文字层

````text
25
reviews
 Why is obtaining a consistent global snapshot difficult in a 
distributed system? Use an example to support your 
argument.
 What are the conditions that need to be satisfied to make a 
global state consistent?
 For some systems, the Chandy-Lamport algorithm can be 
modified so that all the channel states are recorded as 
empty. Which property do these systems need to possess 
and how Chandy-Lamport algorithm should be modified so 
that the algorithm does not need to record the channel 
state?
 Modify the Chandy-Lamport algorithm so that it handles the 
case in which several sites initiates the snapshot algorithm 
simultaneously. You should minimize the amount of messages 
being exchanged as much as possible.
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
reviews
Why is obtaining a consistent global snapshot difficult in a
distributed system? Use an example to support your
argument.
What are the conditions that need to be satisfied to make a
global state consistent?
For some systems, the Chandy-Lamport algorithm can be
modified so that all the channel states are recorded as
empty. Which property do these systems need to possess
and how Chandy-Lamport algorithm should be modified so
that the algorithm does not need to record the channel
state?
Modify the Chandy-Lamport algorithm so that it handles the
case in which several sites initiates the snapshot algorithm
simultaneously. You should minimize the amount of messages
being exchanged as much as possible.
25
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 26 页

[查看此页](../../../../notes/original/711/1/S7%2Bsnapshot%20%282%29.pdf#page=26)

### 原始文字层

````text
26
readings
 K.M. Chandy and L. Lamport, Distributed 
snapshots: determining global states of 
distributed systems, ACM transactions on 
Computer Systems, 3(1), 1985, 63-75
 M. Spezialetti and P. Kearns, Efficient 
distributed snapshots, Proceedings of the 
6th Intl. Conf. on distributed computing 
systems, 1986, 382-388
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
readings
K.M. Chandy and L. Lamport, Distributed
snapshots: determining global states of
distributed systems, ACM transactions on
Computer Systems, 3(1), 1985, 63-75
M. Spezialetti and P. Kearns, Efficient
distributed snapshots, Proceedings of the
6th Intl. Conf. on distributed computing
systems, 1986, 382-388
26
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

