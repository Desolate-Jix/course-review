# Practice+Questions.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI711/source/711/1/Practice+Questions.pdf`
- [打开原文件](../../../../source/711/1/Practice%2BQuestions.pdf)
- 原文件 SHA-256：`78fc4dd0906d0735d65cb7d1963a5a33f20207b305aae359ddadf0e193836bd0`
- 文件索引：F057；PDF 总页数：12
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../source/711/1/Practice%2BQuestions.pdf#page=1)

### 原始文字层

````text
Practice Questions
From the past exam papers
````

### 图片文字 OCR（en-US，待对照原页）

````text
Practice Questions
From the past exam papers
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../source/711/1/Practice%2BQuestions.pdf#page=2)

### 原始文字层

````text
Consider the following code fragment which "folds" a linear array xa.
 const int MAXSIZE = 20000;
 double fold, xa[MAXSIZE];
 ...
 for ( i = 0; i < MAXSIZE/2; ++i )
 fold += xa[i] * xa[MAXSIZE - 1 - i];
This code is to be executed on a MIPS R10K superscalar processor with 4 functional units capable of 
doing one floating-point operation and one integer operation per clock cycle. One of these 
operations could be a memory access (a load or a store). The integer operation could be a branch.
1. Write down the instructions involved in the execution of the loop, and the instruction schedule 
for one iteration. Give the flops per cycle for the schedule, and compute the functional unit 
utilization.
2. Unroll the loop once, and schedule the instructions. Give the flops per cycle for the schedule, 
and compute the functional unit utilization.
3. Unroll the loop twice, and schedule the instructions. Give the flops per cycle for the schedule, 
and compute the functional unit utilization.
Instruction Latency Repeat rate
Integer add/sub/logical/branch 1 1
Integer load/store 2 1
Floating-point load/store 3 1
Floating-point add/sub/multiply 2 1
Floating-point multiply-add 3 1
Floating-point division 19 21
fubyerationloa­incre.int
pointer
iii emsnneirgnnngnipg add.iebmi
t
U­t
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Consider the following code fragment which "folds" a linear array xa.
                                                                                      Instruction             Latency   Repeat rate
        const int MAXSIZE = 20000;                         fubyerationloaincre.intInteger add/sub/logical/branch 1         1
        double fold, xa[MAXSIZE];                                             pointerInteger load/store         2          1
                                                                                      Floating-point load/store 3          1
        ...
                                                                                      Floating-point add/sub/multiply 2    1
        for ( i = 0; i < MAXSIZE/2; ++i )                                             Floating-point multiply-add 3        1
           fold += xa[i] * xa[MAXSIZE - 1 iii- i];                                    Floating-point division   19        21
This code is to be executed on a  MIPS R10K superscalar processor with 4 functional units capable of emsnneirgnnngnipgadd.ie
doing one floating-point operation and one integer operation per clock cycle. One of these
operations could be a memory access (a load or a store). The integer operation could be a branch.bmi
1.   Write down the instructions involved in the execution of the loop, and the instruction schedule
     for one iteration. Give the flops per cycle for the schedule, and compute the functional unit
     utilization.
2.   Unroll the loop once, and schedule the instructions. Give the flops per cycle for the schedule,
     and compute the functional unit utilization.
3.   Unroll the loop twice, and schedule the instructions. Give the flops per cycle for the schedule, t
     and compute the functional unit utilization.                                                              Ut
````

### 图片文字 OCR（en-US，待对照原页）

````text
Consider the following code fragment which "folds" a linear array
sub
Instruction
const int MAXSIZE
20000;
double fold, xa[MAXSIZE]•,
n
d/sub/logical/branch
C intremt pa'
er load/store
loati
int load/store
oating-point add/sub/multiply
fer ( i
- e; i < MAXSIZE/2; ++
Floating-point multiply-add
fold
* xa[MAXSIZE
i];
1
Floating-point division
Latency
2
3
2
3
19
Repeat rate
21
e rqnqh
ava M I PISO
3
This code is to be exec
K superscalar
cessor it 4 functional unl sc pa eo
doing one floa
into eration and one integer operation per lock ycle. One of these
operations could be a memory access (a load or a store). The integer operation could be a branc
1.
2.
3.
Write down the instructions involved in the execution of the loop, and the instruction sched
for one iteration, Give the flops per cycle for the schedule, and compute the functional uni
utilization.
Unroll the loop once, and schedule the instructions. Give the flops per cycle for the schedule,
and compute the functional unit utilization.
Unroll the loop twice, and schedule the instructions. Give the flops per cycle for
schedule,
and compute the functional unit utilization.
0
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../source/711/1/Practice%2BQuestions.pdf#page=3)

### 原始文字层

````text
We studied software pipelining in the context of the MIPS R10K processor, which is capable of 
performing two floating-point operations (one of which could be a memory access) and two integer 
operations (one of which could be a branch) per clock cycle. 
You are asked to consider the following kernel, named DAXMY: 
for (int i = 0; i < N; i++) {
 y[i] = a * x[i] - y[i]; 
}
Provide a schedule that maximizes the functional unit utilization. To this end, you may need to unroll 
the loop as required. Calculate the functional unit utilization you achieved. To earn full marks, your 
schedule should use the minimum number of instructions and achieve the maximum possible 
functional unit utilization.
You may assume reasonable mnemonics for any new instructions (i.e., instructions that we did not 
use in DAXPY) that you may need to use in your solution to DAXMY.
Instruction Latency Repeat rate
Integer add/sub/logical/branch 1 1
Integer load/store 2 1
Floating-point load/store 3 1
Floating-point add/sub/multiply 2 1
Floating-point multiply-add 3 1
Floating-point division 19 21
可用插槽数
overturn crete
Cadd 判断循环
是否
邈 一 嘴负数
䐐 䬟ègionopgi 0
〇菭
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
可⽤插槽数
We studied software pipelining in the context of the MIPS R10K processor, which is capable of
performing two floatingove r  t u r  n-point operations (one of which could be a memory access) and two integer crete
operations (one of which could be a branch) per clock cycle.
                                                                                      Instruction             Latency   Repeat rate
You are asked to consider the following kernel, named DAXMY:                          Integer add/sub/logical/branch 1     1
                                                                                      Integer load/store        2          1
for (int i = 0; i < N; Caddi++) {                            判断循环                     Floating-point load/store 3          1
                                                                                      Floating-point add/sub/multiply 2    1
   y[i] = a * x[i] - y[i];                                                    是否      Floating-point multiply-add 3        1
}                                                                  䐐                  Floating-point division   19        21
                                            ⼀    嘴负数                         䬟ègionopgi                                   0
Provide a schedule that maximizes  the functional unit utilization. T邈          o this end, you may need to unroll 菭
the loop as required. Calculate the functional unit utilization you achieved. To earn full marks, your
schedule should use the minimum number of instructions and achieve the maximum possible                               〇
functional unit utilization.
You may assume reasonable mnemonics for any new instructions (i.e., instructions that we did not
use in DAXPY) that you may need to use in your solution to DAXMY.
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
We studied softwa re pipelining in the context of the M 丨 PS RIOK processor, which is capable Of
performing tWO floating- Oint O erations (one Of which could be a memory access) and 一
operations (one 0 which could be a branch) per clock cycle.
for (int 土
0
y [ i ]
Provid
the loop as re
schedule should use the minimum number Of instructions and achieve the maximum possible
functional unit utilization.
You may assume reasonable mnemonics fO r a ny new instructions (i.e., instructions that we did not
use in DAXPY) that you may need tO use in your solution tO DAXMY.
````

### 图片文字 OCR（en-US，待对照原页）

````text
We studied software pipelining in the context of the MIPS RIOK processor, which is capable of
performing two floating- ointo erations (one of which could be a memory access) and V-tQ.Eg.e.r._
0
operations (one o which could be a branch) per clock cycle.
o re asked to con • er the following ke nel, named DAXMY:
for (int i = 0; i <
Instruction
Integer add/sub/logical/branch
Integer load/store
Floating-point load/store
Floating-point add/sub/multiply
Floating-point multiply-add
loating-point division
t no
Latency
2
3
2
3
.19
Repeat rate
21
x[i]
Provid
sch
le that maxi
i
e functio a unit utilization. To this d, you may n
the loop as re
a culate the functional unit utilization you achieved. To earn full marks, your
schedule should use the minimum number of instructions and achieve the maximum possible
functional unit utilization.
You may assume reasonable mnemonics for any new instructions (i.e., instructions that we did not
use in DAXPY) that you may need to use in your solution to DAXMY.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../source/711/1/Practice%2BQuestions.pdf#page=4)

### 原始文字层

````text
for ( j = 1; j <= N; j += 1 ) {
Ta: x[j] = x[j-1] + 10;
Tb: y[j] = x[j] + y[j];
}
Each statement in the loop body can be executed with a single instruction taking a clock cycle. The 
processor is superscalar with 4 homogenous functional units. Assume no branching overhead. How 
many cycles are needed to execute the entire loop?
How many cycles are needed to execute the loop unrolled once?
If the original loop is unrolled u times (i.e., the original instructions of the loop iteration are repeated 
u times in addition to the original), how many cycles are required to execute the unrolled loop? Show 
that the speedup of the loop unrolled u times is (2u + 2)/(u + 2). 
Show that the functional unit utilization for this loop, gained from unrolling, can never be greater 
than 1/2. 
溺
_
4个pipeline 2条饼 2条呼满
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
for ( j = 1; j <= N; j += 1 ) {
           Ta: x[j] = x[j-1] + 10;
           Tb: y[j] = x[j] + y[j];
}
Each statement in the loop body can be executed with a single instruction taking a clock cycle. The 溺
processor is superscalar with 4 homogenous functional units. Assume no branching overhead. How _
many cycles are needed to execute the entire loop?
How many cycles are needed to execute the loop unrolled once?
If the original loop is unrolled u times (i.e., the original instructions of the loop iteration are repeated
u times in addition to the original), how many cycles are required to execute the unrolled loop? Show
that the speedup of the loop unrolled u times is (2u + 2)/(u + 2).
Show that the functional unit utilization for this loop, gained from unrolling , can never be greater
than 1/2.
                                                                                         2条饼                     2条呼满
                                      4个pipeline
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Each st
Ta: x[j] = x[j-l] + 10 ；
the loop b0dy can be executed with a single instruction taking a clock cycle. The
processor iS superscalar with 4 homogenous functional units. Assume no branching overhead. H OW
many cycles a re needed tO execute the entire IOOP?
H OW many cycles a re needed tO execute the op unrolled once?
If the original IOOP is unrolled u times (i.e., the original instructions Of the 丨 00p iteration a re repeated
u times in addition tO the original), hOW many cycles a re required tO execute the unrolled loop? Show
that the speedup of the loop unrolled u times is ()u + 2)/(u + 2 ） ·
Show that the functional unit utilization for this IOOP, gained from unrolling, can neve r be greater
than 1 / 2 ·
巰 槠 》 2 №
````

### 图片文字 OCR（en-US，待对照原页）

````text
for (j =
Ta: x[j] = x[j-l] + 10;
6
Each st
the loop body can be executed with a single instruction taking a clock cycle. The
processor is superscalar with 4 homogenous functional units. Assume no branching overhead. How
many cycles are needed to execute the entire loop?
How many cycles are needed to execute the loop unrolled once?
If the original loop is unrolled u times (i.e., the original instructions of the loop iteration are repeated
u times in addition to the original), how many cycles are required to execute the unrolled loop? Show
that the speedup of the loop unrolled u times is (2u + 2)/(u + 2).
Show that the functional unit utilization for this loop, gained from unrolling, can never be greater
than 1/2.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../../source/711/1/Practice%2BQuestions.pdf#page=5)

### 原始文字层

````text
TaT
b
Ta0 Tb0
Ta1 Tb1
Ta0 Tb0
Ta1 Tb1
Ta2 Tb2
Ta3 Tb3
u = 0
u = 1
u = 3
4
个pipeline
2
木
M5
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
4个pipeline                             2⽊    M
                                                      Ta0                  5
                     Ta0
Ta
                                                      Tb0            Ta1
                     T               Ta1               T
                       b0                               a2           Tb1
Tb
                                                       Tb2           Ta3
 u = 0
                                     Tb1
                            u = 1                       u = 3
                                                                      Tb3
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
aO
al
````

### 图片文字 OCR（en-US，待对照原页）

````text
bl
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../source/711/1/Practice%2BQuestions.pdf#page=6)

### 原始文字层

````text
Typically, the number of reads to shared data exceeds the number of writes. 
Reading shared data concurrently can be permitted, but writing concurrently 
cannot be. Reading and writing concurrently cannot be permitted either.
Using monitors, implement a ReadWriteLock object that allows concurrent read 
accesses, but disallows concurrent write or read/write accesses.
condition.Variable
mutes m
ready
心心 writing
wife lock read unlock write unto
Lock1 7 lock 1 1 Locks I
Lock1 1
if writing until if writingFalse reader_ fgy.in and reader ifreader 3 awake all
Tender ti iii in awake on write reader
unlock elsTrait 113 mi Band aur
un Ioi CU.waitCm
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Typically, the number of reads to shared data exceeds the number of writes.
       Reading shared data concurrently can be permitted, but writing concurrently condition.Variable
       cannot be. Reading and writing concurrently cannot be permitted either.
       Using monitors, implement a ⼼⼼            writingReadWriteLock object that allows concurrent read mutesm
       accesses, but disallows concurrent write or read/write accesses.
                                                      wife            lock                 re  a  d      unlock                write        unto
 re   a   d   y                                      Lo  c  k  1    7                          lock       1     1                Lo  c  ks        I
  Lo  c  k   1    1                                     if                   Fa    l    s    e    re a d e r_
 if        writing                   until                  writing                               re  a  d  e  r      3        fg             y.             i             n
                                                     and         re a d e r                 if                                awa  ke         all
Te                                 n                                 d                                 e                                 rtiiiiinawa keonwriteBandre a d e r
  unlock                                       elsTr                              a                                 i                                 t113miaur
                                                         un     Ioi            CU.waitCm
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TypicalIy, the number 0f reads t0 shared data exceeds the number 0f writes.
Reading shared data concurrently ca n be permitted, but writing C O n C
cannot be. Reading and writing concurrently cannot be permitted it er.
亻 丿
Using monitors, implementa Read riteLock Object that allows concurrent read
accesses, but disallows concurrent write O r read/write accesses.
r eAé 乙 lc
V 巧
eße ）
伍 列 0ck
````

### 图片文字 OCR（en-US，待对照原页）

````text
Typically, the number of reads to shared data exceeds the number of writes.
Reading shared data concurrently can be permitted, but writing conc
cannot be. Reading and writing concurrently cannot be permitted it er.
rmJer, ul)kißb
Using monitors, implement a ReadWriteLock object that allows concurrent read
accesses, but disallows concurrent write or read/write accesses.
rg.d
reader ff
ren uhloclc
(Inw-
1.0 LEC )
IT ruder —
•freader —02)
lvm-t( )
mWake A1/
awake on
and
mnlock
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../../source/711/1/Practice%2BQuestions.pdf#page=7)

### 原始文字层

````text
Compare and contrast parallel computation and pipeline computation in the light of 
speedup and resource requirements.
CU ㄍ
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
CU          ㄍ
Compare and contrast parallel computation and pipeline computation in the light of
speedup and resource requirements.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Compare and contrast parallel computation and pipeline computation in the light of
speedup and resource requirements.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../../source/711/1/Practice%2BQuestions.pdf#page=8)

### 原始文字层

````text
Explain the various pipeline hazards and how these hazards affect the performance 
of the pipeline. How do we reduce these hazards?
f Struct ed hazard 同时用相同资源
spearte data memory muH port
Data hazard 用来准备 㛤数据
dalay or change sequence
control hazard 分支 时条件未被
计算出
San 蝨计算条件
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Explain the various pipeline hazards and how these hazards affect the performance
of the pipeline. How do we reduce these hazards?
  f   Struct   ed       hazard        同时⽤相同资源
                   spearte    data  memor y   muH   por  t
       Data           hazard        ⽤来准备     㛤数据
                        dalay    or change  sequence
     control        hazard          分⽀   时条件未被
                                    计算出
                          San       蝨计算条件
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Explain the various pipeline hazards and how these hazards affect the performance
0f the pipeline. HOW d0 we reduce these hazards?
5 “ 声 -P«t
````

### 图片文字 OCR（en-US，待对照原页）

````text
Explain the various pipeline hazards and how these hazards affect the performance
of the pipeline. How do we reduce these hazards?
C S-tfmcfc d kveafds
sparte dn-tot -p«t
@ 'III
Jalao se4nence
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../../source/711/1/Practice%2BQuestions.pdf#page=9)

### 原始文字层

````text
Cache misses are categorized as compulsory misses, conflict misses, capacity 
misses, and coherency misses. Briefly describe each of these categories and discuss 
strategies to minimize coherency misses. What effects, if any, your strategies to 
minimize coherency misses would have on other miss types?
ftltimeahgs
caches
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
caches
Cache misses are categorized as compulsory misses, conflict misses, capacity ftltimeahgs
misses, and coherency misses. Briefly describe each of these categories and discuss
strategies to minimize coherency misses. What effects, if any, your strategies to
minimize coherency misses would have on other miss types?
````

### 图片文字 OCR（en-US，待对照原页）

````text
fiYct fir access caches
Cache misses are categorized as compulsory misses, conflict misses, capacity
misses, and coherency misses. Briefly describe each of these categories and discuss
strategies to minimize coherency misses. What effects, if any, your strategies to
minimize coherency misses would have on other miss types?
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../source/711/1/Practice%2BQuestions.pdf#page=10)

### 原始文字层

````text
Briefly describe the cache coherence problem. Describe the MSI protocol and how 
it solves the cache coherence problem. What are the performance drawbacks of the 
MSI protocol? Describe how the MOSI and MESI protocols mitigate some of these 
performance issues. Highlight the differences between the three protocols, paying 
particular attention to the performance issues.
MOSI owned no need
write to memory
when switch to
shared
MES I Exclusive no need
multicast inv9您
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Briefly describe the cache coherence problem. Describe the MSI protocol and how
it solves the cache coherence problem. What are the performance drawbacks of the
MSI protocol? Describe how the MOSI and MESI protocols mitigate some of these
performance issues. Highlight the differences between the three protocols, paying
particular attention to the performance issues.
                        MOSI                 owned                    no     need
                                                                write        to   memory
                                                       when         switch        to
                                                                              shared
                      MES         I           Exclusive                  no    need
                                                             multicast           in v9  您
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Briefly describe the cache coherence problem. Describe the MSI protocol and how
it solves the cache coherence problem. What a re the performance drawbacks of the
MSI protocol? Describe hOW the MOSI and MESI protocols mitigate s O m e Of these
performance issues. Highlight the differences between the three protocols, paying
particular attention tO the performance issues.
乪 OS 工
趴 S 工
0 heec(
h s 么
Ex ， no
````

### 图片文字 OCR（en-US，待对照原页）

````text
Briefly describe the cache coherence problem. Describe the MSI protocol and how
it solves the cache coherence problem. What are the performance drawbacks of the
MSI protocol? Describe how the MOSI and MESI protocols mitigate some of these
performance issues. Highlight the differences between the three protocols, paying
particular attention to the performance issues.
MOS L
no heed
WVIYe
when sppfch
Shared, , .
Exc(lnSvC, no næed
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../source/711/1/Practice%2BQuestions.pdf#page=11)

### 原始文字层

````text
Describe schemes to reduce coherency misses, and discuss how each of these schemes would affect 
compulsory, capacity, and conflict misses.
Consider the following code fragment:
01 float sum[8]; float a[1024][16];
02 int i, j;
03 ....
04
05 for ( int i = 0; i < 16; ++i ) {
06 for ( int j = 0; j < 1024; ++j ) {
07 sum[i] = a[j][i];
08 }
09 }
This code is to be executed in parallel on a 32 processor SMP system by assigning each of the outer 
loop iteration to a separate processor. Assuming that sizeof(float) is 4 and the cache line size is 64 
bytes, what performance problems the parallel execution may face? How can you fix these 
problems? Re-write the code fragment with the problems fixed.
l l
te
wen know E
TIǛ
name line16个浮点
有 咧 float 4字节
46字节
caches line Thad hit 不鹽 多核繁
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
l l                             te
Describe schemes to reduce coherency misses, and discuss how each of these schemes would affect wenknow      E
compulsory, capacity, and conflict misses.
Consider the following code fragment:
01      float sum[8]; float a[1024][16];            TIǛ
02      int i, j;
03      ....
04                                                                                                                         点
05      for ( int i = 0; i < 16; ++i ) {                                                 name            line16个浮
06          for ( int j = 0; j < 1024; ++j ) {
07              sum[i] = a[j][i];
08          }
09      }             有      咧                                                     4字节
                                                                 float
This code is to be executed in parallel on a 32 processor SMP system by assigning each of the outer
loop iteration to a separate processor. Assuming that sizeof(float) is 4 and the cache line size is 64
bytes, what performance problems the parallel execution may face? How can you fix these                      46字节
problems? Re-write the code fragment with the problems fixed.
                     caches          line                              hit          不鹽              多核繁
                                              Thad
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
01
02
03
04
05
06
07
08
09
Describe schemes tO reduce coherency misses, and discuss hOW each Of t ese schemes would a e Ct
compulsory, capacity, and conflict misses.
Consider the following code fragment:
for( inti = 0 ； i < 16 ； ++i ） {
float sum[8]; float a [ 1024 ] [ 16L
int 刂 j;
fo r （ intj = 0 ； j < 1024 ； ++j ） {
This code is tO be executed in parallel on a 32 processor SMP syste m by assigning each Of the outer
IOOP iteration tO a separate processor. Assuming that sizeof(float) is 4 and the cache line size is 64
bytes, what performance problems the parallel execution may face? HOW can you fix these
problems? Re-write the code fragment with the p oble s fi d.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Describe schemes to reduce coherency misses, and discuss how each oft ese schemes would a ect
compulsory, capacity, and conflict misses.
Consider the following code fragment:
01
02
03
04
05
06
07
08
09
float sum[8];
float
int i, j;
for ( int I - 0,
for ( intj-
- o; j < 1024; ++j ) {
sum[i] =
ficathe I
float — 4tf
This code is to be executed in parallel on a 32 processor SMP system by assigning each of the outer
loop iteration to a separate processor. Assuming that sizeof(float) is 4 and the cache line size is 64
bytes, what performance problems the parallel execution may face? How can you fix these
problems? Re-write the code fragment with the p oble s fi d.
anhes
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../source/711/1/Practice%2BQuestions.pdf#page=12)

### 原始文字层

````text
ache Ine
y ie I 取 们 们
列亚
化热
````

> OCR 未识别出可靠文字；本页可能以图形、手写公式或空白为主。

### 图表辅助说明

本页大部分留白，仅顶部有少量蓝色手写残片与箭头；内容不足以恢复一道完整题目或答案。

