from typing import *

class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        total = sum(nums)
        if len(nums) <= 2:
            return True
        if total <= m:
            return False
        anum = 1
        n = len(nums)
        while anum < n:
            if nums[0] > nums[-1]:
                p = nums.pop()
                total -= p
            else:
                p = nums[0]
                nums = nums[1:]
                total -= p
            if total < m and len(nums) > 1:
                return False
            anum += 1
        return True

sol = Solution()

cases = []
for case in cases:
    ans = case
    print(f"output: {sol}, expect: {ans}")

# [2, 2, 1]
# 4
# [2, 1, 3]
# 5
# [2, 3, 3, 2, 3]
# 6