# Monitors-Additional.pdf — 逐页文本副本

- source 原文件路径：`courses/COMPSCI711/source/711/1/Monitors-Additional.pdf`
- [打开原文件](../../../../source/711/1/Monitors-Additional.pdf)
- 原文件 SHA-256：`71e6b6ed79c56c7e76be9995c4c6b9c2d02234c11ddc60fefc081665de5a5cf9`
- 文件索引：F053；PDF 总页数：15
- 页码采用 PDF 物理页码。原幻灯片编号作为原文保留，可能与物理页码不同。
- 此文件是原文提取，不是摘要。保留文字层全文；按需附坐标排版及本地 OCR。两种视图可能重复。
- OCR、数学符号和空间布局不保证完全准确；图示说明是另行标注的辅助文字，原 PDF 为准。

## PDF 第 1 页

[查看此页](../../../../source/711/1/Monitors-Additional.pdf#page=1)

### 原始文字层

````text
Example: Monitors
abstract class Monitor {
private:
 mutex m;
 condition_variable cv;
public:
 void Lock() { m.lock(); }
 void Unlock() { m.unlock(); }
 void Wait() { cv.wait(m); }
 void SignalOne() { cv.signal(); }
 void SignalAll() { cv.broadcast(); }
}
A monitor is a shared object. fdarenni Shared eject
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Example: Monitors
                               A monitor is a shared object.       Shared      eject
                                             fd           a           r      e           n           n           i
     abstract class Monitor {
     private:
        mutex m;
        condition_variable cv;
     public:
        void Lock()                  { m.lock(); }
        void Unlock()                { m.unlock(); }
        void Wait()                  { cv.wait(m); }
        void SignalOne()             { cv.signal(); }
        void SignalAll()             { cv.broadcast(); }
     }
````

### 图片文字 OCR（en-US，待对照原页）

````text
Example: Monitors
declare
A monitor is a shared object.
abstract class Monitor {
private :
mutex m;
condition variable cv;
Shared
object.
public:
void
void
void
void
void
Lock()
Unlock()
Wait()
SignalOne()
SignalA11()
m. lock();
m. unlock();
cv.wait(m);
cv.signal();
cv. broadcast();
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 2 页

[查看此页](../../../../source/711/1/Monitors-Additional.pdf#page=2)

### 原始文字层

````text
Example: Monitors
• A monitor class may derive from Monitor and use the Monitor
operations. 
• Alternatively, a monitor class could simply have a Monitor instance in 
the class and use the Monitor operations through this instance. BUT… 
• Having more than one Monitor instance may lead to incorrect usage, so 
derivation is a better approach than using an instance.
不敏创建关例
in
abstractclass
````

### 坐标排版辅助视图

> 尽量保留列、缩进和公式位置；此视图可能拆分上下标，不能替代上面的原始文字。

````text
Example: Monitors                                      不敏创建关例
                                            abstractclass
•A monitor class may derive from Monitor and use the Monitor
 operations.                   in
•Alternatively, a monitor class could simply  have a Monitor instance  in
 the class and use the Monitor operations  through this instance.  BUT…
   • Having more than one Monitor instance may lead to incorrect usage, so
     derivation is a better approach than using an instance.
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
ExampIe: Monitors
． A monitor class may derive fro m MO 忆 厂 and use the Mon 0 厂
operations.
． Alternatively, a monitor class could simply have a MO 厂 instance in
the class and use the MO 忆 厂 operations through this instance. BUT..
． Having m O re than O n e MO 冂 0 厂 instance may lead tO incorrect usage, SO
derivation is a better approach than using a n instance.
````

### 图片文字 OCR（en-US，待对照原页）

````text
Example: Monitors
quttnq Class,
' A monitor class may derive from Monitor and use the Monitor
operations.
• Alternatively, a monitor class could simply have a Monitor instance in
the class and use the Monitor operations through this instance. BUT...
• Having more than one Monitor instance may lead to incorrect usage, so
derivation is a better approach than using an instance.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 3 页

[查看此页](../../../../source/711/1/Monitors-Additional.pdf#page=3)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（en-US，待对照原页）

````text
Parallel Programming in C#
• We will look closely at the parallel programming features of C#
• C# has a reasonably long history, and these features grew and evolved
over the time.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 4 页

[查看此页](../../../../source/711/1/Monitors-Additional.pdf#page=4)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（en-US，待对照原页）

````text
13021638.110
Parallel Programming in C#
• We will look closely at the parallel programming features of C#
• C# has a reasonably long history, and these features grew and evolved
over the time.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 5 页

[查看此页](../../../../source/711/1/Monitors-Additional.pdf#page=5)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（en-US，待对照原页）

````text
130216-38110
Parallel Programming in C#
• A lot of the API is bundled up in the so-called Task Parallel Library
(TPL) that is part of the .NET framework. The goal of TPL is to simplify
writing parallel programs.
• While they are a higher level mechanisms to simplify writing parallel
programs, a good understanding of concepts underlying multi-
threaded programming (e.g., mutexes, condition variables, race
conditions, deadlocks, etc.) is necessary.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 6 页

[查看此页](../../../../source/711/1/Monitors-Additional.pdf#page=6)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（en-US，待对照原页）

````text
10
x
Parallel Programming in C# — A Big Toolset
Library: BackgroundWorker, Barrier, Interlocked,
Monitor, Mutex, ReaderWriterLock, Semaphore,
SemaphoreSlim, SpinLock, Spin Wait, Thread,
ThreadPool, ThreadStart, Parallel, Para//el.For,
Parallel.lnvoke, Task, Task. Wait, TaskFactory,
ValueTask, PLINQ, etc.
C# Keywords: async, await, lock, volatile
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 7 页

[查看此页](../../../../source/711/1/Monitors-Additional.pdf#page=7)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（en-US，待对照原页）

````text
'3.0216 M "0
Why so many?
• Some of the primitives are named so that they can be used inter-
process. Others are unnamed and therefore they can only be used
intra-process (i.e., between threads of the same process).
• Some primitives use spin waits (e.g., SemaphoreSlim) so they are
optimized for short wait times.
• Some are very specific (e.g., BackgroundWorker used in Ul, PL/NQ
used with queries).
• You need to know your toolset for the best use of the tools.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 8 页

[查看此页](../../../../source/711/1/Monitors-Additional.pdf#page=8)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（en-US，待对照原页）

````text
The volatile keyword
• The volatile keyword indicates that a field might be modified by
multiple threads that are executing at the same time.
• The compiler, the runtime system, and even hardware may rearrange
reads and writes to memory locations for performance reasons.
• Fields that are declared volatile are excluded from certain kinds of
optimizations.
• There is no guarantee of a single total ordering of volatile writes as
seen from all threads of execution.
Source: docs.microsoft.com
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 9 页

[查看此页](../../../../source/711/1/Monitors-Additional.pdf#page=9)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（en-US，待对照原页）

````text
10
The volatile keyword
• Volatile memory operations are for special cases of synchronization,
where normal locking is not an acceptable alternative.
• Under normal circumstances, the C# lock statement and the Monitor
class provide the easiest and least error-prone way of synchronizing
access to data.
Source: docs.microsoft.com
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 10 页

[查看此页](../../../../source/711/1/Monitors-Additional.pdf#page=10)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（en-US，待对照原页）

````text
130 2 'C
The lock keyword
• The lock statement acquires the mutual-exclusion lock for a given
object, executes a statement block, and then releases the lock.
• Any other thread is blocked from acquiring the lock and waits until
the lock is released.
Source: docs.microsoft.com
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 11 页

[查看此页](../../../../source/711/1/Monitors-Additional.pdf#page=11)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（en-US，待对照原页）

````text
The lock keyword
lock (x)
// Your code...
Note: x above must be a reference type; typically we use an
object. This object might be this.
130.2
object _lockObj = x;
bool lockWasTaken = false;
try
Monitor.Enter(_lockObj, ref
// Your code...
finally
if ClockWasTaken)
Monitor.Exit(_lockObj);
lockWasTaken);
Source: docs.microsoft.com
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 12 页

[查看此页](../../../../source/711/1/Monitors-Additional.pdf#page=12)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（en-US，待对照原页）

````text
Task
• Task represents an asynchronous operation. It comes in two flavours:
Tasl< that does not return a value, and Task<TResu1t> which
returns a value (of type T Result).
• The most important (static) method of the Task is Run which points to
a function that specifies the work to run on the ThreadPool and
returns a Task or Task<TResult> handle for that work.
The return handle allows us to wait for the task's completion and to
consume results.
Task. Run (DoSomeLongJob);
= > 42));
Task. Run(()
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 13 页

[查看此页](../../../../source/711/1/Monitors-Additional.pdf#page=13)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（en-US，待对照原页）

````text
The async l<eyword
e Use the async modifier to specify that a method, lambda expression,
or anonymous method is asynchronous.
• If you use this modifier on a method or expression, it's referred to as
an async method.
An async method runs synchronously until it reaches its first await
expression, at which point the method is suspended until the awaited
task is complete.
o In the meantime, control returns to the caller of the method.
Source- docs mtcrosoft.com
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 14 页

[查看此页](../../../../source/711/1/Monitors-Additional.pdf#page=14)

### 原始文字层

````text
配合 task 使用
task its task2
等待时挂起 执行
其它程序集成后返回
await
````

### 图片文字 OCR（zh-Hans-CN，待对照原页）

````text
Async/Awa it
public static async Task Main()
Task<int 〉 downloading = Down10adDocsMainPageAsync();
Cons01e.WriteLine($"Launched downloading. “ ） ；
int bytesLoaded
await downloading;
Cons01e.WriteLine "Down10aded {bytesLoaded} bytes.");
private static async Task 〈 int> DownIoadDocsMainPageAsync()
Cons01e.WriteLine($"About t0 start downloading. “ ） ；
new HttpCIient();
var client
byte[] content
await c1ient.GetByteArrayAsync("https://docs
Cons01e.WriteLine($"Finished downloading. " );
return content.Length;
05 ）
About t 0 s t a r t d 10 d 1 n g ．
L a u n c e d d 0 n 10 a d i n g ．
F i n i s h e d d ： m102d 文 巳 ，
D 0 訶 n I O a d e d × × × × × b y e 3 ．
````

### 图片文字 OCR（en-US，待对照原页）

````text
O
X
Async/Await
public static async Task Main()
Task )
Task<int> downloading = DownloadDocsMainPageAsync();
Console.WriteLine($"Launched downloading. " ) ;
int bytesLoaded =
await downloading;
Console. WriteLine "Downloaded {bytesLoaded} bytes. " ) ;
private static async Task<int> DownloadDocsMainPageAsync()
Console.WriteLine($"About to start downloading. " ) ;
= new HttpC1ient();
var client
byte[] content =
await client.GetByteArrayAsync("https://docs . microsoft . com/en-us/");
Console. WriteLine($"Finished downloading.
return content. Length;
DD6 '*J?)
-tas
fffj
About to start do.unloading.
Launched donnloading.
Finished
Downloaded XXXX X bytes.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

## PDF 第 15 页

[查看此页](../../../../source/711/1/Monitors-Additional.pdf#page=15)

> 本页无可提取文字层；见 OCR 或图示说明。

### 图片文字 OCR（en-US，待对照原页）

````text
Further Work
• Go through the parallel programming documentation at Microsoft
online.
• Compile and run the async/await example. Make sure you understand
the logic and control flow.
````

> 图形提示：本页含图像或矢量图形。可提取标签保留在上方；箭头、颜色、连线、几何位置请对照原页。

