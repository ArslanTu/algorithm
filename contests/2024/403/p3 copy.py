"""
weekply contest p3
"""
from typing import *


class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        negs = [(num, idx) for idx, num in enumerate(nums) if num < 0]
        negs.sort()
        flags = [1 for _ in range(n)]
        for num, idx in negs:
            if idx > 0 and flags[idx - 1] == 1 and (idx == n - 1 or flags[idx + 1] == 1):
                flags[idx] = -1
        for num, flag in zip(nums, flags):
            total += num * flag
        return total




def test():
    """
    test func
    """
    sl = Solution()
    # examples = [([1, -2, 3, 4], 10), ([-14, -13, -20], -7)]
    # examples = [([-14, -13, -20], -7)]
    # examples = [([3, 0, -3, -4, -4], 6)]
    examples = [([3, -2, -2, -1, 0], 4)]
    for example in examples:
        nums, ans = example
        print(f"Output: {sl.maximumTotalCost(nums)}, Ans: {ans}")


if __name__ == "__main__":
    test()
