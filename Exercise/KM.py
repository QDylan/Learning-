# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-24 15:47
 @Author  : QDY
 @FileName: KM.py
 @Software: PyCharm
"""
from collections import deque


class hungarian:  # 匈牙利算法
    def __init__(self, m, n):
        self.N = max(m, n)
        self.g = [[0] * self.N for _ in range(self.N)]  # 图
        self.visL = [False] * self.N  # 左端点的访问数组
        self.visR = [False] * self.N
        self.matchL = [-1] * self.N  # 左端点对应的匹配点
        self.matchR = [-1] * self.N  # 右端点对应的匹配点
        self.q = deque([])
        self.pre = [-1] * self.N  # 连接右端点的左端点
        self.lx = [-float('inf')] * self.N
        self.ly = [-0] * self.N
        self.slack = [float('inf')] * self.N
        self.res = 0

    def addEdge(self, u, v, w):
        self.g[u][v] = max(w, 0)  # 权值为负不如不匹配

    def check(self, v):
        self.visR[v] = True
        if self.matchR[v] != -1:
            self.q.append(self.matchR[v])
            self.visL[self.matchR[v]] = True
            return False
        while v != -1:
            self.matchR[v] = self.pre[v]
            self.matchL[self.pre[v]], v = v, self.matchL[self.pre[v]]
        return True

    def bfs(self, i):  # 广度优先搜索左端点i的匹配
        self.q = deque([i])
        self.visL[i] = True
        while True:
            while self.q:
                u = self.q.popleft()
                for v in range(self.N):
                    if not self.visR[v]:
                        delta = self.lx[u] + self.ly[v] - self.g[u][v]
                        if self.slack[v] >= delta:
                            self.pre[v] = u
                            if delta:
                                self.slack[v] = delta
                            elif self.check(v):  # delta==0，有机会加入相等子图
                                return
            a = float('inf')  # 没有增广路，修改顶标
            for j in range(self.N):
                if not self.visR[j]:
                    a = min(a, self.slack[j])

            for j in range(self.N):
                if self.visL[j]:
                    self.lx[j] -= a
                if self.visR[j]:
                    self.ly[j] += a
                else:
                    self.slack[j] -= a
            for j in range(self.N):
                if not self.visR[j] and self.slack[j] == 0 and self.check(j):
                    return

    def solve(self):
        for i in range(self.N):
            for j in range(self.N):  # 设置左端点的初始顶标，选择最大权的边
                self.lx[i] = max(self.lx[i], self.g[i][j])
        for i in range(self.N):  # 遍历每个节点
            self.slack = [float('inf')] * self.N  # 重置
            self.visR = [False] * self.N
            self.visL = [False] * self.N
            self.bfs(i)
        for i in range(self.N):
            if self.g[i][self.matchL[i]] > 0:
                self.res += self.g[i][self.matchL[i]]
            else:
                self.matchL[i] = -1
        return self.res

if __name__ == '__main__':
    cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
    # for i in range(len(cost)):
    #     for j in range(len(cost[i])):
    #         cost[i][j] *= -1
    L, R = len(cost), len(cost[0])
    hg = hungarian(L, R)
    lmin, rmin = [float('inf')] * L, [float('inf')] * R
    for i in range(L):
        for j in range(R):
            lmin[i] = min(lmin[i], cost[i][j])  # 就算每个左端点可以取得的最小权重
            rmin[j] = min(rmin[j], cost[i][j])
    ans = sum(lmin) + sum(rmin)  # 连接每个端点上最短边
    for i in range(L):
        for j in range(R):
            # 选择连接左端点i和右端点j对获得最小权匹配的增益值 -> 转换为最大权匹配问题
            hg.addEdge(i, j, lmin[i] + rmin[j] - cost[i][j])
    print(ans-hg.solve())
