# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-18 14:29
 @Author  : QDY
 @FileName: 5544. 执行操作后字典序最小的字符串.py
 @Software: PyCharm
"""
"""
给你一个字符串 s 以及两个整数 a 和 b 。其中，字符串 s 的长度为偶数，且仅由数字 0 到 9 组成。

你可以在 s 上按任意顺序多次执行下面两个操作之一：

累加：将 a 加到 s 中所有下标为奇数的元素上（下标从 0 开始）。数字一旦超过 9 就会变成 0，如此循环往复。
例如，s = "3456" 且 a = 5，则执行此操作后 s 变成 "3951"。

轮转：将 s 向右轮转 b 位。例如，s = "3456" 且 b = 1，则执行此操作后 s 变成 "6345"。
请你返回在 s 上执行上述操作任意次后可以得到的 字典序最小 的字符串。

如果两个字符串长度相同，那么字符串 a 字典序比字符串 b 小可以这样定义：
在 a 和 b 出现不同的第一个位置上，字符串 a 中的字符出现在字母表中的时间早于 b 中的对应字符。
例如，"0158” 字典序比 "0190" 小，因为不同的第一个位置是在第三个字符，显然 '5' 出现在 '9' 之前。


示例 1：
输入：s = "5525", a = 9, b = 2
输出："2050"
解释：执行操作如下：
初态："5525"
轮转："2555"
累加："2454"
累加："2353"
轮转："5323"
累加："5222"
累加："5121"
轮转："2151"
累加："2050"
无法获得字典序小于 "2050" 的字符串。

示例 2：
输入：s = "74", a = 5, b = 1
输出："24"
解释：执行操作如下：
初态："74"
轮转："47"
累加："42"
轮转："24"
无法获得字典序小于 "24" 的字符串。

示例 3：
输入：s = "0011", a = 4, b = 2
输出："0011"
解释：无法获得字典序小于 "0011" 的字符串。

示例 4：
输入：s = "43987654", a = 7, b = 3
输出："00553311"

提示：
2 <= s.length <= 100
s.length 是偶数
s 仅由数字 0 到 9 组成
1 <= a <= 9
1 <= b <= s.length - 1

"""
from collections import deque


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        res = s
        N = len(s)
        q = deque([s])
        visited = {s}
        while q:  # BFS 暴力
            cur = q.popleft()
            res = min(res, cur)
            n1 = list(cur)
            for i in range(1, N, 2):
                n1[i] = str((int(n1[i]) + a) % 10)
            n1 = ''.join(n1)
            if n1 not in visited:
                visited.add(n1)
                q.append(n1)
            n2 = cur[b:] + cur[:b]
            if n2 not in visited:
                visited.add(n2)
                q.append(n2)
        return res
