# -*- coding: utf-8 -*-
"""
 @Time    : 2020/7/20 9:30
 @Author  : QDY
 @FileName: 5467. 找到最接近目标值的函数值_hard.py

    def func(arr,l,r):
        if r<l:
            return -10000000000
        ans = arr[l]
        for i in range(l+1,r+1):
            ans = ans & arr[i]
        return ans

    Winston 构造了一个如上所示的函数 func 。他有一个整数数组 arr 和一个整数 target ，
    他想找到让 |func(arr, l, r) - target| 最小的 l 和 r 。
    请你返回 |func(arr, l, r) - target| 的最小值。
    请注意， func 的输入参数 l 和 r 需要满足 0 <= l, r < arr.length 。

    示例 1：
    输入：arr = [9,12,3,7,15], target = 5
    输出：2
    解释：所有可能的 [l,r] 数对包括 [[0,0],[1,1],[2,2],[3,3],[4,4],[0,1],[1,2],[2,3],[3,4],[0,2],[1,3],[2,4],[0,3],[1,4],[0,4]]，
     Winston 得到的相应结果为 [9,12,3,7,15,8,0,3,7,0,0,3,0,0,0] 。最接近 5 的值是 7 和 3，所以最小差值为 2 。

    示例 2：
    输入：arr = [1000000,1000000,1000000], target = 1
    输出：999999
    解释：Winston 输入函数的所有可能 [l,r] 数对得到的函数值都为 1000000 ，所以最小差值为 999999 。

    示例 3：
    输入：arr = [1,2,4,8,16], target = 0
    输出：0
     
    提示：
    1 <= arr.length <= 10^5
    1 <= arr[i] <= 10^6
    0 <= target <= 10^7

"""


class Solution:
    def closestToTarget(self, arr, target):
        # 实际上求的是 arr[l] 到 arr[r] 的「按位与之和」，也就是 arr[l] & arr[l+1] & ... & arr[r-1] & arr[r]
        # 如果我们固定右端点 r，并且从大到小在 [0, r] 的区间内枚举左端点 l，那么这个按位与之和是单调递减的。
        # 这个和最多只有 20 种
        res = abs(arr[0] - target)
        valid = {arr[0]}
        for num in arr:  # 以num作为右边界，arr[l]~arr[r]所有组合的&的结果存入valid中
            valid = {x & num for x in valid} | {num}
            res = min(res, min(abs(x - target) for x in valid))
        return res
