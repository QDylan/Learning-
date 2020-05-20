# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/17 21:57
 @Author  : QDY
 @FileName: 300. 最长上升子序列_动态规划+耐心排序.py

    给定一个无序的整数数组，找到其中最长上升子序列的长度。

    示例:

    输入: [10,9,2,5,3,7,101,18]
    输出: 4
    解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

"""


class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0

        # # 1.动态规划，时间复杂度O(n^2)
        # # dp[i]记录以nums[i]结尾的最长递增子序列长度
        # dp = [1]*len(nums)
        # for i in range(1,len(nums)):
        #     for j in range(i):  # 对于在i之前的子序列
        #         if nums[i]>nums[j]:  # 若nums[i]>nums[j]，
        #         # 则说明可以在以nums[j]结尾的最长子序列的末尾加上nums[i]
        #             dp[i] = max(dp[i],dp[j]+1)
        # return max(dp)

        # 2.改进的动态规划（扑克牌耐心排序算法） 时间复杂度O(nlogn)
        # 首先，给你一排扑克牌，我们像遍历数组那样从左到右一张一张处理这些扑克牌，最终要把这些牌分成若干堆。
        # 处理这些扑克牌要遵循以下规则：只能把点数小的牌压到点数比它大的牌上。
        # 如果当前牌点数较大没有可以放置的堆，则新建一个堆，把这张牌放进去。
        # 如果当前牌有多个堆可供选择，则选择最左边的堆放置。（可以保证最顶部元素是按升序排列的）
        # 按照上述规则执行，可以算出最长递增子序列，牌的堆数就是最长递增子序列的长度

        dp = [nums[0]]  # dp[i] 表示长度为i的子序列的最小末尾元素（即牌堆的顶部元素）
        res = 1  # 最长上升子序列长度（即牌堆的数量）
        for i in range(1, len(nums)):
            left, right = 0, res - 1
            while left <= right:  # 在dp中进行二分搜索，最终位置为left,使得
                mid = left + (right - left) // 2  # dp[left]<nums[i],dp[left-1]>=nums[i] if left>0
                if dp[mid] < nums[i]:  # 中间值小于nums[i]时，增大左边界
                    left = mid + 1  # 若改成不严格递增序列，则此处改为<=即可
                else:  # 中间值大于等于nums[i]时，减小右边界
                    right = mid - 1

            if left == res:
                res += 1
                dp.append(nums[i])
            else:
                dp[left] = nums[i]

        return res
