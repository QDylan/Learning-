# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/28 8:47
 @Author  : QDY
 @FileName: 209. 长度最小的子数组.py

    给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，
    并返回其长度。如果不存在符合条件的连续子数组，返回 0。

    示例: 
    输入: s = 7, nums = [2,3,1,2,4,3]
    输出: 2
    解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。

    进阶:
    如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

"""


class Solution:
    def minSubArrayLen(self, target, nums):
        if not nums: return 0
        #
        n = len(nums)
        res = n + 1
        l, r, sum_ = 0, 0, 0
        while r < n:  # 滑动窗口 O(n)
            while sum_ < target and r < n:
                sum_ += nums[r]
                r += 1
            while sum_ >= target:
                res = min(res, r - l)
                sum_ -= nums[l]
                l += 1
        return 0 if res == n + 1 else res

        # # 前缀和+二分查找 O(nlogn)
        # prefix = [0]
        # for i in range(n):
        #     prefix.append(prefix[-1]+nums[i])
        # if prefix[-1]<target:return 0
        # res = n+1
        # for i in range(n):
        #     l,r = i,n
        #     while l<=r:
        #         mid = l+(r-l)//2
        #         if prefix[mid]-prefix[i]>=target:
        #             r = mid - 1
        #         else:
        #             l = mid + 1
        #     if l<=n:
        #         res = min(res,l-i)

        # return res
