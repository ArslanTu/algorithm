from typing import *


class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        cnt = s.count(c)
        return (cnt * (cnt - 1) // 2) + cnt
        


sl = Solution()
examples = [
]
for example in examples:
    ans = example
    print(f"Output: {sl}, Ans: {ans}")