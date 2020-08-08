# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/8 11:01
 @Author  : QDY
 @FileName: 99. 恢复二叉搜索树.py
 @Software: PyCharm
"""
"""
二叉搜索树中的两个节点被错误地交换。

请在不改变其结构的情况下，恢复这棵树。

示例 1:

输入: [1,3,null,null,2]

   1
  /
 3
  \
   2

输出: [3,1,null,null,2]

   3
  /
 1
  \
   2
示例 2:

输入: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

输出: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
进阶:

使用 O(n) 空间复杂度的解法很容易实现。
你能想出一个只使用常数空间的解决方案吗？

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        # Morris 遍历 空间O(1)
        # 1.若root无左节点，则访问右节点
        # 2.若root有左节点，则找到root的左子树中最右的节点predecessor(root在中序遍历中的前一个节点)
        #   2.1 若predecessor的右子树为空，则将其指向root，然后访问root.left
        #   2.2 若predecessor的右子树不为空，则此时其右子树指向root，说明已经遍历完了root的左子树，这时令predecessor.right=None
        #       然后访问root.rigth
        # 重复上述操作，直至root is None
        prev, x, y = None, None, None
        while root:
            if root.left:
                predecessor = root.left  # 当前root的前一个节点
                while predecessor.right and predecessor.right != root:  # 找到root.left最右节点
                    predecessor = predecessor.right
                if not predecessor.right:
                    predecessor.right = root  # 让predecessor的右子树指向root
                    root = root.left  # 继续遍历左子树
                else:  # 说明左子树已访问完了
                    if prev and root.val < prev.val:
                        y = root
                        if not x:
                            x = prev
                    prev = root
                    predecessor.right = None  # 断开
                    root = root.right
            else:  # 若无左子树，则直接访问右子树
                if prev and root.val < prev.val:
                    y = root
                    if not x:
                        x = prev
                prev = root
                root = root.right
        x.val, y.val = y.val, x.val

        # node, val = [], []  # 中序遍历，空间O(N)
        # cur,stack = root, []
        # while cur or stack:
        #     if cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     else:
        #         cur = stack.pop()
        #         val.append(cur.val)
        #         node.append(cur)
        #         cur = cur.right
        # val.sort()
        # for i in range(len(node)):
        #     node[i].val = val[i]
