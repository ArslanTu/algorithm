from typing import List


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [abs(sum(nums[:idx]) - sum(nums[idx + 1:])) for idx in range(n)]
        return ans


sl = Solution()

p1 = [10,4,8,3]


print(sl.leftRigthDifference(p1))