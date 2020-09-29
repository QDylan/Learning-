# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-29 9:54
 @Author  : QDY
 @FileName: 396. 旋转函数.py
 @Software: PyCharm
"""
"""
给定一个长度为 n 的整数数组A。

假设Bk是数组A顺时针旋转 k 个位置后的数组，我们定义A的“旋转函数”F为：

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]。

计算F(0), F(1), ..., F(n-1)中的最大值。

注意:
可以认为 n 的值小于 105。

示例:
A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
所以 F(0), F(1), F(2), F(3) 中的最大值是 F(3) = 26 。

"""


class Solution:
    def maxRotateFunction(self, A) -> int:
        if not A: return 0
        N = len(A)
        res = tmp = sum(i * A[i] for i in range(N))  # 初始状态
        sumA = sum(A)
        for i in range(N - 1, 0, -1):
            tmp += sumA - A[i] - A[i] * (N - 1)
            res = max(tmp, res)
            # print(tmp)
        return res
