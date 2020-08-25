# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/25 9:30
 @Author  : QDY
 @FileName: 491. 递增子序列.py
 @Software: PyCharm
"""
"""
    给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

    示例:

    输入: [4, 6, 7, 7]
    输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
    说明:

    给定数组的长度不会超过15。
    数组中的整数范围是 [-100,100]。
    给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。

"""


class Solution:
    def findSubsequences(self, nums):
        n = len(nums)
        self.res = []
        visited = set()

        def dfs(index, cur):
            for i in range(index + 1, n):
                if nums[i] >= nums[index]:
                    tmp = cur + [nums[i]]
                    if tuple(tmp) not in visited:
                        visited.add(tuple(tmp))
                        self.res.append(tmp)
                        dfs(i, tmp)

        for i in range(n - 1):
            if nums[i] not in visited:
                visited.add(nums[i])
                dfs(i, [nums[i]])
        return self.res
