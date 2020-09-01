# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-01 14:53
 @Author  : QDY
 @FileName: test.py
 @Software: PyCharm
"""

nums = list(map(int, input().split()))
res = []
right = ''
for num in nums:
    bin_str = bin(num)[2:]
    bin_str = (32-len(bin_str))*'0'+bin_str
    bin_str = list(bin_str)
    for i in range(0,32,2):
        bin_str[i],bin_str[i+1] = bin_str[i+1],bin_str[i]

    new = right + ''.join(bin_str)
    right = new[-2:]
    res.append(new[:-2])
res[0] = right+res[0]
for i in res:
    print(int(i,2),end=' ')

