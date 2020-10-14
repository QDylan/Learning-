# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-14 10:01
 @Author  : QDY
 @FileName: 345. 反转字符串中的元音字母.py
 @Software: PyCharm
"""
"""
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1：
输入："hello"
输出："holle"

示例 2：
输入："leetcode"
输出："leotcede"

提示：
元音字母不包含字母 "y" 。

"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        res = list(s)
        l, r = 0, len(res) - 1
        while l < r:
            while l < r and res[l] not in vowel:
                l += 1
            while l < r and res[r] not in vowel:
                r -= 1
            if l < r:
                res[l], res[r] = res[r], res[l]
                l += 1
                r -= 1
        return ''.join(res)
