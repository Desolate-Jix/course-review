# 1253_Data_Cleaning.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI752/source/752/752（1）/1253_Data_Cleaning.pdf`
- [打开原文件](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf)
- 原文件 SHA-256：`9e4e793697348f3d107c1a8c5cd63b43712e0257ced3f789b1bbca21817dde22`
- 文件索引：F199；PDF 总页数：34
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=1)

### 原始文字层

````text
1
Fundamental Problems
COMPCSI 752: Big Data Management
University of Auckland
Slides are collected and edited from 
http://webdam.inria.fr/Jorge/index9213.html
Credit to Ninh Pham for these slides
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Fundamental Problems
                      COMPCSI 752: Big Data Management
                                  Univer  sity of Auc  kland
                              Slides are collected and edited from
                        http://webdam.inr ia.fr/Jorge/index9213.html
                                 Credit to Ninh Pham for these slides
                                                                                            1
````

### 图片文字 OCR（en-US，待对照原页）

````text
Fundamental Problems
COMPCSI 752: Big Data Management
University of Auckland
Slides are collected and edited from
http : / / webdam. inria.fr/ Jorge / index9213. html
Credit to Ninh Pham for these slides
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=2)

### 原始文字层

````text
Outline
2
 Web crawling
 Near-duplicate detection
 Web search
 PageRank
 Data cleaning
 tfidf representation
 Similarity join
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Outline
Web crawling
Near-duplicate detection
Web search
PageRank
Data cleaning
tfidf representation
Similarity join
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=3)

### 原始文字层

````text
Data cleaning
3
 Near-duplicate detection:
 How to representWeb content efficiently for near duplicate removal?
 Context: each webpage is a text document
近似重复处理
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Data cleaning
． Near-duplicate detection:
确
确
确
Web content efficiently for near duplicate rem oval ？
H ow to
represent
Context ： each webpage is text document
The jaguar is a N ew WorId mammal of the FeIidae family.
Jaguar has designed four n ew engines.
FO r Jaguar, Atari was keen tO use a 68K family device.
The Jacksonville Jaguars are a professional US football team.
Mac OS X Jaguar is available at a price of US $ 1 99 for Apple
n ew "family pack
One such ruling family tO incorporate the jaguar intO their name
is Jaguar Paw.
lt is a big cat.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Data cleaning
Near-duplicate detection:
d3
d7
How to represent Web content efficiently for near duplicate removal?
Context: each webpage is text document
The jaguar is a New World mammal of the Felidae family.
Jaguar has designed four new engines.
For Jaguar, Atari was keen to use a 68K family device.
The Jacksonville Jaguars are a professional US football team.
Mac OS X Jaguar is available at a price of US $199 for Apple's
new "family pack".
One such ruling family to incorporate the jaguar into their name
is Jaguar Paw.
It is a big cat.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=4)

### 原始文字层

````text
Text preprocessing
4
 Text preprocessing steps:
 Number of optional steps: 
o Tokenization
o Stemming
o Stop word removal
 Highly depends on the application
 Highly depends on the document language (illustrated with English)
o
nion 标记化
问干捉取
停用词删除
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Text preprocessing
． preprocessin steps ：
Number of optional steps ：
Tokenization
O
Stemming
Stop word removal
H ighly depends on the application
H ighly depends on th e document langu ag e (illustrated with English)
````

### 图片文字 OCR（en-US，待对照原页）

````text
Text preprocessing
Tex preprocessin steps:
Number of optional steps:
Tokenization
o
Stemming
o
Stop word removal
O
Highly depends on the application
Highly depends on the document language (illustrated with English)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=5)

### 原始文字层

````text
Tokenization
5
 Principle:
 Separate text into tokens (words)
 Characteristics: Not so easy!
 In some languages (Chinese, Japanese), words not separated by whitespace
 Deal consistently with acronyms, numbers, units, URLs, emails…
 Compound words: hostname, host-name and host name. Break into two tokens 
or regroup them as one token? Lexicon and linguistic analysis needed!
 Usually, remove punctuation and normalize case
Cfc
no 道
遮 一
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Tokenization
． Principle:
token
(words)
Separate text int
． Characteristics ：
NOt SO easy.
ln some langua es （ Chine
apanese) ， words not separated by whitespace
Deal consistently with acronyms ， numbers ， units ， URLs, emails ·
Compound words ： hostname, host-name and 為 0 豆 name. Break intO tWO tokens
or regroup them as one token? Lexicon an d linguistic analysis needed!
usually, remove punctuation an d normalize case
````

### 图片文字 OCR（en-US，待对照原页）

````text
Tokenization
e Principle:
token
(words)
Separate text int
Characteristics:
Not so easy!
apanese), words not separated by whitespace
etitJ
Deal consistently with acronyms, numbers, units, URLs, emails...
Compound words: hostname, host-name and host name. Break into two tokens
or regroup them as one token? Lexicon and linguistic analysis needed!
usually, remove punctuation and normalize case
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=6)

### 原始文字层

````text
Tokenization: Example
6
小鸟 标点
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
山
确
Tokenization: Example
thel jaguar2 iS3 a4 new world6 mamma17 0f8 the feIidae10 family
Jaguar1 has designed f0 u r4 n eW5 engines
forl jaguar2 atari3 was4 keen5 t06 use7 a 68k9 famiIY10 device
thel jacksonville2 jaguars3 are4 a professiona16 us f00tba118 team
macl 0S2 X3 jaguar4 iS5 available at7 a price9 0f10 usll $ 199
12
f0r13 apple S14 n ew 5 familY16 pack
17
onel such2 ruIing3 family t05 incorporate the7 jaguar8 intO
their10 namell iS12 Jaguar13 paw
1 4
itl is a big cat5
````

### 图片文字 OCR（en-US，待对照原页）

````text
d3
Tokenization: Example
thel jaguar2 iS3 a4 new5 world6 mamma17 of8 the9 felidae10 family
jaguarl has2 designed3 four4 new5 engines6
forl jaguar2 atari3 was4 keem t06 use7 aa 68k9 familY10 devicel
thel jacksonville2 jaguars3 are4 a5 professiona16 us7 footba118 team9
mac1 os2 x3 jaguar4 iS5 available6 at7 a8 price9 oflo usi $199
12
for13 apple'su new15 familY16 pack
17
onei such2 ruling3 familY4 t05 incorporate6 the7 jaguar8 int09
their10 namell iSi2 jaguar13 paw
iti iS2 a3 big4 cat5
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=7)

### 原始文字层

````text
Stemming
7
 Principle:
 Merge different forms of same word, or closely related words, into single 
stem
 Characteristics:
 Not in all applications!
 Useful for retrieving documents containing geese when searching for goose
 Various degrees of stemming
 Possibility of building different indexes, with different stemming
词对 踙 形式 S ing
goose geese
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Stemming 讠 談
一 穹
． Principle:
Merge differe nt forms of same word ， or closely related words ， into single
stem
． Characteristics ：
Not in all applications ！
Useful for retrieving documents containing geese when searching for 90 ose
Various degrees
Of stemming
Possibility of buil ding different indexes, with different stemming
````

### 图片文字 OCR（en-US，待对照原页）

````text
Stemming
Principle:
Merge different forms of same word, or closely related words, into single
stem
Characteristics:
Not in all applications!
Useful for retrieving documents containing geese when searching for goose
Various degrees of stemming
Possibility of building different indexes, with different stemming
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=8)

### 原始文字层

````text
Stemming: Example
8
i
````

### 图片文字 OCR（en-US，待对照原页）

````text
d3
Stemming: Example
thel jaguar2 iS3 a4 new5 world6 mamma17 of8 the9 felidae10 family
Jaguarl has2 designed3 four4 new5 engines6
forl jaguar2 atari3 was4 keem t06 use7 a8 68k9 familY10 devicel
thel jacksonville2 jaguars3 are4 a5 professiona16 us7 footba118 team9
macl os2 x3 jaguar4 iS5 available6 at7 a8 price9 oflo usi $199
12
for13 apple'su new15 familY16 pack
17
onei such2 ruling3 familY4 t05 incorporate6 the7 jaguar8 int09
their10 namell iSi2 jaguar13 paw
14
iti iS2 a3 big4 cat5
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=9)

### 原始文字层

````text
Stemming: Example
9
https://www.geeksforgeeks.org/python-stemming-words-with-nltk/
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Stemming: Example
        https://www.geeksforgeeks.org/python-stemming-words-with-nltk/
                                                                                9
````

### 图片文字 OCR（en-US，待对照原页）

````text
d3
Stemming: Example
thel jaguar
2 be3 4
a new5 world6 mamma17 of8 the9 felidae10 family
11
jaguarl have2 design3 four4 new
5 engine6
forl jaguar2 atari
3 be4
keem t06 use7 a8 68k9 familY10 devicell
thel jacksonville2 jaguar3 be4 5
a professiona16 us7 footba118 team9
available6 at7 a8 price9 oflo usil $199
mac1 os2 x3 jaguar
12
for13 apple14 new15 familY16 pack
17
onei such
2 rule3
familY4 t05 incorporate6 the7 jaguar8 int09
their10 name
11 be12
jaguar13 paw
14
iti be2 3
a big4 cat5
https : / / www.geeksforgeeks.org/python- stemming-words-with-nltk/
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=10)

### 原始文字层

````text
Stop word removal
10
 Principle:
 Remove uninformative words from documents, in particular to lower the 
cost of storing the index
 Examples:
 determiners: a, the, this, etc.
 function verbs: be, have, make, etc.
 conjunctions: that, and, etc.
 etc.
没有信息的 词
-
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
StO p WO rd remova 《
． Principle:
Remove uninformative
words from documents ， in p ar ti cular tO lower the
cost Of storing the index
． Examples
determiners ： a, the ， thi s ， etc.
function verbs ： be, have ， m ake ， etc ·
conjunctions ： that, and ， etc.
etc.
10
````

### 图片文字 OCR（en-US，待对照原页）

````text
Stop word removal
Principle:
Remove uninformative
words from documents, in particular to lower the
cost of storing the index
Examples
determiners: a, the, this, etc.
function verbs: be, have, make, etc.
conjunctions: that, and, etc.
etc.
10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=11)

### 原始文字层

````text
Before removing stop words
11
````

### 图片文字 OCR（en-US，待对照原页）

````text
d3
Before removing stop words
thel jaguar
2 be3 4
a new5 world6 mamma17 of8 the9 felidae10 family
11
jaguarl have2 design3 four4 new
5 engine6
forl jaguar2 atari
3 be4
keem t06 use7 a8 68k9 familY10 devicell
thel jacksonville2 jaguar3 be4 5
a professiona16 us7 footba118 team9
available6 at7 a8 price9 oflo usil $199
mac1 os2 x3 jaguar
12
for13 apple14 new15 familY16 pack
17
onei such
2 rule3
familY4 t05 incorporate6 the7 jaguar8 int09
their10 name
11 be12
jaguar13 paw
14
iti be2 3
a big4 cat5
11
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=12)

### 原始文字层

````text
Stop word removal: Example
12
删除
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
确
确
确
研
StO p WO rd removal: Example
Jaguar2 new world6 mamma17 felidae10 family
Jaguar1 design four4 n ewro engine
Jaguar2 atari3 keen5 68k9 familY10 device
jacksonville jaguar3 professiona16 us f00tba118 team
macl 0S2 X3 jaguar4 available6 price9 usll $ 19912 apple
14
n ew 5 familY16 pack
17
onel such2 rule family incorporate6 jaguar8 their10 name
Jaguar13 paw
1 4
big4 cat5
12
````

### 图片文字 OCR（en-US，待对照原页）

````text
d3
Stop word removal: Example
jaguar2 new5 world6 mamma17 felidae10 family
jaguarl design3 four4 new5 engine6
jaguar2 atari3 keem 68k9 familyo devicel
jacksonville2 jaguar3 professiona16 us7 footba118 team9
mac1 os2 x3 jaguar4 available6 price9 usu $19912 apple
14
new15 familY16 pack
17
onei such2 rule3 familY4 incorporate6 jaguar8 their10 namel
jaguar13 paw
14
big4 cat5
12
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=13)

### 原始文字层

````text
Word occurrence information
13
 Text preprocessing result:
 Each text document is represented as a set of terms (tokens) or shingles
 Define similarity measure:
 Use set similarity measure (Jaccard similarity, containment similarity,…) 
to define the similarity between documents
 But… we have ignored the word occurrence information
 D1 = “Rose is a rose is a rose is a rose” → {rose}
 D2 has 1000 words where “coronavirus” appears 2 times
 D3 has 1000 words where “coronavirus” appears 30 times
how many
time
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Word occurrence information
Text preprocessing result:
Each text document is represented as a set of terms (tokens) or shingles
Define similarity measure:
use set similarity measure (Jaccard similarity, containment similarity, ... )
to define the similarity between documents
we have ignored the word occurrence information
But..
181m/ Tl&e.
Dl = "Rose is a rose is a rose is a rose" * {rose
D2 has 1000 words where "coronavirus" appears 2 times
D3 has 1000 words where "coronavirus" appears 30 times
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=14)

### 原始文字层

````text
Weighted terms occurrences
14
 Relevance can be computed by giving a weight to term 
occurrences
 Terms occurring frequently in a given document: more relevant
 The term frequency tf(t, d) is the number of occurrences of a term t in a 
document d, divided by the total number of terms in d (normalization) 
where nt’,d is the number of occurrences of any term t’ in document d
o­i
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Weighted terms occurrences
Relevance can be computed by giving a weight
to term
occurrences
Terms occurring frequently in a given document
relevant
: more
The term frequency tf(t, d)
mber of occurrences of a term t in a
is t
document d, divided byth otal numbe of terms in d (normalization)
nt,d
tf(t, d)
nt',d
where nt, d is the number of occurrences of any term t' in document d
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=15)

### 原始文字层

````text
Weighted terms occurrences
15
 Relevance can be computed by giving a weight to term 
occurrences
 Terms occurring rarely in the document collection as a whole: 
more informative
 The inverse document frequency idf(t) is obtained from the 
division of the total number of documents by the number of 
documents where t occurs:
 
where the logarithmic base is 2
- Ǘtg
一 文档点数
至少出现一次的文档老
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Weighted terms occurrences
Relevance c an be computed by giving a we i ght
to term
occurrences
rarely
in the document collection
as a WhOle ：
occurring
informative
more
The inve r s e ocument frequency df(t)
is obtained from the
division Of the tOtal numb e r O ocuments by the number Of
documents where t OCCurs ：
idf(t)
= log
where the logarithmic base is 2
15
````

### 图片文字 OCR（en-US，待对照原页）

````text
Weighted terms occurrences
Relevance can be computed by giving a weight
to term
occurrences
Terms occurring rarely
in the document collection as a whole:
informative
more
The inverse ocument frequency df(t)
is obtained from the
division of the total number o ocuments by the number of
documents where t occurs:
IDI
idf(t)
log e D nt,d' >
where the logarithmic base is 2
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=16)

### 原始文字层

````text
tfidf weighting
16
 Relevance can be computed by giving a weight to term 
occurrences
 Term Frequency-Inverse Document Frequency tfidf(t, d) of the term t
in document d is the combination of tf(t, d) and idf(t)
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
tfidf weighting
Relevance can be computed by giving a weight
to term
occurrences
Term Frequency-Inverse Document Frequency tfidf(t, d)
of the term t
in document d is the combination of tf(t, d) and idf(t)
tfidf(t, d)
nt,d
D
nt,d
log
nt',d
number of occurrences of t in d
set of all documents
16
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=17)

### 原始文字层

````text
 Each document in the collection is represented as a set of 
terms with its tfidf weight
 D1 = {(family, 0.13), (jaguar, 0.04), (new, 0.2), (world, 0.47)}
 D2 = {(jaguar, 0.4), (new, 0.24)}
 D3 = {(jaguar, 0.4), (football, 0.47), (us, 0.3)}
 Define the inner product as a similarity measure
 <D1, D2> = 0.04 * 0.4 + 0.2 * 0.24 = 0.064
 <D1, D3> = 0.04 * 0.4 = 0.016
tfidf representation
17
ۦ, ۧ෍ = t in both S and T
tfidf t, S ∗ tfidf(t, T)
_
-
相同点相乘是
如
與
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
tfidf representation
Each document in the collection is represented as a set of
terms with its tfidf weight
． DI = { (family, 0 · 13 ） ， (j aguar, 0 · 04 ） ， (new, 0 · 2 ） ， (world ， 0 · 47 ） }
(j aguar, 0 · 4 ） ， (new 0 · 24 ）
， (football ， 0 · 47 ） ， ()s ， 0 · 3 ） }
Define the
inner product as a similarity mea
tfidf(), S) * tfidf(), T)
both S and T
<DI, D2> = 0 · 04 * 0 · 4 + 0 ． 2 * 0 · 24 = 0 · 064
<DI, D3> = 0 · 04 * 0 ． 4 = 0 ． 016
17
````

### 图片文字 OCR（en-US，待对照原页）

````text
tfidf representation
Each document in the collection is represented as a set of
terms with its tfidf weight
Dl = { (family, 0.13), (jaguar, 0.04), (new, 0.2), (world, 0.47)}
(jaguar, 0.4), (new 0.24)
(football, 0.47), (us, 0.3)}
Define the
inner product as a similarity mea e
tfidf(t, S) * tfidf(t, T)
t In both
S and T
0.04 * 0.4 + 0.2 * 0.24 - 0.064
<DI,
0.04 * 0.4
<DI,
= 0.016
17
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 18 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=18)

### 原始文字层

````text
Outline
18
 Web crawling
 Near-duplicate detection
 Web search
 PageRank
 Data cleaning
 tfidf representation
 Similarity join
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Outline
Web crawling
Near-duplicate detection
Web search
PageRank
Data cleaning
tfidf representation
Similarity join
18
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 19 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=19)

### 原始文字层

````text
Data cleaning – The heavy task?
19
一
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Data cleaning _ The heavy tas k?
What ， s the least enjoyable part Of data science?
5 ％
． Building training sets: 10 ％
10 ％
． Cleaning and 0 了 g 忉 ng d 忆 ： 5 / ％
． C011ecting da 忆 sets: 21 ％
57 ％
Mining d 了 patterns: 3 ％
0
21 ％
． Refining algorithms: 4 ％
． Other 巧 ％
lmage Credits: whatsthebigdata ℃ om
19
````

### 图片文字 OCR（en-US，待对照原页）

````text
Data cleaning -
21
The heavy task?
What's the least enjoyable part of data science?
0
0
0
Building training sets: 10%
Cleaning and organizing data: 57%
Collecting data sets: 21%
Mining data for patterns: 3%
Refining algorithms: 4%
Other:
Image Credits: whatsthebigdata.com
19
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 20 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=20)

### 原始文字层

````text
20
````

### 图片文字 OCR（en-US，待对照原页）

````text
Example
Name
Jack Lemmon
Harrison Ford
Tom Hanks
Table R
Addr
Maple St.
CulverBlvd
Main St.
Phone
430-871-8294
292-918-2913
2340762-
1234
Name
Ton Hanks
Kevin Spacey
Jack Lemon
Table S
Addr
Main Street
Frost Blvd
Maple Street
Find records from different datasets that
could be the same entity.
Phone
234-162-1234
928-184-2813
430-817-8294
20
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 21 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=21)

### 原始文字层

````text
Similarity join
21
 Similarity join:
 Given a set of n documents X = {x1, x2, …, xn} in Rd and define the 
similarity measure by their inner product
 Given a threshold t, finding all pairs x, y in Xs.t. sim(x, y) ≥ t
 Application:
 Plagiarism detection, collaborative filtering
 Near-duplicate detection, record linkage (entity resolution)
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Similarity join
Similarity join:
, xn} in Rd and define the
Given a set of n documents X = {x x
similarity measure by their inner product
d
sim(x,y) x •Y Exjyj
Given a threshold t, finding all pairs x, y in X s.t. sim(x, y) 2 t
Application:
Pla iarism detection, collaborative filtering
Near-duplicate detection, record linkage (entity resolution)
21
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 22 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=22)

### 原始文字层

````text
tfidf representation
22
 Collection:
 D1 = {(jaguar, 0.4), (new, 0.2), (family, 0.13), (world, 0.47)}
 D2 = {(jaguar, 0.4), (new, 0.24)}
 D3 = {(jaguar, 0.4), (football, 0.47), (us, 0.3)}
 Dim: {(jaguar, 1), (new, 2), (family, 3), (world, 4), (football, 5), (us, 6)}
 High dimensional vector representations:
 Dim: {(jaguar, 1), (new, 2), (family, 3), (world, 4), (football, 5), (us, 6)}
 D1 = {0.4 , 0.2 , 0.13 , 0.47 , 0 , 0 }
 D2 = {0.4 , 0.24 , 0 , 0 , 0 , 0 }
 D3 = {0.4 , 0 , 0 , 0 , 0.47 , 0.3 }
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
tfidf representation
e Collection:
(jaguar, 0.4), (new, 0.2), (family, 0.13), (world, 0.47)}
(jaguar, 0.4), (new, 0.24)
(football, 0.47), (us, 0.3)}
(jaguar, 0.4)
Dim: {
(jaguar, 1), (new, 2), (family, 3), (world, 4), (football, 5), (us, 6)}
High dimensional vector representations
Dim: {
(jaguar, 1), (new, 2), (family, 3), (world, 4), (football, 5), (us, 6)}
Dl = {0.4
D2 = {0.4
D3 = {0.4
0.2
0.13
O. 24
0
0.47
0
0.47
0.3 }
22
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 23 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=23)

### 原始文字层

````text
Sequential solutions
23
 Naïve algorithm:
 O(n2): too expensive for all practical purposes
 Exploit data sparsity:
 Observation: In most of data sets, vectors in X are sparse
 Any two vectors x, y whose non-zero coordinates do not intersect: 
sim(x, y) = 0 < t
 Only check two vectors x, y whose non-zero coordinates intersect with 
at least one coordinate (how to check efficiently?)
㓘
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Sequential solutions
Naive algorithm:
O(n2): too expensive for all practical purposes
Exploit data sparsity:
Observation: In most of data sets, vectors in X are sparse
Any two vectors x, y whose non-zero coordinates do not intersect:
sim(x, y) = O < t
Onl check two vectors x, y whose non- ero coordinates intersect with
at least one coordinate (how to c ec efficient y.
23
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 24 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=24)

### 原始文字层

````text
Inverted index construction
24
 Inverted index:
 For each term, create the list of documents where this term occurs
family (d1, .13), (d3, .13), (d6, .08), (d5, .07)
football (d4, .47)
jaguar (d1, .04), (d2, .04), (d3, .04), (d4,.04), (d6, .04), (d5, .02)
new (d2, .24), (d1, .20), (d5, .10)
rule (d6, .28)
us (d4, .30), (d5, .15)
world (d1, .47)
…
Term Posting list containing documents
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Term
famil
football
ja uar
new
rule
us
world
Inverted index construction
Inverted index:
For each term, create the list of documents where this term occurs
(d6, .28)
Posting list containing documents
( (14 ,
( (14 ,
dl, .13 , d3, .13 , d6, .08 , (15, .07
.04), (d3,
.20), (ds, .10)
.47)
.04), (d2,
.24), (d 1,
.30), (ds, .15)
.47)
.04), .04), ((16, .04), (ds,
.02)
24
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 25 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=25)

### 原始文字层

````text
Inverted Index construction
25
 Small scale:
 Disk storage, with memory mapping techniques
 Secondary index (called vocabulary) for offset of each term in main index 
- usually a B-tree
 Large scale:
 Distributed on a cluster of machines
 Hashing gives the machine responsible for a given term
 Updating the index is costly, so only batch operations (not 
one-by-one addition of term occurrences)
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Inverted Index construction
Small scale:
Disk storage, with memory mapping techniques
Secondary index (called vocabulary) for offset of each term in main index
- usually a -tree
Large scale:
Distributed on a cluster of machines
Hashing gives the machine responsible for a given term
Updating the index is costly, so only batch operations (not
one-by-one addition of term occurrences)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 26 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=26)

### 原始文字层

````text
Inverted index solution
26
family (d1, .13), (d3, .13), (d6, .08), (d5, .07)
football (d4, .47)
jaguar (d1, .04), (d2, .04), (d3, .04), (d4,.04), (d6, .04), (d5, .02)
new (d2, .24), (d1, .20), (d5, .10)
rule (d6, .28)
us (d4, .30), (d5, .15)
world (d1, .47)
…
Term Documents
family: (d1, d3), (d1, d6), (d1, d5), (d3, d6), (d3, d5), (d6, d5)
…
new: (d2, d1), (d2, d5), (d1, d5)
…
Candidate 
pairs
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Inver     ted index  solution
Ter   m                                      Documents
family      (d1, .13), (d3, .13), (d6, .08), (d5, .07)
football   (d4, .47)
jaguar      (d1, .04), (d2, .04), (d3, .04), (d4,.04), (d6, .04), (d5, .02)
new         (d2, .24), (d1, .20), (d5, .10)
r  ule      (d6, .28)
us          (d4, .30), (d5, .15)
world       (d1, .47)
…
    family: (d1, d3), (d1, d6), (d1, d5), (d3, d6), (d3, d5), (d6, d5)          Candidate
    …                                                                              pair s
    new: (d2, d1), (d2, d5), (d1, d5)
    …                                                                                   26
````

### 图片文字 OCR（en-US，待对照原页）

````text
Inverted index solution
Term
famil
football
ja uar
new
rule
us
world
dl, .13 , d3, .13 , d6, .08 , ds, .07
.04), (d3,
.20), (ds, .10)
.04), (d5,
.02)
(d6,
.47)
.04), (d2,
.24), (d 1,
.28)
.30), (ds, .15)
.47)
Documents
.04), .04), (d6,
family: (d 1, d3), (d 1, d6), (d 1, d5), (d3, d6), (d3, d5), (d6, d5)
new:
Candidate
pairs
26
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 27 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=27)

### 原始文字层

````text
Prefix-filtering optimization
27
 Observation:
 We do not want to index all documents for each term. Can we reduce the 
index size?
 Do not want to compute sim(x, y) if
 sim(x, y) = x1y1 + x2y2 + … + xkyk + xk+1yk+1 + … + xdyd < t
 Define vector m containing the maximum value of each 
dimension/term from X
 x1m1 + x2m2 + … + xkmk + xk+1mk+1 + … + xdmd
< t
≥ t
Maximum contribution 
from dimensions 1 to k
all's 取每个词的
最大 IF 坼 值
做向量
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Prefix-fiItering optimization
． Observation:
We do not want to index all documents for each term · C an we reduce the
index size?
DO not want tO compute sim(), y) if
sim(), y) = XIYI + X2Y2 + ． 一 + XkYk + Xk+1Yk+1
+ · 一 + XdYd < t
Define vector m containing t
alue of each
maxlmum
dimension/ term from X
x ml + x m + · 一 + x mk + x m +
k+l k+ 1
< t
contribution
from dimensions 1 to k
+ x m
《 丈 TF 刁 仟
27
````

### 图片文字 OCR（en-US，待对照原页）

````text
Prefix-filtering optimization
Observation:
We do not want to index all documents for each term. Can we reduce the
index size?
Do not want to compute sim(x, y) if
sim(x, y) = + + + XkYk + Xk+1Yk+1
+ XdYd < t
Define vector m containing t
alue of each
maximum
dimension/term from X
x 1 m 1 + + ... + Xkmk+ x m +
Maximum contribution
from dimensions 1 to k
+ x dlT1d
27
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 28 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=28)

### 原始文字层

````text
Prefix-filtering optimization
28
 Observation:
 We do not want to index all documents for each term. Can we reduce the 
index size?
 Do not want to compute sim(x, y) if
 sim(x, y) = x1y1 + x2y2 + … + xkyk + xk+1yk+1 +… + xdyd < t
 Define vector m containing the maximum value for each 
dimension/term from X
 x1m1 + x2m2 + … + xkmk + xk+1mk+1 + … + xdmd
< t
≥ t
Maximum contribution 
from dimensions 1 to k
If no intersection between 
x and y on dimensions k+1
to d then sim(x, y) < t
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Prefix-filtering optimization
Observation:
We do not want to index all documents for each term. Can we reduce the
index size?
Do not want to compute sim(x, y) if
sim(x, y) = + + + XkYk + Xk+1Yk+1
+ XdYd < t
Define vector m containing the
maximum value for each
dimension/term from X
Xlrnl + X2n-12 + ... + Xkmk
Maximum contribution
from dimensions 1 to k
X m + ... + x dill d
If no intersection between
x and y on dimensions k +1
to d then sim(x, y) < t
28
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 29 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=29)

### 原始文字层

````text
Prefix-filtering optimization
29
 Observation:
 We do not want to index all documents for each term. Can we reduce the 
index size?
 Prefix-filtering strategy:
 Consider the max vector m s.t. mj = maxx in X xj
 For each x in X, find p(x) the largest dimension s.t. σj≤p(x) 𝐱𝐣
𝐦𝐣 < t
 For each x in X, define signature S(x) the coordinates after p(x)
 S(x) = xj | j > p(x)
 Idea: If S(x) and S(y) do not intersect, then sim(x, y) < t (why?)
 We can ignore the prefix of the vectors and index only the signature
football
occurey.no
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Prefix-filtering optimization
Observation:
We do not want to index all documents for each term. Can we reduce the
index size?
oaure oh(-z
Prefix-filtering strategy:
Consider the max vector m s. t. m. = max
x in X j
For each x in X, find
the
largest
dimension s.t.
jsp(x) j
For each x in X, define signature S(x)
the coordinates after
xj I j > p(x) )
S(x) ¯
'J Idea: If S(x) and S(y) do not intersect, then sim(x, y) < t (why?)
ignore the prefix of the vectors and index onl the signature
we can
29
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 30 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=30)

### 原始文字层

````text
Prefix-filtering example
30
 Data set and set up:
 D1 = {(jaguar, 0.4), (new, 0.2), (family, 0.13), (world, 0.47)}
 D2 = {(jaguar, 0.4), (new, 0.24)}
 D3 = {(jaguar, 0.4), (football, 0.47), (us, 0.3)}
 m = {(jaguar, 0.4), (new, 0.24), (family, 0.13), (world, 0.47), 
 (football, 0.47), (us, 0.3)} 
 Dim : {(jaguar, 1), (new, 2), (family, 3), (world, 4), (football, 5), (us, 6)}
 Threshold t = 0.2:
 p(D1) = 1:
o 0.4 * 0.4 = 0.16 < t
o 0.4 * 0.4 + 0.2 * 0.24 = 0.208 > t
 S(D1) = {(new, 0.2), (family, 0.13), (world, 0.47)}
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Prefix-filtering example
Data set and set up:
(jaguar, 0.4), (new, 0.2), (family, 0.13), (world, 0.47)}
(jaguar, 0.4), (new, 0.24)
(football, 0.47), (us, 0.3)}
(jaguar, 0.4)
(jaguar, 0.4), (new, 0.24), (family, 0.13), (world, 0.47),
(football, 0.47), (us, 0.3)}
Dim : {
(jaguar, 1), (new, 2), (family, 3), (world, 4), (football, 5), (us, 6)}
Threshold t = 0.2
0.4 * 0.4 = 0.16 < t
0.4 * 0.4 + 0.2 * 0.24 = 0.208 > t
(family, 0.13), (world, 0.47)}
(new, 0.2)
30
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 31 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=31)

### 原始文字层

````text
Prefix-filtering example
31
 Data set and set up:
 D1 = {(jaguar, 0.4), (new, 0.2), (family, 0.13), (world, 0.47)}
 D2 = {(jaguar, 0.4), (new, 0.24)}
 D3 = {(jaguar, 0.4), (football, 0.47), (us, 0.3)}
 m = {(jaguar, 0.4), (new, 0.24), (family, 0.13), (world, 0.47), 
 (football, 0.47), (us, 0.3)} 
 Dim : {(jaguar, 1), (new, 2), (family, 3), (world, 4), (football, 5), (us, 6)}
 Threshold t = 0.2:
 p(D2) = 1:
o 0.4 * 0.4 = 0.16 < t
o 0.4 * 0.4 + 0.24 * 0.24= 0.2176 > t
 S(D2) = {(new, 0.24)}
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Prefix-filtering example
Data set and set up:
(jaguar, 0.4), (new, 0.2), (family, 0.13), (world, 0.47)}
(jaguar, 0.4), (new, 0.24)
(football, 0.47), (us, 0.3)}
(jaguar, 0.4)
(jaguar, 0.4), (new, 0.24), (family, 0.13), (world, 0.47),
(football, 0.47), (us, 0.3)}
Dim : {
(jaguar, 1), (new, 2), (family, 3), (world, 4), (football, 5), (us, 6)}
Threshold t = 0.2
p(D2) = 1.
0.4 * 0.4 = 0.16 < t
0.4 * 0.4 + 0.24 * 0.24= 0.2176 > t
S(D2) = {
new, 0.24)
31
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 32 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=32)

### 原始文字层

````text
Prefix-filtering example
32
 Data set and set up:
 D1 = {(jaguar, 0.4), (new, 0.2), (family, 0.13), (world, 0.47)}
 D2 = {(jaguar, 0.4), (new, 0.24)}
 D3 = {(jaguar, 0.4), (football, 0.47), (us, 0.3)}
 m = {(jaguar, 0.4), (new, 0.24), (family, 0.13), (world, 0.47), 
 (football, 0.47), (us, 0.3)}
 Dim : {(jaguar, 1), (new, 2), (family, 3), (world, 4), (football, 5), (us, 6)}
 Threshold t = 0.2:
 p(D3) = 4:
o 0.4 * 0.4 = 0.16 < t
o 0.4 * 0.4 + 0.47 * 0.47 = 0.3809 > t
 S(D3) = {(football, 0.47), (us, 0.3)}
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Prefix-filtering example
Data set and set up:
(jaguar, 0.4), (new, 0.2), (family, 0.13), (world, 0.47)}
(jaguar, 0.4), (new, 0.24)
(football, 0.47), (us, 0.3)}
(jaguar, 0.4)
(jaguar, 0.4), (new, 0.24), (family, 0.13), (world, 0.47),
(football, 0.47), (us, 0.3)}
Dim : {
(jaguar, 1), (new, 2), (family, 3), (world, 4), (football, 5), (us, 6)}
Threshold t = 0.2
p(D3) = 4:
0.4 * 0.4 = 0.16 < t
0.4 * 0.4 + 0.47 * 0.47 = 0.3809 > t
S(D3) = {(football, 0.47), (us, 0.3)}
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 33 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=33)

### 原始文字层

````text
Prefix-filtering example
33
 Threshold t = 0.2:
 S(D1) = {(new, 0.2), (family, 0.13), (world, 0.47)}
 S(D2) = {(new, 0.24)}
 S(D3) = {(football, 0.47), (us, 0.3)}
 Build the inverted index on signatures:
 Candidate pair: (D1, D2)
 Pruning pairs: (D1, D3) and (D2, D3) due to no intersection
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Prefix-filtering example
Threshold t = 0.2
(new, 0.2), (family, 0.13), (world, 0.47)}
S(D2) = {
new, 0.24)}
S(D3) = { (football, 0.47), (us, 0.3)}
Build the inverted index on signatures:
Candidate pair:
(Dl, D3) and (D2, D3) due to no intersection
Pruning pairs :
33
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 34 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf#page=34)

### 原始文字层

````text
Homework
34
 Implement the tfidf representations, inverted index and 
prefix-filtering algorithms with Python to solve the near￾duplicate detection
 Use the KOS blog entries data set from 
https://archive.ics.uci.edu/ml/datasets/Bag+of+Words
 This data set consists of 3430 documents, each represented as a set of 
keywords. The total number of keywords of the corpus is 6960
 Finding all similar pair of documents whose inner products with tfidf
representations are at least t = 0.5
 Hint: if there are many similar pairs, you can increase the threshold t so 
that we have fewer candidate pairs
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Homework
Implement the tfidf representations, inverted index and
prefix-filtering algorithms with Python to solve the near-
duplicate detection
use the
KOS blog entries
data set from
https://archive.ics.uci.edu/ml/datasets/Bag+ of + Words
This data set consists of 3430 documents, each represented as a set of
keywords. The total number of keywords of the corpus is 6960
Finding all similar pair of documents whose inner products with tfidf
representations are at least t = 0.5
if there are many similar pairs, you can increase the threshold t so
Hint:
that we have fewer candidate pairs
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

