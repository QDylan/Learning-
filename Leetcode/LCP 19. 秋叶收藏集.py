# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-12 19:45
 @Author  : QDY
 @FileName: LCP 19. 秋叶收藏集.py
 @Software: PyCharm
"""
"""
小扣出去秋游，途中收集了一些红叶和黄叶，他利用这些叶子初步整理了一份秋叶收藏集 leaves， 
字符串 leaves 仅包含小写字符 r 和 y， 其中字符 r 表示一片红叶，字符 y 表示一片黄叶。
出于美观整齐的考虑，小扣想要将收藏集中树叶的排列调整成「红、黄、红」三部分。
每部分树叶数量可以不相等，但均需大于等于 1。每次调整操作，小扣可以将一片红叶替换成黄叶或者将一片黄叶替换成红叶。
请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕。

示例 1：
输入：leaves = "rrryyyrryyyrr"
输出：2
解释：调整两次，将中间的两片红叶替换成黄叶，得到 "rrryyyyyyyyrr"

示例 2：
输入：leaves = "ryr"
输出：0
解释：已符合要求，不需要额外操作

提示：
3 <= leaves.length <= 10^5
leaves 中只包含字符 'r' 和字符 'y'

"""


class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        # 动态规划
        # dp[i][0] = leaves[:i+1]全部变为r 最少多少次
        # dp[i][1] = leaves[:i+1]变为r+y 最少多少次
        # dp[i][2] = leaves[:i+1]变为r+y+r 最少多少次
        # dp[i][0] ：从从上一个状态dp[i-1][0]转变，若leaves[i]为y则+1
        # dp[i][1] : 可以从上一个全r状态转变，或者从上一个r+y状态转变
        # dp[i][2] ：从上一个r+y状态转变，或者从上一个r+y+r状态转变
        dp = [[0] * 3 for _ in range(n)]

        dp[0][0] = 0 if leaves[0] == 'r' else 1

        dp[1][0] = dp[0][0] + (0 if leaves[1] == 'r' else 1)
        dp[1][1] = dp[0][0] + (0 if leaves[1] == 'y' else 1)

        dp[2][0] = dp[1][0] + (0 if leaves[2] == 'r' else 1)
        dp[2][1] = min(dp[1][0] + (0 if leaves[2] == 'y' else 1), dp[1][1] + (0 if leaves[2] == 'y' else 1))
        dp[2][2] = dp[1][1] + (0 if leaves[2] == 'r' else 1)

        for i in range(3, n):
            dp[i][0] = dp[i - 1][0] + (0 if leaves[i] == 'r' else 1)
            dp[i][1] = min(dp[i - 1][0] + (0 if leaves[i] == 'y' else 1), dp[i - 1][1] + (0 if leaves[i] == 'y' else 1))
            dp[i][2] = min(dp[i - 1][1] + (0 if leaves[i] == 'r' else 1), dp[i - 1][2] + (0 if leaves[i] == 'r' else 1))

        return dp[n - 1][2]
