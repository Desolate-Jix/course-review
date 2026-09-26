# ALG01｜答案与判分要点

先完成[本节练习](../lessons/ALG01.md)。答案供核对，不代表唯一正确写法。


```java
static int removeValue(int[] nums, int x) {
    int write = 0;
    for (int read = 0; read < nums.length; read++) {
        if (nums[read] != x) nums[write++] = nums[read];
    }
    return write;
}
```

变式O(n)时间/O(1)空间；解释 `[0,write)` 的含义。283先收集非0再补0即可。测试结果分别[]、[0,0]、[1,2]、[1,3,12,0,0]。

若旧题能独立通过且变式正确，可缩短讲解，把时间转给薄弱模块；无需重新刷满时间。


看过答案的题记为“有提示”；隔日换数据独立重做，再决定是否达到B。
