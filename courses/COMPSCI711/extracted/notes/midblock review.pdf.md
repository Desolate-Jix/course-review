# midblock review.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI711/notes/original/midblock review.pdf`
- [打开原文件](../../notes/original/midblock%20review.pdf)
- 原文件 SHA-256：`77e583f8a44b5d1fc9dcf0c2f494d568c8a5b2a9806ebceb2c4a1d1ce317ea37`
- 文件索引：F330；PDF 总页数：17
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../notes/original/midblock%20review.pdf#page=1)

### 原始文字层

````text
Tjǜhronising logical clock a
b.￾occurs cn before be
Logical clock is 腔凹
时间值
as b
Ca e C b
total order Ta Ida
a b if Taib
as b if Taib Ida Idb
711 121
partially ordered logical clock
bfcancb 川
子进程 继承 父进程的时间戳 再加上 自己的 不
交换信息时相互影响 互相继承时间戳 同process的 门
更新为最大的 么哒
先 写没被影响的 is 再考虑影响
a
more expressive
impract.in expensivei zlonglire computer
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
0 巧
丁 5 〔 气 四 ）
乛 b
C@ ） 之 乙 CbJ.
江 < Jdb
c(otk
cb,l)
````

### 图片文字 OCR（en-US，待对照原页）

````text
a octurs
Lo
-to-t.gW or
) CCbJ.
If Ta=Tb,
ordered I
Y4bll
clock
m rite
cb,l)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../notes/original/midblock%20review.pdf#page=2)

### 原始文字层

````text
Multicast aim each process receive a copy
of message which Sent to group
it's et work
FIFO Ordering a process send m before m
other receive m before mi
A的发送顺序和 其它一致
与 Causal ordering的 区别 one process send
Ǖeiiūige
711 13
Causal ordering de rent process 凹 send
Ū message
m happen before m
other should receive m before m
ordered multicast
Total ordering a process send m
before m
all
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
k 、 吧
豸 。 。 1 归 0 $-s sead
7 目 〕
／ 乙
Sev1 d
````

### 图片文字 OCR（en-US，待对照原页）

````text
wuSJdle Ware
he-t
beaa
Son
Rore m!
other
S Causal yvd.e$ send
cveraL mesgve.
711 (3)
severa
Peh betre m
d receb'e
0kdered—flunHiza
)vLeAS gend
megae
send nn
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../notes/original/midblock%20review.pdf#page=3)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
0 和 FIFO / CausaI 的 区 别
FI FO Ordering
Causal
Ordering
Tota 丨 Ordering
保 证 顺 的 范 围
每 个 发 i 关 者 自 己 的 氵 肖 息 按 顺 序 被
deliver
所 有 氵 肖 且 司 的 因 果 关 系
所 有 氵 肖 息 心 须 在 所 有 进 程 中 顺 序 完 全
关 注 点
同 一 个 ． 发 详 者 的 消 息 顺
讠 的 触 发 “ 谁 ， 先 因 后 果
金 局 一 致 的 氵 肖 息 顺 序
否 能 看 出 友 送 者 是
冂 是 谁 发 的 很 重 要
0 谁 触 发 了 谁 很 关
其 谁 发 的 不 重 要
0 举 例 对 比 （ 假 设 有 两 个 发 送 者 PI 和 P2)
1 ． FIFO
如 果 PI 发 了 m ， 接 看 发 了 m
所 有 进 程 须 先 deliver m ， 再 deliver m （ 只 管 PI 发 的 ）
2 ． Causal
PI 发 了 m ， P2 收 到 后 根 据 m 发 了 m
所 有 进 程 必 须 先 deliver m ， 再 deliver m' （ 因 为 有 因 果 关 系 ）
3 ． To 1
不 管 消 息 m 和 m 是 否 有 因 果 关 系 、 是 否 来 自 同 一 发 送 者
只 要 有 一 个 进 程 先 deliver 了 m ， 再 deliver m
所 有 进 程 都 必 须 保 持 一 样 的 顺 序
囗 总 结 一 句 话 ．
FIFO ordering
： 同 一 发 送 者 发 的 消 ， 息 顺 序 要 一 致 。
Causal ordering. 有 先 因 后 果 的 消 息 顺 序 要 一 ，
Total ordering 所 有 消 息 的 顺 序 在 所 有 人 眼 中 都 要 一 致 ， 哪 怕 它 们 无 关 。
````

### 图片文字 OCR（en-US，待对照原页）

````text
Q FIFO / Causal
FIFO Ordering
Causal
Ordering
Total Ordering
deliver
1. FIFO
deliver m, deliver m' (RE Pl >fij)
2. Causal
• Pl m, P2 m m'
deliver m, deliver m'
Total
3.
deliver -r m, deliver m'
FIFO ordering.
• Causal ordering:
Total ordering:
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../notes/original/midblock%20review.pdf#page=4)

### 原始文字层

````text
Reliable multicast
nsendonrdT.ae process
or send tone of hem
每个 接收者都会 发送已 收到的 消息到 其它
进程 除了 sender
complexity nth ltnz n.tl n2
Virtualgncnrony.se
multicasty ˇ
些
进程 加入 或退出 组 view changed
message
Sent
to all process
Virtual Synchrony only ensure
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
SeoJ 亻 。 Laohe 0f
纟 c 飞 genJer)
````

### 图片文字 OCR（en-US，待对照原页）

````text
('c-qs
ncesS
SeoJ To Of
gender)
nchrt
e.c5 —gee
-to 01 p
euSVt
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../notes/original/midblock%20review.pdf#page=5)

### 原始文字层

````text
y
the sequence of view changed mess 一
一些
无视 crash的 保证 reali ble multicast
每个视图里的 消息要一致才能保证 lis
change the view together
implement of FIFO ordering
use sequence number
sender send message Sequence
number 1
receiver if
message sequence num­ber
二 receiver sequence t I
deliver else in
wait queue
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
e 扩
````

### 图片文字 OCR（en-US，待对照原页）

````text
cra5k
Cha e to
J emet
Dill" Jer•
S
etemc-e—
re ceÜvø<
quen
Seqnence f)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../notes/original/midblock%20review.pdf#page=6)

### 原始文字层

````text
implement of causal ordering
lector variable
Vil 0
6
Variable lynge from process
in process i 消息变重
发送时 自上新群
更新process eddie 后更新
vector
rariabiussrectorvnnnnnee.­me
比较消息的 variable
与 process 的 variable
保证是该进示
若 等于 消息的 variable
的 下条消息
1
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
@S5
儀 S 引
bble ·
/ 丿 0 （
````

### 图片文字 OCR（en-US，待对照原页）

````text
}nvlentent
.eS5
ansaL
Tar J a •e
Fule ,
va rDablg
VQV Jo
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../notes/original/midblock%20review.pdf#page=7)

### 原始文字层

````text
倁 正 其 程的 比 灯心 们deliver
所有相关消息已收到 否则 in wait queue
implement total order
send message mtn is
wait all healer back TS
choose largest TS send to receiver
update TS process as final is
deliver rule National Ts
I
first message
in que
3.19
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
） 忆 ／ 9 砌 乙
刃 J 72 ^ TS
[ 厂 羼 一 乙 么
````

### 图片文字 OCR（en-US，待对照原页）

````text
-tool ot-Jere
send Ts
all ver.
e I\lJQr
o receiver
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../notes/original/midblock%20review.pdf#page=8)

### 原始文字层

````text
Mutual
Exclusion
only one task is allowed to access the
shared resource
Centralized approach
drawback
access manager single point of
failure
requirement
Safety or one task can access
lire ness in no endless wait
Fairness fir chance to aces
and Agrawala
Timestamp_based
仙逝
algorithm
eachreqnesegne.Timestampwrrr­.tl al order
who need resource would send request
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
n0
d 千 勿 e
c.an 釔
end
eæh 列 自 m 彦 尸
耳 剑
````

### 图片文字 OCR（en-US，待对照原页）

````text
ess
@ Fcår ness
imes+vh — based
allorved tb access
dram/ )ack
s,
ailure
no end es IvaFb
chance -to atL.etD
bra]q—
each re.qnest Me. lunes-tamp
frtal OT eM
r-C.-e
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../notes/original/midblock%20review.pdf#page=9)

### 原始文字层

````text
1
to others with TS Who receive all
oktpw c.es
smallest TS programmer would
Tetr source 些
小
live ness
the value of the Ts increase
monotonically guy progress have
chance to enter will region fairness
Quorum_ based
Subset of task Maekawàsgy
every Quorum have 壮
籮舆
assign the
progress with at least one
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
仞 阝
乙 tom 尸
Sm
乙 跹
2 / 肥
ag
Sub 七 和
o 厂
````

### 图片文字 OCR（en-US，待对照原页）

````text
others wtftl TS
o Q torn er
Q aces
die Ts
receive
increqs-e
the Valme-
obøvu
Sub e-t Df -task
0 & 110tnm
Maek anJals
'n
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../notes/original/midblock%20review.pdf#page=10)

### 原始文字层

````text
Quorum ask for vote until gain
all off of that Quorum acquire 比兜
Fièif the Quorum have been noted
fairness
compare the IE trans 在 vote the
new one awiddeadnqu.ie
relinquish lives fxdeadikO­Tokenmondgiiiioaccess.ae
resource
unique token
need resource send token_request
message
嚣幽 taken senduneihtetghbour­unt.nl
find ten
every
task has a queue to record the
request
Initialization holder send
message to
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
0
ask
Qtb01
@ tdlS
fa has
````

### 图片文字 OCR（en-US，待对照原页）

````text
sua
e
ask p -E,
Qtb01
token
task has
Q
allow QceCS e
meSSQ e
htfl
aeae
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../notes/original/midblock%20review.pdf#page=11)

### 原始文字层

````text
Cat g
its neighbours neighbour up ate the point
to holder and send to other neighbour
requesti Send request to the neighbour Where
the direction of the point neighbour 什 not
the holder Would add the request to queue
and send the request to neighbour until
to holder
token
holder send it back update holder as
the former one the current holder
detect the request in queue send the
token back to the former one also send the
request later send until the request finish
deadlock
Echo Algorithm
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
叶 0 2 r 叼
和 平
—dea 一 在
````

### 图片文字 OCR（en-US，待对照原页）

````text
het9
eto er
Sequ te-faest to fie heb;kur mere
hot
fie ojnt, net' uy
tile -&mer
-flie
Dhe
Inn-til
holder
the teqnesb fin
later seqJ
—dea
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../notes/original/midblock%20review.pdf#page=12)

### 原始文字层

````text
go
P­itiator in send probes to its neighbours
non_initiator replicates and sends probes to
its neighbour after reeling probes
non initiator send echo when the node
have received the probes
The algorithm terminates when the
initiator receives all echoes from all its
neighbour
Dead lock detection
Wait for graph
use 回 豐 回
Model of deadlock need all the node point it
And model need a 盥
finish
dead lock 3 cycle
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
、 n 阡 厂 叼
non— 、 r 亿 砒 aqd s 召 豳
囱 0 Wheh 千 加
The
厂 ／ 负
Dea 旅
0 引 0
ec all ，
Wal?
````

### 图片文字 OCR（en-US，待对照原页）

````text
Sen
be
and sends pivbes
The
Dead (odc
send
reætves
Jetec€on
rah-
ec o when
Wal? F
-fble de
all
udl
mo el o
ode
need
ad
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../notes/original/midblock%20review.pdf#page=13)

### 原始文字层

````text
兰
Or model need one of the node point to
it finishe
KE go
find a subset
each mode have at least
one outgoing edge
all the outgoing edge point
to
the node in subset
Deadlock detection ˋ ˋ algorithm
no fake deadlock
all deadghouH.be
detected
在删除 edge 前收到新增edge
Centralized detector
use
centra­eueryt.me change of Use of
resource would send
message
to
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
厑 匕 & 0 肥 「 fl/le №
么 彬
倥 乙 t 砷
C 力
七 d
````

### 图片文字 OCR（en-US，待对照原页）

````text
need one ot {Ie node
01
ench node
ve at least
Ohe
fhc
1
611041/ be
-tect Ion
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../notes/original/midblock%20review.pdf#page=14)

### 原始文字层

````text
g
central doctor include detect
edge or add edge
because the arrival time of message
different might form a
gaede
report dead
fake deadlock
Andy deadlock detection
a process is waiting send probe ci.j.la
小 二
开始进程 上个进程 下个进程
ie probe day
other process it has waiting
prowess update probe and Send to waiting
mess if not waiting dropprobe
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
翟 上 覆
乙 、 On ·
不 亇 乬
````

### 图片文字 OCR（en-US，待对照原页）

````text
luz
ren
a roce55
)-obe am d
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../notes/original/midblock%20review.pdf#page=15)

### 原始文字层

````text
process if nl Na Ling dropprobe
org
deadlock detection
use echo algorithm
send probe neighbour pass it
to waiting if not wait ignore
probe if node have receive probe
send echo back initiator receive
all ecno.rs deadlock
然
Garbage collection
reference counting
111
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
〗 ol 匕 匕 化 纪
cØl 千 汽
````

### 图片文字 OCR（en-US，待对照原页）

````text
C.a OVI
have receive
col ecton
ar C
befrerenæ
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../notes/original/midblock%20review.pdf#page=16)

### 原始文字层

````text
嚻
it reference counting 0
release the memory
problem because of message delay
memory would be released too
early when 比上
Weighted reference counting
a object have a weight
assign weight to each pointer
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
3
e OP 川 e
fD
me “ 0 园
形 、 ea 乙
````

### 图片文字 OCR（en-US，待对照原页）

````text
(010m
me MO
3
ecans€ oP mess €
VIAVI I
re@rencp
H each
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../notes/original/midblock%20review.pdf#page=17)

### 原始文字层

````text
四
object weight Sum all pointer height
copy
i split the weight every
til
回
weight no release memory
what it cant be split
5t 5
周 国 一
四
cant handle gcieg
````

### 图片文字 OCR（en-US，待对照原页）

````text
(PII
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

