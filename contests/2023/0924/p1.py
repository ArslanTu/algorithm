from typing import *


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        num_1, num_0 = s.count('1'), s.count('0')
        ans = '1'
        ans = num_0 * '0' + ans
        ans = (num_1 - 1) * '1' + ans
        return ans 


sl = Solution()
examples = [

]
for example in examples:
    ans = example
    print(f"Output: {sl}, Ans: {ans}")