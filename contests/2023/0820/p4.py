from typing import *

class Solution:
    def longest_subarray_sum_less_than_k(self, nums, k):
        if not nums:
            return 0

        left = 0
        max_length = 0
        current_sum = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum > k:
                current_sum -= nums[left]
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length

    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        ans = 0
        mapping = {}
        for i, num in enumerate(nums):
            if mapping.get(num, None) == None:
                mapping[num] = [i, []]
            else:
                last = mapping[num][0]
                mapping[num][1].append(i - last - 1)
                mapping[num][0] = i

        for key, val in mapping.items():
            _, pos = val
            res = self.longest_subarray_sum_less_than_k(pos, k) + 1
            ans = max(res, ans)
        return ans


sl = Solution()
examples = [
    ([1,3,2,3,1,3], 3, 3),
    ([1,1,2,2,1,1], 2, 4),
    ([3,1,5,3,1,1], 0, 2),
]
for example in examples:
    nums, k, ans = example
    print(f"Output: {sl.longestEqualSubarray(nums, k)}, Ans: {ans}")