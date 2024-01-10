from typing import *

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        res = ""
        for w in words:
            res += w[0]
        return res == s

sl = Solution()
examples = [
    (),
]
for example in examples:
    ans = examples
    print(f"Output: {sl}, Ans: {ans}")