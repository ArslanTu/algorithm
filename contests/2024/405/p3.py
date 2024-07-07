"""
weekply contest p3
"""
from typing import *


class Solution:

    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        ans = 0

        xs = set()

        mix_sum = [[[0, 0] for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "X":
                    xs.add((i, j))
                if j > 0:
                    mix_sum[i][j][0] = mix_sum[i][j - 1][0]
                    mix_sum[i][j][0] += 1 if grid[i][
                        j] == "Y" else -1 if grid[i][j] == "X" else 0
                else:
                    mix_sum[i][j][0] = 1 if grid[i][
                        j] == "Y" else -1 if grid[i][j] == "X" else 0
                if i > 0:
                    mix_sum[i][j][1] = mix_sum[i - 1][j][1]
                    mix_sum[i][j][1] += 1 if grid[i][
                        j] == "Y" else -1 if grid[i][j] == "X" else 0
                else:
                    mix_sum[i][j][1] = 1 if grid[i][
                        j] == "Y" else -1 if grid[i][j] == "X" else 0

        if not xs:
            return 0

        for i in range(m):
            for j in range(n):
                u, l = 0, 0
                d_u, d_l = 0, 0
                if i > 0:
                    d_u = mix_sum[i - 1][j][1]
                    u = dp[i - 1][j] - d_u
                if j > 0:
                    d_l = mix_sum[i][j - 1][0]
                    l = dp[i][j - 1] - d_l
                d_c = 1 if grid[i][j] == "Y" else -1 if grid[i][j] == "X" else 0
                dp[i][j] = (u + l) // 2 + d_u + d_l + d_c
                if dp[i][j] == 0 and any(i >= x and j >= y for x, y in xs):
                    ans += 1
        return ans


def test():
    """
    test func
    """
    sl = Solution()
    # examples = [([["X","Y","."],["Y",".","."]], 3)]
    # examples = [
    #     (
    #         [
    #             [".", ".", "."], [".", "X", "X"], ["Y", ".", "."],
    #             ["X", ".", "."]
    #         ], 2
    #     )
    # ]
    examples = [
        ([[".", "Y", "X"], [".", "X", "."], [".", "X", "."], ["X", "Y", "Y"]], 2)
    ]
    for example in examples:
        g, ans = example
        print(f"Output: {sl.numberOfSubmatrices(g)}, Ans: {ans}")


if __name__ == "__main__":
    test()
