# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/5 9:25
 @Author  : QDY
 @FileName: 42. 接雨水_双指针.py

    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，
    下雨之后能接多少雨水。


    示例:
    输入: [0,1,0,2,1,0,1,3,2,1,2,1]
    输出: 6

"""


class Solution:
    def trap(self, height):
        length = len(height)
        if length <= 1:
            return 0
        res = 0

        # 维护一个单调下降的栈(栈中保存的是id)
        # stack = [0]
        # for i in range(1, length):
        #     # height[i]>栈中最小元素时->找到空隙, i为右边界
        #     while stack and height[stack[-1]]<height[i]:
        #         cur_id = stack.pop()  # 间隙中柱子
        #         # 如果栈顶元素一直相等，那么全都pop出去，只留第一个(与i最近的)id
        #         while stack and height[stack[-1]]==height[cur_id]:
        #             stack.pop()
        #         if stack:
        #             left = stack[-1]  # 指向左边界
        #             # 高度：取左右两边界高度的最小值 - 中间柱子高度
        #             # 宽度：i-left-1
        #             res += (min(height[left],height[i])-height[cur_id])*(i-left-1)
        #     stack.append(i)
        #     # print(stack)

        # 双指针
        # 位置i处能接的雨水=min(i左侧的最大高度，i右侧的最大高度) - height[i]
        left, left_max, right, right_max = 0, 0, length - 1, 0
        while left < right:  # 每次只移动高度较小的指针，边走边算
            if height[left] < height[right]:
                if height[left] >= left_max:  # 当left当前高度 不小于 左侧最高高度时，说明left处不能接雨水
                    left_max = height[left]   # 同时更新左侧最高高度
                else:  # 当left当前高度 小于 左侧最高高度时，说明left处可以接雨水
                    res += left_max - height[left]  # left_max<right_max,所以left处接水高度只与left_max有关
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    res += right_max - height[right]
                right -= 1

        return res
