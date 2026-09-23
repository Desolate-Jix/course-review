# Pipelining.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI711/source/711/1/Pipelining.pdf`
- [打开原文件](../../../../source/711/1/Pipelining.pdf)
- 原文件 SHA-256：`e6492c60dbbc27db5fa242f6a68d2a131583cabd7ab9adf1c55c7d5179a52a5a`
- 文件索引：F056；PDF 总页数：46
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=1)

### 原始文字层

````text
Pipelining
mano@cs.auckland.ac.nz
````

### 图片文字 OCR（en-US，待对照原页）

````text
Pipelining
mano@cs.auckland.ac.nz
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=2)

### 原始文字层

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
A B C D
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Pipelining
• Pipelining  provides  an efficient way of executing multiple  tasks
  concurrently
• The laundry  example
    • We have four loads of laundry to do. This consists of washing, drying, and
      folding.
        •  Washer takes 30 minutes
        •  Dryer takes 40 minutes
        •  Folding takes 20 minutes
                    A     B     C    D
````

### 图片文字 OCR（en-US，待对照原页）

````text
Pipelining
' Pipelining provides an efficient way of executing multiple tasks
concurrently
• The laundry example
• We have four loads of laundry to do. This consists of washing, drying, and
folding.
• Washer takes 30 minutes
• Dryer takes 40 minutes
• Folding takes 20 minutes
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=3)

### 原始文字层

````text
Sequential Laundry
30 40 20 30 40 20 30 40 20 30 40 20
6 PM 7 8 9 10 11 Midnight
A
B
C
D
T
a
s
k
O
r
d
e
r
Time
Sequential laundry takes 6 hours for 4 loads
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Sequential Laundry
         6 PM       7         8         9       10        11     Midnight
                                     Time
             30   40   20  30    40  20   30   40   20  30    40  20
 T
 a     A
 s
 k
O      B
 r
 d     C
 e
 r     D
Sequential laundry takes 6 hours for 4 loads
````

### 图片文字 OCR（en-US，待对照原页）

````text
Sequential Laundry
10
11 Midnight
30
7
40 20 30
Time
40 20 30
40 20 30 40 20
Sequential laundry takes 6 hours for 4 loads
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=4)

### 原始文字层

````text
Pipelined Laundry
6 PM 7 8 9 10 11 Midnight
Time
30 40 40 40 40 20
Pipelined laundry takes 3 ½ hours for 4 loads
A
B
C
D
T
a
s
k
O
r
d
e
r
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Pipelined Laundr y
         6 PM       7         8         9        10        11     Midnight
                                     Time
            30    40    40    40    40   20
T
a      A
s
k
O      B
r
d      C
e
r     D
Pipelined laundry takes 3 ½ hours for 4 loads
````

### 图片文字 OCR（en-US，待对照原页）

````text
Pipelined Laundry
30
7
40 40 40
10
Time
40 20
11
Midnight
Pipelined laundry takes 3 1/2 hours for 4 loads
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=5)

### 原始文字层

````text
ABCD
TaskOrder
6 PM
7
8
9
Time
30 40 40 40 40 20
Pipelining
Multiple tasks operating 
simultaneously
Pipelining doesn’t help latency
of single task, it helps 
throughput of entire workload
Pipeline rate limited by the 
slowest pipeline stage
Potential speedup = number 
pipe stages
Unbalanced lengths of pipe 
stages reduces speedup
Also, need time to “fill” and 
“drain” the pipeline.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Pipelining
                                                                          Multiple tasks operating
           6 PM           7            8            9                     simultaneously
                                                Time                      Pipelining doesn’t help latency
                                                                          of single task, it helps
                30     40      40      40      40    20                   throughput of entire workload
T                                                                         Pipeline rate limited by the
a        A                                                                slowest pipeline stage
s
k                                                                         Potential speedup = number
         B                                                                pipe stages
O
r                                                                         Unbalanced lengths of pipe
d       C                                                                 stages reduces speedup
e                                                                         Also, need time to “fill” and
r       D                                                                 “drain” the pipeline.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Pipelining
7
40
8
9
Time
a
d
30
B
40 40 40 20
o
o
o
o
Multiple tasks operating
simultaneously
Pipelining doesn't help latency
of single task, it helps
throughput of entire workload
Pipeline rate limited by the
slowest pipeline stage
Potential speedup = number
pipe stages
Unbalanced lengths of pipe
stages reduces speedup
Also, need time to "fill" and
"drain" the pipeline.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=6)

### 原始文字层

````text
The Load Instruction
• Fetch the instruction from the instruction memory
• Register fetch and instruction decode
• Calculate the memory address (using ALU)
• Read the data from the data memory
• Write the data back to the register file
Cycle 1 Cycle 2 Cycle 3 Cycle 4 Cycle 5
Load Ifetch Reg/Dec Exec Mem Wr
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
The Load Instruction
• Fetch the instruction   from the instruction  memory
• Register fetch  and instruction   decode
• Calculate the memory address  (using  ALU)
• Read the data from the data memory
• Write the data back to the register file
                           Cycle 1 Cycle 2 Cycle 3 Cycle 4 Cycle 5
                     Load  Ifetch  Reg/Dec  Exec    Mem     Wr
````

### 图片文字 OCR（en-US，待对照原页）

````text
The Load Instruction
' Fetch the instruction from the instruction memory
• Register fetch and instruction decode
• Calculate the memory address (using ALU)
• Read the data from the data memory
• Write the data back to the register file
Cycle 1 Cycle 2
Cycle 3 Cycle 4
Load Ifetch
Exec
Mem
: cycle 5
Wr
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=7)

### 原始文字层

````text
The Steps of the MIPS Datapath
Memory
Access
Write
Back
Instruction
Fetch
Instr. Decode
Reg. Fetch
Execute
Address Calc ALU
Instr
Memory
Reg File
MUX MUX
Data
Memory
MUX
Extend
Zero?
IF/ID
ID/EX
EX/MEM
MEM/WB
4
Adder
Next SEQ PC Next SEQ PC
RD RD RD
WB Data
Next PC Address
RS1
RS2
Imm16
MUX
Control signals 
“flow” with data 
down the pipeline
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
The Steps of the MIPS Datapath
         Instruction           Instr. Decode              Execute           Memory          Write
            Fetch               Reg. Fetch             Address Calc          Access         Back
  Next PC                      Next SEQ PC              Next SEQ PC
          4                                                    Zero?
                                 RS1
                                  RS2
  Control signals                       Extend
 “flow ” with data                Imm16
down the pipeline                        RD               RD                  RD
````

### 图片文字 OCR（en-US，待对照原页）

````text
The Steps of the MIPS Datapath
Instruction
Fetch
4
Instr. Decode
Reg. Fetch
Next SEQ PC
RSI
RS2
Extend
m16
RD
Execute
Address Calc
Next SEQ PC
Zero?
C
RD
Memory
Access
RD
Write
Back
Next PC
Control signals
"flow" with data
down the pipeline
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=8)

### 原始文字层

````text
Visualizing Pipelining ALU
IM Reg DM Reg ALU
IM Reg DM RegALU
IM Reg DM Reg ALU
IM Reg DM Reg
I
n
s
t
r.
O
r
d
e
r
Time (clock cycles)
Cycle 1 Cycle 2 Cycle 3 Cycle 4 Cycle 5 Cycle 6 Cycle 7 Multiple instructions 
are in various stages at 
the same time
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Visualizing Pipelining
                                 Time (clock cycles)
            Cycle 1   Cycle 2   Cycle 3   Cycle 4  Cycle 5    Cycle 6   Cycle 7            Multiple instructions
                                                                                          are in various stages at
I             IM                            DM         Reg                                    the same time
n                       Reg
s
t
r.                      IM        Reg                 DM        Reg
O
r                                 IM        Reg                 DM        Reg
d
e
r                                          IM                            DM         Reg
                                                     Reg
````

### 图片文字 OCR（en-US，待对照原页）

````text
Visualizing Pipelining
: 1M
Time (clock cycles)
Cycle 3 Cycle 4 Cycle 5
Cycle 1 Cycle 2
• 1M
Cycle 6
Reg •
Reg
• 1M
Reg
cycle 7
Reg :
Reg
Multiple instructions
are in various stages at
the same time
Reg
````

### 图表辅助说明

流水线时空图横轴为时钟周期、纵轴为指令顺序；每条指令经历 IM、Reg、ALU、DM、Reg 五阶段，依次错开进入，因此同一周期不同指令占据不同阶段。橙色竖条表示阶段间寄存器。

## PDF 第 9 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=9)

### 原始文字层

````text
Visualizing Pipelining ALU
IM Reg DM Reg ALU
IM Reg DM Reg
I
n
s
t
r.
O
r
d
e
r
Time (clock cycles)
Cycle 1 Cycle 2 Cycle 3 Cycle 4 Cycle 5 Cycle 6 Cycle 7
Can help with answering 
questions such as:
1. How many cycles 
does it take to 
execute this code?
2. What is the ALU 
doing during cycle 4?
3. Are two instructions 
trying to use the 
same resource at the 
same time?
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Visualizing Pipelining
                                     Time (clock cycles)                                        Can help with answering
                                                                                                      questions such as:
             Cycle 1    Cycle 2    Cycle 3    Cycle 4   Cycle 5     Cycle 6    Cycle 7          1.    How many cycles
                                                                                                      does it take to
I                                                                                                     execute this code?
n              IM         Reg                   DM          Reg                                 2.    What is the ALU
s                                                                                                     doing during cycle 4?
t                                                                                               3.    Are two instructions
r.                        IM         Reg                   DM          Reg                            trying to use the
                                                                                                      same resource at the
                                                                                                      same time?
O
r
d
e
r
````

### 图片文字 OCR（en-US，待对照原页）

````text
Visualizing Pipelining
Time (clock cycles)
Cycle 3 Cycle 4 Cycle 5
• Cycle 1 Cycle 2
1
n
S
Can help with answering
Cycle 6
Reg •
cycle 7
1.
2.
3.
• 1M
Reg
questions such as:
How many cycles
does it take to
execute this code?
What is the ALU
doing during cycle 4?
Are two instructions
trying to use the
same resource at the
same time?
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=10)

### 原始文字层

````text
Comparison of Processor Design
Clk
Cycle 1
Multiple Cycle Implementation:
Ifetch Reg Exec Mem Wr
Cycle 2 Cycle 3 Cycle 4 Cycle 5 Cycle 6 Cycle 7 Cycle 8 Cycle 9 Cycle 10
Load Ifetch Reg Exec Mem Wr
Ifetch Reg Exec Mem
Load Store
Pipeline Implementation:
Store Ifetch Reg Exec Mem Wr
Clk
Single Cycle Implementation:
Load Store Waste
Ifetch
R-type
R-type Ifetch Reg Exec Mem Wr
Cycle 1 Cycle 2
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Comparison of Processor Design
                           Cycle 1                                         Cycle 2
 Clk
 Single Cycle Implementation:
                         Load                                               Store               Waste
       Cycle 1   Cycle 2   Cycle 3   Cycle 4    Cycle 5   Cycle 6   Cycle 7   Cycle 8    Cycle 9  Cycle 10
Clk
Multiple Cycle Implementation:
       Load                                               Store                                    R-type
        Ifetch     Reg      Exec      Mem         Wr       Ifetch     Reg       Exec      Mem       Ifetch
Pipeline Implementation:
Load    Ifetch     Reg      Exec      Mem         Wr
          Store   Ifetch     Reg      Exec       Mem        Wr
                  R-type    Ifetch      Reg      Exec      Mem        Wr
````

### 图片文字 OCR（en-US，待对照原页）

````text
Comparison of Processor Design
Cycle 1
Clk
Cycle Implementation:
Load
Cycle 2 Cycle 3
Cycle 2
Store
Cycle 7 Cycle 8
Waste
Cycle 9 Cycle 10
Cycle 1
Clk
Multiile Cycle Implementation:
Load
Ifetch
Reg
Cycle 4
Mem
Mem
Exec
Reg
cycle 5
Wr
Wr
Mem
Exec
Cycle 6
Store
Ifetch
Wr
Mem
Reg
Wr
Exec
Mem
R-type
Ifetch
Pipeliäe Implementation:
Load Ifetch
Store
Reg
Ifetch
R-type
Exec
Exec
Reg
Ifetch
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=11)

### 原始文字层

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
• 10 ns/cycle x (1 CPI x 100 inst + 4 cycle “drain”) = 1040 ns
• Ideal pipelined vs. single cycle speedup
• 4500 ns / 1040 ns = 4.33
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Comparison of Processor Design
• Suppose  we have 100 instructions to execute
     •  Single cycle processor has a cycle time of 45 ns
     •  Multi cycle and pipeline processors have cycle times of 10 ns
     •  The multi cycle processor has a CPI of 3.8
• Single cycle processor
     •  45 ns/cycle  x 1 CPI x 100 inst = 4500 ns
• Multi cycle processor
     •  10 ns/cycle x 3.8 CPI x 100 inst = 3800 ns
• Ideal pipelined  machine
     •  10 ns/cycle x (1 CPI x 100 inst + 4 cycle “drain”) = 1040 ns
• Ideal pipelined  vs. single cycle speedup
     •  4500 ns / 1040 ns = 4.33
````

### 图片文字 OCR（en-US，待对照原页）

````text
Comparison of Processor Design
• Suppose we have 100 instructions to execute
• Single cycle processor has a cycle time of 45 ns
• Multi cycle and pipeline processors have cycle times of 10 ns
• The multi cycle processor has a CPI of 3.8
• Single cycle processor
• 45 ns/cycle xl CPI x 100 inst = 4500 ns
• Multi cycle processor
• 10 ns/cycle x 3.8 CPI x 100 inst = 3800 ns
• Ideal pipelined machine
• 10 ns/cycle x (1 CPI x 100 inst + 4 cycle "drain ) =
• Ideal pipelined vs. single cycle speedup
• 4500 ns/ 1040 ns = 4.33
1040 ns
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=12)

### 原始文字层

````text
Pipeline Hazards
• A hazard prohibits the execution of a planned instruction in the 
proper cycle.
• Three forms of hazards may exist in a pipeline.
• Structural hazard
• Data hazard
• Control hazard
危害
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Pipeline Hazards                危害
•A hazard prohibits   the execution of a planned  instruction  in the
 proper cycle.
•Three forms of hazards may exist in a pipeline.
   • Structural hazard
   • Data hazard
   • Control hazard
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Pipeline Hazards 扈
． A hazard prohibits the execution Of a planned instruction in the
proper cycle.
． Three forms 0f hazards may exist in a pipeline.
． StructuraI hazard
． Data hazard
． ControI hazard
````

### 图片文字 OCR（en-US，待对照原页）

````text
Pipeline Hazards
' A hazard prohibits the execution of a planned instruction in the
proper cycle.
• Three forms of hazards may exist in a pipeline.
• Structural hazard
• Data hazard
• Control hazard
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=13)

### 原始文字层

````text
Structural Hazards
• Structural hazards arise when attempting to use the same resource at 
the same time. 
• If we have a combined dryer/washer, then we won’t be able to use the dryer 
and washer simultaneously.
• If we have a unified memory that holds both data as well as instructions, then 
at cycle 4 when there is data access, we won’t be able to read an instruction 
out.
Structural hazard occurs when a planned instruction cannot execute in the 
proper clock cycle because the hardware cannot support the combination of 
instructions that are set to execute in the given clock cycle.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Structural Hazards
• Structural  hazards arise when attempting to use the same resource at
  the same time.
    • If we have a combined dryer/washer, then we won’t be able to use the dryer
      and washer simultaneously.
    • If we have a unified memory that holds both data as well as instructions, then
      at cycle 4 when there is data access, we won’t be able to read an instruction
      out.
Structural hazard occurs when a planned instruction cannot execute in the
proper clock cycle because the hardware cannot support the combination of
instructions that are set to execute in the given clock cycle.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Structural Hazards
' Structural hazards arise when attempting to use the same resource at
the same time.
• If we have a combined dryer/washer, then we won't be able to use the dryer
and washer simultaneously.
• If we have a unified memory that holds both data as well as instructions, then
at cycle 4 when there is data access, we won't be able to read an instruction
out.
Structural hazard occurs when a planned instruction cannot execute in the
proper clock cycle because the hardware cannot support the combination of
instructions that are set to execute in the given clock cycle.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=14)

### 原始文字层

````text
Structural Hazards ALU
M Reg M Reg ALU
M Reg M RegALU
M Reg M Reg ALU
M Reg M Reg
I
n
s
t
r.
O
r
d
e
r
Time (clock cycles)
Cycle 1 Cycle 2 Cycle 3 Cycle 4 Cycle 5 Cycle 6 Cycle 7
We get a structural hazard if we have a unified memory that holds both data as well as instructions.
i
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Structural Hazards
                                      Time (clock cycles)
              Cycle 1    Cycle 2    Cycle 3     Cycle 4   Cycle 5      Cycle 6    Cycle 7
 I
n               M          Reg                     M          Reg
s                                                                        i
 t
r.                         M           Reg                    M          Reg
O
 r                                     M          Reg                     M          Reg
d
e
 r                                                M                                  M          Reg
                                                             Reg
We get a structural hazard if we have a unified memory that holds both data as well as instructions.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Structural Hazards
Time (clock cycles)
• Cycle 1 Cycle 2 Cycle 3 Cycle-4 Cycl
• cycl 6 Cycle 7
Reg .
Reg
Reg :
Reg
Reg
Reg
We get a structural hazard if we have a unified memory that holds both data as well as instructions.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=15)

### 原始文字层

````text
Structural Hazards
• Solutions to structural hazards
• Use separate instruction and data memories rather than a unified one
• Have multi-port memory (i.e. allow several concurrent read/write accesses)
• Stall the pipeline and wait until the current access completes
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Structural Hazards
• Solutions  to structural  hazards
    • Use separate instruction and data memories rather than a unified one
    • Have multi-port memory (i.e. allow several concurrent read/write accesses)
    • Stall the pipeline and wait until the current access completes
````

### 图片文字 OCR（en-US，待对照原页）

````text
Structural Hazards
' Solutions to structural hazards
• Use s parate instruction and data memories rather than a unified one
memo i.e. allow several concurrent read/write accesses)
• Have multi-
• Sta the pipeline and ait ntil the current access completes
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=16)

### 原始文字层

````text
Structural Hazards ALU
IM Reg DM Reg ALU
IM Reg DM RegALU
IM Reg DM Reg ALU
IM Reg DM Reg
I
n
s
t
r.
O
r
d
e
r
Time (clock cycles)
Cycle 1 Cycle 2 Cycle 3 Cycle 4 Cycle 5 Cycle 6 Cycle 7
Using separate 
instruction and data 
memories rather than a 
unified one avoids a 
structural hazard. Datamemory
instruction memory
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Structural Hazards
                                    Time (clock cycles)                                         Using separate
                                                                                                instruction and data
             Cycle 1   Cycle 2    Cycle 3    Cycle 4   Cycle 5    Cycle 6    Cycle 7            memories  rather than a
I                                           Datamemory                                          unified one avoids a
n              IM         Reg                  DM         Reg                                   structural hazard.
s
t
r.                       IM         Reg                  DM          Reg
O
r                                   IM         Reg                  DM         Reg
d
e                                        instruction  memory
r                                              IM                              DM         Reg
                                                         Reg
````

### 图片文字 OCR（en-US，待对照原页）

````text
Structural Hazards
Time (clock cycles)
Cycle 1 Cycle 2
Cycle 3 Cycle 4
Dafo
• 1M
cycle 5
Reg
Cycle 6
Reg •
Reg
• 1M
cycle 7
Reg :
Reg
: 1M
Using separate
instruction and data
memories rather than a
unified one avoids a
structural hazard.
Reg
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=17)

### 原始文字层

````text
Structural Hazards ALU
M Reg M Reg ALU
M Reg M RegALU
M Reg M Reg ALU
M Reg M Reg
I
n
s
t
r.
O
r
d
e
r
Time (clock cycles)
Cycle 1 Cycle 2 Cycle 3 Cycle 4 Cycle 5 Cycle 6 Cycle 7
Having a multi-port 
memory (that allows 
concurrent 
reads/writes) avoids a 
structural hazard.
o
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Structural Hazards
                                    Time (clock cycles)                                          Having a multi-port
                                                                                                 memory  (that allows o
             Cycle 1   Cycle 2    Cycle 3    Cycle 4   Cycle 5    Cycle 6    Cycle 7             concurrent
                                                                                                 reads/writes)  avoids a
I                                                                                                structural hazard.
n              M          Reg                   M         Reg
s
t
r.                       M          Reg                    M         Reg
O
r                                   M          Reg                   M          Reg
d
e
r                                                                               M         Reg
                                               M         Reg
````

### 图片文字 OCR（en-US，待对照原页）

````text
Structural Hazards
Time (clock cycles)
Cycle 3 Cycle 4 Cycle 5
Cycle 1 Cycle 2
Reg
Reg
Reg
ulti-port
Having
memor
concurrent
ows
Cycle 6
Reg •
cycle 7
Reg :
reads/writes) avoids a
structural hazard.
Reg
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 18 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=18)

### 原始文字层

````text
Structural Hazards ALU
M Reg M Reg ALU
M Reg M Reg ALU
M Reg M Reg
I
n
s
t
r.
O
r
d
e
r
Time (clock cycles)
Cycle 1 Cycle 2 Cycle 3 Cycle 4 Cycle 5 Cycle 6 Cycle 7 ALU
M Reg M Reg
Stall the pipeline and 
wait till the completion 
of the current access to 
avoid a structural 
hazard.
For how many cycles 
this pipeline needs to 
stall to avoid the 
structural hazard on 
memory?
o
f
i
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Structural Hazards
                                       Time (clock cycles)
              Cycle 1    Cycle 2     Cycle 3     Cycle 4    Cycle 5     Cycle 6     Cycle 7              Stall othe pipeline and
                                                                                                         wait till the completion
I                                                                                                        of the current access to
n               M           Reg                     M           Reg                                      avoid a structural
s                                                                                                        hazard.
t
r.                          M          Reg                      M          Reg                           For how  many cycles
                                                                                                         this pipeline needs to
O                                                                                                        stall to avoid the
r                                      M           Reg                     M           Reg               structural hazard on
d                                                                                                        memory?
e                                                                f
r
                                                                                                                      i
                                                               M          Reg                      M          Reg
````

### 图片文字 OCR（en-US，待对照原页）

````text
Structural Hazards
Time (clock cycles)
Cycle 1 Cycle 2 Cycle 3 Cycle 4 Cycle 5
1
n
M
Cycle 6
M
cycle 7
Reg :
Reg
o
00
Reg
M
Stal the pipeline and
wait till the completion
of the current access to
avoid a structural
hazard.
For how many cycles
this pipeline needs to
stall to avoid the
structural hazard on
memory?
Cyc16.
Reg
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 19 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=19)

### 原始文字层

````text
Data Hazards
• Data hazards arise when attempting to use some data that isn’t yet 
ready.
Data hazard occurs when a planned instruction cannot execute in the proper clock cycle because 
the data needed to execute the instruction is not available yet.
add $s0, $t0, $t1
sub $t2, $s0, $t3
lw $s0, 20($t1)
sub $t2, $s0, $t3
0
日 - -
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
0
                                                                              -       -
Data Hazards                                                         ⽇
• Data hazards arise when attempting to use some data that isn’t yet
  ready.
              add $s0, $t0, $t1                      lw $s0, 20($t1)
              sub $t2, $s0, $t3                      sub $t2, $s0, $t3
Data hazard occurs when a planned instruction cannot execute in the proper clock cycle because
the data needed to execute the instruction is not available yet.
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Data Hazards
囗 一
． Data hazards arise when attempting tO use SO m e data that isn't yet
ready.
add $sO, $t0, $tl
sub $t2, $sO, $t3
lw $s0, 20 （ $ tl ）
sub $t2, $sO, $t3
Data hazard occurs when a planned instruction cannot execute in the proper clock cycl e because
the data needed tO execute the instruction is n Ot available yet.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Data Hazards
' Data hazards arise when attempting to use some data that isn't yet
ready.
add $s0, $t0, $tl
sub $t2, $sO, $t3
lw $so, 20($t1)
sub $t2, $sO, $t3
Data hazard occurs when a planned instruction cannot execute in the proper clock cycle because
the data needed to execute the instruction is not available yet.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 20 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=20)

### 原始文字层

````text
Data Hazards
I
n
s
t
r.
O
r
d
e
r
Time (clock cycles)
add $s1, $s2, $s3
sub $s4, $s1, $s3
and $s6, $s1, $s7
or $s8, $s1, $s9
xor $s10, $s1, $s11
ALU
IM Reg DM Reg ALU
IM Reg DM Reg ALU
IM Reg DM Reg
IM
ALU
Reg DM Reg ALU
IM Reg DM Reg
Dependencies backwards in time are hazards
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Data Hazards
         Time (clock cycles)
I    add $s1, $s2, $s3      IM    Reg           DM     Reg
n
s    sub $s4, $s1, $s3            IM     Reg          DM      Reg
t
r.  and $s6, $s1, $s7                   IM      Reg          DM      Reg
O
r   or $s8, $s1, $s9                           IM      Reg          DM      Reg
d
e                                                     IM      Reg          DM      Reg
r   xor $s10, $s1, $s11
 Dependencies backwards in time are hazards
````

### 图片文字 OCR（en-US，待对照原页）

````text
Data Hazards
Time (clock cycles)
1
n
s
d
add $sl,
sub $s4,
and $s6,
$0, $s3 1M
Reg .
1M
: 1M
Reg :
Reg
Reg .
or $s8, $sl, $s9
xor $s10, $sl, $sll
1M
Reg .
1M
Reg
Dependencies backwards in time are hazards
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 21 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=21)

### 原始文字层

````text
Data Hazards
“Forward” result from one stage to another
I
n
s
t
r.
O
r
d
e
r
Time (clock cycles)
add $s1, $s2, $s3
sub $s4, $s1, $s3
and $s6, $s1, $s7
or $s8, $s1, $s9
xor $s10, $s1, $s11
ALU
IM Reg DM Reg ALU
IM Reg DM Reg ALU
IM Reg DM Reg
IM
ALU
Reg DM Reg ALU
IM Reg DM Reg
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Data Hazards
         Time (clock cycles)
I    add $s1, $s2, $s3      IM    Reg           DM      Reg
n
s    sub $s4, $s1, $s3            IM     Reg           DM      Reg
t
r.  and $s6, $s1, $s7                    IM     Reg          DM      Reg
O
r   or $s8, $s1, $s9                            IM     Reg          DM      Reg
d
e                                                      IM     Reg          DM      Reg
r   xor $s10, $s1, $s11
“Forward” result from one stage to another
````

### 图片文字 OCR（en-US，待对照原页）

````text
Data Hazards
1
n
s
d
Time (clock cycles)
add $sl, $s2, $s3 1M
sub $s4, $sl, $s3
and $s6, $sl, $s7
or $s8, $sl, $s9
xor $s10, $sl, $sll
Reg .
1M R g
: 1M
1M
: DM Reg .
Reg
Reg
"Forward" result from one stage to another
````

### 图表辅助说明

数据冒险图中多条后续指令依赖 add 写出的 $s1。绿色箭头把结果从较早指令的执行／后续阶段直接传给使用者，展示 forwarding，而不是全部等待寄存器写回。

## PDF 第 22 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=22)

### 原始文字层

````text
Load-use Data Hazards
Time (clock cycles)
lw $s0, 20($t1)
sub $t2, $s0, $t3
ALU
IM Reg DM Reg ALU
IM Reg DM Reg
A load-use data hazard can’t be solved with forwarding alone: Must delay/stall 
instruction dependent on loads. “Delayed” load.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Load-use Data Hazards
     Time (clock cycles)
 lw $s0, 20($t1)       IM    Reg          DM    Reg
 sub $t2, $s0, $t3          IM     Reg         DM      Reg
A load-use data hazard can’t be solved with forwarding alone: Must delay/stall
instruction dependent on loads. “Delayed” load.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Load-use Data Hazards
Time (clock cycles)
lw $so, 20($t1)
sub $2, $so, $t3
Reg :
1M
Reg
A load-use data hazard can't be solved with forwarding alone: Must delay/stall
instruction dependent on loads. "Delayed" load.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 23 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=23)

### 原始文字层

````text
Load-use Data Hazards
Time (clock cycles)
sub $t2, $s0, $t3
ALU
IM Reg DM Reg
lw $s0, 20($t1)
ALU
IM Reg DM Reg
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Load-use Data Hazards
   Time (clock cycles)
lw $s0, 20($t1)     IM    Reg         DM     Reg
sub $t2, $s0, $t3              IM     Reg        DM     Reg
````

### 图片文字 OCR（en-US，待对照原页）

````text
Load-use Data Hazards
Time (clock cycles)
lw $so, 20($t1)
sub $2, $so, $t3
1M Reg .
Reg
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 24 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=24)

### 原始文字层

````text
Load-use Data Hazards
Time (clock cycles)
sub $t2, $s0, $t3
ALU
IM Reg DM Reg
lw $s0, 20($t1)
ALU
IM Reg DM Reg
xor $s3, $s1, $s2
A load-use data hazard can’t be solved with forwarding alone: Must delay/stall 
instruction dependent on loads. “Delayed” load.
此些
口 口 口 口 人 和其它指令换序
ii
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Load-use Data Hazards
   Time (clock cycles)
xor $s3, $s1, $s2
lw $s0, 20($t1)    IM   Reg        DM    Reg                          此
                                                                        些
                      ⼝      ⼝     ⼝    ⼝    ⼈                    和其它指令          换序
sub $t2, $s0, $t3            IM    Reg        DM    Reg
A load-use data hazard can’t be solved with forwarding alone: Must delay/stall
instruction dependent on loads. “Delayed” load.                       ii
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Load-use Data Hazards
Time (clock cycles)
xor $s3, $sl, $s2
lw ， 20 （ $ tl ）
s ub $t2, ， $t3
IQ 刁 ）
IM Re g
0 亠 0 厂
： IM R g
． DM ： Reg
A load-use data hazard can't be solved with forwarding alone: Must elay sta II
instruction dependent 0 n loads. "Delayed" load.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Load-use Data Hazards
Time (clock cycles)
xor $s3, $sl, $s2
lw $so, 20($t1)
sub $2, $so, $t3
teurder
1M Reg .
; DM Reg
A load-use data hazard can't be solved with forwarding alone: Must elay stall
instruction dependent on loads. "Delayed" load.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 25 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=25)

### 原始文字层

````text
Load-use Data Hazards
Time (clock cycles)
sub $t2, $s0, $t3
ALU
IM Reg DM Reg
lw $s0, 20($t1)
ALU
IM Reg DM Reg
xor $s3, $s1, $s2
ALU
IM Reg DM Reg
A load-use data hazard can’t be solved with forwarding alone: Must delay/stall 
instruction dependent on loads. “Delayed” load.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Load-use Data Hazards
    Time (clock cycles)
lw $s0, 20($t1)       IM    Reg          DM     Reg
xor $s3, $s1, $s2          IM     Reg          DM      Reg
sub $t2, $s0, $t3                 IM     Reg         DM      Reg
A load-use data hazard can’t be solved with forwarding alone: Must delay/stall
                  instruction dependent on loads. “Delayed” load.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Load-use Data Hazards
Time (clock cycles)
lw $so, 20($t1)
xor $s3, $sl, $s2
sub $2, $so, $t3
Reg
Reg
- 1M
Reg :
Reg
A load-use data hazard can't be solved with forwarding alone: Must delay/stall
instruction dependent on loads. "Delayed" load.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 26 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=26)

### 原始文字层

````text
Read-After-Write Data Hazard
• Called a “dependence” in compiler terms. This hazard results from an 
actual need for communication.
• Error if instruction j tries to read operand before instruction i writes it.
i: add $s0, $t0, $t1
j: sub $t2, $s0, $t3
Read-After-Write hazards can be avoided by forwarding.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Read-After-Write Data Hazard
•Called a “dependence”  in compiler terms.  This hazard results  from an
 actual need for communication.
•Error if instruction j tries to read operand before instruction i writes it.
                               i: add $s0, $t0, $t1
                               j: sub $t2, $s0, $t3
               Read-After-Write hazards can be avoided by forwarding.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Read-After-Write Data Hazard
' Called a "dependence" in compiler terms. This hazard results from an
actual need for communication.
• Error if instruction j tries to read operand before instruction i writes it.
i: add $s0, $t0, $tl
j: sub $t2, $s0, $t3
Read-After-Write hazards can be avoided by forwarding.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 27 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=27)

### 原始文字层

````text
Read-After-Write Data Hazard
RAW hazard can be avoided by forwarding. 
Time (clock cycles)
add $s0, $t0, $t1
sub $t2, $s0, $t3
ALU
IM Reg DM Reg ALU
IM Reg DM Reg
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Read-After-Write Data Hazard
   Time (clock cycles)
add $s0, $t0, $t1  IM    Reg         DM     Reg
sub $t2, $s0, $t3        IM    Reg         DM     Reg
RAW hazard can be avoided by forwarding.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Read-After-Write Data Hazard
Time (clock cycles)
add $so, $to, $tl 1M : Reg
sub $2, $so, $t3
1M Reg
• DM Reg
RAW hazard can be avoided by forwarding.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 28 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=28)

### 原始文字层

````text
Write-After-Read Data Hazard
• Called an “anti-dependence” in compiler terms. This results from the 
reuse of the registers (e.g. s0).
• Error if instruction j tries to write operand before instruction i reads it.
i: sub $t2, $s0, $t3
j: add $s0, $t0, $t1
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Write-After-Read Data Hazard
•Called an “anti-dependence”  in compiler terms. This results  from the
 reuse of the registers (e. g. s0).
•Error if instruction j tries to write operand before instruction i reads it.
                               i: sub $t2, $s0, $t3
                               j: add $s0, $t0, $t1
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write-After-Read Data Hazard
' Called an "anti-dependence" in compiler terms. This results from the
reuse of the registers (e.g. so).
• Error if instruction j tries to write operand before instruction i reads it.
i: sub $t2, $sO, $t3
j: add $sO, $tO, $tl
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 29 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=29)

### 原始文字层

````text
Write-After-Read Data Hazard
• Cannot happen in MIPS 5 stage pipeline because:
• All instructions take 5 stages, 
• Reads are always in stage 2, and 
• Writes are always in stage 5
i: sub $t2, $s0, $t3
j: add $s0, $t0, $t1
o
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Write-After-Read Data Hazard
• Cannot happen  in MIPS 5 stage pipeline because:
    • All instructions take 5 stages,
   o
    • Reads are always in stage 2, and
    • Writes are always in stage 5
                               i: sub $t2, $s0, $t3
                               j: add $s0, $t0, $t1
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write-After-Read Data Hazard
Canno happen in MIPS 5 stage pipeline because:
Instructions take 5 stages,
• Reads are always in stage 2, and
• Writes are always in stage 5
i: sub $t2, $sO, $t3
j: add $sO, $tO, $tl
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 30 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=30)

### 原始文字层

````text
Write-After-Read Data Hazard
WAR hazard cannot happen in the MIPS 5-stage pipeline. 
Time (clock cycles)
sub $t2, $s0, $t3
add $s0, $t0, $t1
ALU
IM Reg DM Reg ALU
IM Reg DM Reg
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Write-After-Read Data Hazard
     Time (clock cycles)
 sub $t2, $s0, $t3   IM    Reg         DM     Reg
 add $s0, $t0, $t1         IM    Reg         DM     Reg
WAR hazard cannot happen in the MIPS 5-stage pipeline.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write-After-Read Data Hazard
Time (clock cycles)
sub $2, $so, $t3 1M Reg •
add $so, $to, $tl
1M Reg
•DM Reg
WAR hazard cannot happen in the MIPS 5-stage pipeline.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 31 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=31)

### 原始文字层

````text
Write-After-Write Data Hazard
• Called an “output dependence” in compiler terms. This too results 
from the reuse of the registers (e.g. s0).
• Error if instruction j tries to write operand before instruction i writes 
it.
i: sub $s0, $t2, $t3
j: add $s0, $t0, $t1
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Write-After-Write Data Hazard
•Called an “output  dependence”  in compiler terms. This too results
 from the reuse of the registers (e.g. s0).
•Error if instruction j tries to write operand before instruction i writes
 it.
                               i: sub $s0, $t2, $t3
                               j: add $s0, $t0, $t1
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write-After-Write Data Hazard
' Called an "output dependence" in compiler terms. This too results
from the reuse of the registers (e.g. so).
• Error if instruction j tries to write operand before instruction i writes
it.
i: sub $sO, $t2, $t3
j: add $sO, $tO, $tl
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 32 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=32)

### 原始文字层

````text
Write-After-Write Data Hazard
• Cannot happen in MIPS 5 stage pipeline because:
• All instructions take 5 stages, and
• Writes are always in stage 5
i: sub $s0, $t2, $t3
j: add $s0, $t0, $t1
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Write-After-Write Data Hazard
•Cannot happen  in MIPS 5 stage pipeline because:
   • All instructions take 5 stages, and
   • Writes are always in stage 5
                               i: sub $s0, $t2, $t3
                               j: add $s0, $t0, $t1
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write-After-Write Data Hazard
' Cannot happen in MIPS 5 stage pipeline because:
• All instructions take 5 stages, and
• Writes are always in stage 5
i: sub $sO, $t2, $t3
j: add $sO, $tO, $tl
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 33 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=33)

### 原始文字层

````text
Write-After-Write Data Hazard
WAW hazard cannot happen in the MIPS 5-stage pipeline. 
Time (clock cycles)
sub $s0, $t2, $t3
add $s0, $t0, $t1
ALU
IM Reg DM Reg ALU
IM Reg DM Reg
line we
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Write-After-Write Data Hazard
   Time (clock cycles)
sub $s0, $t2, $t3  IM    Reg         DM     Reg
add $s0, $t0, $t1        IM    Reg         DM     Reg
WAW hazard cannot happen in the MIPS 5we      -stage pipeline.
                 line
````

### 图片文字 OCR（en-US，待对照原页）

````text
Write-After-Write Data Hazard
Time (clock cycles)
sub $so, $2, $t3 1M
WAW hazard cannot happen in the MIPS 5-stage pipeline.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 34 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=34)

### 原始文字层

````text
Control Hazards
• Control hazards arise when attempting to make a decision before the 
condition is evaluated.
• Also called a branch hazard
Control hazard occurs when a planned instruction cannot execute in the proper clock cycle because 
the instruction that is fetched is not the one that is needed; that is, the flow of instruction 
addresses is not what the pipeline expected.
add $s0, $t0, $t1
beq $t2, $t3, Label
or $s3, $s4, $s5
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Control Hazards
• Control hazards arise when attempting to make a decision before the
  condition  is evaluated.
    •  Also called a branch hazard
                                    add $s0, $t0, $t1
                                    beq $t2, $t3, Label
                                    or $s3, $s4, $s5
Control hazard occurs when a planned instruction cannot execute in the proper clock cycle because
the instruction that is fetched is not the one that is needed; that is, the flow of instruction
addresses is not what the pipeline expected.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Control Hazards
' Control hazards arise when attempting to make a decision before the
condition is evaluated.
• Also called a branch hazard
add $s0, $t0, $tl
beq $t2, $t3, Label
or $s3, $s4, $s5
Control hazard occurs when a planned instruction cannot execute in the proper clock cycle because
the instruction that is fetched is not the one that is needed; that is, the flow of instruction
addresses is not what the pipeline expected.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 35 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=35)

### 原始文字层

````text
Control Hazards
12: beq $s1, $s3, 36
16: and $s2, $s3, $s5 
20: or $s6, $s1, $s7
24: add $s8, $s1, $s9
36: xor $s10,$s1, $s11 
Reg
ALU
IM DM Reg
Reg
ALU
IM DM Reg
Reg
ALU
IM DM Reg
Reg
ALU
IM DM Reg
Reg
ALU
IM DM Reg
I calculate condition
a where
you
go.­l­t
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Control Hazards
12: beq $s1, $s3, 36       IM    Reg          DM    Reg
     I                                                              calculate            condition
16: and $s2, $s3, $s5            IM     Reg         DM    Reg
    a
20: or  $s6, $s1, $s7                   IM    Reg         DM     Reg         where
                                                                                         yo  u
24: add $s8, $s1, $s9                         IM    Reg          DM    Reg
                                          go.lt
36: xor $s10,$s1, $s11                              IM     Reg         DM    Reg
````

### 图片文字 OCR（en-US，待对照原页）

````text
Control Hazards
12: beq $sl, $0, 36
16: and $0, $0, $s5
20: or $s6, $sl, $s7
24: add $s8, $sl, $s9
36: xor $s10,$s1,
$sll
uun(otte
Uåere
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 36 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=36)

### 原始文字层

````text
Control Hazards
• Solutions to control hazards
• Stall until the decision is clear
• Determine sooner if branch is taken or not and the taken branch address
• MIPS R10K solution
• Move Zero test to ID/RF stage
• Adder to calculate new PC in ID/RF stage
in the tint stage
other hardware calculate
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Control Hazards
• Solutions  to control hazards
    • Stall until the decision is clear
    • Determine sooner if branch is taken or not and the taken branch address
    • MIPS R10K solution
        • Move Zero test to ID/RF stage       in     the     tint
        • Adder to calculate new PC in ID/RF stage                   stage
                    other         hardware        calculate
````

### 图片文字 OCR（en-US，待对照原页）

````text
Control Hazards
' Solutions to control hazards
• Stall until the decision is clear
• Determine sooner if branch is taken or not and the taken branch address
MIPS RIOK solution
fle
• Move Zero test to ID/RF stage
• Adder to calculate new PC in ID/RF stage
other calculate.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 37 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=37)

### 原始文字层

````text
Control Hazards
Time (clock cycles)
beq $t2, $t3, Label
ALU
IM Reg DM Reg
ALU
IM Reg DM Reg
Label: …
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Control Hazards
   Time (clock cycles)
beq $t2, $t3, Label IM    Reg          DM     Reg
 Label: …                             IM     Reg         DM     Reg
````

### 图片文字 OCR（en-US，待对照原页）

````text
Control Hazards
Time (clock cycles)
beq $2, $0, Label 1M
Label• ...
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 38 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=38)

### 原始文字层

````text
Control Hazards
If the zero test and branch target calculations are done in ID/RF stage, then we have 
a single bubble.
Time (clock cycles)
beq $t2, $t3, Label
ALU
IM Reg DM Reg ALU
IM Reg DM Reg
Label: …
o
calculate
Lerner
wenn
f
Manch
an calculate
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Control Hazards
   Time (clock cycles)
beq $t2, $t3, Label IM     Reg         DM     Reg
 Label: …                        IM     Reg         DM     Reg
                           o
                       calculate
If the zero test and branch target calculations are done in ID/RF stage, then we have
a single bubble.Le  r  n  e  r                                      we n n
                                  Manch                        an      calculate
                             f
````

### 图片文字 OCR（en-US，待对照原页）

````text
Control Hazards
Time (clock cycles)
beq $2, $0, Label 1M
QGQO
Label•
st and branch target calculations are done in ID/RF stage, then we have
Ifthe er
a single bubb
Dranc h
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 39 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=39)

### 原始文字层

````text
Control Hazards
• Solutions to control hazards
• Predict the branch and roll back if the prediction is incorrect
• Rolling back involves making the predicted instruction a NOP: ensure no 
results of execution is committed (e.g. de-assert MemWrite and RegWrite for 
non-branches).
T non branch
911 akn he
not cost extra
time
o
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
T            branch              911       akn    he
                                 non                                   not
Control Hazards                                                                cost     ex t ra
                                                                                          time
• Solutions  to control hazards
    • Predict the branch and roll back if the prediction is incorrecto
    • Rolling back involves making the predicted instruction a NOP: ensure no
      results of execution is committed (e.g. de-assert MemWrite and RegWrite for
      non-branches).
````

### 图片文字 OCR（en-US，待对照原页）

````text
n0h
Control Hazards
' Solutions to control haz
s
branch
not
extra
• Predict the branch an roll back i the prediction is incorrect
• Rolling back involves making the predicted instruction a NOP: ensure no
results of execution is committed (e.g. de-assert MemWrite and RegWrite for
non-branches).
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 40 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=40)

### 原始文字层

````text
Control Hazards
• Solutions to control hazards
• Redefine the branch behaviour: declare that the branch takes place after 
executing the instruction following the branch. 
• Called “delayed branch”
add $s0, $t0, $t1
beq $t2, $t3, Label
or $s3, $s4, $s5 hoods hanged
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Control Hazards
•Solutions  to control hazards
   • Redefine the branch behaviour: declare that the branch takes place after
     executing the instruction following the branch.
       • Called “delayed branch”
                              add $s0, $t0, $t1
                              beq $t2, $t3, Label              hanged
                              or $s3, $s4, $s5
                            hoods
````

### 图片文字 OCR（en-US，待对照原页）

````text
Control Hazards
' Solutions to control hazards
• Redefine the branch behaviour: declare that the branch takes place after
executing the instruction following the branch.
• Called "delayed branch"
add $s0, $t0, $tl
beq t2, $t3, Label
or $s3, s4, s5
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 41 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=41)

### 原始文字层

````text
Control Hazards
Do the OR instruction where the bubble is!
Time (clock cycles)
beq $t2, $t3, Label
ALU
IM Reg DM Reg ALU
IM Reg DM Reg
Label: …
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Control Hazards
    Time (clock cycles)
beq $t2, $t3, Label  IM    Reg          DM     Reg
 Label: …                         IM    Reg          DM     Reg
Do the OR instruction where the bubble is!
````

### 图片文字 OCR（en-US，待对照原页）

````text
Control Hazards
Time (clock cycles)
beq $2, $0, Label 1M
QGQO
Label•
Do the OR instruction where the bubble is!
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 42 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=42)

### 原始文字层

````text
Control Hazards
Time (clock cycles)
beq $t2, $t3, Label
ALU
IM Reg DM Reg ALU
IM Reg DM Reg
Label: …
or $s3, $s4, $s5
ALU
IM Reg DM Reg
Do the OR instruction where the bubble is!
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Control Hazards
    Time (clock cycles)
beq $t2, $t3, Label  IM     Reg          DM     Reg
 or $s3, $s4, $s5          IM     Reg          DM      Reg
 Label: …                         IM     Reg          DM      Reg
Do the OR instruction where the bubble is!
````

### 图片文字 OCR（en-US，待对照原页）

````text
Control Hazards
Time (clock cycles)
beq $2, $0, Label 1M
or $0, $s4, $s5
Label•
Reg .
Reg :
1M
Reg
Reg
Reg
Do the OR instruction where the bubble is!
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 43 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=43)

### 原始文字层

````text
Pipeline Hazards
• Avoid some “by design”
• Eliminate WAR by always fetching operands early (during operand fetch stage) 
in pipe
• Eliminate WAW by doing all write-backs in order (e.g. always in the last stage)
• Detect and resolve remaining ones
• Stall or forward (if possible)
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Pipeline Hazards
• Avoid some “by design”
    • Eliminate WAR by always fetching operands early (during operand fetch stage)
      in pipe
    • Eliminate WAW by doing all write-backs in order (e.g. always in the last stage)
• Detect and resolve remaining ones
    • Stall or forward (if possible)
````

### 图片文字 OCR（en-US，待对照原页）

````text
Pipeline Hazards
' Avoid some "by design"
• Eliminate WAR by always fetching operands early (during operand fetch stage)
in pipe
• Eliminate WAW by doing all write-backs in order (e.g. always in the last stage)
• Detect and resolve remaining ones
• Stall or forward (if possible)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 44 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=44)

### 原始文字层

````text
Hazard Detection
• Suppose instruction i is about to be issued and a predecessor instruction j is in the 
instruction pipeline.
• A RAW hazard exists on register r if r  Rr
(i)  Rw(j)
• A WAR hazard exists on register r if r  Rw(i)  Rr
(j)
• A WAW hazard exists on register r if r  Rw(i)  Rw(j)
Rr(i)/Rw(i): Set of registers read/written by instruction i.
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Hazard Detection
• Suppose instruction i is about to be issued and a predecessor instruction j is in the
instruction pipeline.
• A RAW hazard exists on register r if r e Rr(i) n Rw(j)
• A WAR hazard exists on register r if r e Rw(i) n Rr(j)
• A WAW hazard exists on register r if r e Rw(i) n Rw(j)
Rr(i)/Rw(i): Set of registers read/written by instruction i.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 45 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=45)

### 原始文字层

````text
Further Work
• Read Chapter 4 of the book: Computer Organization and Design – The 
Hardware Software Interface RISC-V edition, 2nd edition (2020)
• See what changes are necessary to the datapath to support forwarding.
• Also read Appendix C (Mapping control to hardware).
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Further Work
•Read Chapter 4 of the book: Computer Organization and Design – The
 Hardware Software Interface RISC-V edition, 2nd edition  (2020)
   • See what changes are necessary to the datapath to support forwarding.
   • Also read Appendix C (Mapping control to hardware).
````

### 图片文字 OCR（en-US，待对照原页）

````text
Further Work
' Read Chapter 4 of the book: Computer Organization and Design
- The
Hardware Software Interface RISC-V edition, 2nd edition (2020)
• See what changes are necessary to the datapath to support forwarding.
• Also read Appendix C (Mapping control to hardware).
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 46 页

[查看此页](../../../../source/711/1/Pipelining.pdf#page=46)

### 原始文字层

````text
¿?
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

> OCR 未识别出可靠文字；本页可能以图形、手写公式或空白为主。

### 图表辅助说明

本页中央仅有“¿?”提问／结束标记，没有课件正文。

