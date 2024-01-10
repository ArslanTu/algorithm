from typing import List

class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        ans = 0
        n = len(nums)

        def dfs(start):
            nonlocal MOD, ans, n
            if start == n or nums[start:] == [0] * (n - start):
                ans = (ans + 1) % MOD
                return
            pos_1 = -1
            for i in range(start, n):
                if nums[i] == 1:
                    pos_1 = i
                    break
            has_1 = False
            if pos_1 != -1:
                for i in range(pos_1 + 1, n):
                    if not has_1:
                        dfs(i)
                    else:
                        
            return
        
        dfs(0)
        return ans


params = [([0,1,0,0,1], 3), ([0,1,0], 1)]
sl = Solution()
for nums, ans in params:
    print(f"{sl.numberOfGoodSubarraySplits(nums)} {ans}")