# -*- coding: utf-8 -*-
"""
 @Time    : 2020-11-03 9:51
 @Author  : QDY
 @FileName: 941. 有效的山脉数组.py
 @Software: PyCharm
"""
"""
给定一个整数数组A，如果它是有效的山脉数组就返回true，否则返回 false。

让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：

A.length >= 3
在0 < i< A.length - 1条件下，存在i使得：
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]

示例 1：
输入：[2,1]
输出：false

示例 2：
输入：[3,5,5]
输出：false

示例 3：
输入：[0,3,2,1]
输出：true

提示：
0 <= A.length <= 10000
0 <= A[i] <= 10000

"""


class Solution:
    def validMountainArray(self, A) -> bool:
        # N = len(A)
        # if N<3:return False
        # if A[0]>A[1]:return False
        # down = False
        # for i in range(1,N):
        #     if A[i]==A[i-1]:return False
        #     if A[i]<A[i-1] and not down:
        #         down = True
        #     elif A[i]>A[i-1] and down:
        #         return False
        # return down

        l, r = 0, len(A) - 1  # 双指针
        while l < r and A[l] < A[l + 1]: l += 1
        while r > l and A[r] < A[r - 1]: r -= 1
        return l == r and l != 0 and r != len(A) - 1
