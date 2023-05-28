from collections import defaultdict
from typing import List


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        topLeft = [[0 for _ in range(n)] for _ in range(m)]
        bottomRight = [[0 for _ in range(n)] for _ in range(m)]
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                diffNum = defaultdict(int)
                k, l = i, j
                while k - 1 >= 0 and l - 1 >= 0:
                    k -= 1
                    l -= 1
                    diffNum[grid[k][l]] += 1
                topLeft[i][j] = len(diffNum)

                diffNum.clear()
                k, l = i, j
                while k + 1 < m and l + 1 < n:
                    k += 1
                    l += 1
                    diffNum[grid[k][l]] += 1
                bottomRight[i][j] = len(diffNum)
                ans[i][j] = abs(topLeft[i][j] - bottomRight[i][j])
        return ans



sl = Solution()
p1 = [[1,2,3],[3,1,5],[3,2,1]]

print(sl.differenceOfDistinctValues(p1))