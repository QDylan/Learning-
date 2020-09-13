# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-13 16:10
 @Author  : QDY
 @FileName: 5513. 连接所有点的最小费用.py
 @Software: PyCharm
"""
"""
给你一个points数组，表示 2D 平面上的一些点，其中points[i] = [xi, yi]。

连接点[xi, yi] 和点[xj, yj]的费用为它们之间的 曼哈顿距离：|xi - xj| + |yi - yj|，其中|val|表示val的绝对值。

请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有一条简单路径时，才认为所有点都已连接。

示例 1：
输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
输出：20

解释：
我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
注意到任意两个点之间只有唯一一条路径互相到达。

示例 2：
输入：points = [[3,12],[-2,5],[-4,1]]
输出：18

示例 3：
输入：points = [[0,0],[1,1],[1,0],[-1,1]]
输出：4

示例 4：
输入：points = [[-1000000,-1000000],[1000000,1000000]]
输出：4000000

示例 5：
输入：points = [[0,0]]
输出：0

提示：
1 <= points.length <= 1000
-106<= xi, yi <= 106
所有点(xi, yi)两两不同。

"""
import heapq


class UF:  # 并查集
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1] * N
        self.count = N

    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq: return
        if self.size[rootp] > self.size[rootq]:
            self.parent[rootq] = rootp
            self.size[rootp] += self.size[rootq]
        else:
            self.parent[rootp] = rootq
            self.size[rootq] += self.size[rootp]
        self.count -= 1

    def find(self, p):
        while self.parent[p] != p:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def connect(self, p, q):
        return self.find(p) == self.find(q)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1: return 0
        # # Prim 算法
        # heap = [(0,0)]  # 构建优先队列 (到邻节点的距离，邻节点)
        # visited = set([i for i in range(len(points))])
        # res,cnt = 0,0
        # f = lambda x,y : abs(x[0]-y[0])+abs(x[1]-y[1])
        # while visited and cnt<n:
        #     dis,cur = heapq.heappop(heap)  # 每次取出优先队列中的最短边来构建树
        #     if cur not in visited:  # 已访问过节点的直接跳过
        #         continue
        #     visited.discard(cur)
        #     res += dis
        #     cnt += 1
        #     for nxt in visited:  # 将与cur相连的所有边加入优先队列中
        #         heapq.heappush(heap,(f(points[cur],points[nxt]),nxt))

        # return res

        # Kruskal算法
        edges = []
        for i in range(n):
            for j in range(i + 1, n):  # 把所有边及其权重都加入优先队列中
                dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(edges, (dis, i, j))
        res, cnt = 0, 0
        uf = UF(n)
        while edges and cnt < n - 1:
            dis, x, y = heapq.heappop(edges)  # 每次取出权重最小的边
            if not uf.connect(x, y):  # 如果这条边的两个端点是不连通的，则加入
                res += dis
                cnt += 1
                uf.union(x, y)  # 使两个端点连通
        return res
