# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-14 10:36
 @Author  : QDY
 @FileName: 135. 分发糖果.py
 @Software: PyCharm
"""
"""
老师想给孩子们分发糖果，有 N个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
你需要按照以下要求，帮助老师给这些孩子分发糖果：
每个孩子至少分配到 1 个糖果。
相邻的孩子中，评分高的孩子必须获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？

示例1:
输入: [1,0,2]
输出: 5
解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。

示例2:
输入: [1,2,2]
输出: 4
解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这已满足上述两个条件。

"""


class Solution:
    def candy(self, ratings) -> int:
        N = len(ratings)
        left, right = [1] * N, [1] * N  # 初始化每个人1颗糖果
        for i in range(1, N):  # 第一遍从左往右扫描
            if ratings[i] > ratings[i - 1]:  # 比左边高的话糖果数量就比左边多1
                left[i] = left[i - 1] + 1
        res = left[-1]
        for i in range(N - 2, -1, -1):  # 第二遍从右往左扫描
            if ratings[i] > ratings[i + 1]:  # 比右边高的话糖果数量就比右边多1
                right[i] = right[i + 1] + 1
            res += max(left[i], right[i])  # 最终结果取两种情况的最大值
        return res
