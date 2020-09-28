# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-28 16:11
 @Author  : QDY
 @FileName: 665. 非递减数列.py
 @Software: PyCharm
"""
"""
给你一个长度为n的整数数组，请你判断在 最多 改变1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的：对于数组中所有的i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。

示例 1:
输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。

示例 2:
输入: nums = [4,2,1]
输出: false
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。

说明：
1 <= n <= 10 ^ 4
- 10 ^ 5<= nums[i] <= 10 ^ 5

"""

class Solution:
    def checkPossibility(self, nums) -> bool:
        N = len(nums)
        if N <= 2: return True
        cnt = 1 if nums[0] <= nums[1] else 0
        for i in range(2, N):
            if nums[i] < nums[i - 1]:
                cnt -= 1
                if cnt < 0 or (i < N - 1 and nums[i + 1] < nums[i - 1] and nums[i - 2] > nums[i]): return False
                # 特殊情况 2,4,0,1
        return True
