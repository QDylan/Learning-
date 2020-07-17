# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/17 9:14
 @Author  : QDY
 @FileName: 862. 和至少为 K 的最短子数组_单调队列_hard.py

    返回 A 的最短的非空连续子数组的长度，该子数组的和至少为 K 。
    如果没有和至少为 K 的非空子数组，返回 -1 。

    示例 1：
    输入：A = [1], K = 1
    输出：1

    示例 2：
    输入：A = [1,2], K = 4
    输出：-1

    示例 3：
    输入：A = [2,-1,2], K = 3
    输出：3

"""
from collections import deque


class Solution:
    def shortestSubarray(self, A, K):
        if not A: return -1
        n = len(A)

        prefix = [0]  # 前缀和
        for i in range(n):
            if A[i] >= K: return 1
            prefix.append(prefix[-1] + A[i])

        win, res = deque(), n + 1  # win为双端队列，存储prefix的索引，使得prefix[win[i]]<prefix[win[i+1]]
        for i in range(n + 1):  # 找到prefix中的索引x,y使得prefix[y]-prefix[x]>=K
            while win and prefix[i] <= prefix[win[-1]]:  # 保证队列末的索引指向的前缀和最大（队首的最小）
                win.pop()
            while win and prefix[i] - prefix[win[0]] >= K:  # 找到这样的y=i,x=win[0]
                res = min(res, i - win.popleft())  # 求最小的y-x
            win.append(i)
        return res if res < n + 1 else -1
