# DB51-GW01-QueryOpt1.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI751/source/751/751%25/DB51-GW01-QueryOpt1.pdf`
- [打开原文件](../../../../source/751/751%2525/DB51-GW01-QueryOpt1.pdf)
- 原文件 SHA-256：`dd913f3eb621bb762fa0be52d4f46d8f8b6e940884294e313d7cfe9d37ed4887`
- 文件索引：F110；PDF 总页数：22
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../source/751/751%2525/DB51-GW01-QueryOpt1.pdf#page=1)

### 原始文字层

````text
2019 Gerald Weber's Slides 1
Query Optimization Gerald Weber
 Databases 51
Query optimization with triplestores
• Motivation for triplestores from Semantic Web
• Motivation for triplestores from relational database 
limitations
• Query Language SPARQL
• Query evaluation
• Query cost estimation
• In-memory index join cost
• Join order optimization
Introducing an
example of NoSQL 
databases: triplestores
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Query Optimization                    Gerald Weber
                                                                    Databases 51
 Query optimi  zation with triplestores
 •  Moti  vation for tr iplestores fr om Semantic Web
 •  Moti  vation for tr iplestores fr om r el  ational database
    limitations
 •  Query Language SPA RQL                    Introducing an
 •  Query evaluati  on                        example of NoSQL
 •  Query cost estimation                     databases: trip lestor es
 •  In-memory index join cost
 •  Join order optimization
 20   19                            Geral d Weber's Sl ides                         1
````

### 图片文字 OCR（en-US，待对照原页）

````text
Query Optimization
Query optimization with triplestores
Gerald Weber
Databases 51
Motivation for triplestores from Semantic Web
Motivation for triplestores from relational database
limitations
Query Language SPARQL
Query evaluation
Query cost estimation
In-memory index join cost
Join order optimization
Introducing an
example of NoSQL
databases: triplestores
2019
Gerald Weber's Slides
1
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../source/751/751%2525/DB51-GW01-QueryOpt1.pdf#page=2)

### 原始文字层

````text
The Semantic Web [Lee 1999]
• A web of data.
Tim Berners Lee
April 2017
Gerald Weber's Slides 2
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
The Semanti c Web  [Lee 1999]
• A web of data.
             Tim  Berners  Lee
                                                               April 2017
                                  Geral  d Webe r's  Sl  ides                    2
````

### 图片文字 OCR（en-US，待对照原页）

````text
The Semantic Web
A web of data.
Tim Berners Lee
In the news
[Lee 1999]
• Tim Berners-Lee (pictured) wins
the Turing Award for inventing the
World Wide Web, the first web
browser, and the protocols and
algorithms that allow the Web to
scale.
Gerald Weber's Slides
April 2017
2
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../source/751/751%2525/DB51-GW01-QueryOpt1.pdf#page=3)

### 原始文字层

````text
Triplestores: Motivation from Semantic Web
The World Wide Web
• E.g. showtimes page of a 
movie theatre
• Based on formatted text. 
• HTML (Hypertext Markup
Language)
• Human readable
The Semantic Web
• Integrate all showtimes
from all movie theatres
• Based on semistructured
Data: Triples:
(“SMo700Tiv”, time, “7 pm”) 
(“SMo700Tiv”, movie, “Hi There!”) 
…
 Subject Predicate Object
• RDF (Resource 
Description Format)
• Machine readable
2019 3
Tivoli Theatre
Mon 7pm showing:
 Hi There!
Gerald Weber's Slides
半结构
一一
三 祖
主 诮 宾
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Tri pl estor es : Moti vation from Semanti c Web
T he Wor ld Wid e Web                     T he Seman tic Web
                                          •  Integrate all showtimes
• E.g. showtimes page of a                   fr om all m ovi  e theatres
  movie theatre                           •  Based on semistructured半结构
• Based on formatted text.                   Data: Triples:     三  祖
                                                        ⼀⼀
                   Tivoli Theatre         (“SMo700Tiv ”, t ime, “7 pm”)
      Mon 7pm showing:                    (“SMo700Tiv ”, mov ie,  “Hi  There! ”)
              Hi There!                   …    主        诮           宾
• HT ML ( Hypertext Markup                      Subjec t     Predicate    Objec t
  Language)                               •  RDF  (R  esource
• Human r eadable                            Description F orm at)
                                          •  M achi  ne r eadable
20   19                           Geral  d Webe r's  Sl  ides                    3
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
TripIestores: Motivation fro m Semantic We b
The World Wide We b
E.g. showtimes page 0f a
movie theatre
． Based on formatted text.
丆 / Theatre
Mon 7pm showing:
． HTML (Hypertext Markup
Language)
Human readable
2019
The Semantic We b
《 nteg rate all showtimes
fro m all movie theatres
Based O n semIStructured
Data: Triples•
("SM0700Tiv", time, “ 7 pm")
("SM0700Tiv", movie, "Hi There!")
S u bject Predicate O bject
． RDF (Resource
Description Format)
Machine readable
Gerald Weber's SI ides
3
````

### 图片文字 OCR（en-US，待对照原页）

````text
Triplestores: Motivation from Semantic Web
The World Wide Web
E.g. showtimes page of a
movie theatre
Based on formatted text.
Tivoli Theatre
Mon 7pm showing:
7Æeze,/
HTML (Hypertext Markup
Language)
Human readable
2019
The Semantic Web
Integrate all showtimes
from all movie theatres
Based on semstructured
Data: Triples:
("SM0700Tiv", time, "7 pm")
("SM0700Tiv", movie, "Hi There!")
Subject Predicate Object
RDF (Resource
Description Format)
Machine readable
Gerald Weber's Slides
3
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../source/751/751%2525/DB51-GW01-QueryOpt1.pdf#page=4)

### 原始文字层

````text
SE 351 4
Triplestores: Motivation from Relational Model
Schema:
• Lecturer(lid, name, room)
Course(cid, programme, cnr, year, sem)
Teaches(l[lid from Lecturer], c[cid from Course]) 
Data:
• Lecturer(L1234567, Pat, 829)
Lecturer(L7654321, Vic, 567)
Course(C234567, GENED, 789, 2019, S2)
Course(C45678, SOFTENG, 351, 2017, S1)
Teaches(L1234567, C234567)
Teaches(L7654321, C234567)
Teaches(L1234567, C45678)
Assume: 1. keys unique across tables: no cid clashes with any lid.
2. all column/table names are unique
How would we model this if 
we would have to express all 
data as triples?
Relational data expressed 
here as facts/ground atoms 
of predicate calculus
Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Tri pl estor es : Moti vation from Relational  Model
Schema:
• Lecturer(lid, name, room)
  Course(cid, programme, cnr, year, sem)
  Teaches(l[lid from Lecturer],  c[cid from Course])
Dat a:                                          Relational data ex press ed
• Lecturer(L1234567, Pat, 829)                  here  as f ac ts/ ground atoms
  Lecturer(L7654321, Vic, 567)                  of  predicate  calculus
  Course(C234567, GENED, 789, 2019, S2)
  Course(C45678, SOFTENG, 351, 2017, S1)
  Teaches(L1234567, C234567)                  How  would we  model  this if
  Teaches(L7654321, C234567)                  we  would  hav e to ex press  all
  Teaches(L1234567, C45678)                   data as  triples?
Ass um e:    1. keys  uni que  acr oss tables  :  no cid clas hes  wit h  any  lid.
             2.  all col umn/tabl e  names  ar e un iqu e
SE 351                            Geral  d Webe r's  Sl  ides                    4
````

### 图片文字 OCR（en-US，待对照原页）

````text
Triplestores: Motivation from Relational Model
Schema:
Lecturer (lid, name, room)
Course (cid, programrne, cnr, year, sem)
Teaches (1 [lid from Lecturer] ,
c [cid from Course] )
Data:
Lecturer (L1234567, Pat,
Lecturer (L7654321, Vic,
Course (C234567, GENED,
Course (C45678, SOFTENG,
Relational data expressed
here as facts/ground atoms
829)
of predicate calculus
567)
789, 2019, s2)
351,
Teaches (L1234567, C234567)
Teaches (L7654321, C234567)
Teaches (L1234567, C45678)
2017, sl)
How would we model this if
we would have to express all
data as triples?
Assume: 1. keys unique across tables: no cid clashes with any lid.
2. all column/table names are unique
Gerald Weber's Slides
SE 351
4
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../../source/751/751%2525/DB51-GW01-QueryOpt1.pdf#page=5)

### 原始文字层

````text
SE 351 Gerald Weber's Slides 5
Turning Relational Data into Triples
How would we model the data if we have to use only triples?
• Lecturer(lid, name, room)
Course(cid, programme, cnr, year, sem)
Teaches(l[lid from Lecturer], c[cid from Course]) 
• Lecturer(L1234567, Pat, 829)
Course(C234567, GENED, 567, 2019, S2)
Teaches(L1234567, C234567)
• L1234567 name Pat . 
L7654321 name Vic .
L1234567 room 829 .
C234567 programme GENED .
C45678 programme SOFTENG .
C234567 year 2019 .
L1234567 teaches C234567 .
Sample subset 
of the triples 
generated
主键 列名 值
瓋 表名 主键 2 联合 叇
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Turning Relational  Data i nto Tri pl es
Ho w  wo uld  we model  the data i f  we  have  to u se  onl y  trip les?
• Lecturer(lid, name, room)
  Course(cid, programme, cnr, year, sem)
  Teaches(l[lid from Lecturer],  c[cid from Course])
• Lecturer(L1234567, Pat, 829)
  Course(C234567, GENED, 567, 2019, S2)
  Teaches(L1234567, C234567)
• L1234567 name Pat .  主键列名值
  L7654321 name Vic .                        Sample subset
  L1234567 room 829 .                        of the tri  pl  es
  C234567 programme GENED .                  generated
  C45678 programme SOFTENG .
  C234567 year 2019 .
  L1234567 teaches C234567 .
SE 351瓋        表名        主  键Geral d Weber's Sl ides2联合叇              5
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Turning RelationaI Data into TripIes
HO w would we mode/ the data we have 忆 use 0 y 旭 s ？
Lecturer 《 1 土 d ， name ， room)
Course (cid, progranune ， cnr ， year ， sem)
Teaches 《 工 [ 1 土 d from Lecturer] ，
c [cid from Course ] 》
Lecturer 《 L1234567 ， Pat, 82 9 》
Course 《 c234567 ， GENED ， 567 ， 2019 ， S2 》
Teac e s 《 L1234567 ， c234567 ）
LI 4 67 n
Pa
L7654321 name Vi c
L 12 3 4 5 67 room 829
c234567 programme GENE D
c45678 prograrnme SOFTENG
c234567 year 2019
LI 34567 teache s c234567
SE 351
erald Weber's SI ides
Sample SUbset
of the triples
generated
5
````

### 图片文字 OCR（en-US，待对照原页）

````text
Turning Relational Data into Triples
How would we mode/ the data if we have to use only triples?
Lecturer (lid, name, room)
Course (cid, progranune, cnr, year, sem)
Teaches (1 [lid from Lecturer] ,
c [cid from Course] )
Lecturer (L1234567, Pat, 829)
Course (C234567, GENED, 567, 2019, S2)
Teac es (L1234567, C234567)
LIZ34 67 n
L7654321 name Vic
1.1234567 room 829
C234567 programne GENED
C45678 programe SOFTENG
C234567 year 2019
Ll 34567 teaches C234567
Sample subset
of the triples
generated
SE 351
erald Weber's Slides
5
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../source/751/751%2525/DB51-GW01-QueryOpt1.pdf#page=6)

### 原始文字层

````text
SE 351 6
Expressing Types
Reserved predicate a for expressing isA relation.
• Lecturer(lid, name, room)
Course(cid, programme, cnr, year, sem)
Teaches(l[lid from Lecturer], c[cid from Course]) 
• Lecturer(L1234567, Pat, 829)
Course(C234567, GENED, 567, 2019, S2)
Teaches(L1234567, C234567)
• L1234567 name Pat . 
L1234567 a Lecturer.
L1234567 room 829 .
C234567 programme GENED .
C234567 a Course.
L1234567 teaches C234567 .
Sample subset 
of the triples 
generated
Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Expres si ng Types
Res erv ed  predicate a for ex press ing isA relation.
• Lecturer(lid, name, room)
  Course(cid, programme, cnr, year, sem)
  Teaches(l[lid from Lecturer],  c[cid from Course])
• Lecturer(L1234567, Pat, 829)
  Course(C234567, GENED, 567, 2019, S2)
  Teaches(L1234567, C234567)
• L1234567 name Pat .
  L1234567 a Lecturer.                         Sample subset
  L1234567 room 829 .                          of the tri  pl  es
  C234567 programme GENED .                    generated
  C234567 a Course.
  L1234567 teaches C234567 .
SE 351                        Geral d Weber's Sl ides                   6
````

### 图片文字 OCR（en-US，待对照原页）

````text
Expressing Types
Reserved predicate a for expressing isA relation.
Lecturer (lid, name, room)
Course (cid, programme, cnr, year, sem)
Teaches (1 [lid from Lecturer] ,
c [cid from Course] )
Lecturer (L1234567, Pat, 829)
Course (C234567, GENED, 567, 2019, S2)
Teaches (L1234567, C234567)
L1234567 name Pat
L1234567 a Lecturer.
1.1234567 room 829
C234567 programne GENED
C234567 a Course.
1.1234567 teaches C234567
Sample subset
of the triples
generated
SE 351
Gerald Weber's Slides
6
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../../source/751/751%2525/DB51-GW01-QueryOpt1.pdf#page=7)

### 原始文字层

````text
SE 351 7
Advantage of Triples: ad hoc data
Database URI: http:\\www.auckland.ac.nz\dbnu
• Lecturer(lid, name, room)
Lecturer(L1234567, Pat, 829)
Teaches(L1234567, C234567)
• L1234567 name Pat . 
L7654321 name Vic .
C45678 programme SOFTENG .
C234567 year 2019 .
L1234567 teaches C234567 .
• L1234567 email “pat@akl.ac.nz” .
L7654321 github vic_akl .
L7654321 assesses C45678
Ad-hoc added 
triples, 
no need to 
define/extend a 
relational 
schema
Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Adv antage of Tri pl es : ad hoc data
Dat abase  URI :  http:\\www.auckland.ac.nz\dbnu
• Lecturer(lid, name, room)
  Lecturer(L1234567, Pat, 829)
  Teaches(L1234567,  C234567)
• L1234567 name Pat .
  L7654321 name Vic .                           Ad-hoc added
  C45678 programme SOFTENG .                    tr iples,
  C234567 year 2019 .                           no need to
  L1234567 teaches C234567 .                    define/extend a
• L1234567 email “pat@akl.ac.nz” .              relati onal
  L7654321 github vic_akl .                     schema
  L7654321 assesses C45678
SE 351                        Geral d Weber's Sl ides                  7
````

### 图片文字 OCR（en-US，待对照原页）

````text
Advantage of Triples: ad hoc data
Database URI:
http : \\
www . auckland. ac . nz \dbnu
Lecturer (lid, name, room)
Lecturer (L1234567, Pat, 829)
Teaches (L1234567, C234567)
1.1234567 name Pat
L7654321 name Vic
C45678 programe SOFTENG
C234567 year 2019
1.1234567
1.1234567
1.7654321
1.7654321
SE 351
teaches C234567
email "pat@akl . ac . nz
github vic akl
assesses C45678
Gerald Weber's Slides
Ad-hoc added
triples,
no need to
define/extend a
relational
schema
7
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../../source/751/751%2525/DB51-GW01-QueryOpt1.pdf#page=8)

### 原始文字层

````text
SE 351 8
Advantage of Triples: ad hoc data
Database URI: http:\\www.auckland.ac.nz\dbnu
• Lecturer(lid, name, room , github, email)
Lecturer(L1234567, Pat, 829, NULL, “pat…”)
Teaches(L1234567, C234567)
• L1234567 name Pat . 
L7654321 name Vic .
C45678 programme SOFTENG .
C234567 year 2019 .
L1234567 teaches C234567 .
• L1234567 email “pat@akl.ac.nz” .
L7654321 github vic_akl .
L7654321 assesses C45678
Ad-hoc added 
triples, 
no need to 
define/extend a 
relational 
schema
Don’t need schema any 
more.
Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Adv antage of Tri pl es : ad hoc data
Dat abase  URI :  http:\\www.auckland.ac.nz\dbnu
• Lecturer(lid, name, room , github, email)
  Lecturer(L1234567, Pat, 829, NULL, “pat…”)
  Teaches(L1234567,  C234567)               Don’t  need s chema any
                                            more.
• L1234567 name Pat .
  L7654321 name Vic .                           Ad-hoc added
  C45678 programme SOFTENG .                    tr iples,
  C234567 year 2019 .                           no need to
  L1234567 teaches C234567 .                    define/extend a
• L1234567 email “pat@akl.ac.nz” .              relati onal
  L7654321 github vic_akl .                     schema
  L7654321 assesses C45678
SE 351                        Geral d Weber's Sl ides                  8
````

### 图片文字 OCR（en-US，待对照原页）

````text
Advantage of Triples: ad hoc data
Database URI:
http : \\
www . auckland. ac . nz \dbnu
Lecturer Ii
Lecturer (L1234567 ,
Teaches (L1234567 ,
1.1234567 name Pat
L7654321 name Vic
Pat, 829, NULL, "pat..." )
c234567)
C45678 programe SOFTENG
C234567 year 2019
1.1234567
1.1234567
1.7654321
1.7654321
SE 351
teaches C234567
email "pat@akl . ac . nz
github vic akl
assesses C45678
Don't need schema any
more.
Ad-hoc added
triples,
no need to
define/extend a
relational
schema
Gerald Weber's Slides
8
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../../source/751/751%2525/DB51-GW01-QueryOpt1.pdf#page=9)

### 原始文字层

````text
Triplestores and SPARQL semantics
2019 Gerald Weber's Slides 9
````

### 图片文字 OCR（en-US，待对照原页）

````text
Triplestores and SPARQL semantics
2019
Gerald Weber's Slides
9
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../source/751/751%2525/DB51-GW01-QueryOpt1.pdf#page=10)

### 原始文字层

````text
SE 351 10
Triplestores
Triplestore: a database to store and query triples such as RDF triples
• Has a single table: Triple(subject, predicate, object)
• Should be flexible for collecting data: All three columns are type String
• Can be queried with SPARQL
• L1234567 name Pat . 
L7654321 name Vic .
L1234567 room 829 .
C45678 programme SOFTENG .
C234567 year 2019 .
L1234567 teaches C234567 .
• L1234567 email “pat@akl.ac.nz” .
L7654321 github vic_akl .
L7654321 assesses C45678
SELECT ?name WHERE {
?lecturer name ?name .
?lecturer teaches ?course1 . 
?lecturer teaches ?course2 .
?course1 programme GENED .
?course2 programme 
SOFTENG .
}
semistructured
Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Tri pl estor es
Triplest ore :  a databas e to s tore and  query  triples s uc h as R DF  triples
• Has  a single t able:   Triple(subject, predicate, object)
• Should  be  flexible for c ollec ting data:    All t hree c olumns  are  type St ring
• Can be queried  with  SPARQL                                 semistructured
• L1234567 name Pat .
  L7654321 name Vic .                                    SELEC  T ?nam e WHE   RE {
  L1234567 room 829 .                                    ?lec turer nam e ?nam e .
  C45678 programme SOFTENG .                             ?lec turer teaches  ?cours e1 .
                                                         ?lec turer teaches  ?cours e2 .
  C234567 year 2019 .                                    ? c ou rs e 1  p ro gr   am m e  G  ENED   .
  L1234567 teaches C234567 .                             ?c ours e2 progr   am m e
                                                         SO FTENG  .
• L1234567 email “pat@akl.ac.nz” .}
  L7654321 github vic_akl .
  L7654321 assesses C45678
SE 351                                Geral d Weber's Sl ides                             10
````

### 图片文字 OCR（en-US，待对照原页）

````text
Triplestores
Triplestore: a database to store and query triples such as RDF triples
• Has a single table: Triple (subject, predicate, object)
• Should be flexible for collecting data: All three columns aret e Strin
• Can be queried with SPARQL
L1234567 name Pat
L7654321 name Vic
1.1234567 room 829
C45678 programe SOFTENG
C234567 year 2019
semistructured
SELECT ?name WHERE {
?lecturer name ?name .
?lecturer teaches ?coursel
?lecturer teaches ?course2
?coursel programme GENED
?course2 programme
SOFTENG
1.1234567
1.1234567
1.7654321
1.7654321
SE 351
teaches C234567
email "pat@akl . ac . nz
github vic akl
assesses C45678
Gerald Weber's Slides
10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../source/751/751%2525/DB51-GW01-QueryOpt1.pdf#page=11)

### 原始文字层

````text
SE 351 11
SPARQL
• a recursive acronym for SPARQL Protocol and RDF Query 
Language
• Idea is following “Query By Example” (QBE) [Zloof 1975]:
• Which data matches the shape of the example=query aka.
basic graph pattern ?
?lecturer name ?name .
?lecturer teaches ?course1 . 
?lecturer teaches ?course2 .
?course1 programme GENED .
?course2 programme SOFTENG .
• Triple patterns: triples with variables: 
• variables start with a question mark.
L1234567 name Pat .
L7654321 name Vic .
L1234567 room 829 .
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
SPARQL
• a recursive acronym for SPA RQL                Protocol and RDF Query
  Language
• Idea is following “ Query By Exampl  e” ( QB E) [Z loof 1975]:
• Which data m atches the shape of the exampl  e=query aka.
  basic graph pattern  ?                         L1 234 567  na me  Pat  .
  ?lecturer name ?name .                         L7 654 321  na me  Vic  .
  ?lecturer teaches ?course1 .                   L1 234 567  ro om  829  .
                                                 C2 345 67  pro gra mme  GE NED  .
  ?lecturer teaches ?course2 .                   C4 567 8 p rog ram me  SOF TEN G .
  ?course1 programme GENED .                     C2 345 67  yea r 2 019  .
  ?course2 programme SOFTENG .                   C4 567 8 y ear  20 17  .
                                                 L1 234 567  te ach es  C23 456 7 .
                                                 L1 234 567  te ach es  C45 678  .
                                                 L7 654 321  te ach es  C23 456 7 .
• Triple patt erns:  triples w ith variables:    L7 654 321  as ses ses  C4 567 8 .
• variables st art  wit h a question mark.
SE 351                             Geral d Weber's Sl ides                         11
````

### 图片文字 OCR（en-US，待对照原页）

````text
SPARQL
a recursive acronym for SPARQL Protocol and RDF Query
Language
Idea is following "Query By Example" (QBE) [Zloof 1975]:
Which data matches the shape of the example-query aka.
basic graph pattern
? lecturer name ?name
? lecturer teaches ?coursel
? lecturer teaches ?course2
?coursel progranune GENED
?course2 programme SOFTENG
Triple patterns: triples with variables:
variables start with a question mark.
1.1234567 name Pat
L7 654321 name Vic
L1234567 room 829
C234567 programe GENED
C45678 programme SOFTENG
C234567 year 2019
C45678 year 2017
L1234567
1.1234567
1.7654321
1.7654321
teaches C234567
teaches C45 678
teaches C234567
assesses C45678
SE 351
Gerald Weber's Slides
11
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../source/751/751%2525/DB51-GW01-QueryOpt1.pdf#page=12)

### 原始文字层

````text
SE 351 12
SPARQL
• a recursive acronym for SPARQL Protocol and RDF Query 
Language
• Idea is following “Query By Example” (QBE) [Zloof 1975]: 
find all matching subgraphs for basic graph pattern
•
?lecturer name ?name .
?lecturer teaches ?course1 . 
?lecturer teaches ?course2 .
?course1 programme GENED .
?course2 programme SOFTENG .
• Each Variable in basic graph pattern: 
• Single value in each matching subgraph (simply match)
L1234567 name Pat .
L7654321 name Vic .
L1234567 room 829 .
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
SPARQL
• a recursive acronym for SPA RQL                Protocol and RDF Query
  Language
• Idea is following “ Query By Exampl  e” ( QB E) [Z loof 1975]:
  find al  l matching subgraphs for basic graph pattern
•                                                L1 234 567 na me Pa t .
  ?lecturer name ?name .                         L7 654 321  na me  Vic  .
  ?lecturer teaches ?course1 .                   L1 234 567  ro om  829  .
  ?lecturer teaches ?course2 .                   C2 345 67 pr ogr amm e GE NED  .
                                                 C4 567 8 pr ogr amm e SO FTE NG  .
  ?course1 programme GENED .                     C2 345 67  yea r 2 019  .
  ?course2 programme SOFTENG .                   C4 567 8 y ear  20 17  .
                                                 L1 234 567 te ach es C2 345 67  .
                                                 L1 234 567 te ach es C4 567 8 .
• Each Variable  in  bas ic graph pattern:       L7 654 321  te ach es  C23 456 7 .
                                                 L7 654 321  as ses ses  C4 567 8 .
• Single  value in each mat ching  subgraph (sim ply      matc h)
SE 351                             Geral d Weber's Sl ides                         12
````

### 图片文字 OCR（en-US，待对照原页）

````text
SPARQL
a recursive acronym for SPARQL Protocol and RDF Query
Language
Idea is following "Query By Example" (QBE) [Zloof 1975]:
find all matching subgraphs for basic graph pattern
Olecturer
name ?
name
coursel
Olecturer
teaches ?
course2
Olecturer
teaches ?
?coursel
GENED
prograrmne
•course2
SOFTENG
programme
Each Variable in basic graph pattern:
1.1234567
Pat
name
L7 654321 name Vic
L1234567 room 829
c234567
GENED
programne
C45678
SOFTENG
progranune
C234567 year 2019
C45678 year 2017
1.1234567
teaches
C234567
1.1234567
C45678
teaches
1.7654321 teaches C234567
1.7654321 assesses C45678
Single value in each matching subgraph (simply match)
SE 351
Gerald Weber's Slides
12
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../../source/751/751%2525/DB51-GW01-QueryOpt1.pdf#page=13)

### 原始文字层

````text
SE 351 13
SPARQL
• SPARQL (a recursive acronym for SPARQL Protocol and 
RDF Query Language) 
• SQL like syntax and capabilities (join, filter, aggregate etc).
• Each match gives result row
• SELECT ?name WHERE {
?lecturer name ?name .
?lecturer teaches ?course1 . 
?lecturer teaches ?course2 .
?course1 programme GENED .
?course2 programme SOFTENG .
• }
• Result set: Pat
L1234567 name Pat .
L7654321 name Vic .
L1234567 room 829 .
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
SPARQL
• SP ARQL (a recursi  ve acronym for SPA RQL                   Protocol and
  RDF  Query Language)
• SQL like syntax and capabilities ( join, fil  ter, aggregate etc).
• Each m atch gives result row
• SELECT ?name WHERE {                          L1 234 567 na me Pa t .
  ?lecturer name ?name .                        L7 654 321  na me  Vic  .
                                                L1 234 567  ro om  829  .
  ?lecturer teaches ?course1 .                  C2 345 67 pr ogr amm e GE NED  .
  ?lecturer teaches ?course2 .                  C4 567 8 pr ogr amm e SO FTE NG  .
  ?course1 programme GENED .                    C2 345 67  yea r 2 019  .
                                                C4 567 8 y ear  20 17  .
  ?course2 programme SOFTENG .                  L1 234 567 te ach es C2 345 67  .
• }                                             L1 234 567 te ach es C4 567 8 .
                                                L7 654 321  te ach es  C23 456 7 .
• Result set:         Pa t                      L7 654 321  as ses ses  C4 567 8 .
SE 351                            Geral d Weber's Sl ides                        13
````

### 图片文字 OCR（en-US，待对照原页）

````text
SPARQL
SPARQL (a recursive acronym for SPARQL Protocol and
RDF Query Language)
SQL like syntax and capabilities (join, filter, aggregate etc).
Each match gives result row
WHERE {
• SELECT ?name
Olecturer
name ?
name
0 lecturer
teaches ?
coursel
course2
teaches ?
Olecturer
?coursel progranune GENED
?course2 programme SOFTENG
1.1234567
Pat
name
L7 654321 name Vic
L1234567 room 829
c234567
GENED
programne
C45678
SOFTENG
progranune
C234567 year 2019
C45678 year 2017
1.1234567
1.1234567
1.7654321
1.7654321
teaches
C234567
C45678
teaches
teaches C234567
assesses C45678
Result set:
SE 351
pat
Gerald Weber's Slides
13
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../../source/751/751%2525/DB51-GW01-QueryOpt1.pdf#page=14)

### 原始文字层

````text
SE 351 14
SPARQL: variable predicates
• SPARQL allows generally variables in predicate position:
• Some databases may only allow SPARQL queries with no 
variables in predicate position (est. 77% of queries)
• SELECT ?name, ?has WHERE {
?lecturer name ?name .
?lecturer teaches ?course1 . 
?lecturer ?has ?course2 .
?course1 programme GENED .
?course2 programme SOFTENG .
}
• Result set?: Pat, teaches
• ???
L1234567 name Pat .
L7654321 name Vic .
L1234567 room 829 .
C234567 programme GENED .
C45678 programme SOFTENG .
C234567 year 2019 .
C45678 year 2017 .
L1234567 teaches C234567 .
L1234567 teaches C45678 .
L7654321 teaches C234567 .
L7654321 assesses C45678 .
SPARQL has bag semantics as 
usual for languages in practice
Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
SPARQ L: vari able predi cates
• SP ARQL       allows generally variabl  es in predicate posi  ti  on:
• Som e databases m ay only allow S  PARQL queries with no
  variabl  es in predicate posi  ti  on ( est. 77% of queries)
• SELECT ?name, ?has WHERE {                      L1 234 567 na me Pa t .
  ?lecturer name ?name .                          L7 654 321  na me  Vic  .
  ?lecturer teaches ?course1 .                    L1 234 567  ro om  829  .
                                                  C2 345 67 pr ogr amm e GE NED  .
  ?lecturer ?has ?course2 .                       C4 567 8 pr ogr amm e SO FTE NG  .
  ?course1 programme GENED .                      C2 345 67  yea r 2 019  .
                                                  C4 567 8 y ear  20 17  .
  ?course2 programme SOFTENG .                    L1 234 567 te ach es C2 345 67  .
  }                                               L1 234 567 te ach es C4 567 8 .
                                                  L7 654 321  te ach es  C23 456 7 .
• Result set?:         Pat, teaches               L7 654 321  as ses ses  C4 567 8 .
•                      ???                    SPARQL  has  bag semantic s as
                                              usual f or  languages  in practic e
SE 351                              Geral d Weber's Sl ides                         14
````

### 图片文字 OCR（en-US，待对照原页）

````text
SPARQL: variable predicates
SPARQL allows generally variables in predicate position:
Some databases may only allow SPARQL queries with no
variables in predicate position (est. 77% of queries)
name, Ohas
WHERE {
• SELECT ?
Olecturer
name ?
name
teaches ?
coursel
Olecturer
Olecturer Ohas ?course2
?coursel
programme GENED
•course2
programe SOFTENG
Result set?:
SE 351
Pat, teaches
1.1234567
Pat
name
L7 654321 name Vic
1.1234567 room 829
c234567
GENED
progranune
C45678
SOFTENG
programne
C234567 year 2019
C45678 year 2017
121234567
teaches
C234567
1.1234567 teaches C45678
1.7654321 teaches C234567
1.7654321 assesses C45678
SPARQL has bag semantics as
usual for languages in practice
Gerald Weber's Slides
14
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../../source/751/751%2525/DB51-GW01-QueryOpt1.pdf#page=15)

### 原始文字层

````text
SE 351 15
SPARQL: variable predicates
• SPARQL allows generally variables in predicate position:
• Some databases may only allow SPARQL queries with no 
variables in predicate position (est. 77% of queries).
• SELECT ?name, ?has WHERE {
?lecturer name ?name .
?lecturer teaches ?course1 . 
?lecturer ?has ?course2 .
?course1 programme GENED .
?course2 programme SOFTENG .
• }
• Result set: Pat, teaches;
• Vic, assesses
L1234567 name Pat .
L7654321 name Vic .
L1234567 room 829 .
C234567 programme GENED .
C45678 programme SOFTENG .
C234567 year 2019 .
C45678 year 2017 .
L1234567 teaches C234567 . 
L1234567 teaches C45678 .
L7654321 teaches C234567 .
L7654321 assesses C45678 .
SPARQL has bag semantics as 
usual for languages in practice
Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
SPARQ L: vari able predi cates
• SP ARQL       allows generally variabl  es in predicate posi  ti  on:
• Som e databases m ay only allow S  PARQL queries with no
  variabl  es in predicate posi  ti  on ( est. 77% of queries).
• SELECT ?name, ?has WHERE {                      L1 234 567  na me  Pat  .
  ?lecturer name ?name .                          L7 654 321 na me  Vic  .
  ?lecturer teaches ?course1 .                    L1 234 567  ro om  829  .
                                                  C2 345 67 pr ogr amm e GE NED  .
  ?lecturer ?has ?course2 .                       C4 567 8 pr ogr amm e SO FTE NG  .
  ?course1 programme GENED .                      C2 345 67  yea r 2 019  .
                                                  C4 567 8 y ear  20 17  .
  ?course2 programme SOFTENG .                    L1 234 567  te ach es  C23 456 7 .
• }                                               L1 234 567  te ach es  C45 678  .
                                                  L7 654 321 te ach es C2 345 67  .
• Result set:          Pat, teaches;              L7 654 321 as ses ses C4 567 8 .
•                      Vi  c, assesses        SPARQL  has  bag semantic s as
                                              usual f or  languages  in practic e
SE 351                              Geral d Weber's Sl ides                         15
````

### 图片文字 OCR（en-US，待对照原页）

````text
SPARQL: variable predicates
SPARQL allows generally variables in predicate position:
Some databases may only allow SPARQL queries with no
variables in predicate position (est. 77% of queries).
name, Ohas
WHERE {
• SELECT ?
Olecturer
name ?
name
teaches ?
coursel
Olecturer
Olecturer Ohas ?course2
?coursel
programme GENED
•course2
programe SOFTENG
1.1234567 name Pat
1.7654321
name Vic
1.1234567 room 829
c234567
GENED
progranune
C45678
SOFTENG
programne
C234567 year 2019
C45678 year 2017
L1234567 teaches C234567
1.1234567 teaches C45678
1.7654321
C234567
teaches
1.7654321 assesses C45678
Result set:
SE 351
pat,
Vic,
teaches;
SPARQL has bag semantics as
assesses
usual for languages in practice
Gerald Weber's Slides
15
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../../source/751/751%2525/DB51-GW01-QueryOpt1.pdf#page=16)

### 原始文字层

````text
SE 351 16
SPARQL tip: think in terms of matches 
• Projection by SELECT is an afterthought.
• SELECT ?name, ?has WHERE {
?lecturer name ?name .
?lecturer teaches ?course1 . 
?lecturer ?has ?course2 .
?course1 programme GENED .
?course2 programme SOFTENG .
• }
• Result set: Pat, teaches;
• Vic, assesses
L7654321 name Vic .
C234567 programme GENED .
C45678 programme SOFTENG .
L7654321 teaches C234567 .
L7654321 assesses C45678 .
L1234567 name Pat .
C234567 programme GENED .
C45678 programme SOFTENG .
L1234567 teaches C234567 .
L1234567 teaches C45678 .
Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
SPARQ L tip: thi nk  in terms of matc hes
• Projec tion by  SELECT  is  an  af terthought .
• SELECT ?name, ?has WHERE {                    L1 234 567 na me Pa t .
  ?lecturer name ?name .                        C2 345 67 pr ogr amm e GE NED  .
  ?lecturer teaches ?course1 .                  C4 567 8 pr ogr amm e SO FTE NG  .
                                                L1 234 567 te ach es C2 345 67  .
  ?lecturer ?has ?course2 .                     L1 234 567 te ach es C4 567 8 .
  ?course1 programme GENED .                    L7 654 321 na me  Vic  .
  ?course2 programme SOFTENG .                  C2 345 67 pr ogr amm e GE NED  .
                                                C4 567 8 pr ogr amm e SO FTE NG  .
• }                                             L7 654 321 te ach es C2 345 67  .
                                                L7 654 321 as ses ses C4 567 8 .
• Result set:          Pat, teaches;
•                      Vi  c, assesses
SE 351                             Geral d Weber's Sl ides                         16
````

### 图片文字 OCR（en-US，待对照原页）

````text
SPARQL tip: think in terms of matches
• Projection by SELECT is an afterthought.
SELECT ?name, ?has WHERE {
Olecturer
name ?
name
coursel
Olecturer
teaches ?
Olecturer Ohas ?course2
•coursel
prograrmne GENED
•course2
programme SOFTENG
1.1234567
Pat
name
c234567
GENED
prograrmne
C45678
SOFTENG
progranune
1.1234567
C234567
teaches
1.1234567 teaches C45678
m 654321
name Vic
c234567
GENED
progranune
C45678
SOFTENG
prograrmne
1.7654321
c234567
teaches
1.7654321 assesses C45678
Result set:
SE 351
pat,
Vic,
teaches;
Gerald Weber's Slides
16
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../../source/751/751%2525/DB51-GW01-QueryOpt1.pdf#page=17)

### 原始文字层

````text
SE 351 17
SPARQL: filters
• Filters remove matches that evaluate the filter to false.
• Filters allow common Boolean expressions
• SELECT ?name, ?has WHERE {
?lecturer name ?name .
?lecturer teaches ?course1 . 
?lecturer ?has ?course2 .
?lecturer room ?room .
?course1 programme GENED .
?course2 programme SOFTENG .
• FILTER(?room<600)
• }
• Result Set: Vic, assesses
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
SPARQ L: fil ters
• F ilters r emove matches that eval  uate the filter to false.
• F ilters allow com mon Boolean expressi  ons
• SELECT ?name, ?has WHERE {
  ?lecturer name ?name .                         L1 234 567  na me  Pat  .
  ?lecturer teaches ?course1 .                   L7 654 321 na me  Vic  .
  ?lecturer ?has ?course2 .                      L1 234 567  ro om  829  .
  ?lecturer room ?room .                         L7 654 321 ro om 56 7 .
                                                 C2 345 67 pr ogr amm e GE NED  .
  ?course1 programme GENED .                     C4 567 8 pr ogr amm e SO FTE NG  .
  ?course2 programme SOFTENG .                   C2 345 67  yea r 2 019  .
                                                 C4 567 8 y ear  20 17  .
• FILTER(?room<600)                              L1 234 567  te ach es  C23 456 7 .
                                                 L1 234 567  te ach es  C45 678  .
• }                                              L7 654 321 te ach es C2 345 67  .
                                                 L7 654 321 as ses ses C4 567 8 .
• Result Set:  V  ic, assesses
SE 351                             Geral d Weber's Sl ides                         17
````

### 图片文字 OCR（en-US，待对照原页）

````text
SPARQL: filters
Filters remove matches that evaluate the filter to false.
Filters allow common Boolean expressions
name, Ohas
WHERE {
• SELECT ?
Olecturer
name ?
name
coursel
Olecturer
teaches ?
Olecturer Ohas ?course2
Olecturer
room
?coursel
programe GENED
•course2
programe SOFTENG
<600)
• FILTER ( ?
room
Result Set: Vic, assesses
1.1234567
1.7654321
1.1234567
1.7654321
name Pat
name Vic
room 829
567
room
C234567
GENED
programne
C45678
SOFTENG
programne
C234567 year 2019
C45678 year 2017
1.1234567 teaches C234567
1.1234567 teaches C45678
1.7654321 teaches C234567
L7654321 assesses C45678
SE 351
Gerald Weber's Slides
17
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 18 页

[查看此页](../../../../source/751/751%2525/DB51-GW01-QueryOpt1.pdf#page=18)

### 原始文字层

````text
CS 351, CS 751 18
SPARQL: filters
• Filter expressions allowed:
• Comparison operators: =, !=, >, <, ...
• Logical Operators: !, &&, ||
• Arithmetical operators +, -, *, / 
• Parentheses: allowing nested expressions
• FILTER NOT EXISTS { ?person foaf:name ?name }
Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
SPARQ L: fil ters
• F ilter expressions allowed:
• Com parison operators: =, != , > , <, ...
• Logical Operators: !, && , |  |
• Arithm etical operators +,          -, *, /
• Parentheses: al  lowing nested expressions
• FILTER NOT EXISTS { ?person foaf:name ?name }
CS 351,  CS 751                     Geral d Weber's Sl ides                         18
````

### 图片文字 OCR（en-US，待对照原页）

````text
SPARQL: filters
Filter expressions allowed:
Comparison operators. .- , >, <
Logical Operators: !, &&, II
Arithmetical operators +, -
Parentheses: allowing nested expressions
• FILTER NOT EXISTS { ?person foaf:name ?name }
cs 351, cs 751
Gerald Weber's Slides
18
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 19 页

[查看此页](../../../../source/751/751%2525/DB51-GW01-QueryOpt1.pdf#page=19)

### 原始文字层

````text
CS 351, CS 751 19
Globally Unique Identifiers as URIs
Database URI: http:\\www.auckland.ac.nz\dbnu
System URI: http:\\www.nusoft.com\dbnu
• Lecturer(lid, Name, Room)
Lecturer(L1234567, Pat, 829)
Use URIs to make identifiers globally unique:
• www.auckland.ac.nz\dbnu\L1234567 
www.nusoft.com\dbnu\teaches
Use aliases to avoid repeating long prefixes:
• PREFIX uoa: <http:\\www.auckland.ac.nz\dbnu\>
• PREFIX dbnu: <http:\\www.nusoft.com\dbnu\>
• uoa:L1234567 dbnu:name Pat .
• uoa:L1234567 dbnu:teaches uoa:C234567 .
Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Gl oball y Uni que Identi fiers as URIs
Dat abase  URI :  http:\\www.auckland.ac.nz\dbnu
Sys tem U RI:   http:\\www.nusoft.com\dbnu
• Lecturer(lid, Name, Room)
  Lecturer(L1234567, Pat, 829)
Us e UR Is  to make  identif iers  globally  unique:
• www.auckland.ac.nz\dbnu\L1234567
        www.nusoft.com\dbnu\teaches
Us e aliases t o avoid repeat ing  long prefix es :
• PREFIX uoa: <http:\\www.auckland.ac.nz\dbnu\>
• PREFIX dbnu: <http:\\www.nusoft.com\dbnu\>
• uoa:L1234567   dbnu:name Pat .
• uoa:L1234567 dbnu:teaches uoa:C234567 .
CS 351,  CS 751                 Geral d Weber's Sl ides                     19
````

### 图片文字 OCR（en-US，待对照原页）

````text
Globally Unique Identifiers as URIs
Database URI:
http : \\
www . auckland. ac . nz \dbnu
System URI:
http : \\
www . nusoft . com\dbnu
Lecturer (lid, Name, Room)
Lecturer (L1234567, Pat, 829)
Use URIs to make identifiers globally unique:
• www. auckland. ac .
www . nusoft . com\dbnu\ teaches
Use aliases to avoid repeating long prefixes:
http : \\
www . auckland . ac . nz \dbnu\>
• PREFIX uoa: <
• PREFIX dbnu:
uoa:L1234567
uoa:L1234567
cs 351, cs 751
<http : \ \
www . nusoft . com\dbnu\>
dbnu : name Pat
dbnu : teaches uoa : C234567
Gerald Weber's Slides
19
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 20 页

[查看此页](../../../../source/751/751%2525/DB51-GW01-QueryOpt1.pdf#page=20)

### 原始文字层

````text
SE 351 20
Example SPARQL Query with prefixes
• A SPARQL query with prefixes:
• PREFIX uoa: <http:\\www.auckland.ac.nz\dbnu\db>
PREFIX dbnu: <http:\\www.nusoft.com\dbnu\>
• SELECT ?name, ?has WHERE {
?lecturer dbnu:name ?name .
?lecturer dbnu:teaches ?course1 . 
?lecturer ?has ?course2 .
?course1 dbnu:programme
• dbnu:GENED .
?course2 dbnu:programme
• uoa:SOFTENG .
• }
L1234567 dbnu:name Pat .
L7654321 dbnu:name Vic .
L1234567 dbnu:room 829 .
C234567 dbnu:programme dbnu:GENED .
C45678 dbnu:programme uoa:SOFTENG .
C43434 dbnu:programme uoa:MATH .
C234567 dbnu:year 2019 .
C45678 dbnu:year 2017 .
L1234567 dbnu:teaches C234567 .
L1234567 dbnu:teaches C45678 .
L7654321 dbnu:teaches C234567 .
L7654321 dbnu:assesses C45678 .
Gerald Weber's Slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Example SPARQL Query  wi th prefixes
• A  SPA RQL q uery with  pr efi xes      :
• PR EFI X uo a:  <ht tp:\\ww w.a uck lan d.a c.n z\db nu\db >
  PR EFI X db nu:  <ht tp:\\ww w.n uso ft. com\db nu\>
• SE LEC T ?na me,  ?ha s WH ERE  {
  ?le ctu rer db nu: nam e ?na me .
  ?le ctu rer db nu: tea che s ?co urs e1 .
  ?le ctu rer ?ha s ?co urs e2 .
  ?co urs e1 db nu: pro gra mme           L1234567    dbnu:name    Pat .
                                          L7654321 dbnu:name Vic .
•         db nu: GEN ED .                 L1234567 dbnu:room 829 .
  ?co urs e2 db nu: pro gra mme           C234567 dbnu:programme        dbnu:GENED .
                                          C45678   dbnu:programme      uoa:SOFTENG .
•           uo a:S OFT ENG .              C43434   dbnu:programme      uoa:MATH .
                                          C234567 dbnu:year 2019 .
• }                                       C45678 dbnu:year 2017 .
                                          L1234567    dbnu:teaches     C234567 .
                                          L1234567    dbnu:teaches     C45678 .
                                          L7654321 dbnu:teaches C234567 .
                                          L7654321 dbnu:assesses C45678 .
SE 351                               Geral d Weber's Sl ides                           20
````

### 图片文字 OCR（en-US，待对照原页）

````text
Example SPARQL Query with prefixes
• A SPARQL query with prefixes:
http: \\
www. auckland. ac . n z \dbnu\db>
PREFIX uoa: <
http: \\
www.nusoft. com\dbnu\>
PREFIX dbnu: <
name, Ohas
WHERE {
SELECT ?
Olecturer
dbnu : name ?
name
dbnu : teaches ?coursel
Olecturer
Olecturer ?has ?course2
?coursel
dbnu : programne
dbnu : GENED
•course2
dbnu : progranune
uoa : SOFTENG
L1234567
dbnu : name
Pat
L7654321 dbnu : name Vic
1.1234567 dbnu: room 829
C234567
dbnu : programme
dbnu : GENED
C45678
dbnu : programme
uoa : SOFTENG
C43434
dbnu : programme
uoa :MATH
C234567 dbnu:year 2019
C45678 dbnu: year 2017
L1234567
C234567
dbnu : teaches
L1234567
teaches C45678
dbnu :
L7654321 dbnu: teaches C234567
L7654321 dbnu:
assesses C45678
Gerald Weber's Slides
20
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 21 页

[查看此页](../../../../source/751/751%2525/DB51-GW01-QueryOpt1.pdf#page=21)

### 原始文字层

````text
SE 351 21
SPARQL: Naïve Query evaluation
1. Find all candidate matches for the graph pattern.
2. Evaluate filters, reject candidate match if false.
• SELECT ?name, ?has WHERE {
?lecturer name ?name .
?lecturer teaches ?course1 . 
?lecturer ?has ?course2 .
?lecturer room ?room .
?course1 programme GENED .
?course2 programme SOFTENG .
• FILTER(?room<600)
• }
3. Result Set: projection by 
SELECT clause.
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
SPARQ L:  Naïve Quer y ev al uati on
1.  F ind all candidate matches for the graph pattern.
2.  Evaluate fi  lters, reject candidate m atch if false.
• SELECT ?name, ?has WHERE {
  ?lecturer name ?name .                        L1 234 567  na me  Pat  .
  ?lecturer teaches ?course1 .                  L7 654 321 na me  Vic  .
  ?lecturer ?has ?course2 .                     L1 234 567  ro om  829  .
  ?lecturer room ?room .                        L7 654 321 ro om 56 7 .
                                                C2 345 67 pr ogr amm e GE NED  .
  ?course1 programme GENED .                    C4 567 8 pr ogr amm e SO FTE NG  .
  ?course2 programme SOFTENG .                  C2 345 67  yea r 2 019  .
                                                C4 567 8 y ear  20 17  .
• FILTER(?room<600)                             L1 234 567  te ach es  C23 456 7 .
                                                L1 234 567  te ach es  C45 678  .
• }                                             L7 654 321 te ach es C2 345 67  .
                                                L7 654 321 as ses ses C4 567 8 .
3.  Result Set: projection by
    SE LECT  cl  ause.
SE 351                            Geral d Weber's Sl ides                        21
````

### 图片文字 OCR（en-US，待对照原页）

````text
SPARQL: Näive Query evaluation
1. Find all candidate matches for the graph pattern.
2. Evaluate filters, reject candidate match if false.
name, Ohas
WHERE {
• SELECT ?
Olecturer
name ?
name
coursel
Olecturer
teaches ?
Olecturer Ohas ?course2
Olecturer
room
?coursel
programe GENED
•course2
programe SOFTENG
<600)
• FILTER ( ?
room
3. Result Set: projection by
1.1234567 name
1.7654321
name
1.1234567 room
1.7654321
room
Pat
Vic
829
567
C234567
GENED
programne
C45678
SOFTENG
programne
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
SELECT clause.
SE 351
Gerald Weber's Slides
21
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 22 页

[查看此页](../../../../source/751/751%2525/DB51-GW01-QueryOpt1.pdf#page=22)

### 原始文字层

````text
Summary
Triplestores
• Relational data may be stored in triples.
• In triplestores, ad-hoc predicates can be used to add more 
data
• Can be queried by SPARQL
SPARQL
• Is a query-by example approach.
• Allows to query with variable predicates: 
∘ a semistructured feature that goes beyond SQL
2019 Gerald Weber's Slides 22
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Summary
T riplestor es
• Relational data may be stored i  n triples.
• In triplestores, ad-hoc predicates can be used to add more
  data
• Can be queri  ed by SPA RQL
SP ARQL
• Is a query-by example approach.
• Al  lows to query with vari  able predicates:
    ∘ a semistructured feature that goes beyond SQL
20   19                          Geral d Weber's Sl ides                      22
````

### 图片文字 OCR（en-US，待对照原页）

````text
Summary
Triplestores
Relational data may be stored in triples.
In triplestores, ad-hoc predicates can be used to add more
data
Can be queried by SPARQL
SPARQL
Is a query-by example approach.
Allows to query with variable predicates:
o a semistructured feature that goes beyond SQL
2019
Gerald Weber's Slides
22
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

