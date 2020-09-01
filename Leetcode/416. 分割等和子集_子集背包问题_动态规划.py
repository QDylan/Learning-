# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/18 17:40
 @Author  : QDY
 @FileName: 416. 分割等和子集_子集背包问题_动态规划.py

    给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

    注意:
    每个数组中的元素不会超过 100
    数组的大小不会超过 200

    示例 1:
    输入: [1, 5, 11, 5]
    输出: true
    解释: 数组可以分割成 [1, 5, 5] 和 [11].


    示例2:
    输入: [1, 2, 3, 5]
    输出: false
    解释: 数组不能分割成两个元素和相等的子集.

"""


class Solution:
    def canPartition(self, nums):
        sum_ = sum(nums)
        if sum_ % 2 != 0:
            return False
        sum_ = sum_ // 2
        # 动态规划，转换为子集背包问题
        # 给一个可装载重量为 sum_ 的背包和 N 个物品，每个物品的重量为 nums[i]。现在让你装物品，是否存在一种装法，能够恰好将背包装满
        # dp[i][j] 表示背包容量为j,装nums[:i]的物品能否恰好装满
        # 若dp[i-1][j]=True,则dp[i][j]=True
        # 否则，dp[i][j] = dp[i-1][j-nums[i]]

        length = len(nums)
        # dp_prev = [True]+[False]*sum_  # dp[i][j], 初始i=0
        # dp_cur = [True]+[False]*sum_  # dp[i+1][j], j==0时为True
        dp = [True] + [False] * sum_  # 压缩

        for i in range(length):
            for j in range(sum_, nums[i] - 1, -1):  # 从后往前更新，已经更新的不会影响后面更新的
                dp[j] = dp[j] or dp[j - nums[i]]
        #          for j in range(nums[i],sum_+1):
        #             dp_cur[j] = dp_prev[j] or dp_prev[j-nums[i]]
        #     dp_prev, dp_cur = dp_cur, [True]+[False]*sum_
        # return dp_prev[-1]

        return dp[-1]
