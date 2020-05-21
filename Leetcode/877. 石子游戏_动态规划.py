# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/21 10:26
 @Author  : QDY
 @FileName: 877. 石子游戏_动态规划.py

    亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。
    游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。
    亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。
    这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。
    假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false 。

    示例：
    输入：[5,3,4,5]
    输出：true
    解释：
    亚历克斯先开始，只能拿前 5 颗或后 5 颗石子 。
    假设他取了前 5 颗，这一行就变成了 [3,4,5] 。
    如果李拿走前 3 颗，那么剩下的是 [4,5]，亚历克斯拿走后 5 颗赢得 10 分。
    如果李拿走后 5 颗，那么剩下的是 [3,4]，亚历克斯拿走后 4 颗赢得 9 分。
    这表明，取前 5 颗石子对亚历克斯来说是一个胜利的举动，所以我们返回 true 。
     

    提示：
    2 <= piles.length <= 500
    piles.length 是偶数。
    1 <= piles[i] <= 500
    sum(piles) 是奇数。

"""


class Solution:
    def stoneGame(self, piles):
        # return True  # 先手必胜

        # 动态规划 (可以计算得分，且石子堆数不一定为偶数)
        # dp1[i][j] 表示在piles[i:j+1]中先手能获得的最大分数
        # dp2[i][j] 表示在piles[i:j+1]中后手能获得的最大分数
        # 在piles[i:j+1]中，先手若选择了piles[i]，则能获得piles[i]+dp2[i+1][j]
        # 若选泽了piles[j]，则能获得piles[j]+dp2[i][j-1]
        # dp1[i][j] = max(piles[i]+dp2[i+1][j],piles[j]+dp2[i][j-1])
        n = len(piles)
        dp1 = [[0] * n for i in range(n)]
        dp2 = [[0] * n for i in range(n)]
        for i in range(n - 1, -1, -1):
            dp1[i][i] = piles[i]
            for j in range(i + 1, n):
                left = piles[i] + dp2[i + 1][j]
                right = piles[j] + dp2[i][j - 1]
                if left > right:
                    dp1[i][j], dp2[i][j] = left, dp1[i + 1][j]
                else:
                    dp1[i][j], dp2[i][j] = right, dp1[i][j - 1]

        return dp1[0][-1] > dp2[0][-1]
