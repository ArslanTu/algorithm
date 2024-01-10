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
                    th[(i, j)] = (0, 0)
        for t, near in th.items():
            dp[0][0] += t[0] + t[1]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                v_up = 0
                v_left = 0
                if i > 0:
                    v_up = dp[i - 1][j]
                    for t, near in th.items():
                        if near == (i - 1, j):
                            if abs(i - t[0]) < abs(i - 1 - t[0]):
                                th[t] = (i, j)
                                v_up -= abs(i - 1 - t[0]) - abs(i - t[0])
                if j > 0:
                    v_left = dp[i][j - 1]
                    for t, near in th.items():
                        if near == (i, j - 1):
                            if abs(j - t[1]) < abs(j - 1 - t[1]):
                                th[t] = (i, j)
                                v_left -= abs(j - 1 - t[1]) - abs(j - t[1])
                dp[i][j] = max(v_up, v_left)
        return dp[m - 1][n - 1]


sol = Solution()

cases = [([[1,0,0],[0,0,0],[0,0,1]], 0), ([[0,0,1],[0,0,0],[0,0,0]], 2), ([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]], 2)]
for case in cases:
    grid, ans = case
    print(f"output: {sol.maximumSafenessFactor(grid)}, expect: {ans}")