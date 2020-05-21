# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/21 16:33
 @Author  : QDY
 @FileName: 452. 用最少数量的箭引爆气球_贪心算法.py

    在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以y坐标并不重要，
    因此只要知道开始和结束的x坐标就足够了。开始坐标总是小于结束坐标。平面内最多存在104个气球。

    一支弓箭可以沿着x轴从不同点完全垂直地射出。在坐标x处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend，
    且满足  xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。
    我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。

    Example:
    输入:
    [[10,16], [2,8], [1,6], [7,12]]
    输出:
    2

    解释:
    对于该样例，我们可以在x = 6（射爆[2,8],[1,6]两个气球）和 x = 11（射爆另外两个气球）。

"""


class Solution:
    def findMinArrowShots(self, points):
        if not points: return 0
        # 本质是区间调度问题，若区间有重叠,则只用一支箭
        points.sort(key=lambda x: x[0])
        # print(points)

        # tmp = points[0]
        # res = 1
        # for i in range(1, len(points)):
        #     if points[i][0] <= tmp[1]:  # 有重叠时，不用增加箭，更新tmp为这两个区间重叠的部分
        #         # 若之后的区间也有与tmp重叠的部分，则也不用更新箭
        #         tmp = [max(points[i][0], tmp[0]), min(points[i][1], tmp[1])]
        #     else:
        #         tmp = points[i]
        #         res += 1
        # return res

        # 贪心
        res = 1
        prev = points[0][1]
        for cur in range(1,len(points)):
            if points[cur][0] <= prev: # 删除右边界最大的区间
                prev = min(prev, points[cur][1])  # 更新有边界
            else:
                res += 1
                prev = points[cur][1]

        return res
