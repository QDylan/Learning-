# -*- coding: utf-8 -*-
"""
 @Time    : 2020-03-24 10:48
 @Author  : QDY
 @FileName: Tree.py
 @Software: PyCharm
"""


class Tree(object):
    class __Node(object):
        def __init__(self, item, left=None, right=None):
            self.item = item
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def add(self, item):
        node = self.__Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)
            if cur_node.left is None:
                # print("add")
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)

            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)

    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return None
        queue = [self.root]
        # print(queue)
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.item, end=" ")
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)

    def preorder_travel(self, root=None):
        """先序遍历：根→左→右"""
        if root is None:
            return
        print(root.item, end=" ")
        self.preorder_travel(root.left)
        self.preorder_travel(root.right)

    def midorder_travel(self, root=None):
        """中序遍历：左→根→右"""
        if root is None:
            return
        self.midorder_travel(root.left)
        print(root.item, end=" ")
        self.midorder_travel(root.right)

    def postorder_travel(self, root=None):
        """后序遍历：左→右→根"""
        if root is None:
            return

        self.postorder_travel(root.left)
        self.postorder_travel(root.right)
        print(root.item, end=" ")

    def pre_travel(self):
        if not self.root: return
        cur, stack, res = self.root, [], []
        while cur or stack:
            if cur:
                res.append(cur.item)
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop().right
        return res

    def mid_travel(self):
        if not self.root: return
        cur, stack, res = self.root, [], []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                node = stack.pop()
                res.append(node.item)
                cur = node.right
        return res

    def post_travel(self):
        if not self.root: return
        cur, stack, res = self.root, [], []
        while cur or stack:  # 按 根右左输出 为后序遍历的逆序
            if cur:
                res.append(cur.item)
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop().left
        return res[::-1]


class Solution:
    """
    110. 给定一个二叉树，判断它是否是高度平衡的二叉树。

    本题中，一棵高度平衡二叉树定义为：

    一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
    """

    def balanced(self, root):
        if root is None:
            return 0
        left = self.balanced(root.left)
        if left == -1:
            return -1
        right = self.balanced(root.right)
        if right == -1:
            return -1

        if -1 <= left - right <= 1:
            return 1 + max(left, right)
        else:
            return -1

    def isBalanced(self, root):
        return self.balanced(root) != -1


if __name__ == '__main__':
    t = Tree()
    for i in range(10):
        t.add(i)
    t.breadth_travel()
    print("\n---------------------")
    t.preorder_travel(t.root)
    print('\n', t.pre_travel())
    print("\n---------------------")
    t.midorder_travel(t.root)
    print('\n', t.mid_travel())
    print("\n---------------------")
    t.postorder_travel(t.root)
    print('\n', t.post_travel())
    print("\n---------------------")
