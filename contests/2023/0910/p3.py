from math import inf
from typing import *

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:







sl = Solution()
examples = [
    ([[1,1,0],[1,1,1],[1,2,1]], 3),
    ([[1,3,0],[1,0,0],[1,0,3]], 4),
    ([[3,2,0],[0,1,0],[0,3,0]], 7),
    ([[1,0,1],[1,2,0],[1,0,3]], 3),
    ([[2,0,1],[1,2,0],[1,0,2]], 3),
    ([[0,0,0],[7,0,0],[1,0,1]], 0),
]
for example in examples:
    grid, ans = example
    print(f"Output: {sl.minimumMoves(grid)}, Ans: {ans}")