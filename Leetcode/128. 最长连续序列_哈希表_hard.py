# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/6 9:18
 @Author  : QDY
 @FileName: 128. 最长连续序列_哈希表_hard.py

    给定一个未排序的整数数组，找出最长连续序列的长度。
    要求算法的时间复杂度为 O(n)。

    示例:
    输入: [100, 4, 200, 1, 3, 2]
    输出: 4
    解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

"""


class Solution:
    def longestConsecutive(self, nums):
        hash_m = set(nums)  # 哈希表去重
        res = 0
        for n in nums:
            if n - 1 not in hash_m:  # 只对连续序列的开头进行搜索
                cur = n  # 保证内层循环中每个数都只被遍历一次
                tmp_res = 1
                while cur + 1 in hash_m:
                    tmp_res += 1
                    cur += 1
                res = max(res, tmp_res)
        return res
