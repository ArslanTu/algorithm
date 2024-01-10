from typing import List

class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        n = len(nums)
        
        # 构建差分数组
        diff = [0] * (n + 1)
        diff[1] = nums[0]
        for i in range(1, n):
            diff[i + 1] = nums[i] - nums[i - 1]
        
        start = 1
        while True:
            if start + k > n + 1: return False
            base_num = diff[start]
            diff[start] = 0
            if start + k < n + 1: diff[start + k] += base_num
            # else:
            #     return False
            for i in range(start + 1, n + 1):
                if  diff[i] != 0:
                    start = i
                    break
            if i == n:
                if diff[i] == 0:
                    return True
                else:
                    return False
        return True



sl = Solution()
use_cases = [([2,2,3,1,1,0], 3, True), ([1,3,1,1], 2, False), ([0,0,51,67,80,98,88,75,89,83,100,70,77,82,57,100,80,69,19,17], 3, True), ([0,0,33,72,86,53,14], 3, True), ([89,8,8,8,8,8,8,8,8,8,8,8], 12, False)]
for use_case in use_cases:
    nums, k, ans = use_case
    print(f"{sl.checkArray(nums, k)}, {ans}")