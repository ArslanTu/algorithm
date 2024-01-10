from typing import *

class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        ans = 0
        for num in nums:
            if bin(num)[-1] == '0':
                ans += 1
        return ans > 1

sl = Solution()
examples = [
    
]
for example in examples:
    ans = example
    print(f"Output: {sl}, Ans: {ans}")