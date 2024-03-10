from typing import *


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness = sorted(happiness, reverse=True)
        ans = 0
        for i in range(k):
            ans += max(happiness[i] - i, 0)
        return ans


sl = Solution()
examples = [
    ([1,2,3], 2, 4),
    ([1,1,1,1], 2, 1),
    ([2,3,4,5], 1, 5)

]
for example in examples:
    h, k, ans = example
    print(f"Output: {sl.maximumHappinessSum(h, k)}, Ans: {ans}")