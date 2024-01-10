from typing import *

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        if all([num > 0 for num in nums1]):
            if all([num > 0 for num in nums2]):
                if sum(nums1) != sum(nums2):
                    return -1
                else:
                    return sum(nums1)
            else:
                if sum(nums1) - sum(nums2) < sum([num == 0 for num in nums2]):
                    return -1
                else:
                    return sum(nums1)
        if all([num > 0 for num in nums2]):
            if all([num > 0 for num in nums1]):
                if sum(nums1) != sum(nums2):
                    return -1
                else:
                    return sum(nums2)
            else:
                if sum(nums2) - sum(nums1) < sum([num == 0 for num in nums1]):
                    return -1
                else:
                    return sum(nums2)
        
        low, high = 0, 10 ** 11
        ans = -1
        
        to_fill_1 = sum([num == 0 for num in nums1])
        to_fill_2 = sum([num == 0 for num in nums2])
        total_1 = sum(nums1)
        total_2 = sum(nums2)
        def check(x):
            if x - total_1 >= to_fill_1 and x - total_2 >=  to_fill_2:
                return True
            else:
                return False
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
        return ans

sl = Solution()
examples = [
    ([3,2,0,1,0], [6,5,0], 12),
    ([2,0,2,0], [1,4], -1)
]
for example in examples:
    nums1, nums2, ans = example
    print(f"Output: {sl.minSum(nums1, nums2)}, Ans: {ans}")