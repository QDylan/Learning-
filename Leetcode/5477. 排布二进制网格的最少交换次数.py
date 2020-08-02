# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/2 17:08
 @Author  : QDY
 @FileName: 5477. 排布二进制网格的最少交换次数.py
 @Software: PyCharm
"""
"""
    给你一个nx n的二进制网格grid，每一次操作中，你可以选择网格的相邻两行进行交换。
    一个符合要求的网格需要满足主对角线以上的格子全部都是 0。
    请你返回使网格满足要求的最少操作次数，如果无法使网格符合要求，请你返回 -1。
    主对角线指的是从(1, 1)到(n, n)的这些格子。

    示例 1：
    输入：grid = [[0,0,1],[1,1,0],[1,0,0]]
    输出：3

    示例 2：
    输入：grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
    输出：-1
    解释：所有行都是一样的，交换相邻行无法使网格符合要求。
    
    示例 3：
    输入：grid = [[1,0,0],[1,1,0],[1,1,1]]
    输出：0
    提示：
    n == grid.length
    n == grid[i].length
    1 <= n<= 200
    grid[i][j]要么是0要么是1。

"""


class Solution:
    def minSwaps(self, grid) -> int:
        n = len(grid)
        zero = [0] * n  # zero[i]=j 记录第i行位置j之后全为0
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if grid[i][j]:
                    zero[i] = j
                    break
        # 主对角线上方全为0 ： 对所有的i 使得zero[i] <= i
        res = 0
        for i in range(n):
            if zero[i] <= i:  # 若这一行已经达标
                continue
            check = False
            for j in range(i + 1, n):
                if zero[j] <= i:  # 找到最近的满足该行要求的某行j
                    res += j - i
                    zero[i + 1:j + 1], zero[i] = zero[i:j], zero[j]  # 两两交换把第j行换到第i行
                    check = True
                    break
            if not check:  # 找不到合法的行
                return -1
        return res
