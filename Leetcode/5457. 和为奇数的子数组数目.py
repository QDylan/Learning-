# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/27 10:26
 @Author  : QDY
 @FileName: 5457. 和为奇数的子数组数目.py
 @Software: PyCharm
"""
"""
    给你一个整数数组 arr 。请你返回和为 奇数 的子数组数目。
    由于答案可能会很大，请你将结果对 10^9 + 7 取余后返回。

    示例 1：
    输入：arr = [1,3,5]
    输出：4
    解释：所有的子数组为 [[1],[1,3],[1,3,5],[3],[3,5],[5]] 。
    所有子数组的和为 [1,4,9,3,8,5].
    奇数和包括 [1,9,3,5] ，所以答案为 4 。
    示例 2 ：

    输入：arr = [2,4,6]
    输出：0
    解释：所有子数组为 [[2],[2,4],[2,4,6],[4],[4,6],[6]] 。
    所有子数组和为 [2,6,12,4,10,6] 。
    所有子数组和都是偶数，所以答案为 0 。

    示例 3：
    输入：arr = [1,2,3,4,5,6,7]
    输出：16

    示例 4：
    输入：arr = [100,100,99,99]
    输出：4

    示例 5：
    输入：arr = [7]
    输出：1
     
    提示：
    1 <= arr.length <= 10^5
    1 <= arr[i] <= 100
"""


class Solution:
    def numOfSubarrays(self, arr) -> int:
        if not arr: return 0
        is_odd, odd, even = 0, 0, 0  # is_odd 记录到i为止的前缀和是否为奇数
        for i in arr:
            is_odd ^= i & 1
            if is_odd:
                odd += 1
            else:
                even += 1
        # odd,even记录所有前缀和中出现和奇数和，偶数和的数量
        # 从前缀和里随意选出两个数做差，差值就是子数组的和，当选出的两个数是一个奇数一个偶数时构成的子数组的和为奇数
        return (odd + odd * even) % (10 ** 9 + 7)

        # # 动态规划
        # res,odd,length = 0,[],len(arr)
        # for i in range(length):
        #     if arr[i] & 1:  # 记录每个奇数出现的位置
        #         odd.append(i)
        # if not odd:return 0  # 没有奇数，则不会有和为奇数的子数组
        # num_odd, res  = len(odd), odd[0]+1
        # dp1, dp2 = 0, odd[0]+1  # dp2记录以上一个奇数结尾有多少个合法子数组,dp1记录再上一个奇数
        # for i in range(1, num_odd):
        #     # 第i-1个奇数到第i个奇数之间有多少个偶数：odd[i]-odd[i-1]-1
        #     res += dp2*(odd[i]-odd[i-1]-1)  # 以每个偶数结尾加上以odd[i-1]结尾的合法子数组能构成新的一个合法数组
        #     dp1 += odd[i]-odd[i-1]  # 以odd[i]结尾，只含一个奇数的子数组有 odd[i]-odd[i-1] 个
        #     # 以上上个奇数结尾的合法子数组 往后一直扩展到odd[i]（相当于加了若干个偶数和两个奇数） 仍是合法的子数组
        #     res += dp1
        #     dp1, dp2 = dp2, dp1
        # res += (length-1-odd[-1])*dp2  # length-1-odd[-1]表示最后一个奇数到末尾有多少个偶数
        # return res % (10**9+7)
