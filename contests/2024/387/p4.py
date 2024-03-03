from bisect import bisect_right, insort_right
from typing import *

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, arr2 = [nums[0]], [nums[1]]
        s1, s2 = [nums[0]], [nums[1]]

        def greatr_count(arr, val):
            des = bisect_right(arr, val)
            return len(arr) - des

        for num in nums[2:]:
            d1 = greatr_count(s1, num)
            d2 = greatr_count(s2, num)
            if d1 > d2:
                arr1.append(num)
                d = len(s1) - d1
                insort_right(s1, num)
            elif d1 < d2:
                arr2.append(num)
                d = len(s2) - d2
                insort_right(s2, num)
            else:
                if len(arr1) <= len(arr2):
                    arr1.append(num)
                    d = len(s1) - d1
                    insort_right(s1, num)
                else:
                    arr2.append(num)
                    d = len(s2) - d2
                    insort_right(s2, num)
        return arr1 + arr2




sl = Solution()
examples = [
    ([2,1,3,3], [2,3,1,3]),
    ([5,14,3,1,2], [5,3,1,2,14]),
    ([11,92,25,90], [11,92,25,90])
]
for example in examples:
    nums, ans = example
    print(f"Output: {sl.resultArray(nums)}, Ans: {ans}")