# W9-Stream+Processing.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI752/source/752/752（1）/W9-Stream+Processing.pdf`
- [打开原文件](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf)
- 原文件 SHA-256：`a888351977c3bdeeb06c04cd2d2e1cf58f66c88760a71978f20a4c44aa60297a`
- 文件索引：F224；PDF 总页数：26
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=1)

### 原始文字层

````text
1
Data Stream Processing
COMPSCI 752: Big Data Management
University of Auckland
(Credits to Ninh Pham)
Slides are collected and edited from https://vasia.github.io/dspa20/index.html
and https://homepages.cwi.nl/~boncz/bads/stream.shtml
Auckland, May 2025
R
ragtime data
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
R
                                   Data  Stream Process  ing
                                   C OMPS CI  7 5 2: B ig   Data  Ma nag  ement
                                                       Un iver   sity   o f Auc  kla nd
                                                      (C red it  s to  Ni  nh   Pham)                  rag ti me            data
                         Slid es   a re  co ll   ect   ed   a n d  e d ited   f  ro m ht    tp  s:/  /  va s  i a.    g i thu  b.i o  /  ds  p  a 2  0/  i n  d  ex  .h   tml
                                      and ht  tp s:/ / ho me p a ge s.c   wi.n l/~   bo n cz /b a d s/ s tre am   .s html
                                                             Auck land,  May  2025                                                                1
````

### 图片文字 OCR（en-US，待对照原页）

````text
Data Stream Processing
COMPSCI 752: Big Data Management
University of Auckland
(Credits to Ninh Pham)
Slides are collected and edited from
https://vasia.github.io/dspa20/index.html
and htt s: / / home a es.cwi.nl/—boncz/bads/stream.shtml
Auckland, May 2025
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=2)

### 原始文字层

````text
Outline
2
 Introduction
 Definition, applications, challenges
 Data stream processing
 Data stream modelling
 Data stream processing
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Outline
Introduction
Definition, applications, challenges
Data stream processing
Data stream modelling
Data stream processing
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=3)

### 原始文字层

````text
What is data stream?
3
 Large data volume, likely structured, arriving at a very high 
rate (high enough that machine cannot keep up it)
 Definition (Golab & Ozsu, 2003):
 A data stream is a real-time, continuous, ordered (implicitly by arrival
time of explicitly by timestamp) sequence of items
 It is impossible to control the order in which items arrive, nor it is 
feasible to locally store a stream in its entirety
一
雌控序
②快 难存
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
What is data stream?
Larg e data volume, likely structured, arriving at a very high
rate (high enough that machine cannot keep up it)
． Definition (Golab & Ozsu, 2003 ） ：
A data stream IS a real-time, continuous ， ordered (implicitly by arrival
time of explicitly by timestamp) s equence of items
lt is impossible tO control the order in which items arrive, nor it is
feasible tO locally tore stream in lts entirety
````

### 图片文字 OCR（en-US，待对照原页）

````text
What is data stream?
Large data volume, likely structured, arriving at a very high
rate (high enough that machine cannot keep up it)
Definition (Golab & Ozsu, 2003):
A data stream is a real-time, continuous, ordered (implicitly by arrival
time of explicitly by timestamp) sequence of items
It is impossible to control the order in which items arrive, nor it is
feasible to locally tore stream in Its entirety
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=4)

### 原始文字层

````text
Massive data stream
4
 We do not know entire data set 
in advance
 Data arrives in the streaming 
fashion and if it is not processed 
immediately, it will be lost 
forever 一
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Massive data stream
2023
THE INTERNET IN
EVERY MINIJTE
We do not know entire data set
in advance
Data arrives in th e streaming
fashion and if it is not processed
immediately, it will be lost
forever
（ 0 ）
22 ， 831
visitS tO
ChatGPT
271 ， 309
IOS Android
app downloads
3 ． 02M
241 · 2M
emails sent
1 & 8M
text mes-sages
sent
2 ． 4M
G009 | e seucms
phOtOS created
With sm 满 tp 》 № n05
6 ， 94M
emoji sent
11 ， 834
chats on
M'ctOS0ft Teams
34 ， 247
引 a 球 messages
60
694 ， 000
video hours viewed
SECONDS
347 ， 2z2
tweets
3 ． 47M
引 P5 created
0
6 · 3 浒
tO 巧 《 Zoom
11 ， 035
eting minutes
fake accounts
removed
10 ． 4 M
minutes
0
Created by: eDiscovery Today & LTMG
````

### 图片文字 OCR（en-US，待对照原页）

````text
Massive
data stream
2023
THE INTERNET IN
EVERY MINUTE
We do not know entire data set
in advance
Data arrives in the streaming
fashion and if it is not processed
immediately, it will be lost
forever
•o
22,831
visits to
ChatGPT
271,309
IOS g Android
app downloads
3.02M
241.2M
emails sent
18.8M
text messages
sent
2.4M
Google seucms
photos created
With smartphones
6.94M
emoji sent
11,834
chats on
Microsoft
34,247
Slack messages
60
SECONDS
694,000
video hours viewed
347,222
tweets
3.47M
snaps created
6.3M
etal Zoom
11,035
eting minutes
fake accounts
removed
10.4M
viewing
minutes
Created by: eDiscovery Today & L T MG
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=5)

### 原始文字层

````text
5
````

### 图片文字 OCR（en-US，待对照原页）

````text
2019
This Is What Happens In An
Internet Minute
facebook,
Go gle 1 Million
Logging In
3.8 Million
Search
NETFLIX
Queries
Tube
18.1 Million
Texts Sent
4.5 Million
Videos Viewed
2027
This Is What Happens In An
Internet Minute
facebook
YouC,D
Linked ff
.4 2'. Million,
texts Sent
500 Hours
694,444
Hours
Watched
$996,956
Spent Online
2.1 Million
Snaps
Created
41.6Mi11ion
Messages
Sent
4.8 Million
Gifs Served
0
o
60
o
SECONDS
App Store
390,030
Apps Downloaded
347,222
Scrolling Instagram
87,500
People Tweeting
1.4 Million
Swipes
tinder
188 Million
Emails Sent
9,132
NETFLIX
24000
$16 Million
Smnt
3.4
69 Million
Million
imgur
932
60
SECONDS
o
41
414,764
Apps
695,000
Stcgies Shoed
197.6
.0
GIPHY 180
Smart Speakers
Music
Shipped
Streaming
auon
Subscriptions
1 Million
Views
twitch
St•oxd
5,000
twitch
Created By:
Y@LoriLewis
y@OfficiallyChadd
Croted 'y:
SOfficialJyChadd
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=6)

### 原始文字层

````text
Why do we need data stream?
6
 Online, real-time processing
 Potential objectives:
 Event detection and reaction
 Fast and potentially approximate online aggregation and analytics at different 
granularities
 Various applications:
 Network management, telecommunications
 Load balancing in distributed systems
 Stock monitoring, finance, fraud detection
 Online data mining (click stream analysis)
won worse
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Why do we need data stream?
Online, real-time processing
Potential 0b •ectives:
Even detection n eaction
Fast and potentially approximate online aggregation and analytics at different
granularities
Various applications:
Network management, telecommunications
Load balancing in distributed systems
Stock monitoring, finance, fraud detection
Online data mining (click stream analysis)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=7)

### 原始文字层

````text
Data stream applications
7
 Sensor networks:
 Many sensors feeding into a 
mobile devices
 What occurs if the mobile 
device does not have enough 
computational resources for 
real-time event detection?
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Data stream applications
Sensor networks:
Many sensors feeding into a
mobile devices
What occurs if the mobile
device does not have enough
computational resources for
real-time event detection?
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=8)

### 原始文字层

````text
Data stream applications
8
 Google query streams:
 What queries are more frequent today than yesterday?
 Estimate influenza activities by aggregating Google search queries
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Data stream applications
Google query streams:
What queries are more frequent today than yesterday?
Estimate influenza activities by aggregating Google search queries
Using Google to Monitor the Flu
PERCENT OF HEALTH VISITS FOR FLU.UKE SYMPTOMS Mid.At1antic region
8 percent
2003
ESTIMATED
Based on Google
Flu Trends data
tracking flu-related
search terms
2004
ACTUAL
As reported by
U.S. Centers for
Disease Control
2005
Google Flu Trends can estimate the spread of the disease by
measuring the frequency of certain search terms. Its findings
closely track actual C.D.C. data and can, at times, anticipate the
government reports.
C.D.C, does not
keep data for June
through September
OCT.
2006
2007
Sources: Centers for Disease Control
2008
TUE. YORK 11MFS
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=9)

### 原始文字层

````text
Data stream applications
9
 Yahoo click streams:
 What pages are getting an unusual number of hits in the past hour?
 Mining social network:
 Look for trending topics on Twitter, Facebook based on news feed
 IP packets monitored at a switch in network:
 Detect denial-of-service attacks
 Gather information for optimal routing if
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Data stream applications
Yahoo click streams:
What pages are getting an unusual number of hits in the past hour?
Mining social network:
Look for trending topics on Twitter, Facebook based on news feed
IP packets mo itored at a switch in network:
Detect denia -of-service attacks
Gather information for optimal routing
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=10)

### 原始文字层

````text
IP network monitoring application
10
 24x7 IP packet/flow 
data streams at network 
elements
 Massive stream arriving 
at rapid rates
 AT&T collects ~ 1 TB of 
Netflow data per day
 Off-line analysis is very 
slow and expensive
Source Destination Duration Bytes Protocol
 10.1.0.2 16.2.3.7 12 20K http
 18.6.7.1 12.4.0.3 16 24K http
 13.9.4.3 11.6.8.2 15 20K http
 15.2.2.9 17.1.2.1 19 40K http
 12.4.3.8 14.8.7.4 26 58K http
 10.5.1.3 13.0.0.1 27 100K ftp
 11.1.0.6 10.3.4.5 32 300K ftp
 19.7.1.2 16.5.5.8 18 80K ftp
局域网
-
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
《 P network monitoring application
． 24x7 IP packet/flow
data streams at network
elements
Massive Stre am arrivmg
at rapid rates
AT&T collects ～ 1 TB of
Netflow data per day
Off-line analysis is very
SIOW and expensive
Remote
5 e # 2
Remote
5 e # 1
LAN
Source
10 · 1.0 · 2
1 & 6 · 7 · 1
1 3 · 9 · 4 · 3
巧 · 2 ． 2 · 9
12 · 4 ． 3 · 8
10 · 5 ． 1.3
1 1.1.0 · 6
19 · 7 ． 1.2
lnternet
NetFlow
馑 er
NetFlow
Pa e
Destination
16 ． 2 · 3 ． 7
1 2 ． 4 · 0 ． 3
1 1.6 · & 2
17 ． 1.2 ． 1
14 ． 8 · 7 ． 4
1 3 ． 0 · 0 ． 1
10 · 3 · 4 · 5
16 ． 5 · 5 ． 8
Durati on
1 2
1 6
1 9
2 6
27
3 2
1 8
NetFjow
Collector
FIOW Storoge
B es
20K
24K
20K
40K
58K
100K
300K
80K
力 0 s
Console
Protocol
http
http
http
http
http
0
````

### 图片文字 OCR（en-US，待对照原页）

````text
IP network monitoring application
24x7 IP packet/ flow
data streams at network
elements
Massive stream arriving
at rapid rates
AT&T collects 1 TB of
Netflow data per day
Off-line analysis is very
slow and expensive
Remote
Site #2
Remote
Site #1
LAN
Source
10.1.0.2
18.6.7.1
13.9.4.3
15.2.2.9
12.4.3.8
10.5. 1.3
1 1.1.0.6
19.7. 1.2
Internet
NetFlow
Exporter
NetFlow
Packets
Destination
16.2.3.7
12.4.0.3
11.6.8.2
17.1.2. 1
14.8.7.4
1 3.0.O. I
10.3.4.5
16.5.5.8
NetFjow
Collector
Queries
Flow Storage
20K
24K
20K
40K
58K
100K
300K
80K
Analysis
Console
Protocol
Duration
12
16
15
26
27
32
18
http
http
http
http
http
ftp
ftp
ftp
.10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=11)

### 原始文字层

````text
Stream processing model
Processor
Limited
Working
Storage
. . . 1, 5, 2, 7, 0, 9, 3
. . . a, r, v, t, y, h, b
. . . 0, 0, 1, 0, 1, 1, 0
 
 time
Continuous
queries
Output
Archival
Storage
Standing
Queries
Streams arriving
Each of stream is composed of 
elements/tuples
Impossible 
to answer 
queries from 
this storage
Collect summaries of 
streams to answer 
queries from this storage
Easy queries 
to answer at 
any time
Hard queries 
to answer at 
any time
mmds.org (chapter 4)
档案
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
St  re am   pro ce s s ing mo d e l
                                                                                                                                        Hard   quer  ies
                                                                               Co   n t i  nu o   u s                                   to answer   at
                   Stre ams ar   riv ing                                            que rie s                                           any   tim  e
         Eac  h of stream is c  ompos  ed   of                                                                                          Eas y quer  ies
                   elements/tup   le  s                                                                                                 to answer   at
                  .    .    .    1  ,    5  ,    2  ,    7  ,    0  ,    9  ,    3Sta   ndi ng                                          any   tim  e
                    .    .    .            a    ,    r,    v,    t    ,    y,    h    ,    bQue ries
                  .    .    .    0  ,    0  ,    1  ,    0  ,    1  ,    1  ,    0                                                 Outp   ut
                                                                                   Processor
                                         ti me
                                                                                                                                                Im  poss ible
                                                                                                                                                to answer
Collect   sum  mari es of                                                                                                                       quer  i es  from
s treams  to   answer                                            Limit  ed                                 Archival档案                           th is  stor  age
quer  i es  from   th is  stor  age                              Work ing                                   Sto rage
                                                                  Storage                                                                 m mds. or g (chap  te r  4)
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Stream processing model
Streams
Each of stre am is composed of
elements/tuples
· 0 ， 0 ， 1 ， 0 ， 1 ， 1 ， 0
一 tlme
Collect summaries of
streams tO answer
queries from this storage
Continuous
querles
Standing
Queries
PIAO cessor
Limited
、 vorking
Storage
Hard queries
tO answer at
any time
Easy queries
tO answer at
any time
Output
lmpossible
tO answer
queries from
this storage
Archival
Storage
mmds.org (chapter 4 ）
````

### 图片文字 OCR（en-US，待对照原页）

````text
Stream processing model
Streams arriving
Each of stream is composed of
elements/ tuples
Collect summaries of
streams to answer
queries from this storage
Continuous
queries
Standing
Queries
Processor
Limited
Working
Storage
Hard queries
to answer at
any time
Easy queries
to answer at
any time
Output
Impossible
to answer
queries from
this storage
Archival
Storage
mmds.org (chapter 4)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=12)

### 原始文字层

````text
Structure of data stream
12
 Infinite sequence of items (elements) which have the same 
structured information, e.g. 
 Tuple: (Source, Destination, Duration, Bytes, Protocol)
 Object: a user ID or a search query
 Timestamp:
 Explicit (date/time field in data)
 Implicit (arrival time as a sequence of integers)
 Unbounded length, no control of arrival order and data rate
it
明确的
隐式的 nnr
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Structure Of data stream
lnfinite sequence 0f items (elements) which have the same
structured information ， e.g.
Tuple ： (Source, Destination, Duration ， Bytes, Protocol)
Object: a user ID or a search query
Timestam
Ex li cit (date/ time field in data)
lmplicit (arrival tim e as a sequence Of integers)
Unbounded length ， no control of arrival order and data rate
12
````

### 图片文字 OCR（en-US，待对照原页）

````text
Structure of data stream
ifk
Infinite sequence of items (elements) which have the same
structured information, e.g.
Tuple: (Source, Destination, Duration, Bytes, Protocol)
Object: a user ID or a search query
Timestam
Ex licit (date/ time field in data)
Implicit (arrival time as a sequence of integers)
Unbounded length, no control of arrival order and data rate
12
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=13)

### 原始文字层

````text
Data management approaches
13
https://vasia.github.io/dspa20/index.html
unchanging
data
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
D  ata   management   app  ro ach e s
              unchanging
               data
                         ht tp s:// vasia. git hub. io /d sp a20 /in dex. ht ml
                                                                                        13
````

### 图片文字 OCR（en-US，待对照原页）

````text
Data management approaches
static data
Data Warehouse
• complex, offline analysis
• large and relatively static and
historical data
• batched updates during
every night
Streaming Data
Warehouse
• low-latency materialized view
updates
• pre-aggregated, pre-processed
streams and historical data
storage
DW
SDW
DBMS
DSMS
streaming data
Database Management
System
• ad-hoc queries, data
manipulation tasks
• insertions, updates, deletions of
single row or groups of rows
analytics
Data Stream
Management System
• continuous queries
• sequential data access, high-rate
append-only updates
13
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=14)

### 原始文字层

````text
DSMS vs. DBMS
14
 Data stream management system (DSMS):Voluminous streams-in, 
reduced streams-out
 Database management system (DBMS): Output of DSMS can be 
treated as data feeds to database
https://homepages.cwi.nl/~boncz/bads/streaming.shtml
2
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
DSMS vs. DBMS
data feeds
queries
DBMS
data streams
DSMS
DSMS
queries
i nl
Data stream management system (DSMS): Voluminous streams-in,
reduce s reams-out
Database management system (DBMS): Output of DSMS can be
treated as data feeds to database
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=15)

### 原始文字层

````text
DSMS vs. DBMS
https://vasia.github.io/dspa20/index.html 15
_ __
特别掀
no
延迟
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
DSMS vs ． DBMS
DBMS
Data
persistent relations
Data Access
random
U pdates
arbitraty
relatively IOW
Update rates
quey-driven / pull-based
Queries
ad-hoc
Latency
relatively high
DSMS
streams
append-only
high, bursty
data-driven / push-based
continuous
low
15
````

### 图片文字 OCR（en-US，待对照原页）

````text
DSMS vs. DBMS
DBMS
Data
persistent relations
Data Access
random
Updates
arbitrary
relatively low
Update rates
query-driven / pull-based
Queries
ad-hoc
Latency
relatively high
DSMS
streams
sequenti , single-pass
append-only
high, bursty
data-driven / push-based
continuous
low
15
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=16)

### 原始文字层

````text
Outline
16
 Introduction
 Definition, applications, challenges
 Data stream processing
 Data stream modelling
 Data stream processing
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Outline
Introduction
Definition, applications, challenges
Data stream processing
Data stream modelling
Data stream processing
16
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=17)

### 原始文字层

````text
Modeling data stream
17
up-to-date frequencies of specific (srcIP, destIP)
 A stream can be viewed as never-ending updates of one￾dimensional vector A[1…N] with an unknown N
 The j-th update with the form 
(k, c[j]) modifies the k-th entry 
of A as A[k]←A[k] + c[j]
https://vasia.github.io/dspa20/index.html
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Modeling data stream
A stream can be viewed as never-ending updates of one-
dimensional vector All ON] with an unknown N
No. of active connections
(10.1.3.4, 128.11.10,1)
The j -th update with the form
(k, c[j]) modifies the k-th entry
Of A as +
N: 264
(sourcelP, destinationlP)
up-to-date frequencies of specific (srcIP, destIP)
h
17
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 18 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=18)

### 原始文字层

````text
Time-series model
18
 The j-th update (j, A[j])
 Updates arriving in increasing 
order of j as a time series
 Entries of A are observed with 
the increasing index
 Drawback:
 Cannot change the past entries
 Only practical value for 
modeling time series data 
(sensor data, stock data, etc)
https://www.mfe.govt.nz/fresh-water
i
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Time-series model
The j-th update j A[j])
Updates arriving in increasing
order of j as a time series
Entries o A are observe with
the increasing index
Drawback:
Cannot change the past entries
Only practical value for
modeling time series data
(sensor data, stock data, etc)
6000 -
4000 -
uj
2000 -
o-
2008
Papakura Stream at Porchester Rd Bridge
2010
Measurement Time-Series
2012
14
18
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 19 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=19)

### 原始文字层

````text
Cash-register model
19
https://vasia.github.io/dspa20/index.html
 Allow multiple updates that 
only increment an entry in A:
 The j-th update (k, c[j]) increases 
A[k] by a value c[j] ≥ 0
 Drawback:
 Only practical value for insertion￾only data stream since the old data 
are still in the history
when_ 傾
一
值
只有盥
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Cash-register model
． Allow multiple updates that
ly increment
an entr ． A•
． Th e j-th update (), c[j]
lncreases
A[kl c[jl - 亻
． Drawback:
O nly pra cti cal value for insertion-
only data stream since the old data
are s till in the history
NO. Of active connecfions
（ 10 、 13 ． 4 ， 12 & 11 ． 10 / 1 ）
(sourceIP, destinationIP)
N= 264
19
````

### 图片文字 OCR（en-US，待对照原页）

````text
Cash-register model
Allow multiple updates that
ly increment
an entr A:
Ot' The j-th update (k, c[j])
increases
A[kl by a value c[jl
Drawback:
Only practical value for insertion-
only data stream since the old data
are still in the history
No. of active connections
(10.1.3.4, 128.11.10,1)
(sourcelP, destinationlP)
N = 264
19
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 20 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=20)

### 原始文字层

````text
Turnstile model
20
DOS attack, Obinna Igbe et al.’17
 Allow multiple updates that 
increment/decrement an 
entry in A:
 The j-th update (k, c[j])
updates A[k] by A[k] + c[j]
for any c[j]
 Drawback:
 It is challenging to design space 
and time-efficient algorithms for 
this general model
闸机
an T 小
磁
-
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Turnstile model
． Allow multiple updates that
ncrement/ decrement
entry in A:
． Th e j-th update (), c[j]
updates A [kl by A [kl + c[jl
for any c[j]
． Drawback:
lt is challenging to design space
and time-efficient a orithms or
this genera mo del
Attacker
Controller
Zombie 1
Zombie 2
Zombie 3
Router
Victim
Zombie n
DOS attack, Obinna lgbe et al. ， 17
20
````

### 图片文字 OCR（en-US，待对照原页）

````text
Turnstile model
Allow multiple updates that
Increment/ decrement
an
entry in A:
The j-th update (k, c[j])
updates A[kl by A[kl +
for any c[j]
Drawback:
It is challenging to design space
and time-efficient a orithms or
this genera model
Attacker
Controller
Zombie 1
Zombie 2
Zombie 3
Router
Zombie n
DOS attack, Obinna Igbe et al.' 17
Victim
20
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 21 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=21)

### 原始文字层

````text
Outline
21
 Introduction
 Definition, applications, challenges
 Data stream processing
 Data stream modelling
 Data stream processing
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Outline
Introduction
Definition, applications, challenges
Data stream processing
Data stream modelling
Data stream processing
21
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 22 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=22)

### 原始文字层

````text
DSMS architecture
22
Online queries
````

### 图片文字 OCR（en-US，待对照原页）

````text
DSMS
input
monitor
streaming
inputs
Online queries
a rch itectu re
storage
working
storage
summary
storage
static
storage
DSMS
query
monitor
query
processor
query
repository
user
queries
output
buffer
streaming
outputs
22
www.cwi.nl/—boncz/ba
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 23 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=23)

### 原始文字层

````text
Challenges
23
 Stream properties:
 Infinite and non-stationary
 Rapid rate, never-ending, so impossible to store the entire stream accessibly
 How do we process the 
stream using a distributed 
dataflow to answer queries as 
quickly as possible?
 Exact solutions are possible by 
parsing and manipulating inputs 
on-the-fly
 Distributed dataflow systems: 
Spark, TensorFlow, Flink, etc
https://en.wikipedia.org/wiki/Distributed_data_flow
(written by Krzysztof Ostrowski)
wwrnre
sentence
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Challenges
e Stream properties:
Infinite and non-stationary
Rapid rate, never-ending, so impossibl
t
stor
layer 1
layer 2
o
e entire stream accessibly
event eg occurs ("flows")
at node x3, at time t6
How do we process the
distributed
stream using a
dataflow to answer queries
as
quick y as possible
Exact solutions are possible by
parsing and manipulating inputs
on-the-fly
istributed dataflow systems:
Spark, TensorFI
etc
distributed
data flow
time
e8æö
til I
layer 1
layer 2
o
layer 1
layer 2
o
node x3
node Xl
node
location (node)
(written by Krzysztof Ostrowski)
method
•eall
(event)
fünctional
layer
software
physical
machine
(node)
23
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 24 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=24)

### 原始文字层

````text
Challenges
24
https://blog.fastforwardlabs.com/2016/11/23/probabilistic-data-structure-showdown-cuckoo.html
 Stream properties:
 Infinite and non-stationary
 Rapid rate, never-ending, so impossible to store the entire stream accessibly
 How do we process the stream using a limited amount of memory to 
answer queries in real-time manner?
 Exact solutions are often impossible without entirely storing data
 An approximation answer suffices with theoretical guarantees
一
一
年似俺
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Challenges
． Stream properties ：
lnfinite and non-stationary
Rapid rate ， never 一 en ding ， s O impossible tO store the entire stream accessibly
H OW dO we process the stream using a
limited amount Of m em ory
to
real-time manner?
answer querles ln
E xact solutions are Often impossible without entirely stormg data
suffices with
theoretical guarantees
approximation ℃ r
一 Data S ea 勿
>probabiiistic
A1gorithn
24
````

### 图片文字 OCR（en-US，待对照原页）

````text
Challenges
Stream properties:
Infinite and non-stationary
Rapid rate, never-ending, so impossible to store the entire stream accessibly
How do we process the stream using a limited amount of memory
to
answer queries in real-time manner?
Exact solutions are often impossible without entirely storing data
approximaüon answer suffices with
theoretical guarantees
An
— Data Stream
Algorithn
24
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 25 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=25)

### 原始文字层

````text
Basic probabilistic algorithms
25
 Sampling:
 Hashing:
Graham Cormode, Marios Hadjieleftheriou, CACM 2009
用
代表盥1
hash bucket
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Basic probabilistic algorithms
． S ampling ：
． Hashing ：
000
OO
00
hash ket
OO 0
25
Graham Cormode ， Marios Hadjieleftheriou, CACM 2009
````

### 图片文字 OCR（en-US，待对照原页）

````text
Basic probabilistic algorithms
Sampling:
ooooooooooooooooooooooooooo
oooooooooooooooooo
oooooooo
ooooooooooooooooo
Hashing:
•••ooooooooo
oo
Graham Cormode, Marios Hadjieleftheriou, CACM 2009
ooo
oo
hash Lincket
oo o
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 26 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W9-Stream%2BProcessing.pdf#page=26)

### 原始文字层

````text
References
26
 Lukasz Golab and M. Tamer Özsu. Issues in data stream 
management. SIGMOD Rec. 32, 2 (June 2003)
 Michael Stonebraker, Ugur Çetintemel, and Stan Zdonik. 
The 8 requirements of real-time stream processing. 
SIGMOD Rec. 34, 4 (December 2005)
 Data stream lectures: 
 https://homepages.cwi.nl/~boncz/bads/stream.shtml
 https://vasia.github.io/dspa20/lectures/dspa20-1.pdf
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Lukasz Golab and M. Tamer Ozsu. Issues in data stream
management. SIGMOD Rec. 32, 2 (June 2003)
Michael Stonebraker, ugur Cetintemel, and Stan Zdonik.
The 8 requirements of real-time stream processing.
SIGMOD Rec. 34, 4 (December 2005)
Data stream lectures:
htt s: / / home a es.cwi.nl/—boncz/bads/stream.shtml
htt s: / /vasia. ithub.io/ds a20/lectures/ds a 20-1. df
26
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

