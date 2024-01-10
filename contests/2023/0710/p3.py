from heapq import heappop, heappush
from typing import List

class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        hp = []
        for i, limit in enumerate(usageLimits):
            heappush(hp, (-limit, i))
        ans = 0
        while True:
            used = []
            while hp:
                limit, i = heappop(hp)
                limit = -limit
                if limit == 0:
                    break
                used.append((limit, i))
                if len(used) > ans:
                    break
            if len(used) <= ans:
                break
            else:
                ans += 1
                for limit, i in used:
                    if limit > 1:
                        heappush(hp, (-(limit-1), i))
        return ans


sl = Solution()
cases = [()]
for case in cases:
    print(f"output: {sl}, ans: {ans}")