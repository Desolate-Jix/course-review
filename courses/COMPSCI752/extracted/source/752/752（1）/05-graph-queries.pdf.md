# 05-graph-queries.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI752/source/752/752（1）/05-graph-queries.pdf`
- [打开原文件](../../../../source/752/752%EF%BC%881%EF%BC%89/05-graph-queries.pdf)
- 原文件 SHA-256：`e6eb8c608d248126bc8e937a761474ff7a61a4f05d9a86911a26e4a9e72ae619`
- 文件索引：F198；PDF 总页数：3
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/05-graph-queries.pdf#page=1)

### 原始文字层

````text
COMPSCI 752
Big Data Management
Strategic Exercise 5
Graph Queries
Application Domain. For all the exercises we are looking at an application domain where
customers buy parts of products, and suppliers supply parts of products. Parts can also be
parts of other parts. Customers, Suppliers, and Parts may have various properties. As an
example for the application domain we consider the following property graph G:
Exercise 1 - Regular Path Queries.
For each of the following English language queries,
– Write them down as regular path queries.
– Evaluate them on the property graph G above.
a. List all pairs of customers who have bought the same part.
b. List all pairs of customers c1 and c2 for which there is some customer c that has bought
the same part as c1 and the same part as c2.
c. List a pair of customers c1 and c2 whenever they have bought the same part, or there is
some customer c that has bought the same part as c1 and the same part as c2.
d. We say that two customers c and c0 are linked through a chain c1,...,cn of customers if
c = c1, c0 = cn and for 1  i  n ￾ 1 there is some part that is bought by ci and ci+1.
List all pairs of customers that are linked through some chain.
ei
ibuyslibugs­ezibuyslibugs7ibnysl.bg5
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
COMPSCI 752
Big Data Management
Strategic Exercise 5
Graph Queries
Application Domain. For all the exercises we are looking at an application domain where
customers buy parts of products, and suppliers supply parts of products. Parts can also be
parts of other parts. Customers, Suppliers, and Parts may have various properties. As an
example for the application domain we consider the following property graph G:
2 :Supplier :Customer
name = 'Walther GmBH'
country = 'Germany'
1 :Customer
cid = '007'
cname = 'Bond'
caddress = 'M16'
11 :supplies
s-price='600$'
13 :buys
p-price='800$'
12 :buys
p-price='550$'
4 :Part
pname = 'Spywear'
14 :partOf
type = '00'
number—I
3 :Part
pname = 'Walther PPK'
serial = '053188'
type = 'Gun'
Exercise 1 - Regular Path Queries.
For each of the following English language queries,
a.
b.
c.
d.
Write them down as regular path queries.
Evaluate them on the property graph G above.
buys //,•
List all pairs of customers who have bought the same part.
List all pairs of customers Cl and 02 for which there is some customer that has o ght
:bwqs/.' bugs-i:
the same part as Cl and the same part as c2.
List a pair of customers Cl and co whenever they have bought t e same part, or there is
some customer c that has bought the same part as Cl and the same part as co.
We say that two customers c and d are linked through a chain Cl, ... , n
c of customers if
d cn and for 1 i n — 1 there is some part that is bought by Ci and Ci+l.
List all pairs of customers that are linked through some chain.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/05-graph-queries.pdf#page=2)

### 原始文字层

````text
e. List a pair of customer and supplier whenever the customer has bought a part the supplier
supplied.
f. List a pair of customer and supplier whenever the customer has bought a part the supplier
supplied or bought.
g. List a pair of customer and supplier whenever the customer has bought a part the supplier
supplied and bought.
h. List a customer whenever they have bought a part that is part of some part.
Exercise 2 - Conjunctive Graph Queries.
For each of the following English language queries,
– Write them down as conjunctive graph query.
– Evaluate them on the property graph G above.
a. List all pairs of customers who have bought the same part.
b. List all pairs of customers c1 and c2 for which there is some customer c that has bought
the same part as c1 and the same part as c2.
c. List a pair of customers c1 and c2 whenever they have bought the same part, or there is
some customer c that has bought the same part as c1 and the same part as c2.
d. We say that two customers c and c0 are linked through a chain c1,...,cn of customers if
c = c1, c0 = cn and for 1  i  n ￾ 1 there is some part that is bought by ci and ci+1.
List all pairs of customers that are linked through some chain.
e. List a pair of customer and supplier whenever the customer has bought a part the supplier
supplied.
f. List a pair of customer and supplier whenever the customer has bought a part the supplier
supplied or bought.
g. List a pair of customer and supplier whenever the customer has bought a part the supplier
supplied and bought.
h. List a customer whenever they have bought a part that is part of some part.
Exercise 3 - More expressive Languages.
For the application domain above,
a. Find a conjunctive regular path query that is neither a conjunctive graph query nor a
regular graph query, and evaluate it on G.
b. Find a union of conjunctive regular path query that is not a conjunctive regular path
query, and evaluate it on G
c. Find a relational algebra (RA) query that cannot be expressed by any of the other query
languages we have discussed.
2
Nc gck bugslxc.pl buys
cyp
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
e.
f.
g.
h.
List a pair of customer and supplier whenever the customer has bought a part the supplier
supplied.
List a pair of customer and supplier whenever the customer has bought a part the supplier
supplied or bought.
List a pair of customer and supplier whenever the customer has bought a part the supplier
supplied and bought.
List a customer whenever they have bought a part that is part of some part.
Exercise 2 - Conjunctive Graph Queries.
For each of the following English language queries,
a.
b.
c.
d.
e.
f.
g.
h.
Write them down as conjunctive graph query.
Cyc, 5 ok..— p) ; buys
Evaluate them on the property graph G above.
List all pairs of customers who have bought the same part.
List all pairs of customers Cl and 02 for which there is some customer c that has bought
the same part as Cl and the same part as c2.
List a pair of customers Cl and co whenever they have bought the same part, or there is
some customer c that has bought the same part as Cl and the same part as CQ.
We say that two customers c and d are linked through a chain Cl, ... , n
c of customers if
d cn and for 1 i n — 1 there is some part that is bought by Ci and Ci+l.
List all pairs of customers that are linked through some chain.
List a pair of customer and supplier whenever the customer has bought a part the supplier
supplied.
List a pair of customer and supplier whenever the customer has bought a part the supplier
supplied or bought.
List a pair of customer and supplier whenever the customer has bought a part the supplier
supplied and bought.
List a customer whenever they have bought a part that is part of some part.
Exercise 3 - More expressive Languages.
For the application domain above,
a.
b.
c.
Find a conjunctive regular path query that is neither a conjunctive graph query nor a
regular graph query, and evaluate it on G.
Find a union of conjunctive regular path query that is not a conjunctive regular path
query, and evaluate it on G
Find a relational algebra (RA) query that cannot be expressed by any of the other query
languages we have discussed.
2
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/05-graph-queries.pdf#page=3)

### 原始文字层

````text
Exercise 4 - Regular Property Graph Logic.
For each of the following English language queries,
– Write them down as regular property graph logic query or its extensions.
– Evaluate them on the property graph G above.
a. List all suppliers who supply some type of gun.
b. List all suppliers who supply some type of gun, or some part that has been bought by a
customer from ’MI6’.
c. List all suppliers who have bought some part cheaper than what they supplied it for.
d. Return teams of two customers and one supplier together with the average price of pur￾chasing a product by the customers, whenever that average price is lower than the price
the product was supplied by the supplier.
Exercise 5 - Regular Property Graph Algebra.
For each of the following English language queries write them down as a regular property
graph algerba query.
a. List all suppliers who supply some type of gun.
b. List all suppliers who supply some type of gun, or some part that has been bought by a
customer from ’MI6’.
c. List all suppliers who have bought some part cheaper than what they supplied it for.
3
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Exercise      4             -             Regular             Prop erty             Graph             Logic.
For              each              of              the              following              English              language              queries,
      –        Write              them              down              as              regular              prop erty              graph              logic              query              or              its              extensions.
      –        Evaluate              them              on              the              prop erty              graph                                        G        ab ove.
a.             List              all              suppliers              who              supply              some              typ e              of              gun.
b.             List              all              suppliers              who              supply              some              typ e              of              gun,              or              some              part              that              has              b een              b ought              by              a
               customer              from              ’MI6’.
 c.            List              all              suppliers              who              have              b ought              some              part              cheap er              than              what              they              supplied              it              for.
d.             Return              teams              of              two              customers              and              one              supplier              together              with              the              average              price              of              pur-
               chasing              a              pro duct              by              the              customers,              whenever              that              average              price              is              lower              than              the              price
               the              pro duct              was              supplied              by              the              supplier.
Exercise      5             -             Regular             Prop erty             Graph             Algebra.
For                 each                 of                 the                 following                 English                 language                 queries                 write                 them                 down                 as                 a                 regular                 prop erty
graph              algerba              query.
a.             List              all              suppliers              who              supply              some              typ e              of              gun.
b.             List              all              suppliers              who              supply              some              typ e              of              gun,              or              some              part              that              has              b een              b ought              by              a
               customer              from              ’MI6’.
 c.            List              all              suppliers              who              have              b ought              some              part              cheap er              than              what              they              supplied              it              for.
                                                                                                                                                                         3
````

### 图片文字 OCR（en-US，待对照原页）

````text
Exercise 4 - Regular Property Graph Logic.
For each of the following English language queries,
a.
b.
c.
d.
Write them down as regular property graph logic query or its extensions.
Evaluate them on the property graph G above.
List all suppliers who supply some type of gun.
List all suppliers who supply some type of gun, or some part that has been bought by a
customer from 'M16'.
List all suppliers who have bought some part cheaper than what they supplied it for.
Return teams of two customers and one supplier together with the average price of pur-
chasing a product by the customers, whenever that average price is lower than the price
the product was supplied by the supplier.
Exercise 5 - Regular Property Graph Algebra.
For each of the following English language queries write them down as a regular property
graph algerba query.
a.
b.
c.
List all suppliers who supply some type of gun.
List all suppliers who supply some type of gun, or some part that has been bought by a
customer from 'M16'.
List all suppliers who have bought some part cheaper than what they supplied it for.
3
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

