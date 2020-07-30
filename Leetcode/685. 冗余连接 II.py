# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/30 10:24
 @Author  : QDY
 @FileName: 685. 冗余连接 II.py
 @Software: PyCharm
"""
"""
在本问题中，有根树指满足以下条件的有向图。该树只有一个根节点，所有其他节点都是该根节点的后继。
每一个节点只有一个父节点，除了根节点没有父节点。
输入一个有向图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。
附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
结果图是一个以边组成的二维数组。 每一个边 的元素是一对 [u, v]，
用以表示有向图中连接顶点 u 和顶点 v 的边，其中 u 是 v 的一个父节点。
返回一条能删除的边，使得剩下的图是有N个节点的有根树。
若有多个答案，返回最后出现在给定二维数组的答案。

示例 1:
输入: [[1,2], [1,3], [2,3]]
输出: [2,3]
解释: 给定的有向图如下:
  1
 / \
v   v
2-->3

示例 2:
输入: [[1,2], [2,3], [3,4], [4,1], [1,5]]
输出: [4,1]
解释: 给定的有向图如下:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3

注意:
二维数组大小的在3到1000范围内。
二维数组中的每个整数在1到N之间，其中 N 是二维数组的大小。

"""
from collections import defaultdict


class Solution:
    def findRedundantDirectedConnection(self, edges):
        graph, child_set, visited = defaultdict(list), set(), {}
        delete = []
        for root, child in edges:
            if child in child_set:  # 有入度为 2 的点child
                delete = [root, child]  # 删除的边
                continue
            graph[root].append(child)
            child_set.add(child)
            visited[child] = 0
            visited[root] = 0

        self.cycle = []

        def dfs(cur):  # 搜索是否存在环
            visited[cur] = 1
            if cur not in graph:
                return
            for nxt in graph[cur]:
                if visited[nxt] == 1:
                    self.cycle = [cur, nxt]
                    return
                elif visited[nxt] == 0:
                    dfs(nxt)
                    if self.cycle: return
            visited[cur] = 2

        if delete:  # 删除detele边后，判断剩下的边是否存在环
            for node in graph.keys():
                if visited[node] == 0:
                    dfs(node)
                    if self.cycle:  # 若剩下的边仍存在环，则应删除以detele[1]为子节点的另一条边
                        for root in graph:
                            if delete[1] in graph[root]:
                                return [root, delete[1]]
            return delete
        else:  # 没有入度为2的点，则一定有环，需要删除最后出现的多余的边
            for node in graph.keys():
                if visited[node] == 0:
                    dfs(node)
                if self.cycle:
                    return self.cycle
