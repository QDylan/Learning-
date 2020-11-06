# -*- coding: utf-8 -*-
"""
 @Time    : 2020-11-06 10:55
 @Author  : QDY
 @FileName: 556. 下一个更大元素 III.py
 @Software: PyCharm
"""
"""
给定一个32位正整数n，你需要找到最小的32位整数，其与n中存在的位数完全相同，并且其值大于n。如果不存在这样的32位整数，则返回-1。

示例 1:

输入: 12
输出: 21
示例 2:

输入: 21
输出: -1

"""


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        limit = 2 ** 31
        if n >= limit - 1: return -1
        ns = str(n)
        N = len(ns)
        for i in range(N - 2, -1, -1):
            if int(ns[i]) < int(ns[i + 1]):
                tmp = ns[i + 1:][::-1]
                for j in range(len(tmp)):
                    if int(ns[i]) < int(tmp[j]):
                        res = int(ns[:i] + tmp[j] + tmp[:j] + ns[i] + tmp[j + 1:])
                        return res if res < limit else -1
        return -1
