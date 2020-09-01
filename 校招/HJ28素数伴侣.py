# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-01 20:30
 @Author  : QDY
 @FileName: HJ28素数伴侣.py
 @Software: PyCharm
"""
"""
题目描述
若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，如2和5、6和13，它们能应用于通信加密。
现在密码学会请你设计一个程序，从已有的N（N为偶数）个正整数中挑选出若干对组成“素数伴侣”，
挑选方案多种多样，例如有4个正整数：2，5，6，13，如果将5和6分为一组中只能得到一组“素数伴侣”，
而将2和5、6和13编组将得到两组“素数伴侣”，能组成“素数伴侣”最多的方案称为“最佳方案”，当然密码学会希望你寻找出“最佳方案”。

输入:
有一个正偶数N（N≤100），表示待挑选的自然数的个数。后面给出具体的数字，范围为[2,30000]。

输出:
输出一个整数K，表示你求得的“最佳方案”组成“素数伴侣”的对数。

输入描述:
输入说明
1 输入一个正偶数n
2 输入n个整数

输出描述:
求得的“最佳方案”组成“素数伴侣”的对数。

示例1
输入
复制
4
2 5 6 13
输出
复制
2
"""
n = 60000
is_prime = [0, 0] + [1] * (n - 2)
for i in range(2, int(n ** 0.5) + 1):
    if is_prime[i]:
        is_prime[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)
prime = set()
for i in range(2, n):
    if is_prime[i]: prime.add(i)
from functools import lru_cache


@lru_cache
def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if not num % i: return False
    return True


while True:
    try:
        m, nums = int(input()), list(map(int, input().split()))
        res = 0
        odd, even = [], []
        for i in nums: # 将数分为奇数和偶数
            if i & 1:
                odd.append(i)
            else:
                even.append(i)
        if not odd or not even:
            print(0)
            continue
        odd_num = len(odd)
        # 每一对能组成为素数伴侣的奇数和偶数之间连接一条边，可以构成一个无向图
        # 在无向图中寻找最多的配对

        def find(x, used, match):  # 匈牙利算法：利用增广路径求二分图的最大匹配
            for i in range(odd_num):
                if used[i] == 0 and odd[i] + x in prime:
                    used[i] = 1
                    # 1.若match[i]==0，说明第i个奇数还未被配对，直接将其与x配对即可
                    # 2.若match[i]!=0，说明第i个奇数已被配对，尝试给其配对对象match[i]寻找另一个对象
                    # 递归调用find(match[i], used, match)，used发生了变化，使其不会选择重复的对象
                    if match[i] == 0 or find(match[i], used, match):
                        match[i] = x
                        return True
            return False


        match = [0] * odd_num
        for x in even:  # 遍历所有偶数为其寻找对象
            used = [0] * odd_num  # used记录这次寻找对象的过程中
            if find(x, used, match): res += 1  # 找到了对象，res+1
        print(res)
    except:
        break
