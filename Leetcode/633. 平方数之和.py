# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-05 15:28
 @Author  : QDY
 @FileName: 633. 平方数之和.py
 @Software: PyCharm
"""
"""
给定一个非负整数c，你要判断是否存在两个整数 a 和 b，使得a2 + b2 = c 。

示例 1：
输入：c = 5
输出：true
解释：1 * 1 + 2 * 2 = 5

示例 2：
输入：c = 3
输出：false

示例 3：
输入：c = 4
输出：true

示例 4：
输入：c = 2
输出：true

示例 5：
输入：c = 1
输出：true

提示：
0 <= c <= 231 - 1

"""


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # ss = set()
        # for i in range(int(c**0.5)+1):
        #     tmp = i**2
        #     ss.add(tmp)
        #     if c-tmp in ss:return True
        # return False
        # l, r = 0, int(c**0.5)  # 双指针
        # ll, rr = 0, r*r
        # while l<=r:
        #     if ll + rr == c:return True
        #     elif ll+rr < c:
        #         l += 1
        #         ll = l**2
        #     else:
        #         r -= 1
        #         rr = r**2
        # return False

        # 一个非负整数 c 能够表示为两个整数的平方和，当且仅当 c 的所有形如 4k+3 的质因子的幂次均为偶数。
        if c <= 2: return True
        factor = 2
        while factor ** 2 <= c:
            if c % factor == 0:
                cnt = 0
                while c % factor == 0:
                    c //= factor
                    cnt += 1
                if factor % 4 == 3 and cnt & 1: return False
            factor += 1
        return c % 4 != 3  # 最后剩下的因子，幂次为1，不能是4k+3的形式
