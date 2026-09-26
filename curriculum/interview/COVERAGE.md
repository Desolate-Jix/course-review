# 国内技术面试覆盖地图

2026-09-26按用户要求改为**不限题量，以覆盖为标准**。当前共有290道编号主问题，每题有配套追问或边界说明；追问不另算主问题。基础课67题，专题223题。数量只是盘点结果，不是上限或学习KPI。

## 什么叫覆盖

- 材料覆盖：知识点有具体问题、可核对答案、追问/边界、练习和先修位置；仅写在目录里不算。
- 学习覆盖：对应必修点实际讲过/诊断过，能独立解释和处理变式，有输出证据；不能用一次抽中熟题代替全模块。
- 岗位覆盖：通用基础加本次投递岗位分支，并对照实际JD/面经补差。题库包含某分支，不代表用户已选择或已学该分支。
- 本表覆盖本计划的软件、前端/全栈、Python/Java后端及Data/AI相关范围；没有“全国所有公司所有题”的固定全集。Go/C++/嵌入式、特定中间件源码、深度分布式存储、ML数学推导等若JD明确要求，登记为待补专项，不能标成已覆盖。

## 第一阶段：原课程内补齐

基础卡的Q1/Q2仍是入口题，新增问题也是对应单元必修覆盖点。已有实作验收与新增概念配套使用；新增点无讲解时先补机制与例子，不能直接考未学内容。题量大时拆课顺延。

|单元|覆盖重点|完整题号|
|---|---|---|
|[DB01](DB01.md)|主外键、候选键、业务键、关系基数|DB01-Q1至Q4|
|[DB02](DB02.md)|NULL三值逻辑、排序、去重、稳定分页|DB02-Q1至Q4|
|[DB03](DB03.md)|分组聚合、NULL/空集、集合合并|DB03-Q1至Q4|
|[DB04](DB04.md)|连接语义、行数膨胀、物理连接|DB04-Q1至Q4|
|[DB05](DB05.md)|存在性、反连接、相关子查询、CTE|DB05-Q1至Q4|
|[DB06](DB06.md)|约束、范式、并发唯一性、删除语义|DB06-Q1至Q5|
|[DB07](DB07.md)|B+树、复合索引、索引条件、执行计划、统计与测量|DB07-Q1至Q6|
|[DB08](DB08.md)|ACID、隔离异常、并发更新、锁、死锁、恢复边界|DB08-Q1至Q6|
|[PY01](PY01.md)|容器、哈希键、函数参数与返回|PY01-Q1至Q4|
|[PY02](PY02.md)|复制、默认参数、共享引用、二维列表|PY02-Q1至Q4|
|[PY03](PY03.md)|清洗、流式处理、幂等导入、对账|PY03-Q1至Q4|
|[ALG01](ALG01.md)|复杂度、不变量、数组链表、稳定性|ALG01-Q1至Q4|
|[ALG02](ALG02.md)|哈希计数、冲突扩容、有序结构|ALG02-Q1至Q4|
|[ALG03](ALG03.md)|窗口、前缀和、单调性|ALG03-Q1至Q3|
|[ALG04](ALG04.md)|二分边界、lowerBound、单调判定|ALG04-Q1至Q3|
|[ALG05](ALG05.md)|栈队列、摊还、单调结构|ALG05-Q1至Q4|

## 通用进阶与岗位专项

下列每个链接已有问题、答案要点、追问边界、英文关键词和模块验证。完整教科书式逐节讲义仍需随课程推进补写；此处不会把题库冒充完整讲义。

|模块|覆盖内容|阶段与先修|题号范围|
|---|---|---|---|
|[MYSQL](topics/MYSQL.md)|MySQL索引、事务、锁与日志|B｜数据库进阶；DB01–DB08；先识别MySQL 8.4/InnoDB与PostgreSQL差异|MYSQL-01至20|
|[NET](topics/NET.md)|计算机网络与HTTP|B｜通用基础；函数、基本输入输出|NET-01至15|
|[OS](topics/OS.md)|操作系统、并发与Linux|B｜通用基础；函数、内存引用；NET可并行学习|OS-01至13|
|[DS](topics/DS.md)|数据结构与算法后续覆盖|B→C｜算法进阶；ALG01–ALG05；按题序补递归|DS-01至11|
|[PYX](topics/PYX.md)|Python语言机制与并发|C｜Python/后端专项；PY01–PY03；并发题先学OS|PYX-01至12|
|[JS](topics/JS.md)|JavaScript与TypeScript|C｜前端/全栈专项；主语言函数与引用；NET入门|JS-01至14|
|[WEB](topics/WEB.md)|HTML/CSS、浏览器、安全与构建|C｜前端/全栈专项；NET、JS|WEB-01至13|
|[REACT](topics/REACT.md)|React与Next.js|C｜前端/全栈专项；JS、WEB；熟悉组件与基本状态|REACT-01至14|
|[ENG](topics/ENG.md)|OOP、Git、测试与工程实践|B｜通用工程基础；函数、引用、能运行小程序|ENG-01至12|
|[API](topics/API.md)|后端API、FastAPI与安全|C｜后端/全栈专项；NET、DB08、PYX、ENG|API-01至12|
|[CACHE](topics/CACHE.md)|Redis、缓存与可靠性|C｜后端/全栈专项；API、MYSQL或DB07–08、OS|CACHE-01至12|
|[SYS](topics/SYS.md)|分布式、消息队列与系统设计|D｜岗位进阶；NET、API、DB08、CACHE|SYS-01至10|
|[JAVA](topics/JAVA.md)|Java后端：语言、集合、并发、JVM与Spring|C→D｜投Java岗位时启用；ALG02、OS、ENG、API；基础Java语法|JAVA-01至28|
|[DATA](topics/DATA.md)|数据分析、数据工程与机器学习基础|C→D｜申请Data/ML岗位时启用；PY03、DB01–08；统计题先补概率基础|DATA-01至16|
|[AI](topics/AI.md)|AI应用、RAG与Agent可靠性|D｜AI/Agent专项；API、ENG、DATA评估基础；了解向量和相似度|AI-01至13|
|[VUE](topics/VUE.md)|Vue岗位补充|C｜JD要求Vue时启用；JS、WEB；与React按目标岗位选择|VUE-01至08|

## 岗位选择与防遗漏

|投递方向|共同覆盖|专项覆盖|不自动强加的分支|
|---|---|---|---|
|前端|第一阶段、NET、OS基础、ENG、DS递进|JS、WEB、REACT；JD指定Vue则加VUE|JAVA/JVM/Spring不是前端默认必修|
|全栈|同上，数据库需要MYSQL进阶|前端分支＋API；Python服务用PYX，缓存需求加CACHE|不要求同时学多个后端框架|
|Python后端|第一阶段、NET、OS、ENG、MYSQL、DS递进|PYX、API、CACHE，随后SYS|Java仅因JD需要才学|
|Java后端|第一阶段、NET、OS、ENG、MYSQL、DS递进|JAVA、API通用题、CACHE、SYS|Python框架题按JD取舍|
|Data/数据工程|SQL/Python基础、ENG、NET基础|DATA、MYSQL；工程岗位再加API/CACHE/SYS相关点|前端/JVM不是默认要求|
|AI/Agent工程|编程、NET、ENG、API、数据库基础|AI、DATA评估相关点；按服务栈补PYX或前端|不能用Prompt/RAG替代软件基础|

API里的FastAPI问题对Java方向只作比较，不要求为Java岗位学习整个Python框架。学习顺序和逐段题号见[分阶段课程接入](ROUTE.md)。

## 遇到新JD/面经怎样扩展

将未覆盖的技术词拆成可检验问题，标记岗位、先修、版本、参考资料、验证方式；补答案和追问后再把材料标为已编写。若现有问题已覆盖同一机制，可添加变式而不机械复制题目。必须保持稳定题号，不因扩题改动已有笔记中的题号。

每次阶段复盘检查：①本分支是否有整块缺口；②是否只会定义不会机制；③是否只有熟题没有反例；④是否有无实测却声称实测的项。未满足的点继续留在学习/复习队列。

## 对照资料与版本

范围对照：[JavaGuide](https://github.com/Snailclimb/JavaGuide)、[小林MySQL目录](https://xiaolincoding.com/mysql/)、[前端面试指南](https://feinterview.poetries.top/)。这些是目录检查线索，不是全国统一考纲，也不用它们的“必考”宣传替代岗位判断。

技术答案优先参照每页的官方文档、规范或原论文。MySQL 8.4/InnoDB与PostgreSQL18分开；JDK21只作示例基线；CPython GIL要标构建方式；React/Next/Spring缓存及代理规则按项目实际版本复核。

[全部题号清单](coverage-map.json) · [八股总目录](README.md)
