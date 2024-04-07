from typing import *


class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        tar_pos = len(nums) // 2
        nums.sort()
        if nums[tar_pos] == k:
            return 0
        elif nums[tar_pos] < k:
            ans = k - nums[tar_pos]
            nums[tar_pos] = k
            for i in range(tar_pos + 1, len(nums)):
                if nums[i] < nums[i - 1]:
                    ans += nums[i - 1] - nums[i]
                    nums[i] = nums[i - 1]
        else:
            ans = nums[tar_pos] - k
            nums[tar_pos] = k
            for i in range(tar_pos - 1, -1, -1):
                if nums[i] > nums[i + 1]:
                    ans += nums[i] - nums[i + 1]
                    nums[i] = nums[i + 1]
        return ans


sl = Solution()
examples = [
    ([2,5,6,8,5], 4, 2),
    ([2,5,6,8,5], 7, 3),
    ( [1,2,3,4,5,6], 4, 0)
]
for example in examples:
    nums, k, ans = example
    print(f"Output: {sl.minOperationsToMakeMedianK(nums, k)}, Ans: {ans}")