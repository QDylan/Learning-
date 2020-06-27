# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/27 12:43
 @Author  : QDY
 @FileName: 131. 分割回文串_动态规划+DFS.py


    给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

    返回 s 所有可能的分割方案。

    示例:

    输入: "aab"
    输出:
    [
      ["aa","b"],
      ["a","a","b"]
    ]
"""


class Solution:
    def partition(self, s):
        # dp[i][j]=s[i:j+1]是否是回文
        len_s = len(s)
        dp = [[False] * len_s for i in range(len_s)]
        for i in range(len_s):  # base case:
            dp[i][i] = True  # 单个字符串dp[i][i]=True
            if i < len_s - 1 and s[i] == s[i + 1]:  # 两个字符串
                dp[i][i + 1] = True
        for i in range(3, len_s + 1):
            for j in range(len_s - i + 1):
                dp[j][j + i - 1] = dp[j + 1][j + i - 2] and s[j] == s[j + i - 1]
        # print(dp)
        res = []

        def dfs(x, tmp):
            nonlocal res
            if x == len_s:
                res.append(tmp)
                return
            for y in range(x, len_s):
                if dp[x][y]:
                    dfs(y + 1, tmp + [s[x:y + 1]])

        for i in range(len_s):
            if dp[0][i]:
                dfs(i + 1, [s[:i + 1]])

        return res
