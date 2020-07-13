# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/13 17:50
 @Author  : QDY
 @FileName: 60. 第k个排列.py

    给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
    按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
    "123"
    "132"
    "213"
    "231"
    "312"
    "321"
    给定 n 和 k，返回第 k 个排列。

    说明：
    给定 n 的范围是 [1, 9]。
    给定 k 的范围是[1,  n!]。

    示例 1:
    输入: n = 3, k = 3
    输出: "213"

    示例 2:
    输入: n = 4, k = 9
    输出: "2314"

"""
import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # nums = [str(i) for i in range(1,n+1)]
        # self.cnt,self.res = 0,''
        # def dfs(arr,tmp_nums):
        #     if not tmp_nums:
        #         self.cnt += 1
        #         if self.cnt == k:
        #             self.res = arr
        #         return
        #     for i in range(len(tmp_nums)):
        #         dfs(arr+tmp_nums[i],tmp_nums[:i]+tmp_nums[i+1:])
        #         if self.res:
        #             return
        # dfs('',nums)
        # return self.res
        nums = [str(i) for i in range(1, n + 1)]
        res = ''
        while k > 1:  # 当k==1时，res + nums剩余的字符按顺序排列就为所求
            cnt = math.factorial(len(nums) - 1)
            for i in range(len(nums)):  # 当前位置为nums[i],后面有cnt种排列
                if k > cnt:  # k>cnt，说明第k个不在这cnt种排列种
                    k -= cnt  #
                else:  # k<=cnt 说明 第k个在以当前位置为nums[i]的cnt个排列种
                    res += nums[i]
                    nums.pop(i)  # 从nums种删除这个字符
                    break  # 跳出循环，寻找下一个位置是哪个字符
        return res + ''.join(nums)
