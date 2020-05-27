# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/27 10:15
 @Author  : QDY
 @FileName: 974. 和可被 K 整除的子数组_前缀和_同余定理.py

    给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。

    示例：
    输入：A = [4,5,0,-2,-3,1], K = 5
    输出：7
    解释：
    有 7 个子数组满足其元素之和可被 K = 5 整除：
    [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

"""


class Solution:
    def subarraysDivByK(self, A, K) -> int:
        len_a = len(A)
        prefix = 0  # 前缀和
        remainder = {0: 1}  # prefix中被K除的不同余数的个数
        for i in range(len_a):
            prefix += A[i]
            r = prefix % K
            remainder[r] = remainder.get(r, 0) + 1
        # 若prefix[i]与prefix[j]被K除的余数相同(j>i)，那么prefix[j]-prefix[i]被K整除
        # 取组合数C(2,remainder[i])关于i的求和
        return sum(remainder[i] * (remainder[i] - 1) // 2 for i in remainder)
