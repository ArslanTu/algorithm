from math import inf
from typing import *

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        th = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    th[(i, j)] = 0
        for t, v in th.items():
            dp[0][0] += t[0] + t[1]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                v_up = 0
                v_left = 0
                if i > 0:
                    v_up = dp[i - 1][j]
                    for t, v in th.items():
                        if t[0] >= i and t[1] >= j:
                            v_up -= 1
                if j > 0:
                    v_left = dp[i][j - 1]
                    for t, v in th.items():
                        if t[0] >= i and t[1] >= j:
                            v_left -= 1
                dp[i][j] = max(v_up, v_left)
        return dp[m - 1][n - 1]


sol = Solution()

# cases = [([[1,0,0],[0,0,0],[0,0,1]], 0), ([[0,0,1],[0,0,0],[0,0,0]], 2), ([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]], 2)]
cases = [([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]], 2)]

for case in cases:
    grid, ans = case
    print(f"output: {sol.maximumSafenessFactor(grid)}, expect: {ans}")