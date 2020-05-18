# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/18 11:27
 @Author  : QDY
 @FileName: 152. 乘积最大子数组_动态规划.py

 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

    示例 1:
    输入: [2,3,-2,4]
    输出: 6
    解释: 子数组 [2,3] 有最大乘积 6。

    示例 2:
    输入: [-2,0,-1]
    输出: 0
    解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

"""


class Solution:
    def maxProduct(self, nums):
        # # 1.
        # res = max(nums)
        # while nums[0] == 0:  # 1.1 先去除首尾两端的0
        #     nums.pop(0)
        #     if not nums: return 0 # 全是0的情况直接返回0
        # while nums[-1] == 0:
        #     nums.pop()
        # zero = []
        # negative = []
        # length = len(nums)
        # for i in range(length):  # 1.2 先把0找出来，求以0为分界点分割开的各个区间各自的最大乘积
        #     if nums[i] == 0:
        #         zero.append((i,negative)) # 在找到0之后，把1.3记录的负数的位置也添加进zero[i][1]中
        #         negative = []
        #     elif nums[i] < 0:  # 1.3 同时记录负数出现的位置
        #         negative.append(i)

        # def max_product(nums,start,end,negative):  # 根据起点，终点，和起点到终点直接的负数坐标求nums[start:end+1]的最大乘积
        #     if start==end:return nums[start]
        #     if len(negative) % 2 == 0:  # 若有偶数个负数，则最大乘积=所有数累乘
        #         x = 1
        #         for i in range(start,end+1):
        #             x *= nums[i]
        #         return x
        #     else:  # 若有奇数个负数，则最大乘积=max(从头累乘到最后一个负数之前，从第一个负数之后累乘到终点)
        #         x1,x2 = 1,1
        #         for i in range(start,negative[-1]):
        #             x1 *= nums[i]
        #         for i in range(negative[0]+1,end+1):
        #             x2 *= nums[i]
        #         return max(x1,x2)

        # start = 0
        # for i in zero:  # 求被0分割出的每一段不含0区间的最大乘积
        #     res = max(res,max_product(nums,start,i[0]-1,i[1]))
        #     start = i[0]+1
        # res = max(res,max_product(nums,start,length-1,negative)) # nums[最后一个0 + 1:length]的最大乘积

        # return res

        # 2.动态规划 时间复杂度O(n)
        max_dp, min_dp, res = nums[0], nums[0], nums[0]
        # max_dp[i]记录以nums[i]结尾的子数组的最大乘积
        # min_dp[i]记录以nums[i]结尾的子数组的最小乘积（希望乘积尽可能的小）
        # 2.1 当遇到nums[i]==0时，max_dp[i]=min_dp[i]=0，（终点）
        #     接着不遇到0，就有新的起点
        #     2.1.1 num[i+1]>0时，max_dp[i+1]=num[i+1]，min_dp[i+1]=0
        #     2.1.2 num[i+1]<0时，max_dp[i+1]=0，min_dp[i+1]=num[i+1]
        # 2.2 当nums[i]为第奇数个负数时，max_dp[i-1是非负数
        #     min_dp[i]=max_dp[i-1]*nums[i]
        #     max_dp[i]=nums[i] or 0
        #     2.2.1 当nums[i+1]为正数时，max_dp将以nums[i+1]为新的起点
        # 2.3 当nums[i]为第偶数个负数时，min_dp[i-1]为负数
        #     max_dp[i] = min_dp[i]*nums[i]
        for i in range(1, len(nums)):
            max_tmp = max_dp * nums[i]
            min_tmp = min_dp * nums[i]
            max_dp = max(max_tmp, max(nums[i], min_tmp))
            min_dp = min(min_tmp, min(nums[i], max_tmp))
            res = max(res, max_dp)
        return res

        # # 3.实质是1的改进版：分别从左到右和从右到左各累成一遍，记录其中出现的最大值
        # a,b,res = nums[0],nums[-1],max(nums[0],nums[-1])
        # length = len(nums)
        # # 若共有偶数个负数，则最大累乘就是无零区间全部累乘
        # # 若是奇数个负数，则一个无零区间的最大累乘为max(从左乘到右出现的最大乘积，从右乘到左出现的最大乘积)
        # for i in range(1,length):
        #     if a == 0: a = nums[i]  # 若被乘0后还有后续的数，则开始新的累乘（相当于以0为分割点）
        #     else:a *= nums[i]
        #     if b == 0 : b = nums[length-1-i]
        #     else:b *= nums[length-1-i]
        #     res = max(res,max(a,b))
        # return res
