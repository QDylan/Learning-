# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-27 15:24
 @Author  : QDY
 @FileName: 5526. 最多可达成的换楼请求数目.py
 @Software: PyCharm
"""
"""
我们有n栋楼，编号从0到n - 1。每栋楼有若干员工。由于现在是换楼的季节，部分员工想要换一栋楼居住。

给你一个数组 requests，其中requests[i] = [fromi, toi]，表示一个员工请求从编号为fromi的楼搬到编号为toi的楼。

一开始所有楼都是满的，所以从请求列表中选出的若干个请求是可行的需要满足 每栋楼员工净变化为 0。
意思是每栋楼 离开的员工数目 等于该楼 搬入的员工数数目。比方说n = 3且两个员工要离开楼0，一个员工要离开楼1，一个员工要离开楼 2，
如果该请求列表可行，应该要有两个员工搬入楼0，一个员工搬入楼1，一个员工搬入楼2。
请你从原请求列表中选出若干个请求，使得它们是一个可行的请求列表，并返回所有可行列表中最大请求数目。

示例 1：
输入：n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
输出：5
解释：请求列表如下：
从楼 0 离开的员工为 x 和 y ，且他们都想要搬到楼 1 。
从楼 1 离开的员工为 a 和 b ，且他们分别想要搬到楼 2 和 0 。
从楼 2 离开的员工为 z ，且他想要搬到楼 0 。
从楼 3 离开的员工为 c ，且他想要搬到楼 4 。
没有员工从楼 4 离开。
我们可以让 x 和 b 交换他们的楼，以满足他们的请求。
我们可以让 y，a 和 z 三人在三栋楼间交换位置，满足他们的要求。
所以最多可以满足 5 个请求。

示例 2：
输入：n = 3, requests = [[0,0],[1,2],[2,1]]
输出：3
解释：请求列表如下：
从楼 0 离开的员工为 x ，且他想要回到原来的楼 0 。
从楼 1 离开的员工为 y ，且他想要搬到楼 2 。
从楼 2 离开的员工为 z ，且他想要搬到楼 1 。
我们可以满足所有的请求。

示例 3：
输入：n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]
输出：4

提示：
1 <= n <= 20
1 <= requests.length <= 16
requests[i].length == 2
0 <= fromi, toi < n

"""
from itertools import combinations
from collections import defaultdict, Counter


class Solution:
    def maximumRequests(self, n, req):
        res = 0
        In, Out = defaultdict(Counter), defaultdict(Counter)  # 按入度和出度剪枝
        for L, R in req:
            if L != R:
                Out[L][R] += 1
                In[R][L] += 1
            else:
                res += 1  # 原地换的直接+1

        remove = [i for i in range(n) if not In[i] or not Out[i]]  # 删除没有入度或者没有出度的点
        for i in remove:
            for L in In[i]:
                Out[L][i] -= 1
                if not Out[L][i]: Out[L].pop(i)
                if not Out[L]: remove.append(L)
            for R in Out[i]:
                In[R][i] -= 1
                if not In[R][i]: In[R].pop(i)
                if not In[R]: remove.append(R)
            In.pop(i)
            Out.pop(i)
        req = sum(([(L, R)] * Out[L][R] for L in Out for R in Out[L]), [])  # 将剩余的请求重新组合
        for k in range(len(req), 0, -1):
            for c in combinations(req, k):  # 选取k个请求组合
                degree = [0] * n
                for L, R in c:
                    degree[L] -= 1
                    degree[R] += 1
                if not any(degree):  # 每个位置的净变化量都为0，表明这种选择可行
                    return k + res
        return res
