# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/18 9:03
 @Author  : QDY
 @FileName: 97. 交错字符串_动态规划.py

    给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

    示例 1:
    输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
    输出: true

    示例 2:
    输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
    输出: false

"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp[i][j] = s3[:i+j] 是否是 s1[:i]与s2[:j]组成的交错
        # dp[0][0] = True
        # dp[0][j] = dp[0][j-1] and s3[j-1]==s2[j-1]
        # dp[i][0] = dp[i-1][0] and s3[i-1]==s1[i-1]
        # dp[i][j] = (dp[i-1][j] and s3[i+j-1]==s1[i-1]) or (dp[i][j-1] and s3[i+j-1]==s2[j-1])
        len1, len2 = len(s1), len(s2)
        if len1 + len2 != len(s3):
            return False
        dp = [True]
        for j in range(len2):
            dp.append(dp[-1] and s3[j] == s2[j])
        for i in range(1, len1 + 1):
            dp[0] = dp[0] and s3[i - 1] == s1[i - 1]
            for j in range(1, len2 + 1):
                dp[j] = (dp[j] and s3[i + j - 1] == s1[i - 1]) or (dp[j - 1] and s3[i + j - 1] == s2[j - 1])
        return dp[-1]
