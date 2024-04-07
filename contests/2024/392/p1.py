from typing import *


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1
        def check():
            nonlocal ans
            cur_len = 1
            for i in range(1, len(nums)):
                if nums[i] > nums[i-1]:
                    cur_len += 1
                else:
                    cur_len = 1
                ans = max(ans, cur_len)
        check()
        nums = [-num for num in nums]
        check()
        return ans


sl = Solution()
examples = [
    ( [1,4,3,3,2], 2),
    ([3,3,3,3], 1),
    ([3,2,1],3)

]
for example in examples:
    x, ans = example
    print(f"Output: {sl.longestMonotonicSubarray(x)}, Ans: {ans}")