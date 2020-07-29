# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/29 15:30
 @Author  : QDY
 @FileName: LCP 13. 寻宝_BFS_状态压缩动态规划_hard.py
 @Software: PyCharm
 我们得到了一副藏宝图，藏宝图显示，在一个迷宫中存在着未被世人发现的宝藏。

    迷宫是一个二维矩阵，用一个字符串数组表示。它标识了唯一的入口（用 'S' 表示），
    和唯一的宝藏地点（用 'T' 表示）。但是，宝藏被一些隐蔽的机关保护了起来。
    在地图上有若干个机关点（用 'M' 表示），只有所有机关均被触发，才可以拿到宝藏。

    要保持机关的触发，需要把一个重石放在上面。迷宫中有若干个石堆（用 'O' 表示），
    每个石堆都有无限个足够触发机关的重石。但是由于石头太重，我们一次只能搬一个石头到指定地点。

    迷宫中同样有一些墙壁（用 '#' 表示），我们不能走入墙壁。剩余的都是可随意通行的点（用 '.' 表示）。
    石堆、机关、起点和终点（无论是否能拿到宝藏）也是可以通行的。

    我们每步可以选择向上/向下/向左/向右移动一格，并且不能移出迷宫。搬
    起石头和放下石头不算步数。那么，从起点开始，我们最少需要多少步才能最后拿到宝藏呢？如果无法拿到宝藏，返回 -1 。

    示例 1：
    输入： ["S#O", "M..", "M.T"]
    输出：16

    解释：最优路线为： S->O, cost = 4, 去搬石头 O->第二行的M, cost = 3, M机关触发 第二行的M->O, cost = 3,
    我们需要继续回去 O 搬石头。 O->第三行的M, cost = 4, 此时所有机关均触发 第三行的M->T, cost = 2，去T点拿宝藏。 总步数为16。

    示例 2：
    输入： ["S#O", "M.#", "M.T"]
    输出：-1

    解释：我们无法搬到石头触发机关

    示例 3：
    输入： ["S#O", "M.T", "M.."]
    输出：17

    解释：注意终点也是可以通行的。
    限制：

    1 <= maze.length <= 100
    1 <= maze[i].length <= 100
    maze[i].length == maze[j].length
    S 和 T 有且只有一个
    0 <= M的数量 <= 16
    0 <= O的数量 <= 40，题目保证当迷宫中存在 M 时，一定存在至少一个 O 。

"""
from collections import deque


class Solution:
    def minimalSteps(self, maze):
        height, width = len(maze), len(maze[0])
        start, end, os, ms = None, None, [], []  # 起点，终点，石头点集，机关点集
        for i in range(height):  # 1.记录每个点的类型
            for j in range(width):
                if maze[i][j] == 'S':
                    start = (i, j)
                elif maze[i][j] == 'T':
                    end = (i, j)
                elif maze[i][j] == 'M':
                    ms.append((i, j))
                elif maze[i][j] == 'O':
                    os.append((i, j))
        m, o = len(ms), len(os)
        index_o = {(ox, oy): i for i, (ox, oy) in enumerate(os)}  # 1.1给石头点建立索引

        def bfs2o(i, j):  # 计算(i,j)点到所有o点和end的距离
            to_o, to_t = [float('inf')] * o, float('inf')
            q, visited = deque([(i, j)]), [[False] * width for i in range(height)]
            visited[i][j] = True
            cur_dist = 0
            while q:
                num = len(q)
                for n in range(num):
                    x, y = q.popleft()
                    if (x, y) in index_o:
                        to_o[index_o[x, y]] = cur_dist
                    if x == end[0] and y == end[1]:  # 终点
                        to_t = cur_dist
                    for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                        if 0 <= nx < height and 0 <= ny < width and maze[nx][ny] != '#' and not visited[nx][ny]:
                            q.append((nx, ny))
                            visited[nx][ny] = True
                cur_dist += 1
            return to_o, to_t

        start2o, start2end = bfs2o(start[0], start[1])
        if start2end == float('inf'): return -1  # 起点与终点不连通
        if m == 0: return start2end  # 无机关，之间返回起点到终点的距离

        m2o, m2end = [], []  # 2.计算机关点m到石头点o和终点end的距离
        for i in range(m):
            tmp_o, tmp_end = bfs2o(ms[i][0], ms[i][1])
            if tmp_end == float('inf'):
                return -1  # 这个机关点无法到达终点
            m2o.append(tmp_o)
            m2end.append(tmp_end)

        start2m = []  # 3.计算起点start搬石头到第一个机关m的距离
        for i in range(m):
            dist = min(start2o[k] + m2o[i][k] for k in range(o))
            if dist == float('inf'):
                return -1  # 机关点m与起点或所有石头点不连通
            start2m.append(dist)

        m2m = {}  # 4.计算 机关点i->石头点->机关点j 的最短距离
        for i in range(m - 1):
            for j in range(i + 1, m):
                dist = min(m2o[i][k] + m2o[j][k] for k in range(o))
                # if dist == float('inf'):
                #     return -1  # 两个机关点之间无法连通
                m2m[i, j] = dist
                m2m[j, i] = dist

        # 5.状态压缩的动态规划
        # dp[status][i] = 状态status以i结尾时的最短路径
        # 初始状态=0，结束状态=1<<m - 1
        # 有m个机关点，总共有2**m种状态
        dp = [[float('inf')] * m for _ in range(1 << m)]
        for cur in range(1, 1 << m):
            for bit in range(m):  # 当前状态以第bit个机关结尾时
                if cur >> bit & 1:
                    prev = cur ^ (1 << bit)  # 上一个状态
                    if prev == 0:  # 上一个状态是初始
                        dp[cur][bit] = start2m[bit]
                    else:
                        for i in range(m):  # 计算上个状态以哪个机关i结尾，到当前机关的距离最小
                            if (prev >> i) & 1:
                                dp[cur][bit] = min(dp[cur][bit], dp[prev][i] + m2m[i, bit])
        return min(dp[-1][i] + m2end[i] for i in range(m))

        # S2O,M2O,M2T,S2T = {}, [], [], float('inf')
        # cnt_M = 0
        # h, w = len(maze), len(maze[0])
        # for i in range(h):  # BFS
        #     for j in range(w):
        #         if maze[i][j] in ('S','M'):
        #             if maze[i][j]=='M':
        #                 M2O.append({})
        #                 cnt_M += 1
        #             q = deque([(i,j)])
        #             visited = [[False]*w for i in range(h)]
        #             visited[i][j] = True
        #             d = 0
        #             while q:
        #                 l = len(q)
        #                 for cnt in range(l):
        #                     x,y = q.popleft()
        #                     if maze[x][y] == 'O':
        #                         if maze[i][j] == 'S':  # start->stone
        #                             S2O[(x,y)] = d
        #                         elif maze[i][j] == 'M': # M -> stone
        #                             M2O[cnt_M-1][(x,y)] = d

        #                     elif maze[x][y] == 'T':
        #                         if maze[i][j] == 'M':
        #                             M2T.append(d)
        #                         elif maze[i][j] == 'S':
        #                             S2T = d
        #                     for x_, y_ in ((0,1),(0,-1),(1,0),(-1,0)):
        #                         x1, y1 = x+x_, y+y_
        #                         if x1>=0 and x1<h and y1>=0 and y1<w and maze[x1][y1]!='#' and not visited[x1][y1]:
        #                             q.append((x1,y1))
        #                             visited[x1][y1] = True
        #                 d += 1
        #             if maze[i][j]=='M' and (not M2O[cnt_M-1] or len(M2T)<cnt_M): # 第cnt_M个M找不到stone
        #                 return -1

        # if cnt_M == 0:
        #     return S2T if S2T!=float('inf') else -1
        # if not S2O:return -1
        # M2M = [[float('inf')]*cnt_M for i in range(cnt_M)]
        # for i in range(cnt_M-1):
        #     for j in range(i+1,cnt_M):
        #         for stone in M2O[i]:
        #             M2M[i][j] = min(M2M[i][j],M2O[i][stone]+M2O[j][stone])
        #         M2M[j][i] = M2M[i][j]
        # # print(M2M)
        # memory = {}
        # q = deque()
        # for i in range(cnt_M):
        #     state = 1<<i
        #     memory[(state,i)] = float('inf')
        #     q.append((state,i))
        #     for stone in M2O[i]:
        #         memory[(state,i)] = min(memory[(state,i)],S2O[stone]+M2O[i][stone])

        # while q:
        #     l = len(q)
        #     for cnt in range(l):
        #         state, last = q.popleft()
        #         for i in range(cnt_M):
        #             if not state & (1<<i):
        #                 nxt = state^(1<<i)
        #                 if (nxt,i) not in memory:
        #                     memory[(nxt,i)] = float('inf')
        #                     q.append((nxt,i))
        #                 memory[(nxt,i)] = min(memory[(nxt,i)],memory[(state,last)]+M2M[last][i])
        # final = 2**cnt_M-1
        # res = float('inf')
        # for i in range(cnt_M):
        #     res = min(res,memory[(final,i)]+M2T[i])
        # return res
