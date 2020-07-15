# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/15 9:50
 @Author  : QDY
 @FileName: 59. 螺旋矩阵 II.py

    给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

    示例:
    输入: 3
    输出:
    [
     [ 1, 2, 3 ],
     [ 8, 9, 4 ],
     [ 7, 6, 5 ]
    ]

"""


class Solution:
    def generateMatrix(self, n: int):
        m = [[0] * n for i in range(n)]
        left_top = 0
        i, j = 0, 0
        for x in range(1, n ** 2 + 1):
            m[i][j] = x
            if i == left_top and j != n - 1:
                j += 1
            elif i != n - 1 and j == n - 1:
                i += 1
            elif i == n - 1 and j != left_top:
                j -= 1
            elif i != left_top + 1 and j == left_top:
                i -= 1
            else:
                n -= 1
                left_top += 1
                i = left_top
                j = left_top
        return m

        # tmp = 1
        # while n>0:
        #     for j in range(left_top,n):
        #         m[left_top][j] = tmp
        #         tmp += 1
        #     for i in range(left_top+1,n):
        #         m[i][n-1] = tmp
        #         tmp += 1
        #     for j in range(n-2,left_top-1,-1):
        #         m[n-1][j] = tmp
        #         tmp += 1
        #     for i in range(n-2,left_top,-1):
        #         m[i][left_top] = tmp
        #         tmp += 1
        #     n -= 1
        #     left_top += 1
        # return m
