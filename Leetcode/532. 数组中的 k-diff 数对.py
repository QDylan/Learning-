# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-07 10:34
 @Author  : QDY
 @FileName: 532. 数组中的 k-diff 数对.py
 @Software: PyCharm
"""
"""
给定一个整数数组和一个整数k，你需要在数组里找到不同的k-diff 数对。
这里将k-diff数对定义为一个整数对 (i, j)，其中 i 和 j 都是数组中的数字，且两数之差的绝对值是k 。

示例 1：
输入：[3, 1, 4, 1, 5], k = 2
输出：2
解释：数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
尽管数组中有两个1，但我们只应返回不同的数对的数量。

示例 2：
输入：[1, 2, 3, 4, 5], k = 1
输出：4
解释：数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5)。

示例 3：
输入：[1, 3, 1, 5, 4], k = 0
输出：1
解释：数组中只有一个 0-diff 数对，(1, 1)。

示例 4：
输入：nums = [1,2,4,4,3,3,0,9,2,3], k = 3
输出：2

示例 5：
输入：nums = [-1,-2,-3], k = 1
输出：2

提示：
1 <= nums.length <= 104
-107 <= nums[i] <= 107
0 <= k <= 107

"""
from collections import Counter


class Solution:
    def findPairs(self, nums, k: int) -> int:
        res = 0
        cnt = Counter(nums)
        if k == 0:
            for n in cnt:
                if cnt[n] > 1: res += 1
        else:
            for n in cnt:
                if n + k in cnt: res += 1
        return res
