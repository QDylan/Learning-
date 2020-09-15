# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-15 11:07
 @Author  : QDY
 @FileName: 187. 重复的DNA序列.py
 @Software: PyCharm
"""
from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences(self, s: str):
        if len(s) < 11: return []
        res = []
        h = defaultdict(int)
        # for i in range(10,len(s)+1):
        #     strs = s[i-10:i]
        #     h[strs] += 1
        #     if h[strs] == 2:res.append(strs)
        # return res
        RK, hi = {'A': 0, 'C': 1, 'G': 2, 'T': 3}, 0  # Rabin_Krap算法
        for i in range(10):
            hi += RK[s[i]] * (4 ** (9 - i))
        h[hi] += 1
        for i in range(len(s) - 10):
            hi = hi * 4 - RK[s[i]] * (4 ** 10) + RK[s[i + 10]]
            h[hi] += 1
            if h[hi] == 2: res.append(s[i + 1:i + 11])
        return res
