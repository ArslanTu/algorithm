from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0] * 51
        aft = [0] * 51
        for i in range(n):
            aft[nums[i]] += 1
        ans = []
        for i in range(n):
            pre[nums[i]] += 1
            aft[nums[i]] -= 1
            ans.append(sum([x > 0 for x in pre]) - sum([y > 0 for y in aft]))
        return ans