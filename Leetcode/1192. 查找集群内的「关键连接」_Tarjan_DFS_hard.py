# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/22 23:23
 @Author  : QDY
 @FileName: 1192. 查找集群内的「关键连接」_Tarjan_DFS_hard.py
 @Software: PyCharm
"""
"""
    力扣数据中心有 n 台服务器，分别按从 0 到 n-1 的方式进行了编号。

    它们之间以「服务器到服务器」点对点的形式相互连接组成了一个内部集群，其中连接 connections 是无向的。

    从形式上讲，connections[i] = [a, b] 表示服务器 a 和 b 之间形成连接。任何服务器都可以直接或者间接地通过网络到达任何其他服务器。

    「关键连接」是在该集群中的重要连接，也就是说，假如我们将它移除，便会导致某些服务器无法访问其他服务器。

    请你以任意顺序返回该集群内的所有 「关键连接」。



    示例 1：

    输入：n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
    输出：[[1,3]]
    解释：[[3,1]] 也是正确的。
     
    提示：
    1 <= n <= 10^5
    n-1 <= connections.length <= 10^5
    connections[i][0] != connections[i][1]
    不存在重复的连接

"""
from collections import defaultdict


class Solution:
    def criticalConnections(self, n: int, connections) :
        graph = defaultdict(list)
        for edge in connections:  # 构建图
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        low, res = [-1] * n, []  # 追溯值low[i]=节点i在DFS中不通过父节点访问到祖先节点的最小顺序值

        def tarjan(cur, index, prev):  # tarjan算法
            dfn = low[cur] = index  # dfn表示节点cur在DFS中的顺序编号
            for nxt in graph[cur]:
                if nxt != prev:  # 不经过父节点prev
                    if low[nxt] == -1:
                        index += 1
                        tarjan(nxt, index, cur)
                        if low[nxt] > dfn:  # nxt的访问时间大于cur的访问时间
                            res.append([cur, nxt])  # [cur,nxt]是关键链接
                    low[cur] = min(low[cur], low[nxt])

        tarjan(0, 0, -1)  # 以0为祖先节点
        return res
