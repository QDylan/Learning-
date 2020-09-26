# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-18 9:14
 @Author  : QDY
 @FileName: q2.py
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


def tank_centroid(t):  # 计算每个油箱的重心
    m = t[6] * density
    z = 0.5 * t[6] / (t[3] * t[4]) + t[2] - t[5] / 2
    return [t[0], t[1], z, m]


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


def distance(c1, c2):
    return ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2 + (c1[2] - c2[2]) ** 2) ** 0.5


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
    plt.title('问题2飞行器耗油曲线')
    plt.savefig('q2_aircraft_cost.png', dpi=800)


def plot_center(centers, real):
    fig = plt.figure()
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    ax1 = plt.axes(projection='3d')
    # ax1.scatter3D(x, y, z, cmap='Blues')  # 绘制散点图
    x, y, z = centers[:, 0], centers[:, 1], centers[:, 2]
    ax1.plot3D(x, y, z, 'gray')  # 绘制空间曲线
    ax1.scatter3D(centers[0][0], centers[0][1], centers[0][2], cmap='Blues', label='理想起点')
    plt.legend()
    ax1.scatter3D(centers[-1][0], centers[-1][1], centers[-1][2], cmap='Blues', label='理想终点')
    plt.legend()
    x, y, z = real[:, 0], real[:, 1], real[:, 2]
    ax1.plot3D(x, y, z, 'black')  # 绘制空间曲线
    ax1.scatter3D(real[0][0], real[0][1], real[0][2], cmap='Blues', label='实际起点')
    plt.legend()
    ax1.scatter3D(real[-1][0], real[-1][1], real[-1][2], cmap='Blues', label='实际终点')
    plt.legend()
    # plt.title('问题2飞行器理想质心变化曲线')
    plt.show()
    # plt.savefig('ideal.png', dpi=800)


limit = (1.1, 1.8, 1.7, 1.5, 1.6, 1.1)
select = [(1, 2, 5), (1, 3, 5), (1, 4, 5), (2, 3, 0), (2, 3, 5), (2, 4, 0), (3, 4, 0)]
t2t = {0: 1, 5: 4}


def sa(p, q, r, v, tank, target, cen):
    # global disposable
    max_p = limit[p] / density
    max_q = limit[q] / density
    max_r = limit[r] / density
    vq, vp, vr, final = 0, 0, 0, tank
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

    for i in range(1000):
        vr_ = max_r * i / 1000
        if vr_ > tank[r][6] and vr+tank[t2t[r]][6]>tank[t2t[r]][3]*tank[t2t[r]][4]*tank[t2t[r]][5]: break
        tmp = copy.deepcopy(tank)
        tmp[r][6] -= vr_
        tmp[t2t[r]][6] += vr_
        tmp_cen = centroid(tmp)
        dd_ = distance(tmp_cen, target)
        if dd_ < dd:
            dd = dd_
            vr = vr_
            cen = tmp_cen
            final = tmp
    return dd, vp, vq, vr, cen, final


if __name__ == '__main__':
    cost_list = pd.read_excel('q2_cost.xlsx')
    target_list = pd.read_excel('q2_aircraft.xlsx')
    time = len(cost_list)
    cost_list = np.delete(cost_list.values, 0, axis=1)
    target_list = np.delete(target_list.values, 0, axis=1)
    V = np.zeros([time, 6])
    cur = centroid(tank)
    disposable = 9.2 - sum(cost_list)  # 可丢弃的油
    res_centroid = []
    res_dis = []
    for i in range(time // 60):
        i1, i2 = i * 60, i * 60 + 59
        target = target_list[i2]
        d = distance(cur, target)
        dx, dy, dz = target[0] - cur[0], target[1] - cur[1], target[2] - cur[2]
        # tmp_v = sum(cost_list[i1:i2]) / density
        check = []
        # cost_sum = sum(cost_list[i1:i1 + 60]) / density
        if dy >= 0:
            if tank[4] >= tank[2]:
                p_ = 4
            else:
                p_ = 2
        else:
            if tank[3] >= tank[1]:
                p_ = 3
            else:
                p_ = 1
        for q_ in range(1, 5):
            if q_ == p_: continue
            for r_ in (0, 5):
                tmp = copy.deepcopy(tank)
                dd, vp, vq, vr, cur, tmp = sa(p_, q_, r_, 0.0001, tmp, target, cur)
                check.append((dd, p_, q_, r_))
        check.sort(key=lambda x: x[0])
        dd, p, q, r = check[0]
        for ii in range(i1, i2 + 1):
            d, vp, vq, vr, cur, tank = sa(p, q, r, cost_list[ii][0] / density, tank, target, cur)
            V[ii][p] = vp
            V[ii][q] = vq
            V[ii][r] = vr
            if cost_list[ii][0] / density - (vp + vq) > 0.0001: print(ii)
            res_centroid.append(cur)
            res_dis.append(d)
        print('time=%s~%s' % (i1, i2), max(res_dis[i1:i2 + 1]))

    # print(P)

    # plot_tank_cost(np.array(cost_list))
    plot_center(np.array(target_list), np.array(res_centroid))
