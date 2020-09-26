# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/1 11:58
 @Author  : QDY
 @FileName: 面试题 08.12. 八皇后.py
 @Software: PyCharm
"""
"""
    设计一种算法，打印 N 皇后在 N × N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。
    这里的“对角线”指的是所有的对角线，不只是平分整个棋盘的那两条对角线。
    注意：本题相对原题做了扩展

    示例:

    输入：4
    输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    解释: 4 皇后问题存在如下两个不同的解法。
    [
     [".Q..",  // 解法 1
      "...Q",
      "Q...",
      "..Q."],

     ["..Q.",  // 解法 2
      "Q...",
      "...Q",
      ".Q.."]
    ]

"""


class Solution:
    def solveNQueens(self, n: int):
        self.res = []
        nums = [i for i in range(n)]
        tmp_res = ['.' * i + 'Q' + '.' * (n - 1 - i) for i in range(n)]  # 在第i个位置为Q的字符串

        def dfs(visited, rest):
            if not rest:
                tmp = []
                for j in visited:
                    tmp.append(tmp_res[j])
                self.res.append(tmp)
                return
            i = len(visited)  # 已有i行
            for j in range(len(rest)):
                y, valid = 1, True  # 向上检查 左右对角线
                for x in range(i - 1, -1, -1):
                    if (rest[j] - y >= 0 and rest[j] - y == visited[x]) or (
                            rest[j] + y < n and rest[j] + y == visited[x]):
                        valid = False
                        break
                    y += 1
                if valid:
                    dfs(visited + [rest[j]], rest[:j] + rest[j + 1:])

        dfs([], nums)
        return self.res
