# SuperscalarProcessors.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI711/source/711/1/SuperscalarProcessors.pdf`
- [打开原文件](../../../../source/711/1/SuperscalarProcessors.pdf)
- 原文件 SHA-256：`213693d6da364ffb7dbcfc01aa3cc5564c7e5e108c2763ce07637c79b4979c2d`
- 文件索引：F075；PDF 总页数：21
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../source/711/1/SuperscalarProcessors.pdf#page=1)

### 原始文字层

````text
Superscalar Processors
mano@cs.auckland.ac.nz
超标量
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Superscalar Processors
mano@cs.auckland.ac.nz
````

### 图片文字 OCR（en-US，待对照原页）

````text
Superscalar Processors
mano@cs.auckland.ac.nz
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../source/711/1/SuperscalarProcessors.pdf#page=2)

### 原始文字层

````text
Superscalar Processors
• The pipelined processor we studied so far is able issue one instruction 
per clock cycle
• A superscalar processor has multiple concurrent functional units, and 
therefore able to issue multiple instructions per clock cycle
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Superscalar Processors
•The pipelined  processor  we studied  so far is able issue one instruction
 per clock cycle
•A superscalar processor  has multiple concurrent  functional  units,  and
 therefore able to issue multiple  instructions   per clock cycle
````

### 图片文字 OCR（en-US，待对照原页）

````text
Superscalar Processors
' The pipelined processor we studied so far is able issue one instruction
per clock cycle
• A superscalar processor has multiple concurrent functional units, and
therefore able to issue multiple instructions per clock cycle
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../source/711/1/SuperscalarProcessors.pdf#page=3)

### 原始文字层

````text
Superscalar Processors
• Requires instructions to be grouped for concurrent issuing. Grouping 
decisions take care of the pipeline hazards.
• Static multiple issue: Compiler forms issue packets. The issue packet can be 
thought of as a long instruction (VLIW: very long instruction word; EPIC: 
explicitly parallel instruction computer)
• Dynamic multiple issue: Hardware makes grouping decisions.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Superscalar Processors
• Requires instructions   to be grouped for concurrent  issuing.  Grouping
  decisions  take care of the pipeline  hazards.
    • Static multiple issue: Compiler forms issue packets. The issue packet can be
      thought of as a long instruction (VLIW: very long instruction word; EPIC:
      explicitly parallel instruction computer)
    • Dynamic multiple issue: Hardware makes grouping decisions.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Superscalar Processors
' Requires instructions to be grouped for concurrent issuing. Grouping
decisions take care of the pipeline hazards.
• Static multiple issue: Compiler forms issue packets. The issue packet can be
thought of as a long instruction (VLIW: very long instruction word; EPIC:
explicitly parallel instruction computer)
• Dynamic multiple issue: Hardware makes grouping decisions.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../source/711/1/SuperscalarProcessors.pdf#page=4)

### 原始文字层

````text
Software Pipelining
• We look at an example of software pipelining whereby the compiler 
groups (or schedules) instructions on multiple functional units.
• We use the MIPS R10K processor as an example.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Software Pipelining
•We look at an example of software pipelining  whereby the compiler
 groups (or schedules)  instructions   on multiple  functional units.
•We use the MIPS R10K processor  as an example.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Software Pipelining
' We look at an example of software pipelining whereby the compiler
groups (or schedules) instructions on multiple functional units.
• We use the MIPS RIOK processor as an example.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../../source/711/1/SuperscalarProcessors.pdf#page=5)

### 原始文字层

````text
MIPS R10K Processor
• MIPS R10K is a superscalar processor with 4 functional units. 
• The processor is capable of doing two floating-point operations and 
two integer operations per clock cycle. 
• One of these operations could be a memory access (a load or a store). 
• One of the integer operations could be a branch.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
MIPS R10K Processor
• MIPS R10K is a superscalar processor  with 4 functional units.
• The processor  is capable of doing  two floating-point  operations and
  two integer operations per clock cycle.
    • One of these operations could be a memory access (a load or a store).
    • One of the integer operations could be a branch.
````

### 图片文字 OCR（en-US，待对照原页）

````text
MIPS RIOK Processor
' MIPS RIOK is a superscalar processor with 4 functional units.
• The processor is capable of doing two floating-point operations and
two integer operations per clock cycle.
• One of these operations could be a memory access (a load or a store).
• One of the integer operations could be a branch.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../source/711/1/SuperscalarProcessors.pdf#page=6)

### 原始文字层

````text
Instruction Attributes
Instruction Latency Repeat rate
Integer add/sub/logical/branch 1 1
Integer load/store 2 1
Floating-point load/store 3 1
Floating-point add/sub/multiply 2 1
Floating-point multiply-add 3 1
Floating-point division 19Cost 21
为了某住
许分专门优化 CO
实际所知张
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Instruction Attributes
Instruction                       Latency       Repeat rate
Integer add/sub/logical/branch       1               1
Integer load/store                   2               1
Floating-point  load/store           3               1
Floating-point  add/sub/multiply     2               1               为了某住
Floating-point  multiply-add         3               1
Floating-point  division             19             21             许分专⻔优化
            CO                          Cost
                                 实际所知张
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
lnstruction Attributes
lnstruction
lnteger add/sub/logical/branch
lnteger load/store
FIoating-point load/store
FIoating-point add/sub/multiply
FIoating-point multiply-add
FIoating-poin
lSlOn
Latency
1
2
3
3
Repeat rate
1
1
1
1
1
````

### 图片文字 OCR（en-US，待对照原页）

````text
Instruction Attributes
Instruction
Integer add/sub/logical/branch
Integer load/store
Floating-point load/store
Floating-point add/sub/multiply
Floating-point multiply-add
Floating-poin
iSion
Latency
1
2
3
3
Repeat rate
1
1
1
1
1
21
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../../source/711/1/SuperscalarProcessors.pdf#page=7)

### 原始文字层

````text
Latency
• The latency of an instruction refers to the number of cycles an 
instruction takes to execute. 
• Since the processor is pipelined, the next instruction could start 
executing in the following cycle while the previous one is being 
executed.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Latency
• The latency of an instruction   refers to the number  of cycles an
  instruction   takes to execute.
• Since the processor  is pipelined,  the next instruction  could start
  executing in the following cycle while the previous one is being
  executed.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Latency
' The latency of an instruction refers to the number of cycles an
instruction takes to execute.
• Since the processor is pipelined, the next instruction could start
executing in the following cycle while the previous one is being
executed.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../../source/711/1/SuperscalarProcessors.pdf#page=8)

### 原始文字层

````text
Repeat rate
• The repeat rate of an instruction refers to the number of cycles before 
which another instruction of the same type cannot begin execution. 
• According to the instruction attributes table, all instructions except 
floating-point division could be issued every cycle. A floating-point 
division, however, can be issued only every 21st cycle.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Repeat rate
• The repeat rate of an instruction  refers to the number  of cycles before
  which another instruction   of the same type cannot begin execution.
• According to the instruction  attributes          table, all instructions   except
  floating-point  division  could be issued  every cycle. A floating-point
  division,  however, can be issued  only every 21st            cycle.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Repeat rate
' The repeat rate of an instruction refers to the number of cycles before
which another instruction of the same type cannot begin execution.
• According to the instruction attributes table, all instructions except
floating-point division could be issued every cycle. A floating-point
division, however, can be issued only every 21st cycle.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../../source/711/1/SuperscalarProcessors.pdf#page=9)

### 原始文字层

````text
DAXPY
for (i = 0; i < N; i++) {
 y[i] = a * x[i] + y[i]; 
} 
This multiplies a scalar a by a vector x and adds vector y to it (ax PLUS y = axpy). D 
for double precision.
Assume that a is in $s1, start address of x in $s2, and start address of y in $s3.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
DAXPY
for (i = 0; i < N; i++) {
   y[i] = a * x[i] + y[i];
}
This multiplies a scalar a by a vector x and adds vector y to it (ax PLUS y = axpy). D
for double precision.
Assume that a is in $s1, start address of    x in $s2, and start address of y in $s3.
````

### 图片文字 OCR（en-US，待对照原页）

````text
DAXPY
for (i
* x[i] + y[i];
This multiplies a scalar a by a vector x and adds vector y to it (ax PLUS y = axpy). D
for double precision.
Assume that a is in $sl, start address of x in $s2, and start address of y in $s3.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../source/711/1/SuperscalarProcessors.pdf#page=10)

### 原始文字层

````text
DAXPY
addiu $s4, $s2, 1000 ; set up x end pointer
addiu $s6, $s3, 1000 ; set up y end pointer
Loop: lf $f2, 0($s2) ; load x value in f2
lf $f3, 0($s3) ; load y value in f3
madd $f3, $s1, $f2 ;
sf $f3, 0($s3) ; store f3 to y
addiu $s2, $s2, 4 ; increment x pointer
addiu $s3, $s3, 4 ; increment y pointer
bne $s2, $s4, Loop ; back to the beginning of loop
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
DAXPY
           addiu $s4, $s2, 1000              ; set up x end pointer
           addiu $s6, $s3, 1000              ; set up y end pointer
Loop:      lf $f2, 0($s2)                    ; load x value in f2
           lf $f3, 0($s3)                    ; load y value in f3
           madd $f3, $s1, $f2                ;
           sf $f3, 0($s3)                    ; store f3 to y
           addiu $s2, $s2, 4                 ; increment x pointer
           addiu $s3, $s3, 4                 ; increment y pointer
           bne $s2, $s4, Loop                ; back to the beginning of loop
````

### 图片文字 OCR（en-US，待对照原页）

````text
DAXPY
Loop:
addiu $s4, $s2,
1000
addiu $s6, $s3,
1000
If $f2, 0($s2)
If $f3, 0($s3)
madd $f3, $sl, $f2
sf $f3, 0($s3)
addiu $s2, $s2, 4
addiu $s3, $s3, 4
bne $s2, $s4, Loop
; set up x end pointer
; set up y end pointer
; load x value in f2
; load y value in f3
; storef3 to y
; increment x pointer
; increment y pointer
• back to the beginning of loop
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../source/711/1/SuperscalarProcessors.pdf#page=11)

### 原始文字层

````text
Instruction Scheduling
Cycle FU #1 (FP) FU #2 (INT) FU #3 (INT) FU #4 (FP)
1 lf x1 addiu (x1)
2 lf y1
3
4
5 madd x1, y1
6
7
8 sf y1 addiu ( y1) bne
9
addiu $s4, $s2, 1000
addiu $s6, $s3, 1000
Loop: lf $f2, 0($s2)
lf $f3, 0($s3)
madd $f3, $s1, $f2
sf $f3, 0($s3)
addiu $s2, $s2, 4
addiu $s3, $s3, 4
bne $s2, $s4, Loop
What is the FU 
utilization here?
lag
a
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
addiu $s4, $s2, 1000
                                                                                                               addiu $s6, $s3, 1000
Instruction Scheduling
                                                                                                    Loop:      lf $f2, 0($s2)
                                                                                                               lf $f3, 0($s3)
Cycle         FU #1 (FP)           FU #2 (INT)              FU #3 (INT)               FU #4 (FP)               madd $f3, $s1, $f2
   1       lf x1                 addiu (x1)                                                                    sf $f3, 0($s3)
                                                                                                               addiu $s2, $s2, 4
   2       lf y1                                                                                               addiu $s3, $s3, 4
   3                                                                                                           bne $s2, $s4,  Loop
   4                                                                                                   lag
   5                                                                               madd x1, y1
   6         a                                                                                              What is the FU
                                                                                                            utilization here?
   7
   8       sf y1                 addiu ( y1)            bne
   9
````

### 图片文字 OCR（en-US，待对照原页）

````text
Instruction Scheduling
Cycle
1
2
3
4
5
6
7
8
9
If
If Yl
sf Yl
FU #2 ONT)
addiu (Xl)
addiu ( Yl)
FU #3 ONT)
bne
Loop:
3
madd Xl,
addiu $s4, $s2, 1000
addiu $s6, $s3, 1000
If $f2, 0($s2)
If $f3, 0($s3)
madd $f3, $sl, $f2
sf $f3, 0($s3)
addiu $s2, $s2, 4
addiu $s3, $s3, 4
ne $s2, $s4, Loop
What is the FU
utilization here?
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../source/711/1/SuperscalarProcessors.pdf#page=12)

### 原始文字层

````text
Exercises
• Unroll the DAXPY loop once and schedule the instructions
• Unroll the DAXPY loop twice and schedule the instructions
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Exercises
•Unroll  the DAXPY loop once and schedule  the instructions
•Unroll the DAXPY loop twice and schedule  the instructions
````

### 图片文字 OCR（en-US，待对照原页）

````text
Exercises
' Unroll the DAXPY loop once and schedule the instructions
• Unroll the DAXPY loop twice and schedule the instructions
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../../source/711/1/SuperscalarProcessors.pdf#page=13)

### 原始文字层

````text
DAXPY unrolled once
for (i = 0; i < N/2; i+=2) {
 y[i] = a * x[i] + y[i]; 
 y[i+1] = a * x[i+1] + y[i+1]; 
}
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
DAXPY unrolled once
for (i = 0; i < N/2; i+=2) {
   y[i] = a * x[i] + y[i];
   y[i+1] = a * x[i+1] + y[i+1];
}
````

### 图片文字 OCR（en-US，待对照原页）

````text
DAXPY unrolled once
for (i
0; i < N/ 2; i+=2) {
* x[i] + y[i];
y[i+l]
* x[i+l] + y[i+l]•,
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../../source/711/1/SuperscalarProcessors.pdf#page=14)

### 原始文字层

````text
Cycle FU #1 (FP) FU #2 (INT) FU #3 (INT) FU #4 (FP)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
addiu $s4, $s2, 1000
addiu $s6, $s3, 1000
Loop: lf $f2, 0($s2)
lf $f3, 0($s3)
madd $f3, $s1, $f2
sf $f3, 0($s3)
addiu $s2, $s2, 4
addiu $s3, $s3, 4
lf $f4, 0($s2)
lf $f5, 0($s3)
madd $f5, $s1, $f4
sf $f5, 0($s3)
addiu $s2, $s2, 4
addiu $s3, $s3, 4
bne $s2, $s4, Loop
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
addiu $s4, $s2, 1000
                                                                                                                                          addiu $s6, $s3, 1000
Cycle            FU #1 (FP)                  FU #2 (INT)                    FU #3 (INT)                     FU #4 (FP)Loop:               lf $f2, 0($s2)
   1                                                                                                                                      lf $f3, 0($s3)
   2                                                                                                                                      madd $f3, $s1, $f2
   3                                                                                                                                      sf $f3, 0($s3)
   4                                                                                                                                      addiu $s2, $s2, 4
   5                                                                                                                                      addiu $s3, $s3, 4
   6
   7                                                                                                                                      lf $f4, 0($s2)
   8                                                                                                                                      lf $f5, 0($s3)
   9                                                                                                                                      madd $f5, $s1, $f4
  10                                                                                                                                      sf $f5, 0($s3)
  11                                                                                                                                      addiu $s2, $s2, 4
  12                                                                                                                                      addiu $s3, $s3, 4
  13                                                                                                                                      bne $s2, $s4,  Loop
  14
````

### 图片文字 OCR（en-US，待对照原页）

````text
Cycle
1
2
3
4
5
6
7
8
9
10
11
12
13
14
FU #2 (INT)
FU #3 (INT)
Loop:
addiu $s4, $s2, 1000
addiu $s6, $s3, 1000
If $f2, 0($s2)
If $f3, 0($s3)
madd $f3, $sl, $f2
sf $f3, 0($s3)
addiu $s2, $s2, 4
addiu $s3, $s3, 4
If $f4, 0($s2)
If $f5, 0($s3)
madd $f5, $sl, $f4
sf $f5, 0($s3)
addiu $s2, $s2, 4
addiu $s3, $s3, 4
bne $s2, $s4, Loop
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../../source/711/1/SuperscalarProcessors.pdf#page=15)

### 原始文字层

````text
Cycle FU #1 (FP) FU #2 (INT) FU #3 (INT) FU #4 (FP)
1 lf x1 addiu (x1)
2 lf y1
3 lf x2 addiu (x2)
4 lf y2
5 madd x1, y1
6
7 madd x2, y2
8 sf y1 addiu (y1)
9
10 sf y2 addiu (y2) bne
11
12
13
14
addiu $s4, $s2, 1000
addiu $s6, $s3, 1000
Loop: lf $f2, 0($s2)
lf $f3, 0($s3)
madd $f3, $s1, $f2
sf $f3, 0($s3)
addiu $s2, $s2, 4
addiu $s3, $s3, 4
lf $f4, 0($s2)
lf $f5, 0($s3)
madd $f5, $s1, $f4
sf $f5, 0($s3)
addiu $s2, $s2, 4
addiu $s3, $s3, 4
bne $s2, $s4, Loop
What is the FU 
utilization here?
a
a
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
addiu $s4, $s2, 1000
                                                                                         What is the FU                               addiu $s6, $s3, 1000
                                                                                         utilization here?
Cycle            FU #1 (FP)                 FU #2 (INT)                   FU #3 (INT)                     FU #4 (FP)Loop:             lf $f2, 0($s2)
   1        lf x1                      addiu (x1)                                                                                     lf $f3, 0($s3)
   2        lf y1                                                                                                                     madd $f3, $s1, $f2
   3        lf x                       addiu (x    )                                                      a                           sf $f3, 0($s3)
                2                                 2
   4        lf y2                                                                                                                     addiu $s2, $s2, 4
   5                                                                                                madd x1, y1                       addiu $s3, $s3, 4
   6
   7                                                                                           a    madd x2, y2                       lf $f4, 0($s2)
   8        sf y1                      addiu (y1)                                                                                     lf $f5, 0($s3)
   9                                                                                                                                  madd $f5, $s1, $f4
  10        sf y2                      addiu (y2)                  bne                                                                sf $f5, 0($s3)
  11                                                                                                                                  addiu $s2, $s2, 4
  12                                                                                                                                  addiu $s3, $s3, 4
  13                                                                                                                                  bne $s2, $s4,  Loop
  14
````

### 图片文字 OCR（en-US，待对照原页）

````text
Cycle
1
2
3
4
5
6
7
8
9
10
11
12
13
14
If Xl
If Yl
If x2
If Y2
sf Yl
sf Y2
FU #2 (INT)
addiu (xo
addiu (x)
addiu (yo
addiu (h)
What is the FU
utilization here?
FU #3 (INT)
madd Xl,
madd x2, Y2
Loop:
bne
addiu $s4, $s2, 1000
addiu $s6, $s3, 1000
If $f2, 0($s2)
If $f3, 0($s3)
madd $f3, $sl, $f2
sf $f3, 0($s3)
addiu $s2, $s2, 4
addiu $s3, $s3, 4
If $f4, 0($s2)
If $f5, 0($s3)
madd $f5, $sl, $f4
sf $f5, 0($s3)
addiu $s2, $s2, 4
addiu $s3, $s3, 4
bne $s2, $s4, Loop
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../../source/711/1/SuperscalarProcessors.pdf#page=16)

### 原始文字层

````text
Cycle FU #1 (FP) FU #2 (INT) FU #3 (INT) FU #4 (FP)
1 lf x1 addiu (x1)
2 lf y1
3 lf x2 addiu (x2)
4 lf y2
5 madd x1, y1
6
7 madd x2, y2
8 sf y1 addiu (y1)
9
10 sf y2 addiu (y2) bne
11
12
13
14
addiu $s4, $s2, 1000
addiu $s6, $s3, 1000
Loop: lf $f2, 0($s2)
lf $f3, 0($s3)
madd $f3, $s1, $f2
sf $f3, 0($s3)
addiu $s2, $s2, 4
addiu $s3, $s3, 4
lf $f4, 4($s2)
lf $f5, 4($s3)
madd $f5, $s1, $f4
sf $f5, 0($s3)
addiu $s2, $s2, 8
addiu $s3, $s3, 8
bne $s2, $s4, Loop
What is the FU 
utilization here?
i ld.FI store
F
z it increase
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
addiu $s4, $s2, 1000
                                                                                     What is the FU                              addiu $s6, $s3, 1000
                                                                                     utilization here?
Cycle           FU #1 (FP)                FU #2 (INT)                  FU #3 (INT)                    FU #4 (FP)Loop:            lf $f2, 0($s2)
  1         lf x1                    addiu (x1)                                                                                  lf $f3, 0($s3)
  2         lf y1                                                                                                                madd $f3, $s1, $f2
  3         lf x2                    addiu (x2)                                                                                  sf $f3, 0($s3)
  4         lf y2                                                                                                                addiu $s2, $s2, 4
  5                                                                                              madd x1, y1                     addiu $s3, $s3, 4
  6
  7                                                                                              madd x2, y2                     lf $f4, 4($s2)
  8         sf y1                    addiu (y1)                                                                                  lf $f5, 4($s3)
  9                                                                                                                              madd $f5, $s1, $f4
  10        sf y2                    addiu (y2)                  bne                                                             sf $f5, 0($s3)
  11                                                                                                                             addiu $s2, $s2, 8
  12                                                                                                                             addiu $s3, $s3, 8
  13                                                                                                                             bne $s2, $s4,  Loop
  14
                      i                    ld.FI                     storeF               z       it       increase
````

### 图片文字 OCR（en-US，待对照原页）

````text
What is the FU
utilization here?
Cycle
1
2
3
4
5
6
7
8
9
10
11
12
13
14
If Xl
If Yl
If x2
If Y2
sf Yl
sf Y2
FU #2 (INT)
a.d.d.i.u44)
addiu (x)
addiu (h)
FU #3 (INT)
bne
Loop:
madd Xl,
madd x2, Y2
addiu $s4, $s2, 1000
addiu $s6, $s3, 1000
If $f2, 0($s2)
If $f3, 0($s3)
madd $f3, $sl, $f2
sf $f3, 0($s3)
If $f4, 4($s2)
If $f5, 4($s3)
madd $f5, $sl, $f4
sf $f5, 0($s3)
addiu $s2, $s2, g
addiu $s3, $s3, g
bne $s2, $s4, Loop
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../../source/711/1/SuperscalarProcessors.pdf#page=17)

### 原始文字层

````text
Cycle FU #1 (FP) FU #2 (INT) FU #3 (INT) FU #4 (FP)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
load中 load mad Store 2 1皉 increase
load亏 loadI madF storeF 2 指针 increase branch.I
2， 2
load badzeaddxpo.in
add pointer loads
mad I
stored addypointer load4 0
a made
d b
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
load中       load      mad     Store      2  1皉    increase
                                     storeF    2  指针    increase   branch.I
      load亏       loadI     madF
Cycle   FU #1 (FP)    FU #2 (INT)    FU #3 (INT)     FU #4 (FP)          2/gid1582
 1     load
 2      badzeaddxpo.in
 3                                    add            loads
 4                                         pointer
 5                                                    mad      I
 6
 7
 8     stored       addy
 9                       pointer
 10                                                  load4     0
 11
 12 a    made
 13
 14
                       d               b
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
CycIe
1
2
3
4
5
6
7
8
9
FU # 1 (FP)
FU # 2 (INT)
FU # 3 (INT)
FU # 4 (FP)
````

### 图片文字 OCR（en-US，待对照原页）

````text
Cycle
1
2
3
4
5
6
7
8
9
10
11
12
13
14
FU #2 (INT)
FU #3 (INT)
FU #4 (FP)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 18 页

[查看此页](../../../../source/711/1/SuperscalarProcessors.pdf#page=18)

### 原始文字层

````text
Cycle FU #1 (FP) FU #2 (INT) FU #3 (INT) FU #4 (FP)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15 store addypointer branch
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
15         store          addy       pointer       branch
Cycle      FU #1 (FP)        FU #2 (INT)          FU #3 (INT)          FU #4 (FP)
  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
 11
 12
 13
 14
````

### 图片文字 OCR（en-US，待对照原页）

````text
Cycle
1
2
3
4
5
6
7
8
9
10
11
12
13
14
FU #2 (INT)
FU #3 (INT)
FU #4 (FP)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 19 页

[查看此页](../../../../source/711/1/SuperscalarProcessors.pdf#page=19)

### 原始文字层

````text
Further Work
• Read Chapter 4 of the book: Computer Organization and Design – The 
Hardware Software Interface RISC-V edition, 2nd edition (2020)
• Read https://en.wikipedia.org/wiki/Software_pipelining
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Further Work
•Read Chapter 4 of the book: Computer Organization and Design – The
 Hardware Software Interface RISC-V edition, 2nd edition  (2020)
•Read https://en.wikipedia.org   /wiki/Software_pipelining
````

### 图片文字 OCR（en-US，待对照原页）

````text
Further Work
' Read Chapter 4 of the book: Computer Organization and Design — The
Hardware Software Interface RISC-V edition, 2nd edition (2020)
• Read https://en.wikipedia.org/wiki/Software_pipelining
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 20 页

[查看此页](../../../../source/711/1/SuperscalarProcessors.pdf#page=20)

### 原始文字层

````text
¿?
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

> OCR 未识别出可靠文字；本页可能以图形、手写公式或空白为主。

### 图表辅助说明

本页中央仅有“¿?”提问／结束标记，没有课件正文。

## PDF 第 21 页

[查看此页](../../../../source/711/1/SuperscalarProcessors.pdf#page=21)

### 原始文字层

````text
缓存
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Caches
。 A cache is a small local memory holding items Of interest
ltems Of interest include items we used in the recent past and items we may
use in the future.
。 Example: a browser cache that holds the web content YO u looked at recently
· Why is such a cache useful?
。 Avoiding re-fetching items over a (slow) network
· Processors a re a lOt faster than memory
````

### 图片文字 OCR（en-US，待对照原页）

````text
Caches
• A cache is a small local memory holding items of interest
• Items of interest include items we used in the recent past and items we may
use in the future.
e Example: a browser cache that holds the web content you looked at recently
• Why is such a cache useful?
• Avoiding re-fetching items over a (slow) network
• Processors are a lot faster than memory
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

