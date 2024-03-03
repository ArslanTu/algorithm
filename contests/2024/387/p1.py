from typing import *

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, arr2 = [nums[0]], [nums[1]]
        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        res = arr1 + arr2
        return res


sl = Solution()
examples = [
]
for example in examples:
    ans = example
    print(f"Output: {sl}, Ans: {ans}")