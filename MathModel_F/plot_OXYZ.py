# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-18 10:55
 @Author  : QDY
 @FileName: plot_OXYZ.py
 @Software: PyCharm
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_cuboid(center, size, ax, cor, i):
    """
       Create a data array for cuboid plotting.
       ============= ================================================
       Argument      Description
       ============= ================================================
       center        center of the cuboid, triple
       size          size of the cuboid, triple, (x_length,y_width,z_height)
       :type size: tuple, numpy.array, list
       :param size: size of the cuboid, triple, (x_length,y_width,z_height)
       :type center: tuple, numpy.array, list
       :param center: center of the cuboid, triple, (x,y,z)
   """
    # suppose axis direction: x: to left; y: to inside; z: to upper
    # get the (left, outside, bottom) point

    ox, oy, oz = center
    l, w, h = size
    x = np.linspace(ox - l / 2, ox + l / 2, num=10)
    y = np.linspace(oy - w / 2, oy + w / 2, num=10)
    z = np.linspace(oz - h / 2, oz + h / 2, num=10)
    x1, z1 = np.meshgrid(x, z)
    y11 = np.ones_like(x1) * (oy - w / 2)
    y12 = np.ones_like(x1) * (oy + w / 2)
    x2, y2 = np.meshgrid(x, y)
    z21 = np.ones_like(x2) * (oz - h / 2)
    z22 = np.ones_like(x2) * (oz + h / 2)
    y3, z3 = np.meshgrid(y, z)
    x31 = np.ones_like(y3) * (ox - l / 2)
    x32 = np.ones_like(y3) * (ox + l / 2)

    # outside surface
    ax.plot_wireframe(x1, y11, z1, color=cor, rstride=1, cstride=1, alpha=0.6, label='油箱%s' % (i + 1))
    plt.legend()
    # inside surface
    ax.plot_wireframe(x1, y12, z1, color=cor, rstride=1, cstride=1, alpha=0.6)
    # bottom surface
    ax.plot_wireframe(x2, y2, z21, color=cor, rstride=1, cstride=1, alpha=0.6)
    # upper surface
    ax.plot_wireframe(x2, y2, z22, color=cor, rstride=1, cstride=1, alpha=0.6)
    # left surface
    ax.plot_wireframe(x31, y3, z3, color=cor, rstride=1, cstride=1, alpha=0.6)
    # right surface
    ax.plot_wireframe(x32, y3, z3, color=cor, rstride=1, cstride=1, alpha=0.6)
    ax.plot3D(np.arange(-11, 11), [0] * 22, [0] * 22, 'gray')
    ax.plot3D([0] * 8, np.arange(-4, 4), [0] * 8, 'gray')
    ax.plot3D([0] * 22, [0] * 22, np.arange(-11, 11), 'gray')
    ax.set_xlabel('X')
    ax.set_xlim(-10, 10)
    ax.set_ylabel('Y')
    ax.set_ylim(-3, 3)
    ax.set_zlabel('Z')
    ax.set_zlim(-10, 10)


tank = [[8.91304348, 1.20652174, 0.61669004, 1.5, 0.9, 0.3, 0.3],
        [6.91304348, -1.39347826, 0.21669004, 2.2, 0.8, 1.1, 1.5],
        [-1.68695652, 1.20652174, -0.28330996, 2.4, 1.1, 0.9, 2.1],
        [3.11304348, 0.60652174, -0.18330996, 1.7, 1.3, 1.2, 1.9],
        [-5.28695652, -0.29347826, 0.41669004, 2.4, 1.2, 1, 2.6],
        [-2.08695652, -1.49347826, 0.21669004, 2.4, 1, 0.5, 0.8],
        ]

if __name__ == '__main__':
    fig = plt.figure()
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    colors = ['b', 'k', 'r', 'y', 'c', 'g']
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter3D([0], [0], [0])
    for i, t in enumerate(tank):
        plot_cuboid(t[:3], t[3:6], ax, colors[i], i)
    target_list = pd.read_excel('q2_aircraft.xlsx')
    centers = np.array(np.delete(target_list.values, 0, axis=1))
    x, y, z = centers[:, 0], centers[:, 1], centers[:, 2]
    ax.plot3D(x, y, z, 'gray')  # 绘制空间曲线
    ax.scatter3D(centers[0][0], centers[0][1], centers[0][2], cmap='Blues', label='起点')
    plt.legend()
    ax.scatter3D(centers[-1][0], centers[-1][1], centers[-1][2], cmap='Blues', label='终点')
    plt.legend()
    # ax = plt.axes(projection='3d')
    # ax.scatter3D([0],[0],[0],)  # 绘制散点图
    # plt.savefig('tanks.png', dpi=800)
    plt.show()
