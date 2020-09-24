# -*- coding: utf-8 -*-
"""
 @Time    : 2020-09-24 10:12
 @Author  : QDY
 @FileName: 501. 二叉搜索树中的众数.py
 @Software: PyCharm
"""
"""
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2
返回[2].

提示：如果众数超过1个，不需考虑输出顺序
进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root):
        if not root: return []
        self.res, self.res_cnt = [], 0
        self.prev_num, self.prev_cnt = None, 0

        def inorder(root):  # 中序遍历
            if not root: return
            inorder(root.left)
            if root.val == self.prev_num:
                self.prev_cnt += 1
            else:
                if self.prev_cnt > 0:
                    if self.prev_cnt == self.res_cnt:
                        self.res.append(self.prev_num)
                    elif self.prev_cnt > self.res_cnt:
                        self.res_cnt = self.prev_cnt
                        self.res = [self.prev_num]
                self.prev_num = root.val
                self.prev_cnt = 1

            inorder(root.right)

        inorder(root)
        if self.prev_cnt > 0:
            if self.prev_cnt == self.res_cnt:
                self.res.append(self.prev_num)
            elif self.prev_cnt > self.res_cnt:
                self.res_cnt = self.prev_cnt
                self.res = [self.prev_num]

        return self.res
