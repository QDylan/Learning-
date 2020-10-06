# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-06 10:56
 @Author  : QDY
 @FileName: 834. 树中距离之和.py
 @Software: PyCharm
"""
"""
给定一个无向、连通的树。树中有 N 个标记为 0...N-1 的节点以及 N-1条边。

第 i 条边连接节点edges[i][0] 和 edges[i][1]。

返回一个表示节点 i 与其他所有节点距离之和的列表 ans。

示例 1:

输入: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
输出: [8,12,6,10,10,10]
解释: 
如下为给定的树的示意图：
  0
 / \
1   2
   /|\
  3 4 5

我们可以计算出 dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5) 
也就是 1 + 1 + 2 + 2 + 2 = 8。 因此，answer[0] = 8，以此类推。
说明:1 <= N <= 10000

"""
from collections import defaultdict


class Solution:
    def sumOfDistancesInTree(self, N: int, edges):
        tree = defaultdict(list)
        for x, y in edges:
            tree[x].append(y)
            tree[y].append(x)
        count = [0] * N  # 每个节点的子节点数量
        depth = [0] * N  # 每个节点的深度
        res = [0] * N  # 答案

        def dfs(cur, parent):  # dfs 所有节点的深度和子节点数量
            count[cur] = 1  # 子节点包括自身
            for nxt in tree[cur]:
                if nxt != parent:
                    depth[nxt] = depth[cur] + 1
                    dfs(nxt, cur)
                    count[cur] += count[nxt]

        dfs(0, -1)  # 以0为根节点
        res[0] = sum(depth)  # 根节点的所有节点距离之和 = 所有节点的深度

        def dfs_res(cur, parent):
            for nxt in tree[cur]:
                # 两个相邻的节点cur和nxt，将树分为分别以cur和nxt为根节点的两棵子树new_cur,new_nxt
                # res[cur] = new_res[cur]+new_res[nxt]+count[nxt]
                # --> new_res[cur]+new_res[nxt] = res[cur]-count[nxt]
                # res[nxt] = new_res[nxt]+new_res[cur]+new_count[cur]
                # new_count[cur] = N - count[nxt]
                # res[nxt] = res[cur] + N - 2*count[nxt]
                if nxt != parent:
                    res[nxt] = res[cur] + N - 2 * count[nxt]
                    dfs_res(nxt, cur)

        dfs_res(0, -1)

        return res
