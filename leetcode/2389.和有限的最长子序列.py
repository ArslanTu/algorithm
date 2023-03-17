#
# @lc app=leetcode.cn id=2389 lang=python3
#
# [2389] 和有限的最长子序列
#

# @lc code=start
from bisect import bisect_right
from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return [bisect_right(nums, q) for q in queries]
# @lc code=end

