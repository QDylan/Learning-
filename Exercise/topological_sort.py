# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/22 10:54
 @Author  : QDY
 @FileName: topological_sort.py
 @Software: PyCharm
"""
from collections import defaultdict

def topological_sort(edges):
    res = []
    graph = defaultdict(list)
    visited = {}

    for edge in edges:
        graph[edge[0]].append(edge[1])
        visited[edge[1]] = 0

    valid = True

    def dfs(node):
        nonlocal valid
        visited[node] = 1  # 标记该节点在搜索中
        if node in graph:
            for nxt in graph[node]:
                if visited[nxt] == 1:  # 邻节点在搜索中，出现环
                    valid = False
                    return
                elif visited[nxt] == 0:
                    dfs(nxt)
                    if not valid: return
        res.append(node)
        visited[node] = 2  # 搜索完毕

    for i in edges:
        if i[0] not in visited:
            dfs(i[0])

    print(res[::-1])

if __name__ == '__main__':

    print("拓扑排序结果：")
    topological_sort([[1,2],[1,4],[2,4],[4,3],[3,5],[2,3],[4,5]])
