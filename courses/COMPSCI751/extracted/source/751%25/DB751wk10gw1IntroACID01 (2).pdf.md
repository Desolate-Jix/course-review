# DB751wk10gw1IntroACID01 (2).pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI751/source/751%25/DB751wk10gw1IntroACID01 (2).pdf`
- [打开原文件](../../../source/751%2525/DB751wk10gw1IntroACID01%20%282%29.pdf)
- 原文件 SHA-256：`94c96ecbd9bd8af4521997253afca352b8f2a362819b7c2aae7d84ea59541af0`
- 文件索引：F167；PDF 总页数：15
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../source/751%2525/DB751wk10gw1IntroACID01%20%282%29.pdf#page=1)

### 原始文字层

````text
351/751
Gerald Weber
Transaction Processing
How to perform composite updates safely for a 
remotely and concurrently accessed system.
Motivation and first ACID properties
351/751 TA management 1
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
35  1/7  51
                                       Gerald  Weber
                   Tran sac ti  on  Proc es sing
       Ho  w  to   p e rfor m com  po  si te   upd a te s  s afe ly   for  a
           r em  ote l y  a nd   concur re ntl y  a cce ss e d  s ys te m.
    M ot iv a ti on a nd  fi rs t  AC ID pr op e rt ie s
 351  /751                               TA man ag ement                                     1
````

### 图片文字 OCR（en-US，待对照原页）

````text
351/751
Gerald Weber
Transaction Processing
How to perform composite updates safely for a
remotely and concurrently accessed system.
Motivation and first ACID properties
351/751
TA management
1
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../source/751%2525/DB751wk10gw1IntroACID01%20%282%29.pdf#page=2)

### 原始文字层

````text
• An online multi-leg flight booking system (web or app).
• Users submit their orders and expect them to be:
• Processed as quickly as possible, also meaning that the 
user gets quick feedback on success/no success.
• Exactly as requested, in particularly complete:
• Book all legs of the flight selected, or do nothing.
• Example problem Atomicity:
• My system or the server or the network can fail.
• But I want my order done as a whole.
• The solutions are discussed in transaction processing.
 
351/751 TA management 2
Motivating Example: Flight booking
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Motiv ating Example:                  Flight book ing
• An onl ine mul ti-leg fli ght booki ng sys tem (web or  app).
• User s submit their  or der s and expect them to be:
    •  Pro ces sed as  quickly as pos sible, also  meaning that the
       user  gets quick feedback on succes s/no s uccess .
    •  Exactl y as r equested, in particular ly complete:
         • Book al  l legs of the  flight selec ted,  or do  nothing.
• Exampl e pr oblem Atom icity:
         • My system or  the ser ver  or  the netwo rk can fail.
         • But I want my o rder done as a whole.
• The s olutio ns  are discuss ed in        transaction pro ces sing.
351  /751                          TA man ag ement                                 2
````

### 图片文字 OCR（en-US，待对照原页）

````text
Motivating Example: Flight booking
An online multi-leg flight booking system (web or app).
Users submit their orders and expect them to be:
Processed as quickly as possible, also meaning that the
user gets quick feedback on success/no success.
Exactly as requested, in particularly complete:
Book all legs of the flight selected, or do nothing.
Example problem Atomicity
My system or the server or the network can fail.
• But I want my order done as a whole.
The solutions are discussed in transaction processing.
351/751
TA management
2
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../source/751%2525/DB751wk10gw1IntroACID01%20%282%29.pdf#page=3)

### 原始文字层

````text
351/751 TA management 3
Atomicity
Another Example
In a transfer transaction from account 123 to account 321: 
i.) withdraw $100 from account 123 
ii.) put $100 on account 321
∙ It must not happen that the transaction stops after i.) and 
makes i.) persistent (durable), and never executes ii.)
∙ Why not? This would violate an application level 
consistency constraint:
∘ Overall balance must be kept.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Atomicit y
Another Exampl e
In a tr ansfer tr ans actio n f  rom account 1 23  to acco unt 3 21 :
              i.)    withdraw  $100 from ac count 123
              ii.)   put $100 on acc ount 321
∙ It mus t no t happen that the transaction s to ps  af  ter  i.) and
  makes i.) persi stent (durable), and never executes ii .)
∙ Why not? Thi s would vio late an appli catio n level
  consi stency cons tr aint:
    ∘  Overall  balance mus t be kept.
351  /751                            TA man ag ement                                  3
````

### 图片文字 OCR（en-US，待对照原页）

````text
Atomicity
Another Example
In a transfer transaction from account 123 to account 321:
i.) withdraw $100 from account 123
ii.) put $100 on account 321
It must not happen that the transaction stops after i.) and
makes i.) persistent (durable), and never executes ii.)
Why not? This would violate an application level
consistency constraint:
0 Overall balance must be kept.
351/751
TA management
3
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../source/751%2525/DB751wk10gw1IntroACID01%20%282%29.pdf#page=4)

### 原始文字层

````text
• Example problem Atomicity:
• My system or the server or the network can fail.
• But I want my order done as a whole.
• Needs transaction demarcation:
• System must know:
• when does one user order (start and) end:
• Operation to signal end of transaction: commit().
• Transaction: A sequence of operations that form a logical 
unit; sequence of operations delimited by TA demarcation.
• Transaction script: a subprogram issuing a transaction if 
called.
351/751 TA management 4
Transaction Demarcation for Atomicity
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Tra nsaction Dema rcation  for  Atomicit y
• Exampl e pr oblem Atom icity:
        •  My system or  the ser ver  or  the netwo rk can fail.
        •  But I want my o rder done as a whole.
• Ne e d s tran sa  ct ion  dem arcation         :
• System mus t know:
    •  when does  one us er or der  (s tar t and)         en d:
    •  Oper ati on to  signal end o f transacti on:        commit ().
• Transaction: A  sequence of operatio ns  that for m a l ogical
  unit; sequence of  oper ati ons delimi ted by TA demar cati on.
• Transaction scr ipt: a s ubpro gr am i ssui ng a transacti on if
  called.
351  /751                         TA man ag ement                                4
````

### 图片文字 OCR（en-US，待对照原页）

````text
Transaction Demarcation for Atomicity
Example problem Atomicity
My system or the server or the network can fail.
But I want my order done as a whole.
Needs
transaction demarcation:
System must know:
when does one user order (start and) end:
Operation to signal end of transaction: commit().
Transaction: A sequence of operations that form a logical
unit; sequence of operations delimited by TA demarcation.
Transaction script: a subprogram issuing a transaction if
called.
351/751
TA management
4
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../source/751%2525/DB751wk10gw1IntroACID01%20%282%29.pdf#page=5)

### 原始文字层

````text
351/751 TA management 5
Typical architecture for use of databases
database
system
application 
server 2
application 
server 3
application 
server 1
Remote connections,
ODBC
database clients
terminals,
networks,
etc
internet
transaction scripts
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Typical ar chitecture for use of dat abases
                   database clients
terminals ,                                     Remote connectio ns ,
netwo rks,          appl icati on               ODBC
etc                   ser ver  1
                    appl icati on
                      ser ver  2                                    database
                                                                     sys  tem
                    appl icati on
                      ser ver  3
 i ntern et
                        trans actio n s cripts
351  /751                           TA man ag ement                                 5
````

### 图片文字 OCR（en-US，待对照原页）

````text
Typical
terminals,
networks,
etc
internet
351/751
architecture for use of databases
database clients
application
server 1
application
server 2
application
Remote connections,
ODBC
transaction scripts
TA management
database
system
5
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../source/751%2525/DB751wk10gw1IntroACID01%20%282%29.pdf#page=6)

### 原始文字层

````text
351/751 TA management 6
Rollback for Atomicity
1. The client needs to issue a commit() request. Commit 
must be requested by client: Only if commit has been 
requested, writes in the transaction may become durable.
This protects against failures that lead to incomplete 
transaction processing:
Hence: Database must take care of the rollback in 
case no commit has been registered.
1. b. client can request abort as a programming feature.
2. Atomicity: Either all writes of the transaction, or none 
become durable: If any write becomes durable, all must 
become durable.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Rollback for Atomicity
1.  The cl ient needs  to  iss ue a commit()  reques t. Co mmi t
    must be r equested by cli ent: Only if   co mmi t has been
    r equested, wri tes i n the transacti on may become dur abl e.
    This pro tects agai nst failur es  that lead to i nco mpl ete
    transaction pro ces sing:
    Hence: Dat abas e m us t t ake care  of  th e rollback  in
    cas e no  com mit  has  been  regist ered  .
1 .  b. cl ient can request abor t as  a pr ogramming feature.
2.  Atomici ty:  Either  all wr ites  of the tr ans actio n, o r none
    beco me durable: If   any wr ite becomes durable, al l must
    beco me durable.
351  /751                         TA man ag ement                                6
````

### 图片文字 OCR（en-US，待对照原页）

````text
Rollback for Atomicity
1.
1.
2.
The client needs to issue a commit() request. Commit
must be requested by client: Only if commit has been
requested, writes in the transaction may become durable.
This protects against failures that lead to incomplete
transaction processing:
Hence: Database must take care of the rollback in
case no commit has been registered.
b. client can request abort as a programming feature.
Atomicity: Either all writes of the transaction, or none
become durable: If any write becomes durable, all must
become durable.
351/751
TA management
6
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../source/751%2525/DB751wk10gw1IntroACID01%20%282%29.pdf#page=7)

### 原始文字层

````text
Example Transaction Script
Status TransferWithCheck (amount, account1, account2) {
funds = DB.read(account1);
if ( funds < amount ) {
Db.rollback();
return Status.insufficientFundsError;
} else {
DB.write (account1, funds-amount);
DB.write (account2, DB.read(account2)+amount);
DB.commit();
return Status.success;
}
351/751 TA management 7
(Not referring to a specific database technology)
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Exa mple  Transa ct io n  Scr ipt
        (Not referring to a speci  fi  c database technology)
Stat us    Trans ferWit hCheck ( amoun  t, account 1,  account 2)                   {
   funds = DB.read( accoun  t1);
   if ( funds < amount          ) {
      Db. ro  llback();
      return    Stat us. ins uffi  ci  en  tFun  ds Error;
   } els e {
      DB.write ( accoun  t1, funds-amount );
      DB.write ( accoun  t2, DB.read( accoun  t2)+amo  unt) ;
      DB.commit();
      return Stat us. success;
 }
35   1/ 7   51                          TA     m  ana   gem  ent                              7
````

### 图片文字 OCR（en-US，待对照原页）

````text
Example Transaction Script
(Not referring to a specific database technology)
Status
TransferWithCheck (amount, accountl, account2)
funds = DB.read(account1 );
if (
funds < amount
Db.rollback();
Status.insufficientFundsError;
return
} else {
DB.write (accountl , funds-amount);
DB.write (account2, DB.read(account2)+amount);
DB.commit();
return Status.success;
351/751
TA management
7
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../source/751%2525/DB751wk10gw1IntroACID01%20%282%29.pdf#page=8)

### 原始文字层

````text
From the Tech News MongoDB
351/751 TA management 8
````

### 图片文字 OCR（en-US，待对照原页）

````text
From the Tech News MongoDB
mongoDB, I FOR GIANT IDEAS
Eliot Horowitz
February 15, 2018
Category: Company, Technical
SOLUTIONS
351/751
MongoDB 4.0 will add support for multi-document transactions, making it the only
database to combine the speed, flexibility, and power of the document model with ACID
data integrity guarantees. Through snapshot isolation, transactions provide a globally
consistent view of data, and enforce all-or-nothing execution to maintain data integrity.
ransactions in MongoDB will feel just like transactions developers are familiar with from
relational databases. They will be multi-statement, with similar syntax (e.g.
start transaction and commit transaction), making them familiar to anyone with prior
he changes to MongoDB that enable multi-document
ransaction experience.
transactions will not impact performance for workloads that do not require them. In
MongoDB 4.0, which will be released this summer*, transactions will work across a single
TA management
8
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../source/751%2525/DB751wk10gw1IntroACID01%20%282%29.pdf#page=9)

### 原始文字层

````text
351/751 TA management 9
Atomicity requires rollback
• For Atomicity, the database must be able to undo write 
operations of uncommitted transactions.
• We consider here strategies that work with a log.
• The log is a list of records for write operations in the order 
of execution
∘ optionally with some datastructures 
∘ for easier access. 
• The log will be also important for recovery and ensuring Durability and 
will contain more information than we immediately need for rollback in 
the context of Atomicity.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Atomicit y r equires  rollback
•  For  Ato micity, the databas e must be able to undo wri te
   operatio ns  of uncommitted transacti ons.
•  We consider her e s tr ategies that wo rk with a                     lo  g.
•  The l og is a l ist of r ecords f  or wr ite oper ati ons i n the or der
   of   executi on
     ∘  optionall y with s ome datastructur es
     ∘  fo r easier  access .
•  The  log wil  l be also important f or recovery  and ensuring  Durability  and
   will  contai  n  more  information than we  immediately  need for rollback  in
   the c ontext of  Atomicity .
351  /751                                 TA man ag ement                                    9
````

### 图片文字 OCR（en-US，待对照原页）

````text
Atomicity requires rollback
For Atomicity, the database must be able to undo write
operations of uncommitted transactions.
We consider here strategies that work with a log
The log is a list of records for write operations in the order
of execution
0 optionally with some datastructures
0 for easier access.
• The log will be also important for recovery and ensuring Durability and
will contain more information than we immediately need for rollback in
the context of Atomicity.
351/751
TA management
9
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../source/751%2525/DB751wk10gw1IntroACID01%20%282%29.pdf#page=10)

### 原始文字层

````text
351/751 TA management 10
Database internal architecture
server with
database management system
stable 
database
stable 
Log
log buffer
database
buffer 
transaction
manager
Database
database Clients
clients
Durable
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Dat abase inter nal ar chitecture
                            server  wi th                                            stab le
                            da taba se  man ag em  en t system                     da ta ba se
    Database
       databaseCl ients      transaction              da taba se
         cl ients             ma na ge r               bu  ff er
                                                                                 Durable
                                                     l og b uffer
                                                                                      stab  le
                                                                                        Log
351  /751                                   TA man ag ement                                            10
````

### 图片文字 OCR（en-US，待对照原页）

````text
Database internal architecture
database
clients
351/751
server with
database management system
transaction
database
manager
buffer
log buffer
TA management
stable
database
Durable
stable
Log
10
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../source/751%2525/DB751wk10gw1IntroACID01%20%282%29.pdf#page=11)

### 原始文字层

````text
351/751 TA management 11
The Database Log 
• is a central feature of typical database managers.
• The log contains a list of 
∘ the write operations performed.
∘ The transaction demarcations: (BOT), abort, commit. 
• We consider undo/redo logs: for each write operation, a 
log entry is written that contains:
∘ a log sequence number, or LSN (denoted as “nr:”)
∘ The transaction ID of the executing transaction (“ta:”).
∘ An identifier of the object affected (“obj:”)
∘ the value before the write operation (before-image, 
“b:”).
∘ the value after the write operation (after-image, “a:”).
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
The  Data ba se  Log
• is  a central f  eature of   typical database managers .
• The l og contai ns  a lis t o f
    ∘  the wr ite oper ati ons perfo rmed.
    ∘  The tr ans actio n demarcati ons:  (BOT), abort, commit.
• We consider undo/r edo  logs:  for  each wri te operatio n, a
  lo g entry i s wri tten that co ntains :
    ∘  a lo g s equence number , o r LSN ( denoted as  “nr :”)
    ∘  The tr ans actio n ID of   the executing tr ans actio n (“ta: ”)  .
    ∘  An identi fier  of the o bject affected (“obj:”)
    ∘  the val ue befor e the wri te operatio n ( befo re               -im a g e ,
       “b:”).
    ∘  the val ue after the wr ite operation (after-image, “a:”).
351  /751                               TA man ag ement                                 11
````

### 图片文字 OCR（en-US，待对照原页）

````text
The Database Log
is a central feature of typical database managers.
The log contains a list of
0 the write operations performed.
0 The transaction demarcations: (BOT), abort, commit.
We consider undo/redo logs: for each write operation, a
log entry is written that contains:
0 a log sequence number, or LSN (denoted as "nr:")
0 The transaction ID of the executing transaction ("ta:").
0 An identifier of the object affected ("obj:")
0 the value before the write operation (before-image,
0 the value after the write operation (after-image, "a:").
351/751
TA management
11
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../source/751%2525/DB751wk10gw1IntroACID01%20%282%29.pdf#page=12)

### 原始文字层

````text
351/751 TA management 12
Example log and database
• The log of the database and the database buffer at a 
certain point in time could look the following way (new 
operations are appended at lower end)
• Transaction demarcations contain only LSN and TA.
x 78 z 54
y 87
......
[nr: 109, ta: 22, BOT]
[nr: 110, ta: 22, obj: x, b: 2, a: 53]
[nr: 111, ta: 22, commit]
[nr: 112, ta: 23, BOT]
[nr: 113, ta: 23, obj: x, b: 53, a: 46]
[nr: 114, ta: 24, BOT]
[nr: 115, ta: 24, obj: y, b: 34, a: 87]
[nr: 116, ta: 23, obj: z, b: 23, a: 54]
[nr: 117, ta: 23, obj: x, b: 46, a: 78]
The state of the 
buffer at this point 
in time
Log Sequence Number (LSN)
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Exa mple  log  and data ba se
• The l og of the database and the databas e buffer  at a
  certain point in time co uld loo k the fol lowi ng way (new
  operatio ns  are appended at l ower end)
• Transaction demar catio ns contai n only LSN and TA.......
     [nr: 109, ta: 22, BOT]
     [nr: 110, ta: 22, obj:  x, b:  2,  a:  53]
     [nr: 111, ta: 22, co  mm  it]
     [nr: 112, ta: 23, BOT]                                     x  78     z   54
     [nr: 113, ta: 23, obj:  x, b:  53, a:  46]
     [nr: 114, ta: 24, BOT]
     [nr:  115, ta:  24, obj: y, b: 34, a: 87]                       y   87
     [nr:  116, ta:  23, obj:  z, b:  23, a:  54]
     [nr:  117, ta:  23, obj:  x, b:  46, a:  78]
 Log Sequence Number  (LSN)                                 The s tate of the
                                                            buffer  at this poi nt
351  /751                               TA man ag ement     in time                      12
````

### 图片文字 OCR（en-US，待对照原页）

````text
Example log and database
The log of the database and the database buffer at a
certain point in time could look the following way (new
operations are appended at lower end)
Transaction demarcations contain only LSN and TA.
110, ta:
53, a: 46]
113, ta:
[nr: 115,
[nr:
[nr:
[nr:
[nr:
109, ta: 22, BOT]
[nr: 111, ta:
114,
[nr: 116, ta:
[nr: 117, tan.
[nr: 112, ta: 23, BOT]
22, obj: x, b:
22, commit]
23, obj: x, b:
24, BOT]
24, obj: y, b:
23, obj: z, b:
23, obj: x, b:
2, a: 53]
34, a: 87]
23, a: 54]
46, a: 78]
Log Sequence Number (LSN)
x 78 z 54
Y 87
The state of the
buffer at this point
in time
351/751
TA management
12
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../source/751%2525/DB751wk10gw1IntroACID01%20%282%29.pdf#page=13)

### 原始文字层

````text
351/751 TA management 13
Rollback
• A transaction that is aborted has to be undone in a 
rollback.
Rollback is the undoing of a transaction during normal 
operation (also known as transaction recovery, but we do 
not use this term).
• This rollback is based on the log.
∘ An abort record is entered into the log.
• For all write operations performed so far
∘ The before-image is restored.
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Rollback
• A transaction that i s abo rted has to be undo ne i n a
  rollback.
  Rol lback i s the undoing of a transaction during nor mal
  operatio n ( also  kno wn as  tr ans actio n recovery, but we do
  not use thi s term).
• This r oll back is  bas ed on the log.
    ∘  An abort r eco rd is entered into  the lo g.
• For  al l wri te o per atio ns per for med s o far
    ∘  The befor e-image is r estored.
351  /751                             TA man ag ement                              13
````

### 图片文字 OCR（en-US，待对照原页）

````text
Rollback
A transaction that is aborted has to be undone in a
rollback.
Rollback is the undoing of a transaction during normal
operation (also known as transaction recovery, but we do
not use this term).
This rollback is based on the log.
0 An abort record is entered into the log.
For all write operations performed so far
0 The before-image is restored.
351/751
TA management
13
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../source/751%2525/DB751wk10gw1IntroACID01%20%282%29.pdf#page=14)

### 原始文字层

````text
351/751 TA management 14
Example: rollback of TA 23
• In case of a rollback, the 
operations are undone and the 
before-images are restored. 
x 78 z 54
y 87
[nr: 109, ta: 22, BOT]
[nr: 110, ta: 22, obj: x, b: 2, a: 53]
[nr: 111, ta: 22, commit]
[nr: 112, ta: 23, BOT]
[nr: 113, ta: 23, obj: x, b: 53, a: 46]
[nr: 114, ta: 24, BOT]
[nr: 115, ta: 24, obj: y, b: 34, a: 87]
[nr: 116, ta: 23, obj: z, b: 23, a: 54]
[nr: 117, ta: 23, obj: x, b: 46, a: 78]
[nr: 118, ta: 23, abort]
46
53
23
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Exa mple:   rollback o f  TA  23
• In case of a r oll back, the
  operatio ns  are undo ne and the
  before-images are res to red.
     [nr: 109, ta: 22, BOT]
     [nr: 110, ta: 22, obj: x, b: 2, a: 53]                            53
     [nr: 111, ta: 22, co  mm  it]                                   46        23
     [nr: 112, ta: 23, BOT]                                     x   78    z   54
     [nr: 113, ta: 23, obj: x, b: 53,  a: 46]
     [nr: 114, ta: 24, BOT]
     [nr:  115, ta: 24, obj:  y, b:  34,  a:  87]                    y   87
     [nr: 116,  ta: 23, obj: z, b: 23, a: 54]
     [nr: 117,  ta: 23, obj: x, b: 46,  a: 78]
     [nr: 118,  ta: 23, abort]
351  /751                                TA man ag ement                                 14
````

### 图片文字 OCR（en-US，待对照原页）

````text
Example: rollback of TA 23
In case of a rollback, the
operations are undone and the
before-images are restored.
[nr:
[nr:
[nr:
351/751
[nr: 109, ta: 22, BOT]
110, ta: 22, obj: x, b:
[nr: 111, ta: 22, commit]
112, ta: 23, BOTI
[nr: 113, ta: 23, obJ. x,
[nr: 114, ta: 24, BOT]
115, ta: 24, obj: y, b:
[nr: 116, ta: 23, obJ: z,
[nr: 117, ta: 23, obj. x,
118, ta: 23, abort]
2, a: 53]
b: 53, a: 46]
34, a: 87]
• b: 23, a: 54]
b: 46,
a: 78]
TA management
53
46
23
78 z 54
Y 87
14
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../source/751%2525/DB751wk10gw1IntroACID01%20%282%29.pdf#page=15)

### 原始文字层

````text
Summary
1. we need transaction demarcation for atomicity: 
for example for remote access.
2. Transaction: A sequence of operations that form a logical 
unit; the client has to request commit.
3. The database needs to roll back failed transactions.
4. The ACID Properties (Atomicity, Consistency, Isolation, 
Durability) are the requirements of transaction processing.
5. We consider Database Managers with undo/redo logs.
351/751 TA management 15
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Summa ry
1.  we need transacti on demar catio n f or atomici ty:
    fo r example fo r remot e acces s.
2.  T rans action     : A s equence o f operations that f  orm a lo gi cal
    unit; the cl ient has to r equest commit.
3.  The database needs  to  rol l back fail ed transactions .
4.  The A CID Pr oper ties (A to mi city, Co nsis tency, Is olatio n,
    Durabili ty)  ar e the r equir ements of  tr ans actio n pr ocessi ng.
5.  We consider       Database Managers with undo/ redo lo gs .
 351  /751                           TA man ag ement                                15
````

### 图片文字 OCR（en-US，待对照原页）

````text
Summary
1.
2.
3.
4.
5.
we need transaction demarcation for atomicity:
for example for remote access.
Transaction: A sequence of operations that form a logical
unit; the client has to request commit.
The database needs to roll back failed transactions.
The ACID Properties (Atomicity, Consistency, Isolation,
Durability) are the requirements of transaction processing.
We consider Database Managers with undo/redo logs.
351/751
TA management
15
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

