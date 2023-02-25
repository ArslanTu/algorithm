#
# @lc app=leetcode.cn id=1162 lang=python3
#
# [1162] 地图分析
#

# @lc code=start
from math import inf
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0
        has_1 = 0
        no_0 = 1
        for r in range(n):
            for c in range(n):
                has_1 |= grid[r][c]
                no_0 &= grid[r][c]
        if not has_1 or no_0:
            return -1
        dp = [[inf] * (n + 2) for _ in range(n + 2)]
        for r in range(1, n + 1):
            for c in range(1, n + 1):
                if grid[r - 1][c - 1]:
                    dp[r][c] = 0
                else:
                    dp[r][c] = min(dp[r][c], dp[r][c - 1] + 1, dp[r - 1][c] + 1)
        for r in range(n, 0, -1):
            for c in range(n, 0, -1):
                if not grid[r - 1][c - 1]:
                    dp[r][c] = min(dp[r][c], dp[r][c + 1] + 1, dp[r + 1][c] + 1)
                    ans = max(ans, dp[r][c])
        return ans
# @lc code=end

