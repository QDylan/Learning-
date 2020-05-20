# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/20 18:52
 @Author  : QDY
 @FileName: 594. 最长和谐子序列.py

    和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。

    现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。

    示例 1:
    输入: [1,3,2,2,5,2,3,7]
    输出: 5
    原因: 最长的和谐数组是：[3,2,2,2,3].

"""


class Solution:
    def findLHS(self, nums):
        if not nums: return 0
        # 1.先排序
        # nums.sort()
        # res = 0
        # prev = nums[0]
        # prev_cnt = 1
        # i = 1
        # while i < len(nums):
        #     if nums[i]==prev:
        #         prev_cnt += 1
        #         i += 1
        #     else:
        #         if nums[i]-prev==1:
        #             cur = nums[i]
        #             cur_cnt = 0
        #             while i<len(nums) and nums[i]==cur:
        #                 cur_cnt += 1
        #                 i += 1
        #             res = max(res, prev_cnt + cur_cnt)
        #             prev = cur
        #             prev_cnt = cur_cnt
        #         else:
        #             prev = nums[i]
        #             prev_cnt = 1
        #             i += 1
        # return res

        # 2.哈希映射
        hash_map = {}
        for i in nums:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        # print(hash_map)
        res = 0
        for num in hash_map:
            if num - 1 in hash_map:
                res = max(hash_map[num] + hash_map[num - 1], res)

        return res
