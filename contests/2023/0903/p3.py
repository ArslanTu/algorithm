from typing import *

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        nums = [1 if num % modulo == k else 0 for num in nums]

        m = {0: 1}
        acc = 0
        res = 0
        for num in nums:
            acc += num
            if ((acc % modulo) - k) % modulo in m:
                res += m[((acc % modulo) - k) % modulo]
            if acc % modulo in m:
                m[acc % modulo] += 1
            else:
                m[acc % modulo] = 1
        return res




sl = Solution()
examples = [
    ([3,2,4], 2, 1, 3),
    ([3,1,9,6], 3, 0, 2),
    ([11,12,21,31], 10, 1, 5),
]
for example in examples:
    nums, modulo, k, ans = example
    print(f"Output: {sl.countInterestingSubarrays(nums, modulo, k)}, Ans: {ans}")