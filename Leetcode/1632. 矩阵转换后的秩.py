# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-27 10:34
 @Author  : QDY
 @FileName: 1632. 矩阵转换后的秩.py
 @Software: PyCharm
"""
"""
给你一个m x n的矩阵 matrix，请你返回一个新的矩阵answer，其中answer[row][col]是matrix[row][col]的秩。

每个元素的秩是一个整数，表示这个元素相对于其他元素的大小关系，它按照如下规则计算：

如果一个元素是它所在行和列的最小值，那么它的 秩为 1。
如果两个元素p 和q在 同一行或者 同一列，那么：
如果p < q ，那么rank(p) < rank(q)
如果p == q，那么rank(p) == rank(q)
如果p > q，那么rank(p) > rank(q)
秩需要越 小越好。
题目保证按照上面规则answer数组是唯一的。

示例 1：
输入：matrix = [[1,2],[3,4]]
输出：[[1,2],[2,3]]
解释：
matrix[0][0] 的秩为 1 ，因为它是所在行和列的最小整数。
matrix[0][1] 的秩为 2 ，因为 matrix[0][1] > matrix[0][0] 且 matrix[0][0] 的秩为 1 。
matrix[1][0] 的秩为 2 ，因为 matrix[1][0] > matrix[0][0] 且 matrix[0][0] 的秩为 1 。
matrix[1][1] 的秩为 3 ，因为 matrix[1][1] > matrix[0][1]， 
matrix[1][1] > matrix[1][0] 且 matrix[0][1] 和 matrix[1][0] 的秩都为 2 。

示例 2：
输入：matrix = [[7,7],[7,7]]
输出：[[1,1],[1,1]]

示例 3：
输入：matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
输出：[[4,2,3],[1,3,4],[5,1,6],[1,3,4]]

示例 4：
输入：matrix = [[7,3,6],[1,4,5],[9,8,2]]
输出：[[5,1,4],[1,2,3],[6,3,1]]

提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 500
-109 <= matrix[row][col] <= 109

"""
from collections import defaultdict


class Solution:
    def matrixRankTransform(self, matrix):
        h, w = len(matrix), len(matrix[0])
        M = max(h, w)
        res = [[0] * w for _ in range(h)]
        countR, countC = [0] * h, [0] * w

        # 按元素大小分别存储元素坐标
        pos = defaultdict(list)
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                pos[val].append((r, c))

        union = list(range(M * 2))  # 并查集用于合并行或列相同的元素

        def find(i):  # 寻根
            if union[i] == i: return i
            union[i] = find(union[i])
            return union[i]

        for val in sorted(pos.keys()):  # 按val的顺序填表

            for r, c in pos[val]:  # 用并查集合并行和列相同的元素并分组
                union[find(r)] = find(c + M)

            pool = defaultdict(list)
            for r, c in pos[val]:
                pool[find(r)].append((r, c))

            # 行和列相同的元素，共享相同的rank
            for group in pool.values():
                rank = max(max((countR[r], countC[c])) for r, c in group) + 1
                for r, c in group:
                    countR[r] = countC[c] = res[r][c] = rank
                    # 重置并查集
                    union[r] = r
                    union[c + M] = c + M
        return res
