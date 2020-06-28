# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/28 15:00
 @Author  : QDY
 @FileName: 295. 数据流的中位数_堆_hard.py

    中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

    例如，
    [2,3,4] 的中位数是 3
    [2,3] 的中位数是 (2 + 3) / 2 = 2.5
    设计一个支持以下两种操作的数据结构：

    void addNum(int num) - 从数据流中添加一个整数到数据结构中。
    double findMedian() - 返回目前所有元素的中位数。

    示例：
    addNum(1)
    addNum(2)
    findMedian() -> 1.5
    addNum(3)
    findMedian() -> 2

    进阶:
    如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
    如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？

"""
import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []  # 大根堆
        self.right = []  # 小根堆

    def heapify_left(self, i):  # 维护大根堆
        n = len(self.left)
        if i >= n or n <= 1: return
        largest = i
        l, r = i * 2 + 1, i * 2 + 2
        if l < n and self.left[l] > self.left[largest]:
            largest = l
        if r < n and self.left[r] > self.left[largest]:
            largest = r
        if largest != i:
            self.left[largest], self.left[i] = self.left[i], self.left[largest]
            self.heapify_left(largest)

    def heapify_right(self, i):  # 维护小根堆
        n = len(self.right)
        if i >= n or n <= 1: return
        smallest = i
        l, r = i * 2 + 1, i * 2 + 2
        if l < n and self.right[l] < self.right[smallest]:
            smallest = l
        if r < n and self.right[r] < self.right[smallest]:
            smallest = r
        if smallest != i:
            self.right[smallest], self.right[i] = self.right[i], self.right[smallest]
            self.heapify_right(smallest)

    def left_add(self, num):
        self.left.append(num)
        son = len(self.left) - 1
        pa = (son - 1) // 2
        while pa >= 0 and self.left[pa] < self.left[son]:  # 上浮
            self.left[pa], self.left[son] = self.left[son], self.left[pa]
            pa, son = (pa - 1) // 2, pa

    def right_add(self, num):
        self.right.append(num)
        son = len(self.right) - 1
        pa = (son - 1) // 2
        while pa >= 0 and self.right[pa] > self.right[son]:  # 上浮
            self.right[pa], self.right[son] = self.right[son], self.right[pa]
            pa, son = (pa - 1) // 2, pa

    def addNum(self, num: int) -> None:
        if not self.left:
            self.left.append(num)
            # heapq.heappush(self.left,-num)
        elif len(self.left) == len(self.right):
            if num < self.right[0]:  # num添加到左边
                self.left_add(num)
                # heapq.heappush(self.left,-num)
            else:  # self.right[0]加到左边，num加到右边
                self.left_add(self.right[0])
                self.right[0] = num
                self.heapify_right(0)
                # heapq.heappush(self.left,-self.right[0])
                # self.right[0] = num
                # heapq.heapify(self.right)
        else:
            if num >= self.left[0]:
                # if num>= -self.left[0]:
                self.right_add(num)
                # heapq.heappush(self.right,num)
            else:
                self.right_add(self.left[0])
                self.left[0] = num
                self.heapify_left(0)
                # heapq.heappush(self.right,-self.left[0])
                # self.left[0] = -num
                # heapq.heapify(self.left)

    def findMedian(self) -> float:
        # print(self.left,self.right)
        if len(self.left) == len(self.right):
            return (self.left[0] + self.right[0]) / 2
            # return (-self.left[0]+self.right[0])/2
        else:
            return self.left[0]
            # return -self.left[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
