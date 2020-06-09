# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/9 10:34
 @Author  : QDY
 @FileName: 130. 被围绕的区域_DFS.py

    给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
    找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

    示例:
    X X X X
    X O O X
    X X O X
    X O X X

    运行你的函数后，矩阵变为：
    X X X X
    X X X X
    X X X X
    X O X X

    解释:
    被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
    任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。
    如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

"""


class Solution:
    def solve(self, board):
        if not board: return
        """
        Do not return anything, modify board in-place instead.
        """
        # DFS 遍历四周的'O'，把与其相连的'O'修改为'#'，再把还是'O'的修改为'X'，最后把'#'还原
        height, width = len(board), len(board[0])
        if height <= 2 or width <= 2: return  # 每个元素都在边上

        def dfs(i, j):
            if i < 0 or i == height or j < 0 or j == width or board[i][j] != 'O':
                return
            board[i][j] = '#'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for w in range(width):
            if board[0][w] == 'O':
                dfs(0, w)
            if board[height - 1][w] == 'O':
                dfs(height - 1, w)
        for h in range(1, height - 1):
            if board[h][0] == 'O':
                dfs(h, 0)
            if board[h][width - 1] == 'O':
                dfs(h, width - 1)

        for h in range(height):
            for w in range(width):
                if board[h][w] == 'O':
                    board[h][w] = 'X'
                elif board[h][w] == '#':
                    board[h][w] = 'O'
