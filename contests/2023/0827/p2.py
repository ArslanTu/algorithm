from typing import *

class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        black = set()
        i = 1
        s = 0
        cnt = 0
        while cnt < n:
            if i not in black:
                s += i
                cnt += 1
                if target - i > 0:
                    black.add(target - i)
            i += 1
        return s

sl = Solution()
examples = [
    (),
]
for example in examples:
    ans = examples
    print(f"Output: {sl}, Ans: {ans}")