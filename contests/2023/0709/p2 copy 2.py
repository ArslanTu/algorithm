from typing import List

class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [[1, 1] for i in range(n)]
        for i in range(1, n):
            if nums1[i] >= nums1[i - 1]:
                dp[i][0] = max(dp[i][0], dp[i - 1][0] + 1)
            if nums1[i] >= nums2[i - 1]:
                dp[i][0] = max(dp[i][0], dp[i - 1][1] + 1)
            if nums2[i] >= nums1[i - 1]:
                dp[i][1] = max(dp[i][1], dp[i - 1][0] + 1)
            if nums2[i] >= nums2[i - 1]:
                dp[i][1] = max(dp[i][1], dp[i - 1][1] + 1)
        return max([max(dp[i]) for i in range(n)])

sl = Solution()
use_cases = [([2,3,1], [1,2,1], 2), ([1,3,2,1], [2,2,3,4], 4), ([1,1], [2,2], 2), ([8,7,4], [13,4,4], 2), ([11,7,7,9], [19,19,1,7], 3), ([4,16,10,8], [8,4,1,9], 3), ([16,9,5,7,2,6], [9,5,2,5,19,12], 4)]
for use_case in use_cases:
    nums1, nums2, ans  = use_case
    print(f"{sl.maxNonDecreasingLength(nums1, nums2)}, {ans}")

    

