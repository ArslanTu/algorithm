from math import inf
from typing import *

class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        ans = inf
        n = len(grid)
        for x in [0, 1, 2]: # Y
            for y in [0, 1, 2]: # Others
                if x == y:
                    continue
                else:
                    target = [[y for _ in range(n)] for _ in range(n)]
                    for i in range((n - 1) // 2):
                        target[i][i] = x
                        target[i][n - i - 1] = x
                        
                    for i in range((n - 1) // 2, n):
                        target[i][(n - 1) // 2] = x

                    ans = min(ans, sum([sum([grid[i][j] != target[i][j] for j in range(n)]) for i in range(n)]))
        return ans
    
sl = Solution()
examples = [
    ([[1,2,2],[1,1,0],[0,1,0]], 3),
    ([[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]], 12),
]
for example in examples:
    grid, ans = example
    print(f"Output: {sl.minimumOperationsToWriteY(grid)}, Ans: {ans}")