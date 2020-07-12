# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/12 19:17
 @Author  : QDY
 @FileName: 5463. 服务中心的最佳位置.py

    一家快递公司希望在新城市建立新的服务中心。公司统计了该城市所有客户在二维地图上的坐标，
    并希望能够以此为依据为新的服务中心选址：使服务中心 到所有客户的欧几里得距离的总和最小 。
    给你一个数组 positions ，其中 positions[i] = [xi, yi] 表示第 i 个客户在二维地图上的位置，
    返回到所有客户的 欧几里得距离的最小总和 。
    与真实值误差在 10^-5 之内的答案将被视作正确答案。

    示例1：
    输入：positions = [[0,1],[1,0],[1,2],[2,1]]
    输出：4.00000
    解释：如图所示，你可以选 [xcentre, ycentre] = [1, 1] 作为新中心的位置，
    这样一来到每个客户的距离就都是 1，所有距离之和为 4 ，这也是可以找到的最小值。

    示例2：
    输入：positions = [[1,1],[3,3]]
    输出：2.82843
    解释：欧几里得距离可能的最小总和为 sqrt(2) + sqrt(2) = 2.82843

    示例 3：
    输入：positions = [[1,1]]
    输出：0.00000

    示例 4：
    输入：positions = [[1,1],[0,0],[2,0]]
    输出：2.73205
    解释：乍一看，你可能会将中心定在 [1, 0] 并期待能够得到最小总和，但是如果选址在 [1, 0] 距离总和为 3
    如果将位置选在 [1.0, 0.5773502711] ，距离总和将会变为 2.73205
    当心精度问题！

    示例 5：
    输入：positions = [[0,1],[3,2],[4,5],[7,6],[8,9],[11,1],[2,12]]
    输出：32.94036
    解释：你可以用 [4.3460852395, 4.9813795505] 作为新中心的位置

"""


class Solution:
    def getMinDistSum(self, positions):
        n = len(positions)

        def f(x,y):  # 目标函数
            return sum(((x - xi) ** 2 + (y - yi) ** 2) ** 0.5 for xi, yi in positions)

        sum_x, sum_y = 0, 0
        for i in positions:
            sum_x += i[0]
            sum_y += i[1]
        x0,y0 = sum_x/n,sum_y/n  # 初始点

        # 模拟退火
        # d = [[1,0],[-1,0],[0,1],[0,-1]]
        # pace,eps,t = 1, 10**-8,0.98
        # prev = f(x0,y0)
        # while pace>eps:
        #     mark = 1
        #     while mark:
        #         mark = 0
        #         for i in range(4):
        #             x1 = x0 + d[i][0]*pace
        #             y1 = y0 + d[i][1]*pace
        #             cur = f(x1,y1)
        #             if cur<prev:
        #                 flag = 1
        #                 x0,y0,prev = x1,y1,cur
        #     pace *= t
        # return cur

        def d_f(x,y):  # 对目标函数求梯度
            dx, dy = 0, 0
            for xi,yi in positions:
                tmp = ((x-xi)**2+(y-yi)**2)**0.5
                if tmp == 0:
                    continue
                dx += (x-xi)/tmp
                dy += (y-yi)/tmp
            return dx,dy

        pace = 1
        prev = f(x0,y0)
        dx,dy = d_f(x0,y0)
        x1, y1 = x0-dx, y0-dy
        cur = f(x1,y1)
        while abs(cur-prev) > 10 ** -7:
            if cur>prev:  # 若距离增加了，回溯并减少步长
                pace /= 5
                x1, y1, cur = x0, y0, prev
            dx,dy = d_f(x1,y1)
            x0, y0, prev = x1, y1, cur
            x1 -= dx*pace
            y1 -= dy*pace
            cur = f(x1,y1)
            # print(cur)

        return cur

        # if n<=1:return 0
        # if n==2:return (((positions[0][0]-positions[1][0])**2+(positions[0][1]-positions[1][1])**2)**0.5)/2
        # res = float('inf')
        # for i in range(n-2):
        #     x1,y1 = positions[i]
        #     for j in range(i+1,n-1):
        #         x2,y2 = positions[j]
        #         for k in range(j+1,n):
        #             x3,y3 = positions[k]
        #             tmp = (x3-x1)*(y2-y1)-(x2-x1)*(y3-y1)
        #             if tmp == 0:
        #                 continue
        #             x = 0.5*((y2-y1)*(y3**2-y1**2+x3**2-x2**2)-(y3-y1)*(y2**2-y1**2+x2**2-x1**2))/tmp
        #             y = 0.5*((x2-x1)*(x3**2-x1**2+y3**2-y1**2)-(x3-x1)*(x2**2-x1**2+y2**2-y1**2))/(-tmp)
        #             res = min(res,sum(((x - xi) ** 2 + (y - yi) ** 2) ** 0.5 for xi, yi in positions))
        # return res