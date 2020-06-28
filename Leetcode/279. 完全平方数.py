# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/28 23:48
 @Author  : QDY
 @FileName: 279. 完全平方数.py

    给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

    示例 1:

    输入: n = 12
    输出: 3
    解释: 12 = 4 + 4 + 4.
    示例 2:

    输入: n = 13
    输出: 2
    解释: 13 = 4 + 9.

"""


class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i] = 最少个数
        # dp[i] = min(dp[i-square])
        sqrt = int(n ** 0.5)
        if sqrt ** 2 == n: return 1
        square = [i ** 2 for i in range(1, sqrt + 1)]
        dp = [0] + [float('inf')] * n
        for i in range(1, n + 1):
            for s in square:
                if i >= s:
                    dp[i] = min(dp[i], dp[i - s])
                else:
                    break
            dp[i] += 1
        return dp[n]

        # # 任何一个正整数都可以表示成不超过四个整数的平方之和
        # # 如果一个数最少可以拆成4个数的平方和，则这个数还满足 n = (4^a)*(8b+7)
        # while n%4 == 0:
        #     n //= 4
        # if n%8 == 7:
        #     return 4
        # sqrt = int(n**0.5)
        # if sqrt**2 == n:
        #     return 1
        # for i in range(sqrt,0,-1):
        #     if int((n-i**2)**0.5)**2==n-i**2:
        #         return 2
        # return 3
