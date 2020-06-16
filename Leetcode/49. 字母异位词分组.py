# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/16 22:10
 @Author  : QDY
 @FileName: 49. 字母异位词分组.py

    给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

    示例:
    输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
    输出:
    [
      ["ate","eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]

"""


class Solution:
    def groupAnagrams(self, strs):
        res = {}
        for s in strs:
            # 将每个字符串s 转换为字符数count，由26个非负整数组成
            count = [0] * 26  # count[i]为第i个字母的数量
            for c in s:
                count[ord(c) - 97] += 1
            if tuple(count) in res:
                res[tuple(count)].append(s)
            else:
                res[tuple(count)] = [s]
        return list(res.values())
