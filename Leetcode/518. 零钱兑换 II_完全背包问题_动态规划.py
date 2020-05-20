# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/19 11:03
 @Author  : QDY
 @FileName: 518. 零钱兑换 II_完全背包问题_动态规划.py

    给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。
    假设每一种面额的硬币有无限个。 

    示例 1:
    输入: amount = 5, coins = [1, 2, 5]
    输出: 4
    解释: 有四种方式可以凑成总金额:
    5=5
    5=2+2+1
    5=2+1+1+1
    5=1+1+1+1+1

    示例 2:
    输入: amount = 3, coins = [2]
    输出: 0
    解释: 只用面额2的硬币不能凑成总金额3。

    示例 3:
    输入: amount = 10, coins = [10]
    输出: 1
     
    注意:
    你可以假设：
    0 <= amount (总金额) <= 5000
    1 <= coin (硬币面额) <= 5000
    硬币种类不超过 500 种
    结果符合 32 位符号整数

"""


class Solution:
    def change(self, amount, coins):
        if amount == 0:
            return 1
        # 完全背包问题

        # 1.动态规划
        # dp[i][j] = 使用前i个硬币，恰好凑成j元的组合数
        # dp[i+1][j] = dp[i][j] + dp[i][j-coins[i+1]]
        dp = [1] + [0] * amount  # 压缩到一维
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i - c]
            # print(dp)
        return dp[-1]

        # # 2.DFS  超时
        # res = 0
        # coins.sort(reverse=True)
        # # print(coins)
        # length = len(coins)
        # def dfs(cur_amount,i):
        #     nonlocal res
        #     if cur_amount == 0:
        #         res += 1

        #         return
        #     for j in range(i,length):
        #         if coins[j] > cur_amount:
        #             continue
        #         dfs(cur_amount-coins[j],j)

        # for i in range(length):
        #     if amount >= coins[i]:
        #         dfs(amount-coins[i],i)
        # return res
