"""
weekply contest p3
"""
from functools import lru_cache
from typing import *


class Solution:

    @lru_cache
    def recursive(
        self, rewardValues: Tuple[int], n: int, cur_pos: int, cur_reward: int
    ) -> int:
        self.ans = max(self.ans, cur_reward)
        if cur_pos == n - 1:
            if rewardValues[cur_pos] > cur_reward:
                self.ans = max(self.ans, cur_reward + rewardValues[cur_pos])
            return

        for i in range(cur_pos + 1, n):
            self.recursive(rewardValues, n, i, cur_reward)
            if rewardValues[cur_pos] > cur_reward:
                self.recursive(
                    rewardValues, n, i, cur_reward + rewardValues[cur_pos]
                )

    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues = list(set(rewardValues))
        rewardValues.sort()
        rewardValues = tuple(rewardValues)
        n = len(rewardValues)
        self.ans = 0
        self.recursive(rewardValues, n, 0, 0)
        return self.ans


def test():
    """
    test func
    """
    sl = Solution()
    examples = [
        ([1, 1, 3, 3], 4),
        ([1, 6, 4, 3, 2], 11),
        ([1], 1),
        ([3, 4, 17, 11], 32),
        # (
        #     [
        #         89, 43, 37, 99, 89, 89, 1, 96, 66, 20, 58, 63, 38, 78, 26, 68,
        #         81, 11, 94, 27, 34, 79, 49, 87, 32, 32, 33
        #     ], 0
        # ),
        # (
        #     [
        #         92, 15, 60, 40, 49, 54, 63, 65, 96, 14, 70, 73, 59, 20, 21, 98,
        #         81, 55, 27, 4, 30, 62, 33, 58, 92, 16, 81, 72, 21, 94, 15, 92
        #     ], 0
        # )
    ]
    for example in examples:
        nums, ans = example
        print(f"Output: {sl.maxTotalReward(nums)}, Ans: {ans}")


if __name__ == "__main__":
    test()
