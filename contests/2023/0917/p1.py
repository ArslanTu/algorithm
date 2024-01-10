from typing import *


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            if format(i, 'b').count('1') == k:
                ans += nums[i]
        return ans


sl = Solution()
examples = [

]
for example in examples:
    ans = example
    print(f"Output: {sl}, Ans: {ans}")