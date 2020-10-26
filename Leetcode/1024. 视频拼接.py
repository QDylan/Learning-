# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-26 14:47
 @Author  : QDY
 @FileName: 1024. 视频拼接.py
 @Software: PyCharm
"""
"""
你将会获得一系列视频片段，这些片段来自于一项持续时长为T秒的体育赛事。这些片段可能有所重叠，也可能长度不一。

视频片段clips[i]都用区间进行表示：开始于clips[i][0]并于clips[i][1]结束。
我们甚至可以对这些片段自由地再剪辑，例如片段[0, 7]可以剪切成[0, 1] +[1, 3] + [3, 7]三部分。

我们需要将这些片段进行再剪辑，并将剪辑后的内容拼接成覆盖整个运动过程的片段（[0, T]）。
返回所需片段的最小数目，如果无法完成该任务，则返回 -1 。

示例 1：
输入：clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
输出：3
解释：
我们选中 [0,2], [8,10], [1,9] 这三个片段。
然后，按下面的方案重制比赛片段：
将 [1,9] 再剪辑为 [1,2] + [2,8] + [8,9] 。
现在我们手上有 [0,2] + [2,8] + [8,10]，而这些涵盖了整场比赛 [0, 10]。

示例 2：
输入：clips = [[0,1],[1,2]], T = 5
输出：-1
解释：
我们无法只用 [0,1] 和 [1,2] 覆盖 [0,5] 的整个过程。

示例 3：
输入：clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9
输出：3
解释： 
我们选取片段 [0,4], [4,7] 和 [6,9] 。

示例 4：
输入：clips = [[0,4],[2,8]], T = 5
输出：2
解释：
注意，你可能录制超过比赛结束时间的视频。

提示：
1 <= clips.length <= 100
0 <= clips[i][0] <=clips[i][1] <= 100
0 <= T <= 100

"""


class Solution:
    def videoStitching(self, clips, T: int) -> int:
        if not clips: return -1
        # buckets = [-1]*(T+1)
        # for l,r in clips:  # 桶排序
        #     if l<=T and buckets[l]<r:
        #         buckets[l] = r
        # if buckets[0]<0:return -1
        # if buckets[0]>=T:return 1
        # clips = []
        # for i in range(T+1):
        #     if buckets[i]>0:clips.append([i,buckets[i]])
        clips.sort(key=lambda x: (x[0], -x[1]))  # 按左端点升序排列，(左端点相同的按右端点降序)
        if clips[0][0] > 0: return -1
        if clips[0][1] >= T: return 1
        res, max_r, prev_r = 1, clips[0][1], 0  # max_r记录最右边界，prev_r记录倒数第二个已选区间的右边界
        for i in range(1, len(clips)):
            l, r = clips[i]
            if l == clips[i - 1][0]: continue  # 剪枝
            if l > max_r: break  # 出现空缺
            if r > max_r:
                if l > prev_r:  # 若 l <= prev_r 则上一个已选的区间可以去掉
                    res += 1  # 新增一个区间
                    prev_r = max_r  #
                max_r = r
                if max_r >= T: return res
        return -1
        # if not clips: return -1
        # clips.sort(key=lambda x: (x[0], -x[1]))  # 按左端点升序排列，(左端点相同的按右端点降序)
        # if clips[0][0] > 0: return -1  # 起点大于 0
        # if clips[0][1] >= T: return 1  # 第一个区间就满足
        # res, max_r, prev_r = 1, clips[0][1], clips[0][1]  # 记录最大的右边界，res中最后一个区间的右边界
        # for l, r in clips[1:]:
        #     if prev_r >= l:
        #         max_r = max(max_r, r)
        #         if max_r >= T: return res + 1
        #     else:  # prev_r < l 说明以prev_r结尾会出现空缺，需要加上一个右边界为max_r的区间
        #         res += 1
        #         prev_r = max_r
        #         if max_r >= T: return res
        #     # print(prev_r,max_r)
        #
        # return -1
