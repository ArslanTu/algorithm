"""
weekply contest p1
"""
from typing import *


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ps, pt = {}, {}
        for idx, c in enumerate(s):
            ps[c] = idx
        for idx, c in enumerate(t):
            pt[c] = idx
        ans = 0
        for c in ps:
            ans += abs(ps[c] - pt[c])
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
