# -*- coding: utf-8 -*-
"""
 @Time    : 2020-05-11 9:39
 @Author  : QDY
 @FileName: 407. 接雨水 II_heap_BFS_hard.py
 @Software: PyCharm
"""
"""
给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。

示例：
给出如下 3x6 的高度图:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

返回 4 。
"""

import heapq


class Solution:
    def trapRainWater(self, heightMap):
        bottom, right = len(heightMap) - 1, len(heightMap[0]) - 1
        if bottom < 2 or right < 2: return 0
        self.res = 0
        heap = []  # 维护一个小根堆

        # def heap_sink(heap,id_):
        #     left_, right_ = 2*id_+1, 2*id_+2
        #     smallest = id_
        #     if left_<len(heap) and heap[left_][0]<heap[smallest][0]:
        #         smallest = left_
        #     if right_<len(heap) and heap[right_][0]<heap[smallest][0]:
        #         smallest = right_
        #     if smallest!=id_:
        #         heap[id_], heap[smallest] = heap[smallest], heap[id_]
        #         heap_sink(heap, smallest)

        # def heap_rise(heap,id_):
        #     if id_==0:return
        #     root = (id_-1)//2
        #     if heap[root][0] > heap[id_][0]:
        #         heap[root], heap[id_] = heap[id_], heap[root]
        #         heap_rise(heap,root)

        def bfs(h, x, y):  # 广度优先搜索
            if x < 0 or x > bottom or y < 0 or y > right or visited[x][y]:
                return
            if h > heightMap[x][y]:  # 当该节点小于其相邻围栏的高度h时
                # 说明该点可以存放雨水，雨水体积=其与相邻围栏的高度差
                self.res += h - heightMap[x][y]
            visited[x][y] = True
            # 将两者较高的高度作为该点新的高度，该点作为新的围栏存入小根堆中
            heapq.heappush(heap, (max(h, heightMap[x][y]), x, y))
            # heap.append([max(h,heightMap[x][y]),x,y])
            # heap_rise(heap,len(heap)-1)
            # heap.sort(key=lambda x:x[0])

        # visited数组存放节点是否被访问过，若某节点已经被访问过，
        # 其一定是被与高度更低的围栏比较、更新过，所以后续无需再考虑
        visited = [[False] * (right + 1) for i in range(bottom + 1)]
        for i in range(right + 1):  # 初始化边界(上下两边)
            heapq.heappush(heap, (heightMap[0][i], 0, i))
            # heap.append([heightMap[0][i],0,i])
            # heap_rise(heap,len(heap)-1)
            visited[0][i] = True
            heapq.heappush(heap, (heightMap[bottom][i], bottom, i))
            # heap.append([heightMap[bottom][i],bottom,i])
            # heap_rise(heap,len(heap)-1)
            visited[bottom][i] = True
        for i in range(1, bottom):  # 左右两边
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            # heap.append([heightMap[i][0],i,0])
            # heap_rise(heap,len(heap)-1)
            visited[i][0] = True
            heapq.heappush(heap, (heightMap[i][right], i, right))
            # heap.append([heightMap[i][right],i,right])
            # heap_rise(heap,len(heap)-1)
            visited[i][right] = True
        # heap.sort(key=lambda x:x[0])
        # print(heap)
        while heap:
            # 每次取出最小的围栏，寻找其是否有高度较小的邻节点
            # 因为在相连的区域中，是否能接雨水取决于高度最低的点
            # 用小根堆存储围栏高度和坐标
            height, x, y = heapq.heappop(heap)
            # height,x,y = heap.pop(0)  #
            # height,x,y = heap[0]
            # heap[0] = heap[-1]
            # heap.pop()
            # heap_sink(heap,0)

            # BFS
            bfs(height, x + 1, y)
            bfs(height, x - 1, y)
            bfs(height, x, y + 1)
            bfs(height, x, y - 1)

        return self.res
