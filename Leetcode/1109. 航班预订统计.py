# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-24 14:29
 @Author  : QDY
 @FileName: 1109. 航班预订统计.py
 @Software: PyCharm
"""
"""
这里有n个航班，它们分别从 1 到 n 进行编号。
我们这儿有一份航班预订表，表中第i条预订记录bookings[i] = [i, j, k]意味着我们在从i到j的每个航班上预订了 k 个座位。
请你返回一个长度为 n 的数组answer，按航班编号顺序返回每个航班上预订的座位数。

示例：
输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
输出：[10,55,45,25,25]

提示：
1 <= bookings.length <= 20000
1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000
1 <= bookings[i][2] <= 10000

"""


class Solution:
    def corpFlightBookings(self, bookings, n: int):
        res = [0] * (n + 1)
        for start, end, k in bookings:  # 构造差分数组
            res[start - 1] += k
            res[end] -= k
        for i in range(1, n):
            res[i] += res[i - 1]
        return res[:n]
