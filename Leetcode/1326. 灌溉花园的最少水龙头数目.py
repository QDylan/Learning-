# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/22 15:10
 @Author  : QDY
 @FileName: 1326. 灌溉花园的最少水龙头数目.py
 @Software: PyCharm
"""
"""
    在 x 轴上有一个一维的花园。花园长度为n，从点0开始，到点n结束。
    花园里总共有n + 1 个水龙头，分别位于[0, 1, ..., n] 。
    给你一个整数n和一个长度为n + 1 的整数数组ranges，其
    中ranges[i] （下标从 0 开始）表示：如果打开点i处的水龙头，可以灌溉的区域为[i - ranges[i], i + ranges[i]]。
    请你返回可以灌溉整个花园的最少水龙头数目。如果花园始终存在无法灌溉到的地方，请你返回-1。
    
    示例 1：
    输入：n = 5, ranges = [3,4,1,1,0,0]
    输出：1
    解释：
    点 0 处的水龙头可以灌溉区间 [-3,3]
    点 1 处的水龙头可以灌溉区间 [-3,5]
    点 2 处的水龙头可以灌溉区间 [1,3]
    点 3 处的水龙头可以灌溉区间 [2,4]
    点 4 处的水龙头可以灌溉区间 [4,4]
    点 5 处的水龙头可以灌溉区间 [5,5]
    只需要打开点 1 处的水龙头即可灌溉整个花园 [0,5] 。
    
    示例 2：
    输入：n = 3, ranges = [0,0,0,0]
    输出：-1
    解释：即使打开所有水龙头，你也无法灌溉整个花园。
    
    示例 3：
    输入：n = 7, ranges = [1,2,1,0,2,1,0,1]
    输出：3
    
    示例 4：
    输入：n = 8, ranges = [4,0,0,0,0,0,0,0,4]
    输出：2
    
    示例 5：
    输入：n = 8, ranges = [4,0,0,0,4,0,0,0,4]
    输出：1
    
    提示：
    1 <= n <= 10^4
    ranges.length == n + 1
    0 <= ranges[i] <= 100

"""


class Solution:
    def minTaps(self, n, ranges) -> int:
        prev = [x for x in range(n + 1)]
        for i in range(n + 1):
            l = max(i - ranges[i], 0)
            r = min(i + ranges[i], n)
            prev[r] = min(prev[r], l)

        breakpoint, furthest = n, float('inf')
        ans = 0
        for i in range(n, 0, -1):
            furthest = min(furthest, prev[i])
            if i == breakpoint:
                if furthest >= i:
                    return -1
                breakpoint = furthest
                ans += 1

        return ans

        # for i in range(len(ranges)):
        #     ranges[i] = [i-ranges[i],i+ranges[i]]
        # ranges.sort(key=lambda x:(x[0],x[0]-x[1]))
        # # print(ranges)
        # res,valid = 0, True
        # l,r = ranges[0][0],ranges[0][1]
        # if l>0:return -1
        # prev = [(l,r)]
        # for l,r in ranges[1:]:
        #     if prev[-1][1]>=n:break
        #     if l>prev[-1][1]:
        #         valid = False
        #         break
        #     elif l==prev[-1][1]:
        #         res += len(prev)
        #         prev = [(l,r)]
        #     else:
        #         if r<=prev[-1][1]:
        #             continue
        #         elif l<=0:
        #             prev = [(l,r)]
        #             continue
        #         else:
        #             if len(prev)>1 and prev[-2][1]>=l:
        #                 prev.pop()
        #         prev.append((l,r))
        #     # print(prev)
        # if prev:
        #     if prev[-1][1]<n:return -1
        #     res += len(prev)
        # return res if valid else -1
