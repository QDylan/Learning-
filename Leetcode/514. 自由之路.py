# -*- coding: utf-8 -*-
"""
 @Time    : 2020-11-13 10:44
 @Author  : QDY
 @FileName: 514. 自由之路.py
 @Software: PyCharm
"""
"""
电子游戏“辐射4”中，任务“通向自由”要求玩家到达名为“Freedom Trail Ring”的金属表盘，并使用表盘拼写特定关键词才能开门。

给定一个字符串ring，表示刻在外环上的编码；给定另一个字符串key，表示需要拼写的关键词。您需要算出能够拼写关键词中所有字符的最少步数。

最初，ring的第一个字符与12:00方向对齐。
您需要顺时针或逆时针旋转 ring 以使key的一个字符在 12:00 方向对齐，然后按下中心按钮，以此逐个拼写完key中的所有字符。

旋转ring拼出 key 字符key[i]的阶段中：

您可以将ring顺时针或逆时针旋转一个位置，计为1步。旋转的最终目的是将字符串ring的一个字符与 12:00 方向对齐，并且这个字符必须等于字符key[i] 。
如果字符key[i]已经对齐到12:00方向，您需要按下中心按钮进行拼写，这也将算作1 步。按完之后，您可以开始拼写key的下一个字符（下一阶段）, 直至完成所有拼写。
示例：
输入: ring = "godding", key = "gd"
输出: 4
解释:
 对于 key 的第一个字符 'g'，已经在正确的位置, 我们只需要1步来拼写这个字符。 
 对于 key 的第二个字符 'd'，我们需要逆时针旋转 ring "godding" 2步使它变成 "ddinggo"。
 当然, 我们还需要1步进行拼写。
 因此最终的输出是 4。
提示：

ring 和key的字符串长度取值范围均为1 至100；
两个字符串中都只有小写字符，并且均可能存在重复字符；
字符串key一定可以由字符串 ring旋转拼出。

"""
from collections import defaultdict
from functools import lru_cache


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        size = len(ring)
        pre = [0] * size
        mx = [[] for _ in range(26)];
        a = ord('a')
        for i in range(size):
            mx[ord(ring[i]) - a].append(i)
        for ix in mx[ord(key[0]) - a]:
            t = ix;
            tt = size - ix
            if t <= tt:
                pre[ix] = t
            else:
                pre[ix] = tt
        for i in range(1, len(key)):
            now = [float('inf')] * size
            k = ord(key[i]) - a
            prek = ord(key[i - 1]) - a
            for ix in mx[k]:
                for px in mx[prek]:
                    if ix >= px:
                        t = ix - px + pre[px]
                        tt = size - ix + px + pre[px]
                    else:
                        t = px - ix + pre[px]
                        tt = size - px + ix + pre[px]
                    if t < now[ix]:
                        now[ix] = t
                    if tt < now[ix]:
                        now[ix] = tt
            pre = now
        k = ord(key[-1]) - a
        res = pre[0]
        for ix in mx[k]:
            if pre[ix] < res:
                res = pre[ix]
        return res + len(key)

        # N,K = len(ring),len(key)
        # mat = [defaultdict(list) for _ in range(N)]
        # for i in range(N):
        #     mat[i][ring[i]].append((1,i))
        #     for j in range(i+1,N):
        #         dis = min(j-i,i+N-j)+1
        #         mat[i][ring[j]].append((dis,j))
        #         mat[j][ring[i]].append((dis,i))

        # @lru_cache(None)
        # def dfs(cur,index):
        #     if index==K:return 0
        #     res = float('inf')
        #     c = key[index]
        #     for dis,nxt in mat[cur][c]:
        #         res = min(res,dis+dfs(nxt,index+1))
        #     return res

        # return dfs(0,0)