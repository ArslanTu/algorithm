from typing import *

class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        denny = set()
        res = []
        cur = 1
        while len(res) < n:
            if cur not in denny:
                res.append(cur)
                denny.add(k - cur)
                cur += 1
            else:
                cur += 1
        return sum(res)

sl = Solution()
examples = [
    (5, 4, 18),
    (2,6,3),
    (2,3,4),
]
for example in examples:
    n, k, ans = example
    print(f"Output: {sl.minimumSum(n, k)}, Ans: {ans}")