# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/14 14:28
 @Author  : QDY
 @FileName: 432. 全 O(1) 的数据结构.py

    请你实现一个数据结构支持以下操作：

    Inc(key) - 插入一个新的值为 1 的 key。或者使一个存在的 key 增加一，保证 key 不为空字符串。
    Dec(key) - 如果这个 key 的值是 1，那么把他从数据结构中移除掉。否则使一个存在的 key 值减一。
               如果这个 key 不存在，这个函数不做任何事情。key 保证不为空字符串。
    GetMaxKey() - 返回 key 中值最大的任意一个。如果没有元素存在，返回一个空字符串"" 。
    GetMinKey() - 返回 key 中值最小的任意一个。如果没有元素存在，返回一个空字符串""。
     

    挑战：
    你能够以 O(1) 的时间复杂度实现所有操作吗？

"""


class Node:  # 双向链表
    def __init__(self, val):
        self.val = val
        self.key_set = set()
        self.prev = None
        self.next = None


class AllOne:
    """
    双链表+两个哈希表
    链表中的每个节点按node.val从小到大排序，node.key_set包含所有val==node.val的key

    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(-float('inf'))  # 伪头节点，next指向最小值
        self.tail = Node(float('inf'))  # 伪尾结点，prev指向最大值
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_val = {}  # key:键值
        self.val_key = {}  # val:键值为val的key组成的Node

    def add_node(self, new_node, prev_node):
        # 在prev_node后面插入new_node
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def remove_node_from_list(self, node):
        # 把node从链表中删除
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

    def remove_from_node(self, cur_node, key):
        # 把key从cur_node的key_set中删除
        cur_node.key_set.remove(key)
        if not cur_node.key_set:  # 若删除key后，该节点无任何键值
            self.remove_node_from_list(cur_node)  # 则还要从链表中删除该节点
            self.val_key.pop(cur_node.val)  # 将键值为cur_node.val的节点也删去

    def change(self, key, c):
        # 改变key对应的值，使其+c,c=1or-1
        prev_val = self.key_val[key]
        self.key_val[key] += c
        cur_node = self.val_key[prev_val]  # 原本val的节点
        new_node = None
        if self.key_val[key] in self.val_key:  # 若存在val+1的节点，则直接取出
            new_node = self.val_key[self.key_val[key]]
        else:
            new_node = Node(self.key_val[key])  # 新建结点
            self.val_key[self.key_val[key]] = new_node  # 将新节点存入self.val_key中
            # 在链表中插入结点，若是+1,则在cur_node后插入，若是-1，则在cur_node前插入
            self.add_node(new_node, cur_node if c == 1 else cur_node.prev)
        new_node.key_set.add(key)  # 添加key到该Node的key_set种
        self.remove_from_node(cur_node, key)  # 从旧节点中删除key

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.key_val:
            self.key_val[key] = 1
            if self.head.next.val != 1:  # 若最小节点的值不为1，则在头节点处插入
                self.add_node(Node(1), self.head)
            self.head.next.key_set.add(key)
            self.val_key[1] = self.head.next
        else:
            self.change(key, 1)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.key_val:
            val = self.key_val[key]
            if val == 1:  # 原键值为1，要把这个key删掉
                self.key_val.pop(key)
                self.remove_from_node(self.val_key[val], key)
            else:
                self.change(key, -1)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """

        return next(iter(self.tail.prev.key_set)) if self.key_val else ''

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return next(iter(self.head.next.key_set)) if self.key_val else ''

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
