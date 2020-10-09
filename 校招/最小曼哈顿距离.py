# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-30 17:16
 @Author  : QDY
 @FileName: 最小曼哈顿距离.py
 @Software: PyCharm
"""
"""
1.输入正整数P表示 居民数量
2.接下来输入P行数据 每行表示 居民坐标 x,y
3.输入车站选址数量T
4.接下来输入T行数据，每行表示一个车站 选址坐标 x,y
输出 距离所有居民的曼哈顿距离总和最小的车站坐标（总距离相同输出最先出现的）
"""
from bisect import bisect_left


def Manhattan(x, y, X, Y):
    res = 0
    for i in range(len(X)):
        res += abs(x - X[i]) + abs(y - Y[i])
    return res


if __name__ == '__main__':
    X, Y = [], []
    P = int(input())
    for p in range(P):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    # T = 6
    # X = [1, 4, -3, 2, 2, 0]
    # Y = [2, 4, -1, 0, 3, 3]
    X.sort()
    Y.sort()  # 将居民坐标按X,Y分别排序并计算前缀和
    Xprefix, Yprefix = [0] * (P + 1), [0] * (P + 1)
    for i in range(P):  # 预处理前缀和
        Xprefix[i + 1] = Xprefix[i] + X[i]
        Yprefix[i + 1] = Yprefix[i] + Y[i]
    res = float('inf')
    res_x, res_y = 0, 0
    T = int(input())
    for t in range(T):
        x, y = map(int, input().split())
        # print('True d = %s' % (Manhattan(x, y, X, Y)))
        x_id, y_id = bisect_left(X, x), bisect_left(Y, y)  # logN时间内计算出(x,y)到所有居民的曼哈顿距离总和
        x_d = (x_id * x - Xprefix[x_id]) + (Xprefix[P] - Xprefix[x_id] - (P - x_id) * x)
        y_d = (y_id * y - Yprefix[y_id]) + (Yprefix[P] - Yprefix[y_id] - (P - y_id) * y)
        distance = x_d + y_d
        # print('d%s = %s' % (t, distance))
        if distance < res:
            res, res_x, res_y = distance, x, y
    print(res_x, res_y)

# 5
# 1 2
# 4 3
# -4 6
# -2 -1
# 0 4
