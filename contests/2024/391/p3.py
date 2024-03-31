from typing import *
from collections import Counter


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        l, r = 0, 0
        while l < n:
            while r + 1 < n and nums[r] != nums[r + 1]:
                r += 1
            ans += (r - l + 1) * (r - l + 2) // 2
            l = r + 1
            r = l

        return ans


sl = Solution()
examples = [
    ([0,1,1,1], 5),
    ([1,0,1,0], 10),
]
for example in examples:
    nums, ans = example
    print(f"Output: {sl.countAlternatingSubarrays(nums)}, Ans: {ans}")