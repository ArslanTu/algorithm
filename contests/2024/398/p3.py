"""
weekply contest p3
"""
from functools import reduce
import operator
from typing import *


class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        ans = 0
        nums = [str(num) for num in nums]
        for i in range(len(nums[0])):
            cnt = Counter()
            for num in nums:
                cnt[num[i]] += 1
            if len(cnt) == 1:
                continue
            v = list(cnt.values())
            for j in range(len(v)):
                for k  in range(j + 1, len(v)):
                    ans += v[j] * v[k]
        return ans

def test():
    """
    test func
    """
    sl = Solution()
    examples = [([13, 23, 12], 4), ([10, 10, 10, 10], 0), ([50, 28, 48], 5)]
    for example in examples:
        nums, ans = example
        print(f"Output: {sl.sumDigitDifferences(nums)}, Ans: {ans}")


if __name__ == "__main__":
    test()
