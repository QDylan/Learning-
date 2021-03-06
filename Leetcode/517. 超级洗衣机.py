# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-10 15:18
 @Author  : QDY
 @FileName: 517. 超级洗衣机.py
 @Software: PyCharm
"""
"""
假设有 n台超级洗衣机放在同一排上。开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的。

在每一步操作中，你可以选择任意 m（1 ≤ m ≤ n）台洗衣机，与此同时将每台洗衣机的一件衣服送到相邻的一台洗衣机。

给定一个非负整数数组代表从左至右每台洗衣机中的衣物数量，请给出能让所有洗衣机中剩下的衣物的数量相等的最少的操作步数。
如果不能使每台洗衣机中衣物的数量相等，则返回 -1。

示例 1：
输入: [1,0,5]
输出: 3
解释: 
第一步:    1     0 <-- 5    =>    1     1     4
第二步:    1 <-- 1 <-- 4    =>    2     1     3    
第三步:    2     1 <-- 3    =>    2     2     2  

示例 2：
输入: [0,3,0]
输出: 2
解释: 
第一步:    0 <-- 3     0    =>    1     2     0    
第二步:    1     2 --> 0    =>    1     1     1     

示例 3:
输入: [0,2,0]
输出: -1
解释: 
不可能让所有三个洗衣机同时剩下相同数量的衣物。

提示：
n 的范围是 [1, 10000]。
在每台超级洗衣机中，衣物数量的范围是 [0, 1e5]。

"""


class Solution:
    def findMinMoves(self, machines) -> int:
        #
        sum_ = sum(machines)
        N = len(machines)
        if sum_ % N != 0: return -1
        M = sum_ // N  # 每个洗衣机的目标衣物数量
        res, prefix, max_sum = 0, 0, 0
        for m in machines:
            m -= M  # 若m为负数，则表示还需要的衣物数；正数表示多余的衣物数；目标转变为使每个位置的数量为0
            prefix += m  # prefix前缀和表示总共多余or需要的衣物数
            max_sum = max(max_sum, abs(prefix))  # max_sum记录 前缀和的最大绝对值
            res = max(res, m, max_sum)  # 最少的操作步数为“数组元素的最大值”和“数组元素前缀和的绝对值的最大值”中的较大值
            # 一个位置每次最多减少1，最多能增加2
        return res
