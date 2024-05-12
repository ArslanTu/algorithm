"""
weekply contest p1
"""
from typing import *


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0] * n
        dp[n - 1] = energy[n - 1]
        for i in range(n - 2, -1, -1):
            dp[i] = energy[i] + (0 if i + k >= n else dp[i + k])
        return max(dp)


def test():
    """
    test func
    """
    sl = Solution()
    examples = [([5,2,-10,-5,1], 3, 3), ([-2,-3,-1], 2, -1)
    ]
    for example in examples:
        eng, k, ans = example
        print(f"Output: {sl.maximumEnergy(eng, k)}, Ans: {ans}")


if __name__ == "__main__":
    test()
