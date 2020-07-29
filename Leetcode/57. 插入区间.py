# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/29 22:09
 @Author  : QDY
 @FileName: 57. 插入区间.py
 @Software: PyCharm
"""
"""
    给出一个无重叠的 ，按照区间起始端点排序的区间列表。
    在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

    示例 1:
    输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
    输出: [[1,5],[6,9]]

    示例 2:
    输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    输出: [[1,2],[3,10],[12,16]]
    解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

"""
class Solution:
    def insert(self, intervals, newInterval):
        if not intervals or newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
        length = len(intervals)
        merge = False
        for i in range(length):
            if newInterval[1] < intervals[i][0]:
                intervals.insert(i,newInterval)
                break
            if newInterval[0]<=intervals[i][0]<=newInterval[1] or  intervals[i][0]<=newInterval[0]<=intervals[i][1]:
                intervals[i][0] = min(intervals[i][0],newInterval[0])
                intervals[i][1] = max(intervals[i][1],newInterval[1])
                while i+1 < len(intervals):
                    if intervals[i+1][0] <= intervals[i][1]:
                        intervals[i][1] = max(intervals[i][1],intervals[i+1][1])
                        intervals.pop(i+1)
                    else:
                        break
                break
        return intervals

        # for i in range(length):
        #     if intervals[i][1] >= newInterval[0]:  # intervals[i]为第一个在new右侧的区间
        #         if intervals[i][0] > newInterval[1]:  # intervals[i]整体在new之后
        #             start, end = i, i-1
        #             break
        #         start,end = i, None
        #         for j in range(i+1,length):
        #             if intervals[j][0] > newInterval[1]:
        #                 end = j - 1
        #                 break
        #         if end is None:
        #             end = length-1
        #         break

        # if start <= end:
        #     newInterval[0] = min(newInterval[0],intervals[start][0])
        #     newInterval[1] = max(newInterval[1],intervals[end][1])
        # intervals[start:end+1] = [newInterval]
        # return intervals