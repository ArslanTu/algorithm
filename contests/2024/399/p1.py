"""
weekply contest p1
"""
from typing import *


class Solution:

    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        for i, num1 in enumerate(nums1):
            for j, num2 in enumerate(nums2):
                if num1 % (num2 * k) == 0:
                    ans += 1
        return ans


def test():
    """
    test func
    """
    sl = Solution()
    examples = []
    for example in examples:
        ans = example
        print(f"Output: {sl}, Ans: {ans}")


if __name__ == "__main__":
    test()
