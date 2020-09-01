# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-01 21:24
 @Author  : QDY
 @FileName: HJ77火车进站.py
 @Software: PyCharm
"""
"""
给定一个正整数N代表火车数量，0<N<10，接下来输入火车入站的序列，一共N辆火车，每辆火车以数字1-9编号，
火车站只有一个方向进出，同时停靠在火车站的列车中，只有后进站的出站了，先进站的才能出站。要求以字典序排序输出火车出站的序列号。

输入描述:
有多组测试用例，每一组第一行输入一个正整数N（0<N<10），第二行包括N个正整数，范围为1到9。

输出描述:
输出以字典序从小到大排序的火车出站序列号，每个编号以空格隔开，每个输出序列换行，具体见sample。

示例1
输入

3
1 2 3
输出

1 2 3
1 3 2
2 1 3
2 3 1
3 2 1

其实就是给定一个栈的输入顺序，求这个栈有多少种出栈的顺序
"""


def dfs(rest, helper, cur, res, N):
    # rest:剩余的数，一个队列，每次出队第一个数
    # helper：辅助用的中间态栈，rest输出的数必须先到这里，这里的数输出可以到cur
    # cur: 出栈顺序
    if len(cur) == N:  # 所有的元素都出栈了
        res.append(' '.join(cur))
        return
    if not helper:  # helper为空，需要rest出队一个到helper中
        dfs(rest[1:], helper + [rest[0]], cur, res, N)
    elif not rest:  # rest为空，这时只能从helper中出栈到cur中
        dfs(rest, helper[:-1], cur + [helper[-1]], res, N)
    else:  # 有两种选择：1.rest出队 2.helper出栈
        dfs(rest, helper[:-1], cur + [helper[-1]], res, N)
        dfs(rest[1:], helper + [rest[0]], cur, res, N)


while True:
    try:
        N = int(input())
        nums = input().split()
        res = []
        dfs(nums, [], [], res, N)
        res.sort()
        for i in res:
            print(i, end='\n')
    except:
        break
