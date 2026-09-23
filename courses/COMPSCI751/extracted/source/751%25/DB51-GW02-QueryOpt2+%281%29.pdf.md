# DB51-GW02-QueryOpt2+%281%29.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI751/source/751%25/DB51-GW02-QueryOpt2+%281%29.pdf`
- [打开原文件](../../../source/751%2525/DB51-GW02-QueryOpt2%2B%25281%2529.pdf)
- 原文件 SHA-256：`70e232b0da3234c83630a6cb6f29532f20a6f79e5c10fd35b8bfa6fef5f94f23`
- 文件索引：F157；PDF 总页数：16
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../source/751%2525/DB51-GW02-QueryOpt2%2B%25281%2529.pdf#page=1)

### 原始文字层

````text
2019 Gerald Weber's Slides 1
Databases 51
SPARQL Evaluation, Query optimization
• Index Join
• In-memory Index join cost
• Join Order Optimization
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Databas es  51
 SP ARQL Evaluation, Query optimi  zation
 •  Index Join
 •  In-memory Index join cost
 •  Join Order Optimization
 20   19                           Geral d Weber's Sl ides                        1
````

### 图片文字 OCR（en-US，待对照原页）

````text
Databases 51
SPARQL Evaluation, Query optimization
Index Join
In-memory Index join cost
Join Order Optimization
2019
Gerald Weber's Slides
1
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../source/751%2525/DB51-GW02-QueryOpt2%2B%25281%2529.pdf#page=2)

### 原始文字层

````text
SE 351 2
Evaluation of query with single triple pattern
• Evaluation of single triple pattern is a primitive offered by a triplestore:
• SELECT * {
?lecturer teaches ?course .
}
Result set:
• L1234567, C234567 
• L1234567, C45678 
• L7654321, C234567 
L1234567 name Pat .
L7654321 name Vic .
L1234567 room 829 .
L7654321 room 567 .
C234567 programme GENED .
C45678 programme SOFTENG .
C234567 year 2019 .
C45678 year 2017 .
L1234567 teaches C234567 . 
L1234567 teaches C45678 .
L7654321 teaches C234567 .
L7654321 assesses C45678 .
Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Evaluati on of query  wi th s ingl e tri ple pattern
• Evaluation of  single  triple pattern is  a primitive  of fered  by a triplest ore:
• SELECT * {
  ?lecturer teaches ?course .
  }
Res ult  set :                                      L1 234 567  na me  Pat  .
                                                    L7 654 321  na me  Vic  .
• L1234567, C234567                                 L1 234 567  ro om  829  .
• L1234567, C45678                                  L7 654 321  ro om  567  .
                                                    C2 345 67  pro gra mme  GE NED  .
• L7654321, C234567                                 C4 567 8 p rog ram me  SOF TEN G .
                                                    C2 345 67  yea r 2 019  .
                                                    C4 567 8 y ear  20 17  .
                                                    L1 234 567 te ach es C2 345 67 .
                                                    L1 234 567 te ach es C4 567 8 .
                                                    L7 654 321 te ach es C2 345 67 .
                                                    L7 654 321  as ses ses  C4 567 8 .
SE 351                                Geral d Weber's Sl ides                            2
````

### 图片文字 OCR（en-US，待对照原页）

````text
Evaluation of query with single triple pattern
• Evaluation of single triple pattern is a primitive offered by a triplestore:
• SELECT * {
Olecturer
tea Che S ?
course
Result set:
L1234567,
1.1234567,
1.7654321,
SE 351
c234567
C45678
c234567
1.1234567
1.7654321
L1234567
1.7654321
name
name
room
room
Pat
Vic
829
567
C234567 prograrmne GENED
C45678 programme SOFTENG
C234567 year 2019
C45678 year 2017
1.1234567
1.1234567
1.7654321
1.7654321
Gerald Weber's Slides
c234567
teaches
C45678
teaches
C234567
teaches
assesses C45678
2
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../source/751%2525/DB51-GW02-QueryOpt2%2B%25281%2529.pdf#page=3)

### 原始文字层

````text
SE 351 3
Evaluation of query with single triple pattern
• Evaluation of single triple pattern is a primitive offered by a triplestore:
• The primitive will return the triples, i.e. a subgraph:
• SELECT * {
?lecturer teaches ?course .
}
Result: a set of actual triples
• L1234567 teaches C234567 . 
• L1234567 teaches C45678 .
• L7654321 teaches C234567 .
L1234567 name Pat .
L7654321 name Vic .
L1234567 room 829 .
L7654321 room 567 .
C234567 programme GENED .
C45678 programme SOFTENG .
C234567 year 2019 .
C45678 year 2017 .
L1234567 teaches C234567 . 
L1234567 teaches C45678 .
L7654321 teaches C234567 .
L7654321 assesses C45678 .
Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Evaluati on of query  wi th s ingl e tri ple pattern
• Evaluation of  single  triple pattern is  a primitive  of fered  by a triplest ore:
• The primit ive will  ret urn  the triples,  i.e.   a subgraph:
• SELECT * {
  ?lecturer teaches ?course .
  }
Res ult : a  set of  actual t riples                 L1 234 567  na me  Pat  .
                                                     L7 654 321  na me  Vic  .
• L1234567 teaches C234567 .                         L1 234 567  ro om  829  .
• L1234567 teaches C45678 .                          L7 654 321  ro om  567  .
                                                     C2 345 67  pro gra mme  GE NED  .
• L7654321 teaches C234567 .                         C4 567 8 p rog ram me  SOF TEN G .
                                                     C2 345 67  yea r 2 019  .
                                                     C4 567 8 y ear  20 17  .
                                                     L1 234 567  te ach es  C23 456 7 .
                                                     L1 234 567  te ach es  C45 678  .
                                                     L7 654 321  te ach es  C23 456 7 .
                                                     L7 654 321  as ses ses  C4 567 8 .
SE 351                                Geral d Weber's Sl ides                              3
````

### 图片文字 OCR（en-US，待对照原页）

````text
Evaluation of query with single triple pattern
• Evaluation of single triple pattern is a primitive offered by a triplestore:
• The primitive will return the triples, i.e. a subgraph:
? lecturer teaches ?course
Result: a set of actual triples
• 1.1234567 teaches C234567
1.1234567 teaches C45678
1.7654321 teaches C234567
1.1234567
1.7654321
L1234567
1.7654321
name
name
room
room
Pat
Vic
829
567
C234567 prograrmne GENED
C45678 programme SOFTENG
C234567 year 2019
C45678 year 2017
SE 351
1.1234567
1.1234567
1.7654321
1.7654321
Gerald Weber's Slides
teaches C234567
teaches C45678
teaches C234567
assesses C45678
3
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../source/751%2525/DB51-GW02-QueryOpt2%2B%25281%2529.pdf#page=4)

### 原始文字层

````text
SE 351 4
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
• Evaluation of  single  triple pattern is  a primitive  of fered  by a t riples tore  :
• SELECT * WHERE {C45678  ?predicate  ?object }
• Possible 8 abstract  triple patt erns:
• ?subject ?predicate  ?object     XYZ
  C45678   ?predicate  ?object     SYZ
  ?subject ?predicate  SOFTENG     XYO
  ?subject  programme  ?object     XPZ
  ?subject  programme  SOFTENG     XPO                               Most
  C45678    programme   ?object    SPZ                               specif ic
  C45678   ?predicate   SOFTENG    SYO
  C45678    programme   SOFTENG    SPO
• Optimal query c os t f or  single triple pattern:  linear in s ize of  res ult s et
• Is  achievable wit h enough index s upport!  (but  not alw ay s done)
SE 351                            Geral d Weber's Sl ides                         4
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
4
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../source/751%2525/DB51-GW02-QueryOpt2%2B%25281%2529.pdf#page=5)

### 原始文字层

````text
SE 351 5
Towards evaluating multi-pattern queries
• SPARQL query with two triple patterns and a shared 
variable is an equijoin and a self-join of the triple table:
• SELECT * {
?lecturer name ?name .
?lecturer teaches ?course .
}
• Triple ⋈ equijoin on subject Triple
• How can this be achieved with the 
evaluation of single triple patterns?
Triple(subject, predicate, object)
L1234567 name Pat .
L7654321 name Vic .
L1234567 room 829 .
L7654321 room 567 .
C234567 programme GENED .
C45678 programme SOFTENG .
C234567 year 2019 .
C45678 year 2017 .
L1234567 teaches C234567 . 
L1234567 teaches C45678 .
L7654321 teaches C234567 .
L7654321 assesses C45678 .
Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Towards evaluating mul ti-pattern quer ies
• SP ARQL         query with two triple patterns and a shared
  variabl  e is an equij  oi  n and a self-join of the triple table:
• SELECT * {
  ?lecturer name ?name .
  ?lecturer teaches ?course .
  }                                                 L1 234 567  na me  Pat  .
                                                    L7 654 321  na me  Vic  .
• Triple ⋈ equijoin on subject Triple               L1 234 567  ro om  829  .
                                                    L7 654 321  ro om  567  .
                                                    C2 345 67  pro gra mme  GE NED  .
• How  can t his  be achieved w ith the             C4 567 8 p rog ram me  SOF TEN G .
                                                    C2 345 67  yea r 2 019  .
  evaluation of  single  triple patterns?           C4 567 8 y ear  20 17  .
                                                    L1 234 567  te ach es  C23 456 7 .
                                                    L1 234 567  te ach es  C45 678  .
Triple(subject, predicate, object)                  L7 654 321  te ach es  C23 456 7 .
                                                    L7 654 321  as ses ses  C4 567 8 .
SE 351                               Geral d Weber's Sl ides                             5
````

### 图片文字 OCR（en-US，待对照原页）

````text
Towards evaluating multi-pattern queries
SPARQL query with two triple patterns and a shared
variable is an equijoin and a self-join of the triple table:
• SELECT * {
? lecturer name ?name
? lecturer teaches ?course
• Triple
equijoin on subject r i ple
• How can this be achieved with the
evaluation of single triple patterns?
Triple (subject, predicate, object)
1.1234567
1.7654321
L1234567
1.7654321
name
name
room
room
Pat
Vic
829
567
C234567 prograrmne GENED
C45678 programme SOFTENG
C234567 year 2019
C45678 year 2017
1.1234567
1.1234567
1.7654321
1.7654321
teaches C234567
teaches C45678
teaches C234567
assesses C45678
SE 351
Gerald Weber's Slides
5
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../source/751%2525/DB51-GW02-QueryOpt2%2B%25281%2529.pdf#page=6)

### 原始文字层

````text
SE 351 6
Towards evaluating multi-pattern queries
• Natural approach: dealing with the triple patterns in the order 
that they appear in the query:
• SELECT ?name {
?lecturer name ?name . (a)
?lecturer teaches ?course . (b)
}
• Triple ⋈ equijoin on subject Triple
• Cost of evaluating the first
single triple pattern? XPZ 2
• Idea: for each result of (a), 
• we have to find all matching
results of (b)!
L1234567 name Pat .
L7654321 name Vic .
L1234567 room 829 .
L7654321 room 567 .
C234567 programme GENED .
C45678 programme SOFTENG .
C234567 year 2019 .
C45678 year 2017 .
L1234567 teaches C234567 .
L1234567 teaches C45678 .
L7654321 teaches C234567 .
L7654321 assesses C45678 .
Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Towards evaluating mul ti-pattern quer ies
• Natural approach: dealing with the triple patterns in the order
  that they appear in the query:
• SELECT ?name {
  ?lecturer name ?name .      (a)
  ?lecturer teaches ?course . (b)
  }                                                  L1 234 567  na me  Pat  .
                                                     L7 654 321  na me  Vic  .
• Triple ⋈ equijoin on subject Triple                L1 234 567  ro om  829  .
                                                     L7 654 321  ro om  567  .
• Cos t of  evaluat ing  the firs t                  C2 345 67  pro gra mme  GE NED  .
  single t riple patt ern?   XPZ              2      C4 567 8 p rog ram me  SOF TEN G .
                                                     C2 345 67  yea r 2 019  .
• Idea: for each result  of  (a),                    C4 567 8 y ear  20 17  .
• we  hav e  to f ind all mat ching                  L1 234 567  te ach es  C23 456 7 .
                                                     L1 234 567  te ach es  C45 678  .
  results  of  (b)!                                  L7 654 321  te ach es  C23 456 7 .
                                                     L7 654 321  as ses ses  C4 567 8 .
SE 351                                Geral d Weber's Sl ides                              6
````

### 图片文字 OCR（en-US，待对照原页）

````text
Towards evaluating multi-pattern queries
Natural approach: dealing with the triple patterns in the order
that they appear in the query:
• SELECT ?name {
? lecturer name ?name
? lecturer teaches ?course
(a)
(b)
1.1234567
1.7654321
L1234567
1.7654321
• Triple
equijoin on subject r i ple
• Cost of evaluating the first
single triple pattern? XPZ
• Idea: for each result of (a),
• we have to find all matching
of (b)!
resu
SE 351
name
name
room
room
Pat
Vic
829
567
2
C234567 prograrmne GENED
C45678 programme SOFTENG
C234567 year 2019
C45678 year 2017
1.1234567
1.1234567
1.7654321
1.7654321
Gerald Weber's Slides
teaches C234567
teaches C45678
teaches C234567
assesses C45678
6
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../source/751%2525/DB51-GW02-QueryOpt2%2B%25281%2529.pdf#page=7)

### 原始文字层

````text
SE 351 7
Towards evaluating multi-pattern queries
• Naive evaluation as Nested Loop. Makes no use of 
current chosen match in outer loop.
• SELECT ?name {
?lecturer name ?name . (a)
?lecturer teaches ?course . (b)
}
for (each result of (a)) {
for (each result of (b)) {
 check equijoin;
 process filter;
 project;
 output;
} }
L1234567 name Pat .
L7654321 name Vic .
L1234567 room 829 .
L7654321 room 567 .
C234567 programme GENED .
C45678 programme SOFTENG .
C234567 year 2019 .
C45678 year 2017 .
L1234567 teaches C234567 .
L1234567 teaches C45678 .
L7654321 teaches C234567 .
L7654321 assesses C45678 .
Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Towards evaluating mul ti-pattern quer ies
• Naive evaluation  as Nested  Lo op. Makes no use of
  current chosen match in outer l  oop.
• SE LEC T ? nam e {
  ?l ect ure r n ame  ?n ame  .        ( a)
  ?l ect ure r t eac hes  ?c our se  . ( b)
  }                                                   L1 234 567  na me  Pat  .
for (each result  of  (a))    {                       L7 654 321  na me  Vic  .
                                                      L1 234 567  ro om  829  .
      for (each result  of  (b))  {                   L7 654 321  ro om  567  .
                                                      C2 345 67  pro gra mme  GE NED  .
       check  equijoin;                               C4 567 8 p rog ram me  SOF TEN G .
       process  filter;                               C2 345 67  yea r 2 019  .
                                                      C4 567 8 y ear  20 17  .
       projec t;                                      L1 234 567  te ach es  C23 456 7 .
                                                      L1 234 567  te ach es  C45 678  .
       output;                                        L7 654 321  te ach es  C23 456 7 .
} }                                                   L7 654 321  as ses ses  C4 567 8 .
SE 351                                 Geral d Weber's Sl ides                              7
````

### 图片文字 OCR（en-US，待对照原页）

````text
Towards evaluating multi-pattern queries
Naive evaluation as Nested Loop. Makes no use of
current chosen match in outer loop.
SELECT ?name {
? lecturer name ?name
? lecturer teaches ?course
for (each result of (a)) {
(a)
(b)
1.1234567
1.7654321
L1234567
1.7654321
name
name
room
room
Pat
Vic
829
567
for (each result of (b)) {
check equijoin;
process filter;
project;
output;
SE 351
C234567 prograrmne GENED
C45678 programme SOFTENG
C234567 year 2019
C45678 year 2017
1.1234567
1.1234567
1.7654321
1.7654321
Gerald Weber's Slides
teaches C234567
teaches C45678
teaches C234567
assesses C45678
7
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../source/751%2525/DB51-GW02-QueryOpt2%2B%25281%2529.pdf#page=8)

### 原始文字层

````text
SE 351 8
Towards evaluating multi-pattern queries
• Idea: The effect of outer loops is a variable binding and a 
possible change of abstract triple pattens.
• SELECT * {
?lecturer name ?name . (a)
?lecturer teaches ?course . (b)
}
for (each result of (a)) {
for (each matching result of (b)) {
 process filter; …
} }
• matching: Variable binding: 
• In (b): ?lecturer is known from (a):
• (b) is not XPZ, but SPZ 
L1234567 name Pat .
L7654321 name Vic .
L1234567 room 829 .
L7654321 room 567 .
C234567 programme GENED .
C45678 programme SOFTENG .
C234567 year 2019 .
C45678 year 2017 .
L1234567 teaches C234567 .
L1234567 teaches C45678 .
L7654321 teaches C234567 .
L7654321 assesses C45678 .
equijoin
Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Towards evaluating mul ti-pattern quer ies
•  Idea: T he effect of outer l  oops is a variable bindi  ng and a
   possible change of abstract triple pattens.
•  SE LEC T *  {
   ?l ect ure r n ame  ?n ame  .        ( a)
   ?l ect ure r t eac hes  ?c our se  . ( b)
   }                                                   L1 234 567  na me  Pat  .
for (each result  of  (a))     {                       L7 654 321  na me  Vic  .
                                                       L1 234 567  ro om  829  .
     for (each matc hing result  of  (b))  {           L7 654 321  ro om  567  .
                                                       C2 345 67  pro gra mme  GE NED  .
       process  filter;  …                             C4 567 8 p rog ram me  SOF TEN G .
} }                                     eq uij oin     C2 345 67  yea r 2 019  .
                                                       C4 567 8 y ear  20 17  .
•    matc hing:  Variable binding:                     L1 234 567  te ach es  C23 456 7 .
                                                       L1 234 567  te ach es  C45 678  .
•    In  (b): ?lecturer is  known from  (a):           L7 654 321  te ach es  C23 456 7 .
•    (b) is  not  XPZ,  but  SPZ                       L7 654 321  as ses ses  C4 567 8 .
SE 351                                 Geral d Weber's Sl ides                                8
````

### 图片文字 OCR（en-US，待对照原页）

````text
Towards evaluating multi-pattern queries
Idea: The effect of outer loops is a variable binding and a
possible change of abstract triple pattens.
SELECT * {
? lecturer name ?name
? lecturer teaches ?course
for (each result of (a)) {
(a)
(b)
1.1234567
1.7654321
L1234567
1.7654321
name
name
room
room
Pat
Vic
829
567
for (each matching result of (b))
process filter; ...
equij oin
matching: Variable binding:
In (b): ?lecturer is known from (a):
(b) is not xpz, but SPZ
C234567 prograrmne GENED
C45678 programme SOFTENG
234567 year 2019
C45678 year 2017
1.1234567
1.1234567
1.7654321
1.7654321
SE 351
Gerald Weber's Slides
teaches C234567
teaches C45678
teaches C234567
assesses C45678
8
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../source/751%2525/DB51-GW02-QueryOpt2%2B%25281%2529.pdf#page=9)

### 原始文字层

````text
SE 351 9
Query execution
• Evaluation of Sparql Query as nested for loops:
• Outermost for loop of (a):
• Result set
• for each step of one for loop: new inner for loop for (b)
SELECT * {
?lecturer name ?name . (a)
?lecturer teaches ?course . (b)
}
Triangle: Typical way to represent a node 
with a large fanout in a tree, right side 
representing the child nodes
Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Query executi on
•  Evaluation of Sparql Query as nested for l  oops:
•  Outermost for l  oop of (a):
                                          SE LEC T *  {
                                          ?l ect ure r n ame  ?n ame  .        ( a)
                                          ?l ect ure r t eac hes  ?c our se  . ( b)
                                          }
                                         Trian  gle  :  Typi  cal  wa  y t o  rep  resen  t  a  no  de
                                         wi  th   a   l  arge   fanout in  a  tree , rig ht si de
                                         rep resen ti ng the chi ld no des
•                                          Result set
•  for each step of one for loop: new inner for loop for ( b)
SE 351                                    Geral d Weber's Sl ides                                   9
````

### 图片文字 OCR（en-US，待对照原页）

````text
Query execution
Evaluation of Sparql Query as nested for loops:
Outermost for loop of (a):
SELECT * {
? lecturer name ?name
? lecturer teaches ?course
(b)
Triangle: Typical way to represent a node
with a large fanout in a tree, right side
representing the child nodes
Result set
for each step of one for loop: new inner for loop for (b)
SE 351
Gerald Weber's Slides
9
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../source/751%2525/DB51-GW02-QueryOpt2%2B%25281%2529.pdf#page=10)

### 原始文字层

````text
SE 351 10
Query execution
• Evaluation of Sparql Query as nested for loops:
• Outermost for loop of (a):
• for each step of one for loop: new inner for loop for (b)
• (c) ?course is known, 
• so SPZ single triple pattern query
SELECT * {
?lecturer name ?name . (a)
?lecturer teaches ?course . (b)
?course programme ?p (c)
}
Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Query executi on
•  Evaluation of Sparql Query as nested for l  oops:
•  Outerm ost for l  oop of (a):
                                             SE LEC T *  {
                                             ?l ect ure r n ame  ?n ame  .        ( a)
                                             ?l ect ure r t eac hes  ?c our se  . ( b)
                                             ?c our se  pro gra mme  ?p           ( c)
                                             }
•  for each step of one for loop: new inner for loop for ( b)
•                                      (c)   ?course is know  n,
•                                  so SPZ  single tr iple pattern query
SE 351                                 Geral d Weber's Sl ides                              10
````

### 图片文字 OCR（en-US，待对照原页）

````text
Query execution
Evaluation of Sparql Query as nested for loops:
Outermost for loop of (a):
SELECT * {
? lecturer name ?name
? lecturer teaches ?course
?course programne ?p
for each step of onef loop: new inner for loop for (b)
SE 351
(c) ?course is known,
so SPZ single triple pattern query
Gerald Weber's Slides
(a)
(b)
(c)
10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../source/751%2525/DB51-GW02-QueryOpt2%2B%25281%2529.pdf#page=11)

### 原始文字层

````text
SE 351 11
As nested Join
• (Triple ⋈ equijoin Triple) ⋈ equijoin Triple
SELECT * {
?lecturer name ?name . (a)
?lecturer teaches ?course . (b)
?course programme ?p (c)
}
Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
As nested J oi n
•  (Triple ⋈ equijoin      T riple) ⋈ equijoin Triple
                                               SE LEC T *  {
                                               ?l ect ure r n ame  ?n ame  .        ( a)
                                               ?l ect ure r t eac hes  ?c our se  . ( b)
                                               ?c our se  pro gra mme  ?p           ( c)
                                               }
SE 351                                  Geral d Weber's Sl ides                                11
````

### 图片文字 OCR（en-US，待对照原页）

````text
As nested Join
(Triple
Triple)
Triple
equijoin
equijoin
SE 351
SELECT * {
? lecturer name ?name
? lecturer teaches ?course
?course programne ?p
Gerald Weber's Slides
(a)
(b)
(c)
11
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../source/751%2525/DB51-GW02-QueryOpt2%2B%25281%2529.pdf#page=12)

### 原始文字层

````text
SE 351 12
Estimating Cost
• We can estimate the cost of a query plan if we have the 
average cost of the abstract triple patterns for a given 
predicate:
• E.g. For teaches:
• Each course is taught by an average of 2.2 lecturers.
• Each lecturer teaches an average of 4.2 courses.
• We denote this in the following form:
avg 2.2 (?lecturer teaches ?course) avg 4.2
• If there is only one assessor then we have
1 (?lecturer assesses ?course) avg 1.9
Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Estimati ng Cos t
• We can     estimate     the cost of a query plan if w  e have the
  average cost of the abstract triple patterns for a given
  predicate:
• E.g. For teaches:
• Each course is taught by an average of 2.2 l  ecturers.
• Each lecturer teaches an average of 4.2 courses.
• We denote thi  s i  n the foll  ow  ing form:
     avg 2.2 ( ?l  ecturer teaches ?course) avg 4.2
• If there i  s only one assessor then we have
        1 (?lecturer assesses ?course) avg 1.9
SE 351                            Geral d Weber's Sl ides                      12
````

### 图片文字 OCR（en-US，待对照原页）

````text
Estimating Cost
We can estimate the cost of a query plan if we have the
average cost of the abstract triple patterns for a given
predicate:
E.g. For
teaches:
Each course is taught by an average of 2.2 lecturers.
Each lecturer teaches an average of 4.2 courses.
We denote this in the following form:
avg 2.2 (?lecturer teaches ?course) avg 4.2
If there is only one assessor then we have
1 (?lecturer assesses ?course) avg 1.9
SE 351
Gerald Weber's Slides
12
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../source/751%2525/DB51-GW02-QueryOpt2%2B%25281%2529.pdf#page=13)

### 原始文字层

````text
SE 351 13
Costs and Cost metrics notation we use
• Each course is taught by an average of 2.2 lecturers
• Each lecturer teaches an average of 4.2 courses.
• We denote this in the following form:
avg 2.2 (?lecturer teaches ?course) avg 4.2
• If there is only one assessor then we have
1 (?lecturer assesses ?course) avg 1.9
• For constant subjects or objects: cost may be known:
2 (?lecturer teaches C234567) 
Cost 
metrics 
we use 
Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Costs and Cos t metri cs  notati on we use
• Each course is taught by an average of 2.2 l  ecturers
• Each lecturer teaches an average of 4.2 courses.
• We denote thi  s i  n the foll  ow  ing form:
     avg 2.2 ( ?l  ecturer teaches ?course) avg 4.2
• If there i  s only one assessor then we have                        Co st
                                                                      metrics
        1 (?lecturer assesses ?course) avg 1.9                        we use
• F or constant subj  ects or objects: cost may be known:
        2 (?lecturer teaches C234567)
SE 351                            Geral d Weber's Sl ides                        13
````

### 图片文字 OCR（en-US，待对照原页）

````text
Costs and Cost metrics notation we use
Each course is taught by an average of 2.2 lecturers
Each lecturer teaches an average of 4.2 courses.
We denote this in the following form:
avg 2.2 (?lecturer teaches ?course) avg 4.2
If there is only one assessor then we have
1 (?lecturer assesses ?course) avg 1.9
For constant subjects or objects: cost m
2 (?lecturer teaches C234567)
Cost
metrics
we use
e known:
SE 351
Gerald Weber's Slides
13
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../source/751%2525/DB51-GW02-QueryOpt2%2B%25281%2529.pdf#page=14)

### 原始文字层

````text
SE 351 14
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
• avg 2.2 ( ?l  ecturer teaches ?course) avg 4.2
• 1 (?lecturer assesses ?course) avg 1.9
• 40 (?course programm e SOFT ENG)
• 60 (?course programm e GENED  )
• SELECT * {
  ?course2 programme GENED
  ?lecturer teaches ?course2 .
  ?lecturer assesses ?course1 .
  ?course1 programme SOFTENG .
  }
SE 351                         Geral d Weber's Sl ides                   14
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
14
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../source/751%2525/DB51-GW02-QueryOpt2%2B%25281%2529.pdf#page=15)

### 原始文字层

````text
SE 351 15
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
• avg 2.2 ( ?l  ecturer teaches ?course) avg 4.2
• 1 (?lecturer assesses ?course) avg 1.9
• 40 (?course programm e SOFT ENG)
• 60 (?course programm e GENED  )
• SELECT * {
  ?course2 programme GENED       60               = 60
  ?lecturer teaches ?course2 .      *2.2          = 132
  ?lecturer assesses ?course1 .         *1.9      < 255
  ?course1 programme SOFTENG .                               *1  < 255
  }                                              _____
   Abstr act T ri  pl  e P  attern S  PO          Co nse rva tiv e e st.      < 702
SE 351                         Geral d Weber's Sl ides                  15
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
15
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../source/751%2525/DB51-GW02-QueryOpt2%2B%25281%2529.pdf#page=16)

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
2019 Gerald Weber's Slides 16
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Summary
• Quer y o ptimization : Join  or der o ptimizatio n
• T he order of the triple patterns i  n S  PARQL give a simple
  linear query execution plan.
• Dependi  ng on the order of the tr iples in this plan the cost
  can di  ffer.
• Previous choices in the plan bind variables and change the
  effective abstract triple pattern.
• With cost metri  cs w  e can esti  mate cost of query.
20   19                            Geral d Weber's Sl ides                        16
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
2019
Gerald Weber's Slides
16
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

