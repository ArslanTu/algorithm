from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0:
            return False
        n = len(grid)
        mapping = {grid[row][col]: (row, col) for row in range(n) for col in range(n)}
        for idx in range(1, n * n):
            row_var = abs(mapping[idx][0] - mapping[idx - 1][0])
            col_var = abs(mapping[idx][1] - mapping[idx - 1][1])
            if (row_var == 2 and col_var == 1) or (row_var == 1 and col_var == 2):
                continue
            else:
                return False
        return True

sl = Solution()
p1 = [[24,11,22,17,4],[21,16,5,12,9],[6,23,10,3,18],[15,20,1,8,13],[0,7,14,19,2]]
print(sl.checkValidGrid(p1))