from typing import *

class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = Counter(word)
        freq = sorted([v for v in cnt.values()], reverse=True)
        ans = 0
        x = 0
        for i in range(len(freq)):
            if i % 8 == 0:
                x += 1
            ans += x * freq[i]
        return ans

sl = Solution()
examples = [
    
]
for example in examples:
    ans = example
    print(f"Output: {sl}, Ans: {ans}")