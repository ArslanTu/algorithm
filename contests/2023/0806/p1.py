from typing import *

class Solution:
    def finalString(self, s: str) -> str:
        ans = ""
        n = len(s)
        for i in range(n):
            if s[i] != 'i':
                ans += s[i]
            else:
                ans = ans[::-1]
        return ans

sol = Solution()

cases = []
for case in cases:
    ans = case
    print(f"output: {sol}, expect: {ans}")