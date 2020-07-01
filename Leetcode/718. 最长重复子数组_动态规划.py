# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/1 9:09
 @Author  : QDY
 @FileName: 718. 最长重复子数组_动态规划.py

    给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

    示例 1:
    输入:
    A: [1,2,3,2,1]
    B: [3,2,1,4,7]
    输出: 3
    解释:
    长度最长的公共子数组是 [3, 2, 1]。

    说明:
    1 <= len(A), len(B) <= 1000
    0 <= A[i], B[i] < 100


"""


class Solution:
    def findLength(self, A, B):
        # 动态规划
        # dp[i][j] = 以A[i]结尾与以B[j]结尾的公共最长子数组
        # dp[0][j] = 1 if A[0]==B[j] else 0
        # dp[1][j] = 1+dp[0][j-1] if A[1]==B[j]
        # dp[n][j] = 1+dp[n-1][j-1] if A[1]==B[j]

        a, b = len(A), len(B)
        dp = [1 if A[0] == B[j] else 0 for j in range(b)]
        res = 0
        for i in range(1, a):
            for j in range(b - 1, -1, -1):
                if A[i] == B[j]:
                    dp[j] = 1
                    if j > 0:
                        dp[j] += dp[j - 1]
                else:
                    dp[j] = 0
            res = max(res, max(dp))

        return res
