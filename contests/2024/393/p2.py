"""
weekply contest p1
"""
from typing import *


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        t_s = set()

        for i in range(2, 101):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                t_s.add(i)

        s, t = -1, -1
        for idx, num in enumerate(nums):
            if num in t_s:
                if s == -1:
                    s = idx
                t = idx
        return t - s


def test():
    """
    test func
    """
    sl = Solution()
    examples = [
        ([4, 2, 9, 5, 3], 3),
        ([4, 8, 2, 8], 0),
        ([1, 7], 0)
    ]
    for example in examples:
        nums, ans = example
        print(f"Output: {sl.maximumPrimeDifference(nums)}, Ans: {ans}")


if __name__ == "__main__":
    test()
