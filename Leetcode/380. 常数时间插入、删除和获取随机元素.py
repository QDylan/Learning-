# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/2 16:52
 @Author  : QDY
 @FileName: 380. 常数时间插入、删除和获取随机元素.py

    设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。

    insert(val)：当元素 val 不存在时，向集合中插入该项。
    remove(val)：元素 val 存在时，从集合中移除该项。
    getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。
    示例 :

    // 初始化一个空的集合。
    RandomizedSet randomSet = new RandomizedSet();

    // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
    randomSet.insert(1);

    // 返回 false ，表示集合中不存在 2 。
    randomSet.remove(2);

    // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
    randomSet.insert(2);

    // getRandom 应随机返回 1 或 2 。
    randomSet.getRandom();

    // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
    randomSet.remove(1);

    // 2 已在集合中，所以返回 false 。
    randomSet.insert(2);

    // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
    randomSet.getRandom();

"""
import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        哈希表+列表
        """
        self.Dict = {}
        self.List = []
        self.Len = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        用哈希表判断val是否已存在，若无，则在列表中append(val)，哈希表[val]=len(list)-1
        """
        if val not in self.Dict:
            self.Dict[val] = self.Len
            self.List.append(val)
            self.Len += 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        若val在哈希表中，利用对应键值，找到其在List中的位置，用最后一个元素存入这个位置，删除列表最后一项，同时更新哈希表
        """
        if val not in self.Dict:
            return False
        else:
            val_id = self.Dict[val]
            del self.Dict[val]
            if val_id == self.Len - 1:
                self.List.pop()
            else:
                self.List[val_id] = self.List.pop()
                self.Dict[self.List[val_id]] = val_id
            self.Len -= 1
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.List)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
