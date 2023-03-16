from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ans = 0
        if nums[0] <= 0:
            return 0
        p_sum = 0
        for num in nums:
            p_sum += num
            if p_sum > 0:
                ans += 1
        return ans

sl = Solution()
# p1 = [2,-1,0,1,-3,3,-3]
p1 = [-2,-3,0]

print(sl.maxScore(p1))