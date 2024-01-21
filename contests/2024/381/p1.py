from typing import *

class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        x = 0
        ans = 0
        for i in range(n):
            if i % 8 == 0:
                x += 1
            ans += x
        return ans

sl = Solution()
examples = [
    
]
for example in examples:
    ans = example
    print(f"Output: {sl}, Ans: {ans}")