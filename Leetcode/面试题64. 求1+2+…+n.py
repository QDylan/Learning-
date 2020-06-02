# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/2 9:06
 @Author  : QDY
 @FileName: 面试题64. 求1+2+…+n.py

    求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

    示例 1：
    输入: n = 3
    输出: 6

    示例 2：
    输入: n = 9
    输出: 45

"""


class Solution:
    def __init__(self):
        self.res = 0

    def sumNums(self, n):
        # 逻辑短路
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res
