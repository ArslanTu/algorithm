from typing import List


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        weight = [type[1] for type in types]
        nums = [type[0] for type in types]
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        MOD = 10 ** 9 + 7
        for i in range(len(weight)):
            for j in range(target, weight[i] - 1, -1):
                for k in range(1, nums[i] + 1):
                    if j - k * weight[i] >= 0:
                        dp[j] = (dp[j] + dp[j - k * weight[i]]) % MOD
        return dp[target]
sl = Solution()

# p1 = 6
# p2 = [[6,1],[3,2],[2,3]]

# p1 = 5
# p2 = [[50,1],[50,2],[50,5]]

p1 = 18
p2 = [[6,1],[3,2],[2,3]]

print(sl.waysToReachTarget(p1, p2))