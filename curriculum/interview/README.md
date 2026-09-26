# 课程内的面试八股

按知识点覆盖，不设每课题数上限。当前基础16单元67道主问题，新增专题223道，共290道编号主问题，均配追问或边界说明。追问不重复计入主问题数。

**入口：[覆盖地图](COVERAGE.md) · [分阶段学习顺序](ROUTE.md) · [全部题号](coverage-map.json)。**

基础卡保留中文参考回答和英文表达，专题提供答案要点、英文关键词与验证练习。新增专题题库已编写，完整教科书式逐节讲义尚未全部展开；材料覆盖不代表学习通过。

## 学习顺序

**机制讲解→完整例题→独立练习→八股回答→追问/反例→延迟复习。**

先理解再压缩答案。不会时返回对应讲义，不要求凭空猜。面试回答可按“直接结论→为什么→一个例子→适用边界”组织；不是每题都必须硬套全部四段。

|单元|起始问题（完整题目见对应卡）|
|---|---|
|[DB01](DB01.md)|主键、外键分别解决什么问题？外键为什么可以重复？；为什么把用户和订单分成两张表？什么时候需要关联表？|
|[DB02](DB02.md)|NULL、0和空字符串有什么区别？为什么不能写city = NULL？；DISTINCT和ORDER BY有什么区别？为什么不能用DISTINCT随手修复重复？|
|[DB03](DB03.md)|WHERE、GROUP BY和HAVING的逻辑关系是什么？；COUNT(*)、COUNT(column)和COUNT(DISTINCT column)有什么区别？|
|[DB04](DB04.md)|INNER JOIN和LEFT JOIN有什么区别？连接后为什么行数会增加？；LEFT JOIN的条件放ON和WHERE里为什么结果可能不同？|
|[DB05](DB05.md)|什么时候用EXISTS，而不是JOIN？NOT EXISTS有什么用途？；CTE有什么用？NOT IN遇到NULL为什么可能出错？|
|[DB06](DB06.md)|PRIMARY KEY、FOREIGN KEY、NOT NULL和CHECK分别保证什么？；数据清洗如何判断重复？怎样证明没有错误丢数据？|
|[DB07](DB07.md)|索引为什么能加快查询？为什么不是越多越好？；如何优化慢SQL？EXPLAIN和EXPLAIN ANALYZE有什么区别？|
|[DB08](DB08.md)|ACID分别是什么？为什么用了事务还可能转账错误？；Read Committed和Repeatable Read有什么区别？超时后能直接重试吗？|
|[PY01](PY01.md)|list、tuple、dict、set怎样选择？；函数的return位置为什么重要？如何处理空输入和类型？|
|[PY02](PY02.md)|赋值、浅复制和深复制有什么区别？；为什么不建议用可变对象作默认参数？==和is有什么区别？|
|[PY03](PY03.md)|如何处理CSV中的缺失、类型错误、重复与冲突？；为什么用with和针对性的except？为什么不用split处理任意CSV？|
|[ALG01](ALG01.md)|如何分析时间与空间复杂度？两个循环就是O(n²)吗？；什么是循环不变量？如何解释Move Zeroes的正确性？|
|[ALG02](ALG02.md)|HashMap和HashSet如何选择？查找一定是O(1)吗？；配对计数为什么先查搭档再存当前元素？|
|[ALG03](ALG03.md)|滑动窗口为什么能减少重复计算？；可变窗口里套while，为什么仍可能是O(n)？|
|[ALG04](ALG04.md)|二分查找需要什么前提？怎样避免死循环和边界错误？；普通查找与lowerBound有什么区别？怎样处理重复和不存在？|
|[ALG05](ALG05.md)|栈和队列有什么区别？怎样从题意选择？；什么是摊还复杂度？Recent Calls为什么不是每次都最坏O(1)？|

## 不同类型怎么回答

|题型|回答组织|必须补上的证据|
|---|---|---|
|概念/比较|是什么、区别、适用场景|一个小例子或反例|
|机制/复杂度|过程、维护的状态、为何成立|手推或代码操作次数|
|排错/优化|现象、假设、验证、结果|实际查询/计划/输出，不虚构数字|
|项目追问|个人任务、选择、理由、验证、局限|真实代码或本人记录，区分设计与已完成|

## 如何验收

正常学习日15分钟用在一题口述、追问与英文复述，包含在120分钟内。R1/R2/R3/FINAL从已学单元抽题，在原订正/表达时段进行，不再叠加课时。见[评分补充](../ASSESSMENT.md)。

看过答案之后立刻复述记录为“有提示”；延迟复习时关闭答案，换问题或例子，才能提供独立理解的证据。八股答得好但实作没通过时，课程仍不能判B。

## 扩展专题

- [MYSQL｜MySQL索引、事务、锁与日志](topics/MYSQL.md)：20题；B｜数据库进阶。
- [NET｜计算机网络与HTTP](topics/NET.md)：15题；B｜通用基础。
- [OS｜操作系统、并发与Linux](topics/OS.md)：13题；B｜通用基础。
- [DS｜数据结构与算法后续覆盖](topics/DS.md)：11题；B→C｜算法进阶。
- [PYX｜Python语言机制与并发](topics/PYX.md)：12题；C｜Python/后端专项。
- [JS｜JavaScript与TypeScript](topics/JS.md)：14题；C｜前端/全栈专项。
- [WEB｜HTML/CSS、浏览器、安全与构建](topics/WEB.md)：13题；C｜前端/全栈专项。
- [REACT｜React与Next.js](topics/REACT.md)：14题；C｜前端/全栈专项。
- [ENG｜OOP、Git、测试与工程实践](topics/ENG.md)：12题；B｜通用工程基础。
- [API｜后端API、FastAPI与安全](topics/API.md)：12题；C｜后端/全栈专项。
- [CACHE｜Redis、缓存与可靠性](topics/CACHE.md)：12题；C｜后端/全栈专项。
- [SYS｜分布式、消息队列与系统设计](topics/SYS.md)：10题；D｜岗位进阶。
- [JAVA｜Java后端：语言、集合、并发、JVM与Spring](topics/JAVA.md)：28题；C→D｜投Java岗位时启用。
- [DATA｜数据分析、数据工程与机器学习基础](topics/DATA.md)：16题；C→D｜申请Data/ML岗位时启用。
- [AI｜AI应用、RAG与Agent可靠性](topics/AI.md)：13题；D｜AI/Agent专项。
- [VUE｜Vue岗位补充](topics/VUE.md)：8题；C｜JD要求Vue时启用。

每次学到该主题就练对应题；未完成题留在当前单元或后续分支队列，不因抽过一题就算整模块覆盖。新增问题继续追加稳定题号，不设封顶数量。
