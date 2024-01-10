from typing import *

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans_1 = 0
        ans_2 = 0
        for x, y in dimensions:
            if x ** 2 + y ** 2 > ans_1:
                ans_1 = x ** 2 + y ** 2
                ans_2 = x * y
            elif x ** 2 + y ** 2 == ans_1:
                ans_2 = max(ans_2, x * y)
            else:
                pass
        return ans_2

sl = Solution()
examples = [
    
]
for example in examples:
    ans = example
    print(f"Output: {sl}, Ans: {ans}")