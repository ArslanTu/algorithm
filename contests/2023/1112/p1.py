from typing import *

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ans = (-1, -1)
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    if ans == (-1, -1):
                        ans = (nums[i], nums[j])
                    else:
                        if nums[i] ^ nums[j] > ans[0] ^ ans[1]:
                            ans = (nums[i], nums[j])
        return ans[0] ^ ans[1]

sl = Solution()
examples = [
    
]
for example in examples:
    ans = example
    print(f"Output: {sl}, Ans: {ans}")