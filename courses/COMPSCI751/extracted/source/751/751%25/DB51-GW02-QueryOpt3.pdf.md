# DB51-GW02-QueryOpt3.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI751/source/751/751%25/DB51-GW02-QueryOpt3.pdf`
- [打开原文件](../../../../source/751/751%2525/DB51-GW02-QueryOpt3.pdf)
- 原文件 SHA-256：`249952615f0d6a23578c87f70015a06950fd07991ed290d11b2c2b84a67785ff`
- 文件索引：F112；PDF 总页数：16
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../source/751/751%2525/DB51-GW02-QueryOpt3.pdf#page=1)

### 原始文字层

````text
2019 Gerald Weber's Slides 1
Databases 51
SPARQL Query optimization
• Comparing costs of Plans
• Cost of filters
• Join Order Optimization
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Databas es  51

SP ARQL Query optimization

•  Comparing costs of Plans

•  Cost of filters

•  Join Order Optimization

20   19                                Geral d Weber's Sl ides                             1
````

### 图片文字 OCR（en-US，待对照原页）

````text
Databases 51
SPARQL Query optimization
Comparing costs of Plans
Cost of filters
Join Order Optimization
2019
Gerald Weber's Slides
1
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../source/751/751%2525/DB51-GW02-QueryOpt3.pdf#page=2)

### 原始文字层

````text
SE 351 2
Query evaluation: single triple patterns
• Evaluation of single triple pattern is a primitive offered by a triplestore :
• SELECT * WHERE {C45678 ?predicate ?object }
• Possible 8 abstract triple patterns:
• ?subject ?predicate ?object XYZ
C45678 ?predicate ?object SYZ
?subject ?predicate SOFTENG XYO
?subject programme ?object XPZ
?subject programme SOFTENG XPO
C45678 programme ?object SPZ
C45678 ?predicate SOFTENG SYO
C45678 programme SOFTENG SPO
• Optimal query cost for single triple pattern: linear in size of result set
• Is achievable with enough index support! (but not always done)
Most 
specific
Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Query evaluati on: si ngle tripl e patterns

•  Evaluation of  single  triple pattern is  a primitive  of fered  by a t riples tore  :

•  SELECT * WHERE {C45678  ?predicate  ?object }

•  Possible 8 abstract  triple patt erns :

•  ?subject ?predicate  ?object     XYZ

   C45678   ?predicate  ?object     SYZ

   ?subject ?predicate  SOFTENG     XYO

   ?subject  programme  ?object     XPZ

   ?subject  programme  SOFTENG     XPO

                                                                        Most

   C45678    programme   ?object    SPZ

                                                                        specif ic

   C45678   ?predicate   SOFTENG    SYO

   C45678    programme   SOFTENG    SPO

•  Optimal query c os t f or  single triple pattern:  linear in s ize of  res ult s et

•  Is  achievable wit h enough index s upport!  (but  not alw ay s done)

SE 351                              Geral d Weber's Sl ides                          2
````

### 图片文字 OCR（en-US，待对照原页）

````text
Query evaluation: single triple patterns
• Evaluation of single triple pattern is a primitive offered by a triplestore :
• SELECT * WHERE {C45678 ?predicate ?object }
• Possible 8 abstract triple patterns:
? subject
C45678
•subject
•subject
•subject
C45678
C45678
C45678
•predicate
•predicate
•predicate
progranune
prograrmne
progran•une
•predicate
programne
•object
•object
SOFTENG
•object
SOFTENG
•object
SOFTENG
SOFTENG
XYZ
SYZ
X YO
XPZ
XPO
Most
SPZ
specific
SYO
SPO
Optimal query cost for single triple pattern: linear in size of result set
Is achievable with enough index support! (but not always done)
SE 351
Gerald Weber's Slides
2
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../source/751/751%2525/DB51-GW02-QueryOpt3.pdf#page=3)

### 原始文字层

````text
SE 351 3
Cost with larger basic graph pattern.
• avg 2.2 (?lecturer teaches ?course) avg 4.2
• 1 (?lecturer assesses ?course) avg 1.9
• 40 (?course programme SOFTENG)
• 60 (?course programme GENED)
• SELECT * {
?course2 programme GENED
?lecturer teaches ?course2 . 
?lecturer assesses ?course1 . 
?course1 programme SOFTENG . 
}
Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Cost wi th l ar ger bas ic graph pattern.

•  avg 2.2 ( ?l  ecturer teaches ?course) avg 4.2

•  1 (?lecturer assesses ?course) avg 1.9

•  40 (?course programme SOFT ENG)

•  60 (?course programme GENED  )

•  SELECT * {

   ?course2 programme GENED

   ?lecturer teaches ?course2 .

   ?lecturer assesses ?course1 .

   ?course1 programme SOFTENG .

   }

SE 351                          Geral d Weber's Sl ides                     3
````

### 图片文字 OCR（en-US，待对照原页）

````text
Cost with larger basic graph pattern.
avg 2.2 (?lecturer teaches ?course) avg 4.2
1 (?lecturer assesses ?course) avg 1.9
40 (?course programme SOFTENG)
60 (?course programme GENED)
• SELECT * {
?course2 progranune GENED
? lecturer teaches ?course2
? lecturer assesses ?coursel
?coursel program:ne SOFTENG
SE 351
Gerald Weber's Slides
3
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../source/751/751%2525/DB51-GW02-QueryOpt3.pdf#page=4)

### 原始文字层

````text
SE 351 4
Cost with larger basic graph pattern.
• avg 2.2 (?lecturer teaches ?course) avg 4.2
• 1 (?lecturer assesses ?course) avg 1.9
• 40 (?course programme SOFTENG)
• 60 (?course programme GENED)
• SELECT * {
?course2 programme GENED 60 = 60 
?lecturer teaches ?course2 . *2.2 = 132
?lecturer assesses ?course1 . *1.9 < 255
?course1 programme SOFTENG . *1 < 255
} _____ 
Abstract Triple Pattern SPO < 702
Gerald Weber's Slides
Conservative est.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Cost wi th l ar ger bas ic graph pattern.

•  avg 2.2 ( ?l  ecturer teaches ?course) avg 4.2

•  1 (?lecturer assesses ?course) avg 1.9

•  40 (?course programme SOFT ENG)

•  60 (?course programme GENED  )

•  SELECT * {

   ?course2 programme GENED       60               = 60

   ?lecturer teaches ?course2 .      *2.2          = 132

   ?lecturer assesses ?course1 .         *1.9      < 255

   ?course1 programme SOFTENG .                               *1  < 255

   }                                              _____

    Abstr act T ri  pl  e P  attern S  PO                            < 702

                                         Co nse rva tiv e e st.

SE 351                          Geral d Weber's Sl ides                    4
````

### 图片文字 OCR（en-US，待对照原页）

````text
Cost with larger basic graph pattern.
avg 2.2 (?lecturer teaches ?course) avg 4.2
1 (?lecturer assesses ?course) avg 1.9
40 (?course programme SOFTENG)
60 (?course programme GENED)
*2.2
• SELECT * {
?course2 progranune GENED
? lecturer teaches ?course2
? lecturer assesses ?coursel
?coursel programme SOFTENG
Abstract Triple Pattern SPO
60
*1
SE 351
Conserva tive
Gerald Weber's Slides
= 60
= 132
< 255
< 255
< 702
4
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../../source/751/751%2525/DB51-GW02-QueryOpt3.pdf#page=5)

### 原始文字层

````text
SE 351 5
Cost after changing order
• avg 2.2 (?lecturer teaches ?course) avg 4.2
• 1 (?lecturer assesses ?course) avg 1.9
• 40 (?course programme SOFTENG)
• 60 (?course programme GENED)
• SELECT * {
?course1 programme SOFTENG . 40 = 40
?lecturer assesses ?course1 . *1 = 40
?lecturer teaches ?course2 . *4.2 = 168
?course2 programme GENED *1 = 168
} 416
 
Abstract Triple Pattern SPO
Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Cost after changing order

• avg 2.2 ( ?l  ecturer teaches ?course) avg 4.2

• 1 (?lecturer assesses ?course) avg 1.9

• 40 (?course programme SOFT ENG)

• 60 (?course programme GENED  )

• SELECT * {

  ?course1 programme SOFTENG .    40              = 40

  ?lecturer assesses ?course1 .       *1          = 40

  ?lecturer teaches ?course2 .           *4.2     = 168

  ?course2 programme GENED                    *1  = 168

  }                                                                 416

  Abstract T ri  pl  e P  attern S  PO

SE 351                          Geral d Weber's Sl ides                    5
````

### 图片文字 OCR（en-US，待对照原页）

````text
• SELECT * {
?coursel progranune SOFTENG
? lecturer assesses ?coursel
? lecturer teaches ?course2
?course2 programme GENED
Abstract Triple Pattern SPO
Cost after changing order
avg 2.2 (?lecturer teaches ?course) avg 4.2
1 (?lecturer assesses ?course) avg 1.9
40 (?course programme SOFTENG)
60 (?course programme GENED)
*4.2
40
SE 351
Gerald Weber's Slides
= 168
= 168
416
5
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../source/751/751%2525/DB51-GW02-QueryOpt3.pdf#page=6)

### 原始文字层

````text
SE 351 6
To rule an option out we need lower bound
• avg 2.2 (?lecturer teaches ?course) avg 4.2
• 1 (?lecturer assesses ?course) avg 1.9
• 40 (?course programme SOFTENG)
• 60 (?course programme GENED)
• SELECT * {
?course2 programme GENED 60 = 60 
?lecturer teaches ?course2 . *2.2 = 132
?lecturer assesses ?course1 . *1.9 > 240
?course1 programme SOFTENG . *1 > 240
} _____ 
> 650
Gerald Weber's Slides
Lower bound
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
To rul e an option out we need l ower bound

• avg 2.2 ( ?l  ecturer teaches ?course) avg 4.2

• 1 (?lecturer assesses ?course) avg 1.9

• 40 (?course programme SOFT ENG)

• 60 (?course programme GENED  )

• SELECT * {

  ?course2 programme GENED       60               = 60

  ?lecturer teaches ?course2 .      *2.2          = 132

  ?lecturer assesses ?course1 .         *1.9      > 240

  ?course1 programme SOFTENG .                              *1 > 240

  }                                              _____

                                                                   > 650

                                        Lo wer  bo und

SE 351                         Geral d Weber's Sl ides                   6
````

### 图片文字 OCR（en-US，待对照原页）

````text
To rule an option out we need lower bound
avg 2.2 (?lecturer teaches ?course) avg 4.2
1 (?lecturer assesses ?course) avg 1.9
40 (?course programme SOFTENG)
60 (?course programme GENED)
*2.2
• SELECT * {
?course2 progranune GENED
? lecturer teaches ?course2
? lecturer assesses ?coursel
?coursel programme SOFTENG
60
= 60
= 132
240
240
SE 351
Lower
Gerald Weber's Slides
bound
650
6
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../../source/751/751%2525/DB51-GW02-QueryOpt3.pdf#page=7)

### 原始文字层

````text
SE 351 7
Cost estimation with filters
• avg 2.2 (?lecturer teaches ?course) avg 4.2
• 1 (?lecturer assesses ?course) avg 1.9
• 40 (?course programme SOFTENG)
• 60 (?course programme GENED)
• Courses with courseNumber 700 or higher: 20 percent
• PREFIX uni: <http:\\www.auckland.ac.nz\all\>
SELECT * {
?course1 uni:programme uni:SOFTENG . 40 = 40
?lecturer uni:assesses ?course1 . *1 = 40
?lecturer uni:teaches ?course2 . *4.2 = 168
?course2 uni:programme uni:GENED *1 = 168
?course1 uni:cnr ?coursenr . *1 = 168
FILTER (?coursenr >= 700) *1 = 168
} 752 
Gerald Weber's Slides
Can we do 
better?
Cost 
metric for 
filter
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Cost es ti mation wi th fi lters

•  avg 2. 2  (?lec turer  teaches ?course) avg  4. 2

•  1 (?lecturer ass es ses  ?c ours e)  av g 1.9                Cost

•  40 (?course programme  SOFT ENG)                             m etr ic f or

                                                                filter

•  60 (?course programme  GENED )

•  Courses  with  cours eNumber  700  or  higher: 20 percent

•  PREFIX uni: <http:\\www.auckland.ac.nz\all\>

   SELECT * {

   ?course1 uni:programme uni:SOFTENG .  40     = 40

   ?lecturer uni:assesses ?course1 .     *1     = 40

   ?lecturer uni:teaches ?course2 .      *4.2  = 168

   ?course2 uni:programme uni:GENED       *1   = 168

   ?course1 uni:cnr  ?coursenr . Can w e do               *1   = 168

   FILTER  (?coursenr >= 700)             *1   =better?              168

   }                                                             752

SE 351                            Geral d Weber's Sl ides                      7
````

### 图片文字 OCR（en-US，待对照原页）

````text
Cost estimation with filters
avg 2.2 (?lecturer teaches ?course) avg 4.2
1 (?lecturer assesses ?course) avg 1.9
40 (?course programme SOFT ENG)
60 (?course programme GENED)
Cost
metric for
filter
Courses with courseNumber 700 or higher: 20 percent
www . auckland. ac . nz \a11 \ >
http : \\
• PREFIX uni: <
SELECT * {
?coursel uni : prograrmne uni : SOFTENG
? lecturer uni : assesses ?coursel
? lecturer uni : teaches ?course2
?course2 uni : progranune uni : GENED
Can we do
?coursel uni : cnr ?coursenr
better?
FILTER (?coursenr >= 700)
40
SE 351
Gerald Weber's Slides
= 40
= 40
= 168
= 168
= 168
= 168
752
7
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../../source/751/751%2525/DB51-GW02-QueryOpt3.pdf#page=8)

### 原始文字层

````text
SE 351 8
Cost estimation with filters
• avg 2.2 (?lecturer teaches ?course) avg 4.2
• 1 (?lecturer assesses ?course) avg 1.9
• 40 (?course programme SOFTENG)
• 60 (?course programme GENED)
• Courses with courseNumber 700 or higher: 20 percent
• SELECT * {
?course1 uni:programme SOFTENG . 40 = 40
?lecturer uni:assesses ?course1 . *1 = 40
?course1 uni:cnr ?coursenr . *1 = 40
FILTER (?coursenr >= 700) *1 = 40 
?lecturer uni:teaches ?course2 . *0.2 *4.2 ~ 34
?course2 uni:programme uni:GENED *1 ~ 34
} ~ 228 
 Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Cost es ti mation wi th fi lters

•  avg 2. 2  (?lec turer  teaches ?course) avg  4. 2

•  1 (?lecturer ass es ses  ?c ours e)  av g 1.9

•  40 (?course programme  SOFT ENG)

•  60 (?course programme  GENED )

•  Courses  with  cours eNumber  700  or  higher: 20 percent

•  SELECT * {

   ?course1 uni:programme SOFTENG .        40    = 40

   ?lecturer uni:assesses ?course1 .       *1    = 40

   ?course1 uni:cnr  ?coursenr .           *1    = 40

   FILTER  (?coursenr >= 700)              *1    = 40

   ?lecturer uni:teaches ?course2 . *0.2                   *4.2   ~ 34

   ?course2 uni:programme uni:GENED          *1  ~ 34

   }                                                                 ~ 228

SE 351                           Geral d Weber's Sl ides                       8
````

### 图片文字 OCR（en-US，待对照原页）

````text
Cost estimation with filters
avg 2.2 (?lecturer teaches ?course) avg 4.2
1 (?lecturer assesses ?course) avg 1.9
40 (?course programme SOFT ENG)
60 (?course programme GENED)
Courses with courseNumber 700 or higher: 20 percent
• SELECT * {
?coursel uni : progran•une SOFTENG
? lecturer uni : assesses ?coursel
?coursel uni : cnr ?coursenr
FILTER (?coursenr >= 700)
? lecturer uni : teaches ?course2
*0.2
?course2 uni : programme uni : GENED
SE 351
Gerald Weber's Slides
= 40
34
34
228
8
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../../source/751/751%2525/DB51-GW02-QueryOpt3.pdf#page=9)

### 原始文字层

````text
SE 351 9
Cost estimation with filters
• avg 2.2 (?lecturer teaches ?course) avg 4.2
• 1 (?lecturer assesses ?course) avg 1.9
• 40 (?course programme SOFTENG)
• 60 (?course programme GENED)
• Courses with courseNumber 700 or higher: 20 percent
• SELECT * {
?course1 uni:programme SOFTENG . 40 = 40
?course1 uni:cnr ?coursenr . *1 = 40
FILTER (?coursenr >= 700) *1 = 40 
?lecturer uni:assesses ?course1 . *0.2 *1 = 8
?lecturer uni:teaches ?course2 . *4.2 < 38
?course2 uni:programme uni:GENED *1 < 38
} < 204 
 Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Cost es ti mation wi th fi lters

•  avg 2. 2  (?lec turer  teaches ?course) avg  4. 2

•  1 (?lecturer ass es ses  ?c ours e)  av g 1.9

•  40 (?course programme  SOFT ENG)

•  60 (?course programme  GENED )

•  Courses  with  cours eNumber  700  or  higher: 20 percent

•  SELECT * {

   ?course1 uni:programme SOFTENG .        40    = 40

   ?course1 uni:cnr  ?coursenr .           *1    = 40

   FILTER  (?coursenr >= 700)              *1    = 40

   ?lecturer uni:assesses ?course1 . *0.2  *1    = 8

   ?lecturer uni:teaches ?course2 .       *4.2   < 38

   ?course2 uni:programme uni:GENED          *1  < 38

   }                                                                < 204

SE 351                           Geral d Weber's Sl ides                       9
````

### 图片文字 OCR（en-US，待对照原页）

````text
Cost estimation with filters
avg 2.2 (?lecturer teaches ?course) avg 4.2
1 (?lecturer assesses ?course) avg 1.9
40 (?course programme SOFT ENG)
60 (?course programme GENED)
Courses with courseNumber 700 or higher: 20 percent
• SELECT * {
?coursel uni : progran•une SOFTENG
?coursel uni : cnr ?coursenr
FILTER (?coursenr >= 700)
? lecturer uni : assesses ?coursel
*0.2
? lecturer uni : teaches ?course2
?course2 uni : programme uni : GENED
SE 351
Gerald Weber's Slides
= 40
= 40
38
38
204
9
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../source/751/751%2525/DB51-GW02-QueryOpt3.pdf#page=10)

### 原始文字层

````text
SE 351 10
Lower bound
• avg 2.2 (?lecturer teaches ?course) avg 4.2
• 1 (?lecturer assesses ?course) avg 1.9
• 40 (?course programme SOFTENG)
• 60 (?course programme GENED)
• Courses with courseNumber 700 or higher: 20 percent
• SELECT * {
?course1 uni:programme SOFTENG . 40 = 40
?lecturer uni:assesses ?course1 . *1 = 40
?course1 uni:cnr ?coursenr . *1 = 40
FILTER (?coursenr >= 700) *1 = 40 
?lecturer uni:teaches ?course2 . *0.2 *4.2 > 32
?course2 uni:programme uni:GENED *1 > 32
} > 224 
 Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Lower bound

•  avg 2. 2  (?lec turer  teaches ?course) avg  4. 2

•  1 (?lecturer ass es ses  ?c ours e)  av g 1.9

•  40 (?course programme  SOFT ENG)

•  60 (?course programme  GENED )

•  Courses  with  cours eNumber  700  or  higher: 20 percent

•  SELECT * {

   ?course1 uni:programme SOFTENG .        40    = 40

   ?lecturer uni:assesses ?course1 .       *1    = 40

   ?course1 uni:cnr  ?coursenr .           *1    = 40

   FILTER  (?coursenr >= 700)              *1    = 40

   ?lecturer uni:teaches ?course2 . *0.2                    *4.2   > 32

   ?course2 uni:programme uni:GENED          *1  > 32

   }                                                                 > 224

SE 351                            Geral d Weber's Sl ides                      10
````

### 图片文字 OCR（en-US，待对照原页）

````text
Lower bound
avg 2.2 (?lecturer teaches ?course) avg 4.2
1 (?lecturer assesses ?course) avg 1.9
40 (?course programme SOFT ENG)
60 (?course programme GENED)
Courses with courseNumber 700 or higher: 20 percent
• SELECT * {
?coursel uni : progran•une SOFTENG
? lecturer uni : assesses ?coursel
?coursel uni : cnr ?coursenr
FILTER (?coursenr >= 700)
? lecturer uni : teaches ?course2
*0.2
?course2 uni : programme uni : GENED
= 40
>
>
>
SE 351
Gerald Weber's Slides
32
32
224
10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../source/751/751%2525/DB51-GW02-QueryOpt3.pdf#page=11)

### 原始文字层

````text
Summary
• Query optimization: Join order optimization
• The order of the triple patterns in SPARQL give a simple 
linear query execution plan.
• Depending on the order of the triples in this plan the cost 
can differ.
• Previous choices in the plan bind variables and change the 
effective abstract triple pattern.
• With cost metrics we can estimate cost of query.
• To exclude a plan we need a lower bound, do accept a 
plan we want a conservative estimate.
• Applying filters early is good – reducing the cost.
2019 Gerald Weber's Slides 11
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Summary

•  Quer y o ptimization : Join  or der o ptimizatio n

•  T he order of the triple patterns i  n S  PARQL give a simple

   linear query execution plan.

•  Dependi  ng on the order of the tr iples in this plan the cost

   can di  ffer.

•  Previous choices in the plan bind variables and change the

   effective abstract triple pattern.

•  With cost metri  cs w  e can esti  mate cost of query.

•  T o exclude a plan we need a l  ow  er bound, do accept a

   plan we w  ant a conservati  ve estimate.

•  Applying filters early is good – reducing the cost.

20   19                              Geral d Weber's Sl ides                         11
````

### 图片文字 OCR（en-US，待对照原页）

````text
Summary
Query optimization: Join order optimization
The order of the triple patterns in SPARQL give a simple
linear query execution plan.
Depending on the order of the triples in this plan the cost
can differ.
Previous choices in the plan bind variables and change the
effective abstract triple pattern.
With cost metrics we can estimate cost of query.
To exclude a plan we need a lower bound, do accept a
plan we want a conservative estimate.
Applying filters early is good — reducing the cost.
2019
Gerald Weber's Slides
11
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../source/751/751%2525/DB51-GW02-QueryOpt3.pdf#page=12)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（en-US，待对照原页）

````text
ID xvy€llent description ?name ) avg 1
10
(Qingredlent descnption "Waiheke Honey" ) avg 0 01
SELECT ?product {
"pat. lee" order ? shop.
? shop stocks ? product.
* Imo
* 10
?product contains ? ingredient.
?product class ORGANIC.
? ingredient description "Waiheke Honey
Gerald
20
: 20 ooo
: 200 ooo
: 200 ooo
*1 : 200 ooo
= 620 020
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../../source/751/751%2525/DB51-GW02-QueryOpt3.pdf#page=13)

### 原始文字层

````text
organic
o­nes
1000
i­n
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
orjavll\ t/
description ?name ) avg
(?lngredient description "Waiheke Honey" ) avg 0.01
SELECT ?product {
\ pat. lee" order ? shop.
? shop stocks ? product.
? product contains ? ingredient.
? product class
( 000.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../../source/751/751%2525/DB51-GW02-QueryOpt3.pdf#page=14)

### 原始文字层

````text
一
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
(?ingredlent description 'a\//aiheke Honey" ） avg 0 ． 01
SELECT ?product {
、 p 三 · “ 0 r de r ?shop.
?shop s 乜 0 c s ?product.
?product c 工 a s s ORGAIIIC ·
？ 了 0 记 C 二 C 0 n 乜 a 上 S ？ 《 0 F_I 0 过 ·
* 1000
* 01 * 10
二 20
： 20 000
： 20 000
： 20 000
： 20 000
= 80 020
````

### 图片文字 OCR（en-US，待对照原页）

````text
( %inæ-d.ent description "Waiheke Honey" ) avg 001
SELECT ?product {
'pat. Lee" order ? shop.
? shop stocks ? product.
? product class ORGANIC.
? crociucz contains ? i narezlienz.
* 1000
*1
* 0.1
20
20 ooo
20 ooo
20 ooo
20 ooo
eo 020
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../../source/751/751%2525/DB51-GW02-QueryOpt3.pdf#page=15)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（en-US，待对照原页）

````text
description ?name )
avg 1
10
(?ingredient description "Waiheke Honey" ) avg 0.01
SELECT ?product {
? ingredient description "Waiheke
? product contains ? ingredient.
Honey'
* 100
? product class ORGANIC.
? shop stocks ? product.
*1
* 0.1 * 100
Best Plan found
10
1000
1000
10 ooo
10 ooo
22010
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../../source/751/751%2525/DB51-GW02-QueryOpt3.pdf#page=16)

### 原始文字层

````text
https://chatgpt.com/s/dr_68254ffd33748191a93b753def3ed481
````

### 图片文字 OCR（en-US，待对照原页）

````text
https://chatgpt.com/s/dr_68254ffd33748191 a93b753def3ed481
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

