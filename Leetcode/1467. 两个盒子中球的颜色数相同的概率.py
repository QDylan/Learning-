# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/2 9:56
 @Author  : QDY
 @FileName: 1467. 两个盒子中球的颜色数相同的概率.py

桌面上有 2n 个颜色不完全相同的球，球上的颜色共有 k 种。给你一个大小为 k 的整数数组 balls ，
其中 balls[i] 是颜色为 i 的球的数量。
所有的球都已经 随机打乱顺序 ，前 n 个球放入第一个盒子，后 n 个球放入另一个盒子（请认真阅读示例 2 的解释部分）。
注意：这两个盒子是不同的。例如，两个球颜色分别为 a 和 b，
盒子分别为 [] 和 ()，那么 [a] (b) 和 [b] (a) 这两种分配方式是不同的（请认真阅读示例 1 的解释部分）。
请计算「两个盒子中球的颜色数相同」的情况的概率。

示例 1：
输入：balls = [1,1]
输出：1.00000
解释：球平均分配的方式只有两种：
- 颜色为 1 的球放入第一个盒子，颜色为 2 的球放入第二个盒子
- 颜色为 2 的球放入第一个盒子，颜色为 1 的球放入第二个盒子
这两种分配，两个盒子中球的颜色数都相同。所以概率为 2/2 = 1 。

示例 2：
输入：balls = [2,1,1]
输出：0.66667
解释：球的列表为 [1, 1, 2, 3]
随机打乱，得到 12 种等概率的不同打乱方案，每种方案概率为 1/12 ：
[1,1 / 2,3], [1,1 / 3,2], [1,2 / 1,3], [1,2 / 3,1], [1,3 / 1,2],
[1,3 / 2,1], [2,1 / 1,3], [2,1 / 3,1], [2,3 / 1,1], [3,1 / 1,2], [3,1 / 2,1], [3,2 / 1,1]
然后，我们将前两个球放入第一个盒子，后两个球放入第二个盒子。
这 12 种可能的随机打乱方式中的 8 种满足「两个盒子中球的颜色数相同」。
概率 = 8/12 = 0.66667

示例 3：
输入：balls = [1,2,1,2]
输出：0.60000
解释：球的列表为 [1, 2, 2, 3, 4, 4]。要想显示所有 180 种随机打乱方案是很难的，
但只检查「两个盒子中球的颜色数相同」的 108 种情况是比较容易的。
概率 = 108 / 180 = 0.6 。
示例 4：

输入：balls = [3,2,1]
输出：0.30000
解释：球的列表为 [1, 1, 1, 2, 2, 3]。要想显示所有 60 种随机打乱方案是很难的，
但只检查「两个盒子中球的颜色数相同」的 18 种情况是比较容易的。
概率 = 18 / 60 = 0.3 。

示例 5：
输入：balls = [6,6,6,6,6,6]
输出：0.90327

提示：
1 <= balls.length <= 8
1 <= balls[i] <= 6
sum(balls) 是偶数
答案与真实值误差在 10^-5 以内，则被视为正确答案

"""

import math, itertools
# math.factorial 阶乘
# math.prod 连乘
# itertools.product 对生成器做笛卡尔积

class Solution:
    def multinomial(self, n):  # 计算n=[n0,n1,n2,...]所有可能的组合序列个数
        return math.factorial(sum(n)) / math.prod([math.factorial(i) for i in n])

    def getProbability(self, balls):
        n, Q = sum(balls) // 2, 0  # n表示每个盒子里要取多少个球，Q为满足要求的样本数
        arrays = [range(0, i + 1) for i in balls]  # arrays[i]为range 表示第i种球可以取的数量
        t = list(itertools.product(*arrays))  # 笛卡尔积求出所有的组合
        # 若balls=[1,2,3]，则len(t)=2*3*4=24，每种组合表示盒子一的球颜色的分布情况
        i = 0
        for i in range(len(t) // 2):  # 剪枝，少计算一半
            # 要求：1.球数和=n 2.通过计算缺了多少种颜色来确定颜色数是否与第二个盒子相同
            if sum(t[i]) == n and t[i].count(0) == t[-i - 1].count(0):  # t[-1-i]为对应的第二个盒子
                Q += self.multinomial(t[i]) * self.multinomial(t[-i - 1]) * 2

        if len(t) % 2 == 1:  # 对于每种颜色的球的数量都是偶数的情况，存在一种两个盒子的球的分布完全相同的情况
            Q += self.multinomial(t[i + 1]) * self.multinomial(t[-i - 2])

        return Q / self.multinomial(list(balls))

        #     # c1 是第一个箱子中的颜色数量，c2 是第二个箱子中的颜色数量
    #     c1, c2 = 0, 0
    #     # 所有的满足条件的取球的方式数量
    #     self.res = 0
    #     # 所有的取球的方式数量
    #     self.total = 0
    #     self.balls = balls
    #     self.target_count = sum(balls) // 2
    #     # 题目说明了每种颜色的球数量最大为 6，因此计算 0~6 的阶乘，后面直接查
    #     self.fact = [1] * 7
    #     for i in range(1, 7):
    #         self.fact[i] = self.fact[i-1]*i
    #     self.dfs(1, 0, 0, c1, c2)
    #     return self.res / self.total

    # # choices: 到达这一层的状态时，所有可能的方式数量
    # # counts: 已经取出来的球的数量
    # # ball_idx：这一层要从哪种颜色里面取
    # # c1: 第一个箱子中的颜色数量
    # # c2: 第二个箱子中的颜色数量
    # def dfs(self, choices, counts, ball_idx, c1, c2):
    #     # 如果取的球太多了，直接返回
    #     if counts > self.target_count:
    #         return
    #     # 如果取完了所有的颜色，判断两个箱子中的颜色数量是否相同
    #     if ball_idx == len(self.balls):
    #         if counts != self.target_count:
    #             return
    #         self.total += choices
    #         if c1 == c2:
    #             self.res += choices
    #         return
    #     # 这种颜色一共有多少球
    #     this_ball_num = self.balls[ball_idx]
    #     # 取出 i 个球放在第一个箱子，其余的放入第二个箱子
    #     for i in range(this_ball_num+1):
    #         c11 = c1+1 if i > 0 else c1
    #         c22 = c2+1 if i < this_ball_num else c2
    #         this_choice = self.fact[this_ball_num] / self.fact[i] / self.fact[this_ball_num-i]
    #         self.dfs(choices * this_choice, counts+i, ball_idx+1, c11, c22)
