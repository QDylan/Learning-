# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/19 10:09
 @Author  : QDY
 @FileName: 322. 零钱兑换_动态规划_BFS_DFS_完全背包问题.py

    给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

    示例 1:
    输入: coins = [1, 2, 5], amount = 11
    输出: 3
    解释: 11 = 5 + 5 + 1

    示例 2:
    输入: coins = [2], amount = 3
    输出: -1
     
    说明:
    你可以认为每种硬币的数量是无限的。

"""


class Solution:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        # 完全背包问题

        # # 1.动态规划
        # # dp[i] = 组合成金额i需要的最少硬币数
        # # dp[i+1] = min(dp[i-coins[0]],dp[i-coins[1]],...dp[i-coins[-1]]) + 1
        # dp = [0]+[float('inf')]*amount
        # for i in range(1,amount+1):
        #     for c in coins:
        #         if i-c >= 0:
        #             dp[i] = min(dp[i],dp[i-c])
        #     dp[i] += 1
        # return -1 if dp[-1]==float('inf') else dp[-1]

        # 2.DFS  (最快)
        # 若要达成硬币数最小的目标，则要尽可能取金额大的硬币
        res = float('inf')  # 需要的硬币数
        coins.sort(reverse=True)  # 将硬币按金额大小降序排序
        length = len(coins)

        def dfs(num, cur_amount, i_):
            nonlocal res
            # num = 已使用的硬币数
            # cur_amount = 当前的剩余金额
            # i = 只能使用id在i之后和coins补充剩余金额
            if cur_amount == 0:  # 剩余金额恰好为0，则找到了一种组合方案
                res = min(res, num)
            for j in range(i_, length):
                # 若res-num个coins[j]无法补充剩余金额，则其之后的硬币也不用再尝试了
                if coins[j] * (res - num) < cur_amount:  # 因为其一定无法实现少于res个硬币组合出amount
                    break  # 一种剪枝手段
                if coins[j] > cur_amount:  # 当前硬币额度超过了剩余金额，跳到下一个金额小一点的硬币
                    continue
                dfs(num + 1, cur_amount - coins[j], j)  # 递归，尽可能地先使用金额较大的硬币填满amount

        for i in range(length):  # 在搜索过程中，不会再使用i之前的硬币
            dfs(0, amount, i)
            if res != float('inf'):  # 若res发生了变化，则一定是找到了最优解
                return res  # 因为是优先使用金额较大的硬币搜索的
        return -1

        # # 3.BFS
        # # 从amount开始，每次分别减去一种硬币，将能得到的金额存放在队列queue中
        # # count记录当前queue是减去多少枚硬币后的剩余金额队列
        # # visited为记录剩余金额的集合，若新的cur_amount已存在于visited，则不会将其加入队列
        # # 因为前面存在只需要更少硬币数就能达成这一金额的组合方案
        # # 当queue中有一个为0时，输出count为最小组合数
        # queue = [amount]
        # visited = set()
        # count = 0
        # while queue:
        #     length = len(queue)
        #     for i in range(length):
        #         tmp = queue.pop(0)
        #         for c in coins:
        #             if tmp==c:  # 找到最优组合方案，退出
        #                 return count+1
        #             if tmp>c and tmp-c not in visited:  # 当前硬币额度大于剩余金额的话也无法组合，不添加进队列
        #                 visited.add(tmp-c)
        #                 queue.append(tmp-c)
        #     count += 1
        # return -1
