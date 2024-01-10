from math import inf
from typing import *

class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1
        if sum(nums) == target:
            return 0
        nums.sort()

        ans = inf
        def dfs(cur_pos, cur_target, cur_ops):
            nonlocal ans
            if cur_target == 0:
                ans = min(ans, cur_ops)
                return
            if cur_pos == len(nums):
                return
            if cur_target < 0:
                return
            if nums[cur_pos] > cur_target:
                num = nums[cur_pos]
                ops_cnt = 0
                while num > cur_target:
                    num //= 2
                    ops_cnt += 1
                dfs(cur_pos + 1, cur_target - num, cur_ops + ops_cnt)
            elif nums[cur_pos] == cur_target:
                dfs(cur_pos + 1, 0, cur_ops)
            else:
                dfs(cur_pos + 1, cur_target - nums[cur_pos], cur_ops)
                dfs(cur_pos + 1, cur_target, cur_ops)
            
        dfs(0, target, 0)
        return ans if ans != inf else -1


sl = Solution()
examples = [
    ([1,2,8], 7, 1),
    ([1,32,1,2], 12, 2),
    ([1,32,1], 35, -1),
    ([32,256,4], 2, 1),
    ([1,32,1,2], 12, 2),
    ([16,16,4], 3, 2),
]
for example in examples:
    nums, target, ans = example
    print(f"Output: {sl.minOperations(nums, target)}, Ans: {ans}")