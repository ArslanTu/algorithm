from typing import *

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        pre_sum = []
        for row in grid:
            cur_sum = 0
            pre_sum.append([])
            for num in row:
                cur_sum += num
                pre_sum[-1].append(cur_sum)
        
        pp_sum = [[] for _ in range(len(grid))]
        for j in range(len(grid[0])):
            cur_sum = 0
            for i in range(len(grid)):
                cur_sum += pre_sum[i][j]
                pp_sum[i].append(cur_sum)


        # ans = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         s = sum([row[j] for row in pre_sum[:i+1]])
        #         if s <= k:
        #             ans += 1
        #         else:
        #             break
        # return ans
        return sum([sum([s <= k for s in row]) for row in pp_sum])



sl = Solution()
examples = [
    ([[7,6,3],[6,6,1]], 18, 4),
    ([[7,2,9],[1,5,0],[2,6,6]], 20, 6),
    ([[1,10],[7,2],[9,1],[4,1]], 8, 2),
]
for example in examples:
    grid, k, ans = example
    print(f"Output: {sl.countSubmatrices(grid, k)}, Ans: {ans}")