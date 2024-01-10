from typing import *

class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort()
        dp = [0 for _ in range(n)]
        for s, e, g in offers:
            dp[e] = max(dp[e], (dp[s - 1] if s > 0 else 0) + g)
            for j in range(s, e):
                dp[j] = max(dp[j], dp[s - 1] if s > 0 else 0)
        return max(dp)



sl = Solution()
examples = [
    # (5, [[0,0,1],[0,2,2],[1,3,2]], 3),
    # (5, [[0,0,1],[0,2,10],[1,3,2]], 10),
    # (4, [[0,0,5],[3,3,1],[1,2,5],[0,0,7]], 13),
    (9, [[2,3,4],[7,7,8],[2,5,3]], 12),
]
for example in examples:
    n, offers, ans = example
    print(f"Output: {sl.maximizeTheProfit(n, offers)}, Ans: {ans}")