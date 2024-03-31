from typing import *
from collections import Counter


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        empty = numBottles
        numBottles = 0
        while empty >= numExchange:
            # 换
            numBottles += 1
            empty -= numExchange
            numExchange += 1

            # 喝
            ans += 1
            empty += 1
            numBottles -= 1
        return ans
        


sl = Solution()
examples = [
    (13, 6, 15),
    (10, 3, 13),
]
for example in examples:
    x, y, ans = example
    print(f"Output: {sl.maxBottlesDrunk(x, y)}, Ans: {ans}")