from math import inf
from typing import *


class Solution:
    def minOperations(self, k: int) -> int:
        ans = inf
        for x in range(k + 1):
            l, r = 0, 10 ** 5
            while l <= r:
                y = (l + r) // 2
                if x * y + x + y >= k - 1:
                    ans = min(ans, x + y)
                    r = y - 1
                else:
                    l = y + 1
        return ans


sl = Solution()
examples = [
    (11, 5),
    (1, 0),
]
for example in examples:
    k, ans = example
    print(f"Output: {sl.minOperations(k)}, Ans: {ans}")