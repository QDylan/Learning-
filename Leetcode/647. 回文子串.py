# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/19 9:17
 @Author  : QDY
 @FileName: 647. 回文子串.py
 @Software: PyCharm
"""
"""
    给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
    具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

    示例 1：
    输入："abc"
    输出：3
    解释：三个回文子串: "a", "b", "c"

    示例 2：
    输入："aaa"
    输出：6
    解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"

    提示：
    输入的字符串长度不会超过 1000 。

"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        if length <= 1: return length
        # 动态规划
        # res = length
        # dp = [[False]*(length-i) for i in range(length)]
        # dp[0] = [True]*length
        # for i in range(length-1):
        #     if s[i]==s[i+1]:
        #         res += 1
        #         dp[1][i] = True
        #         # print(s[i:i+2])
        # for j in range(2,length):
        #     for i in range(length-j):
        #         if s[i]==s[i+j] and dp[j-2][i+1]:
        #             dp[j][i] = True
        #             res += 1
        #             # print(s[i:i+j+1])
        # return res

        self.res = length

        def helper(left, right):  # 中心扩散
            if left > 0 and right < length - 1 and s[left - 1] == s[right + 1]:
                self.res += 1
                helper(left - 1, right + 1)

        for i in range(length - 1):
            helper(i, i)
            if s[i] == s[i + 1]:
                self.res += 1
                helper(i, i + 1)
        return self.res
