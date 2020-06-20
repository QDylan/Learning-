# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/20 19:57
 @Author  : QDY
 @FileName: 343. 整数拆分.py

    给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

    示例 1:
    输入: 2
    输出: 1
    解释: 2 = 1 + 1, 1 × 1 = 1。

    示例 2:
    输入: 10
    输出: 36
    解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
    说明: 你可以假设 n 不小于 2 且不大于 58。

"""

class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=3:return n-1
        num = n//3  # 尽量把n用每份为3来分割
        r = n-3*num  # r = n % 3
        if r==2:  # 余 2，则最后一个乘以2
            return (3**num)*2
        elif r==1: # 若余1，则最后一个3变为4
            return (3**(num-1))*4
        else:
            return 3**num