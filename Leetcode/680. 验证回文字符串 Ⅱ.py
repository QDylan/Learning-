# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/19 9:00
 @Author  : QDY
 @FileName: 680. 验证回文字符串 Ⅱ.py

 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

    示例 1:
    输入: "aba"
    输出: True

    示例 2:
    输入: "abca"
    输出: True
    解释: 你可以删除c字符。

    注意:
    字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
    通过次数22,044提交次数59,058

"""


class Solution:

    def validPalindrome(self, s):
        length = len(s)
        for i in range((length - 1) // 2):
            if s[i] != s[length - 1 - i]:  # 当遇到左右不相等的时候，有一次删除的机会
                a, b = s[i:length - 1 - i], s[i + 1:length - i]
                return a == a[::-1] or b == b[::-1]  # 删除两边其中一个，判断剩下的字符串是否构成回文
        return True
