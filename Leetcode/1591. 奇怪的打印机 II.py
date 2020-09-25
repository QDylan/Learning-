# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-25 11:29
 @Author  : QDY
 @FileName: 1591. 奇怪的打印机 II.py
 @Software: PyCharm
"""
"""
给你一个奇怪的打印机，它有如下两个特殊的打印规则：

每一次操作时，打印机会用同一种颜色打印一个矩形的形状，每次打印会覆盖矩形对应格子里原本的颜色。
一旦矩形根据上面的规则使用了一种颜色，那么 相同的颜色不能再被使用。
给你一个初始没有颜色的m x n的矩形targetGrid，其中targetGrid[row][col]是位置(row, col)的颜色。

如果你能按照上述规则打印出矩形targetGrid，请你返回true，否则返回false。

示例 1：
输入：targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
输出：true

示例 2：
输入：targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
输出：true

示例 3：
输入：targetGrid = [[1,2,1],[2,1,2],[1,2,1]]
输出：false
解释：没有办法得到 targetGrid ，因为每一轮操作使用的颜色互不相同。

示例 4：
输入：targetGrid = [[1,1,1],[3,1,3]]
输出：false

提示：
m == targetGrid.length
n == targetGrid[i].length
1 <= m, n <= 60
1 <= targetGrid[row][col] <= 60

"""
from collections import defaultdict


class Solution:
    def isPrintable(self, targetGrid):  # 逆涂色
        graph, h, w = defaultdict(list), len(targetGrid), len(targetGrid[0])
        for i in range(h):  # 构图, 将点按颜色分类
            for j in range(w):
                graph[targetGrid[i][j]].append((i, j))

        def check(color):  # 检测某颜色是否能被合法涂上
            xmin, xmax, ymin, ymax = 60, 0, 60, 0
            for x, y in graph[color]:  # 找出该颜色的矩形边界
                xmax, xmin = max(xmax, x), min(xmin, x)
                ymax, ymin = max(ymax, y), min(ymin, y)
            for i in range(xmin, xmax + 1):
                for j in range(ymin, ymax + 1):  # 该颜色的边界内，所有都是该颜色或是0（表示将会被涂上别的颜色）
                    if targetGrid[i][j] != color and targetGrid[i][j] != 0: return False
            return True

        while len(graph) > 0:
            delete, valid = [], False
            for color in graph:
                if check(color):
                    valid = True  # 将该种颜色加入待删除数组
                    delete.append(color)
            # print(delete)
            if not valid: return False
            for color in delete:
                for x, y in graph[color]:
                    targetGrid[x][y] = 0
                graph.pop(color)
        return True
