class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 双指针
        if sum(nums) < target:
            return 0
        ans = len(nums)
        left = 0
        cur_sum = 0
        for right, num in enumerate(nums):
            cur_sum += num
            while cur_sum - nums[left] >= target:
                cur_sum -= nums[left]
                left += 1
            if cur_sum >= target:
                ans = ans if ans < right - left + 1 else right - left + 1
        return ans
