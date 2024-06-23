"""
weekply contest p1
"""
from bisect import bisect_left
from typing import *


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums = sorted(nums)
        n = len(nums)
        averages = []
        for _ in range(n//2):
            maxE = nums[-1]
            minE = nums[0]
            num = (maxE + minE) / 2
            nums = nums[1:-1]
            averages.append(num)
        return min(averages)


def test():
    """
    test func
    """
    sl = Solution()
    examples = [
    ]
    for example in examples:
        ans = example
        print(f"Output: {sl}, Ans: {ans}")


if __name__ == "__main__":
    test()
