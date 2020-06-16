# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/16 16:20
 @Author  : QDY
 @FileName: 43. 字符串相乘.py

    给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

    示例 1:
    输入: num1 = "2", num2 = "3"
    输出: "6"

    示例 2:
    输入: num1 = "123", num2 = "456"
    输出: "56088"

    说明：
    num1 和 num2 的长度小于110。
    num1 和 num2 只包含数字 0-9。
    num1 和 num2 均不以零开头，除非是数字 0 本身。
    不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

"""


class Solution:
    def multiply(self, num1, num2):
        # return str(int(num1)*int(num2))
        if num1 == '0' or num2 == '0': return '0'
        n1, n2 = len(num1), len(num2)
        res = '0'
        for i in range(n1 - 1, -1, -1):
            product = ''
            if num1[i] == 0: continue
            m = int(num1[i])
            carry = 0
            for j in range(n2 - 1, -1, -1):  # 逐个位置相乘
                tmp = m * int(num2[j]) + carry
                product = str(tmp % 10) + product
                carry = tmp // 10
            if carry:
                product = str(carry) + product
            product += '0' * (n1 - 1 - i)
            # print(product)
            p, r, carry = len(product) - 1, len(res) - 1, 0
            tmp_res = ''
            while p >= 0 or r >= 0:  # 逐个位置相加
                p_ = int(product[p]) if p >= 0 else 0
                r_ = int(res[r]) if r >= 0 else 0
                tmp = p_ + r_ + carry
                carry = tmp // 10
                tmp_res = str(tmp % 10) + tmp_res
                p -= 1
                r -= 1
            res = tmp_res
            if carry:
                res = '1' + res
            # print(res)
        return res
