# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/29 20:52
 @Author  : QDY
 @FileName: 715. Range 模块.py
 @Software: PyCharm
"""
"""
    Range 模块是跟踪数字范围的模块。你的任务是以一种有效的方式设计和实现以下接口。
    addRange(int left, int right) 添加半开区间 [left, right)，跟踪该区间中的每个实数。
    添加与当前跟踪的数字部分重叠的区间时，应当添加在区间 [left, right) 中尚未跟踪的任何数字到该区间中。
    queryRange(int left, int right) 只有在当前正在跟踪区间 [left, right) 中的每一个实数时，才返回 true。
    removeRange(int left, int right) 停止跟踪区间 [left, right) 中当前正在跟踪的每个实数。
     

    示例：
    addRange(10, 20): null
    removeRange(14, 16): null
    queryRange(10, 14): true （区间 [10, 14) 中的每个数都正在被跟踪）
    queryRange(13, 15): false （未跟踪区间 [13, 15) 中像 14, 14.03, 14.17 这样的数字）
    queryRange(16, 17): true （尽管执行了删除操作，区间 [16, 17) 中的数字 16 仍然会被跟踪）
     
    提示：
    半开区间 [left, right) 表示所有满足 left <= x < right 的实数。
    对 addRange, queryRange, removeRange 的所有调用中 0 < left < right < 10^9。
    在单个测试用例中，对 addRange 的调用总数不超过 1000 次。
    在单个测试用例中，对  queryRange 的调用总数不超过 5000 次。
    在单个测试用例中，对 removeRange 的调用总数不超过 1000 次。

"""
from bisect import bisect_left, bisect_right


class RangeModule:

    def __init__(self):
        self.ranges = []

    def bound(self, left, right):  # 找到与[left,right)相交的区间起始索引
        length = len(self.ranges)
        i = 0
        while i < length:
            if left > self.ranges[i][1]:  # self.ranges[i]整体在(left,right)之前
                i += 1
            else:
                # 1.(left,right)整体在self.ranges[i]之前
                if right < self.ranges[i][0]:
                    return i, i - 1
                # 2.(left,right)与self.ranges[i]相交
                for j in range(i, length):  # 找到最后一个与(left,right)相交的区间
                    if self.ranges[j][0] > right:  # (left,right)整体在self.ranges[j]之前
                        return i, j - 1
                return i, j  # 之后所有的区间都与(left,right)相交
        return length, length - 1

    def addRange(self, left: int, right: int) -> None:
        start, end = self.bound(left, right)
        if start <= end:
            left = min(left, self.ranges[start][0])
            right = max(right, self.ranges[end][1])
        self.ranges[start:end + 1] = [(left, right)]
        # print(start,end,self.ranges)

    def queryRange(self, left: int, right: int) -> bool:
        # 二分查找i,使得self.ranges[i-1][0]<=left, self.ranges[i][0]>left
        i = bisect_left(self.ranges, (left, float('inf')))
        # print(self.ranges,i)
        if i: i -= 1
        return (bool(self.ranges) and self.ranges[i][0] <= left and right <= self.ranges[i][1])
        # if not self.ranges:return False
        # # print(self.ranges)
        # for l in range(len(self.ranges)):
        #     if self.ranges[l][0] > left:
        #         return False if l==0 or self.ranges[l-1][1] < right else True
        # return self.ranges[l][1] >= right

    def removeRange(self, left: int, right: int) -> None:
        start, end = self.bound(left, right)
        merge = []
        for i in range(start, end + 1):  # start>end时，merge = []， 不删除
            if self.ranges[i][0] < left:
                merge.append((self.ranges[i][0], left))
            if right < self.ranges[i][1]:
                merge.append((right, self.ranges[i][1]))
        self.ranges[start:end + 1] = merge
        # self.ranges[start:end+1] = [(self.ranges[start][0], left),(right, self.ranges[end][1])]
        # print(self.ranges)

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
