# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/7 23:26
 @Author  : QDY
 @FileName: 126. 单词接龙 II_BFS_DFS_hard.py

    给定两个单词（beginWord 和 endWord）和一个字典 wordList，
    找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

    每次转换只能改变一个字母。
    转换过程中的中间单词必须是字典中的单词。

    说明:
    如果不存在这样的转换序列，返回一个空列表。
    所有单词具有相同的长度。
    所有单词只由小写字母组成。
    字典中不存在重复的单词。
    你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

    示例 1:
    输入:
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]

    输出:
    [
      ["hit","hot","dot","dog","cog"],
      ["hit","hot","lot","log","cog"]
    ]

    示例 2:
    输入:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]

    输出: []
    解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。

"""
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        #
        if endWord not in wordList:return []
        if beginWord==endWord:return [[beginWord]]
        res = []

        if beginWord not in wordList:  # 若beginWord不在wordList中则添加进去
            wordList.append(beginWord)
        len_wl,len_w = len(wordList),len(wordList[0])
        edge = {i:set() for i in range(len_wl)}  # 构建一张无向图，edge[word]={wordList中，word只变换一个字符得到的单词}
        tmp_list = {word:id_ for id_,word in enumerate(wordList)}
        for k in range(len_wl):  # 时间复杂度 O(n*25*len_w)
            for i in range(len_w):
                for j in range(97,123):  # chr(97)='a',chr(122)='z'
                    tmp = wordList[k][:i]+chr(j)+wordList[k][i+1:]
                    if chr(j)!=wordList[k][i] and tmp in tmp_list:
                        edge[tmp_list[tmp]].add(k)
                        edge[k].add(tmp_list[tmp])
        # def can_transform(str1,str2):
        #     diff = 0
        #     for k in range(len_w):
        #         if str1[k] != str2[k]:
        #             diff += 1
        #         if diff > 1: return False
        #     return True
        # for i in range(len_wl-1):  # 时间复杂度O(len_w*N^2) 超时
        #     for j in range(i+1,len_wl):
        #         if can_transform(wordList[i],wordList[j]):
        #             edge[i].add(j)
        #             edge[j].add(i)
        # print(edge)
        start_id = wordList.index(beginWord)
        cost = [float('inf')]*len_wl  # cost[i]=beginWord到wordList[i]需要几步
        cost[start_id] = 0
        queue = [[start_id]]

        while queue and not res:  # BFS
            length = len(queue)
            for i in range(length):
                word = queue.pop(0)

                for w_id in edge[word[-1]]:  # word[-1]为当前词链的最后一个词（的id）
                    if wordList[w_id] == endWord:  # 下一个词是endWord，加入res
                        res.append(word+[w_id])
                        continue
                    if cost[w_id] > cost[word[-1]]:  # 若下一个词w_id到startWord的距离大于word[-1]到startWord的距离
                        cost[w_id] = cost[word[-1]] + 1  # 说明可以把w_id添加到当前词链之后
                        queue.append(word + [w_id])
            # print(queue)

        if res:
            for i in range(len(res)):
                for j in range(len(res[i])):
                    res[i][j] = wordList[res[i][j]]
        return res
