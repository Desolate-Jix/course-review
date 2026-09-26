# ALG04｜有序性、二分与边界

先修：ALG01。先修待验证时先做前节验收；通过可跳过重复讲解。

## 学完要能做到

独立实现半开区间二分，解释每个边界更新以及终止条件，覆盖重复与空输入。

## 讲解与例题


### 1. 二分需要可排除的一半

二分依赖有序性或单调谓词。旧题374 Guess Number Higher or Lower中，每次反馈能排除一边。中点用 `left + (right-left)/2` 避免在正数边界下left+right溢出。

### 2. 用统一区间表达边界

原创练习lowerBound：有序数组中第一个>=target的位置，不存在则返回n。采用半开区间 `[left,right)`，初始0,n：

```java
while (left < right) {
    int mid = left + (right - left) / 2;
    if (nums[mid] < target) left = mid + 1;
    else right = mid;
}
return left;
```

mid位置不满足就连同左半边排除；mid满足则它仍可能是第一个，所以不能改成right=mid-1。始终保证答案位于候选边界范围，left==right时完成。

### 3. 重复值暴露错误

对 `[1,2,2,4]`,target=2，返回1而不是任意一个2；target=3返回3；target=5返回4。空数组返回0。每步候选范围至少缩小，约log₂n次，额外空间O(1)。


## 独立练习


1. 先解释旧题374反馈方向；如不熟先闭卷复刷。
2. Java独立写lowerBound，覆盖空数组、重复值、目标小于最小和大于最大。
3. 原创变式：用lowerBound判断某个值是否存在，注意返回n时不能访问nums[n]。
4. 构造修改成left=mid后可能无法结束的两元素例子。


先写自己的解答，记录用过哪些提示，再打开[答案与判分要点](../answers/ALG04.md)。

## 验收与复习

完成独立题后，按[统一标准](../ASSESSMENT.md)评估。必须处理题目中的边界或变式；刚看完答案的重写不能算独立通过。用自己的话解释一个机制，再用英语说一个60秒摘要。当前不会的内容回到本节具体小点补学。

独立实现半开区间二分，解释每个边界更新以及终止条件，覆盖重复与空输入。

## 资料

[已有24题及代码笔记](https://github.com/Desolate-Jix/learning-plan/blob/main/STUDY_PROGRESS.md)；[LeetCode 75题单](https://github.com/Desolate-Jix/learning-plan/blob/main/LEETCODE_75_CHECKLIST.md)。优先Java闭卷复刷，原创迁移练习不计入75题。

[课程目录](../README.md) · [每日安排](https://github.com/Desolate-Jix/learning-plan)
