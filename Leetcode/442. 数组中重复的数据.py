# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-28 10:18
 @Author  : QDY
 @FileName: 442. 数组中重复的数据.py
 @Software: PyCharm
"""
"""
给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。
找到所有出现两次的元素。
你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？

示例：
输入:
[4,3,2,7,8,2,3,1]
输出:
[2,3]

"""


class Solution:
    def findDuplicates(self, nums):
        res = []
        for i, n in enumerate(nums):
            n = abs(n)
            if nums[n - 1] > 0:
                nums[n - 1] *= -1
            else:  # 原本是负数，说明该位置+1已出现过一次
                res.append(n)
        return res
