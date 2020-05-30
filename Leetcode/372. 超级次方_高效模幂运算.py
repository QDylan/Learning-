# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/30 11:06
 @Author  : QDY
 @FileName: 372. 超级次方_高效模幂运算.py

    你的任务是计算 ab 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。

    示例 1:
    输入: a = 2, b = [3]
    输出: 8

    示例 2:
    输入: a = 2, b = [1,0]
    输出: 1024

"""


class Solution:
    def superPow(self, a, b):
        base = 1337

        def quickPow(n, k):
            if k == 0: return 1

            n %= base
            if k % 2:
                return (n * quickPow(n, k - 1)) % base
            else:
                return (quickPow(n, k // 2) ** 2) % base

        if not b: return 1
        part1 = quickPow(a, b.pop())
        part2 = quickPow(self.superPow(a, b), 10)
        return (part1 * part2) % base
