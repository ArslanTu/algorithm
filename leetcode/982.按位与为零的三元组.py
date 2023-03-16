#
# @lc app=leetcode.cn id=982 lang=python3
#
# [982] 按位与为零的三元组
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        # 考虑值有上限
        cnt = Counter([num_i & num_j for num_i in nums for num_j in nums])
        ans = 0
        for num_k in nums:
            # for mask, freq in cnt.items():
            #     if not (num_k & mask):
            #         ans += freq
            sub = x = num_k ^ 0xffff
            while True:
                if sub in cnt:
                    ans += cnt[sub]
                if sub == 0:
                    break
                sub = (sub - 1) & x

        return ans
# @lc code=end

