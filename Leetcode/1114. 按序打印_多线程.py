# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/31 9:40
 @Author  : QDY
 @FileName: 1114. 按序打印_多线程.py
 @Software: PyCharm
"""
"""
    我们提供了一个类：

    public class Foo {
      public void one() { print("one"); }
      public void two() { print("two"); }
      public void three() { print("three"); }
    }
    三个不同的线程将会共用一个 Foo 实例。

    线程 A 将会调用 one() 方法
    线程 B 将会调用 two() 方法
    线程 C 将会调用 three() 方法
    请设计修改程序，以确保 two() 方法在 one() 方法之后被执行，three() 方法在 two() 方法之后被执行。

    示例 1:
    输入: [1,2,3]
    输出: "onetwothree"
    解释: 
    有三个线程会被异步启动。
    输入 [1,2,3] 表示线程 A 将会调用 one() 方法，线程 B 将会调用 two() 方法，线程 C 将会调用 three() 方法。
    正确的输出是 "onetwothree"。

    示例 2:
    输入: [1,3,2]
    输出: "onetwothree"
    解释: 
    输入 [1,3,2] 表示线程 A 将会调用 one() 方法，线程 B 将会调用 three() 方法，线程 C 将会调用 two() 方法。
    正确的输出是 "onetwothree"。


    注意:
    尽管输入中的数字似乎暗示了顺序，但是我们并不保证线程在操作系统中的调度顺序。
    你看到的输入格式主要是为了确保测试的全面性。

"""

from threading import Lock


class Foo:
    def __init__(self):  # 使用 synchronization
        # 初始化共享变量 firstJobDone 和 secondJobDone，初始值表示所有方法未执行
        self.firstJobDone = Lock()
        self.secondJobDone = Lock()
        self.firstJobDone.acquire()
        self.secondJobDone.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        # 通知正在等待第一个作业完成的线程。
        self.firstJobDone.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self.firstJobDone:
            printSecond()
            self.secondJobDone.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with self.secondJobDone:
            printThird()
