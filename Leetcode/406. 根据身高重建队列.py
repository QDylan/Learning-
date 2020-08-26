# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/26 10:21
 @Author  : QDY
 @FileName: 406. 根据身高重建队列.py
 @Software: PyCharm
"""
"""
    假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，
    k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。

    注意：
    总人数少于1100人。

    示例
    输入:
    [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

    输出:
    [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

"""


class Solution:
    def reconstructQueue(self, people):
        people.sort(key=lambda x: (x[0], -x[1]))  # 先对数组按h升序，k降序排列
        length = len(people)
        res = [None] * length
        rest_num = [_ for _ in range(length)]
        for i in range(length):  # 从头遍历循环数组
            j = rest_num.pop(people[i][1])  # 当前位置就是剩下未被安排中的最矮的，
            res[j] = people[i]  # 能优先选择位置，其k值就是剩余空位的索引

        return res
