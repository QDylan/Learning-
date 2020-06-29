# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/29 16:34
 @Author  : QDY
 @FileName: 315. 计算右侧小于当前元素的个数_归并排序_Hard.py

    给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质：
    counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

    示例:

    输入: [5,2,6,1]
    输出: [2,1,1,0]
    解释:
    5 的右侧有 2 个更小的元素 (2 和 1).
    2 的右侧仅有 1 个更小的元素 (1).
    6 的右侧有 1 个更小的元素 (1).
    1 的右侧有 0 个更小的元素.

"""


class TreeNode(object):
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item
        self.count = 0  # 记录左子树数量


class Solution:
    # 二叉搜索树
    def countSmaller(self, nums):
        length = len(nums)
        nums = [(i, nums[i]) for i in range(length)]  # 索引数组
        self.res = [0] * length  # 记录每个位置的逆序数

        def merge_sort(nums):
            length = len(nums)
            if length <= 1:
                return nums
            mid = length // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            l_id, r_id, pos = 0, 0, 0
            while pos < length:  # 对于left中的每个元素,计算在right中有多少个数比它小
                if r_id == length - mid or (
                        l_id < mid and left[l_id][1] <= right[r_id][1]):  # right中r_id之前的元素都要比left[l_id]小
                    self.res[left[l_id][0]] += r_id  # 更新left[l_id]的逆序数
                    nums[pos] = left[l_id]
                    l_id += 1
                else:
                    nums[pos] = right[r_id]
                    r_id += 1
                # print(self.res)
                pos += 1
            return nums

        merge_sort(nums)
        return self.res

        # length = len(nums)
        # root = None
        # self.res = [0]*length
        # # 插入节点并更新res
        # def insert_node(root, val, index):
        #     if not root:
        #         root = TreeNode(val)
        #         return root
        #     if val <= root.val:  # 小于当前节点值放入左子树
        #         root.count += 1
        #         root.left = insert_node(root.left,val,index)
        #     else:  # 大于放入右子树
        #         self.res[index] += root.count + 1
        #         # 递归
        #         root.right = insert_node(root.right,val,index)
        #     return root

        # for i in range(length-1,-1,-1):
        #     root = insert_node(root,nums[i],i)
        # return self.res
