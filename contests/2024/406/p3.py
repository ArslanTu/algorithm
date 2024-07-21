"""
weekply contest p3
"""
from typing import *


class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort()
        verticalCut.sort()
        ans = 0
        nh, nv = 1, 1
        while horizontalCut and verticalCut:
            h = horizontalCut[-1]
            v = verticalCut[-1]
            if h > v:
                ans += h * nv
                nh += 1
                horizontalCut.pop()
            else:
                ans += v * nh
                nv += 1
                verticalCut.pop()
        while horizontalCut:
            h = horizontalCut[-1]
            ans += h * nv
            nh += 1
            horizontalCut.pop()
        while verticalCut:
            v = verticalCut[-1]
            ans += v * nh
            nv += 1
            verticalCut.pop()
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
