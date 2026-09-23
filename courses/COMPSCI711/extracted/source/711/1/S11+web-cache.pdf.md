# S11+web-cache.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI711/source/711/1/S11+web-cache.pdf`
- [打开原文件](../../../../source/711/1/S11%2Bweb-cache.pdf)
- 原文件 SHA-256：`1080195c2339d0153f1884c80054f6f5ee49e745305ba71bb5b8a101ab686f98`
- 文件索引：F062；PDF 总页数：43
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=1)

### 原始文字层

````text
1
Steps on accessing a web site
````

### 图片文字 OCR（en-US，待对照原页）

````text
Steps on accessing a web site
Client
Open
1 Round Trip
Time (RTT)
1 RTT +
Transmit
(Request)
Transmit
Response)
I Request
Server
Establish
Connection
Response
—I ResponseJ •
time
Response Received
1
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=2)

### 原始文字层

````text
2
 The time for DNS server to resolve the web server’s name to 
IP address (if necessary).
 Not shown in the diagram
 The time for the client to set up a TCP connection with the 
web server
 The time for the request transmitted from the client to the 
web server
 The time for the web server to parse the request and generate 
a web page
 The time for the response transmitted from the host to client
 The time when all the information are received by the client
 The time for the client browser to render the page
 Not shown in the diagram
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
•
The time for DNS server to resolve the web server's name to
IP address (if necessary).
• Not shown in the diagram
The time for the client to set up a TCP connection with the
web server
The time for the request transmitted from the client to the
web server
The time for the web server to parse the request and generate
a web page
The time for the response transmitted from the host to client
• The time when all the information are received by the client
The time for the client browser to render the page
Not shown in the diagram
2
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=3)

### 原始文字层

````text
3
How to reduce the response time
 Reduce the network latency (i.e., transmission delay)
 Place servers closer to the clients
 Could be significant
 Reduce the amount of information that have to be sent 
to the clients
 Benefits the users that connect to the servers through low￾bandwidth networks
 For a given bandwidth, less information to be transmitted 
means less time is needed for transmission
 Reduce the load on the web server
 Generate the response faster
 How to achieve these?
 Proxy server, caching server
 A proxy server normally caches web contents. But web contents can 
be cached on other types of servers as well.
焉
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
H ow tO reduce the response time
0 Reduce th e network latency (i.e., transmission delay)
0 Place servers C ose tO th e clients
到 Could be significant
0 Reduce th e amount Of information that have tO be sent
tO th e clients
0 Benef1ts th e users that connect tO th e servers through IOW-
bandwidth networks
0 FOf a glven bandwidth, less information tO be transmitted
means less tlme IS needed fOf transm1SS10fl
0 Reduce th e load on th e web server
0 Generate th e response faster
0 How tO achieve these?
0 PfOXY server, cachlng server
0 proxy server normally caches web contents. But ℃ b contents can
be cached on other types Of servers as well.
3
````

### 图片文字 OCR（en-US，待对照原页）

````text
How to reduce the response time
• Reduce the network latency (i.e., transmission delay)
• Place servers c ose to the clients
Could be significant
• Reduce the amount of information that have to be sent
to the clients
• Benefits the users that connect to the servers through low-
bandwidth networks
• For a given bandwidth, less information to be transmitted
means less time is needed for transmission
Reduce the load on the web server
• Generate the response faster
How to achieve these?
• Proxy server, caching server
A proxy server normally caches web contents. But web contents can
be cached on other types of servers as well.
3
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=4)

### 原始文字层

````text
4
Web Cache 
 A web cache usually sits between the web server 
and clients 
 Watches requests come by and saves copies of the 
responses for them. 
 When there is a coming request for the same URL 
resource, the web cache can retrieve the cached 
response and send it back to the client without 
asking for the web server to serve this request again. 
缓存
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Web Cache
0 A web cache u s ually sits between th e web server
and clients
0 Watches requests come by and S ave S copies Of th e
responses fOf them.
0 When there is a comlng request fOf th e same URL
resource, th e web cache C an retfieve th e cached
response and send it back tO th e client without
as klng fOf th e web server tO S erve thi s request agalfl ·
````

### 图片文字 OCR（en-US，待对照原页）

````text
Web Cache
A web cache usually sits between the web server
and clients
Watches requests come by and saves copies of the
responses for them.
• When there is a coming request for the same URL
resource, the web cache can retrieve the cached
response and send it back to the client without
asking for the web server to serve this request again.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=5)

### 原始文字层

````text
5
cache server
user
````

### 图片文字 OCR（en-US，待对照原页）

````text
cache
user
server
5
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=6)

### 原始文字层

````text
6
cache server
user
file A
server
````

### 图片文字 OCR（en-US，待对照原页）

````text
cache
zrrer)
file A
user
server
6
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=7)

### 原始文字层

````text
7
cache server
user
file A
````

### 图片文字 OCR（en-US，待对照原页）

````text
cache
user
server
file A
7
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=8)

### 原始文字层

````text
8
cache server
user
A
````

### 图片文字 OCR（en-US，待对照原页）

````text
cache
user
server
8
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=9)

### 原始文字层

````text
9
cache server
user
A A
keep copy
````

### 图片文字 OCR（en-US，待对照原页）

````text
keep COP},
cache
user
server
9
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=10)

### 原始文字层

````text
10
cache server
user
file B A
````

### 图片文字 OCR（en-US，待对照原页）

````text
cache
file B
user
server
10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=11)

### 原始文字层

````text
11
cache server
user
A file B
````

### 图片文字 OCR（en-US，待对照原页）

````text
cache
user
server
file B
11
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=12)

### 原始文字层

````text
12
cache server
user
A B
````

### 图片文字 OCR（en-US，待对照原页）

````text
cache
user
server
12
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=13)

### 原始文字层

````text
13
cache server
user
A
B
B
keep copy
````

### 图片文字 OCR（en-US，待对照原页）

````text
cache
user
server
13
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=14)

### 原始文字层

````text
14
cache server
user
file A A
B
````

### 图片文字 OCR（en-US，待对照原页）

````text
cache
file A
user
server
14
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=15)

### 原始文字层

````text
15
cache server
user
A
B
A
````

### 图片文字 OCR（en-US，待对照原页）

````text
cache
user
server
15
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=16)

### 原始文字层

````text
16
Advantages of Web Caching
 Reducing network latency
 There is a distance between clients and web servers. 
 Caching web object locally can dramatically reduce 
transmitting latency 
I 嘫
far
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Advantages of Web Caching
0 Reducing netwofk latency
0 iS a distance between clients and web SefVefS.
0 C aching web object lo cally can dramatically reduce
tran smitting latency
Table 5 · 1 ， 乙 en and Response e
Connection Speed
10 mbps
56 kbps
56 kbps
Lotencv
10 milliseconds
200 milliseconds
500 milliseconds
Response Time
0 ， 5 seconds
6 seconds
8 ， 5 seconds
````

### 图片文字 OCR（en-US，待对照原页）

````text
Advantages of Web Caching
Reducing network latency
• There is a distance between clients and web servers.
Caching web object locally can dramatically reduce
transmitting latency
Table 5-1. Latency and Response Time
Connection Speed
10 mbps
56 kbps
56 kbps
Latency
10 milliseconds
200 milliseconds
500 milliseconds
Response Time
0.5 seconds
6 seconds
8.5 seconds
16
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=17)

### 原始文字层

````text
17
web page
````

### 图片文字 OCR（en-US，待对照原页）

````text
Veb
282
17
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 18 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=18)

### 原始文字层

````text
18
https://pic.com/1.jpg
https://pic.com/2.jpg
````

### 图片文字 OCR（en-US，待对照原页）

````text
https://pic.com/l.jpg
https://pic.com/2.jpg
18
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 19 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=19)

### 原始文字层

````text
19
https://pic.com/1.jpg
https://pic.com/2.jpg
器 器以舆
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
https://pic.com/l.jpg
https://pic.com/2.jpg
````

### 图片文字 OCR（en-US，待对照原页）

````text
https://pic.com/1.jpg
https://pic.com/2.jpg
one C,vønectbh,
geurocZ
282
19
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 20 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=20)

### 原始文字层

````text
20
 Reducing bandwidth consumption
 Cache the web objects close to the client side 
 Reponses to the same requests do not need to be 
transferred again between the proxy server that 
caches the web objects and the origin web server. 
带宽
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
0 Re ducing ba dwidth consumption
0 Cache th e web objects clo se to th e client side
0 Reponses tO th e same requests dO not need tO be
trans ferred again between th e proxy server that
caches th e web objects an d th e Ofigin web server.
20
````

### 图片文字 OCR（en-US，待对照原页）

````text
Reducing ba dwidth consumption
Cache the web objects close to the client side
• Reponses to the same requests do not need to be
transferred again between the proxy server that
caches the web objects and the origin web server.
20
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 21 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=21)

### 原始文字层

````text
21
cache server
user
server
user
比
Üo
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
user
user
Cache
Server
````

### 图片文字 OCR（en-US，待对照原页）

````text
user
user
cache
server
server
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 22 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=22)

### 原始文字层

````text
22
 Reducing server load 
 Some of the requests do not need to be handled by 
the origin server.
 As some requests can be served from proxy servers, 
the origin web server can direct more capability to 
deal with other requests. 
 Improve the response time for the non-cached contents.
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Reducing server load
Some of the requests do not need to be handled by
the origin server.
As some requests can be served from proxy servers,
the origin web server can direct more capability to
deal with other requests.
• Improve the response time for the non-cached contents.
22
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 23 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=23)

### 原始文字层

````text
23
server
user
user
user
user
````

### 图片文字 OCR（en-US，待对照原页）

````text
user
user
user
user
server
23
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 24 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=24)

### 原始文字层

````text
24
server
cache
user
cache
user
cache
user
cache
user
````

### 图片文字 OCR（en-US，待对照原页）

````text
user
user
user
user
cache
cache
cache
cache
server
24
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 25 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=25)

### 原始文字层

````text
25
Categories of Web Caching
 Browser
 Many web browsers support caching. 
 When a web page is first requested, the browser 
saves the web page on the disk. 
 If the page is requested again or the user clicks the 
“Back” button, the cached page might be used.
 In some cases, the browser might need to check with the 
remote web server to see whether the cached page is still 
valid. If it is valid, the page in the local disk is used. 
 Examples: Firefox, Chrome.
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Categories of Web Caching
Browser
Many web browsers support caching.
When a web page is first requested, the browser
saves the web page on the disk.
If the page is requested again or the user clicks the
"Back" button, the cached page might be used.
• In some cases, the browser might need to check with the
remote web server to see whether the cached page is still
valid. If it is valid, the page in the local disk is used.
Examples: Firefox, Chrome.
25
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 26 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=26)

### 原始文字层

````text
26
Proxy Server
 There are two types of proxy servers, i.e., forward
proxy and reverse proxy
 A forward proxy is an intermediate system that enables 
a browser to connect to a remote network to which it 
normally does not have access. A forward proxy can 
also be used to cache data, reducing load on the 
networks between the forward proxy and the remote 
web server.
 A reverse proxy (http accelerator) is installed in front of 
web servers. All connections coming from the Internet 
addressed to one of the web servers are routed through 
the proxy server, which may either deal with the request 
itself or pass the request to the web server behind.
__
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Proxy Server
• There are two types of proxy servers, i.e., forward
proxy and reverse proxy
• A forward proxy is an intermediate system that enables
a browser to connect to a remote network to which it
normally does not have access. A forward proxy can
also be used to cache data, reducing load on the
networks between the forward proxy and the remote
web server.
A reverse proxy (http accelerator) is installed in front of
web servers. All connections coming from the Internet
addressed to one of the web servers are routed through
the proxy server, which may either deal with the request
itself or pass the request to the web server behind.
26
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 27 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=27)

### 原始文字层

````text
27
server
cache
user
cache
user
server
closer
M­ward frproxy
closer
reverse proxy.mn
reduce load
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
closercache                                    ser    ver
    user
Mwa rd   frproxy
                                              closer      ser    ver
              reve   r   s   eproxycache.mn
    user
                                            re   d   u   c   eload
                                                                   27
````

### 图片文字 OCR（en-US，待对照原页）

````text
cache
guersc
ph)Ko
server
closer
server
user
cache
redhCe
loo J
27
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 28 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=28)

### 原始文字层

````text
28
Content Delivery/Distribution Network 
(CDN) 
 CDN is designed to place content caching 
servers at the edge of network around the world. 
 It reduces the traffic congestion on the network 
and the latency perceived by users. 
 The caching servers at the edge side of network 
are called edge servers which can cache HTML 
pages, images, audio and video files. 
 Examples: Akamai, Digital Island
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Content Delivery/ Distribution Network
(CDN)
CDN is designed to place content caching
servers at the edge of network around the world.
It reduces the traffic congestion on the network
and the latency perceived by users.
The caching servers at the edge side of network
are called edge servers which can cache HTML
pages, images, audio and video files.
Examples: Akamai, Digital Island
28
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 29 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=29)

### 原始文字层

````text
29
````

### 图片文字 OCR（en-US，待对照原页）

````text
Client
Forward Proxy
Content Delivery/l)istribution Network
rver
Web Site
Edge Server
Edge Server
Web Server
Edge Server
29
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 30 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=30)

### 原始文字层

````text
30
 When the client requests a web page, the request is 
firstly sent to a forward proxy. 
 The forward proxy then decides which edge server to 
communicate with. 
 If none of the edge servers cache this page, the request is 
delivered to the web server. 
 Otherwise, one of the edge servers , which is closest to the 
client, will serve the request. 
 Examples: Akamai EdgeSuite, IBM WebSphere Edge 
Server
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
• When the client requests a web page, the request is
firstly sent to a forward proxy.
The forward proxy then decides which edge server to
communicate with.
• If none of the edge servers cache this page, the request is
delivered to the web server.
• Otherwise, one of the edge servers , which is closest to the
client, will serve the request.
Examples: Akamai EdgeSuite, IBM WebSphere Edge
Server
30
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 31 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=31)

### 原始文字层

````text
31
Potential problems
 The end user see stale (e.g., old or out-of-date) content, 
compared to what is available on the origin server (i.e., 
fresh content).
 HTTP does not ensure strong consistency
 Caching tends to improve the response times only for 
cached responses that are subsequently requested (i.e., 
hits). 
 Misses that are processed by a cache generally have decreased 
speed. Thus, a cache only benefits requests for content 
already stored in it. 
 Caching is limited by a high rate of change of source 
data.
 Some responses cannot or should not be cached
 Web server will set and send the HTTP headers that 
determine cacheability
匯
只 对多次请求相国生效 降
nnnnz.hntnnnnrmnnre.­datachangeereque.mg
nnnneen￾nnrrn 不应缓存
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Potential problems
0 The end user see s tale (e.g., 艹 out-of-da (e) content,
compared tO what is available on th e Ofig1n server (i.e.,
fresh content) ·
0 HTTP does not ensure strong consistency
0 C aching tends tO improve th e response times only fOf
cached responses that are subsequently req sted (i.e.,
hi t s) ·
0 Misses that focessed a cache enerall have decrease
S eed. us, a cac e only beneflts f quests Of ntent
alread stored i •t.
0 C aching is limited by a high rate of change of source
data.
not be cache
0 Some fesponses cannot Of S O
1
0 Web server will set and send th e HTTP hea ers that
determine cacheabillty
````

### 图片文字 OCR（en-US，待对照原页）

````text
Potential problems
• The end user see stale (e.g., old-or out-of-date) content,
compared to what is available on the origin server (i.e.,
fresh content).
• HTTP does not ensure strong consistency
• Caching tends to improve the response times only for
cached responses that are subsequently req Sted (i.e.,
hits).
• Misses that are rocessed a cache enerall have decrease
s eed. us, a cac e only benefits r quests or ntent
alread stored i •t.
• Caching is limited by a high rate of change of source
data.
dq±m are
not be cache
• Some responses cannot of s o
• Web server will set and send the HTTP hea ers that
determine cacheability
31
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 32 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=32)

### 原始文字层

````text
32
Dynamic Data Page 
 Dynamic data pages are generated by applications 
according to the underlying frequently changing data 
sources such as databases and files. 
 Dynamic data pages are usually generated on the 
demand of user’s request. 
 Dynamic pages have two characteristics: high volatility
and high variation
 It is volatile because not only it changes more frequently but 
also its change is unpredictable. 
 It is various because it is often customized or personalized 
from a set of content fragments. 
 Compared to a static page, a dynamic data page is 
expensive to create. 
 more valuable to cache a dynamic data page
terrestris three seat 性
寙 change
_i_ifrnnee.­co
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Dynamic Data Page
Dynamic data P age s are generated by appllcations
0
according to th e underlying frequently changing data
sources such as databases and flles ·
0 D namic data pa es are usually generated on th e
eman O user S reques
0 Dynam1c P age s have characteristics: high volatility
and high variatlon
烈 咖 亇
0 lt is volatile because not on y it change s more frequently but
also its change IS unpredictable.
0 lt iS vaflous because lt iS Often customized Of personalized
from a set Of content fragments.
0 Com ared tO a statlc p age, a dynamic data p age IS
expenslve O create.
0 more valuable tO ca e dynamic data page
32
````

### 图片文字 OCR（en-US，待对照原页）

````text
Dynamic Data Page
Dynamic data pages are generated by applications
according to the underlying frequently changing data
sources such as databases and files.
D namic data pa es are usually generated on the
eman o user s reques
Dynamic pages have two characteristics: high volatility
Vahons
and high variation
content donje
• It is volatile because not on y it changes more frequently but
also its change is unpredictable.
• It is various because it is often customized or personalized
from a set of content fragments.
• Com ared to a static page, a dynamic data page is
expensive o create.
• more valuable to ca e dynamic data page
32
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 33 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=33)

### 原始文字层

````text
33
Proxy-based Dynamic Page Caching
 Proxy-based caching approaches can be classified into 
three broad categories
 page-level caching 
 fragment-level caching
 data-centric caching
 In the page-level caching , the proxy server caches full￾page outputs.
 Many commercial products have applied this approach.
 Compared to no-caching, the page-level caching has the
following advantages:
 reduce the page generation delay
 reduce the delay associated with packet filtering and other
firewall-related delays
 reduce the bandwidth required to transmit the content from
the web server to the proxy
talk about
一 缓存整个页面
cash server
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Proxy-based Dynamic Page Caching
0 Proxy-based caching approaches c an be classified into
three broad categories
0 page-level caching
0 fragment-level caching
0 data-centfic caching
0 ln th e p age-level caching ， th e PfOXY s erver caches full-
P age utPuts ·
0 Many commercial products have applied th1S approach.
0 Compared to no-caching, th e page-level c a c hing has th e
following advantage s ：
0 reduce th e page generation delay
0 reduce th e delay associated with packet filtering and other
firewall-related delays
0 reduce th e bandwidth required tO transmit th e content from
th e web server tO th e proxy
匚 勿 厂
33
````

### 图片文字 OCR（en-US，待对照原页）

````text
Proxy-based Dynamic Page Caching
• Proxy-based caching approaches can be classified into
three broad categories
• page-level caching
• fragment-level caching
• data-centric caching
In the page-level caching , the proxy server caches full-
page utputs.
• Many commercial products have applied this approach.
Compared to no-caching, the page-level caching has the
following advantages:
• reduce the page generation delay
• reduce the delay associated with packet filtering and other
firewall-related delays
• reduce the bandwidth required to transmit the content from
the web server to the proxy
cosh serve r
33
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 34 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=34)

### 原始文字层

````text
34
 The page-level caching has the following 
limitations
 There is often very little reusability of full HTML 
pages 
 A personalised page displaying the name of the user at the 
top of the page: the cached page in the proxy is only 
reusable if the same user accesses to the same page 
 Unnecessary invalidation
 If there is only one element of the page becomes invalid, 
then the whole page needs to be invalidated in the cache. 
ftp
nnntn
很少有重用
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
0 The page-level c aching has th e following
mltatlon
0 There is often very little reusabi · ty of full HTML
P age s
0 personalised Page displaying th e name of the user at th e
top of th e Page ： th e cached Page in th e PfOXY is only
reusable if th e same user accesses tO th e same p age
Unnecessary invalidation
0
0 If there is only one element of th e p age becomes invalld,
then th e whole Page needs to be invalldated in th e cache.
34
````

### 图片文字 OCR（en-US，待对照原页）

````text
The page-level caching has the following
mitation
There is often very little reusabi •ty of full HTML
pages
A personalised page displaying the name of the user at the
top of the page: the cached page in the proxy is only
reusable if the same user accesses to the same page
Unnecessary invalidation
• If there is only one element of the page becomes invalid,
then the whole page needs to be invalidated in the cache.
34
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 35 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=35)

### 原始文字层

````text
35
weather
navigation
personalize
news
Hello XYZ
orz
seldom change
change weigh
change g hour
比较最新更新的 时间 来决定是否重用
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Hello XYZ
      navig  ation   orz   seldom  change
       we a t h e r      change   weigh
      personalize
         news            change   g   hour
⽐较最新更新的           时间     来  决定是否重⽤
                                     35
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
H ello XYZ
navlgatlon
weather
personalize
news
0
35
````

### 图片文字 OCR（en-US，待对照原页）

````text
Hello XYZ
navigation
weather
personalize
news
gel doh ChFQoe
-7 chaff
D a/eg hour
35
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 36 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=36)

### 原始文字层

````text
36
 Fragment-level caching requires establishing a 
template for each dynamically generated page. 
 The template file specifies the contents and layout of the 
page. 
 Essentially, each page is factored into a number of fragments of 
differing cacheability profiles and different caching expiration 
time. 
 The fragments and the templates of the pages are maintained as 
separate elements on the origin servers and the proxy servers. 
 A web page is assembled at proxy caching server when the page 
is requested. 
 Popularized by Akamai as part of the Edge Side Includes 
(ESI) initiative 
Fragment-level caching 片段级
一一
template page
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Fragment-level caching
0 Ffagment-level cac ng require s e stablishing a
template f0f each dynamic ally generated P age ．
0 The template 劑 e specifies th e contents and layout of th e
P age ·
0 Essentially, each page is factored into a number of fragments of
differing cacheablllty profiles an d different caching expiratlon
t11 嗆 e ·
0 The fragments an d th e templates Of th e pages are maintained as
S eparate elements on th e Ofig1fl servers an d th e proxy servers ·
0 A we b Page is as sembled at PfOXY caching server when th e P age
IS requested.
0 Popularized by Akamai as p art of th e Edge Side lncludes
(E S I) initiative
36
````

### 图片文字 OCR（en-US，待对照原页）

````text
Fragment-level caching
Fragment-level cac ng requires establishing a
template for each dynamically generated page.
The template file specifies the contents and layout of the
page.
• Essentially, each page is factored into a number of fragments of
differing cacheability profiles and different caching expiration
time.
• The fragments and the templates of the pages are maintained as
separate elements on the origin servers and the proxy servers.
• A web page is assembled at proxy caching server when the page
is requested.
Popularized by Akamai as part of the Edge Side Includes
(ESI) initiative
36
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 37 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=37)

### 原始文字层

````text
37
weather
navigation
personalize
news
weather
navigation
personalize
news
template page
check valued
圝
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
te  m  p  l  a  te page
  we a t h e r
navig  ation
personalize
    news                  check     va l u e d      we a t h e r
                                                   navig  ation
                                圝                  personalize
                                                        news
                                                                         37
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
weather
navlgatlon
personalize
news
weather
navlgatlon
personalize
news
````

### 图片文字 OCR（en-US，待对照原页）

````text
weather
navigation
personalize
Cit ck
news
vallÆJ
weather
navigation
personalize
news
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 38 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=38)

### 原始文字层

````text
38
Edge Side Includes (ESI) 
 Edge Side Includes (ESI) is a simple markup language 
used to define web page fragments of differing 
cacheability profiles and different caching expiration 
time. 
 ESI defines some tags that can be used in the template 
files. 
 A template file is a normal HTML file with ESI tags. 
 Amongst the ESI tags, “esi: include” is used to include a 
fragment.
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Edge Side Includes (ESI)
• Edge Side Includes (ESI) is a simple markup language
used to define web page fragments of differing
cacheability profiles and different caching expiration
time.
• ESI defines some tags that can be used in the template
files.
• A template file is a normal HTML file with ESI tags.
• Amongst the ESI tags, "esi: include" is used to include a
fragment.
38
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 39 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=39)

### 原始文字层

````text
39
<html>
<body>
<esi:include src=http://example.com/weather.jsp />
<esi:include src=http://example.com/navigation.jsp />
<esi:include src=http://example.com/personalize.jsp />
<esi:include src=http://example.com/news.jsp />
</body>
</html>
weather
navigation
personalize
news
only edge server can under张
i send request
h to server
return html
f Client
save in edge
area
山
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
<html>
<body>
  <esi:include src=http://example.com/weather.jsp />
  <esi:include                          src=http://example.com/navig  ation.jsp />
  <esi:include                          src=http://example.com/personalize.jsp />
  <esi:include                          src=http://example.com/news.jsp />
</body>
</html>                 only       edge         ser ver           can        under张
                                   we a t h e r                 i  send         re   q   u   e   s   t
                                                               h      to      ser ver
                                  navig  ation                 re   t   u   r   nhtml
                                 personalize                                Client
                                      news                          f
                                                            save           in    edge
                                                                                     area39
                                                                      ⼭
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
<html>
<body>
< esi:include src=http://example.com/weather.j sp / >
< esi:include src=http://example.com/navigation.j sp / >
< esi:include src=http://example.com/personalize.jsp / >
< esi:include src=http://example.com/news.jsp / >
</body>
< /html>
weather
navlgatlon
personalize
news
````

### 图片文字 OCR（en-US，待对照原页）

````text
<html>
< body>
<esi:include src=http://example.com/weather.jsp / >
<esi:include src=http://example.com/navigation.jsp / >
<esi:include src=http://example.com/personalize.jsp / >
<esi:include src=http://example.com news.jsp / >
</body>
< / html>
oqlå e e Cam
weather
navigation
personalize
news
-O sewer.
Cave l? n
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 40 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=40)

### 原始文字层

````text
40
山
set valued
time
t
second request
小
cheek ˇ些
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Content Assembly / Delivery
Edge using ESI
Edge
Client
Browsers
lnternet
Edge
Edge ：
Edg
millions 0f requestS
millions 0f requestS
ESI Fragment
lJpdates
Web |
Server
， 1000s 0f requests
1000s 0f requests
40
````

### 图片文字 OCR（en-US，待对照原页）

````text
Client
Browsers
Content Assembly I Delivery:
on Edge using ESI
Edge rver
Edger rver
Edge erver
Internet
Edge erver
Edge rver
Edge erver
ESI Fragment
Updates
Web
App
IServer
ValuJ
4.............-+ Databa e
millions of requests
millions of requests
10005 of requests
10005 of requests
40
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 41 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=41)

### 原始文字层

````text
41
 Compared with page-level caching approach, 
fragment-level caching approach can improve 
hit rates as it can specify granular caching 
capability. 
 According to the properties of different fragments, 
the fragment can be set with different caching 
expiring time and cacheability.
 Fragment-level caching need the developer to 
partition the pages.
 Might require the re-writing of pages or applications
 Further reading
 https://docs.oracle.com/cd/B14099_19/caching.10
12/b14046/esi.htm
no
wet
击中年
The 高分区或鹚
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
0 Compared with page-level caching approach,
ffagment-level caching approach C an 嗆 fove
hi t fate S as it can specify granulaf cachlng
capability.
0 According to th e properties of different fragments,
th e fragment can be set with different caching
expifing time and cacheability.
《 gment-level caching need th e developer to
partition th e pages,
0 Might require th e re-w iting of P age s 0f applications
0 Fufther re ading
0 http s ：//docs.oracle.com/cd/B14099 一 19 / caching. 10
12/b14046/esi.htm
````

### 图片文字 OCR（en-US，待对照原页）

````text
Compared with page-level caching approach,
fragment-level caching approach can im rove
hit fates as it can specify granular caching
capability.
According to the properties of different fragments,
the fragment can be set with different caching
expiring time and cacheability.
kra ment-level caching need the developer to
partition the pages.
• Might require the re-w iting of pages or applications
Further reading
https://docs.oracle.com/cd/B14099_19/ caching. 10
12 // b 14046 //
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 42 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=42)

### 原始文字层

````text
Review
 What are the main steps in accessing a web 
applications?
 What measures can be used to reduce the response time 
of a web-based application? What is the techniques for 
implementing these measures?
 What does a web cache work? What does a web cache 
do to reduce the response time to web applications?
 Assume that (a) two clients access a web application 
through two connections with different network 
latencies, and, (b) the difference in network latency for 
the two connection is x ms. Explain why the difference 
in response time to the two clients might be 
significantly higher than x ms. 42
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
Review
• What are the main steps in accessing a web
applications?
What measures can be used to reduce the response time
of a web-based application? What is the techniques for
implementing these measures?
• What does a web cache work? What does a web cache
do to reduce the response time to web applications?
Assume that (a) two clients access a web application
through two connections with different network
latencies, and, (b) the difference in network latency for
the two connection is x ms. Explain why the difference
in response time to the two clients might be
significantly higher than x ms.
42
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 43 页

[查看此页](../../../../source/711/1/S11%2Bweb-cache.pdf#page=43)

### 原始文字层

````text
Review
 How do the forward proxy and reverse proxy work?
 Understand how web caches are placed on the Internet and how 
they are used.
 How does a CDN work?
 What are the problems associated with the use of web cache?
 What are dynamic pages and what are the features of the 
dynamic pages?
 Understand how page-level caching and fragment-level caching 
work and the potential problems associated with them.
43
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
•
Review
How do the forward proxy and reverse proxy work?
Understand how web caches are placed on the Internet and how
they are used.
How does a CDN work?
What are the problems associated with the use of web cache?
What are dynamic pages and what are the features of the
dynamic pages?
Understand how page-level caching and fragment-level caching
work and the potential problems associated with them.
43
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

