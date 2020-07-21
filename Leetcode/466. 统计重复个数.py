# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/21 14:12
 @Author  : QDY
 @FileName: 466. 统计重复个数.py
 @Software: PyCharm
"""
"""
    由 n 个连接的字符串 s 组成字符串 S，记作 S = [s,n]。例如，["abc",3]=“abcabcabc”。
    如果我们可以从 s2 中删除某些字符使其变为 s1，则称字符串 s1 可以从字符串 s2 获得。
    例如，根据定义，"abc" 可以从 “abdbec” 获得，但不能从 “acbbe” 获得。
    现在给你两个非空字符串 s1 和 s2（每个最多 100 个字符长）和两个整数 0 ≤ n1 ≤ 106 和 1 ≤ n2 ≤ 106。
    现在考虑字符串 S1 和 S2，其中 S1=[s1,n1] 、S2=[s2,n2] 。
    请你找出一个可以满足使[S2,M] 从 S1 获得的最大整数 M 。

    示例：
    输入：
    s1 ="acb",n1 = 4
    s2 ="ab",n2 = 2
    返回：
    2

"""


class Solution:
    def getMaxRepetitions(self, s1, n1, s2, n2):
        # 1. 暴力遍历找到循环节
        # 2. 通过循环节计算有多少个循环部分
        # 3. 暴力遍历剩余（长度达不到循环）的部分
        if n1 == 0:
            return 0
        s1_count, index, s2_count = 0, 0, 0
        # recall 是哈希表
        recall = {}
        # 假设 遍历了s1_count个s1时，匹配到第s2_count个s2的第index个字符
        # 若之前recall中记录了遍历了s1_count_时，匹配到s2_count_个s2的第index个字符,
        # 则表示找到了循环节

        # 用 (s1_count_, s2_count_, index) 和 (s1_count, s2_count, index)
        # 表示两次包含相同 index 的匹配结果
        # 那么哈希映射中的键就是 index，值就是 (s1_count_, s2_count_) 这个二元组

        # 循环节就是；
        #    - 前 s1_count_ 个 s1 包含了 s2_count_个 s2
        #    - 以后的每 (s1_count - s1_count_) 个 s1 包含了 (s2_count - s2_count_) 个 s2
        # 那么还会剩下 (n1 - s1_count_) % (s1_count - s1_count_) 个 s1, 我们对这些与 s2 进行暴力匹配
        # 注意 s2 要从第 index 个字符开始匹配

        while True:
            # 我们多遍历一个 s1，看看能不能找到循环节
            s1_count += 1
            for ch in s1:  # 匹配一遍s1
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):  # 用完一个s2后，增加s2_count，index重置为0
                        s2_count, index = s2_count + 1, 0

            if s1_count == n1:  # 还没有找到循环节，所有的 s1 就用完了
                return s2_count // n2

            if index in recall:  # 出现了之前的 index，表示找到了循环节
                # 前 s1_prime 个 s1 包含了 s2_prime 个 s2
                s1_prime, s2_prime = recall[index]
                # 从s1_prime到s1_count是一个循环节
                # 以后的每 (s1_count - s1_prime) 个 s1 包含了 (s2_count - s2_prime) 个 s2
                loop = (s1_count - s1_prime, s2_count - s2_prime)
                # ans 存储的是 s1 包含的 s2 的数量
                # s2_prime：循环开始前的s2数量
                ans = s2_prime + (n1 - s1_prime) // loop[0] * loop[1]
                break  # 找到循环节，跳出
            else:  # 添加进recall中
                recall[index] = (s1_count, s2_count)

        # n1*s1 的末尾还剩下一些 s1，我们暴力进行匹配
        rest = (n1 - s1_prime) % loop[0]
        for i in range(rest):
            for ch in s1:
                # 继续从s2的index位置开始匹配
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        ans, index = ans + 1, 0
        # s1 包含 ans 个 s2，那么就包含 ans / n2 个 s2
        return ans // n2
