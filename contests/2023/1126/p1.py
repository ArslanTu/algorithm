from typing import *

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        ori_mat = [list(row) for row in mat]
        new_mat = []
        for i in range(len(mat)):
            line = list(mat[i])
            if (i % 2) == 0:
                for _ in range(k):
                    line = line[1:] + [line[0]]
            else:
                for _ in range(k):
                    line = [line[-1]] + line[:-1]
            new_mat.append(line)
        return ori_mat == new_mat


sl = Solution()
examples = [
    
]
for example in examples:
    ans = example
    print(f"Output: {sl}, Ans: {ans}")