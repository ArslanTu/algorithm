from typing import *

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        total = 1
        MOD = 12345
        n_MOD = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                total *= grid[i][j]
                n_MOD *= grid[i][j]
                n_MOD += total // MOD
                total %= MOD

        p = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                num = grid[i][j]
                p[i][j] = int((total / num) + ((MOD / num) * n_MOD)) % MOD #((total + n_MOD * MOD) // num) % MOD
        return p


sl = Solution()
examples = [
    # ([[1,2],[3,4]], [[24,12],[8,6]]),
    # ([[12345],[2],[1]], [[2],[0],[0]]),
    # ([[3,2,5],[6,4,3],[6,3,1]], [[615,7095,7776],[6480,9720,615],[6480,615,1845]]),
    ([[7,11],[4,4],[6,5],[10,5],[3,1],[8,7]], [[8760,3330],[2985,2985],[6105,9795],[11070,9795],[12210,11940],[7665,8760]])
]
for example in examples:
    grid, ans = example
    output = sl.constructProductMatrix(grid)
    print(f"Output: {output}, Ans: {ans}, Status: {ans == output}")