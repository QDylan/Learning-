# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-17 10:17
 @Author  : QDY
 @FileName: q1.py
 @Software: PyCharm
"""
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

density = 850
tank = [[8.91304348, 1.20652174, 0.61669004, 1.5, 0.9, 0.3, 0.3],
        [6.91304348, -1.39347826, 0.21669004, 2.2, 0.8, 1.1, 1.5],
        [-1.68695652, 1.20652174, -0.28330996, 2.4, 1.1, 0.9, 2.1],
        [3.11304348, 0.60652174, -0.18330996, 1.7, 1.3, 1.2, 1.9],
        [-5.28695652, -0.29347826, 0.41669004, 2.4, 1.2, 1, 2.6],
        [-2.08695652, -1.49347826, 0.21669004, 2.4, 1, 0.5, 0.8],
        ]  # tank[:3]：x,y,z ；tank[3:6]:长宽高； tank[6]:油量


def craft_oxyz(x, y, z, theta):
    if theta == 0: return x, y, z
    pos = np.array([[x], [y], [z]])
    R = np.array([[np.cos(theta), 0, np.sin(theta)], [0, 1, 0], [-np.sin(theta), 0, np.cos(theta)]])
    pos_ = np.dot(np.transpose(R), pos)
    return [pos_[0][0], pos_[1][0], pos_[2][0]]


def oxyz_craft(x, y, z, theta):
    if theta == 0: return x, y, z
    pos_ = np.array([[x], [y], [z]])
    R = np.array([[np.cos(theta), 0, np.sin(theta)], [0, 1, 0], [-np.sin(theta), 0, np.cos(theta)]])
    pos = np.dot(R, pos_)
    return [pos[0][0], pos[1][0], pos[2][0]]


def get_triangle(points):
    p1, p2, p3 = points
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    x3, y3, z3 = p3
    return (x1 + x2 + x3) / 3, (y1 + y2 + y3) / 3, (
            z1 + z2 + z3) / 3, x1 * y2 - x1 * y3 + x2 * y3 - x2 * y1 + x3 * y1 - x2 * y2
    #


def get_center(centr):
    nx, ny, nz, mass = 0, 0, 0, 0
    for x, y, z, m in centr:  # 求 总的质心
        nx += x * m
        ny += y * m
        nz += z * m
        mass += m
    nx, ny, nz = nx / mass, ny / mass, nz / mass
    return nx, ny, nz


def get_centerpoint(points):
    # if len(points) == 3:
    #     return get_triangle(points)[:3]
    # elif len(points) == 4:
    #     p1 = get_triangle(points[:3])
    #     p2 = get_triangle(points[2:] + [points[0]])
    #     return get_center([p1, p2])
    # elif len(points) == 5:
    #     p1 = get_triangle(points[1:3] + [points[0]])
    #     p2 = get_triangle(points[2:4] + [points[0]])
    #     p3 = get_triangle(points[3:] + [points[0]])
    #     return get_center([p1, p2, p3])
    #
    nx, nz,area = 0.0, 0.0, 0.0
    for i in range(len(points)):
        # x = points[i][0]
        # z = points[i][2]
        #
        # x1 = points[i - 1][0]
        # z1 = points[i - 1][2]
        #
        # fg = (z * x1 - z1 * x) / 2
        #
        # area += fg
        # nx += fg * (x + x1) / 3
        # nz += fg * (z + z1) / 3
        nx += points[i][0]
        nz += points[i][2]

    nx = nx / len(points)
    nz = nz / len(points)

    return nx, points[0][1], nz


def calc(x0, y0, z0, X, Y, Z, V, LH, LL, RL, RH, theta):
    theta1 = np.arctan(Z / X)
    if theta > 0:
        if theta <= theta1:
            V1 = 0.5 * X * X * Y * np.tan(theta)
            V2 = X * Y * Z - V1
            if V <= V1:
                h = (2 * V * np.tan(theta) / Y) ** 0.5
                A = [x0 - X / 2, y0, z0 - Z / 2 + h]  # 数组
                B = [x0 - X / 2 + h / np.tan(theta), y0, z0 - Z / 2]
                points = [A, LL, B]
                return points
            elif V1 < V <= V2:
                v1 = 0.5 * X * X * Y * np.tan(theta)
                h = (V - v1) / (Y * Z)
                A = [x0 - X / 2, y0, z0 - Z / 2 + h + X * np.tan(theta)]
                B = [x0 + X / 2, y0, z0 - Z / 2 + h]
                points = [A, LL, RL, B]
                return points
            else:
                v1 = X * Y * Z - V
                h = (2 * v1 * np.tan(theta) / Y) ** 0.5
                A = [x0 + X / 2, y0, z0 + Z / 2 - h]
                B = [x0 + X / 2 - h / np.tan(theta), y0, z0 + Z / 2]
                points = [LH, LL, RL, A, B]
                return points

        else:
            V1 = 0.5 * Z * Z * Y / np.tan(theta)
            V2 = X * Y * Z - V1
            if V <= V1:
                h = (2 * V * np.tan(theta) / Y) ** 0.5
                A = [x0 - X / 2, y0, z0 - Z / 2 + h]  # 数组
                B = [x0 - X / 2 + h / np.tan(theta), y0, z0 - Z / 2]
                points = [A, LL, B]
                return points
            elif V1 < V <= V2:
                v1 = 0.5 * Z * Z * Y / np.tan(theta)
                h = (V - v1) / (Y * Z)
                A = [x0 - X / 2 + h + Z / np.tan(theta), y0, z0 - Z / 2]
                B = [x0 - X / 2 + h, y0, z0 + Z / 2]
                points = [LH, LL, A, B]
                return points
            else:
                v1 = X * Y * Z - V
                h = (2 * v1 * np.tan(theta) / Y) ** 0.5
                A = [x0 + X / 2, y0, z0 + Z / 2 - h]
                B = [x0 + X / 2 - h / np.tan(theta), y0, z0 + Z / 2]
                points = [LH, LL, RL, A, B]
                return points
    else:
        theta = -theta
        if theta <= theta1:
            V1 = 0.5 * X * X * Y * np.tan(theta)
            V2 = X * Y * Z - V1
            if V <= V1:
                h = (2 * V / (Y * np.tan(theta))) ** 0.5
                A = [x0 + X / 2, y0, z0 - Z / 2 + h * np.tan(theta)]  # 数组
                B = [x0 + X / 2 - h, y0, z0 - Z / 2]
                points = [A, RL, B]
                return points
            elif V1 < V <= V2:
                v1 = 0.5 * X * X * Y * np.tan(theta)
                h = (V - v1) / (Y * Z)
                A = [x0 - X / 2, y0, z0 - Z / 2 + h]
                B = [x0 + X / 2, y0, z0 - Z / 2 + Z * np.tan(theta) + h]
                points = [A, LL, RL, B]
                return points
            else:
                v1 = X * Y * Z - V
                h = (2 * v1 * np.tan(theta) / Y) ** 0.5
                A = [x0 - X / 2, y0, z0 + Z / 2 - h]
                B = [x0 - X / 2 + h / np.tan(theta), y0, z0 + Z / 2]
                points = [A, LL, RL, RH, B]
                return points
        else:
            V1 = 0.5 * Z * Z * Y / np.tan(theta)
            V2 = X * Y * Z - V1
            if V <= V1:
                h = (2 * V * np.tan(theta) / Y) ** 0.5
                A = [x0 + X / 2, y0, z0 - Z / 2 + h]  # 数组
                B = [x0 + X / 2 - h / np.tan(theta), y0, z0 - Z / 2]
                points = [A, RL, B]
                return points
            elif V1 < V <= V2:
                v1 = 0.5 * Z * Z * Y / np.tan(theta)
                h = (V - v1) / (Y * Z)
                A = [x0 + X / 2 - h - Z / np.tan(theta), y0, z0 - Z / 2]
                B = [x0 + X / 2 - h, y0, z0 + Z / 2]
                points = [A, RL, RH, B]
                return points
            else:
                v1 = X * Y * Z - V
                h = (2 * v1 * np.tan(theta) / Y) ** 0.5
                A = [x0 - X / 2, y0, z0 + Z / 2 - h]
                B = [x0 - X / 2 + h / np.tan(theta), y0, z0 + Z / 2]
                points = [LL, RL, RH, B, A]
                return points

# def calc(x0, y0, z0, a, b, c, V, LH, LL, RL, RH, theta):
#     k = c / a
#     points = [LL]
#     if theta > 0:
#         if np.tan(theta) <= k:
#             v1, v2 = (a ** 2) * b * np.tan(theta) / 2, (a * b * c - (a ** 2) * b * np.tan(theta) / 2)
#             if V <= v1:
#                 h = (2 * V * np.tan(theta) / b) ** 0.5
#                 points.append([LL[0] + h / np.tan(theta), y0, LL[2]])
#                 points.append([LL[0], y0, LL[2] + h])
#             elif v1 < V <= v2:
#                 h = (2 * V - b * (c ** 2)) / (2 * c * b * np.tan(theta))
#                 points.append(RL)
#                 points.append([RL[0], y0, RL[2] + h])
#                 points.append([LL[0], y0, LL[2] + h + a * np.sin(theta)])
#             else:
#                 h = (2 * (a * b * c - V) * np.tan(theta) / b) ** 0.5
#                 points.insert(0, RL)
#                 points.append(LH)
#                 points.append([RH[0] - h / np.tan(theta), y0, RH[2]])
#                 points.append([RH[0], y0, RH[2] - h])
#         else:
#             v1, v2 = (c ** 2) * b * np.tan(theta) / 2, (a * b * c - (c ** 2) * b * np.tan(theta) / 2)
#             if V <= v1:
#                 h = (2 * V * np.tan(theta) / b) ** 0.5
#                 points.append([LL[0] + h / np.tan(theta), y0, LL[2]])
#                 points.append([LL[0], y0, LL[2] + h])
#             elif v1 < V <= v2:
#                 h = (2 * V * np.tan(theta) - b * (c ** 2)) / (2 * c * b * np.tan(theta))
#                 points.append(LH)
#                 points.append([LL[0] + h, y0, LH[2]])
#                 points.append([LL[0] + h + c / np.tan(theta), y0, LL[2]])
#             else:
#                 h = (2 * (a * b * c - V) * np.tan(theta) / b) ** 0.5
#                 points.insert(0, RL)
#                 points.append(LH)
#                 points.append([RH[0] - h / np.tan(theta), y0, RH[2]])
#                 points.append([RH[0], y0, RH[2] - h])
#     if theta < 0:
#         pass
#     return points


def tank_centroid(t, theta):  # 计算每个油箱的重心
    x0, y0, z0, X, Y, Z, V, LH, LL, RL, RH = t
    m = V * density
    if theta == 0:
        z = 0.5 * V / (X * Y) + z0 - Z / 2  #
        return [x0, y0, z, m]

    # theta = abs(theta)
    points = calc(x0, y0, z0, X, Y, Z, V, LH, LL, RL, RH, theta)

    for i in range(len(points)):
        points[i] = craft_oxyz(points[i][0], points[i][1], points[i][2], theta)
    x, y, z = get_centerpoint(points)  # 求出每个邮箱的质心坐标
    return [x, y, z, m]


def centroid(tank, theta=0):  # 计算油箱状况为tank, 倾斜角度为angle时的飞机质心
    centr = []
    for t in tank:
        centr.append(tank_centroid(t, theta))  # 计算每个油箱的质心
    centr.append([0, 0, 0, 3000])
    nx, ny, nz, mass = 0, 0, 0, 0
    for x, y, z, m in centr:  # 求 总的质心
        nx += x * m
        ny += y * m
        nz += z * m
        mass += m
    nx, ny, nz = nx / mass, ny / mass, nz / mass
    nx, ny, nz = oxyz_craft(nx, ny, nz, theta)  # 转换到飞行器坐标系
    return nx, ny, nz


if __name__ == '__main__':

    cost_list = pd.read_excel('q1_tank.xlsx')
    angle_list = pd.read_excel('q1_aircraft.xlsx')
    time = len(cost_list)
    cost_list = np.delete(cost_list.values, 0, axis=1)
    angle_list = np.delete(angle_list.values, 0, axis=1)
    for i in range(6):  # 加入油箱四个角的坐标
        for dx, dz in ((-1, 1), (-1, -1), (1, -1), (1, 1)):
            tank[i].append([tank[i][0] + 0.5 * tank[i][3] * dx, tank[i][1], tank[i][2] + 0.5 * tank[i][5] * dz])
            # 分别确定 邮箱的 四个角：左上 左下 右下 右上
    res = []
    for i in range(time):
        cost = cost_list[i]  # 变化的油量 质量
        for j in range(6):
            if cost[j] == 0: continue
            tank[j][6] -= cost[j] / density  # 变化的体积
            if j == 0:
                tank[1][6] += cost[j] / density  # 转移到2号邮箱
            elif j == 5:
                tank[4][6] += cost[j] / density  # 转移到5号邮箱
        theta = angle_list[i][0] * math.pi / 180  # 角度转弧度

        res.append(centroid(tank, theta))

    res = np.array(res)
    x, y, z = res[:, 0], res[:, 1], res[:, 2]
    fig = plt.figure()
    ax1 = plt.axes(projection='3d')
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # ax1.scatter3D(x, y, z, cmap='Blues')  # 绘制散点图
    # ax1.plot3D(x, y, z, 'gray')  # 绘制空间曲线
    ax1.plot3D(x, y, z, 'red')  # 绘制空间曲线
    ax1.scatter3D(x[0], y[0], z[0], cmap='Blues', label='初始点')
    plt.legend()
    ax1.scatter3D(x[-1], y[-1], z[-1], cmap='Blues', label='终末点')
    plt.legend()
    plt.show()
    print(max(x),min(x),max(y),min(y),max(z),min(z))
