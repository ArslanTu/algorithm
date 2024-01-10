from typing import *

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for i in range(len(variables)):
            a, b, c, m = variables[i]
            if (((((a % 10 ) ** b) % 10) % m) ** c) % m == target:
                ans.append(i)
        return ans

sl = Solution()
examples = [
    
]
for example in examples:
    ans = example
    print(f"Output: {sl}, Ans: {ans}")