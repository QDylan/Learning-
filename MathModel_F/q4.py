# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-20 22:28
 @Author  : QDY
 @FileName: q4.py
 @Software: PyCharm
"""
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
import copy
import time

aircraft = [0, 0, 0]
M = 3000
density = 850
tank = [[8.91304348, 1.20652174, 0.61669004, 1.5, 0.9, 0.3, 0.3],
        [6.91304348, -1.39347826, 0.21669004, 2.2, 0.8, 1.1, 1.5],
        [-1.68695652, 1.20652174, -0.28330996, 2.4, 1.1, 0.9, 2.1],
        [3.11304348, 0.60652174, -0.18330996, 1.7, 1.3, 1.2, 1.9],
        [-5.28695652, -0.29347826, 0.41669004, 2.4, 1.2, 1, 2.6],
        [-2.08695652, -1.49347826, 0.21669004, 2.4, 1, 0.5, 0.8],
        ]  # tank[:3]：x,y,z ；tank[3:6]:长宽高； tank[6]:油量
rest = [0.3, 1.5, 2, 1, 1.9, 2.6, 0.8]
t2t = {0: 1, 5: 4}


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


def plot_tank_cost(c):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # t1, t2, t3, t4, t5, t6 = c[:, 0], c[:, 1], c[:, 2], c[:, 3], c[:, 4], c[:, 5]
    x = np.arange(0, 7200)
    plt.plot(x, c, label='耗油速度')
    # plt.plot(x, t1,label='油箱1',color='black')
    # plt.plot(x, t2, label='油箱2')
    # plt.plot(x, t3, label='油箱3')
    # plt.plot(x, t4, label='油箱4')
    # plt.plot(x, t5, label='油箱5')
    # plt.plot(x, t6, label='油箱6')
    plt.xlabel('飞行时间(s)')
    plt.ylabel('飞行器耗油速度(kg/s)')
    plt.title('问题4飞行器耗油曲线')
    plt.show()
    # plt.savefig('q2_aircraft_cost.png', dpi=800)


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
    nx, ny, nz = 0.0, 0.0,0.0
    for i in range(len(points)):
        nx += points[i][0]
        ny += points[i][1]
        nz += points[i][2]

    nx = nx / len(points)
    ny = ny / len(points)
    nz = nz / len(points)

    return nx, ny, nz


def plot_center(centers):
    fig = plt.figure()
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    ax1 = plt.axes(projection='3d')
    # ax1.scatter3D(x, y, z, cmap='Blues')  # 绘制散点图
    x, y, z = centers[:, 0], centers[:, 1], centers[:, 2]
    ax1.plot3D(x, y, z, 'black')  # 绘制空间曲线
    ax1.scatter3D(centers[0][0], centers[0][1], centers[0][2], cmap='Blues', label='理想起点')
    plt.legend()
    ax1.scatter3D(centers[-1][0], centers[-1][1], centers[-1][2], cmap='Blues', label='理想终点')
    plt.legend()
    plt.show()
    # plt.savefig('ideal.png', dpi=800)


def tank_centroid(t, theta):  # 计算每个油箱的重心
    x0, y0, z0, X, Y, Z, V, LH, LL, RL, RH = t
    m = V * density
    if theta == 0:
        z = 0.5 * V / (X * Y) + z0 - Z / 2  #
        return [x0, y0, z, m]

    # theta = abs(theta)
    points = calc(x0, y0, z0, X, Y, Z, V, LH, LL, RL, RH, theta)
    x, y, z = get_centerpoint(points)  # 求出每个邮箱的质心坐标
    return [x, y, z, m]


def centroid(tank, theta):  # 计算油箱状况为tank, 倾斜角度为angle时的飞机质心
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
    return nx, ny, nz


def plot(Y, lim, i):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    X = np.arange(0, len(Y))
    fig = plt.figure()
    plt.plot(X, Y)
    plt.plot(X, [(lim / 850) + 0.000001] * len(Y), label='输油上限')
    plt.xlabel('飞行时间(秒)')
    plt.ylabel('油箱%s耗油量(立方米/秒)' % (i + 1))
    plt.legend()
    plt.show()


def distance(c1, c2):
    return ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2 + (c1[2] - c2[2]) ** 2) ** 0.5


limit = (1.1, 1.8, 1.7, 1.5, 1.6, 1.1)


def sa(p, q, r, v, tank, target, cen, theta):
    max_p = limit[p] / density
    max_q = limit[q] / density

    vq, vp, vrr, final = 0, 0, 0, copy.deepcopy(tank)
    dd = float('inf')
    g = v / 1000
    for i in range(1,999):
        vp_ = v - g * i
        vq_ = g * i
        if vp_ > min(tank[p][6], max_p): continue
        if vq_ > min(tank[q][6], max_q): break
        tmp = copy.deepcopy(tank)
        tmp[p][6] -= vp_
        tmp[q][6] -= vq_
        tmp_cen = centroid(tmp, theta)
        dd_ = distance(tmp_cen, target)
        if dd_ < dd:
            dd = dd_
            vp = vp_
            vq = vq_
            cen = tmp_cen
            final = tmp
    tank = copy.deepcopy(final)
    if r is not None:
        g = limit[r] / (1000 * density)
        for i in range(1,1000):
            vr_ = g * i
            if vr_ > final[r][6] or vr_ + tank[t2t[r]][6] > tank[t2t[r]][3] * tank[t2t[r]][4] * tank[t2t[r]][5]: break
            tmp = copy.deepcopy(tank)
            tmp[r][6] -= vr_
            tmp[t2t[r]][6] += vr_
            tmp_cen = centroid(tmp, theta)
            dd_ = distance(tmp_cen, target)
            if dd_ < dd:
                dd = dd_
                vrr = vr_
                cen = tmp_cen
                final = tmp
    return dd, vp, vq, vrr, cen, final


if __name__ == '__main__':
    cost_list = pd.read_excel('q4_cost.xlsx')
    angle_list = pd.read_excel('q4_angle.xlsx')
    time = len(cost_list)
    cost_list = np.delete(cost_list.values, 0, axis=1)
    angle_list = np.delete(angle_list.values, 0, axis=1)
    for i in range(6):  # 加入油箱四个角的坐标
        for dx, dz in ((-1, 1), (-1, -1), (1, -1), (1, 1)):
            tank[i].append([tank[i][0] + 0.5 * tank[i][3] * dx, tank[i][1], tank[i][2] + 0.5 * tank[i][5] * dz])
    V = np.zeros([time, 6])
    cur = centroid(tank, angle_list[0][0])
    res_centroid = []
    res_dis = []
    target = [0, 0, 0]
    for i in range(time // 60):
        i1, i2 = i * 60, i * 60 + 59
        d = distance(cur, target)
        d_r = []
        d_p = []
        tmp_theta = angle_list[i2]
        for r_ in (0, 5):
            tmp = copy.deepcopy(tank)
            if tmp[r_][6] < 0.000001: continue
            tmp[r_][6] -= 0.0000001
            tmp[t2t[r_]][6] += 0.0000001
            d_ = distance(centroid(tmp, tmp_theta), target)
            d_r.append((d_, r_))
        if d_r:
            d_r.sort()
            r = d_r[0][1]
        else:
            r = None
        for p_ in range(1, 5):
            if tank[p_][6] < 0.0000001: continue
            tmp = copy.deepcopy(tank)
            tmp[p_][6] -= 0.0000001
            d_ = distance(centroid(tmp, tmp_theta), target)
            d_p.append((d_, p_))
        d_p.sort()
        valid = True
        for p_i in range(len(d_p) - 1):
            for q_i in range(p_i + 1, len(d_p)):
                p, q = d_p[p_i][1], d_p[q_i][1]
                origin_tank = copy.deepcopy(tank)
                for ii in range(i1, i2 + 1):
                    # if ii > 5900 and cost_list[ii][0] == 0:
                    #     cost = disposable / 2200
                    cost = cost_list[ii][0]
                    # prev = copy.deepcopy(tank)
                    theta = angle_list[ii][0]
                    if theta == 0 and cost == 0:
                        vp,vr,vq = 0,0,0
                        d = distance(cur,target)
                    else:
                        d, vp, vq, vr, cur, tank = sa(p, q, r, cost / density, tank, target, cur, theta)
                    V[ii][p] = vp
                    V[ii][q] = vq
                    V[ii][r] = vr  # prev[r][6] - tank[r][6]
                    res_centroid.append(cur)
                    res_dis.append(d)
                if valid:
                    break
                tank = origin_tank
            if valid: break
        if not valid: print(ii, '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('time=%s~%s' % (i1, i2), max(res_dis[i1:i2 + 1]),theta)
        if r is not None: print(r, sum(V[:, r]))

        for jj in range(6):
            print(tank[jj][6], end=' ')
        print('\n')
    print(max(res_dis))
    cc = []
    for i in range(len(cost_list)):
        cc.append(cost_list[i][0] / 850)
    Y = []
    for i in range((len(V))):
        Y.append(V[i][1]+V[i][2]+V[i][3]+V[i][4])
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    X = np.arange(0, len(Y))
    fig = plt.figure()
    plt.plot(X, Y,label='主油箱总供油速度曲线')
    plt.legend()
    plt.plot(X,cc,label='问题4计划耗油速度曲线')
    plt.legend()
    plt.xlabel('飞行时间(秒)')
    plt.ylabel('耗油量(立方米/秒)')
    plt.legend()
    plt.show()