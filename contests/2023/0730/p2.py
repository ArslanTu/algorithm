from typing import *
from collections import *

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)
        all_nums = set(nums)
        cur_nums = set()
        cur_nums.add(nums[0])
        cnt = Counter()
        cnt[nums[0]] += 1
        ans = 0
        while 0 <= l <= r and r < n:
            while cur_nums == all_nums:
                if l + 1 <= r and cnt[nums[l]] > 1:
                    l += 1
                    cnt[nums[l]] -= 1
                else:
                    break
            if cur_nums == all_nums:
                ans += l + 1
            r += 1
            if r == n:
                break
            cnt[nums[r]] += 1
            if cnt[nums[r]] == 1:
                cur_nums.add(nums[r])
        return ans


sl = Solution()

cases = [([1,3,1,2,2], 4), ([5,5,5,5], 10), ([1898,370,822,1659,1360,128,370,360,261,1898], 4)]
for case in cases:
    nums, ans = case
    print(f"expect: {ans}, output: {sl.countCompleteSubarrays(nums)}")