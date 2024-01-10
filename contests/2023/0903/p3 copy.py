from typing import *

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        nums = [1 if num % modulo == k else 0 for num in nums]
        prefix_sum = 0  # 用于存储前缀和
        modulo_count = {0: 1}  # 用于存储前缀和对modulo的余数及其出现次数
        count = 0  # 用于存储符合条件的子数组数量

        for num in nums:
            prefix_sum = (prefix_sum + num) % modulo
            if prefix_sum in modulo_count:
                count += modulo_count[prefix_sum]
                modulo_count[prefix_sum] += 1
            else:
                modulo_count[prefix_sum] = 1

        return count



sl = Solution()
examples = [
    ([3,2,4], 2, 1, 3),
    ([3,1,9,6], 3, 0, 2),
    ([11,12,21,31], 10, 1, 5),
]
for example in examples:
    nums, modulo, k, ans = example
    print(f"Output: {sl.countInterestingSubarrays(nums, modulo, k)}, Ans: {ans}")