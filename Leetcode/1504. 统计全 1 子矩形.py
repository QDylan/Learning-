# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/10 17:40
 @Author  : QDY
 @FileName: 1504. 统计全 1 子矩形.py

给你一个只包含 0 和 1 的rows * columns矩阵mat，请你返回有多少个子矩形的元素全部都是 1 。

示例 1：
输入：mat = [[1,0,1],
           [1,1,0],
           [1,1,0]]
输出：13
解释：
有 6个 1x1 的矩形。
有 2 个 1x2 的矩形。
有 3 个 2x1 的矩形。
有 1 个 2x2 的矩形。
有 1 个 3x1 的矩形。
矩形数目总共 = 6 + 2 + 3 + 1 + 1 = 13。

示例 2：
输入：mat = [[0,1,1,0],
           [0,1,1,1],
           [1,1,1,0]]
输出：24
解释：
有 8 个 1x1 的子矩形。
有 5 个 1x2 的子矩形。
有 2 个 1x3 的子矩形。
有 4 个 2x1 的子矩形。
有 2 个 2x2 的子矩形。
有 2 个 3x1 的子矩形。
有 1 个 3x2 的子矩形。
矩形数目总共 = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24 。

示例 3：
输入：mat = [[1,1,1,1,1,1]]
输出：21

示例 4：
输入：mat = [[1,0,1],[0,1,0],[1,0,1]]
输出：5

提示：
1 <= rows<= 150
1 <= columns<= 150
0 <= mat[i][j] <= 1

"""


class Solution:
    def numSubmat(self, mat):
        if not mat: return 0
        h, w = len(mat), len(mat[0])
        res = 0
        for i in range(h):
            for j in range(w):
                if j > 0 and mat[i][j] == 1:  # 计算以(i,j)为矩阵的右下角，所能形成的宽度为1的矩形数量
                    mat[i][j] += mat[i][j - 1]

        for i in range(h):
            for j in range(w):
                if mat[i][j] > 0:
                    tmp = mat[i][j]  # 计算以(i,j)为矩阵的右下角，所能形成的矩形数量
                    for k in range(i, -1, -1):  # tmp表示以(k,j)为一维矩形的长度
                        if mat[k][j] > 0:  # 向上扩展寻找，以(k,j)为右上角和以(i,j)为右下角组成的矩形
                            tmp = min(tmp, mat[k][j])  # 新增一行能增加的矩形的数量，由最短的一行的长度决定
                            res += tmp
                        else:
                            break
        return res
