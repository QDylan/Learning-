# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-12 9:38
 @Author  : QDY
 @FileName: 5538. 统计子树中城市之间最大距离.py
 @Software: PyCharm
"""
"""
给你n个城市，编号为从1 到n。同时给你一个大小为n-1的数组edges，其中edges[i] = [ui, vi]表示城市ui和vi之间有一条双向边。
题目保证任意城市之间只有唯一的一条路径。换句话说，所有城市形成了一棵树。

一棵子树是城市的一个子集，且子集中任意城市之间可以通过子集中的其他城市和边到达。
两个子树被认为不一样的条件是至少有一个城市在其中一棵子树中存在，但在另一棵子树中不存在。

对于d从1 到n-1，请你找到城市间最大距离恰好为 d的所有子树数目。

请你返回一个大小为n-1的数组，其中第d个元素（下标从 1 开始）是城市间 最大距离 恰好等于d的子树数目。

请注意，两个城市间距离定义为它们之间需要经过的边的数目。

示例 1：
输入：n = 4, edges = [[1,2],[2,3],[2,4]]
输出：[3,4,0]
解释：
子树 {1,2}, {2,3} 和 {2,4} 最大距离都是 1 。
子树 {1,2,3}, {1,2,4}, {2,3,4} 和 {1,2,3,4} 最大距离都为 2 。
不存在城市间最大距离为 3 的子树。

示例 2：
输入：n = 2, edges = [[1,2]]
输出：[1]

示例 3：
输入：n = 3, edges = [[1,2],[2,3]]
输出：[2,1]

提示：
2 <= n <= 15
edges.length == n-1
edges[i].length == 2
1 <= ui, vi <= n
题目保证(ui, vi)所表示的边互不相同。

"""
from collections import defaultdict, deque


class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges):
        graph = defaultdict(list)
        dd = [[0] * n for _ in range(n)]
        for x, y in edges:
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)

        for i in range(n):  # 搜索节点之间的距离
            step = 1
            q = deque([i])
            visited = {i}
            while q:
                l = len(q)
                for ii in range(l):
                    cur = q.popleft()
                    for nxt in graph[cur]:
                        if nxt not in visited:
                            visited.add(nxt)
                            dd[i][nxt] = step
                            q.append(nxt)
                step += 1
        res = [0] * (n - 1)
        for i in range(1, 2 ** n):  # 压缩状态
            status = bin(i)[2:]
            NN = status.count('1')  # 状态的节点数量
            if NN <= 1: continue  # 只有一个节点
            status = status[::-1] + '0' * (n - len(status))
            road = 0
            for x, y in edges:  # 计算每种状态的边的数量
                if status[x - 1] == '1' and status[y - 1] == '1': road += 1
            if road < NN - 1:  # 树结构的无向图，要满足 边数=节点数-1
                continue
            # print(status)
            max_dis = 0
            for p in range(n - 1):  # 计算树的最大距离
                if status[p] == '1':
                    for q in range(p + 1, n):
                        if status[q] == '1':
                            max_dis = max(max_dis, dd[p][q] - 1)
            res[max_dis] += 1
        return res
