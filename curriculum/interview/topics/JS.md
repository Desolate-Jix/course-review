# JS｜JavaScript与TypeScript

阶段：C｜前端/全栈专项。先修：主语言函数与引用；NET入门。

先熟悉语言机制，再学习React，避免把框架行为误认为语言规则。

本页为可直接复习的题目、答案要点与追问边界；首次遇到概念，先读资料并完成例子。它不等同于已编写完整教科书讲义，也不代表已经掌握。题量随覆盖缺口增长，不设上限。

|题号|问题|参考答案要点|追问与边界|
|---|---|---|---|
|JS-01|var、let、const与提升有什么区别？|var常为函数作用域并在初始化前可读到undefined；let/const为块作用域并有暂时性死区；const限制绑定重赋值。|const对象能修改属性吗？能，绑定不变不等于对象深度不可变。|
|JS-02|作用域链与闭包有什么用和风险？|函数可访问创建时词法环境中的绑定；可用于封装与回调，也可能保留不再需要的对象。|闭包一定导致泄漏吗？不是，关键在引用是否仍可达和是否不再需要。|
|JS-03|普通函数与箭头函数的this怎样决定？|普通函数this依调用方式；箭头函数从外层词法环境捕获this，没有自己的动态this。|call/bind能改变箭头函数捕获的this吗？不能按普通函数方式重绑。|
|JS-04|原型链、prototype、class是什么关系？|对象通过内部原型链查找属性；构造函数prototype常用于新实例原型；class提供基于原型机制的语法与语义。|实例找不到属性会怎样？逐级查找直到链尾；不是复制所有父属性到实例。|
|JS-05|==、===、Object.is怎样区别？|==可类型转换；===通常不转换但NaN不等于自身、正负零相等；Object.is对NaN和正负零有不同规则。|两个相同内容对象===吗？不是，引用不同即不等。|
|JS-06|浅复制、深复制和JSON复制有哪些边界？|展开与Object.assign只复制一层；深复制需定义类型、循环引用与身份关系；JSON序列化会丢失或改变部分类型且不支持任意对象图。|structuredClone能复制函数吗？不能把它视作万能克隆器。|
|JS-07|浏览器事件循环、任务与微任务如何排序？|同步调用栈先运行完；在相应检查点清空微任务，再有机会处理后续任务与渲染。Promise回调通常进微任务队列。|无限递归排微任务有何风险？可能饿死后续任务和渲染。|
|JS-08|Promise状态与链式错误传播怎样工作？|Promise从pending进入fulfilled或rejected后不再改变；then返回新Promise，返回值/抛异常决定后续链结果。|catch里不重新抛出意味着什么？可能把失败恢复成成功值，不能误以为错误仍在传播。|
|JS-09|async/await与Promise.all/allSettled怎样选？|async返回Promise，await使当前异步函数挂起；all遇拒绝使组合拒绝，allSettled收集所有结果。|all失败后其他任务自动取消吗？不会，需额外取消机制。|
|JS-10|防抖与节流怎么区别？|防抖把密集触发合并到停止一段时间后；节流限制一段时间的触发频率，首尾行为需明确定义。|卸载组件时要做什么？清定时器或取消待处理回调，防止过期操作。|
|JS-11|ES模块、CommonJS与打包有什么关系？|ES模块提供静态import/export语义；CommonJS常用require/module.exports；构建工具处理依赖、转换与资源输出。|模块化等于所有代码都进首屏包吗？不，可按动态导入拆分。|
|JS-12|TS的any、unknown、never怎样选？|any绕过类型检查；unknown要求缩窄后使用；never表示不可能值或不返回的路径。|把接口响应as某类型就验证了吗？没有，类型断言不做运行时校验。|
|JS-13|联合类型、类型守卫与泛型解决什么？|联合表示多种可能，守卫缩窄分支，泛型表达输入输出之间的类型关系，减少any丢失信息。|泛型能保证业务规则正确吗？不能，例如金额非负仍需运行时约束。|
|JS-14|interface与type有什么区别？|两者都可描述对象形状；type还能表示联合等别名，interface支持声明合并等能力，选择依需求与团队约定。|类型系统是否名义上同名才兼容？TS多数场景按结构兼容，但存在私有成员等边界。|

## 课堂验证

手推并运行：同步打印A、排setTimeout打印B、Promise.then打印C、同步打印D；再写有取消能力的防抖函数，用unknown解析外部JSON并缩窄。

**预期与判分：** 常规浏览器此例输出A D C B。防抖需验证连续调用、最后参数、this及取消；JSON缺字段应被拒绝，不能靠as跳过。

**英文关键词：** closure, prototype chain, microtask, type narrowing, generics。用“结论→机制→本例→边界”组织短答。

## 学习与复习

闭卷尝试→对照本表找缺口→完成验证→换场景追问→记录题号与证据。不能只因熟悉名词标为掌握。未覆盖题留在队列，复习使用原+1/+3/+7/+14节奏。项目联系只引用真实记录；本页练习应称课堂练习。

## 技术参考

- [JS指南](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
- [执行模型](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Execution_model)
- [类型缩窄](https://www.typescriptlang.org/docs/handbook/2/narrowing.html)
- [泛型](https://www.typescriptlang.org/docs/handbook/2/generics.html)

[覆盖地图](../COVERAGE.md) · [总目录](../README.md)
