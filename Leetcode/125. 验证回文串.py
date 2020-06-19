# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/19 8:51
 @Author  : QDY
 @FileName: 125. 验证回文串.py

    给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
    说明：本题中，我们将空字符串定义为有效的回文串。

    示例 1:
    输入: "A man, a plan, a canal: Panama"
    输出: true

    示例 2:
    输入: "race a car"
    输出: false

"""


class Solution:
    def isPalindrome(self, s):
        if not s: return True
        # # filter:过滤器 str.isalnum:只选择字母和数字
        # s = ''.join(filter(str.isalnum,s)).lower()
        # return s==s[::-1]
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not (s[l].isdigit() or s[l].isalnum()):
                l += 1
            while l < r and not (s[r].isdigit() or s[r].isalnum()):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
