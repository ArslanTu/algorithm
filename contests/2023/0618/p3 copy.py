from collections import defaultdict
from typing import List

class Solution:
    def findPath(self, graph):
        MOD = 10 ** 9 + 7
        N = len(graph)
        dp = [[0] * N for _ in range(1 << N)]
        # 初始化状态，只有起点被访问过
        for i in range(N):
            dp[1 << i][i] = 1
        # 递推计算dp[i][j]
        for s in range(1 << N):
            for i in range(N):
                if not (s & (1 << i)):
                    continue
                for j in range(N):
                    if graph[i][j] and (s & (1 << j)):
                        dp[s][j] += dp[s ^ (1 << j)][i]
                        dp[s][j] = dp[s][j] % MOD
        # 统计答案，枚举起点
        ans = sum(dp[(1 << N) - 1][i] for i in range(N))
        return ans % MOD

    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)

        graph = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            num1 = nums[i]
            for j in range(n):
                num2 = nums[j]
                if (num2 != 0 and num1 % num2 == 0) or (num1 != 0 and num2 % num1 == 0):
                    graph[i][j] = 1
                    graph[j][i] = 1
        
        return self.findPath(graph)

sl = Solution()

cases = (([2,3,6], 2), ([1,4,3], 2), ([20,100,50,5,10,70,7], 48))
for p1, p2 in cases:
    print(sl.specialPerm(p1), " ", p2)