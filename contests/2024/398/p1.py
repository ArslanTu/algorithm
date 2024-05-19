"""
weekply contest p1
"""
from typing import *


class Solution:

    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if ((nums[i] & 1) ^ (nums[i + 1] & 1)) != 1:
                return False
        return True


def test():
    """
    test func
    """
    sl = Solution()
    examples = [([1], True), ([2, 1, 4], True), ([4,3,1,6], False)]
    for example in examples:
        nums, ans = example
        print(f"Output: {sl.isArraySpecial(nums)}, Ans: {ans}")


if __name__ == "__main__":
    test()
