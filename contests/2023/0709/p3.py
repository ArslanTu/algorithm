from typing import List

class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        n = len(nums)
        start = 0
        while start != n:
            if nums[start:] == [0] * (n - start):
                return True
            if start + k > n:
                return False
            base_num = nums[start]
            end = 0
            for i in range(start, start + k):
                nums[i] -= base_num
                if nums[i] < 0:
                    return False
                if nums[i] > 0:
                    if end == 0:
                        end = i
            if end != 0: start = end
            else:
                start += k
        return True


sl = Solution()
use_cases = [([2,2,3,1,1,0], 3, True), ([1,3,1,1], 2, False)]
for use_case in use_cases:
    nums, k, ans = use_case
    print(f"{sl.checkArray(nums, k)}, {ans}")