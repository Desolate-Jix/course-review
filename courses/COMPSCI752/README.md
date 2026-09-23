# COMPSCI 752：大数据管理

**总体判断：**重点是数据如何表示、查询、采集、处理与保护。与 751 相比，更多是半结构化／图数据和大规模处理；与 753 相比，更侧重数据管理流程。

| 知识模块 | 核心概念 | 面试连接与适合整理的八股 |
|---|---|---|
| 半结构化数据 | XML 树、元素／属性、类型与 schema；XPath 轴、路径、谓词；XQuery 序列模型、FLWOR | 数据格式、树状数据查询、声明式查询；XML 细节在特定企业集成岗位价值较高 |
| 图模型与图查询 | Property Graph、RDF 三元组、图模型扩展；Cypher／Neo4j、SPARQL、路径表达式、RPQ／CRPQ、查询逻辑与代数 | 关系库与图数据库选型；节点、边、属性、路径；知识关系查询；适合图检索与知识库岗位 |
| 知识图谱 | 实体、关系、知识抽取／整合、构建流程、质量与挑战 | AI 数据层、结构化知识、实体关系管理；可以衔接知识增强应用，但不据此宣称学过完整 RAG 系统 |
| Web 数据获取与清洗 | 爬取、近重复检测、文本表示、TF-IDF、相似度、similarity join、搜索与 PageRank | 数据采集与去重、文档检索、数据质量；也可作为 AI 语料准备的基础 |
| 分布式批处理 | Map、Shuffle、Reduce；HDFS、Hadoop、Spark；MapReduce 版 PageRank／相似连接 | 数据工程流水线、分组聚合、数据分区与移动成本；区分框架原理和实际部署经验 |
| 数据流与有限内存 | 数据流模型、固定比例／reservoir 抽样、Bloom filter、Misra–Gries heavy hitters | 无法保存全量数据时如何抽样、去重或估算热点；与 753 合并复习避免重复 |
| 差分隐私 | 匿名化的局限、相邻数据集、隐私参数、敏感度、噪声机制、隐私与效用取舍 | DS／AI 数据治理、为什么“删姓名”不充分、发布统计信息的边界；本轮不提供合规结论 |

**推荐作为八股主干：**MapReduce／Shuffle、HDFS 基础、图数据模型与 Cypher／SPARQL、去重与相似度、reservoir、Bloom filter、差分隐私直觉。RPQ 系列形式语言和 XML 全部语法作为岗位相关专题。

**代表依据：**[F203：752 2 XML](notes/original/752/752%EF%BC%881%EF%BC%89/752%202.pdf)；[F205：752-3 XPath](notes/original/752/752%EF%BC%881%EF%BC%89/752-3.pdf)；[F219：XQuery](notes/original/752/752%EF%BC%881%EF%BC%89/slxquery.pdf)；[F211：graph-models](notes/original/752/752%EF%BC%881%EF%BC%89/graph-models.pdf)；[F213：graph_queries_2025](notes/original/752/752%EF%BC%881%EF%BC%89/graph_queries_2025.pdf)；[F214：Knowledge Graph](source/752/752%EF%BC%881%EF%BC%89/KG_1253%20%282%29.pdf)；[F199：Data Cleaning](source/752/752%EF%BC%881%EF%BC%89/1253_Data_Cleaning.pdf)；[F216：MapReduce Framework](source/752/752%EF%BC%881%EF%BC%89/MapReduce%2BFramework.pdf)；[F220：Differential Privacy](source/752/752%EF%BC%881%EF%BC%89/W10_Differential%2BPrivacy%20%282%29.pdf)；[F227：复习笔记.docx](notes/original/752/752%EF%BC%881%EF%BC%89/%E5%A4%8D%E4%B9%A0%E7%AC%94%E8%AE%B0.docx)。图片式日期笔记中，[F231：5 月 20 日](notes/original/752/752%EF%BC%881%EF%BC%89/%E7%AC%94%E8%AE%B0%202025%E5%B9%B45%E6%9C%8820%E6%97%A5.pdf)是差分隐私，[F233：6 月 3 日](notes/original/752/752%EF%BC%881%EF%BC%89/%E7%AC%94%E8%AE%B0%202025%E5%B9%B46%E6%9C%883%E6%97%A5.pdf)是流处理与隐私考前练习。


## 资料入口

[课程笔记入口](notes/README.md) · [课件目录](source/) · [总知识地图](../../docs/课程知识地图.md) · [复习路线](../../review-plan/roadmap.md)


## 逐页原文

[extracted 文本副本与原件对照](extracted/README.md) · [提取方法与局限](../../docs/课件文本提取说明.md)

保留 PDF 页码、原文字层和 OCR，供搜索与回溯课件使用；与上方课程大纲分开维护。
