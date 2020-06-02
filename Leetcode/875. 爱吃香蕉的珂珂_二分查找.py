# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/2 13:50
 @Author  : QDY
 @FileName: 875. 爱吃香蕉的珂珂_二分查找.py

    珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。
    珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。
    如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  
    珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。
    返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。


    示例 1：
    输入: piles = [3,6,7,11], H = 8
    输出: 4

    示例 2：
    输入: piles = [30,11,23,4,20], H = 5
    输出: 30

    示例 3：
    输入: piles = [30,11,23,4,20], H = 6
    输出: 23

"""


class Solution:
    def minEatingSpeed(self, piles, H):
        # 暴力遍历，从K=1到max(piles),用二分查找加速
        k = max(piles)
        if H == len(piles): return k

        def count_h(K):  # 计算速度为K时，
            h = 0
            for i in piles:
                h += (i - 1) // K + 1
            return h

        left, right = 1, k
        while left <= right:
            mid = left + (right - left) // 2
            if count_h(mid) <= H:  # 时间比预计的少，可以减小速度
                right = mid - 1
            else:  # 时间比预计的多，需要增加速度
                left = mid + 1
        return left
