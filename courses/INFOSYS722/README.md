# INFOSYS 722：数据挖掘与大数据

**总体判断：**提供 Data Science／应用 ML 面试的流程、传统模型与评估基础。和 753 互补：722 侧重如何完成一次建模任务，753 侧重海量数据条件下的特定算法。

| 知识模块 | 核心概念 | 面试连接与适合整理的八股 |
|---|---|---|
| 问题与分析任务定义 | 决策支持、描述／诊断／预测／处方分析；分类、估计、关联、聚类；业务目标与分析目标 | 把业务问题转成标签、特征、目标变量和成功指标；避免为建模而建模 |
| 数据挖掘流程 | KDD、CRISP-DM、业务理解、数据理解／准备、建模、评估、应用；数据探索、缺失值和异常值 | 如何组织端到端 DS 项目；为什么模型训练只是其中一环 |
| 监督学习 | 回归／OLS、分类、决策树／规则、朴素贝叶斯、kNN、SVM、神经网络入门 | 算法适用条件、解释性、线性与非线性边界；旧 SPSS 讲义的工具细节不是当前全部 ML 工具链 |
| 无监督与关联规则 | K-means、层次／密度聚类类型、类内与类间质量；Apriori、support、confidence | 分类与聚类区别、如何选 k、规则的支持度和置信度；不可把关联当因果 |
| 泛化与评估 | 训练／验证／测试、参数与超参数、交叉验证、模型复杂度、过拟合／欠拟合、正则化；混淆矩阵、Precision／Recall、ROC／AUC、回归误差 | DS／AI 高价值八股；指标选择、评估设计与模型选择；后续补充实践时要专门检查数据泄漏 |
| 文本与流式数据 | 文本特征、停用词、文本分类、流数据窗口、实时采集 | 非结构化数据预处理、在线／离线数据差异；不能据此推断掌握 Transformer 训练 |
| 分析系统与模型管理 | DSS、模型库、模型／数据／求解器的分离；Lambda 架构、lakehouse、ML lifecycle／MLOps 概览 | 将模型接入实际系统、训练到使用的链路；讲座层面的概览与亲手部署要区分 |
| 研究与行业案例 | Design Science Research 的问题、artifact、评价；行业数据分析、医疗急救预测、数据叙事 | 论证方案是否解决问题、解释指标与业务结果；医疗案例来自 722 讲座，不能冒充 703 材料 |

**推荐作为八股主干：**监督／无监督、数据切分、交叉验证、过拟合／正则化、混淆矩阵、Precision／Recall、ROC／AUC、常见模型取舍、CRISP-DM。工具按钮操作和讲座公司背景低优先级。

**代表依据：**[F088：Data Mining Tasks](source/722/722%201/Data%2BMining%2BTasks%2B722%2BV3.pdf)；[F087：SPSS Workshop](source/722/722%201/Clementine%2BSPSS%2BModeller%2BWorkshop%2BV2.pdf)；[F089：Ying 讲座](source/722/722%201/INFOSYS%2B722%2BGuest%2BLecture_Ying.pdf)，第 3–63 页，尤其第 32–47 页评估部分；[F090：Models and Their Management](source/722/722%201/Models%2Band%2BTheir%2BManagement.pdf)；[F083：Design Science Research](source/722/722%201/722%2BDesign%2BScience%2BResearch%2B2025.pdf)；[F086：Real World 2025](source/722/722%201/Big%2BData%2BAnalytics%2B%2526%2BML%2Bin%2BReal%2BWorld%2B2025-10.pdf)。最后一份有字体编码异常，本轮采用图像核验补充判断，不根据乱码细化结论。


## 资料入口

[课程笔记入口](notes/README.md) · [课件目录](source/) · [总知识地图](../../docs/课程知识地图.md) · [复习路线](../../review-plan/roadmap.md)
