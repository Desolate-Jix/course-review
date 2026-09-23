# Lab_02_Questions 2.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI751/notes/original/751%25/Lab_02_Questions 2.pdf`
- [打开原文件](../../../notes/original/751%2525/Lab_02_Questions%202.pdf)
- 原文件 SHA-256：`2ee2f217beedfd49931cc3a2560338d152332ae0ced744372163ba693b7eef3d`
- 文件索引：F171；PDF 总页数：6
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../notes/original/751%2525/Lab_02_Questions%202.pdf#page=1)

### 原始文字层

````text
Database System Tutorial 2
You’ve started a new movie-rating website, and you’ve been collecting data on reviewers’ ratings of
various movies. There’s not much data yet, but you can still try out some interesting queries.
Schema
You can download the database files from the following links:
• Download lab2.db – This is the database file. If you need a ready-to-use database, you can directly
use this file.
• Download rating.sql – This SQL script contains the commands to create the database from scratch.
If you prefer to generate the database yourself, use this script.
The database consists of the following tables:
• Movie ( mID, title, year, director )
Represents a movie with a unique ID (mID), a title, a release year, and a director.
• Reviewer ( rID, name )
Represents a reviewer with a unique ID (rID) and a name.
• Rating ( rID, mID, stars, ratingDate )
Represents a review where a reviewer (rID) gives a movie (mID) a star rating (1-5) on a specific
date (ratingDate).
Task
Your task is to write SQL queries to retrieve information from a sample dataset based on this schema.
Instructions
For each problem, write an SQL query that answers the given question. Compare your query’s output
with the provided expected results to verify its correctness.
Important Notes
• Your queries are executed using SQLite, so you must conform to the SQL constructs supported by
SQLite.
• Unless explicitly stated, you may return result rows in any order.
• You are to translate the English into a SQL query that computes the desired result over all possible
databases. All you need to check is that your query gets the right answer on the small sample
database. Thus, even if your output is correct, it is possible that your query does not correctly
reflect the problem at hand. (For example, if we ask for a complex condition that requires accessing
all of the tables, but over our small data set in the end the condition is satisfied only by Star Wars,
then the query “select title from Movie where title = ‘Star Wars’” will be correct even though it
doesn’t reflect the actual question.) Writing such queries may give the right answer on this dataset,
but it does not help you properly learn SQL. On the other hand, if you attempt to write a general
solution but make an error, your query will likely return incorrect results. Therefore, do not assume
that a query is correct just because it produces the expected output on the small sample database.
Always ensure that your query correctly reflects the given problem statement.
You are encouraged to experiment with and refine your queries to improve your understanding of
SQL. Keep practicing until you are confident in your solutions!
1
````

### 图片文字 OCR（en-US，待对照原页）

````text
Database System Tutorial 2
You've started a new movie-rating website, and you've been collecting data on reviewers' ratings of
various movies. There's not much data yet, but you can still try out some interesting queries.
Schema
You can download the database files from the following links:
• Download lab2.db — This is the database file. If you need a ready-to-use database, you can directly
use this file.
• Download rating.sql This SQL script contains the commands to create the database from scratch.
If you prefer to generate the database yourself, use this script.
The database consists of the following tables:
• Movie ( mlD, title, year, director
Represents a movie with a unique ID (mlD), a title, a release year, and a director.
• Reviewer ( rlD, name
Represents a reviewer with a unique ID (rlD) and a name.
• Rating ( rlD, mlD, stars, ratingDate )
Represents a review where a reviewer (rlD) gives a movie (mlD) a star rating (1-5) on a specific
date (ratingDate).
Task
Your task is to write SQL queries to retrieve information from a sample dataset based on this schema.
Instructions
For each problem, write an SQL query that answers the given question. Compare your query's output
with the provided expected results to verify its correctness.
Important Notes
• Your queries are executed using SQLite, so you must conform to the SQL constructs supported by
SQLite.
• Unless explicitly stated, you may return result rows in any order.
You are to translate the English into a SQL query that computes the desired result over all possible
databases. All you need to check is that your query gets the right answer on the small sample
database. Thus, even if your output is correct, it is possible that your query does not correctly
reflect the problem at hand. (For example, if we ask for a complex condition that requires accessing
all of the tables, but over our small data set in the end the condition is satisfied only by Star Wars,
then the query "select title from Movie where title 'Star Wars"' will be correct even though it
doesn't reflect the actual question.) Writing such queries may give the right answer on this dataset,
but it does not help you properly learn SQL. On the other hand, if you attempt to write a general
solution but make an error, your query will likely return incorrect results. Therefore, do not assume
that a query is correct just because it produces the expected output on the small sample database.
Always ensure that your query correctly reflects the given problem statement.
You are encouraged to experiment with and refine your queries to improve your understanding of
SQL. Keep practicing until you are confident in your solutions!
1
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../notes/original/751%2525/Lab_02_Questions%202.pdf#page=2)

### 原始文字层

````text
Questions
1. Retrieve the titles of all movies where the director is Steven Spielberg.
2. Retrieve the years where there are one or more movies rated 4 or 5. Sort the years in ascending
order.
3. Retrieve the titles of all movies that have never been rated.
4. Retrieve the names of all reviewers who submitted ratings where the rating date is NULL.
5. Write a query to return the ratings data in a more readable format: reviewer name, movie title,
stars, and ratingDate. Also, sort the data, first by reviewer name, then by movie title, and lastly
by number of stars.
2
单引号 字符串
in 对应多个
xxx is null
join xxx on xxx 二 xxx
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Questions
1. Retrieve the titles of all movies where the director is Steven Spielberg.
title
1 E.T 、
2 RaidersoftheLostArk
2 ．
years where are one or more movies 4 5 ．
s 代 0 > sel.ect year “ ov 羡 0 地 re nid 炻 (seLect nid + r00 rating 10r stars
19 的 丨
1 19
戕 嘥 、
Sort the years in ascending
order ．
year
1 1937
2 1939
3 1981
4 2 9
3 ． Retrieve the titles of all movies that have never been rated.
1
2
title
Star Wars
Titanic
飞 it ” 飞 c 上 title 黼 以 。 《 d （ 艹 醺 •ld fr• •Nting)•
4 ． Retrieve the names of all reviewers wh0 submitted ratings where the rating date is NULL ．
1
2
name
Daniel Lewis
Chris Jackson
Låte > n00 丝 ． 0 “ " 0 re 01 《 = 上 + r00 飞 raelngdate № 〕 ；
5 ． Write a query t0 return the ratings data in a more readable format ： reviewer name ， movie title,
stars, and ratingDate. AIso sort the data, first by reviewer name, then by movie title, and lastly
by number of stars.
title
Raiders ofthe Lost Ark
Raiders ofthe Lost Ark
The Sound OfMusiC
Raiders ofthe Lost Ark
The Sound ofMusiC
Snow White
Avatar
Snow White
Avatar
Gone with the Wind
Gone with the Wind
Gone with the Wind
stars ratingDate
1
2
3
4
5
6
7
8
9
10
11
12
13
14
name
Ash1ey Whit.e
Brittany HarriS
Brittany Harris
Brittany Harris
Chris Jackson
Chris Jackson
Chris Jackson
Daniel LewiS
Elizabeth Thomas
Elizabeth Thomas
James Cameron
Mike Anderson
Sarah Martinez
Sarah Martinez
3
2
4
2
2
4
3
4
3
5
5
3
2
4
2011 @4．
2011 ． OI ． 30
2011 · 01 ． 1
2011 · 01 ． 20
2011 ． 01 ． 22
2011 ． 01 ． 27
2011 · 01 ． 15
2011 ． 01 ． 19
2011 ． 01 ． 20
2011 ． OI ℃ 9
2011 ． 01 ． 22
2011 ． 01 ． 27
kxx
0 =
SELECT reviewer•na 。 巴 § 趣 @山鼠戔哽堡 刂 咖
FROM movie
」 0 》 N rating ON movie.rnid ，@@&@0芸 卜 h movies 山
JOIN reviewer ON 《 & 0 竺 匹 以 玉 [ 叵 二 Matgh ratings i 山 reviewers
ORDER BY reviewer.name• !Lg 0 还 ！ 到 g 孬 ：
2
````

### 图片文字 OCR（en-US，待对照原页）

````text
Questions
1.
2.
3.
4.
5.
Retrieve the titles of all movies where the director is Steven Spielberg.
title
1 E.T.
2 Raiders of the Lost Ark
Retrieve the years
order.
year
| 1937
2 1939
3 1981
4 2009
where there are one or more movies rated 4 or 5.
Sort the years in ascending
sqIite> year in (Select rating
I year
1937 |
1939 |
1 200-9
Retrieve the titles of all movies that have never been rated.
title
Sqiite> title •ld ;
I
Star Wars
2 Titanic
) Order by
Retrieve the names of all reviewers who submitted ratings where the rating date is NULL.
name
I Daniel Lewis
2
Chris Jackson
rid in rid f— raungdate iS
with
Write a query to return the ratings data in a more readable format: reviewer name, movie title,
stars, and ratingDate. Also, sort the data, first by reviewer name, then by movie title, and lastly
by number of stars.
title
E.T.
Raiders of the Lost Ark
Raiders of the Lost Ark
The Sound of Music
E.T.
Raiders of the Lost Ark
The Sound Of MusiC
Snow White
Avatar
Snow White
Avatar
Gone with the Wind
Gone with the Wind
Gone with the Wind
stars ratingDate
I
2
3
4
5
6
7
8
9
10
11
12
13
14
name
Ashley White
Brittany Harris
Brittany Harris
Brittany Harris
Chris Jackson
Chris Jackson
Chris Jackson
Daniel Lewis
Elizabeth Thomas
Elizabeth Thomas
James Cameron
Mike Anderson
Sarah Martinez
Sarah Martinez
3
2
4
2
4
3
4
3
5
5
3
2
4
2011
2011-01-30
2011-01-12
2011-01-20
2011-01-22
NULL
2011-01-27
NULL
2011-01-15
2011-01-19
2011-01-20
2011-01-09
2011-01-22
2011-01-27
kxX
SELECT reviewer.na ,
FROM movie
JOIN rating ON movie. mid Mateh movies with
JOIN reviewer ON Match with
ORDER BY reviewer-name,
2
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../notes/original/751%2525/Lab_02_Questions%202.pdf#page=3)

### 原始文字层

````text
6. Retrieve the names of reviewers and the titles of movies where the reviewer rated the same movie
twice, with the second rating being higher than the first.
7. For each movie that has at least one rating, find the highest number of stars that movie received.
Return the movie title and number of stars. Sort by movie title.
8. Retrieve the titles of all movies along with their rating spread (the di!erence between the highest
and lowest ratings). Sort results by rating spread (descending), then by title.
9. Compute the di!erence between the average per-movie rating of films released before 1980 and
those released after 1980.
10. Retrieve the names of all reviewers who submitted ratings for the movie Gone with the Wind.
11. For any rating where the reviewer is the same as the director of the movie, return the reviewer
name, movie title, and number of stars.
12. Retrieve a combined list of reviewer names and movie titles, sorted alphabetically.
3
````

### 图片文字 OCR（en-US，待对照原页）

````text
6.
7.
8.
9.
10.
11.
12.
Retrieve the names of reviewers and the titles of movies where the reviewer rated the same movie
twice, with the second rating being higher than the first.
title
name
I Sarah Martinez Gone with the Wind
For each movie that has at least one rating, find the highest number of stars that movie received.
Return the movie title and number of stars. Sort by movie title.
I
3
4
5
6
title
Avatar
Gone with the Wind
Raiders of the Lost Ark
Snow White
The Sound of Music
score
5
3
4
4
5
3
Retrieve the titles of all movies along with their rating spread (the difference between the highest
and lowest ratings). Sort results by rating spread (descending), then by title.
I
2
3
5
6
title
Avatar
Gone with the Wind
Raiders of the Lost Ark
Snow White
The Sound of Music
rs
2
2
2
1
1
1
Compute the difference between the average per-movie rating of films released before 1980 and
those released after 1980.
avg(avl) - avg(av2)
| 0.0555555555555558
Retrieve the names of all reviewers who submitted ratings for the movie Gone with the Wind.
I
2
name
Sarah Martinez
Mike Anderson
For any rating where the reviewer is the same as the director of the movie, return the reviewer
name, movie title, and number of stars.
name
title stars
I James Cameron Avatar 5
Retrieve a combined list of reviewer names and movie titles, sorted alphabetically.
3
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../notes/original/751%2525/Lab_02_Questions%202.pdf#page=4)

### 原始文字层

````text
13. Retrieve the titles of all movies that have not been reviewed by Chris Jackson.
14. Retrieve pairs of reviewer names where both reviewers rated the same movie. Eliminate duplicates,
ensure that each pair appears only once, do not pair reviewers with themselves. For each pair, return
the names in the pair in alphabetical order.
15. For each rating that is the lowest (fewest stars) currently in the database, return the reviewer
name, movie title, and number of stars.
4
````

### 图片文字 OCR（en-US，待对照原页）

````text
I
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
Ashley White
Avatar
Brittany Harris
Chris Jackson
Daniel Lewis
E.T.
Elizabeth Thomas
Gone with the Wind
James Cameron
Mike Anderson
Raiders of the Lost Ark
Sarah Martinez
Snow White
Star Wars
The Sound of Music
Titanic
13.
14.
15.
Retrieve the titles of all movies that have not been reviewed by Chris Jackson.
title
I
Gone with the Wind
2
Star Wars
3 Titanic
4
Snow White
5 Avatar
Retrieve pairs of reviewer names where both reviewers rated the same movie. Eliminate duplicates,
ensure that each pair appears only once, do not pair reviewers with themselves. For each pair, return
the names in the pair in alphabetical order.
I
2
3
4
5
name
Ashley White
Brittany Harris
Daniel Lewis
Elizabeth Thomas
Mike Anderson
name
Chris Jackson
Chris Jackson
Elizabeth Thomas
James Cameron
Sarah Martinez
For each rating that is the lowest (fewest stars)
name, movie title, and number of stars.
4
currently in the database, return the reviewer
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../notes/original/751%2525/Lab_02_Questions%202.pdf#page=5)

### 原始文字层

````text
16. Retrieve movie titles along with their average ratings, sorted by average rating in descending order.
If multiple movies share the same rating, sort them alphabetically.
17. Find the names of all reviewers who have contributed three or more ratings. (As an extra challenge,
try writing the query without HAVING or without COUNT.)
18. Retrieve the names of directors who have directed more than one movie, along with the titles of
all movies they directed. Sort by director name, then by movie title.
19. Find the movie(s) with the highest average rating. Return the movie title(s) and average rating.
20. Find the movie(s) with the lowest average rating. Return the movie title(s) and average rating.
5
````

### 图片文字 OCR（en-US，待对照原页）

````text
title
name
I Sarah Martinez
2 Brittany Harris
3 Brittany Harris
4 Chris Jackson
Gone with the Wind
The Sound of Music
Raiders of the Lost Ark
E.T.
stars
2
2
2
2
16. Retrieve movie titles along with their average ratings, sorted by average rating in descending order.
If multiple movies share the same rating, sort them alphabetically.
title
I
Snow White
2 Avatar
3
Raiders of the Lost Ark
4
Gone with the Wind
6
The Sound of Music
rat
4.5
4.0
3.33333333333333
3.0
2.5
2.5
17. Find the names of all reviewers who have contributed three or more ratings. (As an extra challenge,
try writing the query without HAVING or without COUNT.)
name
I Brittany Harris
2 Chris Jackson
18. Retrieve the names of directors who have directed more than one movie, along with the titles of
all movies they directed. Sort by director name, then by movie title.
title
I Avatar
2 Titanic
3 E.T.
director
James Cameron
James Cameron
Steven Spielberg
4 Raiders Of the Lost Ark Steven Spielberg
19. Find the movie(s) with the highest average rating. Return the movie title(s) and average rating.
title
x
I Snow White 4.5
20. Find the movie(s) with the lowest average rating. Return the movie title(s) and average rating.
title
x
1 Thesound ofMusic 2.5
2.5
5
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../notes/original/751%2525/Lab_02_Questions%202.pdf#page=6)

### 原始文字层

````text
21. For each director, return the director’s name together with the title(s) of the movie(s) they directed
that received the highest rating among all of their movies, and the value of that rating. Ignore
movies whose director is NULL.
Note: We just show the demonstration of before query execution and after query execution, this
is not the actual final result.
22. Add the reviewer Roger Ebert to your database, with an rID of 209.
23. For all movies that have an average rating of 4 stars or higher, add 25 to the release year. (Update
the existing tuples; don’t insert new tuples.)
24. Delete all ratings where the movie’s year is before 1970 or after 2000, and the rating is fewer than
4 stars.
6
````

### 图片文字 OCR（en-US，待对照原页）

````text
21.
22.
23.
24.
For each director, return the director's name together with the title(s) of the movie(s) they directed
that received the highest rating among all of their movies, and the value of that rating. Ignore
movies whose director is NULL.
I
2
3
4
director
Victor Fleming
Robert Wise
James Cameron
Steven Spielberg
title
Gone with the Wind
The Sound of Music
Avatar
stars
4
3
5
Raiders of the Lost Ark 4
Note: We just show the demonstration of before query execution and after query execution, this
is not the actual final result.
Add the reviewer Roger Ebert to your database, with an r ID of 209.
title
mlD
director
year
mlD
title
director
year
1
2
3
4
5
6
7
8
101
102
103
104
105
106
107
108
Gone with the Wind
Star Wars
The Sound of Music
E.T.
Titanic
Snow White
Avatar
1939
1977
1965
1982
1997
1937
2CX)9
Vict.or Fleming
George Lucas
Robert Wise
Steven Spielberg
James Cameron
NULL
James Cameron
Steven Spielberg
1
2
3
4
5
6
7
8
101
102
103
104
105
106
107
108
Gone with the Wind
Star Wars
The Sound of Music
E.T.
Titanic
Snow White
Avatar
1939
1977
1965
1982
1997
1962
2034
Raiders of the Lost Ark 1981
Raiders of the Lost Ark 1981
Victor Fleming
Lucas
Robert Wise
Steven Spielberg
James Cameron
NULL
James Cameron
Steven Spielberg
For all movies that have an average rating of 4 stars or higher, add 25 to the release year. (Update
the existing tuples; don't insert new tuples.)
title
mlD
director
year
mlD
title
director
year
1
2
3
4
5
6
7
8
101
102
103
104
105
106
107
108
Gone with the Wind
Star Wars
The Sound of Music
E.T.
Titanic
Snow White
Avatar
1939
1977
1965
1982
1997
1937
2CX)9
Victor Fleming
George Lucas
Robert Wise
Steven Spielberg
James Cameron
NULL
James Cameron
Steven Spielberg
1
2
3
4
5
6
7
8
101
102
103
104
105
106
107
108
Gone with the Wind
Star Wars
The Sound of Music
E.T.
Titanic
Snow White
Avatar
1939
1977
1965
1982
1997
1962
2034
Raiders of the Lost Ark 1981
Raiders of the Lost Ark 1981
Victor Fleming
George Lucas
Robert Wise
Steven Spielberg
James Cameron
NULL
James Cameron
Steven Spielberg
Delete all ratings where the movie's year is before
1970 or after 2000, and the rating is fewer than
4 stars.
1
2
3
4
5
6
7
8
title
mlD
director
year
title
mlD
director
year
101
102
103
104
105
106
107
108
Gone with the Wind
Star Wars
The Sound of Music
Titanic
Snow White
Avatar
Raiders of the Lost Ark
1939
1977
1965
1982
1997
1937
2009
1981
Victor Fleming
George Lucas
Robert Wise
Steven Spielberg
James Cameron
James Cameron
Steven Spielberg
6
1
2
3
4
5
6
7
8
101
102
103
104
105
106
107
108
Gone with the Wind
Star Wars
The Sound of Music
E.T.
Titanic
Snow White
Avatar
Raiders of the Lost Ark
1939
1977
1965
1982
1997
1937
2009
1981
Victor Fleming
George Lucas
Robert Wise
Steven Spielberg
James Cameron
NULL
James Cameron
Steven Spielberg
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

