# -*- coding: utf-8 -*-
"""
 @Time    : 2020-11-12 9:49
 @Author  : QDY
 @FileName: 922. 按奇偶排序数组 II.py
 @Software: PyCharm
"""
"""
给定一个非负整数数组A， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当A[i] 为奇数时，i也是奇数；当A[i]为偶数时， i 也是偶数。
你可以返回任何满足上述条件的数组作为答案。


示例：
输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。

提示：
2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
"""


class Solution:
    def sortArrayByParityII(self, A):
        odd, even, N = 1, 0, len(A)
        while odd < N and even < N:
            if A[odd] & 1:
                odd += 2
                continue
            if not A[even] & 1:
                even += 2
                continue
            A[even], A[odd] = A[odd], A[even]
            odd += 2
            even += 2
        return A
