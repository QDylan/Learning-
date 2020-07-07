# -*- coding: utf-8 -*-
"""
 @Time    : 2020/6/14 21:19
 @Author  : QDY
 @FileName: 1300. 转变数组后最接近目标值的数组和_双重二分查找.py

    给你一个整数数组 arr 和一个目标值 target ，请你返回一个整数 value ，
    使得将数组中所有大于 value 的值变成 value 后，数组的和最接近  target （最接近表示两者之差的绝对值最小）。
    如果有多种使得和最接近 target 的方案，请你返回这些整数中的最小值。
    请注意，答案不一定是 arr 中的数字。

    示例 1：
    输入：arr = [4,9,3], target = 10
    输出：3
    解释：当选择 value 为 3 时，数组会变成 [3, 3, 3]，和为 9 ，这是最接近 target 的方案。

    示例 2：
    输入：arr = [2,3,5], target = 10
    输出：5

    示例 3：
    输入：arr = [60864,25176,27249,21296,20204], target = 56803
    输出：11361
     
    提示：
    1 <= arr.length <= 10^4
    1 <= arr[i], target <= 10^5

"""
import bisect


class Solution:
    def findBestValue(self, arr, target):
        arr.sort()
        length = len(arr)
        prefix = [0]
        for i in range(length):  # 前缀和
            prefix.append(prefix[-1] + arr[i])

        l, r, res = 0, arr[-1], -1  # 不超过arr[-1]
        while l <= r:  # 在[0,arr[-1]]中二分查找 最小的mid 使得 数组和最接近target
            mid = l + (r - l) // 2
            tmp = bisect.bisect_left(arr, mid)  # 在arr中找到比mid小数的最右位置
            sum_ = prefix[tmp] + (length - tmp) * mid  # 利用prefix快速计算此时的数组和
            if sum_ <= target:  # 数组和比target小，增大l以增大mid
                res = mid  # 更新res
                l = mid + 1
            else:
                r = mid - 1
        # 计算出的res是使sum_从左边逼近target的，即此时的sum_<=target

        def calc_sum(x):  # 计算数组和（大于x的置为x）
            return sum(x if num >= x else num for num in arr)
            # tmp_sum = 0
            # for i in range(length):
            #     if arr[i] < x:
            #         tmp_sum += arr[i]
            #     else:
            #         tmp_sum += x * (length - i)
            #         break
            # return tmp_sum

        sum1 = calc_sum(res)  # 数组和随着res增大是严格单调递增的
        sum2 = calc_sum(res + 1)  # 计算一次取res+1的数组和，可能更逼近于target
        return res if (target-sum1) <= abs(sum2 - target) else res + 1
