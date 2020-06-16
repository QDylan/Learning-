# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/16 22:39
 @Author  : QDY
 @FileName: 78. 子集.py

    给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
    说明：解集不能包含重复的子集。

    示例:
    输入: nums = [1,2,3]
    输出:
    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]

"""


class Solution:
    def subsets(self, nums):
        res = [[]]

        # 遇到一个数就把所有子集加上该数组成新的子集
        for i in nums:
            r = len(res)
            for j in range(r):
                res.append(res[j] + [i])
        return res
        # n = len(nums)
        # def dfs(start,tmp):
        #     nonlocal res
        #     res.append(tmp)
        #     if start<n:
        #         for j in range(start,n):
        #             dfs(j+1,tmp+[nums[j]])

        # for i in range(n):
        #     dfs(i+1,[nums[i]])

        # return res
