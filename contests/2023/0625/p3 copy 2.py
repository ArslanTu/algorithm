from typing import List

class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        start = end = -1
        for i in range(n):
            if nums[i] == 1:
                start = i
                break
        for i in range(n - 1, -1, -1):
            if nums[i] == 1:
                end = i
                break
        nums = nums[start:end + 1]
        n = len(nums)


        def rec(s):
            nonlocal MOD, n
            if s == n:
                return 0
            if s == n - 1:
                return 1
            pos_1 = -1
            for i in range(s + 1, n):
                if nums[i] == 1:
                    pos_1 = i
                    break
            return ((pos_1 - s) * rec(pos_1)) % MOD

        return rec(0)



params = [([0,1,0,0,1], 3), ([0,1,0], 1), ([0,1,0,0], 1)]
sl = Solution()
for nums, ans in params:
    print(f"{sl.numberOfGoodSubarraySplits(nums)} {ans}")