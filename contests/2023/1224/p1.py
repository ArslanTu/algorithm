from typing import *

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = []
        for i in range(0, len(nums), 2):
            arr.append(nums[i + 1])
            arr.append(nums[i])
        return arr


sl = Solution()
examples = [
    
]
for example in examples:
    ans = example
    print(f"Output: {sl}, Ans: {ans}")