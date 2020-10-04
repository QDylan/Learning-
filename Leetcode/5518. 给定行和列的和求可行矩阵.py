# -*- coding: utf-8 -*-
"""
 @Time    : 2020-10-04 15:38
 @Author  : QDY
 @FileName: 5518. 给定行和列的和求可行矩阵.py
 @Software: PyCharm
"""
"""
给你两个非负整数数组rowSum 和colSum，其中rowSum[i]是二维矩阵中第 i行元素的和， colSum[j]是第 j列元素的和。
换言之你不知道矩阵里的每个元素，但是你知道每一行和每一列的和。

请找到大小为rowSum.length x colSum.length的任意 非负整数矩阵，且该矩阵满足rowSum 和colSum的要求。

请你返回任意一个满足题目要求的二维矩阵，题目保证存在 至少一个可行矩阵。


示例 1：

输入：rowSum = [3,8], colSum = [4,7]
输出：[[3,0],
      [1,7]]
解释：
第 0 行：3 + 0 = 0 == rowSum[0]
第 1 行：1 + 7 = 8 == rowSum[1]
第 0 列：3 + 1 = 4 == colSum[0]
第 1 列：0 + 7 = 7 == colSum[1]
行和列的和都满足题目要求，且所有矩阵元素都是非负的。
另一个可行的矩阵为：[[1,2],
                  [3,5]]
                  
示例 2：
输入：rowSum = [5,7,10], colSum = [8,6,8]
输出：[[0,5,0],
      [6,1,0],
      [2,0,8]]
      
示例 3：
输入：rowSum = [14,9], colSum = [6,9,8]
输出：[[0,9,5],
      [6,0,3]]
      
示例 4：
输入：rowSum = [1,0], colSum = [1]
输出：[[1],
      [0]]
示例 5：
输入：rowSum = [0], colSum = [0]
输出：[[0]]

提示：
1 <= rowSum.length, colSum.length <= 500
0 <= rowSum[i], colSum[i] <= 108
sum(rows) == sum(columns)

"""


class Solution:
    def restoreMatrix(self, rowSum, colSum):
        h, w = len(rowSum), len(colSum)
        matrix = [[0] * w for _ in range(h)]  # 初始化矩阵
        for i in range(h):
            for j in range(w):
                minVal = min(rowSum[i], colSum[j])  # 贪心，每次取可以取的最大值
                matrix[i][j] = minVal
                rowSum[i] -= minVal
                colSum[j] -= minVal
                if rowSum[i] == 0 and colSum == 0: break  # 剪枝：当发现 rowSum 和 colSum 都是 0 的时候，就没必要再继续遍历下去了
        return matrix
