# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/30 15:08
 @Author  : QDY
 @FileName: 214. 最短回文串_KMP_hard.py
 @Software: PyCharm
"""
"""
    给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。

    示例 1:
    输入: "aacecaaa"
    输出: "aaacecaaa"

    示例 2:
    输入: "abcd"
    输出: "dcbabcd"

"""


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # # 从字符串开头找到最大的回文子串
        # l = 0 # 双指针+递归
        # # 若字符串n全部为回文,则i会自增len(n)-1次
        # # 若字符串结尾还有其他字符，则i会自增回文子串的长度，n[:i]一定包含从开头开始的最长回文子串
        # for r in range(len(s)-1,-1,-1):
        #     if s[l] == s[r]: # 缩小了从开头寻找最大回文子串的搜索长度
        #         l += 1
        # if l == len(s): return s  # s自身是回文
        # # s[l:] 一定不在从开头开始的回文子串种
        # return s[l:][::-1] + self.shortestPalindrome(s[:l])+s[l:]

        # KMP算法
        # 找到 s前缀 与 s[::-1]后缀 的最大重合部分
        s, len_s = s + '#' + s[::-1], len(s)  # 用特殊符号隔开，因为所求的前缀不能超过原本的s
        n = 2 * len_s + 1
        i, length, lps = 1, 0, [0] * n
        while i < n:  # length 记录当前最长前缀的终点索引
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length > 0:
                length = lps[length - 1]
            else:
                i += 1
        # s[::-1]后缀与s前缀的最大重合部分长度为 lps[n-1]
        return s[len_s + 1:n - lps[n - 1]] + s[:len_s]
