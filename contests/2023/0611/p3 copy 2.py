from math import inf
from typing import List


class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        cost = list(nums)
        ans = sum(cost)
        for step in range(1, n):
            for i in range(n - step):
                cost[i] = min(nums[i:i + step + 1])
            for i in range(n - step, n):
                cost[i] = min(min(nums[i:]), min(nums[:i+step - n + 1]))
            total_cost = step * x + sum(cost)
            ans = min(ans, total_cost)
        return ans

sl = Solution()
# p1 = [20,1,15]
# p2 = 5

# p1 = [31,25,18,59]
# p2 = 27

# p1 = [15,150,56,69,214,203]
# p2 = 42
p1 = [1, 2, 3]
p2 = 4
print(sl.minCost(p1, p2))
