# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/23 8:53
 @Author  : QDY
 @FileName: 67. 二进制求和.py

    给你两个二进制字符串，返回它们的和（用二进制表示）。
    输入为 非空 字符串且只包含数字 1 和 0。

    示例 1:
    输入: a = "11", b = "1"
    输出: "100"

    示例 2:
    输入: a = "1010", b = "1011"
    输出: "10101"
     

    提示：
    每个字符串仅由字符 '0' 或 '1' 组成。
    1 <= a.length, b.length <= 10^4
    字符串如果不是 "0" ，就都不含前导零。

"""


class Solution:
    def addBinary(self, a, b):
        res = ''
        a_id, b_id = len(a) - 1, len(b) - 1
        carry = 0
        while a_id >= 0 or b_id >= 0:
            tmp_a = int(a[a_id]) if a_id >= 0 else 0
            tmp_b = int(b[b_id]) if b_id >= 0 else 0
            tmp = tmp_a + tmp_b + carry
            if tmp >= 2:
                carry = 1
                res = str(tmp - 2) + res
            else:
                carry = 0
                res = str(tmp) + res
            a_id -= 1
            b_id -= 1
        if carry:
            res = '1' + res

        return res
