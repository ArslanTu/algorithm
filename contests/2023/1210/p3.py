from typing import *

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m = max(nums)
        n = len(nums)
        ans = 0
        q = []
        for i in range(n):
            if nums[i] == m:
                if len(q) == k:
                    q.pop(0)
                q.append(i)
            if len(q) == k:
                ans += q[0] + 1
        return ans

sl = Solution()
examples = [
    ([1,3,2,3,3], 2, 6),
    ([61,23,38,23,56,40,82,56,82,82,82,70,8,69,8,7,19,14,58,42,82,10,82,78,15,82], 2, 224),
]
for example in examples:
    nums, k, ans = example
    print(f"Output: {sl.countSubarrays(nums, k)}, Ans: {ans}")