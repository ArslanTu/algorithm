from math import sqrt
from typing import *

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        nums = Counter(nums)
        ans = 1
        for num in sorted(nums.keys()):
            if num == 1:
                ans = max(ans, nums[1] if nums[1] & 1 == 1 else nums[1] - 1)
                continue
            m = 1
            i = 2
            while True:
                if nums[num ** (i // 2)] > 1 and nums[num ** i] > 0:
                    m += 2
                    i *= 2
                else:
                    break
            ans = max(ans, m)
        return ans
    
sl = Solution()
examples = [
    # ([5,4,1,2,2], 3),
    # ([1,3,2,4], 1),
    ([4,4,16,16,256,256,65536,65536], 7),
]
for example in examples:
    nums, ans = example
    print(f"Output: {sl.maximumLength(nums)}, Ans: {ans}")