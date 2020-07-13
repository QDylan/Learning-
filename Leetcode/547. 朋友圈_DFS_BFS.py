# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/13 21:02
 @Author  : QDY
 @FileName: 547. 朋友圈_DFS_BFS.py

    班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。
    如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。
    给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，
    表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。

    示例 1:
    输入:
    [[1,1,0],
     [1,1,0],
     [0,0,1]]
    输出: 2
    说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
    第2个学生自己在一个朋友圈。所以返回2。

    示例 2:
    输入:
    [[1,1,0],
     [1,1,1],
     [0,1,1]]
    输出: 1
    说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。

    注意：
    N 在[1,200]的范围内。
    对于所有学生，有M[i][i] = 1。
    如果有M[i][j] = 1，则有M[j][i] = 1。

"""


class Solution:
    def findCircleNum(self, M):
        if not M: return 0
        res, m, visited = 0, len(M), set()

        # M可以看作邻接矩阵
        def dfs(i):  # 深度遍历i节点的朋友圈，找出所有与i相连的节点
            for j in range(m):
                if M[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        for ii in range(m):
            if ii not in visited:
                visited.add(ii)
                # dfs(ii)
                queue = [ii]
                while queue:  # BFS
                    length = len(queue)
                    for l in range(length):
                        j_ = queue.pop(0)
                        for i_ in range(m):
                            if M[i_][j_] == 1 and i_ not in visited:
                                queue.append(i_)
                                visited.add(i_)
                res += 1

        return res
