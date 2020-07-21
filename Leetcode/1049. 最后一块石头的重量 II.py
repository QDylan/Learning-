# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/21 14:08
 @Author  : QDY
 @FileName: 1049. 最后一块石头的重量 II.py

    有一堆石头，每块石头的重量都是正整数。
    每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
    如果 x == y，那么两块石头都会被完全粉碎；
    如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
    最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。

    示例：
    输入：[2,7,4,1,8,1]
    输出：1
    解释：
    组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
    组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
    组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
    组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
     
    提示：
    1 <= stones.length <= 30
    1 <= stones[i] <= 1000

"""


class Solution:
    def lastStoneWeightII(self, stones):
        # 转换成01子集背包问题，将石头分成两堆，使其和的差值最小
        # 每个背包最多装sum//2的重量，求如何装下最多重量的石头
        sum_ = sum(stones)
        w = sum_ // 2
        # dp[i][j]=背包容量为j时，对stones[:i]中的物品,最多能装多少重量
        # 考虑是否使用stones[i]装包：
        # dp[i][j]=max(dp[i-1][j],dp[j-stones[i]]+stones[i])
        dp = [0] * (w + 1)
        for i in range(len(stones)):
            for j in range(w, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        # stones可被分为dp[w]和sum_-dp[w]两组,其中dp[w]<=sum//2
        return sum_ - 2 * dp[w]  # 最后剩余的重量为sum_-dp[w]*2
