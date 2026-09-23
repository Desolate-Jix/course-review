# COMPSCI 711：并行与分布式计算

**总体判断：**内容同时涉及单机并行／硬件性能和分布式协调。适合后端、系统、基础设施面试，也能支撑数据平台与 AI 服务的可靠性讨论。

| 知识模块 | 核心概念 | 面试连接与适合整理的八股 |
|---|---|---|
| 并行体系结构 | 处理器执行、流水线、超标量、指令级并行、Cache、局部性、多处理器缓存一致性 | 性能瓶颈、为什么并行不等于线性加速；缓存与内存访问成本；硬件 Cache 与 Web cache 要区分 |
| 进程、线程与同步 | 进程／线程、共享状态、互斥、monitor、条件变量、等待与唤醒 | 进程和线程区别、竞态、临界区、互斥与条件同步；能解释代码为什么需要同步 |
| 分布式时间与消息顺序 | happens-before、Lamport 时间戳、向量时钟、偏序／全序；FIFO／因果／全序多播、可靠多播、虚拟同步 | 事件顺序不等于墙上时间；如何判断并发；消息按何种规则交付；全序与因果序的区别 |
| 分布式互斥与死锁 | 安全性、活性、公平性；集中式、Ricart–Agrawala、Maekawa quorum、Raymond token；wait-for graph、AND／OR 死锁、Echo | 单点故障、消息开销、仲裁集合、分布式锁取舍；死锁检测和普通可串行化冲突图不能混为一谈 |
| 全局状态与分布式回收 | Chandy–Lamport snapshot、进程状态、通道中消息、一致切面；引用计数、加权引用计数、循环引用 | 一致快照／检查点的基础；为什么局部状态拼起来未必是一致的全局状态；分布式对象生命周期 |
| 共识、复制与一致性 | 共识问题、FLP、Paxos、多数派；强／弱／最终一致性、CAP、BASE、分区与副本冲突 | 网络分区下的选择、复制系统如何达成一致；共识和事务提交问题的区别；2PC／3PC 在复习题材料中出现 |
| Web 缓存与网络实践 | 缓存命中、过期内容、缓存粒度；C# 网络中间件、TCP、异步收发 | 系统设计中的缓存有效性；客户端／服务端消息流、并发连接与故障处理 |

**推荐作为八股主干：**进程／线程与同步、逻辑时钟、消息有序性、CAP 与一致性、Paxos 基本机制、死锁、缓存。分布式 GC 和特定互斥算法的逐步证明为较低优先级专题。

**代表依据：**[F076：Threads & Processes](source/711/1/Threads%2B%2526%2BProcesses.pdf)；[F053：Monitors](source/711/1/Monitors-Additional.pdf)；[F045：711（1）](source/711/1/711%20%EF%BC%881%EF%BC%89.pdf)与[F041：711 2](source/711/1/711%202.pdf)的图片笔记；[F043：多播](source/711/1/711%203.pdf)，第 7–92 页；[F037：3.19 分布式互斥](source/711/1/3.19.pdf)；[F068：snapshot](source/711/1/S7%2Bsnapshot%20%282%29.pdf)；[F072：Paxos](source/711/1/S8%2Bpaxos.pdf)；[F074：Consistency and CAP](source/711/1/S9%2BnoSQL.pdf)；[F054：多处理器 Cache](source/711/1/Multiprocessor%2BCaches.pdf)；[F330：根目录 midblock review](source/midblock%20review.pdf)。

**项目材料边界：**[F058：PRESENTATION](source/711/1/PRESENTATION.pdf)自述 C# 多线程 Chess server、TCP／HTTP1.1 和 JavaScript 客户端，可用作项目回忆线索；这份自我介绍不等于代码或验收证据。711 目录里的数字钱包展示属于 700 主题，722 反馈属于 722，不计入 711 的授课范围。


## 资料入口

[课程笔记入口](notes/README.md) · [原始文件目录](source/) · [总知识地图](../../docs/课程知识地图.md) · [复习路线](../../review-plan/roadmap.md)
