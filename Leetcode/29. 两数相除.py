# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/13 9:42
 @Author  : QDY
 @FileName: 29. 两数相除.py

    给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
    返回被除数 dividend 除以除数 divisor 得到的商。
    整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

    示例 1:
    输入: dividend = 10, divisor = 3
    输出: 3
    解释: 10/3 = truncate(3.33333..) = truncate(3) = 3

    示例 2:
    输入: dividend = 7, divisor = -3
    输出: -2
    解释: 7/-3 = truncate(-2.33333..) = -2
     

    提示：
    被除数和除数均为 32 位有符号整数。
    除数不为 0。
    假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。

"""


class Solution:
    def divide(self, dividend, divisor):
        res = 0
        sgn = 1

        if dividend < 0:
            dividend = -dividend
            sgn = -sgn
        if divisor < 0:
            divisor = -divisor
            sgn = -sgn

        for n in range(31, -1, -1):
            if divisor << n <= dividend:
                res += 1 << n
                dividend -= divisor << n
            if dividend < divisor: break

        if sgn < 0: res = -res
        return min((1 << 31) - 1, res) if res >= 0 else max(-1 << 31, res)
