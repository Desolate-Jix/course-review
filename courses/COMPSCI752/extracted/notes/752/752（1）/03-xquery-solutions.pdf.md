# 03-xquery-solutions.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI752/notes/original/752/752（1）/03-xquery-solutions.pdf`
- [打开原文件](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/03-xquery-solutions.pdf)
- 原文件 SHA-256：`fbeeb9bafc68a1dccfe992417be016dbe45479e558ddcf076e5c2b6667c36533`
- 文件索引：F195；PDF 总页数：12
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/03-xquery-solutions.pdf#page=1)

### 原始文字层

````text
COMPSCI 752
Big Data Management
Strategic Exercise 3 - Solutions
XQuery
Application domain. Consider the following XML document:
<?xml v e r s i o n =”1.0” enc odin g=”UTF￾8”?>
<bib>
<book year=”1994”>
<title >TCP/ IP I l l u s t r a t e d </title >
<author>
<last >Stevens </last >
<first >W.</first >
</author>
<publisher >Addison￾Wesley</publisher >
<price >65.95</price >
</book>
<book year=”1992”>
<title >Advanced Programming in the Unix environment </title >
<author>
<last >Stevens </last >
<first >W.</first >
</author>
<publisher >Addison￾Wesley</publisher >
<price >65.95</price >
</book>
<book year=”2000”>
<title >Data on the Web</title >
<author>
<last >Abiteboul </last >
<first >Serge </first >
</author>
<author>
<last >Buneman</last >
<first >Peter </first >
</author>
<author>
<last >Suciu </last >
<first >Dan</first >
</author>
<publisher >Morgan Kaufmann Publi she r s </publisher >
<price >39.95</price >
</book>
<book year=”1999”>
<title >The Economics o f Technology and Content f o r D i g i t a l TV</title >
<editor >
<last >Gerbarg</last >
<first >Darcy</first >
<affiliation >CITI</affiliation >
</editor >
<publisher >Kluwer Academic Publishers </publisher >
<price >129.95</price >
</book>
</bib>
1
````

### 图片文字 OCR（en-US，待对照原页）

````text
COMPSCI 752
Big Data Management
Strategic Exercise 3 - Solutions
XQuery
Application domain. Consider the following XML document:
<?xml version 1.0" encoding="UTF—8"?>
< bib >
<book year —"
< title >TP/IP Illustrated < / title >
< last Stevens < / last >
< first < // first >
< / author >
< p u b I is her < / pu blisher>
< price
<book year —"
< title >Advanced Programming in the Unix environment < / title >
< last Stevens < [last >
< first < // first >
< / author >
< p u b I is her < / pu blisher>
< price
<book year="
2000" >
< title >Data on the
< last >Abiteboul < [last >
< first
< / author >
< I as t I ast >
< first
< / author >
< last >Suciu < [last >
< first first >
< / author >
< publisher >Morgan Kaufmann Publishers < / publisher >
< price
<book year —"
< title >The Economics of Technology and Content for
< last >Gerbarg < / I ast >
< first
< affiliation affiliation >
< / editor >
< publisher >Kluwer Academic Publishers < / publisher >
< price > 129.95<1 price >
1
Digital
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/03-xquery-solutions.pdf#page=2)

### 原始文字层

````text
Exercise 1 - XPath and Xquery.
Write the query “Return the names of all authors of books” in
a. XPath
b. XQuery
c. and show the result when evaluated on the document above.
Solution.
a. /bib/book/author
b. l e t $d := doc ( b i b . xml ”)
return <result >{$d/bib /book/ author}</result >
c. <?xml v e r si o n =”1.0” enc odin g=”UTF￾8”?>
<result >
<author>
<last >Stevens </last >
<first >W.</first >
</author>
<author>
<last >Stevens </last >
<first >W.</first >
</author>
<author>
<last >Abiteboul </last >
<first >Serge </first >
</author>
<author>
<last >Buneman</last >
<first >Peter </first >
</author>
<author>
<last >Suciu</last >
<first >Dan</first >
</author>
</result >
2
on
xquery 中 变童一点赋值
不能修改
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Exercise 1 - XPath and Xquery.
Write the query Return the names 0f all authors of books ” in
XPat h
XQuery
and show the result when evaluated on t he document above.
Solution.
bib/book/ author
b.
I e $d
r e t tl r n
doc b i b ． xml ” ）
t >{$d/bib/book/author}</result>
< ？ xml v e r s i O n = 1.0 ” encoding= UTF—8 ” ？ >
< r e s u I t >
<author>
< I a s t >Stevens </last>
< f i r s t >W.</first>
</author>
<author>
< I a s t >Stevens </last>
< f i r s t >W.</first>
</author>
<author>
< I a s t >Abiteboul </last >
< f i r s t >Serge </first>
</author>
<author>
< I a s t >Buneman</l as t >
< f i r s t >Peter </first>
</author>
<author>
< I a s t >Suciu</last>
< f i r s t >Dan</first >
</author>
</result>
2
````

### 图片文字 OCR（en-US，待对照原页）

````text
Exercise 1 - XPath and Xquery.
Write the query "Return the names of all authors of books" in
a.
b.
c.
XPath
XQuery
and show the result when evaluated on the document above.
Solution.
a.
b.
c.
bib / book/ author
return
doc bib .xml " )
t bib / book/
< ? xml version =" 1.0" ? >
< result >
<author>
< last >Stevens < / last >
< first >W.</first>
< / author >
<author>
< last >Stevens < / last >
< first >W.</first>
< / author >
<author>
< last >Abiteboul < / last >
< first >Serge < / first >
< / author >
<author>
< I ast ast >
< first >Peter < / first >
< / author >
<author>
< last
< first first >
< / author >
< / result >
2
*quea
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/03-xquery-solutions.pdf#page=3)

### 原始文字层

````text
Exercise 2 - XPath and Xquery.
Write the query “Return the titles of all books published before 1997” in
a. XPath
b. XQuery
c. and show the result when evaluated on the document above.
Solution.
a. /bib/book [ @year < ”1997”]/ title
b. for $bk in doc ( b i b . xml )/ bib/book
where $bk/@year < ”1997”
return $bk/ t i t l e
c. <?xml v e r si o n =”1.0” enc odin g=”UTF￾8”?>
<title >TCP/ IP I l l u s t r a t e d </title >
<title >Advanced Programming in the Unix environment</title >
3
````

### 图片文字 OCR（en-US，待对照原页）

````text
Exercise 2 - XPath and Xquery.
Write the query "Return the titles of all books published before 1997" in
a.
b.
c.
XPath
XQuery
and show the result when evaluated on the document above.
Solution.
a.
b.
c.
bib/ book [@year < " title
for $bk in doc( bib .xml ) / bib/ book
where $bk/@year < " 1997"
return $bk/title
< ? xml version =" 1.0" ? >
Illustrated
< title >Advanced Programming in the Unix environment</title>
3
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/03-xquery-solutions.pdf#page=4)

### 原始文字层

````text
Exercise 3 - Construction.
a. Write in XQuery ‘Return year and title of all books published before 1997’
b. and show the result when evaluated on the document above.
Solution.
a. for $bk in doc ( b i b . xml )/ bib/book
where $bk/@year < ”1997”
return <book>{ $bk/@year , $bk/ t i t l e }</book>
b. <?xml v e r si o n =”1.0” enc odin g=”UTF￾8”?>
<book year=”1994”>
<title >TCP/ IP I l l u s t r a t e d </title >
</book>
<book year=”1992”>
<title >Advanced Programming in the Unix environment</title >
</book>
4
````

### 图片文字 OCR（en-US，待对照原页）

````text
Exercise 3 - Construction.
a.
b.
Write in XQuery 'Return year and title of all books published before 1997'
and show the result when evaluated on the document above.
Solution.
a.
b.
for $bk in doc( bib .xml ) / bib/ book
where $bk/@year < " 1997"
return <book>{ $bk/@year, $bk/ title }</book>
< ? xml version =" 1.0" ? >
<book year="
Illustrated
</book>
<book year="
1992" >
< title >Advanced Programming in the Unix environment</title>
</book>
4
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/03-xquery-solutions.pdf#page=5)

### 原始文字层

````text
Exercise 4 - Grouping.
a. Write in XQuery ‘Return titles for each author’
b. and show the result when evaluated on the document above.
Solution.
a. <result >
{
l e t $d:= doc (” bib . xml ”)
for $l in distinct ￾values ( $d// author / l a s t )
return
<author name=”{ $l }”>
{ $d/bib /book [ author / l a s t= $l ]/ t i t l e }
</author>
}
</result >
b. <?xml v e r si o n =”1.0” enc odin g=”UTF￾8”?>
<result >
<au th o r name=”S t e v e n s”>
<title >TCP/ IP I l l u s t r a t e d </title >
<title >Advanced Programming in the Unix environment</title >
</author>
<au th o r name=”Abi teb oul”>
<title >Data on the Web</title >
</author>
<au th o r name=”Buneman”>
<title >Data on the Web</title >
</author>
<au th o r name=”Suciu”>
<title >Data on the Web</title >
</author>
</result >
5
````

### 图片文字 OCR（en-US，待对照原页）

````text
Exercise 4 - Grouping.
a.
b.
Write in XQuery 'Return titles for each author'
and show the result when evaluated on the document above.
Solution.
O Patan machQ O 3.10 O CSS 3.0 @
1 for Sa in distinct-values(f/
2 return
(result
6
doc (" bib . xml " )
a.
b.
< result >
let $d:
for $1 in distinct —values ($d//author/last)
return
<author name=" {$1
{ $d/bib/book[author/last=
$1]/ title
< / author >
< / result >
< ? xml version =" 1.0" ? >
< result >
<author name=" Stevens" >
Illustrated
< title >Advanced Programming in the Unix environment</title>
< / author >
<author name=" Abiteboul">
< title >Data on the Web</title>
< / author >
<author name=" Buneman" >
< title >Data on the Web</title>
< / author >
<author name=" Suciu">
< title >Data on the Web</title>
< / author >
< / result >
5
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/03-xquery-solutions.pdf#page=6)

### 原始文字层

````text
Exercise 5 - Aggregation.
a. Write in XQuery ‘Return the average length of authors’ surnames for each book’
b. and show the result when evaluated on the document above.
Solution.
a. f o r $b in doc ( bib . xml )// book
l e t $a:=avg ( $b/ author / string ￾length ( last/text ()))
return
<book>
{$b/ t i t l e }
<avg surname>{$a}</avg surname>
</book>
b. <?xml v e r si o n =”1.0” enc odin g=”UTF￾8”?>
<book>
<title >TCP/ IP I l l u s t r a t e d </title >
<avg surname>7</avg surname>
</book>
<book>
<title >Advanced Programming in the Unix environment</title >
<avg surname>7</avg surname>
</book>
<book>
<title >Data on the Web</title >
<avg surname>7</avg surname>
</book>
<book>
<title >The Economics o f Technology and Content f o r D i g i t a l TV</title >
<avg surname/>
</book>
6
````

### 图片文字 OCR（en-US，待对照原页）

````text
Exercise 5 - Aggregation.
a.
b.
Write in XQuery 'Return the average length of authors' surnames for each book'
and show the result when evaluated on the document above.
Solution.
a.
b.
for $b in doc(bib .xml)// book
let $a:=avg($b/author/string—length(last/text ()))
return
<book>
{8b/ title}
<avg_surname>{$a}</avg_surname>
</book>
< ? xml version =" 1.0" ? >
<book>
Illustrated
<avg-surname>7</avg-surname>
</book>
<book>
< title >Advanced Programming in the Unix environment</title>
<avg-surname>7</avg-surname>
</book>
<book>
< title >Data on the Web</title>
<avg_surname>7</avg_surname>
</book>
<book>
< title >The Economics of Technology and Content for
<avg-surname/>
</book>
6
Digital
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/03-xquery-solutions.pdf#page=7)

### 原始文字层

````text
Exercise 6 - Joins.
a. Write in XQuery ‘Return pairs of books that share authors of the same name’.
b. and show the result when evaluated on the document above.
Solution.
a. for $b1 in //book
for $b2 in //book
where $b1/ t i t l e != $b2/ t i t l e and $b1/ author = $b2/ author
return
<books>
{$b1/ t i t l e }
{$b2/ t i t l e }
</books>
b. <?xml v e r si o n =”1.0” enc odin g=”UTF￾8”?>
<books>
<title >TCP/ IP I l l u s t r a t e d </title >
<title >Advanced Programming in the Unix environment</title >
</books>
<books>
<title >Advanced Programming in the Unix environment</title >
<title >TCP/ IP I l l u s t r a t e d </title >
</books>
7
````

### 图片文字 OCR（en-US，待对照原页）

````text
Exercise 6 - Joins.
a.
b.
Write in XQuery 'Return pairs of books that share authors of the same name'.
and show the result when evaluated on the document above.
Solution.
a.
b.
for $bl in
/ / book
for $b2 in
/ / book
where $bl/title
return
< books>
$b2/title and $bl/author =
$b2/ author
{$bl/title}
{$b2/title}
</books>
< ? xml version =" 1.0" ? >
<books>
Illustrated
< title >Advanced Programming in the Unix environment</title>
</books>
<books>
< title >Advanced Programming in the Unix environment</title>
Illustrated
</books>
7
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/03-xquery-solutions.pdf#page=8)

### 原始文字层

````text
Exercise 7 - Quantification.
a. Write in XQuery ‘Return the books where no author has a first name with less than three
characters’
b. and show the result when evaluated on the document above.
Solution.
a. f o r $b in //book
where every $a in $b/ author / f i r s t s a t i s f i e s
string ￾length ( $a)>2
return
<book>
{$b/ t i t l e }
</book>
b. <?xml v e r si o n =”1.0” enc odin g=”UTF￾8”?>
<book>
<title >Data on the Web</title >
</book>
<book>
<title >The Economics o f Technology and Content f o r D i g i t a l TV</title >
</book>
8
````

### 图片文字 OCR（en-US，待对照原页）

````text
Exercise 7 - Quantification.
a.
b.
Write in XQuery 'Return the books where no author has a first name with less than three
characters '
and show the result when evaluated on the document above.
Solution.
a.
b.
for $b in
/ / book
where every $a in 8b/ author/ first
satisfies
string—length ($a)>2
return
<book>
{8b/ title}
</book>
< ? xml version =" 1.0" ? >
<book>
< title >Data on the Web</title>
</book>
<book>
< title >The Economics of Technology and Content
</book>
8
for
Digital
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/03-xquery-solutions.pdf#page=9)

### 原始文字层

````text
Exercise 8 - Grouping and Aggregation.
a. Write in XQuery ‘Return titles for each author, provided there are at least two.’
b. and show the result when evaluated on the document above.
Solution.
a. <result >
{
l e t $d:= doc (” bib . xml ”)
for $l in distinct ￾values ( $d// author / l a s t )
where count ( distinct ￾v alue s ( $d//book [ author / l a s t= $l ] / t i t l e ))>=2
return
<author name=”{ $l }”>
{ $d/bib /book [ author / l a s t= $l ]/ t i t l e }
</author>
}
</result >
b. <?xml v e r si o n =”1.0” enc odin g=”UTF￾8”?>
<result >
<au th o r name=”S t e v e n s”>
<title >TCP/ IP I l l u s t r a t e d </title >
<title >Advanced Programming in the Unix environment</title >
</author>
</result >
9
````

### 图片文字 OCR（en-US，待对照原页）

````text
Exercise 8 - Grouping and Aggregation.
a.
b.
Write in XQuery 'Return titles for each author, provided there are at least two.'
and show the result when evaluated on the document above.
Solution.
a.
b.
< result >
let $d:
doc (" bib . xml " )
for $1 in distinct —values ($d//author/last)
where count (distinct —values ($d//book [author/last=
return
<author name=" {$1
{ $d/bib/book[author/last=
$1]/ title
< / author >
< / result >
< ? xml version =" 1.0" ? >
< result >
<author name=" Stevens" >
Illustrated
$1]/ title)) >
< title >Advanced Programming in the Unix environment</title>
< / author >
< / result >
9
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/03-xquery-solutions.pdf#page=10)

### 原始文字层

````text
Exercise 9 - Interpreting and evaluating XQueries.
<bib>
{
f o r $b in doc (” bib . xml ”)/ bib /book
where $b/ publisher = ”Addison￾Wesley” and $b [ @year> 1992]
return
<book ye a r=”{ $b/@year }”>
{$b/ t i t l e }
</book>
}
</bib>
a. What does the XQuery query above do?
b. What is the result when evaluating the XQuery on the document above?
Solution.
a. Return the title and year of publication for each book published by Addition-Wesley after
1992.
b. <?xml v e r si o n =”1.0” enc odin g=”UTF￾8”?>
<bib>
<book year=”1994”>
<title >TCP/ IP I l l u s t r a t e d </title >
</book>
</bib>
10
````

### 图片文字 OCR（en-US，待对照原页）

````text
Exercise 9 -
<bib>
Interpreting and evaluating XQueries.
for $b in doc (" bib . xml" ) / bib/ book
where $b/publisher —
Addison—Wesley"
return
<book year="{ $b/@year }">
{8b/ title}
</book>
</bib>
and $b [@year> 1992]
a.
b.
What does the XQuery query above do?
What is the result when evaluating the XQuery on the document above?
Solution.
a.
b.
Return the title and year of publication for each book published by Addition-Wesley after
1992.
< ? xml version =" 1.0" ? >
<bib>
<book year="
Illustrated
</book>
</bib>
10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/03-xquery-solutions.pdf#page=11)

### 原始文字层

````text
Exercise 10 - Interpreting and evaluating XQueries.
<results >
{
f o r $b in doc (” bib . xml ”)/ bib /book ,
$t in $b/ ti tl e ,
$a in $b/ author / l a s t
return
<result >
{ $t }
{ $a }
</result >
}
</results >
a. What does the XQuery query above do?
b. What is the result when evaluating the XQuery on the document above?
Solution.
a. Return each pair of a book title with one of its authors.
b. <?xml v e r s i o n =”1.0” enc odin g=”UTF￾8”?>
<results >
<result >
<title >TCP/ IP I l l u s t r a t e d </title >
<last >Stevens </last >
</result >
<result >
<title >Advanced Programming in the Unix environment</title >
<last >Stevens </last >
</result >
<result >
<title >Data on the Web</title >
<last >Abiteboul </last >
</result >
<result >
<title >Data on the Web</title >
<last >Buneman</last >
</result >
<result >
<title >Data on the Web</title >
<last >Suciu</last >
</result >
</results >
11
````

### 图片文字 OCR（en-US，待对照原页）

````text
Exercise 10 -
< results >
for $b
< / results >
Interpreting and evaluating XQueries.
in doc (" bib . xml" ) / bib/ book ,
in $b/title
in $b/author/last
return
< result >
< / result >
a. What does the XQuery query above do?
b. What is the result when evaluating the XQuery on the document above?
Solution.
a.
Return each pair of a book title with one of its authors.
<?xml version 1.0" encoding="UTF—8"?>
< results >
< result >
< title >TCP/IP Illustrated < [title >
< last >Stevens < / last >
< result >
< title >Advanced Programming in the Unix environment < / title >
< last >Stevens < / last >
< result >
< title >Data on the
< last >Abiteboul < / last >
< result >
< title >Data on the
< last I ast >
< result >
< title >Data on the
< last >Suciu < / last >
< / results >
11
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/03-xquery-solutions.pdf#page=12)

### 原始文字层

````text
Exercise 11 - Interpreting and evaluating XQueries.
<bib>
{
f o r $b in doc (” bib . xml ”)// book
where $b/ publisher = ”Addison￾Wesley” and $b/@year > ”1991”
order by $b/ t i t l e
return <book> { $b/@year }{ $b/ t i t l e } </book>
}
</bib>
a. What does the XQuery query above do?
b. What is the result when evaluating the XQuery on the document above?
Solution.
a. For each book published by Addition-Wesley after 1991, return the year of publication
and book title in alphabetic order of the title.
b. <?xml v e r si o n =”1.0” enc odin g=”UTF￾8”?>
<bib>
<book year=”1992”>
<title >Advanced Programming in the Unix environment</title >
</book>
<book year=”1994”>
<title >TCP/ IP I l l u s t r a t e d </title >
</book>
</bib>
12
````

### 图片文字 OCR（en-US，待对照原页）

````text
Exercise 11 -
<bib>
for $b
Interpreting and evaluating XQueries.
in doc (" bib . xml " ) / / book
where $b/publisher —
Addison—Wesley" and $b/@year > " 1991
order by 8b/ title
return <book> { $b/@year
} { 8b/ title } </book>
</bib>
a.
b.
What does the XQuery query above do?
What is the result when evaluating the XQuery on the document above?
Solution.
a.
b.
For each book published by Addition-Wesley after 1991, return the year of publication
and book title in alphabetic order of the title.
< ? xml version =" 1.0" ? >
<bib>
<book year="
1992" >
< title >Advanced Programming in the Unix environment</title>
</book>
<book year="
Illustrated
</book>
</bib>
12
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

