# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-28 10:09
 @Author  : QDY
 @FileName: 274. H 指数.py
 @Software: PyCharm
"""


class Solution:
    def hIndex(self, citations) -> int:
        if not citations: return 0
        N = len(citations)
        bucket = [0] * (N + 1)
        for c in citations:  # 计数排序
            if c >= N:
                bucket[N] += 1
            else:
                bucket[c] += 1
        H = 0
        for i in range(N, -1, -1):
            while bucket[i] > 0 and i > H:
                H += 1
                bucket[i] -= 1
        return H
