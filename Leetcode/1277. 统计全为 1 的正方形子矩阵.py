# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/24 11:28
 @Author  : QDY
 @FileName: 1277. 统计全为 1 的正方形子矩阵.py
 @Software: PyCharm
"""
"""
    给你一个m * n的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。

    示例 1：
    输入：matrix =
    [
     [0,1,1,1],
     [1,1,1,1],
     [0,1,1,1]
    ]
    输出：15
    解释： 
    边长为 1 的正方形有 10 个。
    边长为 2 的正方形有 4 个。
    边长为 3 的正方形有 1 个。
    正方形的总数 = 10 + 4 + 1 = 15.

    示例 2：
    输入：matrix = 
    [
    [1,0,1],
    [1,1,0],
    [1,1,0]
    ]
    输出：7
    解释：
    边长为 1 的正方形有 6 个。 
    边长为 2 的正方形有 1 个。
    正方形的总数 = 6 + 1 = 7.
    
    提示：
    1 <= arr.length<= 300
    1 <= arr[0].length<= 300
    0 <= arr[i][j] <= 1

"""


class Solution:
    def countSquares(self, matrix):
        h, w = len(matrix), len(matrix[0])
        res = 0
        for i in range(h):  # 原地动态规划
            for j in range(w):  # matrix[i][j] 记录以(i,j)为正方形的右下角能构造多少个正方形
                if i and j and matrix[i][j]:  # 第一行和第一列的只能有1个
                    matrix[i][j] += min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1])
                res += matrix[i][j]
        return res
