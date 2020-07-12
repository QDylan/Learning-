# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/12 10:07
 @Author  : QDY
 @FileName: 174. 地下城游戏_动态规划.py

    一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由 M x N 个房间组成的二维网格。
    我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。
    骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。
    有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；
    其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。
    为了尽快到达公主，骑士决定每次只向右或向下移动一步。

    编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。
    例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 右 -> 右 -> 下 -> 下，则骑士的初始健康点数至少为 7。

    -2 (K)	-3	3
    -5	-10	1
    10	30	-5 (P)


    说明:
    骑士的健康点数没有上限。
    任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。

"""


class Solution:
    def calculateMinimumHP(self, dungeon):
        hei, wid = len(dungeon), len(dungeon[0])
        # 动态规划
        # dp[i][j]=要进入dungeon[i][j]并到终点最少需要多少hp
        # 进入dungeon[i][j]能获得dungeon[i][j]点
        # 若往下走，则需要当前hp有dp[i+1][j]点
        #   若dungeon[i][j]-dp[i+1][j]<0,则进入dungeon[i][j]前还需要有-dungeon[i][j]+dp[i+1][j]点
        #   若dungeon[i][j]-dp[i+1][j]>=0，则进入dungeon[i][j]前只需有1点hp就可以
        # 若往右走，则需要当前hp有dp[i][j+1]点，同理
        # 取两个方向中需要最少的那一条路为dp[i][j]
        # down = 1 if dungeon[i][j]-dp[i+1][j]>=0 else -dungeon[i][j]+dp[i+1][j]
        # right = 1 if dungeon[i][j]-dp[i][j+1]>=0 else -dungeon[i][j]+dp[i][j+1]
        # dp[i][j] = min(down,right)
        dungeon[hei - 1][wid - 1] = 1 if dungeon[hei - 1][wid - 1] >= 0 else -dungeon[hei - 1][wid - 1] + 1
        for j in range(wid - 2, -1, -1):
            tmp = dungeon[hei - 1][j] - dungeon[hei - 1][j + 1]
            dungeon[hei - 1][j] = 1 if tmp >= 0 else -tmp
        for i in range(hei - 2, -1, -1):
            tmp = dungeon[i][wid - 1] - dungeon[i + 1][wid - 1]
            dungeon[i][wid - 1] = 1 if tmp >= 0 else -tmp
        for i in range(hei - 2, -1, -1):
            for j in range(wid - 2, -1, -1):
                tmp = max(dungeon[i][j] - dungeon[i][j + 1], dungeon[i][j] - dungeon[i + 1][j])
                dungeon[i][j] = 1 if tmp >= 0 else -tmp
        # print(dungeon)
        return dungeon[0][0]

        # self.res = float('inf')
        # def dfs(x,y,cur,min_hp):  # dfs超时
        #     cur += dungeon[x][y]
        #     min_hp = min(cur,min_hp)
        #     if x == hei-1 and y == wid-1:
        #         self.res = min(self.res,-min_hp+1)
        #         return
        #     if x < hei-1:
        #         dfs(x+1,y,cur,min_hp)
        #     if y < wid-1:
        #         dfs(x,y+1,cur,min_hp)
        # dfs(0,0,0,0)
        # return self.res
