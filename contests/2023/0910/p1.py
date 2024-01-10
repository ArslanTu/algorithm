from typing import *

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        ans = set()
        for s, e in nums:
            for c in range(s, e + 1):
                ans.add(c)
        return len(ans)



sl = Solution()
examples = [

]
for example in examples:
    ans = example
    print(f"Output: {sl}, Ans: {ans}")