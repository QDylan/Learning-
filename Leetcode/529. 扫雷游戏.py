# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/20 10:17
 @Author  : QDY
 @FileName: 529. 扫雷游戏.py
 @Software: PyCharm
"""
"""
    让我们一起来玩扫雷游戏！
    
    给定一个代表游戏板的二维字符矩阵。'M'代表一个未挖出的地雷，'E'代表一个未挖出的空方块，
    'B'代表没有相邻（上，下，左，右，和所有4个对角线）地雷的已挖出的空白方块，
    数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X'则表示一个已挖出的地雷。
    
    现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：
    
    如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为'X'。
    如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的未挖出方块都应该被递归地揭露。
    如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
    如果在此次点击中，若无更多方块可被揭露，则返回面板。
    
    示例 1：
    输入: 
    
    [['E', 'E', 'E', 'E', 'E'],
     ['E', 'E', 'M', 'E', 'E'],
     ['E', 'E', 'E', 'E', 'E'],
     ['E', 'E', 'E', 'E', 'E']]
    
    Click : [3,0]
    
    输出: 
    
    [['B', '1', 'E', '1', 'B'],
     ['B', '1', 'M', '1', 'B'],
     ['B', '1', '1', '1', 'B'],
     ['B', 'B', 'B', 'B', 'B']]
    
    解释:
    
    示例 2：
    
    输入: 
    [['B', '1', 'E', '1', 'B'],
     ['B', '1', 'M', '1', 'B'],
     ['B', '1', '1', '1', 'B'],
     ['B', 'B', 'B', 'B', 'B']]
    Click : [1,2]
    
    输出: 
    [['B', '1', 'E', '1', 'B'],
     ['B', '1', 'X', '1', 'B'],
     ['B', '1', '1', '1', 'B'],
     ['B', 'B', 'B', 'B', 'B']]
    
    解释:
    注意：
    输入矩阵的宽和高的范围为 [1,50]。
    点击的位置只能是未被挖出的方块 ('M' 或者 'E')，这也意味着面板至少包含一个可点击的方块。
    输入面板不会是游戏结束的状态（即有地雷已被挖出）。
    简单起见，未提及的规则在这个问题中可被忽略。例如，当游戏结束时你不需要挖出所有地雷，考虑所有你可能赢得游戏或标记方块的情况。

"""
from collections import deque
class Solution:
    def updateBoard(self, board, click):
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        h, w = len(board), len(board[0])
        # def dfs(x,y):
        #     board[x][y] = 0
        #     tmp = []
        #     for x_,y_ in ((x+1,y+1),(x,y+1),(x-1,y+1),(x+1,y),(x-1,y),(x+1,y-1),(x,y-1),(x-1,y-1)):
        #         if 0<=x_<h and 0<=y_<w:
        #             if board[x_][y_] in ('M','X'):
        #                 board[x][y] += 1
        #             elif board[x_][y_] == 'E':
        #                 tmp.append((x_,y_))
        #     if board[x][y] == 0:
        #         board[x][y] = 'B'
        #         for x_,y_ in tmp:
        #             dfs(x_,y_)
        #     else: board[x][y] = str(board[x][y])
        # dfs(click[0],click[1])

        q = deque([(click[0],click[1])])
        visited = {(click[0],click[1])}
        while q:
            length = len(q)
            for i in range(length):
                x,y = q.popleft()
                board[x][y] = 0
                tmp = []
                for x_,y_ in ((x+1,y+1),(x,y+1),(x-1,y+1),(x+1,y),(x-1,y),(x+1,y-1),(x,y-1),(x-1,y-1)):
                    if 0<=x_<h and 0<=y_<w:
                        if board[x_][y_] in ('M','X'):
                            board[x][y] += 1
                        elif board[x_][y_] == 'E':
                            tmp.append((x_,y_))
                if board[x][y] == 0:
                    board[x][y] = 'B'
                    for x_,y_ in tmp:
                        if (x_,y_) not in visited:
                            visited.add((x_,y_))
                            q.append((x_,y_))
                else:board[x][y] = str(board[x][y])
        return board
