# COMPSCI 753：海量数据算法

**总体判断：**这是大规模检索、推荐与数据摘要的算法课程，不应把它简单命名为“深度学习课”。很多概念可用于 AI 工程，但完整现代 LLM 训练栈并非已确认的课程模块。

| 知识模块 | 核心概念 | 面试连接与适合整理的八股 |
|---|---|---|
| 数学与随机算法基础 | 向量／矩阵、特征值／特征向量、概率与期望；Monte Carlo／Las Vegas、随机化、通用哈希 | 复杂度与概率保证；哈希碰撞；精确性、速度、空间之间的选择 |
| Web 与大图分析 | 随机游走、PageRank、迭代计算、图结构 | 排序／图分析；解释 PageRank 的直觉、迭代和特殊节点处理 |
| 社区检测与影响力 | 边介数、Brandes、Girvan–Newman、谱聚类、modularity；影响传播与影响力最大化 | 图数据科学、社交网络分析；偏专题，通常晚于通用 ML／SQL |
| 相似搜索与 LSH | shingles、Jaccard、MinHash、签名、banding；距离／相似度、局部敏感哈希、近似近邻 | 大规模去重、候选召回；为什么 LSH 与普通哈希目标不同；banding 如何影响误报／漏报 |
| 流式抽样和过滤 | 固定比例抽样、reservoir sampling、Bloom filter、空间与误报率 | 海量日志采样、成员查询、内存约束；适合小型算法题与原理题 |
| 重频项与频率摘要 | Misra–Gries、Count-Min Sketch、Count Sketch、哈希桶、符号哈希、误差方向／概率界 | 热点统计、近似聚合；三种摘要的估算方式、误差与空间代价 |
| 推荐系统基础与评估 | 内容推荐、用户／物品协同过滤、相似度和插值权重、稀疏性、冷启动；RMSE、Precision@N、Recall@N、排名评估 | 推荐／搜索岗位核心；评分预测与 Top-N 排序不是同一个目标 |
| 潜因子与进阶推荐 | 低秩潜因子、矩阵分解、偏置项、正则化、SGD；上下文／session 推荐、张量分解、Factorization Machines | 推荐建模、过拟合、特征交互；进阶部分优先服务推荐岗位，不泛化成“已学完神经推荐” |

**推荐作为八股主干：**Bloom／reservoir → MinHash／LSH → Sketch 比较 → 协同过滤／矩阵分解／冷启动／评估。PageRank 次之；谱聚类、影响力最大化和张量分解按目标岗位深入。

**代表依据：**[F240：课程介绍](source/753/W1%2B-%2BIntro%2B%2526%2BAdmin.pdf)；[F235：Tutorial 1](source/753/2025_S2_CS752_Tut1_Q.pdf)文件名虽写 CS752，正文明确为 COMPSCI 753；[F255：LSH I](source/753/W5.1%2B-%2BLSH%2BAllPairs%2BI.pdf)；[F258：LSH III](source/753/W6%2B-%2BrNNS.pdf)；[F262：CountMinSketch](source/753/W8.1_Stream%2BCountMin%2BSketch.pdf)；[F263：Count Sketch](source/753/W8.2_Stream%2BCount%2BSketch.pdf)；[F264：推荐基础](source/753/W9.1%2B-%2BBasics%2Bof%2BRecommender%2BSystems.pdf)；[F244：潜因子](source/753/W10.1%2B-%2BLatent%2BFactor%2BModel%20%282%29.pdf)；[F246：进阶推荐](source/753/W10.2%2B-%2BAdvanced%2Btopics%2Bof%2BRS.pdf)。[F267：10 月 29 日](notes/original/753/%E7%AC%94%E8%AE%B0%202025%E5%B9%B410%E6%9C%8829%E6%97%A5.pdf)和[F268：10 月 30 日](notes/original/753/%E7%AC%94%E8%AE%B0%202025%E5%B9%B410%E6%9C%8830%E6%97%A5.pdf)是算法复习笔记，而不是可忽略的日期文件。


## 资料入口

[课程笔记入口](notes/README.md) · [课件目录](source/) · [总知识地图](../../docs/课程知识地图.md) · [复习路线](../../review-plan/roadmap.md)
