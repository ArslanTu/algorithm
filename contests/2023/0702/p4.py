from typing import List

class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                sarr = sorted(nums[i:j + 1])
                for k in range(j - i):
                    if sarr[k + 1] - sarr[k] > 1:
                        ans += 1
        return ans



sl = Solution()
cases = [([2,3,1,4], 3), ([1,3,3,3,5], 8)]
for case in cases:
    nums, ans = case[0], case[1]
    print(f"{sl.sumImbalanceNumbers(nums)}, {ans}")