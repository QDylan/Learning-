# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/27 15:04
 @Author  : QDY
 @FileName: 247. 中心对称数 II.py
 @Software: PyCharm
"""
"""
中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。
找到所有长度为 n 的中心对称数。

示例 :
输入:  n = 2
输出: ["11","69","88","96"]

"""


class Solution:
    def findStrobogrammatic(self, n):
        if n == 1: return ['0', '1', '8']
        c = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        self.res = []
        m = n // 2

        def dfs(part1, part2):
            if len(part1) == m:
                if n & 1:
                    for i in ('0', '1', '8'):
                        self.res.append(part1 + i + part2)
                else:
                    self.res.append(part1 + part2)
                return
            for num in c:
                dfs(part1 + num, c[num] + part2)

        for i in ('1', '6', '8', '9'):
            dfs(i, c[i])
        return self.res
