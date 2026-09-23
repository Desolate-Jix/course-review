# CS752_Cypher_Tutorial.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI752/notes/original/752/752（1）/CS752_Cypher_Tutorial.pdf`
- [打开原文件](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/CS752_Cypher_Tutorial.pdf)
- 原文件 SHA-256：`aa4c6aa4e44016ed93270819b92aaa2c30a7a617682e2e42f7b91466daabd502`
- 文件索引：F209；PDF 总页数：3
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/CS752_Cypher_Tutorial.pdf#page=1)

### 原始文字层

````text
COMPSCI 752 Tutorial (Graph Databases - Cypher - Neo4j) Week 5
Instructions: Log into Neo4j (using the Sandbox (https://neo4j.com/sandbox/)) and create an instance of the
Recommendations database.
Additional resources: For additional help with Neo4j please feel free to explore the material in the free course, Neo4j
Graph Academy (https://graphacademy.neo4j.com/), especially the Beginner course modules. Also see the
Cypher documentation (https://neo4j.com/docs/cypher-manual/current/introduction/) for fur￾ther help.
1. Our first Cypher queries in Neo4j: Execute the following queries and write down the result. Do you notice anything
interesting about certain queries?
• MATCH (p:Person {name: ”Keanu Reeves”}) RETURN p.born AS answer
• MATCH (m:Movie {title: ”Top Gun”}) RETURN m.released AS release date
• MATCH (m:Movie {title: ”Matrix, The”})< →[:ACTED IN]-(p) RETURN p.name AS cast
• MATCH (m:Movie)< →[:ACTED IN]-(p:Person) WHERE m.title = ”Matrix, The” RETURN
p.name AS names
• MATCH (m:Movie {title: ”The Matrix”})< →[:ACTED IN]-(p) RETURN p.name AS cast
• MATCH (m:Movie {name: ”Matrix, The”})< →[:ACTED IN]-(p) RETURN p.name AS cast
2. Execute the following query and explore the resulting graph using its edges through the Neo4j Browser UI (e.g.
which other movies did the cast act in, etc?).
MATCH (m:Movie {title: ”Top Gun”}) RETURN m
3. What is wrong with the following queries and how could we correct these?
• MATCH (p:Person {name = ”Kiefer Sutherland”}) RETURN p.born AS age
• MATCH (m:Movie)-[:ACTED IN]→ >(p:Person) WHERE m.name = ”Da Vinci Code, The”
RETURN p.name AS cast
• CREATE (p:Person) WHERE p.name = ”Jane Doe” AND p.born = 2000
4. Execute the following aggregate queries and view the Neo4j Query Planner using ”PROFILE”.
• MATCH (p:Person)-[:ACTED IN]→ >(m:Movie) RETURN m.title AS Movie, COUNT(p) AS
Cast size
• PROFILE MATCH (p:Person)-[:ACTED IN]→ >(m:Movie) RETURN m.title AS Movie,
COUNT(p) AS Cast size
COMPSCI 752 Tutorial 1 1
Relation in
Neoyonlyllaber.­DE
ALHDElElTzrerr 删关系十Node 不能直接删
Node
O
g
Where里用 云
长 8 G
7M不存在name
m.title
createCp P 爾 心 以毕比
me
返回执行细节 orderby Lim
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
COMPSCI 752
TutonaI (Graph Databases - Cypher - Ne04j ）
Week 5
lnstrucuons ： Log int0 Ne04J (using the Sandbox (https ： / /ne04 j · com/sandbox/)) and create an instance of the
Recommendations database.
Additional resources: For additional help with Ne04j please feel free t0 explore the material m the free course, Ne04J
Graph Academy (https ： / /graphacademy ． ne04 j · com/), especially the Beginner course modules. AIso see the
Cypher documentation (https ： / /ne04 j · com/docs/cypher—manual/current/introduction/) for fur-
ther help.
1. Our first Cypher quenes m Ne04j ： Execute the following quenes and write down the result. Do you nouce anything
interestmg about certain quenes ？
。 MATCH (p:Person {name: ” Keanu Reeves"}) RETURN p.born AS answer
。 MATCH (m:Movie {title: "Top Gun"}) RETURN m.released AS release-date
。 MATCH (m:Movie {title: "Matrix, The"})< —[:ACTED-IN]-(p) RETURN p.name AS cast
。 MATCH (m:Movie) < —[:ACTED-IN]-(p:Person) WHERE m.title = ” Matr1x ， The ” RETURN
p.name AS names
。 MATCH (m:Movie {title: ” The Matnx"})< —[:ACTED-IN]-(p) RETURN p.name AS cast
。 MATCH (m:Movie {name: "Matrix, The"} ） < —[:ACTED-IN]-(p) RETURN p.name AS cast
乙 亻
忄 ， 刁 蒴
2 ， Exec e the
wing query and explore the resultmg graph using its edges through the Ne04J Browser UI (e.g
which Other movies did the cast act in, etc?).
MATCH (m:Movie {title: "Top Gun"}) RETURN m
3 ， What i wrong ith the following quenes and how could we correct these?
。 MATCH (p:Person {nam = ” K1efer Sutherland" } ） RETURN p.born AS age
。 MATCH (m:Movi :ACTED-IN]— p:Person) WHERE m. a
” Da Vinci Code, The ”
RETURN p.name A cast
。 CREATE (p:Person)
〔 印 ： ' h hame ：
rn = 2 佣 0
brn ：
4 ， Execute the following aggregate quenes and view the Ne04J Query PIanner using ， PROFILE ”
。 MATCH (p:Person)-[:ACTED-IN]— > (): Movie) RETURN m.title AS Movie, COUNT(p) AS
Cast_size
。 PROFILE A H ： Perso )-[:ACTED-IN]— > (): Movie) RETURN m.
tle AS Movie,
“ ． 处 6Ü 弋 T 巾 ） AS Cast-size
COMPSCI 752
Tutorial 1
1
````

### 图片文字 OCR（en-US，待对照原页）

````text
COMPSCI 752
Tutorial (Graph Databases - Cypher - Ne04j)
Week 5
Instructions: Log into Ne04j (using the Sandbox (https : / /ne04 j . com/sandbox/)) and create an instance of the
Recommendations database.
Additional resources: For additional help with Ne04j please feel free to explore the material in the free course, Ne04j
Graph Academy (https : / / graphacademy . ne04 j . com/), especially the Beginner course modules. Also see the
Cypher documentation (https : / /ne04 j . com/docs/cypher—manual/current/introduction/) for fur-
ther help.
1. Our first Cypher queries in Ne04j: Execute the following queries and write down the result. Do you notice anything
interesting about certain queries?
• MATCH (p:Person {name: "Keanu Reeves")) RETURN p.born AS answer
• MATCH (m:Movie {title: "Top Gun")) RETURN m.released AS release_date
• MATCH (m:Movie {title: "Matrix, RETURN p.name AS cast
• MATCH WHERE m.title = "Matrix, The" RETURN
p.name AS names
• MATCH (m:Movie {title: "The RETURN p.name AS cast
• MATCH (m:Movie {name: "Matrix, RETURN p.name AS cast
f Node.
2. Exec e the
wing query and explore the resulting graph using its edges through the Ne04j Browser UI (e.g
which other movies did the cast act in, etc?).
MATCH (m:Movie {title: "Top Gun")) RETURN m
3. What i wrong ith the following queries and how could we correct these?
m Tl#name•
• MATCH (p:Person {nam = "Kiefer Sutherland"}) RETURN p.born AS age
• MATCH (m:Movi :ACTEDAN]- p:Person) WHERE m. a
- "Da Vinci code, The"
RETURN p.nameA cast
• CREATE (p:Person)
Cp : pe&h hame
rn = 2000
ttit(e.
n/lere
4. Execute the following aggregate queries and view the Ne04j Query Planner using "PROFILE".
• MATCH RETURN m.title AS Movie, COUNT(p) AS
Cast_size
• PROFILE A H :Perso RETURN m.
tle AS Movie,
AS Cast-size
COMPSCI 752
Tutorial 1
1
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/CS752_Cypher_Tutorial.pdf#page=2)

### 原始文字层

````text
5. Execute the following Cypher queries and write down the results.
• MATCH (p:Person) WHERE p.name = ”Jane Doe” RETURN p.born
• MATCH (p:Person{born: 2000}) RETURN p.name
• MATCH (p)-[ACTED IN]→ >(m) WHERE p.name = ”Tom Cruise” RETURN p.title
• MATCH (m:Movie) RETURN m.title, m.released ORDER BY m.title DESC LIMIT 3
6. Write down the following (informal) queries in Cypher.
(a) List all the movie titles and the respective year they were released ordered (in ascending order) by which year
they were released.
(b) List the names and birth year of all cast members of the movie ”Cast Away”.
7. Note down and execute the respective Cypher queries to perform the following tasks.
(c) Create a node with label ”Movie” and title ”Auckland Adventures”, release date as the year 2025 and come
up with your own idea of additional properties and respective values (i.e. budget as 250.000, etc)
(d) Create a relationship / edge between the Person node with name Jane Doe (that we have created earlier) and
the Movie node ”Auckland Adventures” where the edge points towards the Movie node. Give the edge the
label ”ACTED IN” and the property ”roles” and for the respective value come up with a list of roles Jane
played (e.g. [’Wonder Woman’, ...])
2
Match (m:Movie) 
Return m.title and m.released order by m.release ASC
Match (m:Movie{title:"Cast Away"})<-[acted_in]-(a:Actor)
Return a.name , a.born
````

### 图片文字 OCR（en-US，待对照原页）

````text
5. Execute the following Cypher queries and write down the results.
• MATCH (p:Person) WHERE p.name = "Jane Doe" RETURN p.born
• MATCH 2000}) RETURN p.name
• MATCH WHERE p.name = "Tom Cruise" RETURN p.title
• MATCH (m:Movie) RETURN m.title, m.released ORDER BY m.title DESC LIMIT 3
6. Write down the following (informal) queries in Cypher.
(a) List all the movie titles and the respective year they were released ordered (in ascending order) by which year
they were released.
(b) List the names and birth year of all cast members of the movie "Cast Away".
Match (m:Movie)
Return m.title and m.released order by m.release ASC
Match (m:Movie{title: "Cast Away"})<-[acted_in]-(a:Actor)
Return a.name , a.born
7. Note down and execute the respective Cypher queries to perform the following tasks.
(c) Create a node with label "Movie" and title "Auckland Adventures", release date as the year 2025 and come
up with your own idea of additional properties and respective values (i.e. budget as 250.000, etc)
(d) Create a relationship / edge between the Person node with name Jane Doe (that we have created earlier) and
the Movie node "Auckland Adventures" where the edge points towards the Movie node. Give the edge the
label "ACTED-IN" and the property "roles" and for the respective value come up with a list of roles Jane
played (e.g. ['Wonder Woman', ...l)
2
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/CS752_Cypher_Tutorial.pdf#page=3)

### 原始文字层

````text
8. (Trickier questions) Write down the following (informal) queries in Cypher.
(e) List the names of all actors that acted in the movie ”The Matrix”, but not in the sequels of ”The Matrix” (you
might have to find out the titles of these movies)
(f) List the name of the oldest actor who starred in ”The Da Vinci Code”?
9. Feel free to explore the ”Recommendations” grpah dataset further and execute queries to practice Cypher.
3
````

### 图片文字 OCR（en-US，待对照原页）

````text
8. (Trickier questions) Write down the following (informal) queries in Cypher.
(e) List the names of all actors that acted in the movie "The Matrix", but not in the sequels of "The Matrix" (you
might have to find out the titles of these movies)
(f) List the name of the oldest actor who starred in "The Da Vinci Code"?
9. Feel free to explore the "Recommendations" grpah dataset further and execute queries to practice Cypher.
3
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

