# S5+deadlock.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI711/notes/original/711/1/S5+deadlock.pdf`
- [打开原文件](../../../../notes/original/711/1/S5%2Bdeadlock.pdf)
- 原文件 SHA-256：`e62dd97c7dd2413ccf27952392977b8fb789fced737fee0bdb4cb27eb94b6310`
- 文件索引：F064；PDF 总页数：33
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=1)

### 原始文字层

````text
1
The Echo Algorithm
 The echo algorithm can be used to collect 
and disperse information in a distributed 
system
 It was originally designed for learning network 
topology. But, it can be applied for solving many 
other problems
 Each node only knows and communicates 
with its neighbours.
respond
i­ii
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
tvs
The EcÅo Algorithm
The echo algorithm can be used to collect
and disperse information in a distributed
system
It was originally designed for learning network
o
topology. But, it can be applied for so Ving many
Niher—pnoblems
Each node only knows and communicates
with its neighbours.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=2)

### 原始文字层

````text
Éri
ǖ
n
echotue
囋
i
Send echo
first to l­ift5
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
aS5 幽
） 艹 3
````

### 图片文字 OCR（en-US，待对照原页）

````text
assumæ
40
echo
euo
tefl
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=3)

### 原始文字层

````text
2
 The initiator starts the algorithm by sending 
probes to all its neighbours.
 The algorithm terminates when the initiator 
receives echoes from all its neighbours.
 A non-initiator node replicates and sends probes 
to its neighbours after receiving a probe.
 A non-initiator node sends an echo to the node 
from which it receives the probe when the node 
has received echoes from all its neighbours.
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
The initiator starts the algorithm by sending
probes to all its neighbours.
The algorithm terminates when the initiator
receives echoes from all its neighbours.
o A non-initiator node replicates and sends probes
to its neighbours after receiving a probe.
o A non-initiator node sends an echo to the node
from which it receives the probe when the node
has received echoes from all its neighbours.
2
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=4)

### 原始文字层

````text
3
Deadlock detection in distributed systems
System model
 A computation consists of a set of processes 
running on a collection of processors connected by 
a communication network
 Without loss of generality, it is assumed that each 
process runs on a different processor
 The processors do not share a common global 
memory and communicate solely by passing 
messages over the communication network
 Processes make exclusive access to resources and 
there is only one copy for each resource
 A process can be in two states, running or blocked
 A blocked process is waiting to acquire some resources error errors
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Deadlock detection in distributed systems
System model
A computation consists of a set of processes
running on a collection of processors connected by
a communication network
Without loss of generality, it is assumed that each
process runs on a different processor
The processors do not share a common global
memory and communicate solely by passing
over the communication network
messages
Processes make exclusive access to resources and
there is only one copy for each resource
running or &lggeg
A process can be in two states,
A blocked process is waiting to acquire some resources
O
3
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=5)

### 原始文字层

````text
4
Wait-for graph
 A wait-for graph is a directed graph
 In a wait-for graph, 
 nodes are processes
 There is a directed edge from node P1 to P2 if 
P1 is blocked and waiting for P2 to release some 
resources
 Example
 P1: w1[x] w1[y]r1[x]
 P2: r2[y] r2[x]w2[y]
P1 P2
Our Oas­is
are
iouss wait g
wait X
Pi access I ˋ
12access g
blocked
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Wait-for graph
A wait-for graph is a directed graph
o In a wait-for graph,
o nodes
are processes
T ere is a directed
from node Pl to P2 if
O
Pl s blocked and wai tng or P2 to release some
esources
4e50tyæ.
o Example
Pl: wl[x]
O
P2: r21yJ
O
Pl aces; X
1/0cLJ,
wnt x
phi.eg ,
4
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=6)

### 原始文字层

````text
5
Models of Deadlock
 There are two deadlock models 
 AND model (resource model) 
 OR model (communication model)
 In the AND model 
 A process is permitted to request a set of resources. 
 The process remains blocked until it is granted all
the resources it has requested. 
• Therefore, requests of this type are called AND requests. 
 To find a deadlock in the AND model it is necessary 
to find a cycle in the wait-for graph. 
x y z
0
0
mnotc
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Models of Deadlock
There are two deadlock models
AND model (resource model)
O
o OR model (communication model)
o In the AND model
A process is permitted to request a
set of resources.
O
The process remains blocked until it is granted
O
the resources it has requested.
• Therefore, requests of this type are called AND requests.
To find a deadlock in the
AND model it is necessary
O
to find a cycl
the wait-for graph.
z
5
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=7)

### 原始文字层

````text
6
 In the OR model 
 A process can communicate with a set of other 
processes. 
 The process can make progress as long as one of 
the communication occurs. 
• Therefore, in this model a cycle in the wait-for graph does 
not necessarily mean a deadlock exists
 To detect a deadlock, it is necessary to detect a 
knot in the wait-for graph. 
• All the processes being waited by other processes are in a 
cycle.
A knot in a directed graph is a collection of vertices and edges with 
the property that every vertex in the knot has outgoing edges, and 
all outgoing edges from vertices in the knot terminate at other 
vertices in the knot. Thus, it is impossible to leave the knot while 
following the directions of the edges. 
0
不一定deadlock
结 everyone waiting长
some0
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
囗 ln the OR model
process can communicate with a
set of other
0
processes.
0 The process can make progress aS long aS
one
the communication occurs.
no 忄 necessarily mean a dea OCk exists
0 To detect a deadlock, it is necessary 忄 0 detect a
knot in the wait-for graph.
． 川 《 the processes being waited by other processes are in a
cycle.
knot in a directed graph is a collection 0f vertices an edges with
the property that every vertex in the knot has outgoing edges
and
all outgoing edges from vertices in the knot
terminate at other
vertices in the knot. Thus, 汁 is impossible leave the knot while
following the directions of the edges.
6
````

### 图片文字 OCR（en-US，待对照原页）

````text
o In the OR model
A process can communicate with a
set of other
O
processes.
The process can make progress as long as one of
O
the communication occurs.
• Therefore, in this model cyc in the watt- or g aph does
not necessarily mean a dea ock exists
To detect a deadlock, it is necessary to detect a
O
knot in the wait-for graph.
• All the processes being waited by other processes are in a
One (.IJØI%IS -W'
cycle.
A knot in a directed graph is a collection of vertices an edges with
the property that every vertex in the knot has outgoing edges
and
all outgoing edges from vertices in the knot
terminate at other
vertices in the knot. Thus, it is impossible to leave the knot while
following the directions of the edges.
6
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=8)

### 原始文字层

````text
7
B
A
C B
A
C
D
or model
no outgoing
i edge
O­r
outgoing edge
end with node
inthe same set
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
end
````

### 图片文字 OCR（en-US，待对照原页）

````text
or m,DJe.J
no o
e end node
set.
In
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=9)

### 原始文字层

````text
8
Deadlock Detection
A deadlock detection algorithm must satisfy the 
following two conditions:
 the scheme does not detect a false deadlock
 all deadlocks will be detected
Resolution of a detected deadlock
 Deadlock resolution involves breaking existing 
wait-for dependencies between the processes
 It involves rolling back one or several deadlocked 
processes and assigning their resources to blocked 
processes so that they can resume their execution
邑
__
0
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Deadlock Detection
deadlock detection algorithm must satisfy the
following 忄 WO conditions:
the scheme does not detect a als deadlock
deadlocks will be detected
ResoIution of a detected deadlock
DeadIock resolution involves breaking existing
囗
wait-for dependencies between the processes
囗 工 忄 involves rolling back one 0 r several deadlocked
processes and assigning their resources 忄 0 blocked
processes SO that they can resume their execution
8
````

### 图片文字 OCR（en-US，待对照原页）

````text
Deadlock Detection
A deadlock detection algorithm must satisfy the
following two conditions:
17Nthe scheme does not detecta als deadlock
II deadlocks will be detected
Resolution of a detected deadlock
Deadlock resolution involves breaking existing
wait-for dependencies between the processes
It involves rolling back one or several deadlocked
processes and assigning their resources to blocked
processes so that they can resume their execution
8
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=10)

### 原始文字层

````text
A centralized detection scheme
9
central detector
A B C
C B A
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
centralized detection scheme
central detector
````

### 图片文字 OCR（en-US，待对照原页）

````text
A centralized detection scheme
central detector
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=11)

### 原始文字层

````text
• A releases resource waited by B
• A starts waiting for resource held by C
10
central detector
A B C
C B A
A C
tellin
i
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
central detector
． releases resource waited by B
． starts waiting for resource held by C
````

### 图片文字 OCR（en-US，待对照原页）

````text
central detector
A releases resource waited by B
A starts waiting for resource held by C
10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=12)

### 原始文字层

````text
• B can proceed, i.e. B  A should be removed
11
central detector
A B C
C B A
A C B inA
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
central detector
B can proceed, i.e. B 兮 should be removed
````

### 图片文字 OCR（en-US，待对照原页）

````text
central detector
B can proceed, i.e. B -5 A should be removed
11
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=13)

### 原始文字层

````text
• A’s message arrives first
• A false deadlock is declared 12
central detector
A B C
C B A
A C B A
yt.gg
cycle
receiving
message message not receive
a
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
central detector
B
A
A
C
． A'S message arrives first
false adlock is declared
````

### 图片文字 OCR（en-US，待对照原页）

````text
central detector
A
C
C
B
to-b
no-e
A's message arrives first
A false adlock is declared
12
````

### 图表辅助说明

中心检测器先收到 A 的新等待边 A→C，却尚未收到 B→A 已解除的消息，因此保留 C→B→A 并误认为存在环。下方各站点消息与上方合成图对照，展示消息延迟导致的假死锁。

## PDF 第 14 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=14)

### 原始文字层

````text
13
Distributed Scheme for AND model
 Designed for detecting the cycle which spans 
over several machines. 
 The algorithm is invoked when a process 
starts waiting.
 A probe (i, j, k) is generated and sent to the 
process (or processes) holding the needed 
resources. 
• i is the initiator of the probe, j is the sender, and, k is 
the receiver of the probe.
non0
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Distributed Scheme for AND model
Designed for detecting the cycle hich spans
over several machines.
The algorithm is invo ed when a process
starts waiting.
A probe (i, j, k) is generated and sent to the
o
process (or processes) holding the needed
resources.
• i is the initiator of the probe, j is the sender, and, k is
the receiver of the probe.
13
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=15)

### 原始文字层

````text
14
 When the probe is received, the recipient 
checks to see if itself is waiting for any 
processes. 
 If so, the probe is updated and sent to the 
processes being waited for.
 Otherwise, discard the probe. 
 If the probe comes back to the original 
sender, a cycle exists and there is a 
deadlock in the system.
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
When the probe is received, the recipient
checks to see if itself is waiting for any
processes.
If so, the probe is updated and sent to the
o
processes being waited for.
Otherwise, discard the probe.
O
If the probe comes back to the original
sender, a cycle exists and there is a
deadlock in the system.
14
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=16)

### 原始文字层

````text
15
0 1 2
6
7
8
3
4
5
(0, 2, 3)
(0, 4, 6)
(0, 5, 7)
(0, 8, 0)
所有进程都会启用算法
不会发现 cycle 1会发现 1也会
启动detect算
probe L
dēff
䐐 t_ _
meahine
li
丝 - deadlock
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
（ 0 ， 8 ， 0
3
0
2
1
V 寮
4
0
0 ， 4 ， 6 ）
（ 0 ， 5 ， 7 ）
6
7
8
````

### 图片文字 OCR（en-US，待对照原页）

````text
0760b Ude,
3
0
4
5.
6
7
8
2
1
15
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=17)

### 原始文字层

````text
16
Distributed Scheme for OR model
 Based on the echo algorithm
 A blocked node passes probes along the 
edges in the wait-for graph
 A node only executes the algorithm (i.e., 
passes the probes or sends the echoes) if 
the node is blocked
 If the algorithm terminates, then every 
node in the wait-for graph is blocked. 
 Deadlock
0
echo
t
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Distributed Scheme for OR model
0 Based on th ech algorithm
A blocked no e asses probes along the
edges in the wait-for graph
A node only executes the algorithm (i.e.,
passes the probes or sends the echoes) if
the node is blocked
If the algorithm terminates, then every
node in the wait-for graph is blocked.
Deadlock
o
echo
16
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 18 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=18)

### 原始文字层

````text
17
1
4 5
2 3
7
6
every can use detect algorithm t­o find everyone
approach I block
not outgoing edge 小
send back echo deadlock
approach2
Cho algoritme.­us
e stop deadlock
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
can
senJ
applhuch
2
llse s-top d 应
4
1
5
7
3
6
````

### 图片文字 OCR（en-US，待对照原页）

````text
can Inse deü
@evad
send back echot
apprquch
2
V&ho alorrf
Ilse Stop dedIUk
4
1
3
5
7
(ock.
6
17
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 19 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=19)

### 原始文字层

````text
18
1
4
5
2
3
7
6
probe
````

### 图片文字 OCR（en-US，待对照原页）

````text
18
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 20 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=20)

### 原始文字层

````text
19
1
4 5
2 3
7
6
probe
not send back
throw probe
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
f-hrow 伊
````

### 图片文字 OCR（en-US，待对照原页）

````text
Jaå.
throw pnbe,
19
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 21 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=21)

### 原始文字层

````text
20
1
4
5
2
3
7
6
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
20
````

### 图片文字 OCR（en-US，待对照原页）

````text
20
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 22 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=22)

### 原始文字层

````text
21
1
5
2 3
6
if deadlock
````

### 图片文字 OCR（en-US，待对照原页）

````text
if' DIOA[pda
21
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 23 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=23)

### 原始文字层

````text
22
1
5
2 3
6
probe
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
22
````

### 图片文字 OCR（en-US，待对照原页）

````text
22
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 24 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=24)

### 原始文字层

````text
23
1
5
2 3
6
receive first
````

### 图片文字 OCR（en-US，待对照原页）

````text
Vrec.de f)'rsf,
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 25 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=25)

### 原始文字层

````text
24
15
2
3
6
di
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
24
````

### 图片文字 OCR（en-US，待对照原页）

````text
24
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 26 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=26)

### 原始文字层

````text
25
15
2
3
6
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
25
````

### 图片文字 OCR（en-US，待对照原页）

````text
25
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 27 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=27)

### 原始文字层

````text
26
1
5
2 3
6
received probeTom
send echoha
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
26
````

### 图片文字 OCR（en-US，待对照原页）

````text
L.ebed TQ from 1
9nd
26
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 28 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=28)

### 原始文字层

````text
27
15
2
3
6
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
27
````

### 图片文字 OCR（en-US，待对照原页）

````text
27
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 29 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=29)

### 原始文字层

````text
28
15
2
3
6
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
28
````

### 图片文字 OCR（en-US，待对照原页）

````text
28
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 30 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=30)

### 原始文字层

````text
29
15
2
3
6
````

> OCR 未识别出可靠文字；本页可能以图形、手写公式或空白为主。

### 图表辅助说明

死锁探测动画：节点 1、2、3、5、6 组成有向等待图，黑边包括 1→2、1→3、2→5、3→5、3→6、5→6。红色与绿色反向短箭头分别展示探测和回声沿边传播；这是完整动画中的中间步骤。

## PDF 第 31 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=31)

### 原始文字层

````text
30
1
5
2 3
6
receive all­t
deadlock
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
dead 丿 0
30
````

### 图片文字 OCR（en-US，待对照原页）

````text
> receVø echo
dead lock
30
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 32 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=32)

### 原始文字层

````text
31
Further reading
 G. Andrews. Paradigms for process 
interaction in distributed programs. ACM 
Computing Surveys, 23(1):49--90, March 
1991 (echo algorithm)
 K. Mani Chandy , Jayadev Misra , Laura M. 
Haas, Distributed deadlock detection, ACM 
Transactions on Computer Systems (TOCS), 
v.1 n.2, p.144-156, May 1983 (deadlock 
detection)
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Further reading
G. Andrews. Paradigms for process
interaction in distributed programs. ACM
Computing Surveys, 23(1):49--90, March
1991 (echo algorithm)
K. Mani Chandy , Jayadev Misra , Laura M.
Haas, Distributed deadlock detection, ACM
Transactions on Computer Systems (TOCS),
v.l n.2, p.144-156, May 1983 (deadlock
detection)
31
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 33 页

[查看此页](../../../../notes/original/711/1/S5%2Bdeadlock.pdf#page=33)

### 原始文字层

````text
32
Review 
 Describe the echo algorithm using pseudo code.
 Understand the deadlock detection schemes for the AND 
and OR model.
 Assume that we are running a computation that consists of 
several tasks. The tasks are distributed across the machines 
in a distributed system. Each task only knows the location of 
the tasks that it communicate with. Suppose we want to find 
out the CPU load information on each of the machines 
hosting the tasks. Outline an algorithm that finds the CPU 
load information from the machines that host the execution 
of the tasks.
 Suppose all the processes in the system has a distinct ID 
that can be used to uniquely identify the processes in the 
system. Modify Chandy’s deadlock detection for the AND 
model so that, when a deadlock is detected, the process with 
the smallest ID can be aborted to resolve the deadlock.
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Review
Describe the echo algorithm using pseudo code.
Understand the deadlock detection schemes for the AND
and OR model.
Assume that we are running a computation that consists of
several tasks. The tasks are distributed across the machines
in a distributed system. Each task only knows the location of
the tasks that it communicate with. Suppose we want to find
out the CPU load information on each of the machines
hosting the tasks. Outline an algorithm that finds the CPU
load information from the machines that host the execution
of the tasks.
Suppose all the processes in the system has a distinct lb
that can be used to uniquely identify the processes in the
system. Modify Chandy's deadlock detection for the AND
model so that, when a deadlock is detected, the process with
the smallest ID can be aborted to resolve the deadlock.
32
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

