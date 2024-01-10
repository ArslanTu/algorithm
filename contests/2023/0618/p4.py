from math import inf
from typing import List

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [[float('inf')]*2 for _ in range(n)]
        dp[0][0] = cost[0]
        dp[0][1] = 0
        for i in range(1, n):
            # 不使用免费油漆匠
            dp[i][0] = min(dp[i-1][0]+cost[i], dp[i-1][1]+cost[i])
            dp[i][0] = min(dp[i][0], dp[i-1][0]+time[i])
            # 使用免费油漆匠
            dp[i][1] = dp[i-1][0]
            dp[i][1] = min(dp[i][1], dp[i-1][1]+1)
        return min(dp[n-1])


sl = Solution()

cases = (([1,2,3,2], [1,2,3,2], 3), ([2,3,4,2], [1,1,1,1], 4), ([8,7,5,15], [1,1,2,1], 12))
for cost, time, ans in cases:
    print(sl.paintWalls(cost, time), " ", ans)
