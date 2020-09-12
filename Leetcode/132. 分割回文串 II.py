# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-12 9:34
 @Author  : QDY
 @FileName: 132. 分割回文串 II.py
 @Software: PyCharm
"""
"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回符合要求的最少分割次数。

示例:
输入:"aab"
输出: 1
解释: 进行一次分割就可将s 分割成 ["aa","b"] 这样两个回文子串。

"""


class Solution:
    def minCut(self, s: str) -> int:

        strs = '#'
        for i in s:  # Manacher算法  计算以strs[i]为中心的最长回文子串长度
            strs += i + '#'
        length = len(strs)
        L, R, dp = 0, -1, [0] * length

        for i in range(length - 1):
            if i < R: dp[i] = min(R - i, dp[L + R - i])
            while i - dp[i] - 1 >= 0 and i + dp[i] + 1 < length and strs[i - dp[i] - 1] == strs[i + dp[i] + 1]:
                dp[i] += 1
            if i + dp[i] > R: L, R = i - dp[i], i + dp[i]

        res = [i for i in range(len(s))]  # res[i]记录s[:i+1]的最少分割次数
        for i in range(len(s)):
            r = dp[2 * i + 1] // 2  # 对于回文 s[i-r:i+r+1]
            for j in range(r + 1):
                if i == j:  # s[:i+j+1]都是回文，不用切割
                    res[i + j] = 0
                else:  # s[i-j:i+j+1]是回文，在s[i-j-1]与s[i-j]之间切割 = res[i-j-1]+1
                    res[i + j] = min(res[i + j], res[i - j - 1] + 1)

            r = dp[2 * i + 2] // 2  # 对于回文 s[i+1-r:i+r+1]
            for j in range(r + 1):
                if i + 1 == j:
                    res[i + j] = 0
                else:  # s[i+1-j:i+j+1]是回文，在s[i-j+1-1]与s[i-j+1]之间切割 = res[i-j]+1
                    res[i + j] = min(res[i + j], res[i - j] + 1)
        # print(res)
        return res[-1]
