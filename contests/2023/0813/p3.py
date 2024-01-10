import bisect
from math import inf
from typing import *

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        if x == 0:
            return 0
        n = len(nums)
        diff = []
        for i in range(x, n):
            diff.append(nums[0] - nums[i])
        ans = min([abs(d) for d in diff])




    

sl = Solution()

examples = [
    ([5,3,2,10,15], 1, 3),
]
for ex in examples:
    nums, x, ans = ex
    print(f"output: {sl.minAbsoluteDifference(nums, x)}, expect: {ans}")