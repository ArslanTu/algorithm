"""
weekply contest p1
"""
from typing import *


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = 0
        n = len(hours)
        for i in range(n):
            for j in range(i + 1, n):
                if (hours[i] + hours[j]) % 24 == 0:
                    ans += 1
        return ans


def test():
    """
    test func
    """
    sl = Solution()
    examples = [
    ]
    for example in examples:
        ans = example
        print(f"Output: {sl}, Ans: {ans}")


if __name__ == "__main__":
    test()
