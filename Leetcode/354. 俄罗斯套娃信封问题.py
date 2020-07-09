# -*- coding: utf-8 -*-
"""
 @Time    : 2020-07-09 15:24
 @Author  : QDY
 @FileName: 354. 俄罗斯套娃信封问题.py

    给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。
    当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

    请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

    说明:
    不允许旋转信封。

    示例:

    输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
    输出: 3
    解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

"""


class Solution:
    def maxEnvelopes(self, envelopes):
        if not envelopes: return 0
        envelopes.sort(key=lambda x: [x[0], -x[1]])  # w按升序排序，w相同部分按h降序排序
        # 找到在h维度上的最大上升子序列
        dp = [envelopes[0][1]]
        res = 1
        for i in envelopes:
            l, r = 0, res - 1
            while l <= r:
                m = l + (r - l) // 2
                if dp[m] < i[1]:
                    l = m + 1
                else:
                    r = m - 1
            if l == res:
                dp.append(i[1])
                res += 1
            else:
                dp[l] = i[1]
        return res
