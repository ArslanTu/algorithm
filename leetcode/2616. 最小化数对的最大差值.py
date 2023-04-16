from math import inf
from typing import List
from collections import Counter

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        left, right = 0, nums[-1] - nums[0]
        ans = -1
        
        def check(x):
            cnt = 0
            i, j = 0, 1
            while i < n and j < n:
                if nums[j] - nums[i] <= mid:
                    cnt += 1
                    i += 2
                    j += 2
                else:
                    i += 1
                    j += 1
            return cnt >= p

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid -1
                ans = mid
            else:
                left = mid + 1
                
        return ans



sl = Solution()

# p1 = [10,1,2,7,1,3]
# p2 = 2

# p1 = [4,2,1,2]
# p2 = 1
p1 = [3,4,2,3,2,1,2]
p2 = 3
print(sl.minimizeMax(p1, p2))