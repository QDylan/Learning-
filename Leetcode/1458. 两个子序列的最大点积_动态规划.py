# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/25 21:50
 @Author  : QDY
 @FileName: 1458. 两个子序列的最大点积_动态规划.py

    给你两个数组 nums1 和 nums2 。
    请你返回 nums1 和 nums2 中两个长度相同的 非空 子序列的最大点积。
    数组的非空子序列是通过删除原数组中某些元素（可能一个也不删除）后剩余数字组成的序列，
    但不能改变数字间相对顺序。比方说，[2,3,5] 是 [1,2,3,4,5] 的一个子序列而 [1,5,3] 不是。

    示例 1：
    输入：nums1 = [2,1,-2,5], nums2 = [3,0,-6]
    输出：18
    解释：从 nums1 中得到子序列 [2,-2] ，从 nums2 中得到子序列 [3,-6] 。
    它们的点积为 (2*3 + (-2)*(-6)) = 18 。

    示例 2：
    输入：nums1 = [3,-2], nums2 = [2,-6,7]
    输出：21
    解释：从 nums1 中得到子序列 [3] ，从 nums2 中得到子序列 [7] 。
    它们的点积为 (3*7) = 21 。

    示例 3：
    输入：nums1 = [-1,-1], nums2 = [1,1]
    输出：-1
    解释：从 nums1 中得到子序列 [-1] ，从 nums2 中得到子序列 [1] 。
    它们的点积为 -1 。
"""


class Solution:
    def maxDotProduct(self, nums1, nums2):
        # if all(n1<=0 for n1 in nums1) and all(n2>=0 for n2 in nums2):return max(nums1)*min(nums2)
        # if all(n1>=0 for n1 in nums1) and all(n2<=0 for n2 in nums2):return min(nums1)*max(nums2)

        # 动态规划
        # dp[i][j] 表示nums1[:i]与nums2[:j]的最大点积
        # dp[i][j] = max(1.不选择nums1[i-1]]:dp[i-1][j],
        #                2.不选择nums2[j-1]:dp[i][j-1],
        #                3. 只选择nums1[i-1]和nums2[j-1]:nums1[i-1]*nums2[j-1](因为之前的点积都是负的)
        #                4. 新选择nums1[i-1]和nums[j-1]: dp[i-1][j-1]+nums1[i-1]*nums2[j-1],
        #                )
        len1, len2 = len(nums1), len(nums2)
        dp_prev = [-float('inf')] * (len2 + 1)
        dp_cur = [-float('inf')] * (len2 + 1)
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                x = nums1[i - 1] * nums2[j - 1]
                dp_cur[j] = max(dp_prev[j], dp_cur[j - 1], x, dp_prev[j - 1] + x)
                # dp_cur[j] = max(dp_prev[j],dp_cur[j-1],dp_prev[j-1]+nums1[i-1]*nums2[j-1])
            dp_prev, dp_cur = dp_cur, [-float('inf')] * (len2 + 1)
        return dp_prev[-1]
