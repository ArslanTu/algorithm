#
# @lc app=leetcode.cn id=1630 lang=python3
#
# [1630] 等差子数组
#

# @lc code=start
from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # 暴力？
        ans = []
        for i in range(len(l)):
            if l[i] + 1 == r[i]:
                ans.append(True)
                continue
            flag = True
            arr = sorted(nums[l[i]:r[i] + 1])
            for j in range(2, len(arr)):
                if arr[j] - arr[j - 1] != arr[1] - arr[0]:
                    flag = False
                    break
            ans.append(flag)
        return ans

# @lc code=end

