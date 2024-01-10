from collections import deque
from math import inf
from typing import *

class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1
        if sum(nums) == target:
            return 0
        nums.sort()
        nums = deque(nums)
        ans = inf
        m_ans = inf
        binary_string = bin(target)[2:]
        binary_string = binary_string[::-1]
        target = []
        for i, c in enumerate(binary_string):
            if c == '1':
                target.append(2 ** i)

        def dfs(arr, cur_target, cur_ops):
            nonlocal m_ans
            if cur_target == 0:
                m_ans = min(m_ans, cur_ops)
                return
            if len(nums) == 0:
                return
            if cur_target < 0:
                return
            num = arr.popleft()
            no_use_arr = deque(arr)
            use_arr
            if num > cur_target:
                ops_cnt = 0
                while num > cur_target:
                    num //= 2
                    ops_cnt += 1
                    nums.appendleft(num)
                dfs(arr, cur_target - num, cur_ops + ops_cnt)
            elif num == cur_target:
                dfs(arr, 0, cur_ops)
            else:
                dfs(no_use_arr, cur_target, cur_ops)
                dfs(arr, cur_target - num, cur_ops)


        for t in target:
            m_ans = inf
            dfs(nums, t, 0)
            if m_ans == inf:
                return -1
            ans += m_ans
        return ans if ans != inf else -1



sl = Solution()
examples = [
    # ([1,2,8], 7, 1),
    # ([1,32,1,2], 12, 2),
    # ([1,32,1], 35, -1),
    # ([32,256,4], 2, 1),
    # ([1,32,1,2], 12, 2),
    # ([16,16,4], 3, 2),
    # ([64,32,2,8], 5, 2),
    ([128,1024,1073741824,4194304,268435456,1024,16,1073741824,131072,4,16777216,67108864,16777216,268435456,1073741824,256,16,67108864,1048576,16,4,4194304,1024,16,262144,1048576,1024,128,1073741824,67108864,65536,128,32768,128,32768,8192,256,1024], 38, 1)
]
for example in examples:
    nums, target, ans = example
    print(f"Output: {sl.minOperations(nums, target)}, Ans: {ans}")