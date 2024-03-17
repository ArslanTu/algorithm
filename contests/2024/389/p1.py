from typing import *


class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        ss = s[::-1]
        for i in range(len(s) - 1):
            if s[i:i+2] in ss:
                return True
        return False


sl = Solution()
examples = [
]
for example in examples:
    ans = example
    print(f"Output: {sl}, Ans: {ans}")