from typing import *
from collections import Counter

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                if self.check(s[i:j+1]):
                    ans = max(ans, j-i+1)
        return ans
    
    def check(self, s: str) -> bool:
        cnt = Counter(s)
        for _, v in cnt.items():
            if v > 2:
                return False
        return True


sl = Solution()
examples = [
]
for example in examples:
    ans = example
    print(f"Output: {sl}, Ans: {ans}")