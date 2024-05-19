"""
weekply contest p2
"""
from bisect import bisect_left, bisect_right
from typing import *


class Solution:

    def isArraySpecial(self, nums: List[int],
                       queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        s = [0]
        while s[-1] < n:
            if s[-1] == n - 1:
                break
            start = s[-1]
            for i in range(start, n - 1):
                if ((nums[i] & 1) ^ (nums[i + 1] & 1)) != 1:
                    break
            if ((nums[i] & 1) ^ (nums[i + 1] & 1)) == 1:
                s.append(i + 2)
            else:
                s.append(i + 1)
        while s[-1] >= n:
            s.pop()
        ans = []
        for f, t in queries:
            if f == t:
                ans.append(True)
                continue
            # start_idx = bisect_left(s, f) - 1
            start_idx = bisect_right(s, f) - 1

            end_idx = start_idx + 1

            start = s[start_idx] if start_idx < len(s) else s[-1]
            end = (s[end_idx] - 1) if end_idx < len(s) else (n - 1)
            if t <= end:
                ans.append(True)
            else:
                ans.append(False)
        return ans


def test():
    """
    test func
    """
    sl = Solution()
    examples = [
        ([3, 4, 1, 2, 6], [[0, 4]], [False]),
        ([4, 3, 1, 6], [[0, 2], [2, 3]], [False, True]),
        ([1, 8], [[1, 1]], True),
        ([5, 8, 8, 9],[[1, 2]], [False])
    ]
    for example in examples:
        nums, queries, ans = example
        print(f"Output: {sl.isArraySpecial(nums, queries)}, Ans: {ans}")


if __name__ == "__main__":
    test()
