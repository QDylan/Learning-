# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-04 16:44
 @Author  : QDY
 @FileName: 5517. 找到处理最多请求的服务器.py
 @Software: PyCharm
"""
"""
你有 k个服务器，编号为 0到 k-1，它们可以同时处理多个请求组。每个服务器有无穷的计算能力但是 不能同时处理超过一个请求。请求分配到服务器的规则如下：

第i（序号从 0 开始）个请求到达。
如果所有服务器都已被占据，那么该请求被舍弃（完全不处理）。
如果第(i % k)个服务器空闲，那么对应服务器会处理该请求。
否则，将请求安排给下一个空闲的服务器（服务器构成一个环，必要的话可能从第 0 个服务器开始继续找下一个空闲的服务器）。
比方说，如果第 i个服务器在忙，那么会查看第 (i+1)个服务器，第 (i+2)个服务器等等。
给你一个 严格递增的正整数数组arrival，表示第i个任务的到达时间，和另一个数组load，
其中load[i]表示第i个请求的工作量（也就是服务器完成它所需要的时间）。
你的任务是找到 最繁忙的服务器。最繁忙定义为一个服务器处理的请求数是所有服务器里最多的。

请你返回包含所有最繁忙服务器序号的列表，你可以以任意顺序返回这个列表。

示例 1：
输入：k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3] 
输出：[1] 
解释：
所有服务器一开始都是空闲的。
前 3 个请求分别由前 3 台服务器依次处理。
请求 3 进来的时候，服务器 0 被占据，所以它呗安排到下一台空闲的服务器，也就是服务器 1 。
请求 4 进来的时候，由于所有服务器都被占据，该请求被舍弃。
服务器 0 和 2 分别都处理了一个请求，服务器 1 处理了两个请求。所以服务器 1 是最忙的服务器。

示例 2：
输入：k = 3, arrival = [1,2,3,4], load = [1,2,1,2]
输出：[0]
解释：
前 3 个请求分别被前 3 个服务器处理。
请求 3 进来，由于服务器 0 空闲，它被服务器 0 处理。
服务器 0 处理了两个请求，服务器 1 和 2 分别处理了一个请求。所以服务器 0 是最忙的服务器。

示例 3：
输入：k = 3, arrival = [1,2,3], load = [10,12,11]
输出：[0,1,2]
解释：每个服务器分别处理了一个请求，所以它们都是最忙的服务器。

示例 4：
输入：k = 3, arrival = [1,2,3,4,8,9,10], load = [5,2,10,3,1,2,2]
输出：[1]

示例 5：
输入：k = 1, arrival = [1], load = [1]
输出：[0]

提示：

1 <= k <= 105
1 <= arrival.length, load.length <= 105
arrival.length == load.length
1 <= arrival[i], load[i] <= 109
arrival保证 严格递增。
"""
from sortedcontainers import SortedList
import heapq


class Solution:
    def busiestServers(self, k: int, arrival, load):
        valid = SortedList(range(k))  # 记录可用的服务器
        timeline = []  # 最小堆，存储 (服务器的释放时间，服务器id)
        n = len(arrival)
        count = [0 for i in range(k)]  # 记录服务器使用次数
        for i in range(n):
            while len(timeline) > 0:
                t, pos = heapq.heappop(timeline)  # 取出最早能释放的服务器
                if t <= arrival[i]:  # 可以释放，加入可用列表
                    valid.add(pos)
                else:  # 还不能释放，放回去，跳出循环
                    heapq.heappush(timeline, (t, pos))
                    break

            if len(valid) == 0:  # 无可用服务器，当前任务不执行
                continue

            key = valid.bisect_left(i % k)  # 二分查找选出i%k后的最近可用服务器
            if key < len(valid):  # 取出服务器原id
                pos = valid[key]
            else:  # 若i%k后无可用服务器，则选择最小编号的
                pos = valid[0]
            count[pos] += 1
            valid.remove(pos)  # 从可用列表中移除pos
            heapq.heappush(timeline, (arrival[i] + load[i], pos))
        max_ = max(count)
        res = []
        for i in range(k):
            if count[i] == max_:
                res.append(i)
        return res
