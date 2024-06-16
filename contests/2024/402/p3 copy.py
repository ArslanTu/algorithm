"""
weekply contest p3
"""
from typing import *


class Solution:

    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        ans = 0
        MAX = 10**9
        dp = [[0, 0] for _ in range(3)]
        dp[0][0] = 0
        dp[0][1] = 1 * cnt[1]
        for i in range(2, MAX + 1):
            dp[i % 3][0] = max(
                dp[(i - 1) % 3][0], dp[(i - 2) % 3][0], dp[(i - 1) % 3][1],
                dp[(i - 2) % 3][1]
            )
            dp[i %
               3][1] = max(dp[(i - 2) % 3][0], dp[(i - 2) % 3][0]) + i * cnt[i]
        return max(dp[MAX % 3][0], dp[MAX % 3][1])


def test():
    """
    test func
    """
    sl = Solution()
    examples = [([1, 1, 3, 4], 6), ([7, 1, 6, 6], 13)]
    for example in examples:
        nums, ans = example
        print(f"Output: {sl.maximumTotalDamage(nums)}, Ans: {ans}")


if __name__ == "__main__":
    test()
