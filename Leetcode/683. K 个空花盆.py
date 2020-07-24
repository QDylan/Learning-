# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/24 11:13
 @Author  : QDY
 @FileName: 683. K 个空花盆.py
 @Software: PyCharm
"""
"""
    花园里有 N 个花盆，每个花盆里都有一朵花。这 N 朵花会在 N 天内依次开放，每天有且仅有一朵花会开放并且会一直盛开下去。
    给定一个数组 flowers 包含从 1 到 N 的数字，每个数字表示在那一天开放的花所在的花盆编号。
    例如， flowers[i] = x 表示在第 i+1 天盛开的花在第 x 个花盆中，i 和 x 都在 1 到 N 的范围内。
    给你一个整数 k，请你输出在哪一天恰好有两朵盛开的花，他们中间间隔了 k 朵花并且都没有开放。
    如果不存在，输出 -1。

    样例 1:
    输入: 
    flowers: [1,3,2]
    k: 1
    输出: 2
    解释: 在第二天，第一朵和第三朵花都盛开了。
     
    样例 2:
    输入: 
    flowers: [1,2,3]
    k: 1
    输出: -1
     
    注释 :
    给定的数组范围是 [1, 20000]。

"""


class Solution:
    def kEmptySlots(self, bulbs, K):
        len_b = len(bulbs)
        days = [0] * len_b
        for i in range(len_b):  # days[i] = 索引为i的花的开放时间
            days[bulbs[i] - 1] = i

        res = float('inf')
        left, right = 0, K + 1  # 滑动窗口 左右边界
        while right < len_b:
            tmp = max(days[left], days[right])
            mid = left + 1
            while mid < right:
                if days[mid] < tmp:
                    break
                mid += 1
            if mid == right:  # 该窗口中的K朵花都还未开放
                res = min(tmp, res)
            # 更新窗口边界，left~mid中的花的开放时间都比left的晚
            left, right = mid, mid + K + 1
        return res + 1 if res != float('inf') else -1
