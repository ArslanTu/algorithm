from collections import defaultdict
from email.policy import default
from typing import List

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = 1
        last = [{} for _ in range(n)]

        mapping = {}
        for i in range(n):
            cur_num = nums[i]
            mapping[cur_num] = i
            for diff in range(-2, 3):
                new_num = cur_num + diff
                last[i][new_num] = mapping.get(new_num, -1)

        for i in range(1, n):
            pre_num = nums[i - 1]
            cur_num = nums[i]
            last_unacc_pos = -1
            for diff in range(-2, 3):
                new_num = pre_num + diff
                if abs(new_num - cur_num) > 2:
                    last_unacc_pos = max(last_unacc_pos, last[i - 1][new_num])
            if i == 9:
                print('1')
            if last_unacc_pos == -1:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = min(dp[i - 1] + 1, i - last_unacc_pos)
        return sum(dp)

sl = Solution()
cases = [([50,51,52,53,54,53,53,53,52,53], 42)]
for case in cases:
    nums, ans = case[0], case[1]
    print(f"{sl.continuousSubarrays(nums)}, {ans}")