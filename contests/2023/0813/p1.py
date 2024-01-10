from typing import *

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        for i in range(n):
            for j in range(n):
                if i != j:
                    if max([int(x) for x in str(nums[i])]) == max([int(x) for x in str(nums[j])]):
                        s = nums[i] + nums[j]
                        ans = max(ans, s)
        return ans

sl = Solution()

examples = [
    (),
]
for ex in examples:
    p, ans = ex
    print(f"output: {sl}, expect: {ans}")