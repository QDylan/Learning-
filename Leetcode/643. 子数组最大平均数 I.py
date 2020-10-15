# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-15 9:41
 @Author  : QDY
 @FileName: 643. 子数组最大平均数 I.py
 @Software: PyCharm
"""
"""
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例 1:
输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75
解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75

注意:
1 <= k <= n <= 30,000。
所给数据范围 [-10,000，10,000]。

"""


class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        cur_sum = sum(nums[:k])
        res = cur_sum
        for i in range(k, len(nums)):
            cur_sum += nums[i] - nums[i - k]
            res = max(res, cur_sum)
        return res / k
