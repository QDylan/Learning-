# -*- coding: utf-8 -*-
"""
 @Time    : 2020/8/18 10:48
 @Author  : QDY
 @FileName: 137. 只出现一次的数字 II.py
 @Software: PyCharm
"""
"""
    给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
    说明：
    你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
    
    示例 1:
    输入: [2,2,3,2]
    输出: 3
    
    示例2:
    输入: [0,1,0,1,0,1,99]
    输出: 99

"""


class Solution:
    def singleNumber(self, nums) -> int:
        once, twice = 0, 0  # 记录出现了一次和两次的异或
        for x in nums:
            # x & ~x == 0 ; x & ~0 = x  在x出现第三次时，抵消为0
            once = (once ^ x) & ~twice
            twice = (twice ^ x) & ~once
        return once
