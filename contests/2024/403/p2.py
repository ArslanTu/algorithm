"""
weekply contest p2
"""
from math import inf
from typing import *


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        l, r, u, b = inf, -inf, inf, -inf
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    l = min(l, j)
                    r = max(r, j)
                    u = min(u, i)
                    b = max(b, i)
        return (r - l + 1) * (b - u + 1)


def test():
    """
    test func
    """
    sl = Solution()
    examples = [([[0, 1, 0], [1, 0, 1]], 6)]
    for example in examples:
        grid, ans = example
        print(f"Output: {sl.minimumArea(grid)}, Ans: {ans}")


if __name__ == "__main__":
    test()
