from typing import *

class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)
        dp[2] = max(0, k - max(nums[:3]))
        idx = 0
        for i in range(3):
            if nums[i] >= nums[idx]:
                idx = i
        if nums[idx] < k:
            nums[idx] = k
        for i in range(3, len(nums)):
            if any([nums[i - 2] >= k, nums[i - 1] >= k, nums[i] >= k]):
                dp[i] = dp[i - 1]
            else:
                dp[i] = dp[i - 1] + k - nums[i]
                nums[i] = k
        return dp[len(nums) - 1]

sl = Solution()
examples = [
    ([2,3,0,0,2], 4, 3),
    ([0,1,3,3], 5, 2),
    ([1,1,2], 1, 0),
    ([7,7,2,7], 9, 2),
    ([43,31,14,4], 73, 42),
]
for example in examples:
    nums, k, ans = example
    print(f"Output: {sl.minIncrementOperations(nums, k)}, Ans: {ans}")