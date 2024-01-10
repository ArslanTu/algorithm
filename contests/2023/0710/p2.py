from typing import List

class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        nums2 = []
        for num in nums[::-1]:
            if nums2 and nums2[-1] >= num:
                top = nums2.pop()
                nums2.append(top + num)
            else:
                nums2.append(num)
        return max(nums2)

sl = Solution()
cases = [()]
for case in cases:
    print(f"output: {sl}, ans: {ans}")