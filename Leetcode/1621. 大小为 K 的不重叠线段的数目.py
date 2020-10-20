# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-20 10:27
 @Author  : QDY
 @FileName: 1621. 大小为 K 的不重叠线段的数目.py
 @Software: PyCharm
"""
"""
给你一维空间的n个点，其中第i个点（编号从0 到n-1）位于x = i处，请你找到恰好k个不重叠线段且每个线段至少覆盖两个点的方案数。
线段的两个端点必须都是整数坐标。这k个线段不需要全部覆盖全部n个点，且它们的端点可以重合。

请你返回 k个不重叠线段的方案数。由于答案可能很大，请将结果对10**9 + 7取余 后返回。

示例 1：
输入：n = 4, k = 2
输出：5
解释：
如图所示，两个线段分别用红色和蓝色标出。
上图展示了 5 种不同的方案 {(0,2),(2,3)}，{(0,1),(1,3)}，{(0,1),(2,3)}，{(1,2),(2,3)}，{(0,1),(1,2)} 。

示例 2：
输入：n = 3, k = 1
输出：3
解释：总共有 3 种不同的方案 {(0,1)}, {(0,2)}, {(1,2)} 。

示例 3：
输入：n = 30, k = 7
输出：796297179
解释：画 7 条线段的总方案数为 3796297200 种。将这个数对 109 + 7 取余得到 796297179 。

示例 4：
输入：n = 5, k = 3
输出：7

示例 5：
输入：n = 3, k = 2
输出：1

提示：
2 <= n <= 1000
1 <= k <= n-1

"""
from math import factorial


class Solution:

    def numberOfSets(self, n: int, k: int) -> int:
        if k == 1: return n * (n - 1) // 2 % (10 ** 9 + 7)
        if n == k + 1: return 1

        def C(i, j):
            return factorial(i) // (factorial(i - j) * factorial(j))

        ans = 0

        for i in range(k + 1, min(n, 2 * k) + 1):  # 遍历取点的数量，取k条线段，最少取k+1个点，最多取min(2*k,n)个点
            # 取点 有 C(n,i)种取法
            # i 个点 要连出 k 条线段，第一个点和最后一个点必须要取，剩余i-2个点->i-3个空隙
            # 还需要放k-2条线段，使得没有两个连续的空隙
            # 插空法：把空当元素，把元素当空，在k-2个元素的空(k-1个)中插入(i - 3) - (k - 2)个元素。
            ans += C(n, i) * C(k - 1, i - k - 1)

        return ans % (10 ** 9 + 7)
