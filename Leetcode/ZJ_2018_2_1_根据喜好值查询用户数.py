# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/12 14:22
 @Author  : QDY
 @FileName: ZJ_2018_2_1_根据喜好值查询用户数.py

为了不断优化推荐效果，今日头条每天要存储和处理海量数据。假设有这样一种场景：我们对用户按照它们的注册时间先后来标号，
对于一类文章，每个用户都有不同的喜好值，我们会想知道某一段时间内注册的用户（标号相连的一批用户）中，有多少用户对这类文章喜好值为k。
因为一些特殊的原因，不会出现一个查询的用户区间完全覆盖另一个查询的用户区间(不存在L1<=L2<=R2<=R1)。

输入描述:
输入： 第1行为n代表用户的个数 第2行为n个整数，第i个代表用户标号为i的用户对某类文章的喜好度 第3行为一个正整数q代表查询的组数
第4行到第（3+q）行，每行包含3个整数l,r,k代表一组查询，
即标号为l<=i<=r的用户中对这类文章喜好值为k的用户的个数。 数据范围n <= 300000,q<=300000 k是整型

输出描述:
输出：一共q行，每行一个整数代表喜好值为k的用户的个数
"""
n = int(input())
user_like = list(map(int, input().split()))
q = int(input())
search = [list(map(int, input().split())) for _ in range(q)]

dic = {}
for i in range(n):  # 喜好值：[用户]
    try:
        dic[user_like[i]].append(i + 1)
    except:
        dic[user_like[i]] = [i + 1]
result_list = []

for i in range(q):
    l, r, k = search[i]
    if k not in dic:  # 不存在喜好值为k的
        result = 0
    else:
        temp = dic[k]
        result = 0
        if temp[-1] < l or temp[0] > r:
            pass  # 用户id不在[l,r]内
        else:
            for i in range(len(temp)):
                if l <= temp[i] <= r:
                    result += 1

    result_list.append(result)
for r in result_list:
    print(r)
