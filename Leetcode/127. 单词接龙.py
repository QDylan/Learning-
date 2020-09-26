# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-26 20:44
 @Author  : QDY
 @FileName: 127. 单词接龙.py
 @Software: PyCharm
"""
"""
定两个单词（beginWord和 endWord）和一个字典，找到从beginWord 到endWord 的最短转换序列的长度。转换需遵循如下规则：
每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。

说明:
如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

示例1:
输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
输出: 5
解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
     
示例 2:
输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出:0
解释:endWord "cog" 不在字典中，所以无法进行转换。

"""


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if endWord not in wordList or beginWord == endWord: return 0
        front, back = {beginWord}, {endWord}
        wordList = set(wordList)
        length, dist = len(beginWord), 1
        while front and back:  # 双向BFS
            dist += 1
            next_front = set()
            for word in front:
                for i in range(length):
                    for j in range(ord('a'), ord('z') + 1):
                        new = word[:i] + chr(j) + word[i + 1:]
                        if new in back: return dist
                        if new in wordList:
                            next_front.add(new)
                            wordList.remove(new)
            front = next_front
            if len(front) > len(back):
                front, back = back, front
        return 0
