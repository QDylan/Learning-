# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/22 8:50
 @Author  : QDY
 @FileName: 253. 会议室 II_堆.py
 @Software: PyCharm
"""
"""
给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，
为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

示例 1:
输入: [[0, 30],[5, 10],[15, 20]]
输出: 2

示例 2:
输入: [[7,10],[2,4]]
输出: 1

"""
import heapq


class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals: return 0
        intervals.sort(key=lambda x: x[0])
        heap = [intervals[0][1]]  # heap为小根堆，存储会议的结束时间
        for i in intervals[1:]:
            if heap[0] <= i[0]:  # 当会议i开始时，已经有会议结束了,可以空一间房间
                heapq.heappop(heap)
            heapq.heappush(heap, i[1])

        return len(heap)
