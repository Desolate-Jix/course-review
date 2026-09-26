# ALG04｜面试八股与追问

配套[课程讲义](../lessons/ALG04.md)。先学机制、做例题，再使用本页整理面试表达。下面是参考答案，需用自己的话回答；背出文字不代表通过独立练习。

## 本节必练

每次从下面两题选一题：先30–60秒给直接答案，再用1–2分钟补机制、例子与边界，最后回答追问。第二次学习/复习换另一题，不能永远只练熟悉题。

## Q1：二分查找需要什么前提？怎样避免死循环和边界错误？

**中文参考回答：** 需要有序性或可划分的单调条件，使一次比较能排除一半候选。选定闭区间或半开区间并保持一致，更新后候选范围必须缩小。lowerBound的[left,right)中，nums[mid]<target时left=mid+1，否则right=mid。

**英文回答提纲：** Binary search needs an ordered space or a monotonic condition. Keep one interval convention and ensure every update shrinks the candidate range.

**继续追问：** 为什么不满足条件时不能写left=mid？

**追问要点：** 两元素范围可能算出mid=left，更新后区间不变导致死循环；已经排除mid就应跳过它。

**常见失分：** 不要混用闭区间的right=mid-1与半开区间的终止规则。

## Q2：普通查找与lowerBound有什么区别？怎样处理重复和不存在？

**中文参考回答：** 普通查找可返回某个匹配，lowerBound返回第一个大于等于目标的位置，不存在返回n。对[1,2,2,4]查2返回1，查5返回4。用结果判断存在性时先检查i<n，再读nums[i]，避免越界。

**英文回答提纲：** Lower bound returns the first position whose value is at least the target, or the array length if none exists. Check the returned index before accessing the array.

**继续追问：** 空数组返回什么？中点为什么常写left+(right-left)/2？

**追问要点：** 空数组返回0；该中点写法在本课非负下标范围内避免left+right相加溢出。

**常见失分：** 不要把返回n当成找到下标n的元素，也不要忽略重复值时的最左位置要求。

## 联系自己的经历

可解释配置阈值搜索与单调前提；未经验证的模型分数变化不能假定一定单调。

## 15分钟课堂使用方式

- 3分钟：关闭答案，回答一题。
- 5分钟：用本节数据/代码补例子，接受一轮追问或反例。
- 4分钟：核对遗漏和错误，修改自己的提纲。
- 3分钟：用英语复述核心答案；保留不会说的关键词。

不额外延长学习日。实作仍在原练习时段完成，本页口述不能取代SQL/代码与结果验证。

## 记录

在学习仓库当天唯一笔记写：题号、自己的回答要点、追问结果、错误理解、英文卡词、下次复习时间。技术理解与英文流畅度分开记录，不创建一套与课程等级相矛盾的“背诵等级”。

[八股总目录](README.md) · [课程验收标准](../ASSESSMENT.md)。技术依据见配套讲义的资料章节。
