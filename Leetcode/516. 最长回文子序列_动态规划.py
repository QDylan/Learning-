# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/20 21:15
 @Author  : QDY
 @FileName: 516. 最长回文子序列_动态规划.py

    给定一个字符串s，找到其中最长的回文子序列。可以假设s的最大长度为1000。

    示例 1:
    输入:
    "bbbab"

    输出:
    4
    一个可能的最长回文子序列为 "bbbb"。

    示例 2:
    输入:
    "cbbd"

    输出:
    2
    一个可能的最长回文子序列为 "bb"。

"""


class Solution:
    def longestPalindromeSubseq(self, s):
        if not s: return 0

        # 动态规划
        # dp[i][j] 表示在子串s[i:j+1]中的最长回文子序列长度
        # 若 s[i]==s[j],则dp[i][j]=dp[i+1][j-1]+2
        # 否则,说明它俩不可能同时出现在 s[i:j+1] 的最长回文子序列中，
        # 那么把它俩分别加入 s[i+1:j] 中，看看哪个子串产生的回文子序列更长即可：
        # 所以 dp[i][j] = max(dp[i][j-1],dp[i+1][j])

        # dp = [[0]*len(s) for i in range(len(s))]
        # for i in range(len(s)-1,-1,-1):
        #     dp[i][i] = 1
        #     for j in range(i+1,len(s)):
        #         if s[i]==s[j]:
        #             dp[i][j] = dp[i+1][j-1] + 2
        #         else:
        #             dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        # return dp[0][-1]

        # 压缩空间至一维
        dp2 = dp1 = [0] * len(s)
        for i in range(len(s) - 1, -1, -1):
            dp2[i] = 1
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp2[j] = dp1[j - 1] + 2
                else:
                    dp2[j] = max(dp2[j - 1], dp1[j])
            dp1, dp2 = dp2, [0] * len(s)

        return dp1[-1]
