# Processor+Design+Recap.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI711/source/711/1/Processor+Design+Recap.pdf`
- [打开原文件](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf)
- 原文件 SHA-256：`9fdcfe9ef626ad0ef8f51e4704fa8da300f05d0cb3e796bd2fc98e63b8f95cda`
- 文件索引：F060；PDF 总页数：60
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=1)

### 原始文字层

````text
MIPS Processor Design Recap
mano@cs.auckland.ac.nz
````

### 图片文字 OCR（en-US，待对照原页）

````text
MIPS Processor Design Recap
mano@cs.auckland.ac.nz
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=2)

### 原始文字层

````text
MIPS Introduction
• MIPS is a RISC (reduced instruction set computer) processor.
• We will briefly look at some of the principles of processor design in 
the light of improving performance and using concurrency.
• We will start with the very basics.
Computer Organization and Design – The 
Hardware Software Interface RISC-V 
edition, 2nd edition (2020)
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
MIPS Introduction
• MIPS is a RISC (reduced instruction   set computer) processor.
• We will briefly look at some of the principles  of processor design in
  the light of improving  performance and using concurrency.
• We will start with the very basics.
Computer Organization and Design – The
  Hardware Software Interface RISC-V
      edition, 2nd edition (2020)
````

### 图片文字 OCR（en-US，待对照原页）

````text
MIPS Introduction
' MIPS is a RISC (reduced instruction set computer) processor.
• We will briefly look at some of the principles of processor design in
the light of improving performance and using concurrency.
' We will start with the very basics.
Computer Organization and Design — The
Hardware Software Interface RISC-V
edition, 2nd edition (2020)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=3)

### 原始文字层

````text
Instruction Set Architecture (ISA)
• This is the programmers view of the processor. It defines the machine 
language exposed by the processor.
• Machine language is just a bunch of 0s and 1s. Hard for any of us to speak.
• An assembly language is a human-readable form of the machine language.
• So an ISA mostly uses assembly language to denote the machine language.
• An assembler is a program that translates assembly language to machine 
language. 
• Compilers translate high-level languages (e.g., C++) to assembly language.
• Strictly speaking an ISA is the compiler’s view of the processor.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Instruction Set Architecture (ISA)
• This is the programmers view of the processor.  It defines the machine
  language exposed  by the processor.
    • Machine language is just a bunch of 0s and 1s. Hard for any of us to speak.
    • An assembly language is a human-readable form of the machine language.
    • So an ISA mostly uses assembly language to denote the machine language.
    • An assembler is a program that translates assembly language to machine
      language.
    • Compilers translate high-level languages (e.g., C++) to assembly language.
• Strictly speaking  an ISA is the compiler   ’s  view of the processor.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Instruction Set Architecture (ISA)
' This is the programmers view of the processor. It defines the machine
language exposed by the processor.
• Machine language is just a bunch of Os and Is. Hard for any of us to speak.
• An assembly language is a human-readable form of the machine language.
• So an ISA mostly uses assembly language to denote the machine language.
• An assembler is a program that translates assembly language to machine
language.
• Compilers translate high-level languages (e.g., C++) to assembly language.
• Strictly speaking an ISA is the compiler's view of the processor.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=4)

### 原始文字层

````text
Storage space
• A processor has two sets of storage space: a 
bank of registers and a linear array of memory.
• Memory is organized as bytes and each byte is 
individually addressable.
• Words are the smallest units of data we get out 
of/into memory
• A word, for example, could be 4 bytes (32 bits) or 8 
bytes (64 bits)
0 8 bits of data
1 8 bits of data
2 8 bits of data
… 8 bits of data
… 8 bits of data
corn
s­o
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Storage space
• A processor  has two sets of storage space: a                       0      8 bits of data
  bank of registers and a linear array of memorycorn          .       1      8 bits of data
• Memory is organized as bytes and each byte is                       2      8 bits of data
  individually  addressable.                                          …      8 bits of data
    • Words are the smallest units of data we get out                 …      8 bits of data
      of/into memory                so
    • A word, for example, could be 4 bytes (32 bits) or 8
      bytes (64 bits)
````

### 图片文字 OCR（en-US，待对照原页）

````text
Storage space
o sets of storage space: a
' A process
bank
registers nd a linear array of memory.
• Memory is organized as bytes and each yt is
individually addressable.
• Words are the malle units of data we get out
of/into memory
• A word, for example, could be 4 bytes (32 bits) or 8
bytes (64 bits)
o
1
2
8 bits of data
8 bits of data
8 bits of data
8 bits of data
8 bits of data
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=5)

### 原始文字层

````text
MIPS Storage Space
• For MIPS, a word is 32 bits or 4 bytes.
• 232 bytes with byte addresses from 0 to 232-1
• 230 words with byte addresses 0, 4, 8, ... 232-4
• Registers hold 32 bits of data, and there are 32 registers
0 32 bits of data
4 32 bits of data
8 32 bits of data
12 32 bits of data
… 32 bits of data
0 8 bits of data
1 8 bits of data
2 8 bits of data
… 8 bits of data
… 8 bits of data
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
MIPS Storage Space
• For MIPS, a word is 32  bits or 4 bytes.
    •  232 bytes with byte addresses from 0 to 232-1
    •  230 words with byte addresses 0, 4, 8, ... 232-4
• Registers hold 32 bits of data, and there are 32 registers
 0       8 bits of data               0       32 bits of data
 1       8 bits of data               4       32 bits of data
 2       8 bits of data               8       32 bits of data
 …       8 bits of data               12      32 bits of data
 …       8 bits of data               …       32 bits of data
````

### 图片文字 OCR（en-US，待对照原页）

````text
MIPS Storage Space
' For MIPS, a word is 32 bits or 4 bytes.
• 232 bytes with byte addresses from 0 to 232-1
• 230 words with byte addresses 0, 4, 8, ... 232-4
• Registers hold 32 bits of data, and there are 32 registers
o
1
2
8 bits of data
8 bits of data
8 bits of data
8 bits of data
8 bits of data
o
4
8
12
32 bits of data
32 bits of data
32 bits of data
32 bits of data
32 bits of data
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=6)

### 原始文字层

````text
MIPS Registers – Assembler Conventions
0 zero 16 s0 Callee saves
1 at Reserved for assembler … … (caller can clobber)
2 v0 Expression evaluation 23 s7
3 v1 Function results 24 t8 Temp (cont.)
4 a0 Function arguments 25 t9
5 a1 26 k0 Reserved for OS kernel
6 a2 27 k1
7 a3 28 gp Global pointer
8 t0 Temp (caller saves) 29 sp Stack pointer
… … (callee can clobber) 30 fp Frame pointer
15 t7 31 ra Return address
攡用函数
汇编
_
顧
fumion
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
MIPS Registers – Assembler Conventions
  0    zero                             16  s0    Callee⽤ saves函数
                          汇编顧                    攡
  1    at     Reserved  for assembler   …   …     (caller can clobber)
  2    v0     Expression evaluation_    23  s7
  3    v1     Function results          24  t8    Temp (cont.)
  4    a0     Function arguments        25  t9
  5    a1                               26  k0    Reserved  for OS kernel
  6    a2                               27  k1
  7    a3                               28  gp    Global pointer
  8    t0     Temp (caller saves)       29  sp    Stack pointer
  …    …      (callee can clobber)      30  fp    Frame pointer
  15   t7        fumion                 31  ra    Return address
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
M lPS Registers _ Assembler Conventions
0
1
2
3
4
5
6
7
8
15
zero
at
v0
vl
a0
a 1
a2
a3
t0
t7
Reserved for åssembl
Expression evaluation
Function results
Function arguments
Temp (caller saves)
(callee can clobber)
16
23
24
25
26
27
28
29
30
31
s0
s7
t8
t9
k0
kl
gp
SP
fp
ra
e saves
(caller ca n clobber)
Temp (cont.)
Reserved for OS kernel
GIobaI pointer
Stack pointer
Frame pointer
Return address
- 0 《 亏 岢 仔
编 号
0
1
8 ． 15
16 ． 23
24 · 25
26 ． 27
28
29
30
名 称
Z e ro
at
ve-vl
ae-a3
te-t7
sø-s7
t8-t9
ke—kl
SP
作 用
恒 为 0
保 留 给 汇 编 器
表 达 式 / 函 数 返 回 值
函 数 参 数
临 时 变 量 (caller 保 存 ）
保 存 变 量 (callee 保 存 ）
临 时 变 量 （ 继 续 使 用 ）
OS 内 核 保 留
全 局 指 针
栈 指 针
帧 指 针
返 回 地 址
说 明
读 总 是 返 回 0 ， 写 无 效
assembler temporary ， 汇 编 器
内 部 使 用
用 于 返 回 函 数 结 果
前 4 个 数 通 过 寄 存 器 传 递
调 用 者 在 调 用 函 数 前 需 保 存
被 调 用 者 保 存 和 恢 复 这 些 值
与 tO ． t7 一 样 ， ca r 需 保 存
仅 操 作 系 统 使 用
指 向 全 局 数 据 区 域
指 向 当 前 栈 顶
用 于 访 问 当 前 栈 帧 中 的 变 量 （ 可 选 ）
存 放 函 数 调 用 的 返 回 地 址
````

### 图片文字 OCR（en-US，待对照原页）

````text
MIPS
ae-a3
te-t7
sø-s7
ke-kl
Registers — Assembler Conventions
0
1
2
3
4
5
6
7
8
15
zero
at
vl
to
Reserved for åssembl
Expression evaluation
Function results
Function arguments
Temp (caller saves)
(callee can clobber)
16
23
24
25
26
27
28
29
30
31
t8
t9
k0
gp
sp
fp
ra
ale saves
(caller can clobber)
Temp (cont.)
Reserved for OS kernel
Global pointer
Stack pointer
Frame pointer
Return address
O
1
2-3
4-7
8-15
16-23
24-25
26-27
28
29
30
31
zero
at
t8
gp
sp
fp
ra
-VI
(callerfRF)
(calleefRF)
ihBh
assembler temporary,
(EJi±)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=7)

### 原始文字层

````text
MIPS instructions – A selection
Instruction Meaning Type
add $s1, $s2, $s3 $s1 = $s2 + $s3 R
sub $s1, $s2, $s3 $s1 = $s2 – $s3 R
lw $s1, 100($s2) $s1 = Memory[$s2+100] I
sw $s1, 100($s2) Memory[$s2+100] = $s1 I
bne $s4,$s5,Label Next instr. is at Label if $s4 != $s5 I
beq $s4,$s5,Label Next instr. is at Label if $s4 = $s5 I
j Label Next instr. is at Label J
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
MIPS instructions – A selection
Instruction                 Meaning                                          Type
add $s1, $s2, $s3           $s1 = $s2 + $s3                                    R
sub $s1, $s2, $s3           $s1 = $s2 – $s3                                    R
lw $s1, 100($s2)            $s1 = Memory[$s2+100]                               I
sw $s1, 100($s2)            Memory[$s2+100]  = $s1                              I
bne $s4,$s5,Label           Next instr. is at Label if $s4 != $s5               I
beq $s4,$s5,Label           Next instr. is at Label if $s4 = $s5                I
j Label                     Next instr. is at Label                             J
````

### 图片文字 OCR（en-US，待对照原页）

````text
MIPS instructions — A selection
Next instr. is at Label
Instruction
add $sl, $s2, $s3
sub $sl, $s2, $s3
lw $sl, 100($s2)
sw $sl, 100($s2)
bne $s4,$s5,Label
beq $s4,$s5,Label
j Label
Meaning
$sl = Memory[$s2+100]
Memory[$s2+100] = $sl
Next instr. is at Label if $s4 != $s5
Next instr. is at Label if $s4 =
Type
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=8)

### 原始文字层

````text
Instruction Types
6 bits 5 bits 5 bits 5 bits 5 bits 6 bits
R op rs rt rd shamt func
I op rs rt 16 bit address
J op 26 bit address
For branch instructions, the address is an offset from the current program counter (PC).
Question: how can we do a longer branch than permissible by the 16 bit offset? Answer:
beq $t0, $t1, far
could be implemented as
bneq $t0, $t1, near
j far
near: …
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Instruction Types
             6 bits      5 bits     5 bits      5 bits     5 bits      6 bits
  R             op          rs          rt         rd       shamt        func
  I             op          rs          rt             16 bit address
  J             op                         26 bit address
 For branch instructions, the address is an offset from the current program counter (PC).
 Question: how can we do a longer branch than permissible by the 16 bit offset? Answer:
            beq        $t0, $t1, far
 could be implemented as
            bneq       $t0, $t1, near
            j          far
 near:      …
````

### 图片文字 OCR（en-US，待对照原页）

````text
Instruction Types
6 bits
op
op
op
5 bits
rs
rs
5 bits
rt
rt
5 bits
rd
5 bits
shamt
6 bits
func
16 bit address
26 bit address
For branch instructions, the address is an offset from the current program counter (PC).
Question: how can we do a longer branch than permissible by the 16 bit offset? Answer:
$tO, $tl, far
beq
could be implemented as
bneq
j
near:
$tO, $tl, near
far
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=9)

### 原始文字层

````text
Assembler Macros
• These are convenience “instructions” provided by the assembler. 
Assembler translates them to real instruction during assembly.
• E.g. the macro move $t0, $1 will be translated to add $t0, $t1, $zero.
宏
大 二 十1 to
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Assembler Macros                    宏
•These are convenience “instructions”   provided  by the assembler.
 Assembler  translates them to real instruction  during  assembly.
   • E.g. the macro move $t0, $1 will be translated to add $t0, $t1, $zero.
                                                              ⼤   ⼆ ⼗1    to
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Assembler Macros
． These a re convenience 'finstructions" provided by the assembler.
Assembler translates them tO real instruction during assembly.
． E.g. the macro move $t0, $ 1 will be translated t0 add $t0, $tl, $zero.
千 0 多 到 子 0
````

### 图片文字 OCR（en-US，待对照原页）

````text
Assembler Macros
' These are convenience "instructions" provided by the assembler.
Assembler translates them to real instruction during assembly.
• E.g. the macro move $t0, $1 will be translated to add $t0, $tl, $zero.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=10)

### 原始文字层

````text
Question – Assembler Macros
• Question: MIPS has an slt (set if less than) instruction: slt $t1, $s1, $2 
will set $t1 to one if $s1 is less than $s2, otherwise it clear $t1 (i.e., 
set it to 0). How would you implement a new blt (branch less than) 
instruction as an assembler macro using slt and bne?
• Answer: blt $s1, $s2, label could be implemented as:
slt $t0, $s1, $s2
bne $t0, $zero, label
Questions: (a) do you see any potential for problems in the implementation? (b) can we consider using beq instead of 
bne?
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Question – Assembler Macros
 • Question:  MIPS has an slt (set if less than) instruction: slt $t1, $s1, $2
   will set $t1 to one if $s1 is less than $s2, otherwise it clear $t1 (i.e.,
   set it to 0). How would you implement  a new blt (branch less than)
   instruction   as an assembler macro using slt and bne?
 • Answer: blt $s1,  $s2,  label could be implemented as:
          slt $t0, $s1, $s2
          bne $t0, $zero, label
Questions: (a) do you see any potential for problems in the implementation? (b)  can we consider using beq instead of
bne?
````

### 图片文字 OCR（en-US，待对照原页）

````text
Question — Assembler Macros
' Question: MIPS has an slt (set if less than) instruction: slt $tl, $sl, $2
will set $tl to one if $sl is less than $s2, otherwise it clear $tl (i.e.,
set it to O). How would you implement a new blt (branch less than)
instruction as an assembler macro using slt and bne?
• Answer: blt $sl, $s2, label could be implemented as:
slt $0, $sl, $s2
bne $t0, $zero, label
Questions: (a) do you see any potential for problems in the implementation? (b) can we consider using beq instead of
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=11)

### 原始文字层

````text
MIPS Arithmetic
Instruction Example Meaning
add add $1, $2, $3 $1 = $2 + $3
subtract sub $1, $2, $3 $1 = $2 - $3
add immediate add $1, $2, 100 $1 = $2 + 100
add unsigned addu $1, $2, $3 $1 = $2 + $3
subtract unsigned subu $1, $2, $3 $1 = $2 - $3
add immediate unsigned addiu $1, $2, 100 $1 = $2 + 100
multiply mult $2, $3 Hi, Lo = $2 * $3
multiply unsigned multu $2, $3 Hi, Lo = $2 * $3
divide div $2, $3 Lo = $2/$3; Hi = $2 mod $3
divide unsigned divu $2, $3 Lo = $2/$3; Hi = $2 mod $3
move from hi mfhi $1 $1 = Hi
move from lo mflo $1 $1 = Lo
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
MIPS Arithmetic
Instruction                   Example                Meaning
add                           add $1, $2, $3         $1 = $2 + $3
subtract                      sub $1, $2, $3         $1 = $2 - $3
add immediate                 add $1, $2, 100        $1 = $2 + 100
add unsigned                  addu $1, $2, $3        $1 = $2 + $3
subtract unsigned             subu $1, $2, $3        $1 = $2 - $3
add immediate unsigned        addiu $1, $2, 100      $1 = $2 + 100
multiply                      mult $2, $3            Hi, Lo = $2 * $3
multiply unsigned             multu $2, $3           Hi, Lo = $2 * $3
divide                        div $2, $3             Lo = $2/$3; Hi = $2 mod $3
divide unsigned               divu $2, $3            Lo = $2/$3; Hi = $2 mod $3
move from hi                  mfhi $1                $1 = Hi
move from lo                  mflo $1                $1 = Lo
````

### 图片文字 OCR（en-US，待对照原页）

````text
MIPS Arithmetic
Instruction
add
subtract
add immediate
add unsigned
subtract unsigned
add immediate unsigned
multiply
multiply unsigned
divide
divide unsigned
move from hi
move from 10
Example
add $1, $2, $3
sub $1, $2, $3
add $1, $2, 100
addu $1, $2, $3
subu $1, $2, $3
addiu $1, $2, 100
mult $2, $3
multu $2, $3
div $2, $3
divu $2, $3
mfhi $1
mflo $1
Meaning
$1 = $2-$3
$1 = $2 + 100
$1 = $2-$3
$1 = $2 + 100
Hi, Lo = $2 * $3
Hi, Lo = $2 * $3
Lo = $2/$3; Hi = $2 mod $3
Lo = $2/$3; Hi = $2 mod $3
$1
$1 = Lo
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=12)

### 原始文字层

````text
MIPS Logical
Instruction Example Meaning
and and $1, $2, $3 $1 = $2 and $3
or or $1, $2, $3 $1 = $2 or $3
and immediate andi $1, $2, 100 $1 = $2 and 100
or immediate ori $1, $2, 100 $1 = $2 or 100
shift left logical sll $1, $2, 10 $1 = $2 << 10
shift right logical srl $1, $2, 10 $1 = $2 >> 10
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
MIPS Logical
Instruction          Example               Meaning
and                  and $1, $2, $3        $1 = $2 and $3
or                   or $1, $2, $3         $1 = $2 or $3
and immediate        andi $1, $2, 100      $1 = $2 and 100
or immediate         ori $1, $2, 100       $1 = $2 or 100
shift left logical   sll $1, $2, 10        $1 = $2 << 10
shift right logical  srl $1, $2, 10        $1 = $2 >> 10
````

### 图片文字 OCR（en-US，待对照原页）

````text
Logical
MIPS
Instruction
and
or
sli $1, $2, 10
$2, 10
Example
and $1, $2, $3
or $1, $2, $3
andi $1, $2, 100
and immediate
or immediate
shift left logical
shift right logical
ori $1,
sr1 $1,
$2, 100
Meaning
$1 = $2 and $3
$1 = $2 and 100
$1 = $2 or 100
$1
= $2 << 10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=13)

### 原始文字层

````text
MIPS Data Transfer
Instruction Example Meaning
load word lw $1, 100($2) $1 = Memory[$2+100]
store word sw $1, 100($2) Memory[$2+100] = $1
load upper immediate lui $1, 100 $1 = 100 * 216
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
MIPS Data Transfer
 Instruction             Example            Meaning
 load word               lw $1, 100($2)     $1 = Memory[$2+100]
 store word              sw $1, 100($2)     Memory[$2+100] = $1
 load upper immediate    lui $1, 100        $1 = 100 * 216
````

### 图片文字 OCR（en-US，待对照原页）

````text
MIPS
Instruction
load word
store word
Data Transfer
load upper immediate
Example
lw $1, 100($2)
sw $1,
100($2)
lui $1, 100
Meaning
$1 = Memory[$2+100]
Memory[$2+100] = $1
$1 = *216
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=14)

### 原始文字层

````text
MIPS Control Transfer
Instruction Example Meaning
branch equal beq $1, $2, L1 if ( $1 == $2 ) go to L1
branch not equal bne $1, $2, L1 if ( $1 != $2 ) go to L1
set less than slt $1, $2, $3 $1 = ($2<$3) ? 1 : 0
set less than immediate slti $1, $2, 100 $1 = ($2<100) ? 1 : 0
set less than unsigned sltu $1, $2, $3 $1 = ($2<$3) ? 1 : 0
slt immediate unsigned sltiu $1, $2, 100 $1 = ($2<100) ? 1 : 0
jump j 10000 go to 10000
jump register j $31 go to $31
jump and link jal 10000 $31=PC+4; go to 10000
word length
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
MIPS Control Transfer
Instruction                  Example             Meaning
branch equal                 beq $1, $2, L1      if ( $1 == $2 ) go to L1
branch not equal             bne $1, $2, L1      if ( $1 != $2 ) go to L1
set less than                slt $1, $2, $3      $1 = ($2<$3) ? 1 : 0
set less than immediate      slti $1, $2, 100    $1 = ($2<100) ? 1 : 0
set less than unsigned       sltu $1, $2, $3     $1 = ($2<$3) ? 1 : 0
slt immediate unsigned       sltiu $1, $2, 100   $1 = ($2<100) ? 1 : 0
jump                         j 10000             go to 10000
jump register                j $31               go to $31
jump and link                jal 10000           $31=PC+4; go to 10000
                                                                                                       word              length
````

### 图片文字 OCR（en-US，待对照原页）

````text
MIPS Control Transfer
Instruction
branch equal
branch not equal
set less than
set less than immediate
set less than unsigned
slt immediate unsigned
jump
jump register
jump and link
Example
beq $1, $2, Ll
bne $1, $2, Ll
sit $1, $2, $3
siti $1, $2, 100
situ $1, $2, $3
sitiu $1, $2, 100
j 10000
j $31
jal 10000
Meaning
= $2 ) go to Ll
if ($1 $2 ) go to Ll
go to 10000
go to $31
$31 =PC+4; go to 10000
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=15)

### 原始文字层

````text
Example: How to speedup Loops
while ( i < 10 ) { 
sum += array[i]; 
++i; 
}
for (i = 0; i < 10; ++i ) { 
sum += array[i]; 
}
addiu $t9, $a0, 40
Loop: beq $a0, $t9, Exit
lw $t0, 0($a0)
add $s0, $s0, $t0
addiu $a0, $a0, 4
j Loop
Exit: …
Each loop iteration has 2 branch instructions!
gdlenglh.­endoosartf4
vn a 二 七9 exit
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Example: How to speedup Loopsgdlenglh                               .endoosar    tf4
while ( i < 10 )  {                            addiu $t9, $a0, 40
        sum += array[i];               Loop:   beq $a0, $t9, Exitvn       a    ⼆  七9      ex  i  t
        ++i;                                   lw $t0, 0($a0)
}                                              add $s0, $s0, $t0
for (i = 0;  i < 10; ++i ) {                   addiu $a0, $a0, 4
         sum += array[i];                      j Loop
}                                      Exit:   …
          Each loop iteration has 2 branch instructions!
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
ExampIe: HOW t0 speedup LOOPS
while （ i < 10 ） {
S u m + = array[i];
fo r (i = 0 ； i < 10 ； ++i ） {
sum + = array[i];
e 女 鉕 彤
Loop: beq $a $t9, Exit
lw $t0, 0 （ $ a0 ）
add $sO, $sO, $tO
addiu $aO, $aO, 4
j LOOP
Exit:
Each IOOP iteration has 2 branch instructi
````

### 图片文字 OCR（en-US，待对照原页）

````text
Example: How to speedup Loops
while (i < 10) {
sum += array[i];
for (i = 0; i < 10; ++i ) {
sum += array[i];
Loop:
Exit:
$@Y'b elem..lf
beq $a $t9, Exit
Iw $tO, O($a0)
add $so, $so, $to
addiu $a0, $aO, 4
j Loop
Each loop iteration has 2 branch instructi
s!
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=16)

### 原始文字层

````text
Example: How to speedup Loops
addiu $t9, $a0, 40
beq $a0, $t9, Exit
Loop: lw $t0, 0($a0)
add $s0, $s0, $t0
addiu $a0, $a0, 4
bne $a0, $t9, Loop
Exit: …
addiu $t9, $a0, 40
Loop: beq $a0, $t9, Exit
lw $t0, 0($a0)
add $s0, $s0, $t0
addiu $a0, $a0, 4
j Loop
Exit: …
for (i = 0; i < 10; ++i ) { 
sum += array[i]; 
}
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Example: How to speedup Loops
        addiu $t9, $a0, 40                    addiu $t9, $a0, 40
Loop:   beq $a0, $t9, Exit                    beq $a0, $t9, Exit
        lw $t0, 0($a0)                Loop:   lw $t0, 0($a0)
        add $s0, $s0, $t0                     add $s0, $s0, $t0
        addiu $a0, $a0, 4                     addiu $a0, $a0, 4
        j Loop                                bne $a0, $t9, Loop
Exit:   …                             Exit:   …
                 for (i = 0;  i < 10; ++i ) {
                          sum += array[i];
                 }
````

### 图片文字 OCR（en-US，待对照原页）

````text
Example: How to speedup Loops
Loop:
Exit:
addiu $t9, $a0, 40
beq $a0, $t9, Exit
Iw $t0, O($aO)
add $s0, $sO, $tO
addiu $aO, $aO, 4
j Loop
for (i =
Loop:
Exit:
addiu $t9, $ao, 40
beq $a0, $t9, Exit
Iw $tO, O($a0)
add $s0, $sO, $tO
addiu $a0, $aO, 4
bne $a0, $t9, Loop
sum += array[i];
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=17)

### 原始文字层

````text
Example: How to speedup Loops
addiu $t9, $a0, 40
Loop: lw $t0, 0($a0)
add $s0, $s0, $t0
addiu $a0, $a0, 4
bne $a0, $t9, Loop
Exit: …
addiu $t9, $a0, 40
beq $a0, $t9, Exit
Loop: lw $t0, 0($a0)
add $s0, $s0, $t0
addiu $a0, $a0, 4
bne $a0, $t9, Loop
Exit: …
for (i = 0; i < 10; ++i ) { 
sum += array[i]; 
}
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Example: How to speedup Loops
        addiu $t9, $a0, 40                     addiu $t9, $a0, 40
        beq $a0, $t9, Exit
Loop:   lw $t0, 0($a0)                 Loop:   lw $t0, 0($a0)
        add $s0, $s0, $t0                      add $s0, $s0, $t0
        addiu $a0, $a0, 4                      addiu $a0, $a0, 4
        bne $a0, $t9, Loop                     bne $a0, $t9, Loop
Exit:   …                              Exit:   …
                 for (i = 0;  i < 10; ++i ) {
                          sum += array[i];
                 }
````

### 图片文字 OCR（en-US，待对照原页）

````text
Example: How to speedup Loops
Loop:
Exit:
addiu $t9, $a0, 40
beq $a0, $t9, Exit
Iw $t0, O($aO)
add $s0, $sO, $tO
addiu $aO, $aO, 4
bne $a0, $t9, Loop
for (i =
Loop:
Exit:
addiu $t9, $a0, 40
Iw $tO, O($aO)
add $s0, $sO, $t0
addiu $aO, $aO, 4
bne $a0, $t9, Loop
sum += array[i];
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 18 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=18)

### 原始文字层

````text
Example: Loop Unrolling
for (i = 0; i < 10; ++i ) { 
sum += array[i]; 
}
4 instructions per iteration has now become 7 instructions per 2 
iterations
for (i = 0; i < 10; i +=1) { 
sum += array[i];
++i;
sum += array[i];
}
addiu $t9, $a0, 40
Loop: lw $t0, 0($a0)
add $s0, $s0, $t0
addiu $a0, $a0, 4
lw $t0, 0($a0)
add $s0, $s0, $t0
addiu $a0, $a0, 4
bne $a0, $t9, Loop
Exit: …
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Example: Loop Unrolling
for (i = 0;  i < 10; ++i ) {                    addiu $t9, $a0, 40
         sum += array[i];
}                                      Loop:    lw $t0, 0($a0)
                                                add $s0, $s0, $t0
for (i = 0;  i < 10; i +=1) {                   addiu $a0, $a0, 4
         sum += array[i];                       lw $t0, 0($a0)
         ++i;                                   add $s0, $s0, $t0
         sum += array[i];                       addiu $a0, $a0, 4
}
                                                bne $a0, $t9, Loop
                                       Exit:    …
   4 instructions per iteration has now become 7 instructions per 2
                                iterations
````

### 图片文字 OCR（en-US，待对照原页）

````text
Example: Loop Unrolling
for (i
for (i =
sum += array[i];
sum += array[i];
sum += arrayfil;
Loop:
Exit:
addiu $t9, $a0, 40
Iw $tO, O($a0)
add $s0, $sO, $tO
addiu $a0, $aO, 4
Iw $tO, O($a0)
add $so, $so, $to
addiu $a0, $aO, 4
bne $a0, $t9, Loop
4 instructions per iteration has now become 7 instructions per 2
iterations
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 19 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=19)

### 原始文字层

````text
Example: Loop Unrolling
We now have 6 instructions per 2 iterations
for (i = 0; i < 10; ++i ) { 
sum += array[i]; 
}
for (i = 0; i < 10; i +=1) { 
sum += array[i];
++i;
sum += array[i];
}
addiu $t9, $a0, 40
Loop: lw $t0, 0($a0)
add $s0, $s0, $t0
lw $t0, 4($a0)
add $s0, $s0, $t0
addiu $a0, $a0, 8
bne $a0, $t9, Loop
Exit: …
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Example: Loop Unrolling
for (i = 0;  i < 10; ++i ) {                   addiu $t9, $a0, 40
         sum += array[i];
}                                     Loop:    lw $t0, 0($a0)
                                               add $s0, $s0, $t0
for (i = 0;  i < 10; i +=1) {
         sum += array[i];                      lw $t0, 4($a0)
         ++i;                                  add $s0, $s0, $t0
         sum += array[i];                      addiu $a0, $a0, 8
}
                                               bne $a0, $t9, Loop
                                      Exit:    …
              We now have 6 instructions per 2 iterations
````

### 图片文字 OCR（en-US，待对照原页）

````text
Example: Loop Unrolling
for (i
for (i =
sum += array[i];
sum += array[i];
sum += arrayfil;
Loop:
Exit:
addiu $t9, $a0, 40
Iw $tO, O($a0)
add $s0, $sO, $tO
Iw $tO, 4($a0)
add $so, $so, $to
addiu $a0, $aO, g
bne $a0, $t9, Loop
We now have 6 instructions per 2 iterations
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 20 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=20)

### 原始文字层

````text
Hardware bits
````

### 图片文字 OCR（en-US，待对照原页）

````text
Hardware bits
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 21 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=21)

### 原始文字层

````text
A Single Bit Adder
b
a
Carry In
Carry Out
````

### 图片文字 OCR（en-US，待对照原页）

````text
A Single Bit Adder
Carry In
a
b
Carry Out
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 22 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=22)

### 原始文字层

````text
0
2
1
Operation
Result
CarryOut
CarryIn
b
a
+
A Single Bit ALU
````

### 图片文字 OCR（en-US，待对照原页）

````text
A Single Bit ALU
Carryln
a
b
CarryOut
Operation
1
2
Result
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 23 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=23)

### 原始文字层

````text
Multi Bit ALU
Result 1 0 -bit ALU
a0
b0
Cin
Cout
Result 1 1 -bit ALU
a1
b1
Cout
Operation
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Multi Bit ALU
                  Cin         Operation
a0
            1-bit ALU                 Result0
b0
a1                Cout
            1-bit ALU                 Result1
b1
                  Cout
````

### 图片文字 OCR（en-US，待对照原页）

````text
Multi
Bit ALU
I-bit ALU
I-bit ALU
bl
cout
Operation
Resulto
Resulti
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 24 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=24)

### 原始文字层

````text
Register
Clk
Data In
WriteEnable
N N
Data Out
Combinational logic (or combinatorial logic) is a logic circuit whose 
output depends only on its current input. In contrast, in a sequential
logic, the output will depend not only on the current input but also 
some past inputs. Sequential logic circuits have memory. A register here 
is a sequential logic circuit. The content of the register can be read 
anytime, but the register can only be written at the clock’s tick only 
when WriteEnable is set (to 1).
Similar to the D Flip Flop except: N-bit input and output; 
and WriteEnable input
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Register
WriteEnable                                      Similar to the D Flip Flop except: N-bit input and output;
Data In               Data Out                   and WriteEnable input
    N                   N
                     Clk
Combinational logic (or combinatorial logic) is a logic circuit whose
output depends only on its current input. In contrast, in a sequential
logic, the output will depend not only on the current  input but also
some past inputs. Sequential logic circuits have memory. A register here
is a sequential logic circuit. The content of the register can be read
anytime, but the register can only be written at the clock’s tick only
when WriteEnable is set (to 1).
````

### 图片文字 OCR（en-US，待对照原页）

````text
Register
WriteEnable
Data In
Similar to the D Flip Flop except: N-bit input and output;
and WriteEnable input
Data Out
Clk
Combinational logic (or combinatorial logic) is a logic circuit whose
output depends only on its current input. In contrast, in a sequential
logic, the output will depend not only on the current input but also
some past inputs. Sequential logic circuits have memory. A register here
is a sequential logic circuit. The content of the register can be read
anytime, but the register can only be written at the clock's tick only
when WriteEnable is set (to 1).
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 25 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=25)

### 原始文字层

````text
Register File
Clk
busW
WriteEnable
32
32
busA
32
busB
5 5 5
RW RA RB
32 32-bit
Registers
A register file is simply a set of registers. In case of MIPS, there are 
32 registers in the register file.
BusA and busB always pick up the content of the registers RA and 
RB (irrespective of the clock). Register RW is written to with the 
data on busW at the clock’s tick only if WriteEnable is set.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Register File
WriteEnable        RW    RA   RB
                   5    5     5
                                   busA
  busW             32 32-bit           32
      32Clk        Registers       busB
                                       32
A register file is simply a set of registers. In case of MIPS, there are
32 registers  in the register file.
BusA and busB always pick up the content of the registers  RA and
RB (irrespective of the clock). Register RW is written to with the
data on busW at the clock’s tick only if WriteEnable is set.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Register File
RW RA RB
WriteEnable
busW
32
Clk
5
32 32-bit
Registers
busA
32
busB
32
A register file is simply a set of registers. In case of MIPS, there are
32 registers in the register file.
BusA and busB always pick up the content of the registers RA and
RB (irrespective of the clock). Register RW is written to with the
data on busW at the clock's tick only if WriteEnable is set.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 26 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=26)

### 原始文字层

````text
Memory
Clk
Data In
WriteEnable
32 32
DataOut
Address
The memory is idealized for simplicity. The CLK input is 
a factor only during write operation. During read 
operation, the memory behaves as a combinational 
logic block: DataOut becomes valid after access time.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Memory
  WriteEnable          Address
Data In                       DataOut
   32Clk                            32
The memory is idealized for simplicity. The CLK input is
a factor only during write operation. During read
operation, the memory behaves  as a combinational
logic block: DataOut becomes valid after access time.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Memory
WriteEnable
Data In
32
Clk
Address
DataOut
32
The memory is idealized for simplicity. The CLK input is
a factor only during write operation. During read
operation, the memory behaves as a combinational
logic block: DataOut becomes valid after access time.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 27 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=27)

### 原始文字层

````text
Instruction Fetch Unit
32
Instruction Word
Address
Instruction 
Memory
Clk PC
Next Address
Logic
Fetch the Instruction: InstructionMemory[PC]
Update the program counter:
Sequential Code: PC = PC + 4 
Branch and Jump: PC = “something else”
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Instruction Fetch Unit
                                                     Fetch the Instruction: InstructionMemory[PC]
Clk          PC                                      Update the program counter:
                            Next Address                       Sequential Code: PC = PC + 4
                                Logic
                                                               Branch and Jump:   PC = “something else”
             Address
          Instruction         Instruction Word
           Memory                  32
````

### 图片文字 OCR（en-US，待对照原页）

````text
Instruction Fetch Unit
Clk-----O
Address
Instruction
Memory
Next Address
Logic
Instructio
32
Fetch the Instruction: InstructionMemory[PC]
Update the program counter:
Sequential Code: PC = PC + 4
Branch and Jump: PC = "something else"
Word
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 28 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=28)

### 原始文字层

````text
Single Cycle Datapath – Arithmetic/Logic
32
Result
ALUctr
Clk
busW
RegWr
32
32
busA
32
busB
5 5 5
Rw Ra Rb
32 32-bit
Registers
Rd Rs Rt
ALU
R[rd] = R[rs] op R[rt]
Rs, Rt, and Rd come from instruction’s rs, rt, and rd fields
ALUctr and RegWr: control logic after decoding the instruction 
点线
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Single Cycle Datapath – Arithmetic/Logic
                        Rd   Rs    Rt                         ALUctr
             RegWr     5    5     5
                                          点busA线
                       Rw    Ra   Rb
      busW             32  32-bit               32                            Result
         32            Registers                                       32
           Clk                              busB
                                                32
R[rd] = R[rs] op R[rt]
Rs, Rt, and Rd come from instruction’s rs, rt, and rd fields
ALUctr and RegWr: control logic after decoding the instruction
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Single CycIe Datapath _ Arithmetic/Logic
RegWr
busW
Clk
R[rd] = R[rs] op R[rt]
Rd
5
Rw
Rs
5
Ra
ALUctr
5
32 32-bit
Registers
busA
32
busB
32
Result
32
Rs, R t, and Rd come from instruction's rs / rt, and rd fields
ALUctr and RegWr: control logic after decoding the instruction
````

### 图片文字 OCR（en-US，待对照原页）

````text
Single Cycle Datapath
RegWr
busW
32
Clk
R[rd] = R[rs] op R[rt]
Rd
5
Rw
5
Ra
5
32 32-bit
Registers
busA
32
busB
32
Arithmetic/Logic
ALUctr
Result
32
Rs, Rt, and Rd come from instruction's rs, rt, and rd fields
ALUctr and RegWr: control logic after decoding the instruction
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 29 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=29)

### 原始文字层

````text
imm16
32
ALUctr
Clk
busW
RegWr
32
32
busA
32
busB
5 5 5
Rw Ra Rb
32 32-bit
Registers
Rs
Rt
Rt
Rd
RegDst
Extender
Mux
32 16
imm16
ExtOp ALUSrc
Mux
MemtoReg
Clk
Data In
WrEn 32 Adr
Data
Memory
MemWr
ALU
Equal
Instruction<31:0>
0
1
0
1
1 0 <21:25>
<16:20>
<11:15>
<0:15>
Rs Rt Rd Imm16
=
Adder Adder
PC
Clk
Mux
4
nPC_sel
PC Ext
Addr
Inst
Memory
Notes: PC Ext(imm16) = SignExt(imm16)x4. Rt is the destination for arithmetic ops 
with immediate.
i­t
if Pinstation
jumpaddress
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Inst                                      Instruction<31:0>
                             Memory
                                 Addr
                                           Rs    Rt    Rd    Imm16
                     nPC_sel       RegDst        Rt             Equal         ALUctr   MemWr       MemtoReg
                                            Rd
                                           1    0
        4                          RegWr            Rs   Rt
                                            5    5    5
                                            Rw    Ra  Rb   busA                  =
                                 busW       32  32-bit             32
              it                   32       Registers      busB        0                32               0
                                                            32
                                    Clk                                       32        WrEn    Adr      1
                         Clk                                           1     Data In
                                      imm16     16             32                          Data
                                                                                  Clk     Memory
               Pinstation
jumpifaddress                                             ExtOp    ALUSrc
````

### 图片文字 OCR（en-US，待对照原页）

````text
Instruction<31:0>
Rd
nP
sel
Clk
Inst
Memory
Addr
Re Dst
RegWr
busW
32
Clk
Imm16
Equal
busA
ALUctr
32
Data In
Clk
MemWr
32
MemtoReg
32 32-bit
Registers
imm16
16
bus
32
32
Extop
32
ALUSrc
WrEn Adr
Data
Memory
hts+uctton
honch//
Ju+tp address
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 30 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=30)

### 原始文字层

````text
RegDst ExtOp ALUSrc ALUctr MemWr MemtoReg Equal
Instruction<31:0> <21:25> <16:20>
<11:15>
<0:15>
Rt Rs Rd Imm16
nPC_sel
Inst
Memory
DATA PATH
Control
Op
<21:25>
Func
RegWr
Generating Control Signals
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Generating Control Signals
               Instruction<31:0>
   Inst
Memory
             Op  Func Rt    Rs  Rd    Imm16
                           Control
   nPC_selRegWr RegDstExtOp ALUSrc  ALUctr MemWr   MemtoReg       Equal
                          DATA PATH
````

### 图片文字 OCR（en-US，待对照原页）

````text
Generating Control Signals
Instruction<31:0>
Inst
Memory
O
Op Func
nPC_sel RegWr RegDst
Rs Rd Immi6
Control
Extop ALUSrc ALUctr
DATA PATH
MemWr
MemtoReg
Equal
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 31 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=31)

### 原始文字层

````text
The Five Steps on Instruction Execution
• Fetch the instruction from the instruction memory
• Register fetch and instruction decode
• ALU execution or memory address calculation (using ALU)
• Read the data from the data memory
• Write the data back to the register file
Not all instructions will require all the steps
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
The Five Steps on Instruction Execution
 • Fetch the instruction   from the instruction  memory
 • Register fetch  and instruction   decode
 • ALU execution or memory address calculation (using  ALU)
 • Read the data from the data memory
 • Write the data back to the register file
Not all instructions will require all the steps
````

### 图片文字 OCR（en-US，待对照原页）

````text
The Five Steps on Instruction Execution
' Fetch the instruction from the instruction memory
• Register fetch and instruction decode
• ALU execution or memory address calculation (using ALU)
• Read the data from the data memory
• Write the data back to the register file
Not all instructions will require all the steps
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 32 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=32)

### 原始文字层

````text
Exercise
The MIPS pseudo-instruction swap exchanges the contents of two registers (e.g., 
swap $s0, $s1). After the sequence completes, the destination register has the 
original value of the source register, and the source register has the original value 
of the destination register. 
This pseudo-instruction is synthesized by the MIPS assembler using three xor 
instructions: 
xor a, a, b
xor b, a, b
xor a, a, b
An alternative ISA design for the MIPS might include an opcode for swap, thus 
making it a real instruction. Both the original and the alternative designs use a 
single cycle datapath. Describe the key modifications required in the datapath in 
order to implement swap.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Exercise
The MIPS pseudo-instruction swap exchanges the contents of two registers (e.g.,
swap $s0, $s1). After the sequence completes, the destination register has the
original value of the source register, and the source register has the original value
of the destination register.
This pseudo-instruction is synthesized by the MIPS assembler using three xor
instructions:
    xor a, a, b
    xor b, a, b
    xor a, a, b
An alternative ISA design for the MIPS might include an opcode for swap, thus
making it a real instruction. Both the original and the alternative designs use a
single cycle datapath. Describe the key modifications required in the datapath in
order to implement swap.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Exercise
The MIPS pseudo-instruction swap exchanges the contents of two registers (e.g.,
swap $s0, $sl). After the sequence completes, the destination register has the
original value of the source register, and the source register has the original value
of the destination register.
This pseudo-instruction is synthesized by the MIPS assembler using three xor
instructions:
xor a, a, b
xor b, a, b
xor a, a, b
An alternative ISA design for the MIPS might include an opcode for swap, thus
making it a real instruction. Both the original and the alternative designs use a
single cycle datapath. Describe the key modifications required in the datapath in
order to implement swap.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 33 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=33)

### 原始文字层

````text
Discussion
• Cycle time for load is much longer than needed for all other 
instructions
• Since we have a single cycle, all operations take the longest cycle 
time, i.e., the cycle time of load
• Instruction Memory Access Time 
• Register File Access Time 
• ALU Delay (address calculation) 
• Data Memory Access Time 
• Register File Setup Time
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Discussion
• Cycle time for load is much  longer than needed for all other
  instructions
• Since we have a single cycle, all operations take the longest cycle
  time, i.e., the cycle time of load
    • Instruction Memory Access Time
    • Register File Access Time
    • ALU Delay (address calculation)
    • Data Memory Access Time
    • Register File Setup Time
````

### 图片文字 OCR（en-US，待对照原页）

````text
Discussion
' Cycle time for load is much longer than needed for all other
instructions
• Since we have a single cycle, all operations take the longest cycle
time, i.e., the cycle time of load
Instruction Memory Access Time
Register File Access Time
• ALU Delay (address calculation)
Data Memory Access Time
Register File Setup Time
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 34 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=34)

### 原始文字层

````text
Multiple Cycle Datapath
• Break each instruction into a series of steps corresponding to 
the functional unit operations required
• Each of these steps will take 1 clock cycle
• We can use a functional unit more than once per instruction as 
long as it is used on different clock cycles
• Less resource use; savings on real estate
• We can use a unified memory – no need to have separate 
instruction & data memories
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Multiple Cycle Datapath
• Break each instruction  into a series of steps corresponding  to
  the functional unit operations  required
    • Each of these steps will take 1 clock cycle
• We can use a functional unit  more than once per instruction as
  long as it is used on different clock cycles
    • Less resource use; savings on real estate
• We can use a unified  memory – no need to have separate
  instruction   & data memories
````

### 图片文字 OCR（en-US，待对照原页）

````text
Multiple Cycle Datapath
' Break each instruction into a series of steps corresponding to
the functional unit operations required
• Each of these steps will take 1 clock cycle
' We can use a functional unit more than once per instruction as
long as it is used on different clock cycles
• Less resource use; savings on real estate
' We can use a unified memory — no need to have separate
instruction & data memories
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 35 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=35)

### 原始文字层

````text
Single Cycle Datapath – Logical Blocks ALUctr RegDst ALUSrc ExtOp nPC_sel RegWr MemRd MemWr MemToReg Equal Next PC PC Reg File Instructrion Fetch Exec MemoryReg File
Add registers between blocks for storing 
intermediate values/results
Instruction
Fetch
Register
Fetch
Execution
Memory
Access
Memory read 
completion
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Single Cycle Datapath – Logical Blocks
````

### 图片文字 OCR（en-US，待对照原页）

````text
Single Cycle Datapath
Logical Blocks
8
o
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 36 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=36)

### 原始文字层

````text
Multiple Cycle Datapath – Logical Blocks ALUctr RegDst ALUSrc ExtOp nPC_sel RegWr MemRd MemWr MemToReg Equal Next PC PC Reg File Instructrion Fetch Exec MemoryReg File
Add registers between blocks for storing 
intermediate values/results. The physical data 
transfers between these registers realize the 
logical instructions.
Instruction
Fetch
Register
Fetch
Execution
Memory
Access
Memory read 
completion
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Multiple Cycle Datapath – Logical Blocks
````

### 图片文字 OCR（en-US，待对照原页）

````text
Multiple Cycle Datapath
Logical Blocks
Q.)
o
Q)
Q.)
Q.)
o
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 37 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=37)

### 原始文字层

````text
R-Type Add
• Logical register transfers:
• R[rd]  R[rs] + R[rt]; PC  PC + 4
• Physical register transfers:
• IR  MEM[PC]; PC  PC + 4 ① instruction fetch
• A  R[rs]; B  R[rt] ② instruction decode & register fetch
• ALUOut  A + B ③execution, memory address computation, or 
branch completion
• R[rd]  ALUOut ④ memory access, or R-Type instruction completion
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
R-Type Add
' Logical register transfers:
• R[rd] R[rs] + R[rt]; PC k- PC +4
' Physical register transfers:
IR e MEM[PC]; pc e PC+4 0 instruction fetch
• A R[rs]; B R[rt] @ instruction decode & register fetch
ALUOut e A+B
branch completion
• R[rd] k- ALUOut
@ execution, memory address computation, or
@ memory access, or R-Type instruction completion
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 38 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=38)

### 原始文字层

````text
Load
• Logical register transfers:
• R[rt]  Mem[ R[rs] + SignExt(Imm16) ]; PC  PC + 4
• Physical register transfers:
• IR  MEM[PC]; PC  PC + 4 ① instruction fetch
• A  R[rs] ② instruction decode & register fetch
• ALUOut  A + SignExt(Imm16) ③execution, memory address computation, 
or branch completion
• MDR  Mem[ ALUOut ] ④ memory access, or R-Type instruction 
completion)
• R[rt]  MDR ⑤ memory read completion
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Load
' Logical register transfers:
• R[rt] Mem[ R[rs] + SignExt(lmm16) ]; PC PC +4
' Physical register transfers:
IR e MEM[PC]; pc e PC+4 0 instruction fetch
• A R[rs] @ instruction decode & register fetch
• ALUOut A + SignExt(lmm16) @ execution, memory address computation,
or branch completion
• MDR k- Mem[ ALUOut ] @ memory access, or R-Type instruction
completion)
• R[rt] M DR @ memory read completion
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 39 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=39)

### 原始文字层

````text
Store
• Logical register transfers:
• Mem[ R[rs] + SignExt(Imm16) ]  R[rt]; PC  PC + 4
• Physical register transfers:
• IR  MEM[PC]; PC  PC + 4 ① instruction fetch
• A  R[rs]; B  R[rt] ② instruction decode & register fetch
• ALUOut  A + SignExt(Imm16) ③execution, memory address computation, 
or branch completion
• Mem[ ALUOut ]  B ④ memory access, or R-Type instruction completion
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Store
' Logical register transfers:
• Mem[ R[rs] + SignExt(lmm16) ] R[rt]; PC PC +4
' Physical register transfers:
IR e MEM[PC]; pc e PC+4 0 instruction fetch
• A R[rs]; B R[rt] @ instruction decode & register fetch
• ALUOut A + SignExt(lmm16) @ execution, memory address computation,
or branch completion
• Mem[ ALUOut ] k- B @ memory access, or R-Type instruction completion
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 40 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=40)

### 原始文字层

````text
Branch: BEQ
• Logical register transfers:
• PC  (A==B) ? (PC + 4 + SignExt(Imm16)x4) : (PC + 4)
• Physical register transfers:
• IR  MEM[PC]; PC  PC + 4 ① instruction fetch
• A  R[rs]; B  R[rt]; ALUOut  PC + SignExt(Imm16)x4 ② instruction 
decode & register fetch
• If ( A == B ) PC  ALUOut ③ execution, memory address computation, 
or branch completion
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Branch: BEQ
' Logical register transfers:
PC e ? (PC+4+ : (pc + 4)
' Physical register transfers:
IR e MEM[PC]; pc e PC+4 0 instruction fetch
• A R[rs]; B R[rt]; ALUOut PC + Sign Ext(Imm16)x4 @ instruction
decode & register fetch
• If ( A == B ) PC ALUOut @ execution, memory address computation,
or branch completion
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 41 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=41)

### 原始文字层

````text
Ideal
Memory
Din
Addr
32
Dout
MemWrite
32
ALU
32
32
ALUOp
ALU
Control
32
IRWrite
32
Reg File
Ra
Rw
busW
Rb
5
5 busA
busB
RegWrite
Rs
Rt
0Mux
1
Rt
Rd
ALUSrcA
1 Mux 0
RegDst
0Mux
1
32
MemtoReg
0Mux
1
32
0
1
2
3
4
16 Imm 32
ALUSrcB
Mux
1
0
32
Zero
PCSrc
32
IorD
32
PCWrite
Zero
PCWrCond
<<2
Extend
PC
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
PCWrite           PCWrCond                                                                 PCSrc
                             Zero
          IorD        MemWrite       IRWrite      RegDst         RegWrite       ALUSrcA           1      32
 PC                  32
                32                                                                       0        0         Zero
          0                                       Rs              Ra
    32              Addr                          Rt      5       Rb     busA                    32
   32                  Ideal                  32                                         1
          1                                       Rt  0   5        Reg File                   0
                     Memory                                       Rw                                           32
                                32                Rd                     busB          4      1   32
                    Din   Dout                        1           busW
            32                                                                                2        ALU
                                                    1  Mux    0             <<2               3      Control
                                           Imm            Extend
                                                  16                   32                             ALUOp
                                                                     MemtoReg            ALUSrcB
````

### 图片文字 OCR（en-US，待对照原页）

````text
PCWrite
32
3
lorD
0
32
PCWrCond
Zero
MemWrite
32
32
Addr
Ideal
Memory
32
Din Dout
IRWrite
32
RegDst
5
5
1 Mux
RegWrite
busA
Reg File
Rw
busB
busW
ALUSrcA
0
4
0
PCSrc
0
1
2
3
1
32
32
32
Zero
32
ALU
Control
ALUOp
o
Imm
16
Extend
32
MemtoReg
ALUSrcB
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 42 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=42)

### 原始文字层

````text
Generating Control Signals
• Generating control signals is more complex than for the single cycle 
datapath.
• Control signals are generated using a finite state machine or using 
microprogramming. 
• Refer to the textbook mentioned in the last slide if interested.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Generating Control Signals
•Generating control signals is more complex than for the single cycle
 datapath.
•Control signals are generated using a finite state machine or using
 microprogramming.
   • Refer to the textbook mentioned in the last slide if interested.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Generating Control Signals
' Generating control signals is more complex than for the single cycle
datapath.
• Control signals are generated using a finite state machine or using
microprogramming.
• Refer to the textbook mentioned in the last slide if interested.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 43 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=43)

### 原始文字层

````text
Single Cycle Datapath
• If all instructions must complete within one clock cycle, then the 
cycle time has to be large enough to accommodate the slowest
instruction.
• For example, lw $t0, –4($sp) needs 8ns/13ns, assuming the delays 
shown here.
Case 1 Case 2
reading the instruction memory 2ns 3ns
reading the base register $sp 1ns 2ns
computing memory address $sp-4 2ns 3ns
reading the data memory 2ns 3ns
storing data back to $t0 1ns 2ns
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Single Cycle Datapath
• If all instructions   must  complete within one clock cycle, then the
  cycle time has to be large enough to accommodate the slowest
  instruction.
• For example, lw $t0, –4($sp) needs 8ns/13ns,   assuming  the delays
  shown here.
                                         Case 1       Case 2
reading the instruction  memory           2ns          3ns
reading the base register $sp             1ns          2ns
computing memory address $sp-4            2ns          3ns
reading the data memory                   2ns          3ns
storing data back to $t0                  1ns          2ns
````

### 图片文字 OCR（en-US，待对照原页）

````text
Single Cycle Datapath
' If all instructions must complete within one clock cycle, then the
cycle time has to be large enough to accommodate the slowest
instruction.
• For example, lw $0, —4($sp) needs 8ns/13ns, assuming the delays
shown here.
reading the instruction memory
reading the base register $sp
computing memory address $sp-4
reading the data memory
storing data back to $t0
Case 1
2ns
Ins
2ns
2ns
Ins
Case 2
3ns
2ns
3ns
3ns
2ns
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 44 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=44)

### 原始文字层

````text
Single Cycle Datapath
• If we make the cycle time 8ns then every instruction will take 8ns, 
even if they don’t need that much time.
• For example, the instruction add $s4, $t1, $t2 really needs just 
6ns/10ns.
Case 1 Case 2
reading the instruction memory 2ns 3ns
reading registers $t1 and $t2 1ns 2ns
computing $t1 + $t2 2ns 3ns
storing the result into $s0 1ns 2ns
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Single Cycle Datapath
• If we make the cycle time 8ns  then every instruction  will take 8ns,
  even if they don’t need that much time.
• For example, the instruction add $s4,  $t1, $t2 really needs just
  6ns/10ns.
                                         Case 1       Case 2
reading the instruction  memory            2ns          3ns
reading registers $t1 and $t2              1ns          2ns
computing $t1 + $t2                        2ns          3ns
storing the result into $s0                1ns          2ns
````

### 图片文字 OCR（en-US，待对照原页）

````text
Single Cycle Datapath
' If we make the cycle time 8ns then every instruction will take 8ns,
even if they don't need that much time.
• For example, the instruction add $s4, $tl, $t2 really needs just
6ns/10ns.
reading the instruction memory
reading registers $tl and $t2
computing $tl + $t2
storing the result into $s0
Case 1
2ns
Ins
2ns
Ins
Case 2
3ns
2ns
3ns
2ns
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 45 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=45)

### 原始文字层

````text
Multiple Cycle Datapath
• The GNU C compiler, gcc, is reported to have the following instruction 
mix
• What is the performance gain of a multiple cycle implementation over 
a single cycle implementation for running gcc?
Instruction Frequency
Arithmetic 48%
Loads 22%
Stores 11%
Branches 19%
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Multiple Cycle Datapath
• The GNU C compiler, gcc, is reported to have the following instruction
  mix
                            Instruction   Frequency
                            Arithmetic      48%
                              Loads         22%
                              Stores        11%
                             Branches       19%
• What is the performance  gain of a multiple  cycle implementation over
  a single cycle implementation for running gcc?
````

### 图片文字 OCR（en-US，待对照原页）

````text
Multiple Cycle Datapath
' The GNU C compiler, gcc, is reported to have the following instruction
mix
Instruction
Arithmetic
Loads
Stores
Branches
Frequency
48%
22%
11%
19%
' What is the performance gain of a multiple cycle implementation over
a single cycle implementation for running gcc?
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 46 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=46)

### 原始文字层

````text
Further Reading
• Computer Organization and Design – The Hardware Software 
Interface RISC-V edition, 2nd edition (2020)
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Further Reading
•Computer Organization and Design – The Hardware Software
 Interface RISC-V edition, 2nd edition (2020)
````

### 图片文字 OCR（en-US，待对照原页）

````text
Further Reading
' Computer Organization and Design — The Hardware Software
Interface RISC-V edition, 2nd edition (2020)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 47 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=47)

### 原始文字层

````text
¿?
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

> OCR 未识别出可靠文字；本页可能以图形、手写公式或空白为主。

### 图表辅助说明

本页中央仅有“¿?”提问／结束标记，没有课件正文。

## PDF 第 48 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=48)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（en-US，待对照原页）

````text
Pipelining
mano@cs.auckland.ac.nz
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 49 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=49)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（en-US，待对照原页）

````text
Pipelining
• Pipelining provides an efficient way of executing multiple tasks
concurrently
• The laundry example
• We have four loads of laundry to do. This consists of washing, drying, and
folding.
• Washer takes 30 minutes
• Dryer takes 40 minutes
• Folding takes 20 minutes
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 50 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=50)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（en-US，待对照原页）

````text
Sequential Laundry
61'M
30
7
40 20 30
10
11 Midnight
Time
40 20 30
40 20 30 40 20
Sequential laundry takes 6 hours for 4 loads
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 51 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=51)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（en-US，待对照原页）

````text
Pipelined Laundry
30
7
40
40
40
10
Time
40 20
11
Midnight
Pipelined laundry takes 3 h hours for 4 loads
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 52 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=52)

### 原始文字层

````text
0
recurve
````

### 图片文字 OCR（en-US，待对照原页）

````text
Pipelining
30
7
40
40
8
40
9
Time
40 20
a
S
d
Multiple tasks operating
simultaneously
Pipelining doesn't help atency
of single
throughput of entire workload
Pi eline rate limited by the
slowes ipelin sta e
Potential speedup = number
pipe stages
Unbalanced lengths of pipe
stages reduces speedup
Also, need time to "fill" and
"drain" the pipeline.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 53 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=53)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（en-US，待对照原页）

````text
The Load Instruction
• Fetch the instruction from the instruction memory
• Register fetch and instruction decode
• Calculate the memory address (using ALIJ)
• Read the data from the data memory
• Write the data back to the register file
Cycle 1 Cycle 2
Load Ifetch
Re ec
Cycle 3 Cycle 4
Exec
Mem
Cycle 5 •
Wr
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 54 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=54)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（en-US，待对照原页）

````text
The Steps of the MIPS Datapath
Instruction
Fetch
4
Instr. Decode
Reg. Fetch
Next SEQ pc
RSI
RS2
Extend
m 16
RD
Execute
Address Calc
Next SEQ pc
Zero?
C
c
RD
Memory
Access
O
RD
Write
Back
Next PC
m
Control signals
"flow" with data
down the pipeline
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 55 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=55)

### 原始文字层

````text
f pig
````

### 图片文字 OCR（en-US，待对照原页）

````text
Visualizing Pipelining
Time (clock cycles)
• Cycle 1 Cycle 2 Cycle 3 Cycle 4? ycle 5
Reg
Reg
Reg I
: Cycle 6 Cycle 7
Reg .
Reg
Multiple instructions
are in various stages at
the same time
Reg
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 56 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=56)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（en-US，待对照原页）

````text
Visualizing Pipelining
Time (clock cycles)
: Cycle 1 Cycle 2 Cycle 3 Cycle 4 Cycle 5 : Cycle 6
Can help with answering
Cycle 7
1
S
t
e
1.
2.
3.
Reg
Reg
questions such as:
How many cycles
does it take to
execute this code?
What is the ALIJ
doing during cycle 4?
Are two instructions
trying to use the
same resource at the
same time?
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 57 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=57)

### 原始文字层

````text
0多了 攤 存读数据
只用4个阶段
5个阶断鬻要
需要进行net 全 惭
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Comparison Of Processor Design
Clk
Singlé Cycl e lmplementation:
Load
三 Cycle 1 § cycle 2 cycle 3
Clk
Multiple CycIe lmplementation:
St re
《 CycIe 7 § cycle 8
： Waste
三 Cycl e 4
Mem
Mem
Exec
Reg
三 Cyc
Wr
Wr
Mem
Exec
ycle 6
： Store
lfetch
Wr
Mem
三 CycIe 9
Mem
cle 《 0
三 R-type
lfetch
： Load
lfetch
Reg
Pipeliie lmplementation:
Load lfetch
Reg
Sto re lfetch
R-type
Exec
Exec
Reg
lfetch
Reg
Wr
Exec
````

### 图片文字 OCR（en-US，待对照原页）

````text
Comparison of Processor Design
Cycle 1
Clk
Singl? Cycle Implementation:
Load
Cycle I Cycle 2 Cycle 3
Clk
Multiéle Cycle Implementation:
St re
: Cycle 7 Cycle 8
Cycle 4
Mem
Mem
Exec
Reg
cyc
Wr
Wr
Mem
Exec
ycle 6
Store
Ifetch
Wr
Mem
Cycle 9
Mem
Waste
cle iO
R-type
Ifetch
Load
Ifetch
Reg
Pipeliie Implementation:
Load Ifetch
Reg
Store Ifetch
R-type
Exec
Exec
Reg
Ifetch
Reg
Wr
Exec
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 58 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=58)

### 原始文字层

````text
men 时针同期数
t 平均每个指令
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Comparison Of Processor Design
· SUPPOse we have 100 instructions tO execute
· Single cycle processor has a cycle time of 45 ns
Multi cycle and pipeline processors have cycle times 0f 10 ns
· SingIe cycle processor
45 ns/cycle x 1 CPI × 100 inst = 4500 ns
MuIti cycle processor
10 n s/cycl e × 3 ． 8 CPI x 100 inst = 3800 ns
。 ldeal pipelined machine
10 ns/cycle × （ 1 CPI × 100 inst + 4 cycle "drain") = 1040 ns
· ldeal pipelined vs. single cycle speedup
4500 ns / 1040 ns = 4 ． 33
````

### 图片文字 OCR（en-US，待对照原页）

````text
Comparison of Processor Design
• Suppose we have 100 instructions to execute
• Single cycle processor has a cycle time of 45 ns
• Multi cycle and pipeline processors have cycle times of 10 ns
• The multi cycle processor has a CPI of 3.8
• Single cycle processor
• 45 ns/cycle x 1 CPI x 100 inst = 4500 ns
• Multi cycle processor
• 10 ns/cycle x 3.8 CPI x 100 inst = 3800 ns
• Ideal pipelined machine
• 10 ns/cycle x (1 CPI x 100 inst + 4 cycle "drain") = 1040 ns
• Ideal pipelined vs. single cycle speedup
• 4500 ns/ 1040 ns=4.33
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 59 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=59)

### 原始文字层

````text
一
隐患
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Pipeline Hazards
。 A hazard prohibits the execution Of a planned instruction in the
proper cycle.
。 Three forms 0f hazards m ay exist in a pipeline.
。 Structural hazard
· Data hazard
· Control hazard
````

### 图片文字 OCR（en-US，待对照原页）

````text
Pipeline Hazards
• A hazard prohibits the execution of a planned instruction in the
proper cycle.
• Three forms of hazards may exist in a pipeline.
• Structural hazard
• Data hazard
• Control hazard
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 60 页

[查看此页](../../../../source/711/1/Processor%2BDesign%2BRecap.pdf#page=60)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（en-US，待对照原页）

````text
Structural Hazards
• Structural hazards arise when attempting to use the same resource at
the same time.
• If we have a combined dryer/washer, then we won't be able to use the dryer
and washer simultaneously.
• If we have a unified memory that holds both data as well as instructions, then
at cycle 4 when there is data access, we won't be able to read an instruction
out.
Structural hazard occurs when a planned instruction cannot execute in the
proper clock cycle because the hardware cannot support the combination of
instructions that are set to execute in the given clock cycle.
1 3 Ot 46
NZD,'IPY
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

