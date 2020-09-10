# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/22 15:56
 @Author  : QDY
 @FileName: 188. 买卖股票的最佳时机 IV_动态规划_hard.py

    给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
    设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
    注意:你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

    示例1:
    输入: [2,4,1], k = 2
    输出: 2
    解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。

    示例 2:
    输入: [3,2,6,5,0,3], k = 2
    输出: 7
    解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
        随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

"""


class Solution:
    def maxProfit(self, k, prices):
        if not prices or not k: return 0
        # 动态规划
        days = len(prices)
        if k >= days // 2:  # 当k大于等于天数的一半，可以认为k的次数没有了限制
            res = 0  # 问题退化，用贪心算法即可
            for i in range(1, days):
                res += max(0, prices[i] - prices[i - 1])
            return res

        # dp[i][j][1] 表示在第i天，已经进行了j次交易，手上有股票的利润
        # dp[i][j][0] 表示在第i天，已经进行了j次交易，手上没有股票的利润
        # Base case:
        # dp[0][j][1] = -float('inf'), dp[0][j][0] = 0
        # dp[i][0][1] = -float('inf'), dp[i][0][0] = 0
        # 状态转移：
        # dp[i][j][1] = max(dp[i-1][j][1],dp[i-1][j-1][0]-prices[i-1])  # 是否买入第i天的股票
        # dp[i][j][0] = max(dp[i-1][j][0],dp[i-1][j][1]+prices[i-1])  # 是否在第i天把股票卖出

        dp = [[0, -float('inf')] for i in range(k + 1)]

        for i in range(days):
            for j in range(k, 0, -1):
                dp[j][0], dp[j][1] = max(dp[j][0], dp[j][1] + prices[i]), max(dp[j][1], dp[j - 1][0] - prices[i])

        return dp[-1][0]
