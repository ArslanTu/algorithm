class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        res_min_odd = res_min_even = 0
        n = len(nums)
        if n == 1:
            return 0
        # min_odd
        for idx in range(1, n, 2):
            if idx < n - 1:
                res_min_odd += max(nums[idx] - min(nums[idx - 1], nums[idx + 1]) + 1, 0)
            else:
                res_min_odd += max(nums[idx] - nums[idx - 1] + 1, 0)
        res_min_even += max(nums[0] - nums[1] + 1, 0)
        for idx in range(2, n, 2):
            if idx < n - 1:
                res_min_even += max(nums[idx] - min(nums[idx - 1], nums[idx + 1]) + 1, 0)
            else:
                res_min_even += max(nums[idx] - nums[idx - 1] + 1, 0)
        return min(res_min_even, res_min_odd)