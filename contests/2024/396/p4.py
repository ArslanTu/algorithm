"""
weekply contest p1
"""
from typing import *


class Solution:

    def minCostToEqualizeArray(
        self, nums: List[int], cost1: int, cost2: int
    ) -> int:
        MOD = 10**9 + 7
        if cost2 >= cost1 * 2:
            return sum(num - max(nums) for num in nums) * cost1
        


def test():
    """
    test func
    """
    sl = Solution()
    examples = [
        # ([4, 1], 5, 2, 15), ([2, 3, 3, 3, 5], 2, 1, 6), ([3, 5, 3], 1, 3, 4),
        ([1, 14, 14, 15], 2, 1, 20)
    ]
    for example in examples:
        nums, c1, c2, ans = example
        print(f"Output: {sl.minCostToEqualizeArray(nums, c1, c2)}, Ans: {ans}")


if __name__ == "__main__":
    test()
