# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/16 15:26
 @Author  : QDY
 @FileName: 41. 缺失的第一个正数.py

    给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。

    示例 1:
    输入: [1,2,0]
    输出: 3

    示例 2:
    输入: [3,4,-1,1]
    输出: 2

    示例 3:
    输入: [7,8,9,11,12]
    输出: 1
     
    提示：
    你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。

"""


class Solution:
    def firstMissingPositive(self, nums):  # 原地修改数组
        n = len(nums)
        if 1 not in nums: return 1
        if n == 1: return 2

        for i in range(n):  # 将非正数设置为1
            if nums[i] <= 0:
                nums[i] = 1

        for i in range(n):  # 利用数组索引对出现过的正数进行记录
            id_ = abs(nums[i])
            if id_ == n:  # 若出现了n,则用id为0的位置进行记录
                nums[0] = -abs(nums[0])
            elif id_ < n:  # 出现过的正数，数组对应索引位置上的数是负的
                nums[id_] = -abs(nums[id_])

        for i in range(1, n):  # 从id=1开始,第一个是正数的位置，其索引就是没出现的最小正数
            if nums[i] > 0: return i
        # 从1到末尾都是负数，说明1~n-1都出现过
        if nums[0] > 0:  # 若n没出现过，返回n
            return n
        return n + 1  # 1~n都出现过，返回n+1
