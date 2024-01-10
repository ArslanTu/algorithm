from typing import *

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        ans = [-1, -1]
        n = len(nums)
        for i in range(n - indexDifference):
            for j in range(i + indexDifference, n):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    ans = [i, j]
                    break
            if ans[0] != -1:
                break
        return ans


sl = Solution()
examples = [

]
for example in examples:
    ans = example
    print(f"Output: {sl}, Ans: {ans}")