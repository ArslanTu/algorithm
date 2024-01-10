from typing import *
from collections import *

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)
        ans = 0
        cnt = Counter()
        all_nums = set(nums)
        cur_nums = set()
        while 0 <= l <= r and r < n:
            cur_nums.add(nums[r])
            cnt[nums[r]] += 1
            while cur_nums == all_nums:
                if l + 1 <= r and cnt[nums[l]] > 1:
                    cnt[nums[l]] -= 1
                    l += 1
                else:
                    break
            if cur_nums == all_nums:
                ans += l + 1
            r += 1
        return ans


sl = Solution()

cases = [([1,3,1,2,2], 4), ([5,5,5,5], 10), ([1898,370,822,1659,1360,128,370,360,261,1898], 4)]
for case in cases:
    nums, ans = case
    print(f"expect: {ans}, output: {sl.countCompleteSubarrays(nums)}")