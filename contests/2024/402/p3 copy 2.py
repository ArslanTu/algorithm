"""
weekply contest p3
"""
from typing import *


class Solution:

    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        nums = sorted([(k, v) for k, v in cnt.items()])
        dp = [[0, 0] for _ in range(3)]
        dp[0][0] = 0
        dp[0][1] = nums[0][0] * nums[0][1]
        for i in range(1, len(nums)):
            if nums[i - 1][0] >= nums[i][0] - 2:
                dp[i % 3][1] = max(
                    dp[i % 3][1], dp[(i - 1) % 3][0] + nums[i][0] * nums[i][1]
                )
            else:
                dp[i % 3][1] = max(
                    dp[i % 3][1], dp[(i - 1) % 3][1] + nums[i][0] * nums[i][1],
                    dp[(i - 1) % 3][0] + nums[i][0] * nums[i][1]
                )
            if i > 1 and nums[i - 2][0] >= nums[i][0] - 2:
                dp[i % 3][1] = max(
                    dp[i % 3][1], dp[(i - 2) % 3][0] + nums[i][0] * nums[i][1]
                )
            else:
                if i > 1:
                    dp[i % 3][1] = max(
                        dp[i % 3][1],
                        dp[(i - 2) % 3][1] + nums[i][0] * nums[i][1],
                        dp[(i - 2) % 3][0] + nums[i][0] * nums[i][1]
                    )
            dp[i % 3
              ][0] = max(dp[i % 3][0], dp[(i - 1) % 3][0], dp[(i - 1) % 3][1])
        return max(dp[(len(nums) - 1) % 3][0], dp[(len(nums) - 1) % 3][1])


def test():
    """
    test func
    """
    sl = Solution()
    # examples = [([1, 1, 3, 4], 6), ([7, 1, 6, 6], 13)]
    examples = [([5, 9, 2, 10, 2, 7, 10, 9, 3, 8], 31)]
    for example in examples:
        nums, ans = example
        print(f"Output: {sl.maximumTotalDamage(nums)}, Ans: {ans}")


if __name__ == "__main__":
    test()
