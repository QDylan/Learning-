# -*- coding: utf-8 -*-
"""
 @Time    : 2020/5/27 16:30
 @Author  : QDY
 @FileName: 204. 计数质数_埃拉托斯特尼筛法.py

    统计所有小于非负整数 n 的质数的数量
"""


class Solution:
    def countPrimes(self, n):
        # Sieve of Eratosthenes
        # 操作数= n × (1/2 + 1/3 + 1/5 + 1/7...) 时间复杂度 O(N * loglogN)
        is_prime = [0, 0] + [1] * (n - 2)
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                is_prime[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)
                # j = i**2  # 避免重复
                # while j < n:
                #     is_prime[j] = 0
                #     j += i

        return sum(is_prime)
