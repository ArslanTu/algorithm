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
        final_step = max(move)
        for i in range(n - final_step):
            cost[i] = min(nums[i:i + final_step + 1])
        for i in range(n - final_step, n):
            cost[i] = min(min(nums[i:]), min(nums[:i+final_step - n + 1]))
        return final_step * x + sum(cost)

sl = Solution()
# p1 = [20,1,15]
# p2 = 5

# p1 = [31,25,18,59]
# p2 = 27

p1 = [15,150,56,69,214,203]
p2 = 42
print(sl.minCost(p1, p2))
