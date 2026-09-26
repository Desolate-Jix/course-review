# 共用练习数据与运行方式

DB01–DB06 使用同一套用户和订单数据。SQL答案按 PostgreSQL 语义讲解；这些基础查询也在 Python 标准库 SQLite 中核对。DB07 的执行计划和 DB08 的隔离实验必须使用 PostgreSQL，不能拿SQLite输出替代。

## 表与数据

users 每行代表一个用户；orders 每行代表一个订单。金额为整数练习单位，避免引入浮点货币误差。

| users.id | name | city |
|---|---|---|
|1|小王|Auckland|
|2|小李|Wellington|
|3|小张|NULL|
|4|小王|Auckland|

| orders.id | user_id | amount | status |
|---|---|---|---|
|101|1|100|paid|
|102|1|200|pending|
|103|2|50|paid|
|104|4|0|cancelled|
|105|1|100|paid|

## 不安装数据库也能先学基础SQL

在仓库根目录，把查询保存为例如 `query.sql`，执行：

```bash
python curriculum/labs/run_sql.py query.sql
```

每次启动创建全新的内存练习库，加载 [seed.sql](seed.sql)。脚本逐条打印查询列名和结果，不保留修改。Python用 `python` 或机器上对应的 `python3` 命令。

## PostgreSQL 实验

使用自己的空练习数据库，先执行 `seed.sql`。DB07 有独立的TEMP表实验；DB08 使用TEMP账户表和两会话演示步骤。无需升级已有兼容版本，讲义以 PostgreSQL 18 官方文档核对。

SQL查询与约束没有ORDER BY时，不承诺输出次序。核对结果应看行集合；要求稳定顺序的练习明确写ORDER BY。

没有 PostgreSQL 环境时，先完成手算和SQL部分，把“数据库机制实测”记为待完成；不能把阅读示例输出登记为已实测。
