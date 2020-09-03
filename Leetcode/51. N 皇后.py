# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-03 9:32
 @Author  : QDY
 @FileName: 51. N 皇后.py
 @Software: PyCharm
"""
"""
给定一个整数 n，返回所有不同的n皇后问题的解决方案。

每一种解法包含一个明确的n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例：

输入：4
输出：[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。


提示：
皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。

"""

class Solution:
    def solveNQueens(self, n):
        res = []

        def dfs(mat, i, used):
            if i == n:
                res.append([''.join(mat[j]) for j in range(n)])
                return
            for j in range(n):
                if j not in used:
                    used.add(j)
                    left, right = j - 1, j + 1
                    valid = True
                    for prev_i in range(i - 1, -1, -1):
                        if (left >= 0 and mat[prev_i][left] == 'Q') or (right < n and mat[prev_i][right] == 'Q'):
                            valid = False
                            break
                        left -= 1
                        right += 1
                    if valid:
                        mat[i][j] = 'Q'
                        dfs(mat, i + 1, used)
                    used.discard(j)
                    mat[i][j] = '.'

        dfs([['.'] * n for _ in range(n)], 0, set())
        return res