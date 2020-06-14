# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/14 23:24
 @Author  : QDY
 @FileName: 5423. 找两个和为目标值且不重叠的子数组_动态规划.py
 给你一个整数数组 arr 和一个整数值 target 。

    请你在 arr 中找 两个互不重叠的子数组 且它们的和都等于 target 。可能会有多种方案，请你返回满足要求的两个子数组长度和的 最小值 。
    请返回满足要求的最小长度和，如果无法找到这样的两个子数组，请返回 -1 。

    示例 1：
    输入：arr = [3,2,2,4,3], target = 3
    输出：2
    解释：只有两个子数组和为 3 （[3] 和 [3]）。它们的长度和为 2 。

    示例 2：
    输入：arr = [7,3,4,7], target = 7
    输出：2
    解释：尽管我们有 3 个互不重叠的子数组和为 7 （[7], [3,4] 和 [7]），但我们会选择第一个和第三个子数组，因为它们的长度和 2 是最小值。

    示例 3：
    输入：arr = [4,3,2,6,2,3,4], target = 6
    输出：-1
    解释：我们只有一个和为 6 的子数组。

    示例 4：
    输入：arr = [5,5,4,4,5], target = 3
    输出：-1
    解释：我们无法找到和为 3 的子数组。

    示例 5：
    输入：arr = [3,1,1,1,5,1,2,1], target = 3
    输出：3
    解释：注意子数组 [1,2] 和 [2,1] 不能成为一个方案因为它们重叠了。
     

    提示：
    1 <= arr.length <= 10^5
    1 <= arr[i] <= 1000
    1 <= target <= 10^8

"""


class Solution:
    def minSumOfLengths(self, arr, target):
        length = len(arr)
        # 动态规划
        # dp[i]=arr[:i+1]中和为target的最短子数组长度
        # 若有以arr[i]结尾的子数组arr[x+1:i+1]和为target
        #   dp[i] = min(dp[i-1],(i-x)+dp[x])
        # 否则 dp[i] = dp[i-1]

        dp = [float('inf')] * length
        prefix, res = 0, float('inf')
        sum_dict = {0: -1}  # prefix:id 前缀和为prefix的末尾元素id,没有负数就不会有相同的prefix
        # 初始设置0:-1，这样若存在arr[x]==target也能找到

        for i in range(length):
            prefix += arr[i]
            dp[i] = dp[i - 1]
            if prefix - target in sum_dict:  # 此时存在x,使得arr[:x+1]=prefix-target
                # 即 子数组arr[x+1:i+1]==target，长度cur_len=i-x
                cur_len = i - sum_dict[prefix - target]
                if i - cur_len >= 0:  #
                    # 若在arr[:i-cur_len+1]中有和为target的子数组，则可以尝试更新res
                    res = min(res, cur_len + dp[i - cur_len])
                dp[i] = min(dp[i], cur_len)  # 更新dp[i]
            sum_dict[prefix] = i
        return res if res != float('inf') else -1
