from typing import List


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        l, r = 0, (len(nums) >> 1) - 1
        while l < (len(nums) >> 1) and r < len(nums):
            if nums[l] * 2 <= nums[r]:
                ans += 2
                l += 1
                r += 1
            else:
                r += 1
        return ans

sl = Solution()

# p1 = [3,5,2,4]
# p1 = [9,2,5,4]
# p1 = [7,6,8]
p1 = [42,83,48,10,24,55,9,100,10,17,17,99,51,32,16,98,99,31,28,68,71,14,64,29,15,40]


print(sl.maxNumOfMarkedIndices(p1))