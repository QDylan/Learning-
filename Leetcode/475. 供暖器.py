# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-15 10:57
 @Author  : QDY
 @FileName: 475. 供暖器.py
 @Software: PyCharm
"""
"""
冬季已经来临。你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。

在加热器的加热半径范围内的每个房屋都可以获得供暖。

现在，给出位于一条水平线上的房屋houses 和供暖器heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。
说明：所有供暖器都遵循你的半径标准，加热的半径也一样。

示例 1:
输入: houses = [1,2,3], heaters = [2]
输出: 1
解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。

示例 2:
输入: houses = [1,2,3,4], heaters = [1,4]
输出: 1
解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。

示例 3：
输入：houses = [1,5], heaters = [2]
输出：3

提示：
1 <= houses.length, heaters.length <= 3 * 104
1 <= houses[i], heaters[i] <= 109

"""


class Solution:
    def findRadius(self, houses, heaters) -> int:
        houses.sort()
        heaters.sort()
        H = len(heaters)
        res, cur = 0, 0
        for i in houses:  # 对于每个房屋，要么用前面的暖气，要么用后面的，取距离近的
            while cur + 1 < H and abs(i - heaters[cur]) >= abs(i - heaters[cur + 1]):  # >= 可以跳过重复的heater
                cur += 1
            res = max(res, abs(i - heaters[cur]))
        return res
