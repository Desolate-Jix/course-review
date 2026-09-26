# WEB｜HTML/CSS、浏览器、安全与构建

阶段：C｜前端/全栈专项。先修：NET、JS。

把页面的结构、布局、加载、安全和可访问性全部纳入，避免只背JavaScript。

本页为可直接复习的题目、答案要点与追问边界；首次遇到概念，先读资料并完成例子。它不等同于已编写完整教科书讲义，也不代表已经掌握。题量随覆盖缺口增长，不设上限。

|题号|问题|参考答案要点|追问与边界|
|---|---|---|---|
|WEB-01|语义化HTML与可访问性为什么重要？|使用正确标题层级、按钮/链接、表单label和替代文本，帮助键盘、读屏与文档结构理解。|可点击div等于button吗？不，焦点、键盘行为及语义需额外实现。|
|WEB-02|盒模型与box-sizing怎么影响宽度？|content-box的width通常只含内容，padding/border另加；border-box把它们计入指定宽度。|width100再加左右10padding和1border总宽多少？无其他约束时content-box122，border-box100。|
|WEB-03|CSS层叠、优先级和继承怎么判断？|先考虑来源/重要性与层等层叠规则，再比较选择器优先级和出现顺序；继承仅对可继承或显式继承属性适用。|后写一定覆盖先写吗？只有前面优先条件相同才按顺序判断。|
|WEB-04|Flex、Grid、定位与BFC各解决什么？|Flex偏一维布局，Grid偏二维；定位调整元素布局参照；BFC为特定块布局与浮动/外边距行为提供边界。|z-index很大还被遮住为什么？可能受父级层叠上下文约束，不能只增数字。|
|WEB-05|响应式布局怎样实现和验证？|结合弹性尺寸、断点、媒体查询与内容适配，检查小屏、缩放、长文本和触控目标。|只按设备型号写断点够吗？不，应按布局在内容下失效的位置设计。|
|WEB-06|DOM、CSSOM到布局绘制是什么过程？|解析构建相应结构，计算样式、布局几何，再绘制与合成；实现中可增量更新。|重排与重绘有什么区别？几何变化涉及布局，纯视觉变化可能只绘制；实际路径用性能工具看。|
|WEB-07|怎样避免布局抖动和长任务？|避免交替读取几何与写样式导致同步布局；批量更新，拆分耗时任务，对适合计算考虑Worker。|transform一定免费吗？不是，仍有合成、内存及设备成本。|
|WEB-08|捕获、冒泡与事件委托怎么用？|事件沿传播路径经历阶段；可在祖先处理子元素事件，结合target与currentTarget区分来源和监听位置。|preventDefault等于stopPropagation吗？不是，前者取消默认动作，后者影响传播。|
|WEB-09|同源策略和CORS是什么？|同源主要比较协议、主机、端口；CORS通过响应头允许浏览器跨源读取特定响应，部分请求需预检。|CORS是服务端鉴权吗？不是，非浏览器客户端不受同等限制，服务端仍需认证授权。|
|WEB-10|XSS与CSRF如何区别和防御？|XSS让攻击代码在站点上下文执行，需按输出上下文编码及安全DOM使用；CSRF利用浏览器自动带凭据发请求，需令牌、SameSite及来源检查等。|HttpOnly能消除XSS吗？不能，只限制脚本读取相应Cookie，脚本仍可能执行带凭据请求。|
|WEB-11|Cookie、localStorage、sessionStorage怎样取舍？|Cookie可随匹配请求发送并有安全属性；localStorage通常跨会话保存；sessionStorage按会话/标签页范围使用；容量与可访问性不同。|长期令牌放localStorage安全吗？可被同源脚本读取，必须评估XSS与令牌生命周期。|
|WEB-12|首屏与交互性能怎样量化？|按资源瀑布、LCP、INP、CLS及真实用户数据定位，采取图片优化、拆包、缓存、减少主线程工作。|本机Lighthouse一次满分能证明用户体验吗？不能，需设备网络与分布数据。|
|WEB-13|Tree shaking、代码拆分、source map有什么作用？|消除可判定未使用代码、按需加载模块、把构建产物映射回源码；效果依模块语义及副作用配置。|开发服务器启动快等于生产包小吗？不是，构建产物需独立分析；敏感源码映射应评估暴露范围。|

## 课堂验证

做一个有label的响应式搜索表单，用键盘完成操作；DevTools检查盒模型、慢网络瀑布和一次布局变化；画出带Cookie请求遭CSRF的路径及防护点。

**预期与判分：** 表单无需鼠标可用，小屏无关键内容溢出；能说明一次具体网络/渲染瓶颈，并区分CORS与鉴权。练习可分多课。

**英文关键词：** box model, layout, compositing, CORS, XSS, CSRF, code splitting。用“结论→机制→本例→边界”组织短答。

## 学习与复习

闭卷尝试→对照本表找缺口→完成验证→换场景追问→记录题号与证据。不能只因熟悉名词标为掌握。未覆盖题留在队列，复习使用原+1/+3/+7/+14节奏。项目联系只引用真实记录；本页练习应称课堂练习。

## 技术参考

- [MDN核心课程](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core)
- [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)
- [OWASP XSS](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [OWASP CSRF](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

[覆盖地图](../COVERAGE.md) · [总目录](../README.md)
