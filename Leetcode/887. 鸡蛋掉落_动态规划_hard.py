# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/19 21:42
 @Author  : QDY
 @FileName: 887. 鸡蛋掉落_动态规划_hard.py

    你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。
    每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。
    你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。
    每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。
    你的目标是确切地知道 F 的值是多少。
    无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？

    示例 1：
    输入：K = 1, N = 2
    输出：2
    解释：
    鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
    否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
    如果它没碎，那么我们肯定知道 F = 2 。
    因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。

    示例 2：
    输入：K = 2, N = 6
    输出：3

    示例 3：
    输入：K = 3, N = 14
    输出：4
     

    提示：
    1 <= K <= 100
    1 <= N <= 10000

"""


class Solution:
    def superEggDrop(self, K, N):
        if not K or not N: return 0
        if K == 1: return N
        # # 动态规划  (快速)
        # # 1. dp[m][k] 表示k个蛋扔m次能 保证 确定的楼层数的最大值
        # # 对于k个蛋扔m+1次的情况 dp[m+1][k]，
        # # 在第一次扔蛋中，任选一个楼层x
        # # 1.若蛋碎了，则相当于少一个蛋，需要在1~x-1层楼中用k-1个蛋扔m次
        # # x-1的最大值=dp[m][k-1]
        # # 2.若蛋没碎，则只少了一次扔蛋机会，dp[m+1][k]= x + dp[m][k]
        # # 所以 dp[m+1][k] = dp[m][k-1] + dp[m][k] + 1

        # dp = [0]+[1]*K  # m=1时,dp[k]=1,k>0
        # m = 1
        # while dp[K] < N:
        #     for k in range(K,0,-1):
        #         dp[k] += dp[k-1] + 1
        #     m += 1
        # return m

        # 2. dp(k,n) 表示k个蛋在n层楼扔需要多少次

        memory = {}  # 记忆已计算出的dp(k,n)

        def dp(k, n):
            # nonlocal visited
            if k == 1: return n
            if not n: return 0

            if (k, n) in memory:
                return memory[(k, n)]
            res = float('inf')
            # 线性搜索，超时
            # for i in range(1,n+1):
            #     # 第一次扔在第i层,
            #     # 若碎了，后续只需在1~i-1层内扔k-1个蛋，则 dp(k,n)=dp(k-1,i-1)+1
            #     # 若没碎，后续只需在第i+1~n(n-i层)内扔k个蛋，则dp(k,n)=dp(k,n-i)+1
            #     # 取这两种情况的最大值 为k个蛋在n层楼扔(第一次扔在i层时)的次数
            #     res = min(res,max(dp(k,n-i),dp(k-1,i-1))+1)

            # 二分搜索
            # dp(k-1,i-1)关于i单调递增，dp(k,n-i)关于i单调递减
            # max(dp(k,n-i),dp(k-1,i-1)) 是一条V型的折线
            #  dp(k-1,i-1)与dp(k,n-i)的交点就是min(max(dp(k,n-i),dp(k-1,i-1)))
            low, high = 1, n
            while low <= high:
                mid = low + (high - low) // 2  # 第一次扔在mid层
                broken = dp(k - 1, mid - 1) + 1  # 在mid层碎了
                not_broken = dp(k, n - mid) + 1  # 没碎
                if broken == not_broken:  # 直接找到能当前的最优解
                    memory[(k, n)] = broken
                    return broken
                elif broken > not_broken:  # 若在mid层碎了后，需要的搜索次数更多
                    high = mid - 1  # 则降低最高层数high, 接下来在low~mid-1中搜索
                    res = min(res, broken)
                else:  # 若在mid层没碎后，需要的搜索次数更多
                    low = mid + 1  # 则增加最低层数low, 接下来在mid+1~high中搜索
                    res = min(res, not_broken)

            memory[(k, n)] = res
            return res

        return dp(K, N)
