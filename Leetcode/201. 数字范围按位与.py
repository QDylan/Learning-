# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/23 9:33
 @Author  : QDY
 @FileName: 201. 数字范围按位与.py
 @Software: PyCharm
"""
"""
    给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。

    示例 1:
    输入: [5,7]
    输出: 4

    示例 2:
    输入: [0,1]
    输出: 0

"""
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # 0 & x == 0
        # i = 0
        # while m != n:
        #     m >>= 1  # m n 每次右移一位，直到相等
        #     n >>= 1  # 找到了最长公共前缀 m
        #     i += 1  # 记录右移了多少步
        # return m << i

        while n>m:
            n &= n-1  # 每次把n最右的1变为0
        return n