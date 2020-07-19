# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/19 23:48
 @Author  : QDY
 @FileName: 5466. 最多的不重叠子字符串.py

    给你一个只包含小写字母的字符串 s ，你需要找到 s 中最多数目的非空子字符串，满足如下条件：

    这些字符串之间互不重叠，也就是说对于任意两个子字符串 s[i..j] 和 s[k..l] ，要么 j < k 要么 i > l 。
    如果一个子字符串包含字符 c ，那么 s 中所有 c 字符都应该在这个子字符串中。
    请你找到满足上述条件的最多子字符串数目。如果有多个解法有相同的子字符串数目，
    请返回这些子字符串总长度最小的一个解。可以证明最小总长度解是唯一的。

    请注意，你可以以 任意 顺序返回最优解的子字符串。

    示例 1：
    输入：s = "adefaddaccc"
    输出：["e","f","ccc"]
    解释：下面为所有满足第二个条件的子字符串：
    [
      "adefaddaccc"
      "adefadda",
      "ef",
      "e",
      "f",
      "ccc",
    ]
    如果我们选择第一个字符串，那么我们无法再选择其他任何字符串，所以答案为 1 。如果我们选择 "adefadda" ，
    剩下子字符串中我们只可以选择 "ccc" ，它是唯一不重叠的子字符串，所以答案为 2 。
    同时我们可以发现，选择 "ef" 不是最优的，因为它可以被拆分成 2 个子字符串。
    所以最优解是选择 ["e","f","ccc"] ，答案为 3 。不存在别的相同数目子字符串解。

    示例 2：
    输入：s = "abbaccd"
    输出：["d","bb","cc"]
    解释：注意到解 ["d","abba","cc"] 答案也为 3 ，但它不是最优解，因为它的总长度更长。
     
    提示：
    1 <= s.length <= 10^5
    s 只包含小写英文字母。

"""
from collections import defaultdict


class Solution:
    def maxNumOfSubstrings(self, s):
        dic, len_s = defaultdict(list), len(s)
        for i in range(len_s):  # 记录每个字符出现的位置
            dic[s[i]].append(i)
        list_ = []
        for c in dic:  # 对于某个字符，计算包含这个字符的最小字符串起始索引
            i, tmp = dic[c][0] + 1, [dic[c][0], dic[c][-1]]
            while i <= tmp[1]:
                tmp[0] = min(tmp[0], dic[s[i]][0])
                tmp[1] = max(tmp[1], dic[s[i]][-1])
                i += 1
            dic[c] = tmp
            list_.append(dic[c])  # 将起始索引存入list_中
        # 按照字符串长度优先的原则进行排序
        list_.sort(key=lambda x: (x[1] - x[0], x[0], x[1]))

        check, res = {}, []
        for l in list_:
            if l[1] == l[0]:  # 贪心，优先选择那些只出现了一次的字符串
                check[s[l[0]]] = True  # 并将其标记存入check中
                res.append(s[l[0]])
            else:
                valid = True
                for i in range(l[0], l[1] + 1):  # 对于字符串l
                    if s[i] in check:  # 若其中包含了出现在check中的字符，则不选择
                        valid = False
                        break
                if valid:  #
                    res.append(s[l[0]:l[1] + 1])
                    for i in range(l[0], l[1] + 1):
                        check[s[i]] = True
            # print(check)
        return res
