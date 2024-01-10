from typing import List

class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        ans = 0

        def dfs(start):
            nonlocal MOD, n, ans
            if start == n:
                ans = (ans + 1) % MOD
                return
            pos_1 = -1
            for i in range(start, n):
                if nums[i] == 1:
                    pos_1 = i
                    break
            if pos_1 == -1:
                return
            for i in range(pos_1 + 1, n + 1):
                dfs(i)
                if i < n and nums[i] == 1:
                    break
            return
        
        dfs(0)
        return ans



params = [([0,1,0,0,1], 3), ([0,1,0], 1), ([0,1,0,0], 1)]
sl = Solution()
for nums, ans in params:
    print(f"{sl.numberOfGoodSubarraySplits(nums)} {ans}")