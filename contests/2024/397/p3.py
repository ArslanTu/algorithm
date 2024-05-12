"""
weekply contest p1
"""
from math import inf
from typing import *


class Solution:

    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-inf for _ in range(n)] for _ in range(m)]

        max_val_pos = [[(-1, -1) for _ in range(n)] for _ in range(m)]

        for j in range(n - 1, -1, -1):
            for i in range(m - 1, -1, -1):
                if i < m - 1 and n < n -1:
                    

        return max([max(row) for row in dp])


def test():
    """
    test func
    """
    sl = Solution()
    examples = [
        # ([[9, 5, 7, 3], [8, 9, 6, 1], [6, 7, 14, 3], [2, 5, 3, 1]], 9),
        # ([[4, 3, 2], [3, 2, 1]], -1),
        (
            [
                [6, 1, 4, 6], [5, 6, 3, 5], [5, 3, 10, 3], [8, 7, 1, 5],
                [1, 6, 6, 2]
            ], 9
        )
    ]
    for example in examples:
        g, ans = example
        print(f"Output: {sl.maxScore(g)}, Ans: {ans}")


if __name__ == "__main__":
    test()
