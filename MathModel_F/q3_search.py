# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-20 15:59
 @Author  : QDY
 @FileName: q3.py
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
tank = [[8.91304348, 1.20652174, 0.61669004, 1.5, 0.9, 0.3, 1.5 * 0.9 * 0.3],
        [6.91304348, -1.39347826, 0.21669004, 2.2, 0.8, 1.1, 2.2 * 0.8 * 1.1],
        [-1.68695652, 1.20652174, -0.28330996, 2.4, 1.1, 0.9, 2.4 * 1.1 * 0.9],
        [3.11304348, 0.60652174, -0.18330996, 1.7, 1.3, 1.2, 1.7 * 1.3 * 1.2],
        [-5.28695652, -0.29347826, 0.41669004, 2.4, 1.2, 1, 2.4 * 1.2 * 1],
        [-2.08695652, -1.49347826, 0.21669004, 2.4, 1, 0.5, 2.4 * 1 * 0.5],
        ]  # tank[:3]：x,y,z ；tank[3:6]:长宽高； tank[6]:油量
rest = [0.3, 1.5, 2, 1, 1.9, 2.6, 0.8]
t2t = {0: 1, 5: 4}


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
    plt.title('问题3飞行器耗油曲线')
    plt.show()
    # plt.savefig('q2_aircraft_cost.png', dpi=800)


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


def tank_centroid(t):  # 计算每个油箱的重心
    m = t[6] * density
    z = 0.5 * t[6] / (t[3] * t[4]) + t[2] - t[5] / 2
    return [t[0], t[1], z, m]


def distance(c1, c2):
    return ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2 + (c1[2] - c2[2]) ** 2) ** 0.5


def centroid(tank):  # 计算油箱状况为tank, 倾斜角度为angle时的飞机质心
    centr = []
    for t in tank:
        if t[6] == 0: continue
        centr.append(tank_centroid(t))  # 计算每个油箱的质心
    centr.append([0, 0, 0, 3000])
    nx, ny, nz, mass = 0, 0, 0, 0
    for x, y, z, m in centr:  # 求 总的质心
        nx += x * m
        ny += y * m
        nz += z * m
        mass += m
    nx, ny, nz = nx / mass, ny / mass, nz / mass
    return [nx, ny, nz]


limit = (1.1, 1.8, 1.7, 1.5, 1.6, 1.1)


def sa(p, q, r, v, tank, target, cen):
    max_p = limit[p] / density
    max_q = limit[q] / density

    vq, vp, vrr, final = 0, 0, 0, copy.deepcopy(tank)
    dd = float('inf')
    g = v / 1000
    for i in range(1000):
        vp_ = v - g * i
        vq_ = g * i
        if vp_ > min(tank[p][6], max_p): continue
        if vq_ > min(tank[q][6], max_q): break
        tmp = copy.deepcopy(tank)
        tmp[p][6] -= vp_
        tmp[q][6] -= vq_
        tmp_cen = centroid(tmp)
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
        for i in range(1000):
            vr_ = g * i
            if vr_ > final[r][6] or vr_ + tank[t2t[r]][6] > tank[t2t[r]][3] * tank[t2t[r]][4] * tank[t2t[r]][5]: break
            tmp = copy.deepcopy(tank)
            tmp[r][6] -= vr_
            tmp[t2t[r]][6] += vr_
            tmp_cen = centroid(tmp)
            dd_ = distance(tmp_cen, target)
            if dd_ < dd:
                dd = dd_
                vrr = vr_
                cen = tmp_cen
                final = tmp
    return dd, vp, vq, vrr, cen, final


if __name__ == '__main__':
    cost_list = pd.read_excel('q3_cost.xlsx')
    target_list = pd.read_excel('q3_aircraft.xlsx')
    time = len(cost_list)
    cost_list = np.delete(cost_list.values, 0, axis=1)
    target_list = np.delete(target_list.values, 0, axis=1)
    # plot_tank_cost(np.array(cost_list))
    # plot_center(np.array(target_list))
    total = sum(cost_list)[0] / 850 + 1
    cur = centroid(tank)
    cur = centroid(tank)
    # disposable = 9.2 - sum(cost_list)  # 可丢弃的油
    target = target_list[0]
    d = distance(cur, target)
    while d > 0.01:
        d_r = []
        d_p = []
        for r_ in (0, 5):
            tmp = copy.deepcopy(tank)
            if tmp[r_][6] < 0.000001: continue
            tmp[r_][6] -= 0.0000001
            tmp[t2t[r_]][6] += 0.0000001
            d_ = distance(centroid(tmp), target)
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
            d_ = distance(centroid(tmp), target)
            d_p.append((d_, p_))
        d_p.sort()
        valid = True
        for p_i in range(len(d_p) - 1):
            for q_i in range(p_i + 1, len(d_p)):
                p, q = d_p[p_i][1], d_p[q_i][1]
                origin_tank = copy.deepcopy(tank)
                d, vp, vq, vr, cur, tank = sa(p, q, r, 0.001, tank, target, cur)
                if 0.001 / density - (vp + vq) > 0.0001:
                    valid = False
                    break
                else:
                    valid = True
                if valid:
                    break
                tank = origin_tank
            if valid: break
        sum_gas = 0
        for i in range(6):
            sum_gas += tank[i][6]
            print(tank[i][6], end=' ')
        print('\n', sum_gas, total, d)
        if sum_gas <= total: break
