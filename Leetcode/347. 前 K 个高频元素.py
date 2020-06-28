# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/28 17:47
 @Author  : QDY
 @FileName: 347. 前 K 个高频元素.py

    给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

    示例 1:
    输入: nums = [1,1,1,2,2,3], k = 2
    输出: [1,2]

    示例 2:
    输入: nums = [1], k = 1
    输出: [1]
     
    提示：
    你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
    你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
    题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
    你可以按任意顺序返回答案。

"""
from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        d = Counter(nums)
        res = []

        def heapify(i):  # 维护一个小根堆
            if i >= k: return
            l, r, smallest = 2 * i + 1, 2 * i + 2, i
            if l < k and d[res[l]] < d[res[smallest]]:
                smallest = l
            if r < k and d[res[r]] < d[res[smallest]]:
                smallest = r
            if smallest != i:
                res[smallest], res[i] = res[i], res[smallest]
                heapify(smallest)

        for key in d:
            if len(res) < k:
                res.append(key)
                son = len(res) - 1
                pa = (son - 1) // 2
                while son > 0 and d[res[son]] < d[res[pa]]:
                    res[son], res[pa] = res[pa], res[son]
                    pa, son = (pa - 1) // 2, pa
            elif len(res) == k and d[key] > d[res[0]]:
                res[0] = key
                heapify(0)
        return res
