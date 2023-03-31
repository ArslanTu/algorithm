#
# @lc app=leetcode.cn id=2367 lang=python3
#
# [2367] 算术三元组的数目
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        cnt = Counter(nums)
        return sum([1 if cnt[num - diff] and cnt[num + diff] else 0 for num in nums])
# @lc code=end

