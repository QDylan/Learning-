# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/31 15:32
 @Author  : QDY
 @FileName: 1012. 至少有 1 位重复的数字_hard.py
 @Software: PyCharm
"""
"""
    给定正整数 N，返回小于等于 N 且具有至少 1 位重复数字的正整数的个数。

    示例 1：
    输入：20
    输出：1
    解释：具有至少 1 位重复数字的正数（<= 20）只有 11 。

    示例 2：
    输入：100
    输出：10
    解释：具有至少 1 位重复数字的正数（<= 100）有 11，22，33，44，55，66，77，88，99 和 100 。

    示例 3：
    输入：1000
    输出：262
     
    提示：
    1 <= N <= 10^9
    通过次数1,973提交次数

"""
from math import factorial


class Solution:

    def numDupDigitsAtMostN(self, N: int) -> int:

        digits = [int(x) for x in str(N)]  #
        length = len(digits)

        # A = {}  # 打表
        # for i in range(length):
        #     m = 9-i
        #     for j in range(m+1):
        #         A[m,j] = factorial(m)//factorial(m-j)

        def A(i, j):
            return factorial(i) // factorial(i - j)

        # 计算 各数位上无重复数字的数 的个数
        count = 1  # 先假设N是无重复数字的
        # 计算i+2位数最高位为0时，剩余数位为i+1,第一位取1~9,剩余i位：从9个数中取i个数进行排列A(9,i)
        for i in range(length - 1):
            # count += 9 * A[9,i]
            count += 9 * A(9, i)

        # 计算最高位不为0时
        used_num = set()
        for i in range(length):  # 从最高位开始遍历
            # 若 N = 35462, 则先计算10000~20000, 20000~30000中有多少个不重复的数
            # 再 计算 30000~35000 有多少个不重复数字的数 -> 35000~35400 -> 35400~35460 -> 35460~35462
            for j in range(int(i == 0), digits[i]):
                if j not in used_num:  # length位数，已有i+1个数字，从剩余9-i个数字中，选出length-i-1个
                    # count += A[9 - i, length - i - 1]
                    count += A(9 - i, length - i - 1)
            if digits[i] in used_num:  # 遇到重复的数字，跳出循环
                count -= 1  # N是有重复数字的，count-1
                break
            used_num.add(digits[i])

        return N - count
