from typing import *

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy:
            return t != 1
        dy = abs(fy - sy)
        dx = abs(fx - sx)
        min_t = max(dy, dx)
        if t < min_t:
            return False
        else:
            return True



sl = Solution()
examples = [
    (1,1,1,1,3, True),
]
for example in examples:
    sx, sy, fx,fy,t,ans = example
    print(f"Output: {sl.isReachableAtTime(sx, sy,fx,fy, t)}, Ans: {ans}")