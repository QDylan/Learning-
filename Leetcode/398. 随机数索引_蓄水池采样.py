# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/8 17:07
 @Author  : QDY
 @FileName: 398. 随机数索引_蓄水池采样.py

    给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。

    注意：
    数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。

    示例:
    int[] nums = new int[] {1,2,3,3,3};
    Solution solution = new Solution(nums);

    // pick(3) 应该返回索引 2,3 或者 4。每个索引的返回概率应该相等。
    solution.pick(3);

    // pick(1) 应该返回 0。因为只有nums[0]等于1。
    solution.pick(1);

"""
import random


class Solution:

    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):  # 当你遇到第 i 个元素时，有1/i的概率选择该元素，1-1/i的概率保持原有的选择
        i, res = 1, None
        for j in range(len(self.nums)):
            if self.nums[j] == target:
                if random.randint(1, i) == 1:
                    res = j
                i += 1
        return res

    # Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
