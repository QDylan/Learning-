# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/10 10:54
 @Author  : QDY
 @FileName: 440. 字典序的第K小数字_hard.py

    给定整数 n 和 k，找到 1 到 n 中字典序第 k 小的数字。
    注意：1 ≤ k ≤ n ≤ 109。

    示例 :
    输入:
    n: 13   k: 2
    输出:
    10

    解释:
    字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。

"""


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        k -= 1
        prefix = 1  # 搜索前缀从1开始
        while k != 0:
            num = 0
            start, end = prefix, prefix + 1  # start=当前前缀起点，end=下一个前缀起点
            # 寻找在n以内，以prefix为前缀的节点个数num
            while start <= n:  # 前缀超过上界时退出循环
                # end-start=该层树的节点个数
                # 若end>n+1，说明该层树的结点不是满的
                num += min(n + 1, end) - start
                start *= 10  # 进入树的下一层
                end *= 10  #
            if num > k:  # 若num>k,说明第k个数在以prefix为根节点的树中，其前缀为prefix
                prefix *= 10  # 进入prefix的下一层寻找
                k -= 1  #
            else:  # 若 num<=k，说明第k个数在以prefix为根的树之后，前缀应大于prefix
                k -= num  # prefix树下的num个节点都不会是第k个数
                prefix += 1  # 在prefix后面的树中找出第k-num个数
        return prefix
