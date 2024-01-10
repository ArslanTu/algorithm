from typing import *

class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        def check_subarrays(arr, m):
            count = 1
            cur_sum = 0
            for num in arr:
                cur_sum += num
                if cur_sum > m:
                    count += 1
                    cur_sum = num
            return count

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check_subarrays(nums, mid) <= m:
                right = mid
            else:
                left = mid + 1
        return left == max(nums)

sol = Solution()

cases = []
for case in cases:
    ans = case
    print(f"output: {sol}, expect: {ans}")

# [2, 2, 1]
# 4
# [2, 1, 3]
# 5
# [2, 3, 3, 2, 3]
# 6
# [2, 1, 2]
# 4