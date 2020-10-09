# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-08 11:32
 @Author  : QDY
 @FileName: 525. 连续数组.py
 @Software: PyCharm
"""
"""
给定一个二进制数组, 找到含有相同数量的 0 和 1 的最长连续子数组（的长度）。

示例 1:
输入: [0,1]
输出: 2
说明: [0, 1] 是具有相同数量0和1的最长连续子数组。

示例 2:
输入: [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。

"""


class Solution:
    def findMaxLength(self, nums) -> int:
        res, length = 0, len(nums)
        prefix, hm = 0, {0: -1}
        for i in range(length):
            # 将原数组的0全部变为-1 则问题等价于“元素值总和为0的连续数组”
            prefix += nums[i] if nums[i] > 0 else -1
            if prefix in hm:
                res = max(res, i - hm[prefix])
            else:
                hm[prefix] = i
        return res
