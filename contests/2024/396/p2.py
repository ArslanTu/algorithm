"""
weekply contest p1
"""
from math import inf
from typing import *


class Solution:

    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        possible_s = [word[i:i + k] for i in range(0, len(word), k)]
        cnt = Counter(possible_s)
        return sum(cnt.values()) - max(cnt.values())


def test():
    """
    test func
    """
    sl = Solution()
    examples = [("leetcodeleet", 4, 1), ("leetcoleet", 2, 3)]
    for example in examples:
        word, k, ans = example
        print(
            f"Output: {sl.minimumOperationsToMakeKPeriodic(word, k)}, Ans: {ans}"
        )


if __name__ == "__main__":
    test()
