# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/21 23:11
 @Author  : QDY
 @FileName: 腾讯2018_逛街.py
 @Software: PyCharm
"""
"""
小Q在周末的时候和他的小伙伴来到大城市逛街，一条步行街上有很多高楼，共有n座高楼排成一行。
小Q从第一栋一直走到了最后一栋，小Q从来都没有见到这么多的楼，
所以他想知道他在每栋楼的位置处能看到多少栋楼呢？（当前面的楼的高度大于等于后面的楼时，后面的楼将被挡住） 
"""
while True:
    try:
        n = int(input())
        buildings = list(map(int, input().split()))
        stack = []  # 单调栈
        res = [1] * n
        for i in range(n):
            res[i] += len(stack)
            while stack and stack[-1] <= buildings[i]:
                stack.pop()
            stack.append(buildings[i])
        stack = []
        for i in range(n - 1, -1, -1):
            res[i] += len(stack)
            while stack and stack[-1] <= buildings[i]:
                stack.pop()
            stack.append(buildings[i])
        for i in res:
            print(i, end=' ')
    except:
        break
