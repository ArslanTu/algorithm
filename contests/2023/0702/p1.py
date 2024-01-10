from typing import List

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0
        n = len(nums)
        start = 0
        while start < n:
            if nums[start] % 2 != 0 or nums[start] > threshold:
                start += 1
                continue
            max_len = 1
            i = n
            for i in range(start + 1, n):
                if nums[i] <= threshold and nums[i] % 2 != nums[i - 1] % 2:
                    max_len += 1
                else:
                    start = i
                    break
            ans = max(ans, max_len)
            if i >= n - 1:
                break
        return ans



sl = Solution()
cases = [([3,2,5,4], 5, 3), ([1,2], 2, 1), ([2,3,4,5], 4, 3)]
for case in cases:
    nums, th, ans = case[0], case[1], case[2]
    print(f"{sl.longestAlternatingSubarray(nums, th)}, {ans}")