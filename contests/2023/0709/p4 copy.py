from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                if abs(nums[j] - nums[i]) <= target:
                    graph[i].append(j)
        ans = 0

        dp = [0] * n
        for i in range(n-1, -1, -1):
            if graph[i]:
                for j in graph[i]:
                    if dp[j] or j == n-1:
                        dp[i] = max(dp[i], dp[j]+1)
        return dp[0] if dp[0] else -1

sl = Solution()
use_cases = [([1,3,6,4,1,2], 2, 3), ([1,3,6,4,1,2], 3, 5), ([1,3,6,4,1,2], 0, -1)]
for use_case in use_cases:
    nums, target, ans = use_case
    print(f"{sl.maximumJumps(nums, target)}, {ans}")