# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/22 16:51
 @Author  : QDY
 @FileName: 309. 最佳买卖股票时机含冷冻期_动态规划.py

    给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
    设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
    你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

    示例:
    输入: [1,2,3,0,2]
    输出: 3
    解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

"""


class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 1: return 0
        # 动态规划
        # dp[i][0] 表示第i天没持有股票的利润
        # dp[i][1] 表示第i天持有股票的利润
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        # dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i]) 第i天选择买入的时候，要从i-2的状态转移，而不是i-1
        #
        dp1 = [0, -float('inf')]
        dp2 = [0, -float('inf')]
        dp3 = [0, -float('inf')]

        for i in range(len(prices)):
            dp3[0] = max(dp2[0], dp2[1] + prices[i])
            dp3[1] = max(dp2[1], dp1[0] - prices[i])
            dp1, dp2, dp3 = dp2, dp3, [0, -float('inf')]

        return dp2[0]
