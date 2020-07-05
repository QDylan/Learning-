# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/5 23:40
 @Author  : QDY
 @FileName: 218. 天际线问题.py

城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。
现在，假设您获得了城市风光照片（图A）上显示的所有建筑物的位置和高度，请编写一个程序以输出由这些建筑物形成的天际线

每个建筑物的几何信息用三元组 [Li，Ri，Hi] 表示，
其中 Li 和 Ri 分别是第 i 座建筑物左右边缘的 x 坐标，Hi 是其高度。
可以保证 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX 和 Ri - Li > 0。
您可以假设所有建筑物都是在绝对平坦且高度为 0 的表面上的完美矩形。

例如，图A中所有建筑物的尺寸记录为：[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] 。

输出是以 [ [x1,y1], [x2, y2], [x3, y3], ... ] 格式的“关键点”（图B中的红点）的列表，
它们唯一地定义了天际线。关键点是水平线段的左端点。请注意，最右侧建筑物的最后一个关键点仅用于标记天际线的终点，
并始终为零高度。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。

例如，图B中的天际线应该表示为：[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]。

说明:

任何输入列表中的建筑物数量保证在 [0, 10000] 范围内。
输入列表已经按左 x 坐标 Li  进行升序排列。
输出列表必须按 x 位排序。
输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；
三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]

"""
import heapq
class Solution:
    def getSkyline(self, buildings):
        if not buildings:return []
        heap = [[0, float('inf')]]  # 构建一个大顶堆
        res = [[0, 0]]
        points = []
        #1.将所有端点加入到点集中(每个建筑物的左右端点)
        for l, r, h in buildings:
            points.append((l, -h, r)) #这里负号将最小堆，变成了最大堆
            points.append((r, h, 0)) #r的右端点为0

        #2.将端点从小到大排序
        points.sort() #如果当前点相等，则按照高度升序

        #3.遍历每一个点，分别判断出堆、入堆、添加关键点操作。
        for l, h, r in points:
            while l >= heap[0][1]: #出堆：保证当前堆顶为去除之前建筑物右端点的最大值。
                heapq.heappop(heap)
            if h < 0: #入堆：所有左端点都要入堆
                heapq.heappush(heap, [h, r])
            if res[-1][1] != -heap[0][0]: #关键点：必然是左端点，堆顶，因此需要加负号
                res.append([l, -heap[0][0]])
        return res[1:]

        # def heapify(i,n):
        #     if i >=n:return
        #     l = 2*i + 1
        #     r = 2*i + 2
        #     largest = i
        #     if l<n and heap[largest][0]<heap[l][0]:
        #         largest = l
        #     if r<n and heap[largest][0]<heap[r][0]:
        #         largest = r
        #     if largest!=i:
        #         heap[largest],heap[i] = heap[i], heap[largest]
        #         heapify(largest,n)

        # #1.将所有端点加入到点集中(每个建筑物的左右端点)
        # for l, r, h in buildings:
        #     points.append((l, h, r)) #
        #     points.append((r, h, 0)) #r的右端点为0

        # #2.将端点从左到右排序
        # points.sort() #如果当前点相等，则按照高度升序

        # #3.遍历每一个点
        # for l, h, r in points:
        #     while l >= heap[0][1]: #出堆：保证当前堆顶为去除之前建筑物右端点的最大值。
        #         heap[0] = heap[-1]
        #         heap.pop()
        #         heapify(0,len(heap))
        #     if h < 0: #入堆：所有左端点都要入堆
        #         heap.append([h, r])
        #         son = len(heap)-1
        #         pa = (son-1)//2
        #         while pa>=0 and heap[pa][0]<heap[son][0]:
        #             heap[son], heap[pa] = heap[pa], heap[son]
        #             pa,son = (pa-1)//2,pa

        #     if res[-1][1] != heap[0][0]: #关键点：必然是左端点
        #         res.append([l, heap[0][0]])
        # return res[1:]
