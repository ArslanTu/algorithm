from math import inf
from typing import *

class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # 看车
        n_che = inf
        if a == e or b == f:
            if a == e:
                if c == e and (b < d < f or f < d < b):
                    n_che = 2
                else:
                    n_che = 1
            elif b == f:
                if d == f and (a < c < e or e < c < a):
                    n_che = 2
                else:
                    n_che = 1
        else:
            n_che = 2
        
        n_x = inf
        if abs(c - e) == abs(d - f):
            if abs(a - e) == abs(b - f) and (c < a < e or e < a < c):
                n_x = 2
            else:
                n_x = 1
        else:
            n_x = 2
        return min(n_che, n_x)

sl = Solution()
examples = [
    (4, 3, 3, 4, 5, 2, 2),
    (4, 3, 3, 4, 2, 5, 1),
    (1, 1, 1, 4, 1, 8, 2),
]
for example in examples:
    a, b, c, d, e, f, ans = example
    print(f"Output: {sl.minMovesToCaptureTheQueen(a, b, c, d, e, f)}, Ans: {ans}")