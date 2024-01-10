from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) == 1: return -1
        max_num, min_num = max(nums), min(nums)
        nums.remove(max_num)
        nums.remove(min_num)
        return nums[0] if nums else -1


sl = Solution()
p1 = 

print(sl)