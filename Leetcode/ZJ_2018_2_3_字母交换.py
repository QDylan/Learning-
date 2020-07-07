# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/12 14:24
 @Author  : QDY
 @FileName: ZJ_2018_2_3_字母交换.py

    字符串S由小写字母构成，长度为n。定义一种操作，每次都可以挑选字符串中任意的两个相邻字母进行交换。
    询问在至多交换m次之后，字符串中最多有多少个连续的位置上的字母相同？

    输入描述:
    第一行为一个字符串S与一个非负整数m。(1 <= |S| <= 1000, 1 <= m <= 1000000)

    输出描述:
    一个非负整数，表示操作之后，连续最长的相同字母数量。

    输入例子1:
    abcbaa 2

    输出例子1:
    2

    例子说明1:
    使2个字母a连续出现，至少需要3次操作。即把第1个位置上的a移动到第4个位置。
    所以在至多操作2次的情况下，最多只能使2个b或2个a连续出现。
"""
from collections import defaultdict

s, num = input().split()
num = int(num)

d = defaultdict(list)
# 记录每个字母出现的位置
for pos, char in enumerate(s):
    d[char].append(pos)

# 动态规划
# dp[i][j]:第i个char到第j个char的字母要移动在一起，需要移动的次数
# vec: 某种字母cahr出现在原字符串中的位置
# dp[i][j]=dp[i+1][j-1]+(vec[j]-vec[i]-1)-(j-i-1)，i<j
# 对于左边位置i和右边位置j,若只需将这两个字母移动到一起，需要固定的vec[j]-vec[i]-1次
# 但这个区间内已经有移动好的j-i-1个字母，所以可以减去这么j-i-1次
res = 0
for char, vec in d.items():  # vec记录字母char在原字符串中的位置
    n = len(vec)  # 字母char在s中出现的次数
    dp = [[0] * n for _ in range(n)]
    for i in range(1, n):  # 最近的两个char移动在一起
        dp[i - 1][i] = vec[i] - vec[i - 1] - 1
    for i in range(2, n):  # 间隔从2开始,直到n-1（表示对第一个char和最后一个char）
        for j in range(n - i):
            left, right = j, j + i  # 左侧从0开始，直到n-i；右侧从j+i开始，直到n
            dp[left][right] = dp[left + 1][right - 1] + vec[right] - vec[left] - 1 - (i - 1)
            # i=2时，dp[left+1][right-1]==0,  (i-1)表示left和right中间有多少个char
            #  减去(i=2)-1表示：left移动到中间的char的左侧时，再移动right到中间的char的右侧，可以少移动一位
            # 间隔i越大，可以减去的步数越多
            # 经过dp[left+1][right-1]步后，中心有i-1个连续的char
            # vec[right]-vec[left]-1-(i-1)：将left移动到中心的左侧+将right移动到中心的右侧需要的步数

    for i in range(n):
        for j in range(i, n):
            if dp[i][j] <= num:  # 满足移动步数的限制
                res = max(res, j - i + 1)
    print(dp)
print(res)
