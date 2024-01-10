from typing import *

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high + 1):
            i_str = str(i)
            if len(i_str) % 2 != 0:
                continue
            sum_1 = sum([int(i_str[j]) for j in range(len(i_str)//2)])
            sum_2 = sum([int(i_str[j]) for j in range(len(i_str)//2, len(i_str))])
            if sum_1 == sum_2:
                ans += 1
        return ans



sl = Solution()
examples = [

]
for example in examples:
    ans = example
    print(f"Output: {sl}, Ans: {ans}")