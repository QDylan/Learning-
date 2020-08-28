# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/1 10:00
 @Author  : QDY
 @FileName: 632. 最小区间.py
 @Software: PyCharm
"""
"""
    你有k个升序排列的整数数组。找到一个最小区间，使得k个列表中的每个列表至少有一个数包含在其中。
    我们定义如果b-a < d-c或者在b-a == d-c时a < c，则区间 [a,b] 比 [c,d] 小。

    示例 1:
    输入:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
    输出: [20,24]
    解释: 
    列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
    列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
    列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。

    注意:
    给定的列表可能包含重复元素，所以在这里升序表示 >= 。
    1 <= k <= 3500
    -105 <= 元素的值<= 105

"""
import heapq, collections


class Solution:
    def smallestRange(self, nums):
        k, heap = len(nums), []
        for i in range(k):  # 构建小根堆 时间复杂度O(nklogk),空间复杂度O(k)
            heapq.heappush(heap, (nums[i][0], i, 0))

        max_val = max(heap)[0]  # 记录 小根堆中 最大的值
        res = [heap[0][0], max_val]

        while heap[0][2] < len(nums[heap[0][1]]) - 1:
            val, id1, id2 = heapq.heappop(heap)  # 每次取出区间的左端点
            id2 += 1
            heapq.heappush(heap, (nums[id1][id2], id1, id2))
            max_val = max(nums[id1][id2], max_val)  # 更新最大的值
            tmp = [heap[0][0], max_val]
            if tmp[1] - tmp[0] < res[1] - res[0] or (tmp[1] - tmp[0] == res[1] - res[0] and tmp[0] < res[0]):
                res = tmp

        return res

        # # 哈希表+滑动窗口 时间复杂度O(nk+|V|),空间复杂度O(nk)
        # count = collections.defaultdict(int)
