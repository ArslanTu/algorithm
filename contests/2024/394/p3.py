"""
weekply contest p1
"""
from typing import List
from collections import Counter


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # 预处理
        cnts = [Counter([grid[i][j] for i in range(m)]) for j in range(n)]

        # 初始化 dp 数组，dp[i][j] 表示使得前 i 列的元素满足条件，并且第 i 列的元素值为 j 时的最小改变次数
        dp = [[float('inf')] * 10 for _ in range(n)]

        # 初始状态，第一列的元素可以任意选择
        for j in range(10):
            dp[0][j] = m - cnts[0][j]

        # 动态规划，更新状态
        for i in range(1, n):
            for j in range(10):
                for k in range(10):
                    if j != k:
                        count = m - cnts[i][j]
                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + count)

        # 返回结果，最后一列的最小改变次数
        return min(dp[-1])


def test():
    """
    test func
    """
    sl = Solution()
    examples = [
        ([[1, 0, 2], [1, 0, 2]], 0),
        ([[1, 1, 1], [0, 0, 0]], 3),
        ([[1], [2], [3]], 2)
    ]
    for example in examples:
        grid, ans = example
        print(f"Output: {sl.minimumOperations(grid)}, Ans: {ans}")


if __name__ == "__main__":
    test()
