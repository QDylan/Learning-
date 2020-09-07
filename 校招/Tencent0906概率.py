# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-07 9:44
 @Author  : QDY
 @FileName: Tencent0906概率.py
 @Software: PyCharm
"""
"""
给定一根木棍长度L和阈值d
若L>d，则在木棍随机位置上砍一刀将木棍分成左右两部分
丢弃左边，若右边仍大于d，则再砍一刀，重复以上的操作
求期望

设阈值为d木棍长为L的期望 = f(x=L)
f(x=L) = f(0<x<d)+f(d<=x<L)+1 = f(d<=x<L)+1
f(d<=x<L) = (1/L)*∫(f(x=T))dT,x from d to L, T为d~L上的分割点
所以 f(x=L) = (1/L)*∫(f(x=T))dT + 1
两边同时求导，有
f'(x=L) = -1/(L**2)*(∫(f(x=T))dT,x from d to L) + (1/L)*f(x=L) ......(1)
因为 f(x=L) = (1/L)*∫(f(x=T))dT,x from d to L
所以 (∫(f(x=T))dT,x from d to L) = f(x=L)*L, 带入(1)式
-> f'(x=L) = (-1/L)*(f(x=L)*L) + (1/L)*f(x=L)
-> f'(x=L) = 1/L
-> f(x=L) = ln(L)+C
因为 f(x=d) = ln(d)+C = 1  所以 C=1-ln(d)
所以 f(x=L) = ln(L)-ln(d)+1

"""

from math import log

if __name__ == '__main__':
    L, d = map(int, input().split())
    if L>d:
        print('%.4f'%(log(L)-log(d)+1))
    else:
        print('%.4f'%0)
