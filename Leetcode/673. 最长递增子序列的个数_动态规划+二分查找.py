# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/18 15:05
 @Author  : QDY
 @FileName: 673. 最长递增子序列的个数_动态规划+二分查找.py

    给定一个未排序的整数数组，找到最长递增子序列的个数。

    示例 1:
    输入: [1,3,5,4,7]
    输出: 2
    解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。

    示例 2:
    输入: [2,2,2,2,2]
    输出: 5
    解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。

"""


class Solution:
    def findNumberOfLIS(self, nums):
        if not nums: return 0
        # # 1.动态规划 时间复杂度O(n^2)
        # # dp[i] = [以nums[i]结尾的最长递增子序列的长度,数量]
        # dp = [[1,1]]*len(nums)
        # max_len = 1
        # for i in range(1,len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             if dp[j][0] >= dp[i][0]:
        #                 dp[i] = [dp[j][0]+1,dp[j][1]]
        #             elif dp[j][0] + 1 == dp[i][0]:
        #                 dp[i][1] += dp[j][1]
        #     max_len = max(max_len, dp[i][0])
        # res = 0
        # for i in dp:
        #     if i[0] == max_len:
        #         res += i[1]
        # return res

        # 2. 改进的动态规划 时间复杂度O(nlogn)
        # dp[i] = [[长度为i的递增子序列的结尾元素，以大于等于该元素结尾的长度为i的递增子序列的数目],[]]
        dp = [[[nums[0], 1]]]
        # dp[i][-1] [为长度为i的递增子序列中结尾元素最小的元素，以大于等于该元素结尾的长度为i的递增子序列的数目]
        length = 1
        for i in range(1, len(nums)):
            left, right = 0, length - 1  # 在dp中二分搜索查找nums[i]应放位置left，应满足
            while left <= right:  # dp[left][-1][0]是大于等于nums[i]的最左位置
                mid = left + (right - left) // 2
                if dp[mid][-1][0] < nums[i]:  # 中间值小于目标值，增大左边界
                    left = mid + 1
                else:
                    right = mid - 1
            if left == length:  # 若left==length，说明找到了新的最长的子序列
                length += 1
                tmp = 0
                l, r = 0, len(dp[-1]) - 1  # dp[-1][][0]为降序排序
                while l <= r:  # 二分搜索查找dp[-1][][0]中大于等于nums[i]的最右位置right
                    m = l + (r - l) // 2
                    if dp[-1][m][0] >= nums[i]:
                        l = m + 1
                    else:
                        r = m - 1
                if r >= 0:  # 若right<0，则说明dp[-1][][0]都小于nums[i]
                    tmp = dp[-1][r][1]
                dp.append([[nums[i], dp[-1][-1][1] - tmp]])
            else:
                if left > 0:  # 若left>0，则长度为left的以大于等于nums[i]的结尾的子序列的数量
                    tmp = 0  # == dp[left][-1][1]+dp[left-1][-1][1]-dp[left-1][大于等于nums[i]的最右位置][1]
                    l, r = 0, len(dp[left - 1]) - 1  # dp[left-1][][0]为降序排序
                    while l <= r:  # 二分搜索查找dp[left-1][][0]中大于等于nums[i]的最右位置right
                        m = l + (r - l) // 2
                        if dp[left - 1][m][0] >= nums[i]:
                            l = m + 1
                        else:
                            r = m - 1
                    if r >= 0:
                        tmp = dp[left - 1][r][1]
                    dp[left].append([nums[i], dp[left][-1][1] + dp[left - 1][-1][1] - tmp])
                else:  # 若left==0,则长度为1的以大于等于nums[i]的结尾的子序列的数量=dp[left][-1][1]+1
                    dp[left].append([nums[i], dp[left][-1][1] + 1])
        # print(dp)
        return dp[-1][-1][1]

# 3.树状数组
