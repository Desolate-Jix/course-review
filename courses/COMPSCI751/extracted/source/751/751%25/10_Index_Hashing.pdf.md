# 10_Index_Hashing.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI751/source/751/751%25/10_Index_Hashing.pdf`
- [打开原文件](../../../../source/751/751%2525/10_Index_Hashing.pdf)
- 原文件 SHA-256：`b2e7fbd1db6f7fcec3d6f540dfc0a2a74833957fd08b26707e49c174fabbc065`
- 文件索引：F096；PDF 总页数：42
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=1)

### 原始文字层

````text
Miao Qiao
The University of Auckland
Index
````

### 图片文字 OCR（en-US，待对照原页）

````text
Index
Miao Qiao
The University of Auckland
THE UNIVERSITYOF
AUCKLAND
Te Whare Wananga o Tamaki Makaurau
NEW ZEALAND
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=2)

### 原始文字层

````text
Outline
▪ Basic Concepts
▪ Ordered Indices 
▪ B+-Tree Index Files
▪ B-Tree Index Files
▪ Hashing
▪ Write-optimized indices
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Outl ine
▪    Ba sic   Co n ce pt  s
▪    Ordered  Indic es
▪    B+-Tree Index  Files
▪    B-Tree Index  Files
▪    Ha  sh  i n  g
▪    Wr   i  t e-opt imized indic es
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Outline
Basic Concepts
Ordered Indices
B+-Tree Index Files
B-Tree Index Files
Hashing
Write-optimized indices
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=3)

### 原始文字层

````text
Hashing
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Hashing
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=4)

### 原始文字层

````text
Example of Hash Index
hash index on instructor, on attribute ID
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Example of Hash Index
bucket 0
76766
bucket 1
45565
76543
bucket 2
22222
bucket 3
10101
bucket 4
bucket 5
15151
33456
bucket 6
83821
bucket 7
12121
32343
58583
98345
76766
10101
45565
83821
98345
12121
76543
32343
58583
15151
22222
33465
Crick
Srinivasan
Katz
Brandt
Kim
wu
Singh
El Said
Califieri
Mozart
Einstein
Gold
Biology
Comp. Sci.
Comp. Sci.
Comp. Sci.
Elec. Eng.
Finance
Finance
History
History
Music
Physics
Physics
hash index on instructor,
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
72000
65000
75000
92000
80000
90000
80000
60000
62000
40000
95000
87000
on attribute ID
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=5)

### 原始文字层

````text
Static Hashing
▪ A bucket is a unit of storage containing one or more entries (a bucket 
is typically a disk block). 
• we obtain the bucket of an entry from its search-key value using a 
hash function
▪ Hash function h is a function from the set of all search-key values K to 
the set of all bucket addresses B.
▪ Hash function is used to locate entries for access, insertion as well as 
deletion.
▪ Entries with different search-key values may be mapped to the same 
bucket; thus entire bucket has to be searched sequentially to locate an 
entry. 
▪ In a hash index, buckets store entries with pointers to records
▪ In a hash file-organization buckets store records
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Stat ic Hashing
▪      A bucket is   a   unit   of   st  or age c ontaining one   or  more ent  ries   (a buc ket
       is   typically   a   dis k block) .
         •     we   o  b  ta  i n    th  e    bu  ck   et    o  f a  n   e  nt   ry    fr   om     i ts    se  ar   ch-ke  y    va  l ue   u  si n  g   a
               hash function
▪      Ha  sh   f   un  ct   i on   h is   a   func tion   fr om t  he s et   of all s ear ch-ke  y    va  l ue  s K to
       th e  se t    of    a ll b uc  ke t a d dr  e sse s B.
▪      Ha  sh   f   un  ct   i on   i s    u  se  d    to   l o  ca  te   e  nt   ri e  s    fo  r a  cc   es   s,    i ns   er   ti o  n   a  s w   el l     as
       deletion.
▪      En tr  ies   wit  h   dif  fe re n t s  ea rc  h-ke  y    va  l ue  s    m ay    b  e    ma  p  pe  d   to   t   he   s   am e
       bucket;  thus ent ire bucket  has  to be  searched sequentially  to locate an
       ent ry.
▪      In  a  hash i ndex,    bu ck  et   s s  to re  e n trie s    with  p o int   er  s    to  re co r  ds
▪      In  a  hash f il e-organiz ation buckets  store  records
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Static Hashing
•
•
A bucket is a unit of storage containing one or more entries (a bucket
is typically a disk block).
we obtain the bucket of an entry from its search-key value using a
hash function
Hash function h is a function from the set of all search-key values K to
the set of all bucket addresses B.
Hash function is used to locate entries for access, insertion as well as
deletion.
Entries with different search-key values may be mapped to the same
bucket; thus entire bucket has to be searched sequentially to locate an
entry •
In a hash index, buckets store entries with pointers to records
In a hash file-organization buckets store records
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=6)

### 原始文字层

````text
Handling of Bucket Overflows
▪ Bucket overflow can occur because of 
• Insufficient buckets 
• Skew in distribution of records. This can occur due to two reasons:
▪ multiple records have same search-key value
▪ chosen hash function produces non-uniform distribution of key 
values
▪ Although the probability of bucket overflow can be reduced, it cannot be 
eliminated; it is handled by using overflow buckets.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Handling of  Bucket  Overf lows
 ▪     Bu ck  et   o ve rflo w   ca n   oc  cu r   be ca u se  o f
         •    In su ff   icie nt    b uc  ke ts
         •    Sk  ew   in  d istr  ibu tio n  o f r  e co rd s.    Th is c  an  o cc  ur   d ue  t  o   two  r  e as  on s:
                ▪    mu ltip le   re co rd s   ha ve  s ame  se a rc h-ke  y    va  l ue
                ▪    ch  o  se  n    ha  sh   f   un  ct   i on   p  r  od  u  ce  s n  o  n-unif orm distribut ion of  key
                     va  l u  es
 ▪     Alt  ho u gh  t  he  p ro b ab ility   o f b u cke t   ov  er  flo w   ca n   be  r  ed u ce d,   it   ca nn o t b e
       eliminated; it  is  handled by using overflow  buckets.
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Handling of Bucket Overflows
Bucket overflow can occur because of
Insufficient buckets
Skew in distribution of records. This can occur due to two reasons:
multiple records have same search-key value
chosen hash function produces non-uniform distribution of key
values
Although the probability of bucket overflow can be reduced, it cannot be
eliminated; it is handled by using overflow buckets.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=7)

### 原始文字层

````text
Handling of Bucket Overflows (Cont.)
▪ Overflow chaining – the overflow buckets of a given bucket are chained 
together in a linked list.
▪ Above scheme is called closed addressing (also called closed hashing 
or open hashing depending on the book you use) 
• An alternative, called 
open addressing 
(also called 
open hashing or
closed hashing 
depending on the 
book you use) which 
does not use over￾flow buckets, is not 
suitable for database 
applications.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Handling of  Bucket  Overf lows ( Cont .)
▪      Overfl ow  chaining – th e  o ve rf   low   b uc  ke ts    of    a  g ive n    bu ck  et    a re  ch a ine d
       to g et   he r   in  a  lin ke d    list.
▪      Ab o ve  sc  he me   is c  alle d  closed addressing (                                           also called closed hashi ng
       or open  hashing depending  on t he book you use                                                          )
          •     An  a lte rn a tive ,   ca lled
                open  addressing
                (also called
                open  hashing or
                closed hashi ng
                depending  on t he
                book  you  use) which
                does  not  use  over-
                flo w    bu ck  et   s,    is n o t
                su  i ta  b  l e    fo  r    da  ta  b  as   e
                applications.
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Overflow chaining — the overflow buckets of a given bucket are chained
together in a linked list.
Above scheme is called closed addressing (also called closed hashing
or open hashing depending on the book you use)
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
An alternative, called
open addressing
(also called
open hashing or
closed hashing
depending on the
book you use) which
does not use over-
flow buckets, is not
suitable for database
applications.
bucket 0
bucket 1
bucket 2
bucket 3
overflow buckets for bucket 1
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=8)

### 原始文字层

````text
Example of Hash File Organization 
Hash file organization of instructor file, using dept_name as key.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Ex a mp le  of  Ha sh  Fi le  Or gani za t ion
    Ha  sh   f   i l e    or  g  an  i za  ti o  n   o  f instr uctor file ,    us  ing  dept_name as key.
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Example of Hash File Organization
Hash file organization of instructor file, using dept_name as key.
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
bucket 0
bucket 1
15151 Mozart
bucket 2
32343 El Said
58583 Califieri
bucket 3
22222 Einstein
33456 Gold
98345 Kim
Music
History
History
Ph sics
Physics
Elec. Eng.
40000
80000
60000
95000
87000
80000
bucket 4
12121 wu
76543 Sin h
bucket 5
76766 Crick
bucket 6
Finance
Finance
Biolo
90000
80000
72000
10101 Srinivasan Comp. Sci. 65000
Com . Sci. 75000
45565 Katz
83821 Brandt Comp. Sci. 92000
bucket 7
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=9)

### 原始文字层

````text
Deficiencies of Static Hashing
▪ In static hashing, function h maps search-key values to a fixed set of B of 
bucket addresses. Databases grow or shrink with time. 
• If initial number of buckets is too small, and file grows, performance 
will degrade due to too much overflows.
• If space is allocated for anticipated growth, a significant amount of 
space will be wasted initially (and buckets will be underfull).
• If database shrinks, again space will be wasted.
▪ One solution: periodic re-organization of the file with a new hash function
• Expensive, disrupts normal operations
▪ Better solution: allow the number of buckets to be modified dynamically.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Defi cienci es  of St atic  Hashing
 ▪      In  s  ta tic    ha sh in g,    fu n ctio n  h ma ps  se a rch-ke  y    va  l ue  s    to   a   fi x   ed   s   et    o  f B of
        bucket addresses.  Databases grow or shrink  with t ime.
          •     If    in itia l n umb e r o f    bu ck  et   s is   to o  sma ll,    an d  file  g ro ws  , p e rf   or  man ce
                wi l l     de  g  ra  d  e    du  e   to   t   oo   m u  ch   o  ve  rf   l ow   s.
          •     If    sp a ce  is    allo ca te d  fo r   a nt   icip at   ed  g ro wt   h,    a  sig n ifica n t a mo un t    of
                sp  a  ce   wi l l     be   w  as   te  d    i ni t   i al l y    (  an  d   b  uc   ke  ts    wi l l  b  e   underf ull).
          •     If    d at   ab a se  sh r  ink  s,    ag a in    sp ac  e    will b e  wa st   ed .
 ▪      One s olution: periodic re-organizat ion of  the  file wit h  a  new  hash f unct ion
          •     Ex  pe n sive ,   dis  ru pt  s n o rma l o pe r  at  ion s
 ▪      Be tt  er   so lu tio n:   a llow   th e  n umb e r o f   bu ck  et  s t  o   be  mo d ifie d   dy  na mica lly.
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Deficiencies of Static Hashing
• In static hashing, function h maps search-key values to a fixed set of Bof
bucket addresses. Databases grow or shrink with time.
If initial number of buckets is too small, and file grows, performance
will degrade due to too much overflows.
If space is allocated for anticipated growth, a significant amount of
space will be wasted initially (and buckets will be underfull).
If database shrinks, again space will be wasted.
One solution: periodic re-organization of the file with a new hash function
Expensive, disrupts normal operations
Better solution: allow the number of buckets to be modified dynamically.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=10)

### 原始文字层

````text
Dynamic Hashing
▪ Periodic rehashing
• If number of entries in a hash table becomes (say) 1.5 times size of 
hash table, 
▪ create new hash table of size (say) 2 times the size of the 
previous hash table
▪ Rehash all entries to new table
▪ Linear Hashing
• Do rehashing in an incremental manner
▪ Extendable Hashing
• Tailored to disk based hashing, with buckets shared by multiple hash 
values
• Doubling of # of entries in hash table, without doubling # of buckets
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Dy na mic  Ha s hing
▪      Pe rio d ic r  e ha sh in g
         •     If    n umb e r o f    en tr  ie s in  a  h a sh  ta b le    be co mes   (  sa y)    1.   5    time s s  ize  o f
               hash  table,
                  ▪    cr  e  at   e    ne  w    ha  sh   t   ab  l e   o  f s   i ze    (  sa  y)   2   ti m e  s t   he   s   i ze   o  f t   he
                       previous hash table
                  ▪    Re  h  as   h    al l     en  tr   i e  s t   o    ne  w    ta  bl e
▪      Linear  Hashing
         •     Do   r   e  ha  sh  i n  g    i n    an   i n  cr   em e  n  ta  l  m an  n  er
▪      Ex  te nd a ble  H  as  hin g
         •     Tailor ed t o  dis k based  hashing,  wit h  buck et s s har ed by  multiple has h
               va  l u  es
         •     Do  u  bl i n  g   o  f #   o  f    en  tr   i e  s i n   h  a  sh   ta  b  l e,    wi t   ho  u  t d  o  ub  l i n  g    #    of    b  uc   ke  ts
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Dynamic Hashing
Periodic rehashing
If number of entries in a hash table becomes (say) 1.5 times size of
hash table,
create new hash table of size (say) 2 times the size of the
previous hash table
Rehash all entries to new table
Linear Hashing
Do rehashing in an incremental manner
Extendable Hashing
Tailored to disk based hashing, with buckets shared by multiple hash
values
Doubling of # of entries in hash table, without doubling # of buckets
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=11)

### 原始文字层

````text
Extendable Hashing
▪ Extendable hashing – one form of dynamic hashing 
• Hash function generates values over a large range — typically b-bit 
integers, with b = 32.
• At any time use only a prefix of the hash function to index into a table 
of bucket addresses. 
• Let the length of the prefix be i bits, 0  i  32. 
▪ Bucket address table size = 2i. Initially i = 0
▪ Value of i grows and shrinks as the size of the database grows 
and shrinks.
• Multiple entries in the bucket address table may point to a bucket 
(why?)
• Thus, actual number of buckets is < 2i
▪ The number of buckets also changes dynamically due to 
coalescing and splitting of buckets.
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Extendable Hashing
• Extendable hashing — one form of dynamic hashing
Hash function generates values over a large range — typically b-bit
integers, with b = 32.
At any time use only a prefix of the hash function to index into a table
of bucket addresses.
Let the length of the prefix be i bits, 0 < is 32.
Bucket address table size = 21• Initially i = 0
Value of i grows and shrinks as the size of the database grows
and shrinks.
Multiple entries in the bucket address table may point to a bucket
(why?)
Thus, actual number of buckets is < 21
The number of buckets also changes dynamically due to
coalescing and splitting of buckets.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=12)

### 原始文字层

````text
General Extendable Hash Structure 
In this structure, i2 = i3 = i, whereas i1 = i – 1 (see next slide for details)
i i1
i2
i3
bucket 1
bucket 2
bucket 3
00..
01..
10..
11..
bucket address table
hash prefix
…
…
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
General  Ext endable Hash St ructur e
                         hash prefix
                           i                                   i1
                    00..
                    01..                                              bucket 1
                    10..                                       i
                                                               2
                    11..
                                                                      bucket 2
                                                               i3
                       bucket address table                           bucket 3
      In  t   his   st   ru ct   ur  e,    i2 = i3 = i,    wh er  e as   i1 = i – 1 (see  next  slide for  details)
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
General Extendable Hash Structure
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
hash prefix
00..
01..
10..
11..
bucket address table
In this structure, i2 = i3 = i, whereas
13
bucket 1
bucket 2
bucket 3
1 (see next slide for details)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=13)

### 原始文字层

````text
Use of Extendable Hash Structure
▪ Each bucket j stores a value ij
• All the entries that point to the same bucket have the same values on 
the first ij bits.
▪ To locate the bucket containing search-key Kj
:
1. Compute h(Kj
) = X
2. Use the first i high order bits of X as a displacement into bucket 
address table, and follow the pointer to appropriate bucket
▪ To insert a record with search-key value Kj
• follow same procedure as look-up and locate the bucket, say j. 
• If there is room in the bucket j insert record in the bucket. 
• Else the bucket must be split and insertion re-attempted (next slide.)
▪ Overflow buckets used instead in some cases (will see shortly)
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Use of  Ext endable  Hash St ructur e
▪    Ea ch  b u cke t j st   or  e  s a   v   al u  e   ij
       •    All t  he entr ies  that point   to t  he s ame buc ket have the same values  on
            th e  fir  st    ij bits.
▪    To locate the buc ket c ontaining s earc h-ke  y Kj:
       1.   Co  m p  ut   e h(Kj) = X
       2.   Us   e    th  e    fi r   st i high order  bit s of X as a displacement  int o  bucket
            address t able, and  follow the pointer  to appropriate bucket
▪    To insert  a  record w ith searc h-ke  y    va  l ue   Kj
       •    fo llo w s  ame  p ro ce d ur  e  a s lo o k-up  and locate the bucket,  say                    j.
       •    If    th e re  is   ro o m in  th e  b uc  ke t j insert   recor d   in   the   buck et  .
       •    Els  e   th e   bu ck  et   mus  t b e  sp lit   an d  in se rt  ion  r  e-attempted  (next slide.)
              ▪  Overf low buc kets  us ed inst ead in some  cases (will  see  shortly)
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Use of Extendable Hash Structure
Each bucket j stores a value ij
All the entries that point to the same bucket have the same values on
the first ij bits.
To locate the bucket containing search-key Kj:
Compute h(Kj) = X
Use the first i high order bits of Xas a displacement into bucket
2.
address table, and follow the pointer to appropriate bucket
To insert a record with search-key value Kj
follow same procedure as look-up and locate the bucket, say j.
If there is room in the bucket j insert record in the bucket.
Else the bucket must be split and insertion re-attempted (next slide.)
Overflow buckets used instead in some cases (will see shortly)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=14)

### 原始文字层

````text
Insertion in Extendable Hash Structure (Cont.) 
▪ If i > ij (more than one pointer to bucket j)
• allocate a new bucket z, and set ij = iz = (ij + 1)
• Update the second half of the bucket address table entries originally 
pointing to j, to point to z
• remove each record in bucket j and reinsert (in j or z)
• recompute new bucket for Kj and insert record in the bucket (further 
splitting is required if the bucket is still full)
▪ If i = ij (only one pointer to bucket j)
• If i reaches some limit b, or too many splits have happened in this 
insertion, create an overflow bucket 
• Else
▪ increment i and double the size of the bucket address table.
▪ replace each entry in the table by two entries that point to the same 
bucket.
▪ recompute new bucket address table entry for Kj
Now i > i
j
 so use the first case above. 
To split a bucket j when inserting record with search-key value Kj
:
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
In s  e  rt  io n  i  n   E xt  e  n da  b le     H as  h  S t  ru c  tu r  e   (C o n t  .)
    To                                  s                    p            l                i                t                                    a                                  b                  u            c                    k              e                  t                j wh  e  n    i ns   er   ti n  g   re  co  r   d    wi th   s   ea  rc   h-ke  y    va  l ue   Kj:
     ▪       If    i > ij (more than one pointer to bucket j)
               •      allocat e  a  new  bucket  z,    an d  se t ij = iz =     (ij +    1)
               •      Up  d  at   e    th  e    se  co  nd   h  a  l f o  f    th  e    bu  ck   et    a  dd  r   es   s t   ab  l e   e  nt   ri e  s o  r   i gi n  a  l l y
                      pointing to j, to  p o int    to  z
               •      remove each record in bucket j and reinsert (in j or z)
               •      recompute new bucket for Kj and insert record in the bucket (furt her
                      sp  l i tt   i ng   i s    r  eq  u  i re  d    i f t   he   b  u  cke  t    i s s   ti l l  f   ul l )
     ▪       If    i = ij (only one pointer to bucket j)
               •      If    i reaches some limit b,    or   t   oo  ma ny   sp lits   h av  e    ha p pe n ed  in  t   his
                      insert  ion,   create an   ov er flow   buck et
               •      Els  e
                        ▪    incr ement   i and double the size of the bucket address table.
                        ▪    replace each entry in the table by two entries that point to the same
                             bucket.
                        ▪    recompute new bucket address table entry for                                                        Kj
                             No  w i > ij  so   u  se   t   he   f   i rs   t c   as   e    ab  o  ve  .
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Insertion in Extendable Hash Structure (Cont.)
To split a bucket j when inserting record with search-key value Kj:
If i > ij (more than one pointer to bucket J)
allocate a new bucket z, and set 0 = iz-
Update the second half of the bucket address table entries originally
pointing to j, to point to z
remove each record in bucket j and reinsert (in jor z)
recompute new bucket for Kj and insert record in the bucket (further
splitting is required if the bucket is still full)
If 1 = ij (only one pointer to bucket J)
If i reaches some limit b, or too many splits have happened in this
insertion, create an overflow bucket
Else
• increment i and double the size of the bucket address table.
replace each entry in the table by two entries that point to the same
bucket.
recompute new bucket address table entry for Kj
Now i > ij so use the first case above.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=15)

### 原始文字层

````text
Deletion in Extendable Hash Structure
▪ To delete a key value, 
• locate it in its bucket and remove it. 
• The bucket itself can be removed if it becomes empty (with appropriate 
updates to the bucket address table). 
• Coalescing of buckets can be done (can coalesce only with a “buddy”
bucket having same value of ij and same ij –1 prefix, if it is present) 
• Decreasing bucket address table size is also possible
▪ Note: decreasing bucket address table size is an expensive 
operation and should be done only if number of buckets becomes 
much smaller than the size of the table
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Delet ion in Ext endable Hash Str ucture
▪     To delete a k ey  value,
        •    locate it   in   its   buck et   and r emove it  .
        •    The  buck et  its elf  can be  remov ed if  it  becomes  empt y ( with appr opr iat e
             updates t o  the  bucket  address t able).
        •    Co  a  l es   ci n  g    of    b  uc   ke  ts    ca  n    be   d  o  ne   (   ca  n   co  a  l es   ce   o  nl y    wi t   h    a “buddy”
             bucket having  same  value of                     ij and same ij –1 prefix, if  it  is present)
        •    De  cr   e  as   i ng   b  u  cke  t    ad  d  re  ss    ta  bl e   s   i ze   i s    al s   o    po  ss   i bl e
               ▪   No  te  :    de  cr  e  as   i ng   b  u  cke  t    ad  d  re  ss    ta  bl e   s   i ze   i s    an   e  xp  e  ns   i ve
                   operat ion and  should be  done  only  if number  of  buckets  becomes
                   much smaller  t  han the siz e   of   the table
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Deletion in Extendable Hash Structure
TO delete a key value,
locate it in its bucket and remove it.
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
The bucket itself can be removed if it becomes empty (with appropriate
updates to the bucket address table).
Coalescing of buckets can be done (can coalesce only with a "buddy/'
bucket having same value of ij and same ij—l prefix, if it is present)
Decreasing bucket address table size is also possible
Note: decreasing bucket address table size is an expensive
operation and should be done only if number of buckets becomes
much smaller than the size of the table
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=16)

### 原始文字层

````text
Use of Extendable Hash Structure: Example
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Use of Extendable Hash Structure:
Example
dept_name
Biology
Comp. Sci.
Elec. Eng.
Finance
History
Music
Physics
h(dept_name)
0011 0101 1010 0110 1100 1001 1110 1011
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=17)

### 原始文字层

````text
Example (Cont.)
▪ Initial hash structure; bucket size = 2
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Example (Cont.)
• Initial hash structure; bucket size = 2
hash prefix
bucket address table
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
bucket 1
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 18 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=18)

### 原始文字层

````text
Example (Cont.)
▪ Hash structure after insertion of “Mozart”
, 
“Srinivasan”, and “Wu” records
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Ex a mp le  ( Cont .)
▪     Ha  sh   s   tr   uc   tu  re   a  fte  r    i n  se  rti o  n   o  f “Mo za rt”, “Sr  iniv  as  an”,    an d  “Wu” records
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Example (Cont.)
Hash structure after insertion of "Mozart", "Srinivasan'
and "Wu" records
hash prefix
bucket address table
15151
Mozart
10101
12121 wu
Music
40000
Srinivasan Comp. Sci. 90000
Finance
90000
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 19 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=19)

### 原始文字层

````text
Example (Cont.)
▪ Hash structure after insertion of Einstein record
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Example (Cont.)
• Hash structure after insertion of Einstein record
hash prefix
bucket address table
15151 Mozart
12121 WU
22222 Einstein
Music
Finance
Ph sics
40000
90000
95000
10101 Srinivasan Com
. Sci. 65000
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 20 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=20)

### 原始文字层

````text
Example (Cont.)
▪ Hash structure after insertion of Gold and El Said records
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Example (Cont.)
Hash structure after insertion of Gold and El Said records
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
hash prefix
3
bucket address table
15151
22222
33456
12121
10101
32343
Mozart
Einstein
Gold
wu
Music
Physics
Physics
Finance
Srinivasan Com . Sci.
El Said History
40000
95000
87000
90000
65000
60000
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 21 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=21)

### 原始文字层

````text
Example (Cont.)
▪ Hash structure after insertion of Katz record
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Example (Cont.)
Hash structure after insertion of Katz record
hash prefix
3
bucket address table
15151
22222
33456
12121
32343
10101
45565
Mozart
Einstein
Gold
wu
El Said
Music
Physics
Physics
Finance
History
Srinivasan Comp. Sci.
Katz
Comp. Sci.
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
40000
95000
87000
90000
60000
65000
75000
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 22 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=22)

### 原始文字层

````text
Example (Cont.)
And after insertion of 
eleven records
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Example (Cont.)
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
And after insertion of
eleven recordS
hash prefix
3
bucket address table
15151
76766
22222
33456
12121
76543
32343
58583
10101
45565
Mozart
Crick
Einstein
Gold
wu
Singh
El Said
Califieri
Music
Biology
Physics
Physics
Finance
Finance
History
History
Srinivasan Comp.
Sci.
Sci.
40000
72000
95000
87000
90000
80000
60000
62000
65000
75000
83821
Brandt
Com
. Sci.
92000
Katz
Comp.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 23 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=23)

### 原始文字层

````text
Example (Cont.)
And after insertion of 
Kim record in previous 
hash structure
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Example
hash prefix
3
bucket address table
15151
76766
98345
22222
33456
12121
76543
32343
58583
10101
45565
Mozart
Crick
Kim
Einstein
Gold
wu
Singh
El Said
Califieri
Music
Biolog
Elec. En
Physics
Physics
Finance
Finance
History
History
40000
72000
80000
95000
87000
90000
80000
60000
62000
65000
75000
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
And after insertion of
Kim record in previous
hash structure
Srinivasan Comp.
Sci.
Sci.
83821
Brandt
Com
. Sci.
92000
Katz
Comp.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 24 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=24)

### 原始文字层

````text
Extendable Hashing vs. Other Schemes
▪ Benefits of extendable hashing: 
• Hash performance does not degrade with growth of file
• Minimal space overhead
▪ Disadvantages of extendable hashing
• Extra level of indirection to find desired record
• Bucket address table may itself become very big (larger than memory)
▪ Cannot allocate very large contiguous areas on disk either
▪ Solution: B+-tree structure to locate desired record in bucket 
address table
• Changing size of bucket address table is an expensive operation
▪ Linear hashing is an alternative mechanism 
• Allows incremental growth of its directory (equivalent to bucket 
address table)
• At the cost of more bucket overflows
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Extendabl e Hashi ng  vs.  Ot her Schem  es
▪      Be n ef  its   of   e xte n da b le   ha sh in g:
         •     Ha  sh   p  e  rf   or   m an  ce   d  o  es    n  ot    d  eg  ra  d  e    wi th   g  r   ow   th   o  f f   i l e
         •     Min ima l s pa ce  o ve r he a d
▪      Di s   ad  va  n  ta  ge  s    of    e  xte  n  da  b  l e    ha  sh  i n  g
         •     Ex  tra  le ve l o f   ind ir  ec  tio n   to  fin d  d es  ire d   re co rd
         •     Bu ck  et   a dd re ss   ta b le   may   its  elf   b ec  ome  ve r  y b ig  (la r  ge r   th an  me mor  y)
                  ▪   Ca  n  no  t    al l o  ca  te   v   er   y    l ar   ge   c   on  ti g  u  ou  s    ar   e  as    o  n    di s   k e  i th  e  r
                  ▪   So lu tio n:   B+-tr  e e    str  uc  tu re  t   o    loc  at   e    de sir  ed  r  e co rd  in  b uc  ke t
                      address t able
         •     Ch  a  ng  i n  g    si ze   o  f    bu  ck   et    a  dd  r   es   s t   ab  l e   i s    an   e  xp  e  ns   i ve   o  pe  ra  ti o  n
▪      Linear   hashing                 is   an alter nativ e   mechanis m
         •     Allo ws   in cre me nt  al   gr  ow  th  o f it  s d ir  ec  to ry   (e q uiv  ale n t t  o   bu ck  et
               address t able)
         •     At   th e  co st   o f mo re  b u cke t   ov  er  flo ws
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Extendable Hashing vs. Other Schemes
Benefits of extendable hashing:
Hash performance does not degrade with growth of file
Minimal space overhead
Disadvantages of extendable hashing
Extra level of indirection to find desired record
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Bucket address table may itself become very big (larger than memory)
Cannot allocate very large contiguous areas on disk either
Solution: B+-tree structure to locate desired record in bucket
address table
Changing size of bucket address table is an expensive operation
Linear hashing is an alternative mechanism
Allows incremental growth of its directory (equivalent to bucket
address table)
At the cost of more bucket overflows
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 25 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=25)

### 原始文字层

````text
Comparison of Ordered Indexing and Hashing
▪ Cost of periodic re-organization
▪ Relative frequency of insertions and deletions
▪ Is it desirable to optimize average access time at the expense of worst￾case access time?
▪ Expected type of queries:
• Hashing is generally better at retrieving records having a specified 
value of the key.
• If range queries are common, ordered indices are to be preferred
▪ In practice:
• PostgreSQL supports hash indices, but discourages use due to poor 
performance
• Oracle supports static hash organization, but not hash indices
• SQLServer supports only B+-trees
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Comp a ri  son of  Or de r e d   Inde xi  ng   a nd   Has hing
           ▪      Co  st    o  f p  e  ri o  d  i c r   e-organizat ion
           ▪      Re  l a  ti ve   f   re  q  ue  n  cy    of    i n  se  rti o  n  s a  n  d    de  l e  ti o  ns
           ▪      Is   it    de sir  a ble  t   o    op timize  a ve r  ag e  a cce ss   time  a t t   he  e xp e ns  e    of    wo r  st-
                  ca  se   a  cc   es   s t   i m e?
           ▪      Ex  pe ct  ed  t  yp e   of   q ue rie s:
                    •     Ha  sh  i n  g    i s g  e  ne  r   al l y    b  et   te  r a  t    re  tr   i ev   i ng   r   e  co  rd  s h  a  vi n  g    a    sp  ec   i fi e  d
                          va  l u  e    of    th  e   ke  y.
                    •     If    r  an g e    qu e rie s a r  e    co mmo n , o rd e re d  in dic  es   a re  to  b e  p re fe rr  e d
           ▪      In  p r  ac  tice :
                    •     Po st  gr  eS   QL  s  up p or  ts   ha sh  in d ice s,   bu t   dis  co ur  a ge s   us  e   du e  to  p o or
                          performance
                    •     Oracle s upports  static  has h  organization, but not hash indic es
                    •     SQ L Ser  ve r su  p  po  r  ts    on  l y    B+-tr  e es
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Comparison of Ordered Indexing and Hashing
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
•
•
Cost of periodic re-organization
Relative frequency of insertions and deletions
Is it desirable to optimize average access time at the expense of worst-
case access time?
Expected type of queries:
Hashing is generally better at retrieving records having a specified
value of the key.
If range queries are common, ordered indices are to be preferred
In practice:
PostgreSQL supports hash indices, but discourages use due to poor
performance
Oracle supports static hash organization, but not hash indices
SQLServer supports only B+-trees
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 26 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=26)

### 原始文字层

````text
Multiple-Key Access
▪ Use multiple indices for certain types of queries.
▪ Example: 
select ID
from instructor
where dept_name = 
“Finance” and salary = 80000
▪ Possible strategies for processing query using indices on single attributes:
1. Use index on dept_name to find instructors with department name 
Finance; test salary = 80000 
2. Use index on salary to find instructors with a salary of $80000; test
dept_name = “Finance”.
3. Use dept_name index to find pointers to all records pertaining to the 
“Finance” department. Similarly use index on salary. Take 
intersection of both sets of pointers obtained.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Mult iple-Key Access
▪     Us   e    m ul t   i pl e   i n  d  i ce  s f   or   ce  r  ta  i n    typ  e  s o  f    qu  e  ri e  s.
▪     Ex  amp le:
        sel ect ID
        from instr uctor
        where dept_name = “Finance                           ” and        sa  l a  ry =    80 0 00
▪     Po ss  ible  s  tra te g ies   fo r  p ro ce ssin g  q ue r y u sin g  in dic  es   o n   sin gle  a tt  rib ut  es  :
        1.   Us   e    i nd  e  x o  n   dept_name to  f   ind  in st   ru ct   or  s w  ith  d ep a rt   me n t n a me
             Finance;  test          sa  l a  ry    = 8  0  00  0
        2.   Us   e    i nd  e  x on sa  l a  ry    to  f   ind  in st   ru ct   or  s w  ith  a  sa la ry   o f $ 8 00 0 0;    te st
             dept_name = “Finance”.
        3.   Us   e dept_name index   to find pointer s t  o   all   records   pert  aining   to the
             “Finance” depart ment.   Similarly use index  on                                   sa  l a  ry.     T a ke
             inters ec tion   of   bot  h   sets   of   pointers  obt  ained.
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Multiple-Key Access
Use multiple indices for certain types of queries.
Example:
select ID
from instructor
where dept_name = "Finance" and salary = 80000
Possible strategies for processing query using indices on single attributes:
1. Use index on dept_name to find instructors with department name
Finance; test salary = 80000
2. Use index on salatyto find instructors with a salary of $80000; test
dept_name = "Finance' .
3. Use dept_name index to find pointers to all records pertaining to the
"Finance" department. Similarly use index on salary. Take
intersection of both sets of pointers obtained.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 27 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=27)

### 原始文字层

````text
Indices on Multiple Keys
▪ Composite search keys are search keys containing more than one 
attribute
• E.g., (dept_name, salary)
▪ Lexicographic ordering: (a1, a2) < (b1, b2) if either 
• a1 < b1, or 
• a1=b1 and a2 < b2
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
In d ic  e  s   o n  M u l  tip l  e   K e  ys
▪    Composite  search keys               are search  keys  cont aining  more  than one
     attribut e
      •    E.  g.  , (dept_name,  salary)
▪    Lexicographic  ordering:  (a1,    a2) < (b1,    b2) if either
      •    a1 <    b1,    or
      •    a1=b1 and   a2 <    b2
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Indices on Multiple Keys
•
Composite search keys are search keys containing more than one
attribute
E.g., (dept_name, salary)
Lexicographic ordering: (al, a) < (bl, b2) if either
al < bl, or
al=bl and a2 < b2
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 28 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=28)

### 原始文字层

````text
Indices on Multiple Attributes
▪ With the where clause
 where dept_name = “Finance” and salary = 80000
the index on (dept_name, salary) can be used to fetch only records that 
satisfy both conditions.
• Using separate indices in less efficient — we may fetch many 
records (or pointers) that satisfy only one of the conditions.
▪ Can also efficiently handle 
 where dept_name = 
“Finance” and salary < 80000
▪ But cannot efficiently handle
 where dept_name < 
“Finance” and balance = 80000
• May fetch many records that satisfy the first but not the second 
condition
Suppose we have an index on combined search-key
(dept_name, salary).
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
In d ic  e  s   o n  M u l  tip l  e   A tt  ri  bu t  e  s
 Su p po se  w  e   ha ve  a n  in de x   on  c  omb ine d  se a rc  h-ke  y
                                         (dept_name,  salary).
    ▪      Wi  t    h     t h   e where cl a  u  se
                              where dept_name = “Finance” and sa  l a  ry    = 80000
          th e  in de x    on  (dept_name,  salary) can be used to fetch only records that
          sa  ti s   fy    bo  th   c   on  d  i ti o  ns   .
            •     Us   i ng   s   ep  a  ra  te   i n  d  i ce  s i n   l e  ss    e  ffi c   i en  t — we   m a  y    fe  tch   m a  ny
                  records (or pointers) that satisfy only one of the conditions.
    ▪     Ca  n   a  l so   e  ffi c   i en  tl y    h  an  d  l e
                              where dept_name = “Finance” and sa  l a  ry    <    80 0 00
    ▪     Bu t   ca nn o t e ff  icie nt  ly h a nd le
                             where dept_name < “Finance” and balance = 80000
            •     Ma y f  et  ch  man y   re co rd s   th at   sa tis fy   th e   fir st   bu t   no t   th e   se co nd
                  co  n  di t   i on
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Indices on Multiple Attributes
Suppose we have an index on combined search-key
(dept_name, salary).
With the where clause
where dept_name = "Finance" and salary = 80000
the index on (dept_name, salary) can be used to fetch only records that
satisfy both conditions.
Using separate indices in less efficient — we may fetch many
records (or pointers) that satisfy only one of the conditions.
Can also efficiently handle
where dept_name = "Finance" and salary< 80000
But cannot efficiently handle
where dept_name < "Finance" and balance = 80000
May fetch many records that satisfy the first but not the second
condition
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 29 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=29)

### 原始文字层

````text
Other Features
▪ Covering indices
• Add extra attributes to index so (some) queries can avoid fetching the 
actual records
• Store extra attributes only at leaf
▪ Why?
▪ Particularly useful for secondary indices 
• Why?
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Ot her  Features
▪     Coveri ng  indices
        •    Ad d  e xtr  a   at  tr  ibu te s   to  in de x   so  (s  ome )   qu e rie s   ca n   av  oid  f  et  ch ing  t  he
             actual records
        •    St  or  e   ex  tr  a   at  trib u te s o n ly a t   lea f
               ▪    Wh  y?
▪     Pa rt  icu lar  ly   us  ef  ul   fo r s  ec  on d ar  y   ind ice s
        •    Wh   y?
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Other Features
•
Covering indices
Add extra attributes to index so (some) queries can avoid fetching the
actual records
Store extra attributes only at leaf
Why?
Particularly useful for secondary indices
Why?
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 30 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=30)

### 原始文字层

````text
Creation of Indices
▪ Example
 create index takes_pk on takes (ID,course_ID, year, semester, section)
 drop index takes_pk
▪ Most database systems allow specification of type of index, and 
clustering.
▪ Indices on primary key created automatically by all databases
• Why?
▪ Some database also create indices on foreign key attributes
• Why might such an index be useful for this query:
▪ takes ⨝ σname='Shankar' (student)
▪ Indices can greatly speed up lookups, but impose cost on updates
• Index tuning assistants/wizards supported on several databases to 
help choose indices, based on query and update workload
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Cr eat ion of  Indices
▪     Ex  amp le
        create i ndex              ta ke s_ p k on ta ke s (ID  ,co u rs  e_ ID,    ye ar  ,    se me st   er  ,    se ctio n)
        drop  index              ta ke s_ p k
▪     Mo st   da ta b as e   sys te ms  a llow  sp e cific at  ion  o f   typ e  o f in d ex , a n d
      cl u  st   er  i n  g.
▪     In d ice s o n  p rima ry   ke y    cre a te d    au to ma tica lly    by   a ll d at   ab a se s
         •    Wh   y?
▪     So me   da ta b as  e   als  o   cr  ea te  in d ice s o n  fo re ig n   ke y a tt  rib u te s
         •    Wh   y     m i  gh   t      su   ch     a   n     i  nd   e   x  b   e     u   se   f u   l    f o   r     t h   i  s  q   u   er   y:
                 ▪   ta ke s ⨝ σna  me  ='Sh ank ar'          (st   ud  e  nt)
▪     In d ice s c  an  g r  ea tly   sp e ed  u p  lo ok  up s,    b ut    impo se  c  os  t o n  u pd a te s
         •    In d ex   tu n ing  a ss  ista n ts/   wiza r  ds   su p po rt   ed  o n  se ve r  al    da ta b as  es   to
              help choose indices, based  on query  and update workload
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Creation of Indices
Example
•
•
create index takes_pkon takes (ID,course_lD, year, semester, section)
drop index takes_pk
Most database systems allow specification of type of index, and
clustering.
Indices on primary key created automatically by all databases
Some database also create indices on foreign key attributes
Why might such an index be useful for this query:
takes o
name—Shankar' (Student)
Indices can greatly speed up lookups, but impose cost on updates
Index tuning assistants/wizards supported on several databases to
help choose indices, based on query and update workload
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 31 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=31)

### 原始文字层

````text
Index Definition in SQL
▪ Create an index
create index <index-name> on <relation-name>
(<attribute-list>)
E.g.,: create index b-index on branch(branch_name)
▪ Use create unique index to indirectly specify and enforce the condition 
that the search key is a candidate key is a candidate key.
• Not really required if SQL unique integrity constraint is supported
▪ To drop an index 
drop index <index-name>
▪ Most database systems allow specification of type of index, and 
clustering.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
In d e  x   D e  fi  n iti  o n   in  S Q L
▪     Cr   e  at   e    an   i n  d  ex
                        create i ndex           <i n d ex-name> on <r  el a ti o n-name>
                                                                                   (<attribute-list  >)
        E.  g.  ,:    create i ndex          b-index on branch(branch_name)
▪     Us   e create unique index                    to  in d ire ct   ly s  pe cif   y a n d    en fo rc  e    th e    co nd itio n
      th a t t   he  s  ea r  ch  ke y    is a  c  an d ida te  k  ey   is    a    ca nd id at   e    ke y.
        •    No  t    re  a  l l y r   eq  u  i re  d   i f    SQL   unique integr ity  constr aint   is s uppor ted
▪     To drop  an index
                                      drop  index <i n d ex-name>
▪     Mo st   da ta b as e   sys te ms  a llow  sp e cific at  ion  o f   typ e  o f in d ex , a n d
      cl u  st   er  i n  g.
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Index Definition in SQL
Create an index
create index <index-name> on <relation-name>
(<attribute-list>)
E.g.,: create index b-index on branch(branch_name)
Use create unique index to indirectly specify and enforce the condition
that the search key is a candidate key is a candidate key.
Not really required if SQL unique integrity constraint is supported
To drop an index
drop index <index-name>
Most database systems allow specification of type of index, and
clustering.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 32 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=32)

### 原始文字层

````text
Write Optimized Indices
▪ Performance of B+-trees can be poor for write-intensive workloads
• One I/O per leaf, assuming all internal nodes are in memory
• With magnetic disks, < 100 inserts per second per disk
• With flash memory, one page overwrite per insert
▪ Two approaches to reducing cost of writes
• Log-structured merge tree
• Buffer tree
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Wr it e  Optim   iz ed  Indic e s
▪      Pe rf  or  man ce  o f    B+-tr  e es   ca n  b e    po o r f   or   w  rite-intens ive wor kloads
         •     One I /O per leaf,  as suming all internal nodes are in memory
         •     Wi  t    h     m ag   n   et    i  c  d   i  sk    s,      <  1   00     i  n   se   r   t s     pe   r     se   co   nd     p   e   r     di  s    k
         •     Wi  t    h     f l  a   sh     m e   mo   r   y,      on   e     p   ag   e     o   ve   rwr   i  t e     p   e   r  i  n   se   r   t
▪      Two appr oaches t o  reduc ing c os t of  writ es
         •     Log-structured  merge tree
         •     Buffer tree
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Write Optimized Indices
Performance of B+-trees can be poor for write-intensive workloads
One 1/0 per leaf, assuming all internal nodes are in memory
With magnetic disks, < 100 inserts per second per disk
With flash memory, one page overwrite per insert
•
Two approaches to reducing cost of writes
Log-structured merge tree
Buffer tree
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 33 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=33)

### 原始文字层

````text
Bloom Filters
▪ A bloom filter is a probabilistic data structure used to check membership 
of a value in a set
• May return true (with low probability) even if an element is not present
• But never returns false if an element is present
• Used to filter out irrelevant sets
▪ Key data structure is a single bitmap
• For a set with n elements, typical bitmap size is 10n
▪ Uses multiple independent hash functions
▪ With a single hash function h() with range=number of bits in bitmap:
• For each element s in set S compute h(s) and set bit h(s)
• To query an element v compute h(v), and check if bit h(v) is set
▪ Problem with single hash function: significant chance of false positive due 
to hash collision
• 10% chance with 10n bits
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Bloom   Fi lt er s
▪     A bloom f il ter is   a   pr obabilistic  dat  a   str uc ture used to c heck  membership
      of a value in a set
         •    Ma y r et  ur n  tr ue  ( wit  h   low  p ro ba b ility)  e ve n  if   an  e le me n t is  n ot   p re se n t
         •    Bu t   ne ve r   re tu rn s   fa lse  if   an  e le men t   is p re se n t
         •    Us   ed   t   o    fi l te  r    o  ut    i rr   e  l ev   an  t    se  ts
▪     Ke y   da ta  s  tru ct  ur  e  is   a   sin gle  b itma p
         •    For   a  set w ith           n   elements,  typical  bit map size  is 10n
▪     Us   es    m u  l ti p  l e    i nd  e  pe  n  de  n  t h  a  sh   fu  n  cti o  n  s
▪     Wi  t    h     a     si  n  gl  e    h  a  sh    f u  n  ct i  o  n    h  ()     wi  t    h     ra  n  ge  =n  um b  e  r  o  f      bi  t    s  i  n    b  i  t m a  p  :
         •    For each element                   s in set S co  m p  ut   e h(s) and set bit h(s)
         •    To query  an  element  v                      co  m p  ut   e h(v), and check if bit h(v) is set
▪     Pr  ob le m wit  h   sin gle  h a sh  fu n ctio n :    sig nif  ica nt   ch a nc  e   of   fa lse  p o sitiv  e   du e
      to  h a sh  co llisio n
         •    10% chance  with 10n  bit s
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Bloom Filters
A bloom filter is a probabilistic data structure used to check membership
of a value in a set
May return true (with low probability) even if an element is not present
But never returns false if an element is present
Used to filter out irrelevant sets
Key data structure is a single bitmap
For a set with n elements, typical bitmap size is 10n
Uses multiple independent hash functions
With a single hash function h() with range=number of bits in bitmap:
For each element s in set S compute h(s) and set bit h(s)
To query an element v compute h(v), and check if bit h(v) is set
Problem with single hash function: significant chance of false positive due
to hash collision
10% chance with 1 On bits
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 34 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=34)

### 原始文字层

````text
Bloom Filters (Cont.)
▪ Key idea of Bloom filter: reduce false positives by use multiple hash 
functions hi
() for i = 1..k
• For each element s in set S for each i compute hi
(s) and set bit hi
(s)
• To query an element v for each i compute hi
(v), and check if bit hi
(v) is 
set
▪ If bit hi
(v) is set for every i then report v as present in set
▪ Else report v as absent
• With 10n bits, and k = 7, false positive rate reduces to 1% instead of 
10% with k = 1
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Bloom   Fi lt er s  ( Cont .)
▪     Ke y   ide a  o f Blo o m filt  er  :    re d uc  e   fa lse  p os  itive s   by   u se  mult  iple  h a sh
      fu n ctio n s hi()  for i =    1.   .k
        •     For each element s in set S   fo r e a ch  i co  m p  ut   e hi(s) and set bit hi(s)
        •     To query  an  element  v                   fo r   e ac  h i co  m p  ut   e hi(v), and check if bit hi(v) is
              se  t
                ▪   If    b it hi(v) is set for every i th e n    re p or  t v               as present  in  set
                ▪   Els  e   re po r  t v as absent
        •     Wi  t    h     10   n     b   i  t s,      a   nd    k =    7,    fa l se  p o si ti v  e    ra te  r  ed u ce s t   o    1%    i ns  te ad  o f
              10%  wit h k =    1
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Bloom Filters (Cont.)
Key idea of Bloom filter: reduce false positives by use multiple hash
functions hi() for k
For each element s in set S for each i compute hi(s) and set bit hi(s)
To query an element v for each i compute hi(v), and check if bit hi(v) is
set
• If bit hi(v) is set for every i then report v as present in set
Else report vas absent
With 10n bits, and k= 7, false positive rate reduces to 1% instead of
10% with k = 1
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 35 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=35)

### 原始文字层

````text
Log Structured Merge (LSM) Tree
▪ Consider only inserts/queries for 
now
▪ Records inserted first into in￾memory tree (L0 tree)
▪ When in-memory tree is full, 
records moved to disk (L1 tree)
• B+-tree constructed using 
bottom-up build by merging 
existing L1 tree with records 
from L0 tree
▪ When L1 tree exceeds some 
threshold, merge into L2 tree
• And so on for more levels
• Size threshold for Li+1 tree 
is k times size threshold for 
Li tree
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Log Structured Merge (LSM) Tree
▪     Co  n  si d  er    o  n  l y i n  se  rt   s/q  u  er   i e  s f   or
      now
▪     Re  co  r   ds    i n  se  rte  d   fi r   st    i n  to   i n-
      me mo r y t  re e   (L0 tr  e e)
▪     Wh  e  n     i n-me mo r y t  re e   is f  ull,
      records moved to disk (L1 tr  e e)
        •     B+-tr  e e    co ns  tru ct   ed  u sin g
              bot tom-up  build by merging
              exist ing L1 tr  e e    with  r  ec  or  d s
              fr  o m    L0 tr  e e
▪     Wh   e   n     L1 tr  e e    ex  ce ed s    so me
      th r  es  ho ld , me rg e  in to  L2 tr  e e
        •     An d  so  o n  fo r   mor  e   lev  els
        •     Siz  e   th re sh old  f  or   Li+1 tr  e e
              is k time s    size  t   hr  es  ho ld  fo r
              Li tr  e e
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Log Structured Merge (LSM) Tree
Consider only inserts/queries for
now
Records inserted first into in-
memory tree (Lo tree)
When in-memory tree is full,
records moved to disk (Ll tree)
B+-tree constructed using
bottom-up build by merging
existing Ll tree with records
from 1-0 tree
When Ll tree exceeds some
threshold, merge into 1-2 tree
And so on for more levels
Size threshold for Li+l tree
is k times size threshold for
Li tree
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Memory
Disk
102
````

### 图表辅助说明

LSM 层级图：L0 位于 Memory，其下 L1、L2、L3 位于 Disk，三角形逐层变大。内存层满后与磁盘层合并，超过层阈值后继续向下一层合并；图旁说明层容量阈值按 k 倍增长。

## PDF 第 36 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=36)

### 原始文字层

````text
LSM Trees (Cont.)
▪ Deletion handled by adding special “delete” entries
• Lookups will find both original entry and the delete entry, and must 
return only those entries that do not have matching delete entry
• When trees are merged, if we find a delete entry matching an original 
entry, both are dropped.
▪ Update handled using insert+delete
▪ LSM trees were introduced for disk-based indices
• But useful to minimize erases with flash-based indices
• The stepped-merge variant of LSM trees is used in many BigData
storage systems
▪ Google BigTable, Apache Cassandra, MongoDB
▪ And more recently in SQLite4, LevelDB, and MyRocks storage 
engine of MySQL
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
LSM Trees (Cont.)
▪     De  l e  ti o  n    ha  n  dl e  d   b  y a  d  di n  g   sp  e  ci a  l  “   de  l e  te  ” e  n  tr   i es
        •     Lookups will find bot h  original entry and t he delet e  entry,  and must
              return only those entries that do not have matching delete entry
        •     Wh   e   n     t r   ee   s     ar   e     m er   ge   d   ,   i  f      we     f    i  nd     a     d   e   l  et    e     en   t r   y     ma   t c    hi  n   g     a   n     or   i  g   i  na   l
              ent ry, both are dropped.
▪     Up  d  at   e    ha  n  dl e  d   u  si n  g insert  +delete
▪     LSM trees were introduced for  disk-based indices
        •     Bu t   us  ef  ul   to  minimiz  e   er  as  es   wit  h   fla sh-based indices
        •     The  stepped-merge   variant of   LSM   trees is  used   in   many Big Da ta
              st   or  a  ge   s   yst   em s
                ▪   Google BigTable,    Ap ac  he  C  as  sa nd ra ,    Mon g oD  B
                ▪   An d  mor  e  re ce n tly   in   SQ Lit  e4 , LevelDB,    an d  MyR oc ks st   or  a  ge
                    engine  of  MySQL
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
LSM Trees (Cont.)
Deletion handled by adding special "delete" entries
Lookups will find both original entry and the delete entry, and must
return only those entries that do not have matching delete entry
When trees are merged, if we find a delete entry matching an original
entry, both are dropped.
Update handled using insert+delete
LSM trees were introduced for disk-based indices
But useful to minimize erases with flash-based indices
The stepped-merge variant of LSM trees is used in many BigData
storage systems
Google BigTable, Apache Cassandra, MongoDB
And more recently in SQLite4, LevelDB, and MyRocks storage
engine of MySQL
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 37 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=37)

### 原始文字层

````text
LSM Tree (Cont.)
▪ Benefits of LSM approach
• Inserts are done using only sequential I/O operations
• Leaves are full, avoiding space wastage
• Reduced number of I/O operations per record inserted as compared to 
normal B+-tree (up to some size)
▪ If each leaf has m entries, m/k entries merged in using 1 IO
▪ Total I/O operations: k/m logk(I/M) where I = total number of 
entries, and M is the size of L0 tree.
▪ Drawback of LSM approach
• Queries have to search multiple trees
• Entire content of each level copied multiple times
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
LSM Tree (Cont.)
▪     Be n ef  its   of   L SM a pp ro a ch
        •     In se r  ts    ar  e    do n e    us  ing  o n ly s  eq u en tia l I   /O  o pe r  at   ion s
        •     Leaves are full, avoiding space wastage
        •     Re  d  uc   ed   n  u  m be  r    of    I/   O    op  e  ra  ti o  n  s p  e  r r   e  co  rd   i n  se  rt   ed   a  s    co  mp  a  re  d   to
              normal  B+-tr  e e    (u p    to  so me  siz  e)
                ▪   If    e ac  h    lea f    ha s m ent ries,  m/k  ent ries  merged in using  1  IO
                ▪   Total I/ O  operations:     k/   m logk(I/   M) wh  e  re   I =    to ta l  n umb er   o f
                    ent ries,  and M is   the   size of   L0 tr  e e.
▪     Dr   a  wb  ac   k o  f    LSM     ap  p  ro  ac   h
        •     Queries  hav e  to search multiple trees
        •     En tir  e   co nt  en t   of   e ac  h   lev  el   co pie d  mu ltip le   times
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
LSM Tree (Cont.)
Benefits of LSM approach
Inserts are done using only sequential 1/0 operations
Leaves are full, avoiding space wastage
Reduced number of 1/0 operations per record inserted as compared to
normal B+-tree (up to some size)
• If each leaf has m entries, m/kentries merged in using 1 10
Total 1/0 operations: Wm logk(l/M) where total number of
entries, and Mis the size of Lo tree.
Drawback of LSM approach
Queries have to search multiple trees
Entire content of each level copied multiple times
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 38 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=38)

### 原始文字层

````text
▪ Rolling merge
▪ LSM/Stepped Merge often implemented on a partitioned relation
• Each partition size set to some max, split if over-sized 
• Spread partitions over multiple machines
Optimizations of LSM
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Op ti  miz a ti  on s  o f   L SM
▪    Rol ling merge
▪    LSM/St epped Merge often implement ed on a partitioned relat ion
       •   Ea ch  p a rtit  ion  s  ize  se t   to  so me  max  , s  plit   if   ov  er-si z   ed
       •   Sp re a d   pa r  titio n s o ve r mu ltip le   ma ch in es
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Optimizations of LSM
•
Rolling merge
LSM/Stepped Merge often implemented on a partitioned relation
Each partition size set to some max, split if over-sized
Spread partitions over multiple machines
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 39 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=39)

### 原始文字层

````text
Stepped Merge Index
▪ Stepped-merge index: variant of 
LSM tree with k trees at each 
level on disk
• When all k indices exist at a 
level, merge them into one 
index of next level. 
• Reduces write cost 
compared to LSM tree
▪ But queries are even more 
expensive since many trees need 
to be queries
▪ Optimization for point lookups
• Compute Bloom filter for 
each tree and store in￾memory
• Query a tree only if Bloom 
filter returns a positive result
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Stepped Merge I ndex
▪     St  ep p ed-me rg e   ind e x:   va ria n t o f
      LSM tree  with k tr  e es   a t e a ch
      level on   dis k
        •    Wh   e   n     al  l   k indic es  exist   at a
             level, merge them into one
             index   of   nex t level.
        •    Re  d  uc   es    wr  i te   c   os   t
             co  m p  ar  ed   t   o    LS   M    tr  ee
▪     Bu t   qu e rie s a r  e   ev  en  mo re
      expensive  since many trees  need
      to  b e  q ue r  ies
▪     Opt imization  for point  look ups
        •    Co  m p  ut   e    Bl oo  m  f   i l te  r f   or
             each  tree and  store in             -
             me mo r y
        •    Query a t ree  only  if B loom
             filt   er   r  et   ur  n s a  p o sitiv  e    re su lt
````

### 图片文字 OCR（en-US，待对照原页）

````text
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Stepped Merge Index
Stepped-merge index: variant of
LSM tree with k trees at each
level on disk
When all k indices exist at a
level, merge thern into one
Llo
index of next level.
Reduces write cost
Lil
compared to LSM tree
But queries are even more
expensive since many trees need
to be queries
Optimization for point lookups
Compute Bloom filter for
each tree and store in-
memory
Query a tree only if Bloom
filter returns a positive result
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
Memory
Disk
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 40 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=40)

### 原始文字层

````text
LSM Trees (Cont.)
▪ Deletion handled by adding special “delete” entries
• Lookups will find both original entry and the delete entry, and must 
return only those entries that do not have matching delete entry
• When trees are merged, if we find a delete entry matching an original 
entry, both are dropped.
▪ Update handled using insert + delete
▪ LSM trees were introduced for disk-based indices
• But useful to minimize erases with flash-based indices
• The stepped-merge variant of LSM trees is used in many BigData
storage systems
▪ Google BigTable, Apache Cassandra, MongoDB
▪ And more recently in SQLite4, LevelDB, and MyRocks storage 
engine of MySQL
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
LSM Trees (Cont.)
▪     De  l e  ti o  n    ha  n  dl e  d   b  y a  d  di n  g   sp  e  ci a  l  “   de  l e  te  ” e  n  tr   i es
        •     Lookups will find bot h  original entry and t he delet e  entry,  and must
              return only those entries that do not have matching delete entry
        •     Wh   e   n     t r   ee   s     ar   e     m er   ge   d   ,   i  f      we     f    i  nd     a     d   e   l  et    e     en   t r   y     ma   t c    hi  n   g     a   n     or   i  g   i  na   l
              ent ry, both are dropped.
▪     Up  d  at   e    ha  n  dl e  d   u  si n  g    i ns   er   t    + d  el e  te
▪     LSM trees were introduced for  disk-based indices
        •     Bu t   us  ef  ul   to  minimiz  e   er  as  es   wit  h   fla sh-based indices
        •     The  stepped-me rg e   va ria n t o f   LSM   tre e s is  u se d   in   man y Big Da ta
              st   or  a  ge   s   yst   em s
                ▪    Google BigTable,    Ap ac  he  C  as  sa nd ra ,    Mon g oD  B
                ▪    An d  mor  e  re ce n tly   in   SQ Lit  e4 , LevelDB,    an d  MyR oc ks st   or  a  ge
                     engine  of  MySQL
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
LSM Trees (Cont.)
Deletion handled by adding special "delete" entries
Lookups will find both original entry and the delete entry, and must
return only those entries that do not have matching delete entry
When trees are merged, if we find a delete entry matching an original
entry, both are dropped.
Update handled using insert + delete
LSM trees were introduced for disk-based indices
But useful to minimize erases with flash-based indices
The stepped-merge variant of LSM trees is used in many BigData
storage systems
Google BigTable, Apache Cassandra, MongoDB
And more recently in SQLite4, LevelDB, and MyRocks storage
engine of MySQL
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 41 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=41)

### 原始文字层

````text
Buffer Tree
▪ Alternative to LSM tree
▪ Key idea: each internal node of B+-tree has a buffer to store inserts
• Inserts are moved to lower levels when buffer is full
• With a large buffer, many records are moved to lower level each time
• Per record I/O decreases correspondingly 
▪ Benefits
• Less overhead on queries
• Can be used with any tree index structure
• Used in PostgreSQL Generalized Search Tree (GiST) indices
▪ Drawback: more random I/O than LSM tree
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Buff er  Tr ee
▪       Alt  er  na tiv  e   to  L SM tr  e e
▪       Ke y   ide a : e a ch  in te rn al   no d e   of   B+-tr  e e    ha s    a    bu ff   er   to  s  to re  in se rt   s
           •      In se r  ts    ar  e    mov  ed  t   o    low  er   le ve ls w  he n  b uf   fe r    is f   ull
           •      Wi  t    h     a     l  ar   g   e     bu   f f    er   ,   m a   n   y  r   ec    or   d   s  a   re     m o   ve   d     t o     l  o   we   r     l  ev    el       ea   ch     t    i  m e
           •      Pe r   re co rd  I  /O  d ec  re a se s c  or  re sp o nd in gly
▪       Be n ef  its
           •      Less overhead  on queries
           •      Ca  n   b  e    us   ed   w   i th   a  ny    tr   e  e    i nd  e  x s   tru  ct   ur   e
           •      Us   ed   i n   P    os   tg  re  SQ  L    Ge  n  er   al i z   ed   S    ea  rc   h    T re  e    (GiST) indices
▪       Dr   a  wb  ac   k:    mo  r   e    ra  nd  o  m  I/   O    th  an   L  SM  t   re  e
````

### 图片文字 OCR（en-US，待对照原页）

````text
THE UNIVERSITY OF
AUCKLAND
Wln•ng• o Timüi
NEW ZEALAND
SCIENCE
DEPARTMENT OF
COMPUTER SCIENCE
Buffer Tree
Alternative to LSM tree
Key idea: each internal node of B+-tree has a buffer to store inserts
Inserts are moved to lower levels when buffer is full
With a large buffer, many records are moved to lower level each time
Per record 1/0 decreases correspondingly
Benefits
Less overhead on queries
Can be used with any tree index structure
Used in PostgreSQL Generalized Search Tree (GiST) indices
Drawback: more random 1/0 than LSM tree
Internal node
Pl
Buffer
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 42 页

[查看此页](../../../../source/751/751%2525/10_Index_Hashing.pdf#page=42)

### 原始文字层

````text
FIN
Any questions?
````

### 图片文字 OCR（en-US，待对照原页）

````text
00 THE UNIVERSITYOF
AUCKLAND
Te Whare Wananga o Tamaki Yakaur•u
NEW ZEALAND
FIN
Any questions?
SCIENCE
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

