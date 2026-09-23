# 04-PGM-model.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI752/notes/original/752/752（1）/04-PGM-model.pdf`
- [打开原文件](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/04-PGM-model.pdf)
- 原文件 SHA-256：`463b4954e637703c4f820de4ada63c40902c99ab4e1315b4ecfc445f7f4f0253`
- 文件索引：F197；PDF 总页数：6
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/04-PGM-model.pdf#page=1)

### 原始文字层

````text
COMPSCI 752
Big Data Management
Strategic Exercise 4
Graph Models - Model Solutions
Exercise 1 - Property graphs.
Imagine the scenario where we would like to develop a graph database for movie data. The
minimum requirements are to model actors, directors, movies, sequels of movies, awards, their
properties, and their relationships.
a. Write down a small property graph with real-world data.
b. Explain the properties and relationships on examples of your graph.
Actors have a name and a birthyear, such as Robert de Niro born in 1943. Similarly, directors
have a name and a birthyear, such as FF Coppola born in 1939. Movies have a title and a
year they were produced in, such as The Godfather produced in 1972. Awards have a name,
such the Academy awards. Actor may act in movies, such as the actor R De Niro acting in the
role of Vito Corleone in the movie Godfather II. Directors direct movies, such as FF Coppola
directing the movie The Godfather. Awards can be awarded to di↵erent entities, such as the
Academy award being awarded to the Actor R De Niro in the category Best Supporting Actor.
Finally, a movie can be a sequel to another movie, such as the movie Godfather II being a
sequel to movie The Godfather.
````

### 图片文字 OCR（en-US，待对照原页）

````text
COMPSCI 752
Big Data Management
Strategic Exercise 4
Graph Models - Model Solutions
Exercise 1 - Property graphs.
Imagine the scenario where we would like to develop a graph database for movie data. The
minimum requirements are to model actors, directors, movies, sequels of movies, awards, their
properties, and their relationships.
a.
b.
Write down a small property graph with real-world data.
Explain the properties and relationships on examples of your graph.
2 :Director
name = 'FF Coppola'
1 :Award
11 :awardedTo birthyear = 1939
name = 'Academy'
category = 'Best Director'
1 2 :awardedTo
category = 'Best
Supporting Actor'
16 :actsln
role = 'Vito Corleone'
13 :awardedTo
category =
'Best Movie'
3 :Actor
name = 'R De Niro'
birthyear = 1943
4 Movie
title = 'Godfather II'
year= 1974
14 :directs
17 :isSequelto
18 :actsln
role = 'Michael
orleone'
6 :Actor
name = 'A1 Pacino'
birthyear = 1940
15 :directs
5 :Movie
title = 'The Godfather'
year = 1972
19 :actsln
role = 'Michael Corleone'
Actors have a name and a birthyear, such as Robert de Niro born in 1943. Similarly, directors
have a name and a birthyear, such as FF Coppola born in 1939. Movies have a title and a
year they were produced in, such as The Godfather produced in 1972. Awards have a name,
such the Academy awards. Actor may act in movies, such as the actor R De Niro acting in the
role of Vito Corleone in the movie Godfather II. Directors direct movies, such as FF Coppola
directing the movie The Godfather. Awards can be awarded to different entities, such as the
Academy award being awarded to the Actor R De Niro in the category Best Supporting Actor.
Finally, a movie can be a sequel to another movie, such as the movie Godfather II being a
sequel to movie The Godfather.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/04-PGM-model.pdf#page=2)

### 原始文字层

````text
Exercise 2 - Formal model.
For the property graph from the first Exercise,
a. write down the formal definition of a property graph in terms of G =(V,E, ⌘, ￾, ⌫).
The property graph that constitutes one solution for the first exercise is formally defined as
follows:
– V = {1, 2, 3, 4, 5, 6}
– E = {11, 12, 13, 14, 15, 16, 17, 18, 19}
– ⌘ :
• 11 7! (1, 2)
• 12 7! (1, 3)
• 13 7! (1, 4)
• 14 7! (2, 4)
• 15 7! (2, 5)
• 16 7! (3, 4)
• 17 7! (4, 5)
• 18 7! (6, 4)
• 19 7! (6, 5)
– ￾ :
• 1 7! :Award
• 2 7! :Director
• 3, 6 7! :Actor
• 4, 5 7! :Movie
• 11, 12, 13 7! :awardedTo
• 14, 15 7! :directs
• 16, 18, 19 7! :actsIn
• 17 7! :isSequelTo
– ⌫ :
• (1, name) 7! ’Academy’
• (2, name) 7! ’FF Coppola’
• (2, birthyear) 7! 1939
• (3, name) 7! ’R De Niro’
• (3, birthyear) 7! 1943
• (4,title) 7! ’Godfather II’
• (4, year) 7! 1974
• (5,title) 7! ’The Godfather’
• (5, year) 7! 1972
• (6, name) 7! ’Al Pacino’
• (6, birthyear) 7! 1940
• (11, category) 7! ’Best Director’
• (12, category) 7! ’Best Supporting Actor’
• (13, category) 7! ’Best Movie’
• (16,role) 7! ’Vito Corleone’
• (18,role) 7! ’Michael Corleone’
• (19,role) 7! ’Michael Corleone’
2
````

### 图片文字 OCR（en-US，待对照原页）

````text
Exercise 2 - Formal model.
For the property graph from the first Exercise,
a. write down the formal definition of a property graph in terms of G (V, E, 0, A, v).
The property graph that constitutes one solution for the first exercise is formally defined as
follows:
E = {11, 12, 13, 14, 15, 16, 17, 18, 19}
2)
12 (I,
3)
13 (I,
4)
14 (2, 4)
15 (2, 5)
16 (3, 4)
5)
18 (6, 4)
19 (6, 5)
1 : Award
Director
3,6 :Actor
4, 5 : Movie
11, 12, 13 + :awardedTo
14, 15 + :directs
16, 18, 19 :actsln
17 + :isSequelTo
(1, name) + 'Academy'
(2, name) + 'FF Coppola'
(2, birthyear) + 1939
(3, name) + 'R De Niro'
(3, birthyear) + 1943
(4, title) + 'Godfather II'
(4, year) 1974
(5, title) + 'The Godfather'
(5, year) 1972
(6, name) + 'A1 Pacino'
(6, birthyear) + 1940
11, category) + 'Best Director'
(12, category) + 'Best Supporting Actor'
(13, category) + 'Best Movie'
(16, role) + 'Vito Corleone'
(18, role) + 'Michael Corleone'
(19, role) + 'Michael Corleone'
2
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/04-PGM-model.pdf#page=3)

### 原始文字层

````text
Exercise 3 - Objectified Path Property Graph.
For the property graph and its formal definition from the first two exercises,
a. Develop a meaningful extension to an Objectified Path Property Graph.
b. Extend the formal definition from the Property Graph to an OPPG G =(V, E, P, ⌘, ￾, ￾, ⌫).
The following definitions need to be added to the formal property graph from the previous
exercise to obtain a formal definition for the objectified path property graph above:
– P = {20}
– ￾(20) = [13, 17]
– ￾(20) = ‘:AwardWinningSequel’
– ⌫(20, category) = ’Academy’
3
````

### 图片文字 OCR（en-US，待对照原页）

````text
Exercise 3 - Objectified Path Property Graph.
For the property graph and its formal definition from the first two exercises,
a. Develop a meaningful extension to an Objextified Path Property Graph.
b. Extend the formal definition from the Property Graph to an OPPG G (V, E, P, 0, ö, A, v).
1 :Award
2 :Director
name = 'FF Coppola'
11 :åwardedTo birthyear = 1939
uname = 'Academy'
category = 'Aest Director'
3 :awardedTo
12 :awardedTo
category = 'Best
Supporting Actor'
category =
'Best Movie'
14 :directs
17 :isSequelto
:aétsln
role = 'Michael
orleone'
6 :Actor
name = 'A1 Pacino'
birthyear = 1940
15 :directs
16 :actsln
role = 'Vito Corleone'
20 :AwardWinningSequeI
category = 'Academy'
5 :Movie
title = 'The Godfather'
year = 1972
3 :Actor
name = 'R De Niro'
birthyear = 1943
4 Movie
title = 'Godfather II'
year= 1974
19 :actsln
role = 'Michael Corleone'
The following definitions need to be added to the formal property graph from the previous
exercise to obtain a formal definition for the objectified path property graph above:
P {20}
- ö(20) [13, 17]
':AwardWinningSequel'
v(20, category) 'Academy'
3
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/04-PGM-model.pdf#page=4)

### 原始文字层

````text
Exercise 4 - Objectified Subgraph Property Graph.
For the property graph and its formal definition from the first two exercises,
a. Develop a meaningful extension to an Objectified Subgraph Property Graph.
b. Extend the formal definition from the Property Graph to an OSPG G =(V, E, G, ⌘, ￾, ￾, ⌫).
The following definitions need to be added to the formal property graph from the second
exercise to obtain a formal definition for the objectified subgraph property graph above:
– G = {20, 21}
– ￾ :
• 20 7! ({1, 3, 4}, {12, 13, 16})
• 21 7! ({1, 2, 4}, {11, 13, 14})
– ￾ :
• 20 7! :awardWinningRole
• 21 7! :awardWinningDirector
– ⌫ :
• (20, year-awarded) 7! 1975
• (21, year-awarded) 7! 1975
4
````

### 图片文字 OCR（en-US，待对照原页）

````text
Exercise 4 - Objectified Subgraph Property Graph.
For the property graph and its formal definition from the first two exercises,
a. Develop a meaningful extension to an Objextified Subgraph Property Graph.
b. Extend the formal definition from the Property Graph to an OSPG G (V, E, G, 0, 7, A, v).
21 :awardWinningDirector•
year-awarded = 1975
20 :awardWinningRole
year-awarded = 1975
2 :Director
name = 'FF Coppola'
1 :Award
11 :awärdedTo birthyear = 1939
= 'Academy'
name
category = 'Bé t Director'
{12 :awardedTo:
category = 'Best :
Supporting Actor'
13 :awardedTo••
category =
'Best Movie'
.14 :directs
17 :isSequelto
18 :actsln
role = 'Michael
orleone'
6 :Actor
name = 'A1 Pacino'
birthyear = 1940
'15 :directs
'16 :actsln
role -"Vito Corleone'
3 :Actor
name = 'R De Niro'
birthyear = 1943
4 Movie
title = 'Godfather II'
1974
5 :Movie
title = 'The Godfather'
year = 1972
19 :actsln
role = 'Michael Corleone'
The following definitions need to be added to the formal property graph from the second
exercise to obtain a formal definition for the objectified subgraph property graph above:
G = {20, 21}
20 ({1,3, 4}, {12, 13, 16})
21 + ({1,2, 4}, {11, 13, 14})
0 + :awardWinningRole
21 + :awardWinningDirector
0, year-awarded) + 1975
21, year-awarded) + 1975
4
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/04-PGM-model.pdf#page=5)

### 原始文字层

````text
Exercise 5 - Hypervertex Property Graph.
For the subgraph property graph from the previous exercise,
a. Develop a meaningful extension to a Hypervertex Property Graph.
b. Extend the formal definition from the Objectified Subgraph Property Graph to an HVPG
G =(V,E, ⌘, ￾, ￾, ⌫).
The property graph that constitutes one solution for the first exercise is formally defined as
an extension of the formal property graph model from the second exercise as follows:
– V = {1, 2, 3, 4, 5, 6, 20, 21}
– E = {11, 12, 13, 14, 15, 16, 17, 18, 19, 22, 23}
– ⌘ :
• ...
• 22 7! (20, 21)
• 23 7! (21, 4)
– ￾ :
• 1 7! ({1}, ;)
• ...
• 20 7! ({1, 3, 4}, {12, 13, 16})
• 21 7! ({1, 2, 4}, {11, 13, 14})
– ￾ :
• ...
• 20 7! :awardWinningRole
5
````

### 图片文字 OCR（en-US，待对照原页）

````text
Exercise 5 - Hypervertex Property Graph.
For the subgraph property graph from the previous exercise,
a.
b.
Develop a meaningful extension to a Hypervertea; Property Graph.
Extend the formal definition from the Objectified Subgraph Property Graph to an HVPG
• •-22 :directedby
• 21 :awardWinningDirector
year-awarded = 1975
20 :awardWinningRole
year-awarded = 1975 •
I :Award
= 'Academy'
, name
"12 :awardedTo:
category = 'Best •
Supporting Actor'
'16 :actsln
role Corleone'
2 :Director
name = 'FF Coppola'
11 :awärdedTo birthyear = 1939
category = 'Bést Director'
13 :awardedTo'•
category =
'Best Movie'
23 :receivedFor
' '15 :directs
3 :Actor
name = 'R De Niro'
birthyear = 1943
4 Movie
title = 'Godfather II'
year= 1974
.14 :directs
• 17 :isSequelto
iä:actsln
role = 'Michael
orleone'
6 :Actor
name = 'A1 Pacino'
birthyear = 1940
5 :Movie
title = 'The Godfather'
year = 1972
19 :actsln
role = 'Michael Corleone'
The property graph that constitutes one solution for the first exercise is formally defined as
an extension of the formal property graph model from the second exercise as follows:
v = 6, 20, 21}
E {11, 12, 13, 14, 15, 16, 17, 18, 19, 22, 23}
22 (20, 21)
(21, 4)
20 ({1,3, 4}, {12, 13, 16})
21 + ({1,2, 4}, {11, 13, 14})
0 + :awardWinningRole
5
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../notes/original/752/752%EF%BC%881%EF%BC%89/04-PGM-model.pdf#page=6)

### 原始文字层

````text
• 21 7! :awardWinningDirector
• 22 7! :directedBy
• 23 7! :receivedFor
– ⌫ :
• ...
• (20, year-awarded) 7! 1975
• (21, year-awarded) 7! 1975
6
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
． 21 ： awardWinningDirector
2 :directedBy
卜 分 :receivedFor
， year-awarded) 1975
21 ， year-awarded) 1975
6
````

### 图片文字 OCR（en-US，待对照原页）

````text
21 + :awardWinningDirector
2 :directedBy
3 : received For
0, year-awarded) + 1975
21, year-awarded) + 1975
6
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

