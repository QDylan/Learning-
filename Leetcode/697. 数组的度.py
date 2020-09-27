# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-27 15:36
 @Author  : QDY
 @FileName: 697. 数组的度.py
 @Software: PyCharm
"""
"""
给定一个非空且只包含非负数的整数数组nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
你的任务是找到与nums拥有相同大小的度的最短连续子数组，返回其长度。

示例 1:
输入: [1, 2, 2, 3, 1]
输出: 2
解释: 
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.

示例 2:
输入: [1,2,2,3,1,4,2]
输出: 6

注意:
nums.length在1到50,000区间范围内。
nums[i]是一个在0到49,999范围内的整数。

"""


class Solution:
    def findShortestSubArray(self, nums) -> int:
        pos, max_cnt = {}, 1
        for i, n in enumerate(nums):
            if n not in pos:
                pos[n] = [i, i, 1]
            else:
                pos[n][1] = i
                pos[n][2] += 1
                max_cnt = max(max_cnt, pos[n][2])
        res = len(nums)
        for n in pos:
            if pos[n][2] == max_cnt:
                res = min(pos[n][1] - pos[n][0] + 1, res)
        return res
