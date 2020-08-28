# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/30 9:05
 @Author  : QDY
 @FileName: 498. 对角线遍历.py
 @Software: PyCharm
"""
"""
    给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素。

    示例:
    输入:
    [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
    ]

    输出:  [1,2,4,7,5,3,6,8,9]

"""


class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        res = []
        x, y, up = 0, 0, True
        while True:
            # print(x,y)
            res.append(matrix[x][y])
            if x == m - 1 and y == n - 1: return res
            if up:
                if x - 1 >= 0 and y + 1 < n:
                    x -= 1
                    y += 1
                elif y + 1 < n:
                    y += 1
                    up = False
                else:
                    x += 1
                    up = False
            else:
                if x + 1 < m and y - 1 >= 0:
                    x += 1
                    y -= 1
                elif x + 1 < m:
                    x += 1
                    up = True
                else:
                    y += 1
                    up = True
