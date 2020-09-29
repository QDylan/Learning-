# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-29 10:36
 @Author  : QDY
 @FileName: 303. 区域和检索 - 数组不可变.py
 @Software: PyCharm
"""
"""
给定一个整数数组 nums，求出数组从索引i到j(i≤j) 范围内元素的总和，包含i, j两点。

示例：
给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

说明:
你可以假设数组不可变。
会多次调用sumRange方法。

"""


class NumArray:

    def __init__(self, nums):
        self.prefix = [0]
        for i in nums:
            self.prefix.append(self.prefix[-1] + i)

    def sumRange(self, i: int, j: int) -> int:
        return self.prefix[j + 1] - self.prefix[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
