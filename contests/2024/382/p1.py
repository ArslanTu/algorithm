from typing import *

class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        ans = 0
        if len(s) == 1:
            return 0
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                ans += 1
        return ans

sl = Solution()
examples = [
    ("mDVD", 3)
]
for example in examples:
    s, ans = example
    print(f"Output: {sl.countKeyChanges(s)}, Ans: {ans}")