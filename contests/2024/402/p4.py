"""
weekply contest p4
"""
import bisect
from typing import *


class Solution:

    def countOfPeaks(self, nums: List[int],
                     queries: List[List[int]]) -> List[int]:
        peaks = []
        ans = []
        for i in range(len(nums)):
            if i > 0 and i < len(nums) - 1:
                if nums[i - 1] < nums[i] and nums[i + 1] < nums[i]:
                    peaks.append((i, nums[i]))
        for q in queries:
            if q[0] == 1:
                start = bisect.bisect_left(peaks, q[1], key=lambda x: x[0])
                end = bisect.bisect_right(peaks, q[2], key=lambda x: x[0])
                res = end - start
                if 0 <= start < len(peaks) and peaks[start][0] == q[1]:
                    res -= 1
                ans.append(res)
            else:
                idx = bisect.bisect_left(peaks, q[1], key=lambda x: x[0])
                if 0 <= idx < len(peaks) and peaks[idx][0] == q[1]:
                    peaks[idx] = (peaks[idx][0], q[2])
                    if nums[peaks[idx][0] -
                            1] >= peaks[idx][1] or nums[peaks[idx][0] +
                                                        1] >= peaks[idx][1]:
                        peaks.pop(idx)
                if q[1] > 0:
                    idx = bisect.bisect_left(
                        peaks, q[1] - 1, key=lambda x: x[0]
                    )
                    if 0 <= idx < len(peaks) and peaks[idx][0] == q[1] - 1:
                        if q[2] >= peaks[idx][1]:
                            peaks.pop(idx)
                if q[1] < len(nums) - 1:
                    idx = bisect.bisect_left(
                        peaks, q[1] + 1, key=lambda x: x[0]
                    )
                    if 0 <= idx < len(peaks) and peaks[idx][0] == q[1] + 1:
                        if q[2] >= peaks[idx][1]:
                            peaks.pop(idx)
                nums[q[1]] = q[2]
        return ans


def test():
    """
    test func
    """
    sl = Solution()
    examples = [
        ([3, 1, 4, 2, 5], [[2, 3, 4], [1, 0, 4]], [0]),
        ([4, 1, 4, 2, 1, 5], [[2, 2, 4], [1, 0, 2], [1, 0, 4]], [0, 1])
    ]
    for example in examples:
        nums, queries, ans = example
        print(f"Output: {sl.countOfPeaks(nums, queries)}, Ans: {ans}")


if __name__ == "__main__":
    test()
