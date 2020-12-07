# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/10 8:52
 @Author  : QDY
 @FileName: 9. 回文数.py
    判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

    示例 1:
    输入: 121
    输出: true

    示例2:
    输入: -121
    输出: false
    解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

    示例 3:
    输入: 10
    输出: false
    解释: 从右向左读, 为 01 。因此它不是一个回文数。

    进阶:
    你能不将整数转为字符串来解决这个问题吗？

"""


class Solution:
    def isPalindrome(self, x):
        if x < 0 or (x != 0 and x % 10 == 0): return False
        if x < 10: return True
        num = 0
        while x > num:  # 反转一半的数字
            num = num * 10 + x % 10
            x //= 10
        # 数位为偶数时相等，为奇数时num比x多了最后一位
        return x == num or x == num // 10
