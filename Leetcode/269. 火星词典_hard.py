# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/22 15:08
 @Author  : QDY
 @FileName: 269. 火星词典_hard.py
 @Software: PyCharm
"""
"""
    现有一种使用字母的全新语言，这门语言的字母顺序与英语顺序不同。
    假设，您并不知道其中字母之间的先后顺序。但是，会收到词典中获得一个 不为空的 单词列表。
    因为是从词典中获得的，所以该单词列表内的单词已经 按这门新语言的字母顺序进行了排序。

    您需要根据这个输入的列表，还原出此语言中已知的字母顺序。

    示例 1：
    输入:
    [
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt"
    ]
    输出: "wertf"

    示例 2：
    输入:
    [
    "z",
    "x"
    ]
    输出: "zx"

    示例 3：
    输入:
    [
    "z",
    "x",
    "z"
    ] 
    输出: "" 
    解释: 此顺序是非法的，因此返回 ""。


    提示：
    你可以默认输入的全部都是小写字母
    若给定的顺序是不合法的，则返回空字符串即可
    若存在多种可能的合法字母顺序，请返回其中任意一种顺序即可

"""


class Solution:
    def alienOrder(self, words):
        if not words: return ''
        graph, visited = {}, {}

        for w in words:
            for c in w:
                graph[c] = []
                visited[c] = 0

        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]
            cur1, cur2 = 0, 0
            while cur1 < len(w1) and cur2 < len(w2):
                if w1[cur1] == w2[cur2]:
                    cur1 += 1
                    cur2 += 1
                else:  # w1[cur1]<w2[cur2]
                    graph[w1[cur1]].append(w2[cur2])
                    break
                if cur2 == len(w2) and cur1 < len(w1):  # 'abc','ab'
                    return ''

        self.res, self.valid = '', True

        def dfs(c):  # dfs实现拓扑排序
            visited[c] = 1  # 搜索中的标记为1
            if c in graph:
                for nxt in graph[c]:
                    if visited[nxt] == 1:  # 遇到环，返回
                        self.valid = False
                        return
                    if visited[nxt] == 0:
                        dfs(nxt)
                        if not self.valid: return
            visited[c] = 2
            self.res += c

        for char in graph:
            if visited[char] == 0:
                dfs(char)
                if not self.valid:
                    return ''

        return self.res[::-1]
