from typing import *

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        nums = [1 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    nums[j] = 0
        for i in range(n):
            if nums[i] == 1:
                return i