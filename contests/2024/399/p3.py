"""
weekply contest p3
"""
from bisect import bisect_left, bisect_right
from math import ceil, floor
from typing import *

from collections import defaultdict
from typing import List
import math


class Solution:

    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums2 = [y * k for y in nums2]
        ans = 0
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        nums1 = list(counter1.keys())
        nums2 = list(counter2.keys())
        nums1.sort()
        nums2.sort()
        for x in nums1:
            for y in range(1, floor(math.sqrt(x)) + 1):
                if x % y == 0:
                    if x // y == y:
                        ans += counter1[x] * counter2[y]
                    else:
                        ans += counter1[x] * counter2[y] + counter1[
                            x] * counter2[x // y]
        return ans


def test():
    """
    test func
    """
    sl = Solution()
    examples = [
        ([1, 3, 4], [1, 3, 4], 1, 5), ([1, 2, 4, 12], [2, 4], 3, 2),
        ([70, 50], [5, 7], 10, 2), ([2, 8, 17, 6], [3, 1, 1, 8], 2, 7)
    ]
    for example in examples:
        nums1, nums2, k, ans = example
        print(f"Output: {sl.numberOfPairs(nums1, nums2, k)}, Ans: {ans}")


if __name__ == "__main__":
    test()
