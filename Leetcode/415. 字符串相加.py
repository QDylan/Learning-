# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/16 16:25
 @Author  : QDY
 @FileName: 415. 字符串相加.py

    给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

    注意：
    num1 和num2 的长度都小于 5100.
    num1 和num2 都只包含数字 0-9.
    num1 和num2 都不包含任何前导零。
    你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。

"""


class Solution:
    def addStrings(self, num1, num2):
        i1, i2 = len(num1) - 1, len(num2) - 1
        res, carry = '', 0
        while i1 >= 0 or i2 >= 0:
            n1 = int(num1[i1]) if i1 >= 0 else 0
            n2 = int(num2[i2]) if i2 >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i1 -= 1
            i2 -= 1
        if carry:
            res = '1' + res

        return res
