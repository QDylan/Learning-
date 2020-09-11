# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-11 11:45
 @Author  : QDY
 @FileName: 115. 不同的子序列.py
 @Software: PyCharm
"""
"""
给定一个字符串S和一个字符串T，计算在 S 的子序列中 T 出现的个数。

一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。
（例如，"ACE"是"ABCDE"的一个子序列，而"AEC"不是）

题目数据保证答案符合 32 位带符号整数范围。

示例1：
输入：S = "rabbbit", T = "rabbit"
输出：3

解释：
如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^

示例2：
输入：S = "babgbag", T = "bag"
输出：5
解释：
如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。 
(上箭头符号 ^ 表示选取的字母)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^

"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        len_s, len_t = len(s), len(t)
        # dp[i][j] = t[:i] 在 s[:j] 中的出现次数
        # base case : dp[0][j]=1
        # dp[i][j] 最少为 dp[i][j-1]
        # 若t[i-1] == s[j-1]，则需要增多dp[i-1][j-1]种
        dp = [[0] * (len_s + 1) for _ in range(len_t + 1)]
        dp[0] = [1] * (len_s + 1)
        for i in range(1, len_t + 1):
            for j in range(i, len_s + 1):
                dp[i][j] = dp[i][j - 1]
                if t[i - 1] == s[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        # print(dp)
        return dp[-1][-1]
