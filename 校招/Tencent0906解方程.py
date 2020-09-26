# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-07 11:18
 @Author  : QDY
 @FileName: Tencent0906解方程.py
 @Software: PyCharm
"""
"""
输入n,表示n次方程,n<=5
接下来输入n+1个整数
表示方程 An*(x**n)+...+A1*x+A0=0， |Ai|<=10
输出方程的根，重根只输出一次,保留两位小数
若无根则输出'No'

对于 f(x) = x**n+...+(A1/An)*x+A0/An = 0
根的上界为 M = k+1, k为最小负数系数的绝对值
设x为f(x)的根，则M-x=z>0 ->x = M-z  z>0
替换 f(x)=f(M-z)=g(z)
对于g(z)=0,根的下界为0，可以重新计算g(z)的上界

对g(z)连续求导，逐级求根
"""
if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
