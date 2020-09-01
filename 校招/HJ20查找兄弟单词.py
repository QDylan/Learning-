# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-01 17:53
 @Author  : QDY
 @FileName: HJ20查找兄弟单词.py
 @Software: PyCharm
"""
from collections import defaultdict

while True:
    try:
        d = defaultdict(list)
        tmp = input().split()
        N = int(tmp[0])
        words = tmp[1:1 + N]
        search_w = tmp[-2]
        num = int(tmp[-1])
        for w in words:
            cnt = [0] * 26
            for c in w:
                cnt[ord(c) - ord('a')] += 1
            d[tuple(cnt)].append(w)
        for t in d:
            d[t].sort()
        cnt = [0] * 26
        for c in search_w:
            cnt[ord(c) - ord('a')] += 1
        bothers = d[tuple(cnt)].copy()
        while search_w in bothers:
            bothers.remove(search_w)
        print(len(bothers))
        if bothers and num <= len(bothers):
            print(bothers[num - 1])
    except:
        break
