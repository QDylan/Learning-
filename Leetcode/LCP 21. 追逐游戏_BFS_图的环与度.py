# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-13 21:37
 @Author  : QDY
 @FileName: LCP 21. 追逐游戏_BFS_图的环与度.py
 @Software: PyCharm
"""
"""
秋游中的小力和小扣设计了一个追逐游戏。他们选了秋日市集景区中的 N 个景点，景点编号为 1~N。此外，
他们还选择了 N 条小路，满足任意两个景点之间都可以通过小路互相到达，且不存在两条连接景点相同的小路。
整个游戏场景可视作一个无向连通图，记作二维数组 edges，数组中以 [a,b] 形式表示景点 a 与景点 b 之间有一条小路连通。

小力和小扣只能沿景点间的小路移动。小力的目标是在最快时间内追到小扣，小扣的目标是尽可能延后被小力追到的时间。
游戏开始前，两人分别站在两个不同的景点 startA 和 startB。
每一回合，小力先行动，小扣观察到小力的行动后再行动。小力和小扣在每回合可选择以下行动之一：

移动至相邻景点
留在原地
如果小力追到小扣（即两人于某一时刻出现在同一位置），则游戏结束。若小力可以追到小扣，请返回最少需要多少回合；若小力无法追到小扣，请返回 -1。
注意：小力和小扣一定会采取最优移动策略。

示例 1：
输入：edges = [[1,2],[2,3],[3,4],[4,1],[2,5],[5,6]], startA = 3, startB = 5
输出：3

解释：
第一回合，小力移动至 2 号点，小扣观察到小力的行动后移动至 6 号点；
第二回合，小力移动至 5 号点，小扣无法移动，留在原地；
第三回合，小力移动至 6 号点，小力追到小扣。返回 3。

示例 2：
输入：edges = [[1,2],[2,3],[3,4],[4,1]], startA = 1, startB = 3
输出：-1

解释：
小力如果不动，则小扣也不动；否则小扣移动到小力的对角线位置。这样小力无法追到小扣。

提示：
edges 的长度等于图中节点个数
3 <= edges.length <= 10^5
1 <= edges[i][0], edges[i][1] <= edges.length 且 edges[i][0] != edges[i][1]
1 <= startA, startB <= edges.length 且 startA != startB

"""
from collections import defaultdict, deque


class Solution:
    def chaseGame(self, edges, startA: int, startB: int) -> int:
        if startA == startB: return 0
        n = len(edges)
        graph = defaultdict(set)
        for x, y in edges:
            graph[x - 1].add(y - 1)
            graph[y - 1].add(x - 1)
        A, B = startA - 1, startB - 1
        Ato, Bto = [float('inf')] * n, [float('inf')] * n

        def bfs(start, mat):  # 通过bfs搜索出A,B距离其他点的最短距离
            q = deque([start])
            mat[start] = 0
            visited = {start}
            while q:
                length = len(q)
                for i in range(length):
                    cur = q.popleft()
                    for nxt in graph[cur]:
                        if nxt not in visited:
                            visited.add(nxt)
                            mat[nxt] = mat[cur] + 1
                            q.append(nxt)

        bfs(A, Ato)
        bfs(B, Bto)
        if Ato[B] == 1: return 1
        # 若能被抓到，则要么在第一个回合就被抓到，要么在一个度为1的节点被抓到

        in_degrees = [len(graph[i]) for i in range(n)]  # 每个节点的度
        visited = [0] * n
        # 关键：利用度 搜索无向图的环
        def dfs(cur):  # 深度遍历度为1的节点，并将其标记
            visited[cur] = 1  # 度为1的节点不可能在环上，标记为1
            nxt = graph[cur].pop()  # 切断nxt 与 cur 的连接
            graph[nxt].discard(cur)
            in_degrees[nxt] -= 1
            if in_degrees[nxt] == 1:  # 若nxt 切断与 cur的连接后度减小为1
                dfs(nxt)  # 则nxt也不可能在环上，继续对nxt进行搜索

        for i in range(n):
            if not visited[i] and in_degrees[i] == 1:  # 遍历所有度为1且还未被判定不在环上的节点
                dfs(i)
        len_cycle = n - sum(visited)  # 剩余未标记为1的点构成环
        # print(visited)
        res = 0
        for i in range(n):
            if Ato[i] - Bto[i] > 1:  # B可以到达i <=> B到i的最短距离比A到i的最短距离短1以上
                res = max(res, Ato[i])
                if visited[i] == 0 and len_cycle > 3: return -1  # B能到达环上1点i,且环的长度大于3
        return res
