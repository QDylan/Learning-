# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-29 15:58
 @Author  : QDY
 @FileName: 917. 仅仅反转字母.py
 @Software: PyCharm
"""
"""
给定一个字符串S，返回“反转后的”字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。

示例 1：
输入："ab-cd"
输出："dc-ba"

示例 2：
输入："a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"

示例 3：
输入："Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"

提示：

S.length <= 100
33 <= S[i].ASCIIcode <= 122
S 中不包含\ or "
"""


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        res = list(S)
        l, r = 0, len(S) - 1
        while l < r:
            if res[l].isalpha():
                while not res[r].isalpha():
                    r -= 1
                res[l], res[r] = res[r], res[l]
                r -= 1
            l += 1
        return ''.join(res)
