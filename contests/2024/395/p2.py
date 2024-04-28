"""
weekply contest p1
"""
from math import inf
from typing import *


class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        n = len(nums1)
        ans = inf
        for i in range(n):
            for j in range(i+1, n):
                nums3 = nums1[:i] + nums1[i+1:j] + nums1[j+1:]
                diff = nums2[0] - nums3[0]
                if all(nums2[k] - nums3[k] == diff for k in range(1, n-2)):
                    ans = diff if diff < ans else ans

        return ans


def test():
    """
    test func
    """
    sl = Solution()
    examples = [
        ([4,20,16,12,8], [14,18,10], -2)
    ]
    for example in examples:
        n1, n2, ans = example
        print(f"Output: {sl.minimumAddedInteger(n1, n2)}, Ans: {ans}")


if __name__ == "__main__":
    test()
