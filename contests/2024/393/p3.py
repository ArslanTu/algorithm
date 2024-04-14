"""
weekply contest p1
"""
from typing import *


def test():
    """
    test func
    """
    sl = Solution()
    examples = [
        # ([3,6,9], 3, 9),
        # ([5, 2], 7, 12),
        # ([6, 1, 2, 4], 4, 4),
        ([4, 1, 7, 6], 7, 7)
    ]
    for example in examples:
        coins, k, ans = example
        print(f"Output: {sl.findKthSmallest(coins, k)}, Ans: {ans}")


if __name__ == "__main__":
    test()
