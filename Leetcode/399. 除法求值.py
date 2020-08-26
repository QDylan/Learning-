# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/26 9:15
 @Author  : QDY
 @FileName: 399. 除法求值.py
 @Software: PyCharm
"""
"""
    给出方程式 A / B = k, 其中 A 和 B 均为用字符串表示的变量， 
    k 是一个浮点型数字。根据已知方程式求解问题，并返回计算结果。如果结果不存在，则返回 -1.0。

    示例 :
    给定 a / b = 2.0, b / c = 3.0
    问题: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
    返回 [6.0, 0.5, -1.0, 1.0, -1.0 ]

    输入为: vector<pair<string, string>> equations, 
    vector<double>& values, vector<pair<string, string>> queries(方程式，方程式结果，问题方程式)， 
    其中 equations.size() == values.size()，即方程式的长度与方程式结果长度相等（程式与结果一一对应），
    并且结果值均为正数。以上为方程式的描述。 返回vector<double>类型。

    基于上述例子，输入如下：
    equations(方程式) = [ ["a", "b"], ["b", "c"] ],
    values(方程式结果) = [2.0, 3.0],
    queries(问题方程式) = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
    输入总是有效的。你可以假设除法运算中不会出现除数为0的情况，且不存在任何矛盾的结果。

"""
from collections import defaultdict


class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)
        visited, relation = {}, {}
        for i, eq in enumerate(equations):
            graph[eq[0]].append(eq[1])
            graph[eq[1]].append(eq[0])
            relation[(eq[0], eq[1])] = values[i]
            relation[(eq[1], eq[0])] = 1 / values[i]
            visited[eq[0]] = 0
            visited[eq[1]] = 0
        res = []

        def dfs(cur, val, target):
            if target in graph[cur]:
                return val * relation[(cur, target)]
            visited[cur] = 1
            for nxt in graph[cur]:
                if visited[nxt] == 0:
                    ans = dfs(nxt, val * relation[(cur, nxt)], target)
                    if ans >= 0:
                        visited[cur] = 0
                        return ans
            visited[cur] = 0
            return -1

        for i, q in enumerate(queries):
            if q[0] not in graph or q[1] not in graph:
                res.append(-1.0)
            elif q[0] == q[1]:
                res.append(1.0)
            else:
                res.append(dfs(q[0], 1, q[1]))

        return res
