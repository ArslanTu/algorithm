from typing import *


class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        if nums[0] > 0:
            ans += 1
        if nums[-1] < len(nums):
            ans += 1
        for k in range(1, len(nums)):
            if k > nums[k - 1] and k < nums[k]:
                ans += 1
        return ans

sl = Solution()
examples = [

]
for example in examples:
    ans = example
    print(f"Output: {sl}, Ans: {ans}")