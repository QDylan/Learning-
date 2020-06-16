# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/16 11:15
 @Author  : QDY
 @FileName: 365. 水壶问题_贝祖定理.py

    有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？
    如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。

    你允许：
    装满任意一个水壶
    清空任意一个水壶
    从一个水壶向另外一个水壶倒水，直到装满或者倒空

    示例 1: (From the famous "Die Hard" example)
    输入: x = 3, y = 5, z = 4
    输出: True

    示例 2:
    输入: x = 2, y = 6, z = 5
    输出: False

"""


class Solution:
    def canMeasureWater(self, x, y, z):
        if z > x + y:
            return False
        if z == 0:
            return True
        if x < y:
            x, y = y, x
        if y == 0:
            return z == x
        while x % y != 0:  # 带余除法求x,y的最大公约数
            x, y = y, x % y

        return z % y == 0
