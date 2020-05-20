# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/20 18:20
 @Author  : QDY
 @FileName: 1143. 最长公共子序列_动态规划.py

    给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。
    一个字符串的 子序列 是指这样一个新的字符串：
    它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
    例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
    两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。
    若这两个字符串没有公共子序列，则返回 0。

    示例 1:
    输入：text1 = "abcde", text2 = "ace"
    输出：3
    解释：最长公共子序列是 "ace"，它的长度为 3。

    示例 2:
    输入：text1 = "abc", text2 = "abc"
    输出：3
    解释：最长公共子序列是 "abc"，它的长度为 3。

    示例 3:
    输入：text1 = "abc", text2 = "def"
    输出：0
    解释：两个字符串没有公共子序列，返回 0。

"""


class Solution:
    def longestCommonSubsequence(self, text1, text2):
        len1, len2 = len(text1), len(text2)
        # 动态规划
        # dp[i][j] 表示t1[:i]和t2[:j]的最长公共子序列
        # 若t1[i-1]==t2[j-1] 那么t1[:i-1]与t2[:j-1]的最长公共子序列可以增加长度
        #  dp[i][j]=dp[i-1][j-1] + 1
        # 否则，最长公共子序列得不到更新，t1[:i]和t2[:j]的最长公共子序列
        # 为 t1[:i-1]和t2[:j]的最长公共子序列 和 t1[:i]和t2[:j-1]的最长公共子序列 中较长的一个
        # dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # dp = [[0]*(len2+1) for i in range(len1+1)]
        # for i in range(1,len1+1):
        #     for j in range(1,len2+1):
        #         if text1[i-1] == text2[j-1]:
        #             dp[i][j] = dp[i-1][j-1] + 1
        #         else:
        #             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # return dp[-1][-1]

        # 压缩空间
        dp1 = dp2 = [0] * (len2 + 1)
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp2[j] = dp1[j - 1] + 1
                else:
                    dp2[j] = max(dp1[j], dp2[j - 1])
            dp1, dp2 = dp2, [0] * (len2 + 1)
        return dp1[-1]
