from typing import List


class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        move = [0 for _ in range(n)]
        cost = [0 for _ in range(n)]
        for i in range(n):
            diff = [0 for _ in range(n)]
            for j in range(n):
                step = (j - i) % n
                diff[j] = step * x + nums[j] - nums[i]
            target = diff.index(min(diff))
            move[i] = (target - i) % n
            cost[i] = nums[target]
        return max(move) * x + sum(cost)

sl = Solution()
# p1 = [20,1,15]
# p2 = 5

p1 = [31,25,18,59]
p2 = 27
print(sl.minCost(p1, p2))