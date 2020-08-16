# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/16 16:44
 @Author  : QDY
 @FileName: 5489. 两球之间的磁力.py
 @Software: PyCharm
"""
"""
    在代号为 C-137 的地球上，Rick 发现如果他将两个球放在他新发明的篮子里，它们之间会形成特殊形式的磁力。
    Rick 有n个空的篮子，第i个篮子的位置在position[i]，
    Morty想把m个球放到这些篮子里，使得任意两球间最小磁力最大。
    已知两个球如果分别位于x和y，那么它们之间的磁力为|x - y|。
    给你一个整数数组position和一个整数m，请你返回最大化的最小磁力。

    示例 1：
    输入：position = [1,2,3,4,7], m = 3
    输出：3
    解释：将 3 个球分别放入位于 1，4 和 7 的三个篮子，两球间的磁力分别为 [3, 3, 6]。最小磁力为 3 。我们没办法让最小磁力大于 3 。

    示例 2：
    输入：position = [5,4,3,2,1,1000000000], m = 2
    输出：999999999
    解释：我们使用位于 1 和 1000000000 的篮子时最小磁力最大。
    
    提示：
    n == position.length
    2 <= n <= 10^5
    1 <= position[i] <= 10^9
    所有position中的整数 互不相同。
    2 <= m <= position.length

"""


class Solution:
    def maxDistance(self, position, m):
        position.sort()
        len_p = len(position)
        if m == 2: return position[-1] - position[0]
        if m == len_p:
            return min(position[j] - position[j - 1] for j in range(1, len_p))

        def check(min_val, balls):  # 判断以min_val为最小磁力是否可行
            prev = 0
            for i in range(1, len_p):
                if position[i] - position[prev] >= min_val:
                    balls -= 1
                    prev = i
                    if balls == 0:
                        break
            return balls == 0

        low, high = 1, position[-1] - position[0]
        while low < high:  # 二分搜索最小磁力
            mid = low + (high - low) // 2
            # print(low,high,mid,check(mid,m-1))
            if check(mid, m - 1):
                low = mid + 1
            else:
                high = mid

        return low - 1
