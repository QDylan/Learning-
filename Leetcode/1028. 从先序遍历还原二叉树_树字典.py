# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/18 9:11
 @Author  : QDY
 @FileName: 1028. 从先序遍历还原二叉树_树字典.py

    我们从二叉树的根节点 root 开始进行深度优先搜索。
    在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。
    （如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。
    如果节点只有一个子节点，那么保证该子节点为左子节点。
    给出遍历输出 S，还原树并返回其根节点 root。

    示例 1：
    输入："1-2--3--4-5--6--7"
    输出：[1,2,5,3,4,6,7]

    示例 2：
    输入："1-2--3---4-5--6---7"
    输出：[1,2,5,3,null,6,null,4,null,7]

    示例 3：
    输入："1-401--349---90--88"
    输出：[1,401,null,349,88,90]


    提示：
    原始树中的节点数介于 1 和 1000 之间。
    每个节点的值介于 1 和 10 ^ 9 之间。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverFromPreorder(self, S):
        if not S:
            return
        len_s = len(S)
        i = 0
        while i < len_s and S[i].isdigit():  # 初始化第一个节点
            i += 1
        root = TreeNode(int(S[:i]))
        node_dict = {0: [root]}  # 树字典

        while i < len_s:
            cnt = 0
            while S[i] == '-':  # 记录'-'数量，确定其所在层数，并据此找到父节点
                i += 1
                cnt += 1
            j = i
            while i < len_s and S[i].isdigit():
                i += 1
            node = TreeNode(int(S[j:i]))
            if node_dict[cnt - 1][-1].left:  # 判断node的父节点有无左子树
                node_dict[cnt - 1][-1].right = node  # 若无，则添加node为右子树
            else:  # 否则添加node为左子树
                node_dict[cnt - 1][-1].left = node

            if cnt in node_dict:  # 加入树字典
                node_dict[cnt].append(node)
            else:
                node_dict[cnt] = [node]

        return root
