from typing import *


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apple = sum(apple)
        capacity = sorted(capacity, reverse=True)
        ans = 0
        cur = 0
        for c in capacity:
            cur += c
            ans += 1
            if cur >= total_apple:
                return ans
        


sl = Solution()
examples = [
]
for example in examples:
    ans = example
    print(f"Output: {sl}, Ans: {ans}")