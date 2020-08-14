# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/14 10:07
 @Author  : QDY
 @FileName: 90. 子集 II.py
 @Software: PyCharm
"""
"""
    给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
    说明：解集不能包含重复的子集。
    
    示例:
    输入: [1,2,2]
    输出:
    [
      [2],
      [1],
      [1,2,2],
      [2,2],
      [1,2],
      []
    ]

"""


class Solution:
    def subsetsWithDup(self, nums):
        res = [[]]
        nums.sort()
        prev_add = 0
        for i in range(len(nums)):
            length = len(res)
            if i > 0 and nums[i] == nums[i - 1]:
                for j in range(length - prev_add, length):
                    res.append(res[j] + [nums[i]])
            else:
                prev_add = length
                for j in range(length):
                    res.append(res[j] + [nums[i]])
        return res
