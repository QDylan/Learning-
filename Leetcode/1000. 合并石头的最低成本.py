# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/11 9:40
 @Author  : QDY
 @FileName: 1000. 合并石头的最低成本.py
 @Software: PyCharm
"""
"""
    有 N 堆石头排成一排，第 i 堆中有stones[i]块石头。
    每次移动（move）需要将连续的K堆石头合并为一堆，而这个移动的成本为这K堆石头的总数。
    找出把所有石头合并成一堆的最低成本。如果不可能，返回 -1 。

    示例 1：
    输入：stones = [3,2,4,1], K = 2
    输出：20
    解释：
    从 [3, 2, 4, 1] 开始。
    合并 [3, 2]，成本为 5，剩下 [5, 4, 1]。
    合并 [4, 1]，成本为 5，剩下 [5, 5]。
    合并 [5, 5]，成本为 10，剩下 [10]。
    总成本 20，这是可能的最小值。

    示例 2：
    输入：stones = [3,2,4,1], K = 3
    输出：-1
    解释：任何合并操作后，都会剩下 2 堆，我们无法再进行合并。所以这项任务是不可能完成的。.

    示例 3：
    输入：stones = [3,5,1,2,6], K = 3
    输出：25
    解释：
    从 [3, 5, 1, 2, 6] 开始。
    合并 [5, 1, 2]，成本为 8，剩下 [3, 8, 6]。
    合并 [3, 8, 6]，成本为 17，剩下 [17]。
    总成本 25，这是可能的最小值。
    
    提示：
    1 <= stones.length <= 30
    2 <= K <= 30
    1 <= stones[i] <= 100

"""


class Solution:
    def mergeStones(self, stones, K: int) -> int:
        n = len(stones)
        if (n - 1) % (K - 1): return -1  # 判断是否最终可以合成一堆
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + stones[i - 1]
        # 动态规划 dp[i][j]=合并stones[i]~stones[j]的最低成本
        dp = [[0] * n for _ in range(n)]
        for j in range(K, n + 1):  # 合并j堆石头，j=k+m*(K-1)
            for i in range(n - j + 1):  # 最左堆索引i,最右堆索引i+j-1，且i+j-1<n -> i<n-j+1
                # stones[i]~stones[p] 可以合成1堆, p=i+x*(K-1)
                # 若(j-1)%(K-1)!=0,则i~i+j-1堆石头不能合并成一堆
                # prefix[i+j]-prefix[i] = dp[i][p]和dp[p+1][i+j-1]正好能合并成一堆，需要增加的成本
                dp[i][i + j - 1] = min(dp[i][p] + dp[p + 1][i + j - 1] for p in range(i, i + j - 1, K - 1)) + (
                    prefix[i + j] - prefix[i] if (j - 1) % (K - 1) == 0 else 0)
        # print(dp)
        return dp[0][n - 1]
