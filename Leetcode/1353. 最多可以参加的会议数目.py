# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/11 11:50
 @Author  : QDY
 @FileName: 1353. 最多可以参加的会议数目.py

    给你一个数组 events，其中 events[i] = [startDayi, endDayi] ，表示会议 i 开始于 startDayi ，结束于 endDayi 。
    你可以在满足 startDayi <= d <= endDayi 中的任意一天 d 参加会议 i 。注意，一天只能参加一个会议。
    请你返回你可以参加的 最大 会议数目。
     
    示例 1：
    输入：events = [[1,2],[2,3],[3,4]]
    输出：3
    解释：你可以参加所有的三个会议。
    安排会议的一种方案如上图。
    第 1 天参加第一个会议。
    第 2 天参加第二个会议。
    第 3 天参加第三个会议。

    示例 2：
    输入：events= [[1,2],[2,3],[3,4],[1,2]]
    输出：4

    示例 3：
    输入：events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
    输出：4

    示例 4：
    输入：events = [[1,100000]]
    输出：1

    示例 5：
    输入：events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
    输出：7
     
    提示：
    1 <= events.length <= 10^5
    events[i].length == 2
    1 <= events[i][0] <= events[i][1] <= 10^5

"""
import heapq


class Solution:
    def maxEvents(self, events):
        n = len(events)
        if n <= 1: return n
        # 贪心：优先确定参加最早结束的会议
        events.sort(reverse=True)
        heap = []  # 维护一个小根堆
        day, res = 1, 0
        # def heapify(i):
        #     n = len(heap)
        #     if i>=n:return
        #     l,r = 2*i+1,2*i+2
        #     smallest = i
        #     if l<n and heap[l]<heap[smallest]:
        #         smallest = l
        #     if r<n and heap[r]<heap[smallest]:
        #         smallest = r
        #     if smallest!=i:
        #         heap[smallest],heap[i] = heap[i],heap[smallest]
        #         heapify(smallest)

        while events or heap:
            while heap and heap[0] < day:  # 删除已经结束还未参加的会议
                heapq.heappop(heap)
                # heap[0] = heap[-1]
                # heap.pop()
                # heapify(0)

            while events and events[-1][0] == day:  # 将在day开始的会议的结束时间加入heap中
                heapq.heappush(heap, events.pop()[1])
                # heap.append(events.pop())
                # son,pa = len(heap)-1,(len(heap)-2)//2
                # while pa>=0 and heap[pa]>heap[son]:  # 结束日期早的优先
                #     heap[pa],heap[son] = heap[son],heap[pa]
                #     pa, son = (pa-1)//2, pa
            if heap:  # 优先参加最早结束的会议
                res += 1
                heapq.heappop(heap)
                # heap[0] = heap[-1]
                # heap.pop()
                # heapify(0)  #
            day += 1
        return res
