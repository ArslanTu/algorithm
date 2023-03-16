#
# @lc app=leetcode.cn id=1605 lang=python3
#
# [1605] 给定行和列的和求可行矩阵
#

# @lc code=start
from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        res = [[0] * n for _ in range(m)]
        pre_row_sum = [0] * m
        pre_col_sum = [0] * n
        for r in range(m):
            for c in range(n):
                res[r][c] = min(rowSum[r] - pre_row_sum[r], colSum[c] - pre_col_sum[c])
                pre_row_sum[r] += res[r][c]
                pre_col_sum[c] += res[r][c]
        return res


# @lc code=end