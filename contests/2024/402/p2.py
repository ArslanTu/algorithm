"""
weekply contest p2
"""
from typing import *


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        hours = [h % 24 for h in hours]
        cnt = Counter(hours)
        ans = 0
        for k in cnt.keys():
            if k != 0 and k != 12:
                ans += cnt[k] * cnt[24 - k]
        ans //= 2
        ans += cnt[0] * (cnt[0] - 1) // 2
        ans += cnt[12] * (cnt[12] - 1) // 2
        return ans


def test():
    """
    test func
    """
    sl = Solution()
    examples = [([12, 18, 29, 19, 27, 5], 2)]
    for example in examples:
        nums, ans = example
        print(f"Output: {sl.countCompleteDayPairs(nums)}, Ans: {ans}")


if __name__ == "__main__":
    test()
