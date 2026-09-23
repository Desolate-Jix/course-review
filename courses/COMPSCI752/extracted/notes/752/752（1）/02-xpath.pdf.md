# 02-xpath.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI752/notes/original/752/752（1）/02-xpath.pdf`
- [打开原文件](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/02-xpath.pdf)
- 原文件 SHA-256：`9030d25beb2465e14e2f287037d0765cbcc638aa20ea58e8e3ba6cc1b2a4b18c`
- 文件索引：F193；PDF 总页数：4
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/02-xpath.pdf#page=1)

### 原始文字层

````text
COMPSCI 752
Big Data Management
Strategic Exercise 2
XPath
Application domain. For questions 1, 2, and 3, consider the following XML document:
<?xml v e r si o n = ‘ ‘ 1. 0 ’ ’ enc odin g = ‘ ‘UTF￾8’’?>
<a><a><a/><b/><b/></a><a><a/><b><a/><a/></b></a></a>
Exercise 1 - XML documents and trees.
a. Draw the XML tree that corresponds to the XML document.
b. For each node, write down the pre- and post-identifiers.
Exercise 2 - XPath expressions.
Write the XPath expressions that correspond to the queries below, and evaluate the XPath
expressions on the given XML document. Use the pre-identifiers to denote the output nodes
of the queries.
a. select all a nodes that have a b-parent
b. select all b nodes that have no preceding b-elements
c. select all b nodes that are leaves
d. select all nodes with more than one b-sibling.
Exercise 3 - Node tests. Explain what the following XPath queries do and show the pre￾identifier of nodes that are selected by them:
a. //a[2]
b. //a/*[preceding-sibling::a and preceding-sibling::b]
c. //*[count(a)=count(b)]
d. //*[count(preceding::a)>3]
e. //a[not(ancestor::b)] | //b[not(ancestor::a)]
1
aa7lci
TM ts n
T
W
t­d.n­l
aIparenti bI output 9， 1
11b 悠 preceding 𠱃 output4 HE notdeandantii米 with output4， 5
有相同数量的子节点 aib
先前有3个 a 以上的节点
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
COMPSCI 752
Big Data M anageme nt
Strategic Exercise 2
XPath
Application domain · For questions 1 2 ， and 3 ， consider the following XML document ：
< ． ml
Exercise 1 - XML documents and trees.
a. Draw the XML tree that corresponds to the XML documen
b. For each node, write down t he pre- and post-identifiers ．
Exercise 2 - XPath expresslons.
Write the XPath expressions that correspond tO the queries below, and evaluate the XPath
expressions on the given XML document. Use the pre-identifiers tO denote the output nodes
Of the queries ．
严 re ] 对 9 如
select all a nodes that have a b-parent
select all b nodes that have no preceding b-elements 丿
b 匚 壳 n 月 5
select all b nodes that are leaves
select all nodes with more than one b-sibling ．
。 ,//a lparcnt ： :bl with ontpnt 9 ， ] 0
。 //bfnot(preceding::b)) with output 4
//b[not(descx•ndant ： ：刁] with output 4 ， 5
/ / ' l(count (preceding-sibling: ： b)+count(following-sibling::b)) > 1 ] with output 3
Exercise 3 - No e tests. Explain what the tOllowing XPath queries dO and show the pre-
identifier 0f nodes that are selected by them ：
b.
/ / a/* [preceding-sibling ： ： a and preceding-sibling ： ： b]
//*[count(a)=count(b)] 同
count (preceding: ： a) > 3 ]
/ /a[not(ancestor::b)] | / /b ： ： a) ]
0
a-elelnents that are in the second position ， with output 6 ， 10
t hO 艹 cllildren Of a-parents that have a preceding a-sibling and a preceding b-sibling, W
011tput 5
element nodes wliicli have the smne mnnbers Of a- and b-children, with output 3 ， 4 ． 5 ，
un
7 ， 9 ， ] 0
elelnents that ， lljore t han 3 preced ing a-elelnents ， with 011t put ] 0
a ． 0 nents t dO 1iOt have any b- 田 还 吓 tO 吓 together with b-element s that dO not 沅
MI.V a- 、 st 0 吓 ， witll ontptlt 1 ， 2 ， 3 ， 6 ， 7
0
````

### 图片文字 OCR（en-US，待对照原页）

````text
COMPSCI 752
Big Data Management
Strategic Exercise 2
XPath
Application domain. For questions 1, 2, and 3, consider the following XML document:
< . ml
<aXa a>
Exercise 1 - X NIL documents and trees.
a. Draw the XML tree that corresponds to the XML documen
b. For each node, write down the pre- and post-identifiers.
Exercise 2 - XPath expressions.
Write the XPath expressions that correspond to the queries below, and evaluate the XPath
expressions on the given XML document. Use the pre-identifiers to denote the output nodes
of the queries.
a.
b.
c.
d.
// at parent 9 , (o
/ abd ont
select all a nodes that have a b-parent
select all b nodes that have no preceding b-elements)
// bChctCdec.endant;,• on-C 5
select all b nodes that are leaves
select all nodes with more than one b-sibling.
• // with output 9, 10
• // with output 4
with output
with output 3
Exercise 3 - No e tests. Explain what the tOllowing XPath queries do and show the pre-
identifier of nodes that are selected by them:
a.
b.
c.
e.
/ and preceding-sibling::b]
count(a)=count(b)] J
// [count (preceding:
//a[not(ancestor::b)] I //b[not(ancestor::a)]
a.
b.
c.
d.
e.
a-elements that are in the second position, with output G, 10
those children of a-parents that have a preceding a-sibling and a preceding b-sibling, w
output 5
element nodes which have the smne mnnbers of a- and b-children, with output 3. 4. 5,
un
7. 9. 10
elements that have Inore than 3 preceding a-elenwnts, with output 10
a-elcnnents that do not have any b-nncestors together with b-elements that do not In
any a-ancestors, witli output l, 2, 3, G, 7
1,
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/02-xpath.pdf#page=2)

### 原始文字层

````text
1 a 2
米
先选所有a 再看是否是第二位置的
只崧 第2个a
big q
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
C().MPS('1 752
Biø l)ata 瞓
````

### 图片文字 OCR（en-US，待对照原页）

````text
CONIPSCI 752
Application
I • .X.V,L do€ur„cli'.s and
Solution
b aaa
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/02-xpath.pdf#page=3)

### 原始文字层

````text
<?xml v e r si o n =”1.0” enc odin g=”i s o ￾8859￾1”?>
<catalog>
<dvd year=”1954”>
<movie>The Seven Samuarai</movie>
<director >Akira Kurosawa</director >
<actor>Toshiro Mifune</actor>
<feature >English Subtitles </feature >
<price >29.99</price >
</dvd>
<dvd year=”2005”>
<movie>Finding Neverland</movie>
<musthave>Yes</musthave>
<actor>Johnny Depp</actor>
<actor>Kate Winslett </actor>
<price >39.95</price >
</dvd>
<dvd year=”1994”>
<movie>Pulp Fiction </movie>
<director >Quentin Tarantino </director >
<actor>Bruce Willis </actor>
<scratch>Yes</scratch>
<feature >Making Of</feature >
<price >9.99</price >
</dvd>
</catalog>
Exercise 4 - XML document and tree. Draw the corresponding XML tree.
Exercise 5 - Xpath queries. Write the following in XPath:
a. Select all the price elements.
b. Select all the price and movie elements.
c. Select the second dvd.
d. Select the self node of the second dvd.
e. Select the parent of the second dvd.
f. Select the ancestors of the second dvd.
g. Select the children of the second dvd.
h. Select the attribute children of the second dvd.
i. Select the descendant elements of the second dvd.
2
````

### 图片文字 OCR（en-US，待对照原页）

````text
<?xml version =" 1.0" encoding=" iso —8859—1"? >
<catalog>
<dvd year="
<movie>The Seven Samuarai
<director >Akira Kurosawa</director>
< actor>Toshiro Mifune</actor>
< feature>English Subtitles < / feature >
< price >29.99</price>
<dvd year="
2005" >
<movie>Finding Neverland
<musthave>Yes</musthave>
< actor >Johnny Depp</actor>
< actor>Kate Winslett < / actor >
< price price >
<dvd year="
1994 >
<movie>Pulp Fiction </movie>
<director >Quentin Tarantino</director>
< actor>Bruce Willis < / actor >
< scratch >
< feature >Making Of</feature>
< price >9.99</price>
< / catalog >
Exercise 4 - X NIL document and tree.
Draw the corresponding XML tree.
Exercise 5 - Xpath queries. Write the following in XPath:
a.
b.
c.
d.
e.
f.
g.
h.
i.
Select all the price elements.
Select all the price and movie elements.
Select the second dvd.
Select the self node of the second dvd.
Select the parent of the second dvd.
Select the ancestors of the second dvd.
Select the children of the second dvd.
Select the attribute children of the second dvd.
Select the descendant elements of the second dvd.
2
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/02-xpath.pdf#page=4)

### 原始文字层

````text
j. Select the descendant nodes of the second dvd.
k. Select the preceding elements of the second dvd.
l. Select the preceding nodes of the second dvd.
m. Select the preceding sibling elements of the second dvd.
n. Select the preceding sibling nodes of the second dvd.
o. Select the following elements of the second dvd.
p. Select the following nodes of the second dvd.
q. Select the following sibling elements of the second dvd.
r. Select the following sibling nodes of the second dvd.
3
````

### 图片文字 OCR（en-US，待对照原页）

````text
j.
k.
l.
m.
n.
o.
p.
q.
r.
Select the descendant nodes of the second dvd.
Select the preceding elements of the second dvd.
Select the preceding nodes of the second dvd.
Select the preceding sibling elements of the second dvd.
Select the preceding sibling nodes of the second dvd.
Select the following elements of the second dvd.
Select the following nodes of the second dvd.
Select the following sibling elements of the second dvd.
Select the following sibling nodes of the second dvd.
3
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

