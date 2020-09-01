# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/15 22:56
 @Author  : QDY
 @FileName: 37. 解数独_回溯_hard.py

    编写一个程序，通过已填充的空格来解决数独问题。

    一个数独的解法需遵循如下规则：

    数字1-9在每一行只能出现一次。
    数字1-9在每一列只能出现一次。
    数字1-9在每一个以粗实线分隔的3x3宫内只能出现一次。
    空白格用'.'表示。

    Note:

    给定的数独序列只包含数字 1-9 和字符 '.' 。
    你可以假设给定的数独只有唯一解。
    给定数独永远是 9x9 形式的。

    输入：
    [["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]
    输出：
    [["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]]
"""


class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for i in range(9)]
        columns = [set() for i in range(9)]
        boxes = [[set(), set(), set()] for i in range(3)]

        for i in range(9):  # 把已有的元素放入
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    columns[j].add(board[i][j])
                    boxes[i // 3][j // 3].add(board[i][j])

        # print(boxes)
        def check(num, x, y):  # 检查num是否可以放在(x,y)处
            if num in rows[x] or num in columns[y] or num in boxes[x // 3][y // 3]:
                return False
            return True

        def place_next(row, col):  # 放置（row,col）的下一个数
            if row == 8 and col == 8:  # 若到达了最后一个，说明找到了一种解法
                nonlocal solved
                solved = True
            else:
                if col == 8:  # 到了最后一列，下一个要处理的位置是(row+1,0)
                    backtrace(row + 1, 0)
                else:  #
                    backtrace(row, col + 1)

        def backtrace(row, col):
            if board[row][col] == '.':
                for i in range(1, 10):
                    n = str(i)
                    if check(n, row, col):
                        rows[row].add(n)  # 添加n
                        columns[col].add(n)
                        boxes[row // 3][col // 3].add(n)
                        board[row][col] = n

                        place_next(row, col)  # 设置下一个元素

                        if not solved:  # 若solved仍为False，说明这个位置不能放n，需要尝试下一个(n+1)
                            rows[row].remove(n)  # 还原
                            columns[col].remove(n)
                            boxes[row // 3][col // 3].remove(n)
                            board[row][col] = '.'
            else:  # 若已有设置好的元素，直接设置下一个位置
                place_next(row, col)

        solved = False
        backtrace(0, 0)
