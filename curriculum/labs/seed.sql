-- 在新的练习数据库运行一次；重复练习请创建新数据库。
CREATE TABLE users (
 id INTEGER PRIMARY KEY,
 name TEXT NOT NULL,
 city TEXT
);
CREATE TABLE orders (
 id INTEGER PRIMARY KEY,
 user_id INTEGER NOT NULL REFERENCES users(id),
 amount INTEGER NOT NULL CHECK(amount >= 0),
 status TEXT NOT NULL CHECK(status IN ('paid','pending','cancelled'))
);
INSERT INTO users VALUES (1,'小王','Auckland'),(2,'小李','Wellington'),(3,'小张',NULL),(4,'小王','Auckland');
INSERT INTO orders VALUES (101,1,100,'paid'),(102,1,200,'pending'),(103,2,50,'paid'),(104,4,0,'cancelled'),(105,1,100,'paid');
