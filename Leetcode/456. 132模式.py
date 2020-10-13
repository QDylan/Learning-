# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-13 10:17
 @Author  : QDY
 @FileName: 456. 132模式.py
 @Software: PyCharm
"""
"""
给定一个整数序列：a1, a2, ..., an，一个132模式的子序列ai, aj, ak被定义为：当 i < j < k 时，ai < ak < aj。
设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。

注意：n 的值小于15000。

示例1:
输入: [1, 2, 3, 4]
输出: False
解释: 序列中不存在132模式的子序列。

示例 2:
输入: [3, 1, 4, 2]
输出: True
解释: 序列中有 1 个132模式的子序列： [1, 4, 2].

示例 3:
输入: [-1, 3, 2, 0]
输出: True
解释: 序列中有 3 个132模式的的子序列: [-1, 3, 2], [-1, 3, 0] 和 [-1, 2, 0].

"""


class Solution:
    def find132pattern(self, nums) -> bool:
        if len(nums) < 3: return False
        stack, min_val = [], -float('inf')  # 构造一个单调下降的栈
        for i in nums[::-1]:  # 从后往前遍历
            if i < min_val: return True  # 当i比min_val还小(2的上界)时，找到132序列
            while stack and i > stack[-1]:  # 此时 i 可以作为3
                min_val = stack.pop()  # 记录最后从栈中弹出的元素，作为2的上界
            stack.append(i)
        return False
