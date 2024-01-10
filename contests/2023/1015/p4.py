from typing import *

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        total = 1
        MOD = 12345
        n_MOD = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                total = (total * grid[i][j]) % MOD
                if grid[i][j] % MOD == 0:
                    n_MOD += 1

        if n_MOD > 1:
            return [[0 for _ in range(n)] for _ in range(m)]
        
        if n_MOD == 1:
            p = [[0 for _ in range(n)] for _ in range(m)]
            pos = (-1, -1)
            val = 1
            for i in range(m):
                for j in range(n):
                    if grid[i][j] % MOD == 0:
                        pos = (i, j)
                    else:
                        val = (val * grid[i][j]) % MOD
            p[pos[0]][pos[1]] = val
            return p
        


        p = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                num1 = total
                num2 = grid[i][j]
                while num1 % num2 > 0:
                    num1 += MOD
                p[i][j] = num1 // num2
        return p


sl = Solution()
examples = [
    # ([[1,2],[3,4]], [[24,12],[8,6]]),
    # ([[12345],[2],[1]], [[2],[0],[0]]),
    ([[3,2,5],[6,4,3],[6,3,1]], [[615,7095,7776],[6480,9720,615],[6480,615,1845]]),
]
for example in examples:
    grid, ans = example
    print(f"Output: {sl.constructProductMatrix(grid)}, Ans: {ans}")