# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/24 9:57
 @Author  : QDY
 @FileName: 5498. 石子游戏 V.py
 @Software: PyCharm
"""
"""
    几块石子 排成一行 ，每块石子都有一个关联值，关联值为整数，由数组 stoneValue 给出。
    游戏中的每一轮：Alice 会将这行石子分成两个 非空行（即，左侧行和右侧行）；
    Bob 负责计算每一行的值，即此行中所有石子的值的总和。Bob 会丢弃值最大的行，Alice 的得分为剩下那行的值（每轮累加）。
    如果两行的值相等，Bob 让 Alice 决定丢弃哪一行。下一轮从剩下的那一行开始。

    只 剩下一块石子 时，游戏结束。Alice 的分数最初为 0 。
    返回 Alice 能够获得的最大分数 。

    示例 1：
    输入：stoneValue = [6,2,3,4,5,5]
    输出：18
    解释：在第一轮中，Alice 将行划分为 [6，2，3]，[4，5，5] 。左行的值是 11 ，右行的值是 14 。Bob 丢弃了右行，Alice 的分数现在是 11 。
    在第二轮中，Alice 将行分成 [6]，[2，3] 。这一次 Bob 扔掉了左行，Alice 的分数变成了 16（11 + 5）。
    最后一轮 Alice 只能将行分成 [2]，[3] 。Bob 扔掉右行，Alice 的分数现在是 18（16 + 2）。游戏结束，因为这行只剩下一块石头了。

    示例 2：
    输入：stoneValue = [7,7,7,7,7,7,7]
    输出：28

    示例 3：
    输入：stoneValue = [4]
    输出：0
     
    提示：
    1 <= stoneValue.length <= 500
    1 <= stoneValue[i] <= 10^6

"""

from functools import lru_cache


class Solution:
    def stoneGameV(self, stoneValue) -> int:
        length = len(stoneValue)
        if length <= 1: return 0
        if length == 2: return min(stoneValue)
        prefix = [0]
        for i in stoneValue:
            prefix.append(prefix[-1] + i)

        # print(prefix)
        # # dp[i][j]
        # dp = [[0]*length for _ in range(length)]
        # for i in range(length-1):
        #     dp[i][i+1] = min(stoneValue[i],stoneValue[i+1])
        # for l in range(2,length):
        #     for i in range(length-l):
        #         # mid_l,mid_r = None,None
        #         tmp = 0
        #         for j in range(i,i+l):
        #             left, right = prefix[j+1]-prefix[i],prefix[i+l+1]-prefix[j+1]
        #             if left < right:
        #                 tmp = left+dp[i][j]
        #             elif left > right:
        #                 tmp = right+dp[j+1][i+l]
        #             else:
        #                 if dp[i][j]>dp[j+1][i+l]:tmp = left+dp[i][j]
        #                 else:tmp = left + dp[j+1][i+l]
        #                 # tmp = left + max(dp[i][j],dp[j+1][i+l])
        #             if tmp > dp[i][i+l]:dp[i][i+l] = tmp
        # return dp[0][length-1]
        @lru_cache(None)
        def helper(i, j):  # 记忆化递归要比dp填表少状态，速度块
            if i == j: return 0
            if i == j - 1: return min(stoneValue[i], stoneValue[j])
            res = 0
            for m in range(i, j):
                left, right = prefix[m + 1] - prefix[i], prefix[j + 1] - prefix[m + 1]
                if left < right:
                    res = max(res, left + helper(i, m))
                elif left > right:
                    res = max(res, right + helper(m + 1, j))
                else:
                    res = max(res, left + max(helper(i, m), helper(m + 1, j)))
            return res

        return helper(0, length - 1)
