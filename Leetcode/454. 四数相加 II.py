# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/2 16:27
 @Author  : QDY
 @FileName: 454. 四数相加 II.py

    给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。
    为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。
    所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

    例如:
    输入:
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]

    输出:
    2

    解释:
    两个元组如下:
    1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
    2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

"""
from collections import defaultdict


class Solution:
    def fourSumCount(self, A, B, C, D) -> int:
        A_B = defaultdict(int)
        N = len(A)
        if N == 0: return 0
        for i in range(N):  # 遍历A,B，将他们的和存入哈希表，键值为出现的次数
            for j in range(N):
                A_B[A[i] + B[j]] += 1

        res = 0
        for i in range(N):  # 遍历C,D，若他们的和的相反数出现在A_B中，更新res
            for j in range(N):
                tmp = -(C[i] + D[j])
                if tmp in A_B:
                    res += A_B[tmp]

        return res
