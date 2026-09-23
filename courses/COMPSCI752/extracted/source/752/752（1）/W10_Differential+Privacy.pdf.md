# W10_Differential+Privacy.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI752/source/752/752（1）/W10_Differential+Privacy.pdf`
- [打开原文件](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf)
- 原文件 SHA-256：`55645c3dec77f0bbb11a38dc700dbd6948fcac94d77a15c401b1a503b772c4b4`
- 文件索引：F221；PDF 总页数：90
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=1)

### 原始文字层

````text
1
Differential Privacy
COMPCSI 752: Big Data Management
University of Auckland
(Credits to Ninh Pham)
Slides are collected and edited from many resources in the reference
Auckland, May 2025
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
D   i   f       fe   r   e   n   t  i   a   l    P   r   i   v a   c   y
                               COMPCSI 752: Big Data Management
                                                Univer  sity of Auc  kland
                                                (Credits to Ninh Pham)
                    Slides are collected and edited from many resources in the reference
                                                      Au  c    k  l  a  n  d  ,   M  ay     2  0  2  5                            1
````

### 图片文字 OCR（en-US，待对照原页）

````text
Differential Privacy
COMPCSI 752: Big Data Management
University of Auckland
(Credits to Ninh Pham)
Slides are collected and edited from many resources in the reference
Auckland, May 2025
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=2)

### 原始文字层

````text
Outline
2
 Motivation
 Why is anonymization hard?
 Differential privacy
 Applications
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Outline
 Motivation
 Why is anonymization hard?
 Differential pr  ivac y
 Applications
                                                                          2
````

### 图片文字 OCR（en-US，待对照原页）

````text
Outline
Motivation
Why is anonymization hard?
Differential privacy
Applications
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=3)

### 原始文字层

````text
Data release horror stories
3
 NYC Taxi and Limousine 
Commission released 
anonymized data
 De-anonymize:
 Google images of a star getting out 
of a taxi (e.g. celebrity gossip blogs)
 Cross-reference with released data
 Alba took a taxi from Trump 
SoHo, and did not add a tip to 
$9 fare!
https://www.fastcompany.com/3036573/
nyc-taxi-data-blunder-reveals-which-celebs-dont-tip-and-who-frequents-strip-clubs
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Data release horror stories
                                                NYC Taxi and Limousine
                                                 Commission released
                                                 anonymized data
                                                De-anonymize:
                                                       Google images of a star getting out
                                                        of a taxi (e.g. celebr ity gossip blogs)
                                                       Cross-reference with released data
                                                Alba took a taxi from Tr   ump
                                                 SoHo, and did not add a tip to
                                                 $9 fare!
https://www.fastcompany.com/3036573/
ny c-taxi-data-bl u n d e r-reveals-whic h-celebs-dont-tip-and-who-frequents-str ip-clubs
                                                                                                3
````

### 图片文字 OCR（en-US，待对照原页）

````text
Data
release horror stories
Taxi & Limousine
Commission
Jessica Alba (actor)
htt s: / / www.fastcom an ".com/3036573/
NYC Taxi and Limousine
Commission released
anonymized data
D e -anonymize:
Google images of a star getting out
of a taxi (e.g. celebrity gossip blogs)
Cross-reference with released data
Alba took a taxi from Trump
SoHo, and did not add a tip to
$9 fare!
nvc-taxi-data-blunder-reveals-which-celebs-dont-ti -and-who-fre uents-stri -clubs
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=4)

### 原始文字层

````text
Data release horror stories
4 https://thedatamap.org/risks.html
````

### 图片文字 OCR（en-US，待对照原页）

````text
Data release horror stories
Matching Known Patients to Health Records
in Washington State Data
Phone
numbers
Addresses
ZIP
Age
Residence
Name
Sex
Hospital
Admit Month
Diagnoses
Residence
Name
Race
Sex
Ethnicity
Age
Procedures
Hospital
Admit Month
Physicians
Diagnoses
Costs
ZIP
Payment
Public Records
News Story
Step 1
News + Public Hospital Data
Step 2
Information from news accident reports uniquely and exactly
matched medical records in publicly available Washington State
health data in 43% of the cases, thereby putting names to patient
records.
https://thedatamap.org/risks.html
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=5)

### 原始文字层

````text
Data release horror stories
5
87% of all Americans can be 
uniquely identified using 3 bits 
of information: ZIP code, 
birth date, and gender.
We need to solve this data release problem...
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Data release horror stories
                                                                                                                                                                                                                                                                                                                                                   87% of all Amer  icans can be
                                                                                                                                                                                                                                                                                                                                                   uniquely identified using 3 bits
                                                                                                                                                                                                                                                                                                                                                   of infor   mation: ZIP code,
                                                                                                                                                                                                                                                                                                                                                   bir    th date, and gender.
We                                                            n                              e                              e                              d                                                            t                             o                                                            s                              o                              l                              v                        e                                                            t                             h                              i                             s                                                            d                              a                            t                             a                                                            r                           e                              l                              e                              a                              s                              e                                                            p                              r                           o                              b                         l                              e                              m                              .                             .                             .
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                5
````

### 图片文字 OCR（en-US，待对照原页）

````text
Data release horror stories
Strava's fitness tracker heat map reveals the
location of military bases
Geolocation isn't a new problem for the military
By Andrew Liptak I @AndrewLiptak I Jan 28, 2018, 3:51pm EST
Fitness tracking map reveals U.S. ess
Kandahar airbase, Afghanistan
0:57
A Commonwealth of Massachusetts
Group Insurance Commission
Your
Benefits
Connection
870 0 of all Americans can be
uniquely identified using 3 bits
of information: ZIP code,
birth date, and gender.
We need to solve this data release problem...
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=6)

### 原始文字层

````text
Why release data?
6
 Urban mobility modelling at scale
 Smart traffic design is critical since congestion gets worse
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Why release data?
 Urban mobility modelling at scale
       Smar   t traffic design is cr itical since congestion gets wor se
                                                                                  6
````

### 图片文字 OCR（en-US，待对照原页）

````text
Why release data?
Urban mobility modelling at scale
Smart traffic design is critical since congestion gets worse
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=7)

### 原始文字层

````text
Deep learning & big data
https://builtin.com/artificial-intelligence/ai-vs-machine-learning 7
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Deep learning & big data
        https://builtin.com/ar  tificial-intelligence/ai-vs-mac hine-lear  ning          7
````

### 图片文字 OCR（en-US，待对照原页）

````text
Deep learning & big data
Q)
Data
https://builtin.com/artificial -intelligence / ai-vs-machine-learnino
Large Neural Network
Small Neural Network
Traditional
Machine Learning
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=8)

### 原始文字层

````text
Big data to solve big problems
 Computation with big data:
 Statistical correlation (genetic association)
 Aggregate statistics (web analytics)
 Identify events (disease outbreaks)
 Data mining 
 Individual has useful data but wants privacy
 How can we work on sensitive data?
 Easy answer: Anonymize it and share
 Problem: How to do that?
8
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Big data to solve big problems
  Computation with big data:
        Statistical cor relation (genetic association)
        Agg  regate statistics (web analytics)
        Identify events (disease outbreaks)
        Data mining
  Individual has useful data but wants pr   ivac  y
  How can we work on sensitive data?
        Easy answer: Anonymize it and share
        Problem: How to do that?
                                                                                             8
````

### 图片文字 OCR（en-US，待对照原页）

````text
Big data to solve big problems
Computation with big data:
Statistical correlation (genetic association)
Aggregate statistics (web analytics)
Identify events (disease outbreaks)
Data mining
Individual has useful data but wants privacy
How can we work on sensitive data?
Easy answer: Anonymize it and share
Problem: How to do that?
significance
nature
The
Economist
slatisliv. making sense
BIG ORTH
The data deluge
ORTN Rno
THE CITY
POPULAR
SCIENCE
Review
CONTROL
OF
DATA iS
POW
Government
Executive
BIG
DATA
AGENCIES'
mm mm
noot
n nr
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=9)

### 原始文字层

````text
Outline
9
 Motivation
 Why is anonymization hard?
 Differential privacy
 Applications
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Outline
 Motivation
 Why is anonymization hard?
 Differential pr  ivac y
 Applications
                                                                          9
````

### 图片文字 OCR（en-US，待对照原页）

````text
Outline
Motivation
Why is anonymization hard?
Differential privacy
Applications
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=10)

### 原始文字层

````text
Defence against privacy attacks
10
 Anonymization techniques:
 Remove personally identifiable information
 K-anonymization
 Encryption techniques:
 Homomorphic encryption
 Multi-party computation
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Defence against privacy attacks
 Anonymization tec  hniques:
       Remove per sonally identifiable infor  mation
       K-anonymization
 Encr yption tec  hniques:
       Homomor phic encryption
       Multi-par   ty computation
                                                                                 10
````

### 图片文字 OCR（en-US，待对照原页）

````text
Defence against privacy attacks
Anonymization techniques:
Remove personally identifiable information
K-anonymization
Encryption techniques:
Homomorphic encryption
Multi-party computation
10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=11)

### 原始文字层

````text
User ID Name Address Account Sub. Date
001 Alice 123 A St Pro 01/02/20
002 Bob 234 B St Free 02/03/21
003 Charlie 456 C St Pro 03/04/18
Anonymization technique
11
User ID Name Address Account Sub. Date
001 Alice 123 A St Pro 01/02/20
002 Bob 234 B St Free 02/03/21
003 Charlie 456 C St Pro 03/04/18
 Principle:
 Remove identifying information in the data before releasing
 E.g. Sensitive columns (i.e. Name and Address) are masked
 Can we compute on anonymized data, i.e. not including 
personally identifiable information?
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Anonymization technique
           Pr  inciple:
                  Remove identifying infor  mation in the data before releasing
                  E.g. Sensitive columns (i.e. Name and Address) are masked
           Can we compute on anonymized data, i.e. not including
            per   sonally identifiable infor    mation?
User ID  Name     Address    Account    Sub. Date         User ID   Name     Address    Account   Sub. Date
001      Alice    123 A St   Pro        01/02/20          001       Alice    123 A St   Pro       01/02/20
002      Bob      234 B St   Free       02/03/21          002       Bob      234 B St   Free      02/03/21
003      Charlie  456 C St   Pro        03/04/18          003       Charlie  456 C St   Pro       03/04/18
                                                                                                          11
````

### 图片文字 OCR（en-US，待对照原页）

````text
Anonymization technique
e Principle:
identifying information in the data before releasing
Remove
E.g. Sensitive columns (i.e. Name and Address) are masked
Can we compute on anonymized data, i.e. not including
personally identifiable information?
User ID Name
Address
123 A St
234 B St
456 C St
Account Sub. Date
User ID Name
001
002
003
Address
Account Sub. Date
001
002
003
Alice
Bob
Charlie
Pro
Free
Pro
01/02/20
02/03/21
03/04/18
Pro
Free
Pro
01/02/20
02/03/21
03/04/18
11
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=12)

### 原始文字层

````text
Linkage attack
12
 Netflix challenge:
 Netflix released its database for the $1 million contest
 Sanitization: Personal identities removed
 Sparsity of data:
 No two Netflix records are similar more than 50% with high probability
 If profiles can be matched up to 50% to a profile in IMDB, then adversary 
knows the true identity of the profile w.h.p.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Linkage attack
   Netflix c  hallenge:
           Netflix released its database for the $1 million contest
           Sanitization: Per sonal identities removed
   Spar  sity of data:
           No two Netflix records are similar more than 50% with high probability
           If profiles can be matc  hed up to 50% to a profile in IMDB, then adver sary
            knows the tr  ue identity of the profile w.                        h                        .                        p.
                                                                                                                     12
````

### 图片文字 OCR（en-US，待对照原页）

````text
Linkage attack
e Netflix challenge:
Netflix released its database for the $ 1 million contest
Sanitization: Personal identities removed
Sparsity of data:
No two Netflix records are similar more than 500 0 with high probability
If profiles can be matched up to 500 0 to a profile in IMDB, then adversary
knows the true identity of the profile w.h.p.
IMDb
NETFLIX
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=13)

### 原始文字层

````text
Personally identifiable information (PII)
13
 PII definitions (from Wikipedia):
 US: Information which can be used to distinguish or trace an individual's identity, 
such as their name, social security number, biometric records, etc. alone, or when 
combined with other personal or identifying information which is linked or linkable 
to a specific individual, such as date and place of birth, mother’s maiden name,...
 EU: 'personal data' shall mean any information relating to an identified or 
identifiable natural person ('data subject'); an identifiable person is one who can be 
identified, directly or indirectly, in particular by reference to an identification 
number or to one or more factors specific to his physical, physiological, mental, 
economic, cultural or social identity;
 Problem:Without releasing entire data, how can we 
compute some innocent statistics for analysis?
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Personally identifiable information (PII)
  PII definitions (from Wikipedia):
          US: Infor  mation which can be used to distinguish or trace an individual's identity,
           such as their name, social secur  ity number, biometr  ic records, etc. alone, or when
           combined with other personal or identifying infor  mation which is linked or linkable
           to a specific individual, such as date and place of bir  th, mother’s maiden name,...
          EU: 'personal data' shall mean any infor  mation relating to an identified or
           identifiable natural person ('data subject'); an identifiable person is one who can be
           identified, directly or indirectly, in par  ticular by referen ce to an identification
           number or to one or more factors specific to his physical, physiolog ical, mental,
           economic, cultural or social identity;
  Problem: Without releasing entire data, how can we
   compute some innocent statistics for analysis?
                                                                                                         13
````

### 图片文字 OCR（en-US，待对照原页）

````text
Personally identifiable information (PII)
PII definitions (from Wikipedia) :
US: Information which can be used to distinguish or trace an individual's identity,
such as their name, social security number, biometric records, etc. alone, or when
combined with other personal or identifying information which is linked or linkable
to a specific individual, such as date and place ofbirth, mother's maiden name
ELI: 'personal data' shall mean any information relating to an identified or
identifiable natural person ('data subject); an identifiable person is one who can be
identified, directly or indirectly, in particular by reference to an identification
number or to one or more factors specific to his physical, physiological, mental,
economic, cultural or social identity;
e Problem:
Without releasing entire data, how can we
for analysis?
compute some innocent
statistics
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=14)

### 原始文字层

````text
Attacks from published statistics
14
````

### 图片文字 OCR（en-US，待对照原页）

````text
Attacks from published statistics
Learning Your Identity and Disease from Research Papers:
Information Leaks in Genome Wide Association Study
Rui Wang, Yong Li, XiaoFeng Wang, Haixu Tang, Xiaoyong Zhou
Indiana University Bloomington
Bloomington, IN
{wang63,yonli,xw7,hatang,zhou}@indiana.edu
Abstract
Genome-wide association studies (GWAS) aim at discovering the
association between genetic variations, particularly single-nucleotide
polymorphism (SNP), and common diseases, which have been well
recognized to be one of the most important and active areas in
biomedical research. Also renowned is the privacy implication of
such studies, which has been brought into the limelight by the re-
cent attack proposed by Homer et al. Homer's attack demonstrates
that it is possible to identify a participant ofa GWAS from analyz-
1. INTRODUCTION
The rapid advancement in genome technology has revolutionized
the field of human genetics by enabling the large-scale applications
of genome-wide association study (GWAS) [7], a study that aims
at discovering the association between human genes and common
diseases. To this end, GWAS investigators determined the geno-
types of two groups of participants, people with a disease (cases)
and similar people without (controls) in an attempt to use statisti-
cal testing to identify genetic markers, typically single-nucleotide
14
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=15)

### 原始文字层

````text
Database privacy
15
Queries
 Need a formal privacy definition since ad-hoc solutions do 
not work
 How can we have privacy-preserving queries?
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Database privacy
                              Quer  ies
 Need a for   mal pr  ivac y definition since ad-hoc solutions do
  not work
 How can we have pr  ivac y-preser     ving quer   ies?
                                                                              15
````

### 图片文字 OCR（en-US，待对照原页）

````text
Database privacy
Queries
Need a formal privacy definition since ad-hoc solutions do
not work
How can we have privacy-preserving queries?
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 16 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=16)

### 原始文字层

````text
Blending into a crowd
16
 “I am safe in a group of K or more!”
 K could vary in (3, … 100, … , 5.1M)
 Reasons:
 Rare properties help re￾identify someone
 Privacy is “protection of 
being brought to the 
attention of others”
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Blending into a crowd
  “I am safe in a g  roup of K or more!”
        K could vary in (3, … 100, … , 5.1M)
  Reasons:
        Rare proper   ties help re-
         identify someone
        Pr ivac y is “protection of
         being brought to the
         attention of other s”
                                                                                            16
````

### 图片文字 OCR（en-US，待对照原页）

````text
Blending into a crowd
"I am safe in a group of K or more!"
K could vary in (3,
100, ... , 5.1M)
Reasons:
Rare properties help re
identify someone
Privacy is "protection of
being brought to the
attention of others"
The Yale Law Journal
Volume 89, Number 3, January 1980
Privacy and the Limits of Law
Ruth Gavisont
Anyone who studies the law of privacy today may well feel a sense of
uneasiness. On one hand, there are popular demands for increased
protection of privacy, discussions of new threats to privacy, and an
intensified interest in the relationship between privacy and other
16
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 17 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=17)

### 原始文字层

````text
Cluster-based definition
17
 K-anonymity:
 Attributes are suppressed or generalized until each row is identical to at least 
K – 1 other rows. The database is called K-anonymous.
 Linkage attack will result in a group of K records
 Methods:
 Suppression: Replace individual attributes with a *
 Generalization: Replace individual attributes with a broader category (e.g. 
office: CBD ⇒ office: Auckland)
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Cluster-based def inition
  K  -anonymity:
         Attr ibutes are suppressed or ge n e ra l i ze d until eac  h row is identical to at least
          K – 1 other rows. The database is called K-anonymous.
         Linkage attac  k will result in a g  roup of   K records
  Methods:
         Suppression: Replace individual attr ibutes with a *
         Generalization: Replace individual attr ibutes with a broader category (e.g.
          office: CBD ⇒ office: Auc  kland)
                                                                                                   17
````

### 图片文字 OCR（en-US，待对照原页）

````text
Cluster-based definition
K-anonymity:
Attributes are suppressed or generalized until each row is identical to at least
K — 1 other rows. The database is called K-anonymous.
Linkage attack will result in a group of K records
Methods:
Suppression: Replace individual attributes with a *
Generalization:
Replace individual attributes with a broader category (e.g.
office: CBD office: Auckland)
17
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 18 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=18)

### 原始文字层

````text
Why is anonymization hard?
18
 High-dimensional/high-resolution data is essentially unique
 Significant computations to achieve K-anonymity
 Low-dimension/low-resolution is more private, but less 
useful in analysis
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Why is anonymization hard?
  High-dimensional/high-resol ut i on  dat a   i s  essent i a l ly   uni que
        Significant computations to ac  hieve K-anonymity
  Low-dimension/low-resol ut i on  i s  m ore  pr   i vat e,  but   l ess
   useful in analysis
                                                                                      18
````

### 图片文字 OCR（en-US，待对照原页）

````text
Why is anonymization hard?
High-dimensional/ high-resolution data is essentially unique
Significant computations to achieve K-anonymity
office department date joined salary d.o.b.
nationality gender
Apr 2015 May 1985 Portuguese Female
London
Low-dimension/ low-resolution is more private, but less
useful in analysis
office department date joined salary d.o.b.
2015
1985
nationality gender
Female
18
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 19 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=19)

### 原始文字层

````text
Encryption techniques
19
 Encryption:
 A cryptography approach converts the original representation of 
information (plaintext) into an alternative form (ciphertext)
 Common techniques:
 Homomorphic encryption (HE)
 Secure multi-party computation (MPC)
https://www.twilio.com/blog/what-is-public-key-cryptography
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Encr    yption techniques
  Encr yption:
         A cryptog  raphy approac  h conver   ts the or ig  inal representation of
          infor  mation (plaintext) into an alter  native for  m (cipher   text)
  Common tec  hniques:
         Homomor phic encryption (HE)
         Secure multi-par   ty computation (MPC)
            https://www.twilio.com/blog/what-is-public-key-cryptog raphy                         19
````

### 图片文字 OCR（en-US，待对照原页）

````text
Encryption techniques
e Encryption:
A cryptography approach converts the original representation of
information (plaintext) into an alternative form (ciphertext)
Common techniques
Homomorphic encryption (HE)
Secure multi-party computation (MPC)
Bob,
Stop trying
to make
fetch happen.
- Alice
plaintext
Bob's
Public Key
Encrypt
keys are different but
mathematically linked
PIQ6NzOKW
CXSL03zta+
soRTuwJ/7JO
Q7gzwyJBuy
CYBn
ciphertext
Bob's
Private Key
Decrypt
Bob,
Stop trying
to make
fetch happen.
- Alice
plaintext
htt s: / /www.twilio.com/bloo/what-is-
ublic-kev-cr toora h
19
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 20 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=20)

### 原始文字层

````text
Homomorphic encryption (HE)
 Allow computations on encrypted data without decrypting it
 Use a public key to encrypt data, and apply algebraic system (e.g. addition, 
multiplication) to allow computations on ciphertext
 Only person with matching private key can access the decrypted results
Wood et al., CSUR 2020 20
同态
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Homomorphic encr    yption (HE)
           同态
     Allow computations on encr ypted data without decr ypting it
                  Use a public key to encrypt data, and apply algebraic system (e.g. addition,
                   multiplication) to allow computations on cipher   text
                  Only per son with matc  hing pr ivate key can access the decrypted results
                                                          Wo                  o                  d                                     e                 t                                    a                  l                  .                 ,                             C                  S                 U                 R                                    2                  0                  2                  020
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Homomorphic encryption (HE)
Allow computations on encrypted data without decrypting it
public key to encrypt data ， and ap p ly algebraic system (e.g. addition ，
use a
multiplication) tO all ow computations on ciphertext
O nly person with matching private key
c an access the decrypted results
Addition
Encryption
Encryvtion
x + Y
Homomorphic
Wood et al., CSUR 2020
[x + yJ
Homomorph1c
Evaluation
x + Y
l)ecryption
20
````

### 图片文字 OCR（en-US，待对照原页）

````text
Homomorphic encryption (HE)
Allow computations on encrypted data without decrypting it
public key to encrypt data, and apply algebraic system (e.g. addition,
use a
multiplication) to allow computations on ciphertext
Only person with matching private key can access the decrypted results
Addition
Encryption
Encryption
Homomorphic
Addition
CSUR 2020
Homomorphic
Evaluation
Decryption
Decryption
oo
1
1
Wood et al. ,
20
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 21 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=21)

### 原始文字层

````text
Homomorphic encryption (HE)
 Use cases:
 In machine learning, training data are encrypted and sent to a server 
(cloud) for model aggregation. Only authorized parties can access model.
 Data owner wants to use MLaaS (Machine Learning as a Service) or cloud 
computing services but does not trust the service provider
21
https://www.usenix.org/conference/atc20/presentation/zhang-chengliang
梯度
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Homomorphic encr    yption (HE)
  Use cases:
         In mac  hine lear  ning, training data are encrypted and sent to a ser   ver
          (cloud) for model agg  regation. Only author ized par   ties can access model.
         Data owner wants to use MLaaS (Mac  hine Lear  ning as a Ser   vice) or cloud
          computing ser   vices but does not tr  ust the ser   vice provider
              梯度
       https://www.usenix.org/conference/atc20/presentation/zhang     -chengliang                   21
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Homomorphic encryption (HE)
． cases:
ln machine learning, training data are encrypted and sent tO a server
(cloud) for model aggregation · O nly authorized parties can access model.
D ata owner wants tO use MLaaS (Machine Learning as a Service) or cloud
c omp uting services b ut does not trust the service provider
Aggregator
O Aggregation
@ Encryption
． Gr
com utation
Single CIient
Gradients
Aggregated
Gradients
丶 ClientA
@ Decryption
（ Encryption
Model
《 《 ． Gradient
u date
com putation
HE PubIic Key
HE P rivate Key
Client N
Client B
@ Decryption
Model
update
21
https ： / / www.uscnix ． 0 / confercncc / atc20 /prcscntation / zhang-chcngliang
````

### 图片文字 OCR（en-US，待对照原页）

````text
Homomorphic encryption (HE)
use cases:
In machine learning, training data are encrypted and sent to a server
(cloud) for model aggregation. Only authorized parties can access model.
Data owner wants to use MLaaS (Machine Learning as a Service) or cloud
computing services but does not trust the service provider
Aggregator
O Aggregation
@ Encryption
com utation
Single Client
Gradients
Aggregated
Gradients
Client A
@ Decryption
@ Encryption
Model
I I O Gradient
u date
computation
HE Public Key
HE Private Key
Client NI
Client Bl
@ Decryption
5 Model
update
21
https : / / www.usenix.org/conference/atc20/presentation/zhang-chcngliang
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 22 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=22)

### 原始文字层

````text
Secure multi-party computation (MPC)
22
 Allow multiple parties to jointly perform computation over 
their private data without sharing it
 Each party does not trust other parties or the server
Lemus et al. 2019
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Secure multi-par     ty computation (MPC)
  Allow multiple par    ties to jointly perfor   m computation over
   their pr  ivate data without shar  ing it
        Eac  h par   ty does not tr  ust other par   ties or the ser   ver
                                                            Lemus et al. 2019          22
````

### 图片文字 OCR（en-US，待对照原页）

````text
Secure multi-party computation (MPC)
Allow multiple parties to jointly perform computation over
their private data without sharing it
Each party does not trust other parties or the server
8
YN
Lemus et al.
2019
22
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 23 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=23)

### 原始文字层

````text
Secure multi-party computation (MPC)
23
 Use cases:
 Query a database to get information without revealing the question 
asked (i.e. private information retrieval)
 Secure auction
 Insurance companies want to know the common flagged customers and 
their activities without sharing the whole flagged customer list
 Covid contact tracing (e.g. each user has a set of locations)
https://en.wikipedia.org/wiki/
Private_set_intersection
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Secure multi-par     ty computation (MPC)
  Use cases:
         Query a database to get infor  mation without revealing the question
          asked (i.e. pr ivate infor  mation retr ieval)
         Secure auction
         Insurance companies want to know the common flagged customer s and
          their activities without shar ing the whole flagged customer list
         Covid contact tracing (e.g. eac  h user has a set of locations)
                                                                  https://en.wikipedia.org/wiki/
                                                                  Pr ivate_set_inter section     23
````

### 图片文字 OCR（en-US，待对照原页）

````text
Secure multi-party computation (MPC)
use cases:
Query a database to get information without revealing the question
asked (i.e. private information retrieval)
Secure auction
Insurance companies want to know the common flagged customers and
their activities without sharing the whole flagged customer list
Covid contact tracing (e.g. each user has a set of locations)
4
Alice
Alice's Set
1
2
3
Bob
5
9
Bob's Set
https://en.wikipedia.org/wiki/
Private set intersection
23
````

### 图表辅助说明

隐私集合交集插图：Alice 与 Bob 各有一个集合，用重叠区域表示共同元素；两边红叉提示不要泄露各自的非交集内容。该图辅助说明安全多方计算的 private set intersection 用途。

## PDF 第 24 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=24)

### 原始文字层

````text
HE vs MPC
24
 MPC protects the privacy of data in collaborative learning
 Each party does not trust the others or the server
 HE keeps the data hidden from external adversaries
 Only the data owner can decrypt the result
 Both require significant computations and communication 
overheads and are often infeasible for big data
 A large number of rounds to aggregate the models
 Significant computation on the ciphertext
 Impractical for most of big data primitives
expensive
we 不可行
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
HE vs MPC
  MPC protects the pr   ivac  y of data in                      collaborative lear    ning
          Eac  h par   ty does not tr  ust the other s or the ser   ver
  HE keeps the data hidden from exter    nal adver  sar  ies
          Only the data owner can decrypt the result
  Both require significant computations and communication ex p e n s i ve
   ov e    r    h    e    a    d    s         a    n    d         a    r   e         o    f    t    e    n     infeasible for big data
          A large number of rounds to agg  regate the modelswe不可⾏
          Significant computation on the cipher   text
          Impractical for most of big data pr imitives
                                                                                                             24
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
H E vs MPC
MPC protects the privacy of data in collaborative learning
Each p ar ty does not trust the others or the server
HE keeps th e data hidden from
external adversarles
Only the data owner c an decrypt the result
BOth require significa t computations an d communication
overheads an d ar e Often
infeasible f big data
A larg e numb er of rounds to aggregat
models
Significant computation on the ciphertext
lmpractical for most Of big data primitives
24
````

### 图片文字 OCR（en-US，待对照原页）

````text
HE vs MPC
MPC protects the privacy of data in collaborative learning
Each party does not trust the others or the server
HE keeps the data hidden from
external adversaries
Only the data owner can decrypt the result
e.Fr9
Both require significant computations and communication
overheads and are often
infeasible f r big data
A large number of rounds to aggregat
models
Significant computation on the ciphertext
Impractical for most of big data primitives
24
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 25 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=25)

### 原始文字层

````text
Privacy expectations
25
 Unreasonable privacy expectations:
 Privacy for free? No, privatizing requires removing information (hence 
accuracy loss) or increasing computation
 Absolute privacy? No, your neighbor’s habits are correlated with your habit
 Reasonable privacy expectations:
 Quantitative: Offer a knob to tune accuracy vs privacy loss
 Plausible deniability:Your presence in a database cannot be ascertained
 Prevent targeted attacks: Limit information leaked even in the presence of 
side knowledge
在里的
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Privacy expectations
  Unreasonable pr  ivac y expectations:
         Pr  ivac y for free? No, pr ivatizing requires removing infor  mation (hence
          accurac y loss) or increasing computation
         Absolute pr  ivac y? No, your neighbor’s habits are cor related with your habit
  Reasonable pr  ivac y expectations:
         Quantitative: Offer a knob to tune accurac y vs pr ivac y loss
         Plausible deniability:在⾥的 Your presence in a database cannot be ascer   tained
         Prevent targeted attacks: Limit infor  mation leaked even in the presence of
          side knowledge
                                                                                                  25
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Privacy expectations
． Unreasonable privacy expectations ：
NO, pr ivati zing requires removing information (hence
accuracy IOSS) or mcreasing computation
Absolute privacy? NO, your neighbor's habits are correlated with your habit
． Reasonable privacy expectations ：
Offer a knob tO tun e accuracy VS privacy IOSS
Qyantit ：
Your presence in a database cannot be ascertained
Prevent e d attacks: Limit information leaked even in th e presence Of
side knowledge
25
````

### 图片文字 OCR（en-US，待对照原页）

````text
Privacy expectations
Unreasonable privacy expectations:
Privacyforfree? No, privatizing requires removing information (hence
accuracy loss) or increasing computation
Absolute privacy? No, your neighbor's habits are correlated with your habit
Reasonable privacy expectations:
Offer a knob to tune accuracy vs privacy loss
Qyantit tive:
ä Sl le deniability: Your presence in a database cannot be ascertained
Limit information leaked even in the presence of
Prevent targeted attacks:
side knowledge
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 26 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=26)

### 原始文字层

````text
Privacy for free?
26
 I feel safe submitting a survey if I knew that my answer had 
no impact on the released results
 Q(DI-me) = Q(DI)
 But… if individual answers had no impact on the released 
results, the results would have no utility
 Q(DI) = Q(D⌀)
 Problem: Trade-off between privacy and utility
薇
石衡 蒳
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Privacy for free?
  I feel safe submitting a sur     vey if I knew that my answer had
   no impact on the released results
        Q(DI-me) = Q(DI)
  But… if individual answer  s had no impact on the released
   resul t s,  t he  resul t s  woul d  have no utility
         Q(DI) = Q(D⌀)
                                                薇
  Problem: Tr             a             d            e-off between pr   ivac  y and utility
                    ⽯衡                                       蒳
                                                                                        26
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Privacy fO r free?
I feel safe submitting a sur vey if I knew that my answer had
on th e released results
no impact
． Q(DI-me) = Q(DI)
。 if individual answers had no impact on th e released
But ·
results ， th e results would have no utility
Q(DI) = Q(DØ)
． Problem ： Trade-off between privacy an d uy!!_!,y
26
````

### 图片文字 OCR（en-US，待对照原页）

````text
Privacy for free?
I feel safe submitting a survey if I knew that my answer had
no impact on the released results
= Q(DI)
if individual answers had no impact on the released
But. ..
results, the results would have no utility
Q(DI) = Q(DØ)
Problem: Trade-off between privacy and
26
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 27 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=27)

### 原始文字层

````text
Absolute privacy?
27
 I feel safe submitting a survey if I knew that any attacker 
looking at the released results R could not learn w.h.p. any 
new information about me personally
 Pr [secret(me) | R] = Pr [secret(me)]
 But… if R shows a strong trend in my population (e.g. 
everyone is age 20 – 30 and likes Taylor Swift), w.h.p. the trend is 
true of me too (even if I do not submit a survey)
 Pr [secret(me) | R] > Pr [secret(me)]
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Absolute privacy?
   I feel safe submitting a sur     vey if I knew that any attac  ker
    looking at the released results R could not lear    n w.                                h                               .                                p.       a     n  y
    new infor   mation about me per  sonally
            Pr [secret(me) | R] = Pr [secret(me)]
   But… if R shows a strong trend in my population (e.g.
    everyone is age 20 – 30 and likes Taylor Swift), w.                                h                               .                                p.       t      h     e      trend is
    tr   ue of me too (even if I do not submit a sur     vey)
            Pr [secret(me) | R] > Pr [secret(me)]
                                                                                                                               27
````

### 图片文字 OCR（en-US，待对照原页）

````text
Absolute privacy?
I feel safe submitting a survey if I knew that any attacker
looking at the released results R could not learn w.h.p. any
new information about me personally
Pr [secret(me) I R] = Pr [secret(me)]
But... if R shows a strong trend in my population (e.g.
everyone is age 20 30 and likes Taylor Swift), w.h.p. the
trend is
true of me
too (even if I do not submit a survey)
Pr [secret(me) I RI > Pr
27
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 28 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=28)

### 原始文字层

````text
Absolute privacy?
28
 Even worse, if an attacker knows something about me related
to general facts about the populations, then releasing these 
general facts gives the attacker specific information about me 
(even if I do not submit a survey)
 From a survey, there is a strong 
correlation between smoking and 
being cancer
 If the insurance company knows 
that Alice is a smoker, it will 
increase her premium (even Alice 
had not submitted a survey)
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Absolute privacy?
  Even wor  se, if an attac  ker knows something about me rel at ed
   to general facts about the populations, then releasing these
   general facts g  ives the attac  ker specific infor   mation about me
   (even if I do not submit a sur     vey)
  From a sur   vey, there is a strong
   cor relation between smoking and
   being cancer
  If the insurance company knows
   that Alice is a smoker, it will
   increase her premium (even Alice
   had not submitted a sur   vey)
                                                                                          28
````

### 图片文字 OCR（en-US，待对照原页）

````text
Absolute privacy?
Even worse, if an attacker knows something about me
related
general facts about the populations, then releasing these
to
general facts gives the attacker specific information about me
(even if I do not submit a survey)
From a survey, there is a strong
correlation between smoking and
being cancer
If the insurance company knows
that Alice is a smoker, it will
increase her premium (even Alice
had not submitted a survey)
0020
0.015
0.010
O.cos
go
20
60
40
Smoking intensity (cigarettes/day)
28
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 29 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=29)

### 原始文字层

````text
Reasonable privacy expectations 
29
 We cannot promise:
 My data will not affect the results
 An attacker could not learn new information about me, giving proper 
background information
 I feel safe submitting a survey…
 … if I knew the chance that the privatized released result R
was nearly the same, whether or not I submitted my 
information
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Reasonable privacy expectations
      We                                                    c                          a                          n                          n                          o                          t                                                     p                          r                        o                          m                           i                          s                          e                         :
                    My data will not affect the results
                    An attac    ker could not lear     n new infor     mation about me, g    iving proper
                     bac    kg    round infor     mation
      I feel safe submitting a sur     vey…
      … if I knew the c  hance that the pr  ivatized released result R
       wa s   nea r ly   t h e  s a m e, whether or not I submitted my
       infor   mation
                                                                                                                                                                                                          29
````

### 图片文字 OCR（en-US，待对照原页）

````text
Reasonable privacy expectations
We cannot promise:
My data will not affect the results
An attacker could not learn new information about me, giving proper
background information
I feel safe submitting a survey...
if I knew the chance that the privatized released result R
was nearly the same,
whether or not
I submitted my
information
29
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 30 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=30)

### 原始文字层

````text
Differential privacy
30
https://blog.openmined.org/a-survey-of-differential-privacy-frameworks/
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Dif    ferential privacy
    https://blog.openmined.org/a-sur   vey-of-differential-pr ivacy-frameworks/
                                                                                                 30
````

### 图片文字 OCR（en-US，待对照原页）

````text
Differential privacy
privacy
privacy
Model 1
Model 2
https://blog.openmincd.org/a-survey-of-differential-privacy-framcworks/
30
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 31 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=31)

### 原始文字层

````text
The promise of differential privacy
31
 Dwork and Roth, 2014:
 Differential privacy describes a promise, made by a data holder, or curator, to a data 
subject: “You will not be affected, adversely or otherwise, by allowing your data to be 
used in any study or analysis, no matter what other studies, data sets, or information 
sources, are available.”
 The 2017 Gödel Prize award to Dwork, McSherry, Nissim, Smith
 Differential privacy was carefully constructed to avoid numerous and subtle pitfalls
that other attempts at defining privacy have faced.
 The intellectual impact of differential privacy has been broad, with influence on the
thinking about privacy being noticeable in a huge range of disciplines, ranging from
traditional areas of computer science (databases, machine learning, networking,
security) to economics and game theory, false discovery control, official statistics and
econometrics, information theory, genomics and, recently, law and policy.
三一
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
The promise of dif    ferential privacy
   Dwork and Roth, 2014:
             Differential pr  ivac y descr  ibes a promise, made by a data holder, or curator, to a data
              subject:“You will not be affected, adversely or otherwise, by allowing your data to be
              used in any study or analysis, no matter what other studies, data sets, or infor  mation
              sources, are available.”
                                                                     三⼀
   The 2017 Gödel Pr  ize award to Dwork,      M     c     S     h     e     r        r       y,      N     i     s     s     i     m     ,      S     m     i     t     h
             Differential pr   ivac y was carefully constr ucted to avoid numerous and subtle pitfalls
              that other attempts at defining pr   ivac y have faced.
             The intellectual impact of differential pr   ivac y has been broad, with influence on the
              thinking about pr   ivac y being noticeable in a huge range of disciplines, ranging from
              traditional areas of computer science (databases, machine lear   ning, networking,
              secur   ity) to economics and game theory, false discovery control, official statistics and
              econometr   ics, infor   mation theory, genomics and, recently, law and polic y.
                                                                                                                                         31
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
The promise Of differential privacy
． D wo rk an d Roth, 2014 ：
D 《 ℃ ntial privacy descri es a rom 八 a de 0 ／ a data holder, or curator, 0 a data
subject:"You 而 77 not g 彦 d ， adversely or r 而 ， d770 而 劐 your be
used in S 丿 厂 ana IS, no matter What 0 為 er sttldies, data sets, or lnformation
sources, are available.
． The 2017 Gödel Prize award to Dwork, McSherry, Nissim, Smith
Different1al privacy was c “ 冒 0 constructed 艹 0 numerous and subtle 77S
0 “ mp defining privacy 為 ‰ 和 ce
丆 in llec 山 引 mpact 酽 d 毋 enti 引 privacy 為 been broad, 而 mJluence on the
in 劐 a 旆 privacy b 劐 noticeable in a 為 u 俨 range 酽 disciplines, rangingfrom
a 諂 00nd7 areas ofcomputer sci en ce (databases, machine learning, networking,
security 丿 0 economics and game theory,false discovery con 07 ， ？ 龙 ial statistics and
econometrics, ll?formation 為 eo 《 ， ' ， genomics and, recen ， ' law and PO 方 ， ' ·
31
````

### 图片文字 OCR（en-US，待对照原页）

````text
The promise of differential privacy
Dwork and Roth, 2014:
Differential privacy describes a romise, ade by a data holder, or curator, to a data
subject: "You will not be affected, adversely or otherwise, by allowing your data to be
used in a s yor ana IS, no matter what other studies, data sets, or in ormation
sources, are available."
The 2017 Gödel Prize award to Dwork, McSherry, Nissim, Smith
Differential privacy was carefully constructed to avoid numerous and subtle pitfalls
that other attempts at defining privacy have face
The intellectual impact of differential privacy has been broad, with influence on the
thinking about privacy being noticeable in a huge range of disciplines, ranging from
traditional areas of computer science (databases, machine learning, networking,
security) to economics and game theory, false discovery control, official statistics and
econometrics, ifformation theory, genomics and, recently, law and policy.
31
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 32 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=32)

### 原始文字层

````text
Outline
32
 Motivation
 Why is anonymization hard?
 Differential privacy (DP)
 Definition
 Mechanism
 Local DP vs global DP
 DP variants and properties
 Applications
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Outline
  Motivation
  Why is anonymization hard?
  Differential pr  ivac y (DP)
        Definition
        Mec  hanism
        Local DP vs global DP
        DP var iants and proper   ties
  Applications
                                                                                    32
````

### 图片文字 OCR（en-US，待对照原页）

````text
Outline
Motivation
Why is anonymization hard?
Differential privacy (DP)
Definition
Mechanism
Local DP vs global DP
DP variants and properties
Applications
32
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 33 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=33)

### 原始文字层

````text
DP concept
33
D
Algorithm
Prob(R)
Alice Bob Chris Donna Ernie
_ 敏感数据
Data
Set
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
DP concept
Prob(R)
0
Algorithm
0
33
````

### 图片文字 OCR（en-US，待对照原页）

````text
DP concept
D Alice
pod
Prob(R)
Bob
Chris
Algorithm
Donna
Ernie
33
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 34 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=34)

### 原始文字层

````text
DP concept
34
D
Algorithm
Prob(R)
Alice Bob Chris Xaver Donna Ernie
replace
remove data
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
re p l a c e
  DP concept                                re m ove  data
                                             Xavier
      D      Alice           Bob             Chr is         Donna          Er   nie
                                       Algor ithm
Prob(R)
                                                                                          34
````

### 图片文字 OCR（en-US，待对照原页）

````text
DP concept
re ace ,
daåa,
temuo
D Alice
Prob(R)
Bob
Xavier
Algorithm
Donna
Ernie
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 35 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=35)

### 原始文字层

````text
DP concept
35
D
Algorithm
Prob(R)
ratio bounded
Alice Bob Chris Xaver Donna Ernie
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
DP concept
                                             Xavier
      D      Alice           Bob             Chr is        Donna          Er   nie
                                      Algor ithm
                                                          ratio bounded
Prob(R)
                                                                                         35
````

### 图片文字 OCR（en-US，待对照原页）

````text
DP concept
D Alice
Prob(R)
Bob
Xavier
Algorithm
Donna
ratio bounded
Ernie
````

### 图表辅助说明

差分隐私概念图把其中一位个人记录替换为红色 Xavier 文件夹；算法下方画出替换前后相近的输出概率曲线，并强调同一输出处概率比有界。曲线接近的约束针对相邻数据集。

## PDF 第 36 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=36)

### 原始文字层

````text
DP definition
36
 X: The data universe
 D ⊂	X: The data set (one element per person)
 The neighboring relation captures what is protected
Definition: Two datasets D, D’ ⊂ X are neighbors if 
they differ in the data of a single individual
断体数据差异
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
DP def inition
            X: T     h     e            d     a    t      a            u     n     i      v   e     r         s     e
            D ⊂	X: T     h     e            d     a    t      a            s     e     t             (     o     n     e            e     l     e     m      e     n     t             p     e     r             p     e     r         s     o     n     )
                                                                                                                        断             体数据差异
Definition: Tw                   o                                                         d                            a                          t                            a                             s                            e                            t                            s                             D,        D       ’ ⊂ X are neighbors if
they differ in the data of a single individual
            The neighbor  ing relation captures what is protected
                                                                                                                                                                                                                                                36
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
DP definition
X: Th e data universe
D 匚 X: The data set (one element per per 0
Definition ：
Two datasets D, D' 匚 X are neighbors if
they differ in the data of a single individual
Th e neighboring relation captures
wh at
is protected
36
````

### 图片文字 OCR（en-US，待对照原页）

````text
DP definition
X: The data universe
D C X: The data set (one element per per o
Definition:
Two datasets D, D' C X are neighbors if
they differ in the data of a single individual
The neighboring relation captures
what
is protected
36
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 37 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=37)

### 原始文字层

````text
DP definition
37
 X: The data universe
 D ⊂	X: The data set (one element per person)
 Privacy parameter: ε	≥	0
 The probability bound captures how much protection we get
Definition: An algorithm M is ε-differentially private if for all
pairs of neighboring datasets D, D’, and for all outputs R:
 Pr [M(D) = R] ≤ eε Pr [M(D’) = R]
ET 保护b
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
DP def inition
        X: T     h     e            d     a    t      a            u     n     i      v   e     r         s     e
        D ⊂	X: T     h     e            d     a    t      a            s     e     t             (     o     n     e            e     l     e     m      e     n     t             p     e     r             p     e     r         s     o     n     )
        Pr   ivac  y parameter:                       ε  	≥	0                                            ET               保护b
Definition: An algor  ithm M is ε-differentially pr  ivate if for all
pair  s of neighbor  ing datasets D,       D      ’,       a       n       d              f      o       r        all outputs R:
               Pr [M(D) = R] ≤ eε Pr [M(D’) = R]
        The probability bound captures how muc  h protection we get
                                                                                                                                                        37
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
DP definition
X: Th e data universe
D 匚 X: The data set (one element per person)
E 0
Privacy parameter ：
An algorithm M is E-differentially private if for 引 7
Definition:
p air s of neighboring datasets D, D' and for d77 outputs R:
Pr [M(D) = RI 孓 Pr [M(D') = R]
Th e probability bound captures
h ow much
protection we get
37
````

### 图片文字 OCR（en-US，待对照原页）

````text
DP definition
X: The data universe
D C X: The data set (one element per person)
Privacy parameter:
An algorithm M is E-differentially private if for all
Definition:
pairs of neighboring datasets D, II, and for all outputs R:
The probability bound captures
how much protection we get
37
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 38 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=38)

### 原始文字层

````text
ε-indistinguishable
38
xn
xn-1

x3
x2
x1
M
query 1
answer 1
query T
answer T
D 
random coins
¢ ¢ ¢ 
output
R
xn
xn-1

y3
x2
x1
M
query 1
answer 1
query T
answer T
D’ 
random coins
¢ ¢ ¢ 
output
R’
Differ in 1 row
Distance 
between 
distributions
is at most ee
````

> 文字层存在可疑字体映射／乱码；下方 OCR 可辅助对照。原始字符仍保留。

### 图片文字 OCR（en-US，待对照原页）

````text
e-indistinguishable
D'
xn-I
x
xn-I
x
random coins
random coins
query 1
answer 1
query T
answer T
query 1
answer 1
query T
answer T
output
Distance
between
distributions
is at most eE
output
R'
38
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 39 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=39)

### 原始文字层

````text
Outline
39
 Motivation
 Why is anonymization hard
 Differential privacy (DP)
 Definition
 Mechanism
 Local DP vs global DP
 DP variants and properties
 Applications
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Outline
  Motivation
  Why is anonymization hard
  Differential pr  ivac y (DP)
        Definition
        Mec  hanism
        Local DP vs global DP
        DP var iants and proper   ties
  Applications
                                                                                    39
````

### 图片文字 OCR（en-US，待对照原页）

````text
Outline
Motivation
Why is anonymization hard
Differential privacy (DP)
Definition
Mechanism
Local DP vs global DP
DP variants and properties
Applications
39
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 40 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=40)

### 原始文字层

````text
Randomized response [Warner, 1965]
40
 Consider a survey of “Have you engaged X last week?”. The 
respondent is instructed to perform the following steps: 
 Flip a first coin
 If tails, then respond truthfully
 If heads, then flip a second coin and respond “Yes” if heads, and “No” if 
tails (i.e. random answer)
 Provide “plausible deniability” for the answer:
 A response of “Yes” may been offered because the first and second coins 
are both heads, which occurs with prob. ¼
 We achieve the privacy by the process of randomized response
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Randomized response [Warner, 1965]
  Consider a sur     vey of “Have you engaged X last week?”. The
   respondent   i s  i nst r    uct ed  t o  per for     m   t he  fol l ow i ng   st eps:
         Flip a fir st coin
         If tails, then respond tr  uthfully
         If heads, then flip a second coin and respond “Yes” if heads, and “No” if
          tails (i.e. random answer)
  Provide “plausible deniability” for the answer:
         A response of “Yes” may been offered because the fir st and second coins
          are both heads, whic  h occur s with prob. ¼
         We ac  hieve the pr ivac y by the process of randomized response
                                                                                               40
````

### 图片文字 OCR（en-US，待对照原页）

````text
Randomized response [Warner, 1965]
Consider a survey of "Have you engaged X last week?". The
respondent is instructed to perform the following steps:
Flip a
first coin
If tails, then respond truthfully
If heads, then flip a
second
coin and respond "Yes" if heads, and "No" if
tails (i.e. random answer)
Provide "plausible deniability" for the answer:
A response of "Yes" may been offered because the first and second coins
are both heads, which occurs with prob. 1 4
We achieve the privacy by the process of randomized response
40
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 41 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=41)

### 原始文字层

````text
Randomized response [Warner, 1965]
41
 Consider a survey of “Have you engaged X last week?”.The 
respondent is instructed to perform the following steps: 
 Flip a first coin
 If tails, then respond truthfully
 If heads, then flip a second coin and respond “Yes” if heads, and “No” if 
tails (i.e. random answer)
 Analysis:
 Pr[Res = Yes | Truth = Yes] = Pr[1st coin = tails] + Pr[1st coin = heads
& 2nd coin = heads] = ½ + ½ * ½ = ¾
 Pr[Res = Yes | Truth = No] = Pr[1st coin = heads & 2nd coin = heads] 
= ½ * ½ = ¼
 Pr[Res = No | Truth = No] = ¾ , Pr[Res = No | Truth = Yes] = ¼
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Randomized response [Warner, 1965]
  Consider a sur     vey of “Have you engaged X last week?”. The
   respondent   i s  i nst r    uct ed  t o  per for     m   t he  fol l ow i ng   st eps:
         Flip a fir st coin
         If tails, then respond tr  uthfully
         If heads, then flip a second coin and respond “Yes” if heads, and “No” if
          tails (i.e. random answer)
  Analysis:
         Pr[Res = Yes | Tr  uth = Yes] = Pr[1st coin = tails] + Pr[1st coin = heads
          & 2nd coin = heads] = ½ + ½ * ½ = ¾
         Pr[Res = Yes | Tr  uth = No] = Pr[1st coin = heads & 2nd coin = heads]
          = ½ * ½ = ¼
         Pr[Res = No | Tr  uth = No] = ¾ , Pr[Res = No | Tr  uth = Yes] = ¼
                                                                                               41
````

### 图片文字 OCR（en-US，待对照原页）

````text
Randomized response [Warner, 1965]
Consider a survey of "Have you engaged X last week?". The
respondent is instructed to perform the following steps:
Flip a
first coin
If tails, then respond truthfully
If heads, then flip a
second
coin and respond "Yes" if heads, and "No" if
tails (i.e. random answer)
Analysis:
Res = Yes Truth
& 2nd coin = heads]
Res = Yes Truth
Pr[
4
Res = No Truth
Pr[
Yes] = Pr[lst coin
= 1 2+12* 1
4
No
] = Pr[lst coin
34 , Pr[
Res -
tails] + Pr[lst coin — heads
heads & 2nd coin = heads]
No Truth = Yes]
4
41
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 42 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=42)

### 原始文字层

````text
Randomized response [Warner, 1965]
42
 Consider a survey of “Have you engaged X last week?”.The 
respondent is instructed to perform the following steps: 
 Flip a first coin
 If tails, then respond truthfully
 If heads, then flip a second coin and respond “Yes” if heads, and “No” if 
tails (i.e. random answer)
 Analysis:
output
DBs differ in 1
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Randomized response [Warner, 1965]
          Consider a sur     vey of “Have you engaged X last week?”. The
           respondent   i s  i nst r    uct ed  t o  per for     m   t he  fol l ow i ng   st eps:
                 Flip a fir st coin
                 If tails, then respond tr  uthfully
                 If heads, then flip a second coin and respond “Yes” if heads, and “No” if
                  tails (i.e. random answer)
          Analysis:
                                                                           DBs differ in 1
output
                                                                                                    42
````

### 图片文字 OCR（en-US，待对照原页）

````text
Randomized response [Warner, 1965]
Consider a survey of "Have you engaged X last week?". The
respondent is instructed to perform the following steps:
Flip a
first coin
If tails, then respond truthfully
If heads, then flip a
second
coin and respond "Yes" if heads, and "No" if
output
tails (i.e. random answer)
Analysis:
Pr[Response = Yes uth
P [Response = Ye Truth
3/4 P r [Response
1/4 P r [Response
Yes]
DBs differ in 1
NolTruth = No]
3.
NolTruth = Yes]
42
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 43 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=43)

### 原始文字层

````text
Randomized response [Warner, 1965]
43
 Consider a survey of “Have you engaged X last week?”.The 
respondent is instructed to perform the following steps: 
 Flip a first coin
 If tails, then respond truthfully
 If heads, then flip a second coin and respond “Yes” if heads, and “No” if 
tails (i.e. random answer)
 This mechanism is ln(3)-DP
 Specific:We respond truthfully with prob. ¾ and falsely with prob. ¼
 General: Respond truthfully with prob. !"#
$ and falsely with prob. !%#
$
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Randomized response [Warner, 1965]
  Consider a sur     vey of “Have you engaged X last week?”. The
   respondent   i s  i nst r    uct ed  t o  per for     m   t he  fol l ow i ng   st eps:
         Flip a fir st coin
         If tails, then respond tr  uthfully
         If heads, then flip a second coin and respond “Yes” if heads, and “No” if
          tails (i.e. random answer)
  This mec  hanism is ln(3)-DP
         Specific: We respond tr  uthfully with prob. ¾ and falsely with prob. ¼
         General: Respond tr  uthfully with prob. !"# and falsely with prob. !%#
                                                         $                              $
                                                                                               43
````

### 图片文字 OCR（en-US，待对照原页）

````text
Randomized response [Warner, 1965]
Consider a survey of "Have you engaged X last week?". The
respondent is instructed to perform the following steps:
Flip a
first coin
If tails, then respond truthfully
If heads, then flip a
second
coin and respond "Yes" if heads, and "No" if
tails (i.e. random answer)
This mechanism is In(3)-DP
Specific: We respond truthfully with prob. 3/4 and falsely with prob. 1 4
General:
Respond truthfully with prob. — and falsely with prob.
2
2
43
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 44 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=44)

### 原始文字层

````text
Randomized response [Warner, 1965]
44
 Randomized response:
 The truthful answer is x = {0, 1}
 The respondent answers truthfully (y = x) with prob. (1 + ε)/2 and falsely 
(y = 1 - x) with prob. (1 - ε)/2 
 Randomized response is 2ε-DP
 Pr [y = 0|x = 0] = (1 + ε)/2 ≈ eε
/2
 Pr [y = 0|x = 1] = (1 - ε)/2 ≈ e-ε
/2
 Pr [y = 0|x = 0] / Pr [y = 0|x = 1] ≈ e2ε
 Changing prob. to eε/(1 + eε) and 1/(1 + eε) yields ε-DP
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Randomized response [Warner, 1965]
 Randomized response:
       The tr  uthful answer is x = {0, 1}
       The respondent answer s tr  uthfully (y = x) with prob. (1 + ε)/2 and falsely
        (y = 1 - x) with prob. (1 - ε)/2
 Randomized response is 2ε-DP
       Pr [y = 0|x = 0] = (1 + ε)/2 ≈ eε/2
       Pr [y = 0|x = 1] = (1 - ε)/2 ≈ e-ε/2
       Pr [y = 0|x = 0] / Pr [y = 0|x = 1] ≈ e2ε
 Chang  ing prob. to eε/(1 + eε) and 1/(1 + eε) yields ε-DP
                                                                                   44
````

### 图片文字 OCR（en-US，待对照原页）

````text
Randomized response [Warner, 1965]
e Randomized response:
The truthful answer is x = {0, 1}
The respondent answers truthfully (y = x) with prob. (1 + E)/ 2 and falsely
(y = 1 - x) with prob.
Randomized response is 2E-DP
Pr [
- (1 + eE/2
Pr [
- (1 - E)/2 e-E/2
28
Pr [
01 / Pr [
and
yields
1/(1 + eE)
Changing prob. to
E-DP
44
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 45 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=45)

### 原始文字层

````text
Randomized response [Warner, 1965]
45
 Randomized response to estimate private mean:
 n individual answer a survey with one binary question
 The truthful answer for individual i is xi = {0, 1}
 Each individual answers truthfully (yi = xi
) with prob. (1 + ε)/2 and 
falsely (yi = 1 - xi
) with prob. (1 - ε)/2 
 Denote the mechanism by (y1, … , yn) = RRε(x1, … , xn)
 Estimate the mean:
 E[yi
] = xi (1 + ε)/2 + (1 – xi
)(1 - ε)/2 = xi ε + (1 - ε)/2
 ⇒	&
' ∑ %( = 
&
' ∑ &# ε	+ (1 - ε)/2
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Randomized response [Warner, 1965]
  Randomized response to estimate pr  ivate mean:
        n individual answer a sur   vey with one binary question
        The tr  uthful answer for individual i is xi = {0, 1}
        Eac  h individual answer s tr  uthfully (yi = xi) with prob. (1 + ε)/2 and
         falsely (yi = 1 - xi) with prob. (1 - ε)/2
        Denote the mec  hanism by    (y1, … , yn) = RRε(x1, … , xn)
  Estimate the mean:
        E[yi] = xi (1 + ε)/2 + (1 – xi)(1 - ε)/2 = xi ε + (1 - ε)/2
        ⇒	&   ∑ %   =   & ∑ &    ε	+ (1 - ε)/2
             '     (     '     #
                                                                                         45
````

### 图片文字 OCR（en-US，待对照原页）

````text
Randomized response [Warner, 1965]
Randomized response to estimate private mean:
n individual answer a survey with one binary question
The truthful answer for individual i is Xi = {0, 1}
Each individual answers truthfully (Yi = Xi) with prob. (1 + E)/ 2 and
falsely (Yi = 1 - Xi) with prob. (1 - E)/ 2
Denote the mechanism by (Yl,
Y ) = RRE(xl, ...
Estimate the mean:
E[Yil = (1 + E)/ 2 + (1 — - E)/ 2 = Xi E + (1 - E)/ 2
45
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 46 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=46)

### 原始文字层

````text
Randomized response [Warner, 1965]
46
 Randomized response to estimate private mean:
 n individual answer a survey with one binary question
 The truthful answer for individual i is xi = {0, 1}
 Each individual answers truthfully (yi = xi
) with prob. (1 + ε)/2 and 
falsely (yi = 1 - xi
) with prob. (1 - ε)/2 
 Denote the mechanism by (y1, … , yn) = RRε(x1, … , xn)
 Estimate the mean:

&
' ∑ %( = 
&
' ∑ &# ε	+ (1 - ε)/2
 Chernoff bound: &
') ∑ %( − &%)
*) − &
' ∑ &# ≤ * &
) ' w.h.p.
µ
Probability
distribution Tail probability
ε ε
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Randomized response [Warner, 1965]
  Randomized response to estimate pr  ivate mean:
          n individual answer a sur   vey with one binary question
          The tr  uthful answer for individual i is xi = {0, 1}
          Eac  h individual answer s tr  uthfully (yi = xi) with prob. (1 + ε)/2 and
           falsely (yi = 1 - xi) with prob. (1 - ε)/2
          Denote the mec  hanism by         (y1, … , yn) = RRε(x1, … , xn)
                                                                  Probability
                                                                 distribution                  Tail probability
  Estimate the mean:
          & ∑  %    =   & ∑   &    ε	+ (1 - ε)/2                               ε    µ    ε
           '      (      '       #
          Cher  noff bound:         &  ∑  %   −  &%)    −     & ∑  &      ≤  *      &     w.                        h                        .                        p.
                                    ')       (     *)          '      #            )  '
                                                                                                         46
````

### 图片文字 OCR（en-US，待对照原页）

````text
Randomized response [Warner,
Randomized response to estimate private mean:
n individual answer a survey with one binary question
The truthful answer for individual i is Xi = {0, 1}
1965]
Each individual answers truthfully (Yi = Xi) with prob. (1 + E)/ 2 and
falsely (Yi = 1 - Xi) with prob. (1 - E)/ 2
Denote the mechanism by (Yl,
y)
Estimate the mean:
1
I(n1EEYi-
12:)
Chernoff bound :
RRE(xl, ...
Probability
distribution
Tail probability
(n1EXi)I 0
(l
w•h.p.
46
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 47 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=47)

### 原始文字层

````text
Randomized response [Warner, 1965]
47
 Each individual releases their differentially private answer
 The curator aggregates and releases the mean estimate with 
low error
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Randomized response [Warner, 1965]
 Eac  h individual releases their differentially pr   ivate answer
 The curator agg  regates and releases the mean estimate with
  low er  ror
                                                                        47
````

### 图片文字 OCR（en-US，待对照原页）

````text
Randomized response [Warner, 1965]
Each individual releases their
differentially private
answer
The curator aggregates and releases the mean estimate with
low error
4
3
2
5
1
47
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 48 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=48)

### 原始文字层

````text
Laplace mechanism
48
 Laplace mechanism to estimate private mean:
 A trusted curator holds one bit xi = {0, 1} for each of n individuals
 The curator proceeds by
o Compute the mean µ	= (x1 + … + xn) / n
o Sampling noise Z ~ Lap(0, 1/εn)
o Release the noisy mean -, = µ + Z
 Denote the mechanism by -, = MLap(x1, … , xn)
 MLap is ε-DP
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Laplace mechanism
  Laplace mec  hanism to estimate pr  ivate mean:
        A tr  usted curator holds one bit xi = {0, 1} for eac  h of n individuals
        The curator proceeds by
             o Compute the mean µ	= (x1 + … + xn) / n
             o Sampling noise Z ~ Lap(0, 1/εn)
             o Release the noisy mean -,   =  µ + Z
        Denote the mec  hanism by -,  = MLap(x1, … , xn)
  MLap is ε-DP
                                                                                      48
````

### 图片文字 OCR（en-US，待对照原页）

````text
Laplace mechanism
e Laplace mechanism to estimate private mean:
trusted curator holds one bit Xi =
for each of n individuals
A
The curator proceeds by
Compute the mean g = (Xl + + xn) / n
O
Sampling noise Z Lap(O, 1 / En)
O
Release the noisy mean = g + Z
o
Denote the mechanism by = MLap(X1,
MLapis E-DP
48
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 49 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=49)

### 原始文字层

````text
Laplace distribution Lap(µ , b)
49
p(z) = exp(-|z - µ|/b)/2b
variance = 2b2
Increasing b flattens curve
https://en.wikipedia.org/wiki/Laplace_distribution
Abuse of notation:
Lap(b) = Lap(0, b)
b T 保护越强
准确率小
方差
d
默认M 0
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Laplace distribution Lap(µ , b)
                                                      b  T     保护越强
                                                              准确率⼩
                                                   p(z) = exp(-|z - µ|/b)/2b
                                             ⽅差var iance = 2b2
                                                   Increasing b flattens cur   ve
                                                   Abuse of notation:
                                                    Lap(b) = Lap(0, b)
                                                          d
                                                      默认M          0
    https://en.wikipedia.org/wiki/Laplace_distr ibution                    49
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
0 丐
0 ． 4
3
2
0 以
0
0
Laplace distribution Lap()1 ， b)
p=-5, b=4
p = 0 ， b=l
p=0, b=2
p=0, b=4
· 8 · 6 · 4 0 2
4
艿
6 8
p(z) = exp(- - 国 /b)/2b
2
variance =
lncreasing b flattens cur ve
Abuse of notation ：
Lap (b) = Lap()' b)
10
49
https ： / /Laplace
(listribution
````

### 图片文字 OCR（en-US，待对照原页）

````text
Laplace distribution Lap(g , b)
0.5
0.4
0.3
0.2
0.1
-10
-0,
-0,
-0,
-5,
4
P(z) —
exp(- I z - g I / b)/ 2b
variance = 2b2
Increasing b flattens curve
Abuse of notation:
Lap(b) = Lap(O, b)
10
49
https://en.wikipedia.org/wiki/Laplace
distribution
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 50 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=50)

### 原始文字层

````text
Laplace mechanism
50
 Laplace mechanism to estimate private mean:
 A trusted curator holds one bit xi = {0, 1} for each of n individuals
 The curator proceeds by
o Compute the mean µ	= (x1 + … + xn) / n
o Sampling noise Z ~ Lap(1/εn)
o Release the noisy mean -, = µ + Z
 Denote the mechanism by -, = MLap(x1, … , xn)
 MLap is ε-DP 
 Given two different databases D, D’ different from 1, then 
|µ D – µ D’| = 1/n
 Compute Pr[MLap(D) = a] / Pr[MLap(D’) = a] for any outcome a
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Laplace mechanism
  Laplace mec  hanism to estimate pr  ivate mean:
        A tr  usted curator holds one bit xi = {0, 1} for eac  h of n individuals
        The curator proceeds by
             o  Compute the mean µ	= (x1 + … + xn) / n
             o  Sampling noise Z ~ Lap(1/εn)
             o  Release the noisy mean -,    =  µ + Z
        Denote the mec  hanism by -,    = MLap(x1, … , xn)
  MLap is ε-DP
        Given two different databases D, D’ different from 1, then
         |µ D –	µ D’| = 1/n
        Compute Pr[MLap(D) = a] / Pr[MLap(D’) = a] for any outcome a
                                                                                          50
````

### 图片文字 OCR（en-US，待对照原页）

````text
Laplace mechanism
e Laplace mechanism to estimate private mean:
trusted curator holds one bit Xi =
for each of n individuals
A
The curator proceeds by
Compute the mean g = (Xl + + xn) / n
O
Sampling noise Z Lap(l / En)
O
Release the noisy mean = g + Z
o
Denote the mechanism by = MLap(X1,
MLapis E-DP
Given two different databases D, D' different from 1 , then
I PD¯PDI
Compute = a] / = a] for any outcome a
50
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 51 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=51)

### 原始文字层

````text
Laplace mechanism
51
 Laplace mechanism to estimate private mean:
 A trusted curator holds one bit xi = {0, 1} for each of n individuals
 The curator proceeds by
o Compute the mean µ	= (x1 + … + xn) / n
o Sampling noise Z ~ Lap(1/εn)
o Release the noisy mean -, = µ + Z
 Denote the mechanism by -, = MLap(x1, … , xn)
 MLap is ε-DP
Pr[2$ + 3 = 4]
Pr[2$′ + 3′
= 4]
=
Pr[3 = 4 − 2$]
Pr[3′
= 4 − 2+,]
=
exp(−;<|4 − 2$|) ∗ ;</2
exp(−;<|4 − 2+,|) ∗ ;</2
= exp ;< 4 − 2$′ − 4 − 2$ = exp ;< ∗
1
<
= e'
Lap(b) : p(z) = exp(-|z|/b)/2b
|µ	D – µ D’|=1/n
Z and $# are continuous variables
exp like
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Laplace mechanism
  Laplace mec   hanism to estimate pr   ivate mean:
        A tr  usted curator holds one bit xi = {0, 1} for eac  h of n individuals
        The curator proceeds by
             o Compute the mean µ	= (x1 + … + xn) / n
             o Sampling noise Z ~ Lap(1/εn)                       ex p     like
             o Release the noisy mean -,   =  µ + Z             Z and	$# are continuous var iables
        Denote the mec  hanism by -,   = MLap(x1, … , xn)
  MLap is ε-DP                                                Lap(b) : p(z) = exp(-|z|/b)/2b
       Pr[2$   + 3  =  4]  =   Pr[3   =  4 −  2$]   =  exp(−;<|4     −  2$|)  	∗	;</2
      Pr[2$′  +  3′  =  4]    Pr[3′  =  4  −  2+,]     exp(−;<|4     −  2+,|)  ∗ 	;</2
       =  exp   ;<   4  −  2    −   4 −  2      =  exp   ;<	  ∗ 1   =  e'
                            $′            $                     <
                                    |µ	 –	µ  |=1/n                                     51
                                       D    D’
````

### 图片文字 OCR（en-US，待对照原页）

````text
Laplace mechanism
e Laplace mechanism to estimate private mean:
trusted curator holds one bit Xi =
for each of n individuals
A
The curator proceeds by
Compute the mean g = (Xl + + xn) / n
O
Sampling noise Z Lap(l / En)
O
Release the noisy mean = g + Z
Z and are continuous variables
o
Denote the mechanism by = MLap(X1,
MLapis E-DP
Lap(b) : p(z) = exp(- I z / b)/ 2b
Pr[ßD + Z = a]
Pr[z = a -
exp(¯
enla — IIDI) * en/ 2
Pr[gm + Z' = a] ¯ Pr[Z' = a — VD,]
exp(
—enla — UD,I) * en/ 2
l)
— exp en
51
I g D PD'l=l/n
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 52 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=52)

### 原始文字层

````text
Laplace mechanism
52
 Laplace mechanism to estimate private mean:
 A trusted curator holds one bit xi = {0, 1} for each of n individuals
 The curator proceeds by
o Compute the mean µ	= (x1 + … + xn) / n
o Sampling noise Z ~ Lap(1/εn)
o Release the noisy mean -, = µ + Z
 Denote the mechanism by -, = MLap(x1, … , xn)
 MLap is ε-DP
 E [-,] = µ since E[Z] = 0
 Tail bound of Lap(1/εn): -, − - ≤ * &
)' w.h.p.
If Z~Lap(b) and t > 0, Pr [|Z|≥ t.b] ≤ exp(-t)
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Laplace mechanism
  Laplace mec  hanism to estimate pr  ivate mean:
          A tr  usted curator holds one bit xi = {0, 1} for eac  h of n individuals
          The curator proceeds by
               o   Compute the mean µ	= (x1 + … + xn) / n
               o   Sampling noise Z ~ Lap(1/εn)
               o   Release the noisy mean -,        =   µ + Z
          Denote the mec  hanism by -,         = MLap(x1, … , xn)
  MLap is ε-DP
          E [-, ] = µ since E[Z] = 0
          Tail bound of Lap(1/εn):          -, −  -   ≤   *     &    w.                        h                        .                        p.
                                                                )'
             If Z~Lap(b) and t > 0, Pr [|Z|≥ t.b] ≤ exp(-t)                                             52
````

### 图片文字 OCR（en-US，待对照原页）

````text
Laplace mechanism
e Laplace mechanism to estimate private mean:
trusted
curator holds one bit Xi = {0, 1} for each of n individuals
A
The curator proceeds by
Compute the mean g = (Xl + + xn) / n
O
Sampling noise Z Lap(l / En)
O
Release the noisy mean = g + Z
o
Denote the mechanism by = MLap(X1,
MLapis E-DP
E [Pl = g since E[Z] = O
Tail bound of Lap(l / En) :
If Z-Lap(b) and t > O, Pr [ Z | 2 t.b] exp(-t)
52
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 53 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=53)

### 原始文字层

````text
Other private computing
53
 Examples of private mean estimate in {0, 1}:
 What is the percentage of passed students in CS 752-2023?
 What is the average female survey taker? 
 Variants of private mean estimate in real-value:
 What is the average of grades of CS 752-2023?
 What is the average income of Auckland?
 Private counting/sum in real-value:
 What is the number of passed student in CS 752-2023?
 In total, how many Taylor Swift albums are bought by survey takers?
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Other private computing
      Examples of pr  ivate mean estimate in {0, 1}:
                     What is the percentage of passed students in CS 752-2023?
                     What is the average female sur   vey taker?
      Va                  r                      i                  a                  n                 t                  s                                     o                 f                                     p                 r                      i                  v               a                t                  e                                    m                  e                 a                  n                                    e                 s                  t                  i                  m                  a                t                  e                                    i                  n                  rea l-va l u e:
                     What is the average of g  rades of CS 752                                                            -2023?
                     What is the average income of Auc  kland?
      Pr  ivate counting/sum in rea l-va l u e:
                     What is the number of passed student in CS 752                                                                             -2023?
                     In total, how many Taylor Swift albums are bought by sur   vey taker s                                                                                                    ?
                                                                                                                                                                                                                  53
````

### 图片文字 OCR（en-US，待对照原页）

````text
Other private computing
e Examples of private mean estimate in {O, 1} :
What is the percentage of passed students in CS 752-2023?
What is the average female survey taker?
Variants of private mean estimate in real-value:
What is the average of grades of CS 752-2023?
What is the average income of Auckland?
Private counting/ sum in real-value:
What is the number of passed student in CS 752-2023?
In total, how many Taylor Swift albums are bought by survey takers?
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 54 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=54)

### 原始文字层

````text
Laplace mechanism
54
 Laplace mechanism to estimate private mean:
 A trusted curator holds one bit xi = {0, 1} for each of n individuals
 The curator proceeds by
o Compute the mean µ	= (x1 + … + xn) / n
o Sampling noise Z ~ Lap(1/εn)
o Release the noisy mean %$ = µ+ Z
 Denote the mechanism by %$ = MLap(x1, … , xn)
 MLap is ε-DP
Pr[*$ + , = -]
Pr[*$′ + ,′
= -]
=
Pr[, = - − *$]
Pr[,′
= - − *!"]
=
exp(−56|- − *$|) ∗ 56/2
exp(−56|- − *!"|) ∗ 56/2
= exp 56 - − *$′ − - − *$ = exp 56 ∗
1
6
= e'
Lap(b) : p(z) = exp(-|z|/b)/2b
Since|µ	D – µ D’|=1/n, Lap(1/εn) suffices
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Laplace mechanism
  Laplace mec  hanism to estimate pr  ivate mean:
        A tr  usted curator holds one bit xi = {0, 1} for eac h of n individuals
        The curator proceeds by
             o  Compute the mean µ	= (x1 + … + xn) / n
             o  Sampling noise Z ~ Lap(1/εn)
             o  Release the noisy mean %$  =  µ+ Z
        Denote the mec hanism by %$    = MLap(x1, … , xn)
  MLap is ε-DP                                                    Lap(b) : p(z) = exp(-|z|/b)/2b
       Pr[*$   + ,  =  -]  =   Pr[,  =  - −  *$]   =  ex p(−56|-    −  *$|) 	∗ 	56/2
       Pr[*$′ +  ,′  = -]     Pr[,′  =  - −  *!"]     ex p(−56|-    −  *!"|) ∗ 	56/2
         =  ex p  56   - −  *    −  -  −  *      =  ex p  56	 ∗ 1   =  e'
                             $′            $                    6
                    Since|µ	 –	µ  |=1/n, Lap( 1/εn) suffices                              54
                            D    D’
````

### 图片文字 OCR（en-US，待对照原页）

````text
Laplace mechanism
Laplace mechanism to estimate private mean:
trusted curator holds one bit Xi =
for each of n individuals
A
The curator proceeds by
Compute the mean g = (Xl + + xn) / n
O
Sampling noise
Z Lap(1/En)
O
Release the noisy mean = g + Z
O
Denote the mechanism by = MLap(x1, , n
x)
MLapis E-DP
Pr[ßD + Z = a]
Pr[z = a - VD]
Pr[gw + Z' = a] ¯ Pr[Z' = a — VD,]
1
— — la —
¯ exp € 71 *
= 1 / n, Lap(l / En) suffices
Since D I-ID' I
Lap(b) : p(z) = exp(- I Z I / b)/ 2b
— VDI) * en/ 2
— VD,I) * en/ 2
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 55 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=55)

### 原始文字层

````text
Laplace mechanism
55
 Intuition: f(x) can be released accurately when f is insensitive to 
individual entries x1, … , xn∈	R
 Global sensitivity GSf = maxneighbors D,D’ f(D) – f(D’) 1
 Example: GSaverage = 1/n for sets of bits
 Theorem: f(x) + Lap(GSf / e) is e-DP
 Noise generated from Laplace distribution
Tell me f(D)
f(D)+noise
x1
…
xn
Database
Lipschitz
constant of f
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Laplace mechanism
                                                                     Database
                              Tell me f(D)                                x
                                                                          …1
                               f(D)+noise                                 xn
  Intuition: f(x) can be released accurately when f is insensitive to
   individual entr  ies x1, … , xn ∈	R
  Global sensitivity GSf = maxneighbors D,   D   ’       f(D) – f(D’)       1
        Example: GSav e   r   a  g   e = 1/n  for sets of bits           Lipschitz
  Theorem: f(x) + Lap(GSf / e) is e-DP                                   constant of f
        Noise generated from Laplace distr ibution
                                                                                        55
````

### 图片文字 OCR（en-US，待对照原页）

````text
Laplace mechanism
Tell me f(D)
Database
xn
f(x) can be released accurately when fis
Intuition:
insensitive to
individual entries Xl, , xn e R
Ilf(D) -
Global sensitivity GSf = maxneighbors D,D'
Example: GS
= 1/ n for sets of bits
average
Theorem: f(x) + Lap(GSf / E) is E-DP
Noise generated from Laplace distribution
Lipschitz
constant of f
55
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 56 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=56)

### 原始文字层

````text
Laplace mechanism
56
 Private mean/sum estimate in real-value:
 What is the average of grades of CS 752-2023?
o GS = 10/200 (if scale = 10 and #students = 200)
 What is the number of passed student in CS 752-2023?
o GS = 1
 What is the total yearly income of Auckland?
o GS = 560,000 (i.e. the max personal income in Auckland)
 In total, how many Taylor Swift albums are bought by survey takers?
o GS = 11 (Taylor has 11 released albums)
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Laplace mechanism
  Pr  ivate mean/sum estimate in rea l-va l u e:
         What is the average of g  rades of CS 752    -2023?
              o  GS = 10/200 (if scale = 10 and #students = 200)
         What is the number of passed student in CS 752-2023?
              o  GS = 1
         What is the total yearly income of Auc  kland?
              o  GS = 560,000 (i.e. the max per sonal income in Auc  kland)
         In total, how many Taylor Swift albums are bought by sur   vey taker s     ?
              o  GS = 11 (Taylor has 11 released albums)
                                                                                             56
````

### 图片文字 OCR（en-US，待对照原页）

````text
Laplace mechanism
e Private mean/ sum estimate in real-value:
What is the average of grades of CS 752-2023?
— 10 and #students = 200)
GS = 10/200 (if scale
O
What is the number of passed student in CS 752-2023?
GS = 1
o
What is the total yearly income of Auckland?
GS = 560,000 (i.e. the max personal income in Auckland)
O
In total, how many Taylor Swift albums are bought by survey takers?
GS = 11 (Taylor has 1 1 released albums)
O
56
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 57 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=57)

### 原始文字层

````text
Laplace mechanism
57
 Global sensitivity: GSf = Δf = maxneighbors D,D’ f(D) – f(D’) 1
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Laplace mechanism
 Global sensitivity: GSf = Δf = maxneighbors D,  D  ’ f(D) – f(D’)1
                                                                             57
````

### 图片文字 OCR（en-US，待对照原页）

````text
Laplace mechanism
, Ilf(D) -
Global sensitivity:
GS = Af = maxneighbors
0
-4b
-2b
-b
b
2b
3b
4b
Noise depends on f and e, not on the database
Smaller sensitivity (Af) means less distortion
5b
57
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 58 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=58)

### 原始文字层

````text
Output perturbation mechanism
58
 Global sensitivity:
 For any function f: X → Rd, define Δf = maxneighbors D,D’ F
F
f(D) –
f(D’) (
 The Laplace mechanism is an example of a general class of 
mechanisms where f = (x1 + … + xn)/n and xi is a real
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Output per     turbation mechanism
 Global sensitivity:
       For any function f: X → Rd, define Δf = maxneighbors D,  D  ’ Ff(D) –
         f(D’)F(
 The Laplace mec  hanism is an example of a general class of
  mec  hanisms where f = (x1 + … + xn)/n and xi is a real
                                                                             58
````

### 图片文字 OCR（en-US，待对照原页）

````text
Output perturbation mechanism
Global sensitivity:
Ilf(D) -
For any function f: X -4 Rd define Af = maxneighbors D,D'
The Laplace mechanism is an example of a general class of
mechanisms where f = (Xl + + xn)/ n and Xi is a real
58
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 59 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=59)

### 原始文字层

````text
Output perturbation mechanism
59
 Global sensitivity:
 For any function f: X → Rd, define Δf = maxneighbors D,D’ F
F
f(D) –
f(D’) (
 Output perturbation Mf,Lap(x1, … , xn):
 A trusted curator holds one vector xi ∈ Rd for each of n individuals
 The curator proceeds by
o Compute the function f(x1 , … , xn) of the data
o Sampling a noise vector Z ~ Lap(Δf	/ε)d
o Release the noisy vector f(x1 , … , xn)+ Z
 Mf,Lap(x1, … , xn) is e-DP
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Output per     turbation mechanism
  Global sensitivity:
        For any function f: X → Rd, define Δf = maxneighbors D,  D  ’ Ff(D) –
          f(D’)F(
  Output per    turbation Mf,Lap(x1, … , xn):
        A tr  usted curator holds one vector xi ∈ Rd for eac  h of n individuals
        The curator proceeds by
             o  Compute the function f(x1 , … , xn) of the data
             o  Sampling a noise vector Z ~ Lap(Δf	/ε)d
             o  Release the noisy ve  c  t  o r  f(x1 , … , xn)+ Z
  Mf,Lap(x1, … , xn) is e-DP
                                                                                          59
````

### 图片文字 OCR（en-US，待对照原页）

````text
Output perturbation mechanism
Global sensitivity:
, Ilf(D) -
For any function f: X -4 Rd, define Af = max
neighbors D,D
Output perturbation .
curator holds one vector Xi E Rd for each of n individuals
trusted
A
The curator proceeds by
Compute the function f(X1 , ... , xn) of the data
o
Sampling a noise vector Z Lap(Af / E) d
O
Release the noisy vector f(X1 , ...
o
, xn) is e-DP
59
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 60 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=60)

### 原始文字层

````text
Differential Privacy: Summary
 M gives e-differential privacy if for all values of DB and Me
and all responses R:
slide 60
Pr [R]
Pr[ M (DB) = R]
Pr[ M (DB + Me) = R]
≤ %H 1 - e » % » 1 + e IH ≤
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Dif    ferential Privacy: Summar    y
      M gives e-differential pr   ivac  y if for all va l u e s    o f  DB and Me
       and all responses R:
           IH              Pr[ M (DB) = R]                        H
1 - e » %      ≤      Pr[ M (DB + Me) = R]                   ≤ %    » 1 + e
    Pr [R]
                                                                            slide 60
````

### 图片文字 OCR（en-US，待对照原页）

````text
Differential Privacy: Summary
ives e-differential privacy
if for
all
values of DB and Me
and all responses R:
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 61 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=61)

### 原始文字层

````text
Promise of DP
 No perceptible risk is incurred by joining DB
 Anything adversary can do to me, it could do without me
Bad Responses: R R R
Pr [response]
slide 61
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Promise of DP
         No perceptible r  isk is incur  red by joining DB
         Anything adver  sar y can do to me, it could do without me
       Pr [response]
Bad Responses:         R              R                   R
                                                                                     slide 61
````

### 图片文字 OCR（en-US，待对照原页）

````text
Promise of DP
No perceptible risk is incurred by joining DB
Anything adversary can do to me, it could do without me
Pr [response]
Bad Responses:
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 62 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=62)

### 原始文字层

````text
Outline
62
 Motivation
 Why is anonymization hard
 Differential privacy (DP)
 Definition
 Mechanism
 Local DP vs global DP
 DP variants and properties
 Applications
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Outline
  Motivation
  Why is anonymization hard
  Differential pr  ivac y (DP)
        Definition
        Mec  hanism
        Local DP vs global DP
        DP var iants and proper   ties
  Applications
                                                                                    62
````

### 图片文字 OCR（en-US，待对照原页）

````text
Outline
Motivation
Why is anonymization hard
Differential privacy (DP)
Definition
Mechanism
Local DP vs global DP
DP variants and properties
Applications
62
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 63 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=63)

### 原始文字层

````text
Randomized response vs Laplace
63
 Randomized response to estimate private mean:
 Given the truthful answer for individual i is xi = {0, 1}, and µ	= 
&
' ∑ &#
 Individual i answers truthfully (yi = xi
) with prob. (1 + ε)/2 and falsely 
(yi = 1 - xi
) with prob. (1 - ε)/2 
 Release an unbiased estimate -,) = 
&
') ∑ %( − &%)
*)
 -,) − - ≤ * &
) '
 Laplace mechanism to estimate private mean:
 A trusted curator holds one bit xi = {0, 1} for each of n individuals
 The curator compute the mean µ
 Release an unbiased estimate -,* = µ + Z where Z ~ Lap(1/εn)
 -,* − - ≤ * &
)'
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Randomized response vs Laplace
  Randomized response to estimate pr  ivate mean:
        Given the tr  uthful answer for individual i is x = {0, 1}, and µ	= &   ∑ &
                                                          i                    '     #
        Individual i answer s tr  uthfully (yi = xi) with prob. (1 + ε)/2 and falsely
         (yi = 1 - xi) with prob. (1 - ε)/2
        Release an unbiased estimate    -,  =  & ∑  %  −  &%)
                                          )    ')     (     *)
         -,  −  -  	≤  *     &
            )               )  '
  Laplace mec  hanism to estimate pr  ivate mean:
        A tr  usted curator holds one bit xi = {0, 1} for eac  h of n individuals
        The curator compute the mean µ
        Release an unbiased estimate -,  * =  µ + Z where Z ~ Lap(1/εn)
         -,  −  -  ≤  *    &
            *              )'                                                           63
````

### 图片文字 OCR（en-US，待对照原页）

````text
Randomized response vs Laplace
Randomized response to estimate private mean:
Given the truthful answer for individual i is Xi = {O, 1}, and g = —E Xi
Individual i answers truthfully (Yi = Xi) with prob. (1 + E)/ 2 and falsely
(Yi = 1 - Xi) with prob. (1 - E)/ 2
1
I—E
Release an unbiased estimate
Laplace mechanism to estimate private mean:
trusted curator holds one bit Xi =
for each of n individuals
The curator compute the mean g
Release an unbiased estimate = g + Z where Z Lap(l / En)
63
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 64 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=64)

### 原始文字层

````text
Randomized response vs Laplace
64
 Randomized response achieves local DP:
 Each individual releases a noisy answer
 No trusted curator with access to the raw data
 -,) − - ≤ * &
) '
 Laplace mechanism achieves global/centralized DP:
 A trusted curator holds one bit xi = {0, 1} for each of n individuals
 Need a trusted central aggregator with access to the raw data
 -,* − - ≤ * &
)'
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Randomized response vs Laplace
  Randomized response ac  hieves local DP:
        Eac  h individual releases a noisy answer
        No tr  usted curator with access to the raw data
         -,  − -   	≤  *    &
            )               ) '
  Laplace mec  hanism ac  hieves global/centralized DP:
        A tr  usted curator holds one bit xi = {0, 1} for eac  h of n individuals
        Need a tr  usted central agg  regator with access to the raw data
         -, −  -   ≤  *   &
            *              )'
                                                                                      64
````

### 图片文字 OCR（en-US，待对照原页）

````text
Randomized response vs Laplace
Randomized response achieves local DP:
Each individual releases a noisy
answer
No trusted curator with access to the raw data
Elfi)
Laplace mechanism achieves global/ centralized DP:
trusted curator holds one bit Xi =
for each of n individuals
A
Need a trusted central aggregator with access to the raw data
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 65 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=65)

### 原始文字层

````text
Local vs global DP
65
https://research.aimultiple.com/
differential-privacy/
````

### 图片文字 OCR（en-US，待对照原页）

````text
Local vs global DP
Untrusted
Aggregator
noise
O
(Bob)
private
data
noise
raw data
Data generators
(people)
Local privacy
noise
O
O
raw
answer
Trusted
Curator
(Alice)
raw data
O
O
Data generators
(people)
private
answer
noise
query
Untrusted
Querier
(Bob)
https://research.aimultiple.com/
differential-privacy /
65
Global privacy
````

### 图表辅助说明

左右比较：local DP 在用户端先加噪，再把处理后的数据送给不受信任的 aggregator；global DP 由受信任 curator 接收原始数据，在回答查询时加噪，再把隐私化答案返回外部查询者。绿色虚线边界标出信任范围。

## PDF 第 66 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=66)

### 原始文字层

````text
Outline
66
 Motivation
 Why is anonymization hard
 Differential privacy (DP)
 Definition
 Mechanism
 Local DP vs global DP
 DP variants and properties
 Applications
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Outline
  Motivation
  Why is anonymization hard
  Differential pr  ivac y (DP)
        Definition
        Mec  hanism
        Local DP vs global DP
        DP var iants and proper   ties
  Applications
                                                                                    66
````

### 图片文字 OCR（en-US，待对照原页）

````text
Outline
Motivation
Why is anonymization hard
Differential privacy (DP)
Definition
Mechanism
Local DP vs global DP
DP variants and properties
Applications
66
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 67 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=67)

### 原始文字层

````text
(ε,	δ)-differential privacy
67
 X: The data universe
 D ⊂	X: The data set (one element per person)
 Privacy parameters: ε	≥	0,	0	≤	δ	≤	1
 δ	accounts for “bad events” that might result in high privacy loss
Definition: An algorithm M is ε-differentially private if for all
pairs of neighboring datasets D, D’, and for all outputs R:
 Pr [M(D) = R] ≤ eε Pr [M(D’) = R] + δ
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
(ε,	δ)-dif    ferential privacy
     X: T     h     e            d     a    t      a            u     n     i      v   e     r         s     e
     D ⊂	X: T     h     e            d     a    t      a            s     e     t             (     o     n     e            e     l     e     m      e     n     t             p     e     r             p     e     r         s     o     n     )
     Pr   ivac  y parameter   s:                    ε  	≥	0,	0	≤	δ	≤	1
Definition: An algor  ithm M is ε-differentially pr  ivate if for all
pair  s of neighbor  ing datasets D,       D      ’,       a       n       d              f      o       r        all outputs R:
            Pr [M(D) = R] ≤ eε Pr [M(D’) = R] + δ
     δ	accounts for “bad events” that might result in high pr  ivac y loss
                                                                                                                                                     67
````

### 图片文字 OCR（en-US，待对照原页）

````text
(E, ö)-differential privacy
X: The data universe
D C X: The data set (one element per person)
E 2 0, osö<l
Privacy parameters:
An algorithm M is E-differentially private if for all
Definition:
pairs of neighboring datasets D, II, and for all outputs R:
accounts for "bad events" that might result in high privacy loss
67
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 68 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=68)

### 原始文字层

````text
(ε,	δ)-differential privacy
68
 Random sampling M(x1, …, xn) = xUnif([n]) is (0, 1/n)-DP
 Consider D’ = D & me
 Pr [sample xme from D] = 0 and Pr [sample xme from D’] = 1/n
 Pr [sample xme from D’] ≤ Pr [sample xme from D] + 1/n
 ⇒	We should take δ	≪	1/n
Bad Responses: R R R
Pr [response]
δ
e0
, ε	=	0
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
(ε,	δ)-dif    ferential privacy
     Random sampling M(x1, …, xn) = xUnif([n]) is (0, 1/n)-DP
           Consider D’ = D & me
           Pr [sample xme from D] = 0 and Pr [sample xme from D’] = 1/n
           Pr [sample xme from D’]  ≤  Pr [sample xme from D] + 1/n
           ⇒	We should take δ	≪	1/n
                                                      e0, ε	=	0
       Pr [response]
                                                                                  δ
Bad Responses:          R              R                    R
                                                                                     68
````

### 图片文字 OCR（en-US，待对照原页）

````text
(E, ö)-differential privacy
Random sampling M(XI,
is (0, 1/n)-DP
Consider D' = D & me
Pr [sample x me from D] = O and Pr [sample x me from D'] = 1/ n
Pr [sample x me from D'I Pr [sample x me from Dl + 1/ n
We should take 1 / n
Pr [response]
Bad Responses:
68
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 69 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=69)

### 原始文字层

````text
Fundamental properties
69
 Robustness to post-processing:
 If M is (ε,	δ)-DP then F o M is (ε,	δ)-DP
 Composition:
 If Mj is (εj	
,	δj
)-DP for j = 1, … , k then for a vector x, the combination 
mechanism M = (M1(x), …, Mj
(x)) is ∑- M- , ∑- N- -DP. In the 
homogeneous case, this yields (k	ε	
,	k	δ)-DP.
 This holds against active attacker (i.e. each query depends on the previous 
queries’ result)
 Group privacy:
 If M is (ε,	δ)-DP w.r.t D ≃	1 D’, then M is (t	ε,	t	etε	δ)-DP w.r.t D ≃	t D’
(i.e. t changes)
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Fundamental proper     ties
  Robustness to post-processing:
         If M is (ε,	δ)-DP then F o M is (ε,	δ)-DP
  Composition:
         If Mj is (εj	,	δj)-DP for j = 1, … , k then for a vector x, the combination
          mec  hanism M = (M1(x), …, Mj(x)) is           ∑-  M- ,∑-  N-  -DP. In the
          homogeneous case, this yields (k	ε	,	k	δ)-DP.
         This holds against active attac  ker (i.e. eac  h query depends on the previous
          quer ies’ result)
  Group pr   ivac  y:
         If M is (ε,	δ)-DP w.r.t D ≃	1 D’, then M is (t	ε,	t	etε	δ)-DP w.r.t D ≃	t D’
          (i.e. t changes)
                                                                                               69
````

### 图片文字 OCR（en-US，待对照原页）

````text
Fundamental properties
Robustness to post-processing:
If M is (E, ö)-DP then F o M is (E, ö)-DP
Composition:
If Mj is (Ej, (SD-DP forj = 1,
k then for a vector x, the combination
mechanism
-DP. In the
(MI Mj(x)) is
homogeneous case, this yields
This holds against active attacker (i.e. each query depends on the previous
queries' result)
Group privacy:
If M is (E, ö)-DP w.r.t D I D', then M is (t E, t ö)-DP w.r.t D t D'
(i.e. t changes)
69
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 70 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=70)

### 原始文字层

````text
Outline
70
 Motivation
 Why is anonymization hard
 Differential privacy
 Applications
 RAPPOR
 Private empirical risk minimization
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Outline
 Motivation
 Why is anonymization hard
 Differential pr  ivac y
 Applications
       RAPPOR
       Pr ivate empir ical r isk minimization
                                                                                 70
````

### 图片文字 OCR（en-US，待对照原页）

````text
Outline
Motivation
Why is anonymization hard
Differential privacy
Applications
RAPPOR
Private empirical risk minimization
70
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 71 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=71)

### 原始文字层

````text
Applications in big tech companies
71
 In Apple iOS and MacOS, collect typing statistics
 To replace text by an icon w.r.t semantics
 To recommend the relevant text
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Applications in big tech companies
  In Apple iOS and MacOS,       c     o     l     l     e     c     t       typing statistics
         To replace text by an icon w.r.t semantics
         To recommend the relevant text
                                                                                            71
````

### 图片文字 OCR（en-US，待对照原页）

````text
Applications in big tech companies
In Apple iOS and MacOS, collect typing statistics
To replace text by an icon w.r.t semantics
To recommend the relevant text
oaøoaao
aoooooa
ooaoo
Differential privacy
71
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 72 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=72)

### 原始文字层

````text
In Google Chrome browser, to collect browsing statistics
 To estimate the popularity of Yahoo! Search, Bing, … 
 To know the most Chrome homepage URL
Applications in big tech companies
72
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Applications in big tech companies
  In Google Chrome browser,       t      o            c     o     l     l     e     c     t       browsing statistics
         To estimate the popular ity of  Yahoo! Searc  h, Bing, …
         To know the most Chrome homepage URL
                                                                                                  72
````

### 图片文字 OCR（en-US，待对照原页）

````text
Applications in big tech companies
In Google Chrome browser,
to collect
browsing statistics
To estimate the popularity of Yahoo! Search, Bing, ...
To know the most Chrome homepage URL
Estimated proportions
"google.com" "msn.comn
avg.com• "google.com.tr" "ask.com"
Dec 1
Jan I
1/97
Feb 1
google
msn
avg
google tr
google br
72
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 73 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=73)

### 原始文字层

````text
Applications in big tech companies
73
 In Microsoft Windows to collect telemetry data over time
 From Snap to perform modeling of user preference
 All deployments are based on RR, but extend it substantially
 To deal with over 100 million users each
 To handle the large space of possible values a user might have
 Local Differential Privacy is state of the art in 2018
 Randomized response invented in 1965: five decades ago!
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Applications in big tech companies
 In Microsoft Windows to collect telemetr y data over time
 From Snap to perfor   m modeling of user preference
 All deployments are based on RR, but extend it substantially
       To deal with over 100 million user s eac  h
       To handle the large space of possible values a user might have
 Local Differential Pr  ivac y is state of the ar    t in 2018
       Randomized response invented in 1965: five decades ago!
                                                                                  73
````

### 图片文字 OCR（en-US，待对照原页）

````text
Applications in big tech companies
In Microsoft Windows
to collect telemetry data over time
Snap to perform modeling of user preference
From
All deployments are based on RR, but extend it substantially
To deal with over 100 million users each
To handle the large space of possible values a user might have
Local Differential Privacy is state of the art in 2018
Randomized response invented in 1965: five decades ago!
73
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 74 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=74)

### 原始文字层

````text
Recap of Randomized Response
74
 Each user has a single bit of private information
 Encoding e.g. political/sexual/religious preference, illness, etc.
 Randomize Response: toss an unbiased coin [Warner 65]
 If Heads (probability p = ½), report the true answer
 Else, toss unbiased coin again: if Heads, report true answer, else lie
 Collect responses from n users, subtract noise
 Error in the estimate is proportional to R/ S
 Simple LDP algorithm with parameter ε = ln((¾)/(¼)) = ln(3)
 Generalization: allow biased coins (p ≠ ½)
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Recap of Randomized Response
  Eac  h user has a single bit of pr   ivate infor    mation
        Encoding e.g. political/sexual/relig  ious preference, illness, etc.
  Randomize Response: toss an unbiased coin [War   ner 65]
        If Heads (probability p = ½), repor   t the tr  ue answer
        Else, toss unbiased coin again: if Heads, repor   t tr  ue answer, else lie
  Collect responses from n user   s, subtract noise
        Er ror in the estimate is propor   tional to R/   S
        Simple LDP algor ithm with parameter ε = ln((¾)/(¼)) = ln(3)
        Generalization: allow biased coins     (p ≠ ½)
                                                                                           74
````

### 图片文字 OCR（en-US，待对照原页）

````text
Recap of Randomized Response
Each user has a
single bit of private information
Encoding e.g. political/ sexual/ religious preference, illness, etc.
Randomize Response: toss an unbiased coin [Warner 65]
If Heads
(probability
report the
true answer
Else, toss unbiased coin again: if
Heads
else lie
report true answer,
Collect responses from n users, subtract noise
Error in the estimate is proportional to
Simple LDP algorithm with parameter
Generalization: allow biased coins
(p 1/2)
In(3)
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 75 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=75)

### 原始文字层

````text
RAPPOR
75
 Deployed in Google Chrome to collect browsing statistics
 Use case:We want to know the most popular homepage
 Each user has a 1 chrome homepage, e.g. google.com, yahoo.com, …
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
RAPPOR
                  Deployed in Google Chrome to collect browsing statistics
                  Use case: We                                                    w                        a                          n                          t                                                     t                          o                                                     k                          n                          o                  w                                                     t                          h                          e                                                    m                           o                          s                          t                                                     p                          o                          p                          u                          l                          a                          r                                                      h                          o                          m                           e                         p                          a                          g                          e
                                                         Eac    h user has a 1 c    hrome homepage, e.g. google.com, yahoo.com, …
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             75
````

### 图片文字 OCR（en-US，待对照原页）

````text
RAPPOR
Deployed in Google Chrome to collect browsing statistics
We want to know the most popular homepage
use case:
Each user has a 1 chrome homepage, e.g. google.com, yahoo.com, ...
Estimated proportions
"google.com" "msn.com"
avg.com" "google.com.br"
"ask.com"
Dec 1
Jan 1
1/97
google
msn
avg
google tr
google br
75
Feb 1
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 76 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=76)

### 原始文字层

````text
RAPPOR
76
 First attempt:
 Present all possible homepages (domain size) as a binary vector
 A user has a sparse binary vector with one 1
 Apply RR on every bit of the user vector
0 0 0 1 0 0 0 0
google.com
0 0 0 0
0/1 0/1 0/1 1/0 0/1 0/1 0/1 0/1 0/1 0/1 0/1 0/1
RR
Original
Privatized
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
RAPPOR
          Fir   st attempt:
                 Present all possible homepages (domain size) as a binary vector
                 A user has a spar se binary vector with one 1
                 Apply RR on every bit of the user vector
                google.com
Or ig inal     0      0      0     1      0     0      0      0     0      0      0     0
                                                       RR
Pr ivatized   0/1    0/1   0/1    1/0   0/1    0/1    0/1   0/1    0/1    0/1   0/1    0/1
                                                                                                       76
````

### 图片文字 OCR（en-US，待对照原页）

````text
RAPPOR
e First attempt:
Present all possible homepages (domain size) as a binary vector
A user has a sparse binary vector with one 1
Apply RR on every bit of the user vector
google.com
Original
Privatized
0
0/1
0
0/1
0
0/1
1
0
0
0
0
0
0/1
0
1/0
0/1
0/1 0/1 0/1
0
0/1
0
0/1
76
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 77 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=77)

### 原始文字层

````text
RAPPOR
77
 Limitations:
 Slow: Have to send each bit 1 of the privatized vector
 Threat: Average of repeated privatized vectors eventually reveals the answer
0 0 0 1 0 0 0 0
google.com
0 0 0 0
0/1 0/1 0/1 1/0 0/1 0/1 0/1 0/1 0/1 0/1 0/1 0/1
RR
Original
Privatized
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
RAPPOR
          Limitations:
                 Slow: Have to send eac  h bit 1 of the pr ivatized vector
                 Threat: Average of repeated pr ivatized vector s eventually reveals the answer
                google.com
Or ig inal      0     0      0      1     0      0     0      0      0     0      0      0
                                                       RR
Pr ivatized   0/1    0/1    0/1   1/0   0/1    0/1    0/1    0/1   0/1    0/1    0/1   0/1
                                                                                                       77
````

### 图片文字 OCR（en-US，待对照原页）

````text
RAPPOR
e Limitations:
Slow:
Have to send each bit 1 of the privatized vector
Threat:
Average of repeated privatized vectors eventually reveals the answer
google.com
Original
Privatized
0
0/1
0
0/1
0
0/1
1
0
0
0
0
0
0/1
0
1/0
0/1
0/1 0/1 0/1
0
0/1
0
0/1
77
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 78 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=78)

### 原始文字层

````text
RAPPOR
78
 Limitations:
 Slow: Have to send each bit 1 of the privatized vector
 Threat: Average of repeated privatized vectors eventually reveals the answer
 Fix:
 Fast: Reduce the domain size through hashing
 Privacy: Memoize the RR-based privatized vector to reuse later, and apply a 
“random” flipping (e.g. 0 →	1 with prob. 1/2 , 1 →	0 with prob. 1/4) on 
the privatized vector and report it
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
RAPPOR
  Limitations:
          Slow: Have to send eac  h bit 1 of the pr ivatized vector
          Threat: Average of repeated pr ivatized vector s eventually reveals the answer
  Fix:
          Fa  s  t   : Reduce the domain size through hashing
          Pr  ivac y: Memoize the RR-based pr ivatized vector to reuse later, and apply a
           “random” flipping (e.g. 0 →	1 with prob. 1/2 , 1 →	0 with prob. 1/4) on
           the pr ivatized vector and repor   t it
                                                                                                       78
````

### 图片文字 OCR（en-US，待对照原页）

````text
RAPPOR
e Limitations:
Slow:
Have to send each bit 1 of the privatized vector
Threat:
Average of repeated privatized vectors eventually reveals the answer
e Fix:
Reduce the domain size through hashing
Fast:
Privacy: Memoize the RR-based privatized vector to reuse later, and apply a
"random" flipping (e.g. O -4 | with prob. 1/2 , 1 O with prob. 1/4) on
the privatized vector and report it
78
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 79 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=79)

### 原始文字层

````text
RAPPOR: 2-level randomization
79
 RAPPOR: Use a Bloom filter to reduce the domain size
 Consider the URL as an integer (e.g. index of 1 in the binary vector)
 Use k hash function to construct a Bloom filter B
 Apply RR on each bit of the Bloom filter to have a privatized B’
 Store the privatized Bloom filter B’ to reuse later
k=4
Store Changed Unchanged
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
RAPPOR: 2-level randomization
        RAPPOR: Use a Bloom filter to reduce the domain size
              Consider the URL as an integer (e.g. index of 1 in the binary vector)
              Use k hash function to constr  uct a Bloom filter B
              Apply RR on eac  h bit of the Bloom filter to have a pr ivatized B’
              Store the pr ivatized Bloom filter B’ to reuse later
                                                                           k=4
Store                                                         Changed         Unc hanged     79
````

### 图片文字 OCR（en-US，待对照原页）

````text
RAPPOR: 2-level randomization
e RAPP OR: use a Bloom filter to reduce the domain size
Consider the URL as an integer (e.g. index of 1 in the binary vector)
use k hash function to construct a Bloom filter B
Apply RR on each bit of the Bloom filter to have a privatized B'
Store the privatized Bloom filter B' to reuse later
Participant 8456 in cohort 1
True value:
Bloom filter (B):
Fake Bloom
filter (B'):
Store
"The number 68"
Changed
k=4
4 signal bits
69 bits on
Unchanged
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 80 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=80)

### 原始文字层

````text
RAPPOR: 2-level randomization
80
 RAPPOR: Apply 2-level randomization on a Bloom filter
 Consider the URL as an integer (e.g. index of 1 in the binary vector)
 Use k hash function to construct a Bloom filter B
 Apply RR on each bit of the Bloom filter to have a privatized B’
 Apply random flipping on each bit of B’ and send it
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
RAPPOR: 2-level randomization
  RAPPOR: Apply 2-level randomization on a Bloom filter
        Consider the URL as an integer (e.g. index of 1 in the binary vector)
        Use k hash function to constr  uct a Bloom filter B
        Apply RR on eac  h bit of the Bloom filter to have a pr ivatized B’
        Apply random flipping on eac  h bit of B’ and send it
                                                                                       80
````

### 图片文字 OCR（en-US，待对照原页）

````text
RAPPOR: 2-level randomization
e RAPP OR: Apply 2 -level randomization on a Bloom filter
Consider the URL as an integer (e.g. index of 1 in the binary vector)
use k hash function to construct a Bloom filter B
Apply RR on each bit of the Bloom filter to have a privatized B'
Apply random flipping
on each bit of B' and send it
Participant 8456 in cohort 1
True value:
Bloom filter (B):
Fake Bloom
filter (B'):
Report sent
to server:
"The number 68"
I III
II I II I III I I III I I III II I I I I III III III III I III II II III II II I II I II I I
32
64
III
128
4 signal bits
69 bits on
145 bits on
256
Bloom filter bits
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 81 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=81)

### 原始文字层

````text
RAPPOR: 2-level randomization
81
 RAPPOR: Apply 2-level randomization on a Bloom filter
 Storing a privatized B’ to prevent that average of B’ reveals true value
 Apply random flipping on each bit of B’ and send it to the server to 
prevent that repeatedly sending B’ forms a unique tracking ID
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
RAPPOR: 2-level randomization
  RAPPOR:       Apply 2     -level randomization on a Bloom filter
        Stor ing a pr ivatized B’ to prevent that average of B’ reveals tr  ue value
        Apply random flipping on eac  h bit of B’ and send it to the ser   ver to
         prevent that repeatedly sending    B’ for  ms a unique trac  king ID
                                                                                         81
````

### 图片文字 OCR（en-US，待对照原页）

````text
RAPPOR: 2-level randomization
e RAPP OR: Apply 2 -level randomization on a Bloom filter
Storing a privatized B' to prevent that average of B' reveals true value
Apply random flipping
on each bit of B' and send it to the server to
prevent that repeatedly sending B' forms a unique tracking ID
Participant 8456 in cohort 1
True value:
Bloom filter (B):
Fake Bloom
filter (B'):
Report sent
to server:
"The number 68"
I III
II I II I III I I III I I III II I I I I III III III III I III II II III II II I II I II I I
32
64
III
128
4 signal bits
69 bits on
145 bits on
256
Bloom filter bits
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 82 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=82)

### 原始文字层

````text
RAPPOR: 2-level randomization
82
 RAPPOR: Apply 2-level randomization on a Bloom filter 
 If the RR is ε-DP, then B’ is kε-DP (i.e. protecting at most k bits)
 The “random” flipping (e.g. 0 →	1 with prob. 1/2 , 1 →	0 with prob. 
1/4) ensure that the bit 1 of Bloom filter is well preserved
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
RAPPOR: 2-level randomization
  RAPPOR: Apply 2-level randomization on a Bloom filter
        If the RR is ε-DP, then B’ is kε-DP (i.e. protecting at most k bits)
        The “random” flipping (e.g. 0 →	1 with prob. 1/2 , 1 →	0 with prob.
         1/4) ensure that the bit 1 of Bloom filter is well preser   ved
                                                                                     82
````

### 图片文字 OCR（en-US，待对照原页）

````text
RAPPOR: 2-level randomization
e RAPP OR: Apply 2 -level randomization on a Bloom filter
If the RR is E-DP, then B' is kE-DP (i.e. protecting at most k bits)
The "random" flipping (e.g. O 1 with prob. 1/2 , 1 0 with prob.
1 / 4) ensure that the bit 1 of Bloom filter is well preserved
Participant 8456 in cohort 1
True value:
Bloom filter (B):
Fake Bloom
filter (B'):
Report sent
to server:
"The number 68"
I III
II I II I III I I III I I III II I I I I III III III III I III II II III II II I II I II I I
32
64
III
128
4 signal bits
69 bits on
145 bits on
256
Bloom filter bits
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 83 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=83)

### 原始文字层

````text
Decoding noisy Bloom filter & RR
83
 Combine all user reports and observe how often each bit is set
 Each report is a noisy Bloom filter
 Each bit of the noisy Bloom filter is set with some probability
 To estimate the frequency of a particular value (e.g. URL):
 Look up its bit locations in the Bloom filter
 Compute the unbiased estimate of the probability each is 1
 Take the minimum of these estimates as the frequency
 More advanced decoding heuristics to decode all at once
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Decoding noisy Bloom f ilter & RR
  Combine all user repor    ts and obser     ve how often eac  h bit is set
         Eac  h repor   t is a noisy Bloom filter
         Eac  h bit of the noisy Bloom filter is set with some probability
  To                                       estimate the frequenc  y of a par    ticular value (e.g. URL):
         Look up its bit locations in the Bloom filter
         Compute the unbiased estimate of the probability eac  h is            1
         Take the minimum of these estimates as the frequenc y
         More advanced decoding heur istics to decode all at once
                                                                                                    83
````

### 图片文字 OCR（en-US，待对照原页）

````text
Decoding noisy Bloom filter & RR
Combine all user reports and observe how often each bit is set
Each report is a noisy Bloom filter
Each bit of the noisy Bloom filter is set with some probability
To estimate the frequency of a particular value (e.g. URL) :
Look up its bit locations in the Bloom filter
Compute the unbiased estimate of the probability each is 1
Take the
of these estimates as the frequency
minimum
More advanced decoding heuristics to decode
all
at once
83
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 84 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=84)

### 原始文字层

````text
RAPPOR in practice
84
 RAPPOR is implemented in the Chrome browser
 Collect data from opt-in users, tends of millions per day
 Open source implementation: https://github.com/google/rappor
 Tracks settings in the browser, e.g. homepage, search engine
 Many users unexpectedly change homepage ⇒	possible malware
 Typical configuration:
 128 bit Bloom filter, 2 hash functions, privacy parameter ε	=	0.5
 Needs about 10K reports to identify a value with confidence
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
RAPPOR in practice
          RAPPOR is implemented in the Chrome browser
                                Collect data from opt-in user s, tends of millions per day
                                Open source implementation: https://g  ithub.com/google/rappor
          Tr             a             c                k            s                          s            e            t             t             i             n            g             s                          i             n                          t             h            e                          b            r           o       w             s            e            r,                   e        .             g.                   h            o            m             e            p            a             g             e        ,                   s            e            a             r             c                h                          e            n            g                i             n            e
                                Many user  s unexpectedly c   hange homepage                                                                                                                      ⇒	possible malware
          Ty                       p                      i                       c                       a                       l                                               c                       o                      n                      f                       i                       g                       u                      r                       a                    t                       i                       o                      n                      :
                                128 bit Bloom filter, 2 hash functions, pr ivac y parameter ε	=	0.5
                                Needs about 10K repor   ts to identify a value with confidence
                                                                                                                                                                                                                                                                                                                84
````

### 图片文字 OCR（en-US，待对照原页）

````text
RAPPOR in practice
RAPPOR is implemented in the Chrome browser
Collect data from opt-in users, tends of millions per day
Open source implementation: https://github.com/google/rappor
Tracks settings in the browser, e.g. homepage, search engine
Many users unexpectedly change homepage possible malware
Typical configuration:
128 bit Bloom filter, 2 hash functions, privacy parameter E = 0.5
Needs about 10K reports to identify a value with confidence
84
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 85 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=85)

### 原始文字层

````text
Apple: Sketches and transform
85
 Similar problem to RAPPOR: count frequencies of many items
 Instead of Bloom filter, they use sketches (CountMean)
 Similar idea but better suited to capturing frequencies
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Apple: Sketches and transform
 Similar problem to RAPPOR: count frequencies of many items
 Instead of Bloom filter, they use sketc  hes (CountMean)
      Similar idea but better suited to captur ing frequencies
                                                                           85
````

### 图片文字 OCR（en-US，待对照原页）

````text
Apple: Sketches and transform
Similar problem to RAPP OR: count frequencies of many items
Instead of Bloom filter, they use sketches (CountMean)
Similar idea but better suited to capturing frequencies
eooeoeeooo
The Count Mean Sketch technique allows Apple to determine the most popular emoji to help
design better ways to find and use our favorite emoji. The top emoji for US English speakers
contained some surprising favorites.
85
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 86 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=86)

### 原始文字层

````text
Outline
86
 Motivation
 Why is anonymization hard
 Differential privacy
 Applications
 RAPPOR
 Private empirical risk minimization
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Outline
 Motivation
 Why is anonymization hard
 Differential pr  ivac y
 Applications
       RAPPOR
       Pr ivate empir ical r isk minimization
                                                                                 86
````

### 图片文字 OCR（en-US，待对照原页）

````text
Outline
Motivation
Why is anonymization hard
Differential privacy
Applications
RAPPOR
Private empirical risk minimization
86
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 87 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=87)

### 原始文字层

````text
Private empirical risk minimization
87
 Setup:
 A curator has training data X = ((x1, y1), … , (xn, yn)) about n
individuals and wants to train a model by minimizing over U ∈ V
W X, Y =
1
<Z
./!
0
[(\., ]., Y) +
^(Y)
<
 Examples: Logistic regression, SVM, linear regression, DNN, …
 Problem: Curator wants to protect the privacy of X
Loss function
Regularization
Objective function
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Private empirical risk minimization
  Setup:
        A curator has training data X = ((x1, y1), … , (xn, yn)) about n
         individuals and wants to train a model by minimizing over     U ∈  V
                                1  0                  ^(Y)
                   W  X, Y   =  < Z    [(\.,]. ,Y)  +    <          Regular ization
                                  ./!
        Objective function             Loss function
        Examples: Log  istic reg  ression, SVM, linear reg  ression, DNN, …
  Problem: Curator wants to protect the pr  ivac y of X
                                                                                       87
````

### 图片文字 OCR（en-US，待对照原页）

````text
Private empirical risk minimization
e Setup:
A curator has training data X = ((XI, Yl), , (xn, h)) about n
individuals and wants to train a model by minimizing over e e O
L(x, O)
I(Xi' Y i, O) +
Regularization
Objective function
n
i=l
Loss function
Examples: Logistic regression, S V M, linear regression, DNN,
Problem:
Curator wants to protect the privacy of X
87
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 88 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=88)

### 原始文字层

````text
Private empirical risk minimization
88
 Setup:
 A curator has training data X = ((x1, y1), … , (xn, yn)) about n
individuals and wants to train a model by minimizing over U ∈ V
W X, Y =
1
<Z
./!
0
[(\., ]., Y) +
^(Y)
<
 Private empirical risk minimization (ERM) algorithms:
 Output perturbation: add some noise Z to `_ = argmin , a b, `
 Objective perturbation: Reveal the optimum of a b, ` + `, c for 
some noise Z (adding noise to the objective function prior to minimizing)
 Gradient perturbation: optimize a b, ` using SGD with noisy gradients
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Private empirical risk minimization
  Setup:
        A curator has training data X = ((x1, y1), … , (xn, yn)) about n
         individuals and wants to train a model by minimizing over       U  ∈ V
                                     0
                    W  X, Y   =  1 Z    [(\  ,] , Y) +  ^(Y)
                                 <          .  .           <
                                   ./!
  Pr  ivate empir  ical r  isk minimization (ERM) algor  ithms:
        Output per   turbation: add some noise Z to `_    = argmin , a     b, `
        Objective per   turbation: Reveal the optimum of a     b, `   +   `, c   for
         some noise Z (adding noise to the objective function pr ior to minimizing)
        Gradient per   turbation: optimize a   b, `  	using SGD with noisy g  radients
                                                                                          88
````

### 图片文字 OCR（en-US，待对照原页）

````text
Private empirical risk minimization
Setup:
A curator has training data X = ((XI, Yl), , (xn, y n)) about n
individuals and wants to train a model by minimizing over e e O
L(x, O)
I(Xi, Yi, 0) +
n
i=l
Private empirical risk minimization (ERM) algorithms:
Output perturbation: add some noise Z to 9 = argmin 9 1(X, 9)
Objective perturbation: Reveal the optimum of I(X, 9) -I- (9, Z) for
some noise Z (adding noise to the objective function prior to minimizing)
Gradient perturbation: optimize I(X, 9) using SGD with noisy gradients
88
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 89 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=89)

### 原始文字层

````text
DP-ERM comparison
89
````

### 图片文字 OCR（en-US，待对照原页）

````text
DP-ERM comparison
Perturb
Objective
Output
Output
Output
Gradient
Gradient
Optimization
Exact
Exact
SGD
SGD
SGD
SGD
Privacy
e
Abadi et al.,
Assumptions
mear mo e
convexity
mear mo e
convexity
mear mo e
convexity
mear mo e
strong convexity
convexity
strong convexity
20161
Excess Risk
ö
1
1
d
d
See also [Talwar et al., 2014,
[Jain and Thakurta, 20141
[Jain and Thakurta, 20141
[wu et al., 20161
[Wu et al., 20161
[Bassily et al., 20141
[Bassily et al., 20141
research
89
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 90 页

[查看此页](../../../../source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy.pdf#page=90)

### 原始文字层

````text
Reference
90
 https://www.cs.utexas.edu/~shmat/courses/cs380s_fall09/
 https://cs.ioc.ee/ewscs/2016/maffei/maffei-slides-lecture1.pdf
 http://dimacs.rutgers.edu/~graham/pubs/papers/ldptutorial.pdf
 https://sites.google.com/view/kdd2018-tutorial/home
 http://dimacs.rutgers.edu/archive/Workshops/BigDataHub/Slides/RAPPO
R-talk-for-DIMACS-workshop-April-2017.pdf
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Re   fe   r   e   n   c   e
  https://www.cs.utexas.edu/~shmat/courses/cs380s_fall09/
  https://cs.ioc.ee/ewscs/2016/maffei/maffei-slides-lecture1.pdf
  http://dimacs.r  utger s.edu/~g  raham/pubs/paper s/ldptutor ial.pdf
  https://sites.google.com/view/kdd2018           -tutorial/home
  http://dimacs.rutgers.edu/archive/Workshops/BigDataHub/Slides/RAPPO
   R-talk-for-DIMACS-workshop-April-2017.pdf
                                                                                               90
````

### 图片文字 OCR（en-US，待对照原页）

````text
https://www.cs.utexas.edu/—shmat/courses/cs380s fa1109/
https://cs.ioc.ee/ewscs/2016/ maffei/maffei-slides-lecture 1 .pdf
http://dimacs.rutgers.edu/-v graham / pubs / papers / ldptutorial .pdf
https://sites.google.com/view/kdd2018 -tutorial / home
http://dimacs.rutgers.edu/archive/VVorkshops/BigDataHub/Slides/ RA PPO
R-talk-for-DIMACS-workshop-April- 2017 .pdf
90
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

