# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/24 8:25
 @Author  : QDY
 @FileName: 16. 最接近的三数之和.py

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

示例：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

提示：
3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

"""


class Solution:
    def threeSumClosest(self, nums, target):
        min_dist = float('inf')
        res = None
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                sum_ = nums[i] + nums[l] + nums[r]
                if sum_ == target:
                    return target
                elif sum_ > target:
                    if min_dist > sum_ - target:
                        min_dist = sum_ - target
                        res = sum_
                    r -= 1
                    while r >= 0 and nums[r] == nums[r + 1]:
                        r -= 1
                else:
                    if min_dist > target - sum_:
                        min_dist = target - sum_
                        res = sum_
                    l += 1
                    while l < n and nums[l] == nums[l - 1]:
                        l += 1

        return res
