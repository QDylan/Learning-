# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-07 14:58
 @Author  : QDY
 @FileName: 最短路径.py
 @Software: PyCharm
"""
from collections import defaultdict


def dfs(cur, end, mat):
    pass


def Dijkstra(start, mat):
    N = len(mat)
    visited = [False] * N
    visited[start] = True
    mat[start][start] = 0
    # dis = mat[start]
    cnt = 1
    while cnt < N:
        min_dis, idx = float('inf'), None
        for i in range(N):  # 找到最小的路径
            if not visited[i] and mat[start][i] < min_dis:
                min_dis = mat[start][i]
                idx = i
        if idx is None:
            break  # 无后继节点
        else:
            visited[idx] = True
            cnt += 1
        for i in range(N):
            if not visited[i] and mat[start][idx] + mat[idx][i] < mat[start][i]:
                mat[start][i] = mat[start][idx] + mat[idx][i]


# def Bellman_Ford():


if __name__ == '__main__':
    # path = [(1, 2, 2), (2, 3, 3), (3, 1, 4), (5, 3, 3), (3, 4, 4), (4, 5, 5), (2, 5, 7), (1, 5, 10)]
    path = [(1, 2, 1), (2, 3, 1), (3, 5, 2), (5, 1, 1), (5, 4, 1)]
    N = 5
    graph = defaultdict(list)
    matrix = [[float('inf')] * N for _ in range(N)]
    for x, y, d in path:
        graph[x].append(y)
        matrix[x - 1][y - 1] = min(matrix[x - 1][y - 1], d)
    for i in range(N):
        Dijkstra(i, matrix)
    for i in matrix:
        print(i)
