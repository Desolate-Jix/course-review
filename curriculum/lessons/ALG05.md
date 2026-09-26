# ALG05｜栈、队列与摊还分析

先修：ALG01。先修待验证时先做前节验收；通过可跳过重复讲解。

## 学完要能做到

根据LIFO/FIFO选择结构，独立处理时间窗口边界，解释单次最坏与摊还成本区别。

## 讲解与例题


### 1. 操作顺序决定结构

栈是后进先出LIFO，适合撤销最近加入的有效元素。旧题2390 Removing Stars From a String里，星号删除最近的未删除字符，所以可以用栈或StringBuilder末尾删除。

队列是先进先出FIFO，适合按进入顺序淘汰过期请求。新题933 Number of Recent Calls把时间t加入队尾，再从队头移除小于t-3000的请求，剩下的数量就是闭区间 `[t-3000,t]` 中的请求数。

### 2. 边界决定何时删除

时间1、100、3001、3002的返回值为1、2、3、3。处理3001时，时间1恰好等于t-3000，必须保留；不能写成<=。

Java的ArrayDeque可通过offerLast/pollFirst实现队列，通过push/pop实现栈。名字相近不代表删除的是同一端；先说清语义再用API。

### 3. 摊还不是每次都常数

某次ping可能一次移除很多元素，所以单次并非总是O(1)。但处理n次调用时，每个请求只入队一次、出队最多一次，总体O(n)，平均到每次是摊还O(1)。空间与窗口内保留的请求数有关。


## 独立练习


1. 复述或闭卷复刷2390，解释为什么删除最近字符。
2. 学会队列操作后独立做933；题目在原75白名单中，只有真实Accepted后才增加历史题数。
3. 原创变式：把3000改成参数window，解释等于边界时的保留规则。
4. 构造一次ping删除多个旧请求的输入，区分单次最坏和总成本。


先写自己的解答，记录用过哪些提示，再打开[答案与判分要点](../answers/ALG05.md)。

## 验收与复习

完成独立题后，按[统一标准](../ASSESSMENT.md)评估。必须处理题目中的边界或变式；刚看完答案的重写不能算独立通过。用自己的话解释一个机制，再用英语说一个60秒摘要。当前不会的内容回到本节具体小点补学。

根据LIFO/FIFO选择结构，独立处理时间窗口边界，解释单次最坏与摊还成本区别。

## 资料

[已有24题及代码笔记](https://github.com/Desolate-Jix/learning-plan/blob/main/STUDY_PROGRESS.md)；[LeetCode 75题单](https://github.com/Desolate-Jix/learning-plan/blob/main/LEETCODE_75_CHECKLIST.md)。优先Java闭卷复刷，原创迁移练习不计入75题。 [Java ArrayDeque文档](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/ArrayDeque.html)。

[课程目录](../README.md) · [每日安排](https://github.com/Desolate-Jix/learning-plan)
