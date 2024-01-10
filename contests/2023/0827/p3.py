from typing import *

class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1
        if sum(nums) == target:
            return 0
        nums.sort()
        nums_one = nums.count(1)
        if nums_one == 0 and (target & 1) == 1:
            return -1
        if (target & 1) == 1:
            target -= 1
        nums = nums[1:]



sl = Solution()
examples = [
    ([1,2,8], 7, 1),
    ([1,32,1,2], 12, 2),
    ([1,32,1], 35, -1),
]
for example in examples:
    ans = example
    print(f"Output: {sl}, Ans: {ans}")