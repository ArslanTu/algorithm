#
# @lc app=leetcode.cn id=1053 lang=python3
#
# [1053] 交换一次的先前排列
#

# @lc code=start
from typing import List


class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if sorted(arr) == arr:
            return arr
        flag = [0] * n
        min_num = arr[-1]
        for i in range(n - 2, -1, -1):
            if arr[i] > min_num:
                flag[i] = 1
            else:
                min_num = arr[i]
        left = right = -1
        for i in range(n - 1, -1, -1):
            if flag[i]:
                left = i
                break
        cur_min = 0
        for i in range(left, n):
            if arr[i] < arr[left]:
                if arr[i] > cur_min:
                    right = i
                    cur_min = arr[i]
        arr[left], arr[right] = arr[right], arr[left]
        return arr
# @lc code=end

