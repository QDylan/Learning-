# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-27 10:23
 @Author  : QDY
 @FileName: 433. 最小基因变化.py
 @Software: PyCharm
"""
"""
一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。
假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。
例如，基因序列由"AACCGGTT"变化至"AACCGGTA"即发生了一次基因变化。
与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。
现在给定3个参数 — start, end, bank，分别代表起始基因序列，目标基因序列及基因库，
请找出能够使起始基因序列变化为目标基因序列所需的最少变化次数。如果无法实现目标变化，请返回 -1。

注意:
起始基因序列默认是合法的，但是它并不一定会出现在基因库中。
所有的目标基因序列必须是合法的。
假定起始基因序列与目标基因序列是不一样的。

示例 1:
start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]
返回值: 1

示例 2:
start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
返回值: 2

示例 3:
start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
返回值: 3

"""


class Solution:
    def minMutation(self, start: str, end: str, bank) -> int:
        length = len(start)
        bank = set(bank)
        if start == end: return 0
        if length != len(end) or end not in bank: return -1
        char, dis = {'A', 'C', 'G', 'T'}, 0
        front = {start}
        back = {end}
        while front and back:
            dis += 1
            nxt_front = set()
            for g in front:
                for i in range(length):
                    for c in char:
                        new = g[:i] + c + g[i + 1:]
                        if new in back: return dis
                        if new in bank:
                            nxt_front.add(new)
                            bank.remove(new)
            front = nxt_front
            if len(front) > len(back):
                front, back = back, front
        return -1
