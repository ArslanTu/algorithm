from typing import List

class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[n - 1] - nums[0]
        for idx in range(1, n):
            ans = min(ans, nums[idx] - nums[idx - 1])
        return ans

sl = Solution()

cases = (([1,3,2,4], 1), ([100,1,10], 9), ([84,11,100,100,75], 0))
for p1, p2 in cases:
    print(sl.findValueOfPartition(p1), " ", p2)