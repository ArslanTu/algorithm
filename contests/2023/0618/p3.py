from collections import defaultdict
from typing import List

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        ans = 0
        MOD = 10 ** 9 + 7
        mapping = defaultdict(list)
        used = {}
        nums.sort()
        n = len(nums)
        for num1 in nums:
            used[num1] = 0
            for num2 in nums:
                if num1 != num2:
                    if (num2 != 0 and num1 % num2 == 0) or (num1 != 0 and num2 % num1 == 0):
                        mapping[num1].append(num2)
        
        def dfs(cur_pos, cur_num):
            nonlocal n, ans, used, mapping, MOD
            if cur_pos == n:
                return
            for num in mapping[cur_num]:
                if used[num] == 0:
                    used[num] = 1
                    if cur_pos == n - 1:
                        ans = (ans + 1) % MOD
                    dfs(cur_pos + 1, num)
                    used[num] = 0
        
        for num in nums:
            used[num] = 1
            dfs(1, num)
            used[num] = 0
        
        return ans

sl = Solution()

cases = (([2,3,6], 2), ([1,4,3], 2), ([20,100,50,5,10,70,7], 48))
for p1, p2 in cases:
    print(sl.specialPerm(p1), " ", p2)