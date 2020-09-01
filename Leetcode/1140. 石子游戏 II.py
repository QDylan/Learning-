# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-01 10:40
 @Author  : QDY
 @FileName: 1140. 石子游戏 II.py
 @Software: PyCharm
"""
"""
    亚历克斯和李继续他们的石子游戏。许多堆石子排成一行，每堆都有正整数颗石子piles[i]。游戏以谁手中的石子最多来决出胜负。
    亚历克斯和李轮流进行，亚历克斯先开始。最初，M = 1。
    在每个玩家的回合中，该玩家可以拿走剩下的前X堆的所有石子，其中1 <= X <= 2M。然后，令M = max(M, X)。
    游戏一直持续到所有石子都被拿走。
    假设亚历克斯和李都发挥出最佳水平，返回亚历克斯可以得到的最大数量的石头。

    示例：
    输入：piles = [2,7,9,4,4]
    输出：10
    解释：
    如果亚历克斯在开始时拿走一堆石子，李拿走两堆，接着亚历克斯也拿走两堆。在这种情况下，亚历克斯可以拿到 2 + 4 + 4 = 10 颗石子。 
    如果亚历克斯在开始时拿走两堆石子，那么李就可以拿走剩下全部三堆石子。在这种情况下，亚历克斯可以拿到 2 + 7 = 9 颗石子。
    所以我们返回更大的 10。 
    
    提示：
    1 <= piles.length <= 100
    1 <= piles[i]<= 10 ^ 4

"""
from functools import lru_cache


class Solution:
    def stoneGameII(self, piles) -> int:
        n = len(piles)
        suffix = [0]
        for i in piles[::-1]:
            suffix.append(suffix[-1] + i)
        suffix.reverse()

        # print(suffix)

        @lru_cache(None)  # 记忆化dfs
        def helper(start, M):
            if 2 * M >= n - start: return suffix[start]
            tmp = float('inf')
            for X in range(1, 2 * M + 1):
                tmp = min(tmp, helper(start + X, max(X, M)))
            return suffix[start] - tmp

        return helper(0, 1)
