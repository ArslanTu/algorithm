"""
weekply contest p3
"""
from math import inf
from typing import *


class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-inf, -inf] for _ in range(n)]
        dp[0][0] = nums[0]
        dp[0][1] = nums[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + nums[i]
            dp[i][1] = dp[i-1][0] - nums[i]
        return max(dp[n-1])






def test():
    """
    test func
    """
    sl = Solution()
    # examples = [([1, -2, 3, 4], 10), ([-14, -13, -20], -7)]
    examples = [([-14, -13, -20], -7)]
    # examples = [([3, 0, -3, -4, -4], 6)]
    # examples = [([3, -2, -2, -1, 0], 4)]
    for example in examples:
        nums, ans = example
        print(f"Output: {sl.maximumTotalCost(nums)}, Ans: {ans}")


if __name__ == "__main__":
    test()
