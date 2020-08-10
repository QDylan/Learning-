# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/10 14:19
 @Author  : QDY
 @FileName: 1547. 切棍子的最小成本.py
 @Software: PyCharm
"""
"""
    有一根长度为 n 个单位的木棍，棍上从 0 到 n 标记了若干位置。例如，长度为 6 的棍子可以标记如下：
    
    给你一个整数数组 cuts ，其中 cuts[i] 表示你需要将棍子切开的位置。
    你可以按顺序完成切割，也可以根据需要更改切割的顺序。
    每次切割的成本都是当前要切割的棍子的长度，切棍子的总成本是历次切割成本的总和。
    对棍子进行切割将会把一根木棍分成两根较小的木棍（这两根木棍的长度和就是切割前木棍的长度）。
    请参阅第一个示例以获得更直观的解释。
    
    返回切棍子的 最小总成本 。
    
    示例 1：
    输入：n = 7, cuts = [1,3,4,5]
    输出：16
    解释：按 [1, 3, 4, 5] 的顺序切割的情况如下所示：
    
    第一次切割长度为 7 的棍子，成本为 7 。第二次切割长度为 6 的棍子（即第一次切割得到的第二根棍子），
    第三次切割为长度 4 的棍子，最后切割长度为 3 的棍子。总成本为 7 + 6 + 4 + 3 = 20 。
    而将切割顺序重新排列为 [3, 5, 1, 4] 后，总成本 = 16（如示例图中 7 + 4 + 3 + 2 = 16）。
    
    示例 2：
    
    输入：n = 9, cuts = [5,6,1,4,2]
    输出：22
    解释：如果按给定的顺序切割，则总成本为 25 。总成本 <= 25 的切割顺序很多，
    例如，[4，6，5，2，1] 的总成本 = 22，是所有可能方案中成本最小的。
    
    提示：
    2 <= n <= 10^6
    1 <= cuts.length <= min(n - 1, 100)
    1 <= cuts[i] <= n - 1
    cuts 数组中的所有整数都 互不相同

"""


class Solution:
    def merge(self, nums):
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):  # 计算前缀和
            prefix[i] = nums[i - 1] + prefix[i - 1]
        # 动态规划 dp[i][j]为合并nums[i]和nums[j]的最小成本
        dp = [[0] * n for _ in range(n)]
        for j in range(2, n + 1):  # 合并的个数j，从合并两个开始，直到最后合并n个
            for i in range(n - j + 1):  # 合并的最左部分的索引i,最右部分i+j-1, 需要i+j-1<n -> i<n-j+1
                # 在合并第i部分与第i+j-1部分时,先分别合并第i到第k部分 和 第k+1部分到第i+j-1部分, 再将两部分合并  i<=k<i+j-1
                # 合并第i到第k部分的成本=dp[i][k]  合并k+1部分到第i+j-1部分的成本=dp[k+1][i+j-1]
                # 将两部分合并的成本 = sum(nums[i:i+j]) = prefix[i+j]-prefix[i]
                dp[i][i + j - 1] = min(dp[i][k] + dp[k + 1][i + j - 1] for k in range(i, i + j - 1)) + prefix[i + j] - \
                                   prefix[i]

        return dp[0][n - 1]

    def minCost(self, n, cuts):
        cuts.sort()
        cuts.append(n)
        lengths = [cuts[0]]
        for i in range(1, len(cuts)):  # 将最后切分好后每一段的长度依次存入lengths
            lengths.append(cuts[i] - cuts[i - 1])
        # 将问题看作是：每次可以合并两个相邻的长度，合并的成本为合并后的长度，求全合并后的最小成本
        return self.merge(lengths)
