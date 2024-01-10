from typing import *

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l = moves.count('L')
        r = moves.count('R')
        u = moves.count('_')
        return abs(l - r) + u

sl = Solution()
examples = [
    (),
]
for example in examples:
    ans = examples
    print(f"Output: {sl}, Ans: {ans}")