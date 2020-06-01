# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/1 10:58
 @Author  : QDY
 @FileName: 5426. 重新规划路线_Graph_BFS_DFS.py

n 座城市，从 0 到 n-1 编号，其间共有 n-1 条路线。因此，要想在两座不同城市之间旅行只有唯一一条路线可供选择（路线网形成一颗树）。
去年，交通运输部决定重新规划路线，以改变交通拥堵的状况。
路线用 connections 表示，其中 connections[i] = [a, b] 表示从城市 a 到 b 的一条有向路线。
今年，城市 0 将会举办一场大型比赛，很多游客都想前往城市 0 。
请你帮助重新规划路线方向，使每个城市都可以访问城市 0 。返回需要变更方向的最小路线数。
题目数据 保证 每个城市在重新规划路线方向后都能到达城市 0 。

示例 1：
输入：n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
输出：3
解释：更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。

示例 2：
输入：n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
输出：2
解释：更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。

示例 3：
输入：n = 3, connections = [[1,0],[2,0]]
输出：0

"""


class Solution:
    def minReorder(self, n, connections):
        # 因为n个节点间共有n-1条单向边,以0为根节点，可看作是一棵树
        reach = {}
        for start, end in connections:  # 构造邻接表，将有向变为无向
            tmp = reach.get(start, [])
            tmp.append([end, True])  # 表示start->end
            reach[start] = tmp
            tmp = reach.get(end, [])
            tmp.append([start, False])  # 表示end->start
            reach[end] = tmp
        visited, res = {0}, 0

        # # BFS，从0开始
        # queue, = [0]
        # while queue:
        #     node = queue.pop(0)
        #     for i in reach[node]:
        #         if i[0] not in visited:
        #             if i[1]:
        #                 res += 1
        #             visited.add(i[0])
        #             queue.append(i[0])

        # DFS
        def dfs(node):
            nonlocal res
            for i in reach[node]:
                if i[0] not in visited:
                    if i[1]:
                        res += 1
                    visited.add(i[0])
                    dfs(i[0])

        dfs(0)
        return res
