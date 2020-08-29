# -*- coding: utf-8 -*-
"""
 @Time    : 2020-08-29 17:28
 @Author  : QDY
 @FileName: 621. 任务调度器.py
 @Software: PyCharm
"""
"""
    给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。
    任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。
    CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。
    然而，两个相同种类的任务之间必须有长度为n 的冷却时间，
    因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
    你需要计算完成所有任务所需要的最短时间。
    
    示例 ：
    输入：tasks = ["A","A","A","B","B","B"], n = 2
    输出：8
    解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
         在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，
         而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。 
    
    
    提示：
    任务的总个数为[1, 10000]。
    n 的取值范围为 [0, 100]。

"""
from collections import Counter


class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        N = len(tasks)
        cnter = Counter(tasks)  # 统计每种任务的次数
        order = sorted(cnter.keys(), key=lambda x: -cnter[x])  # 按从多到少排序
        # 对于最多的任务X,其出现次数为p=cnter[order[0]]
        # 排列任务X将需要(p-1)*(N+1)+1个位置
        max_val = cnter[order[0]] - 1
        rest = n * (max_val)  # 将产生(p-1)*N个空位 (分成了p-1块空间)
        for i in range(1, len(order)):  # 将之后的任务填入这些空位中
            # 若某个任务Y的次数与X相同，则其占掉p-1个空位，第p个Y新加在最后
            # 若某个任务Z的次数为p-1，则其占掉p-1个空位
            # 若某个任务的次数q小于p-1，则其占掉q个空位（在p-1块区域中任选q个都可行）
            # 当剩余空间不足时，剩余的任务可以均匀的分布到p-1块中的q块尾部，仍然可行
            rest -= min(max_val, cnter[order[i]])

        return rest + N if rest > 0 else N  # 若剩余空位>0则总位置数为rest+N
