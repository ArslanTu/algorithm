from math import gcd
from typing import List


class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        cur = 0
        fac_set = []
        n = len(nums)
        end_check = 0
        while cur <= end_check:
            has = False
            for fac in fac_set:
                if fac % nums[cur] == 0:
                    has = True
            if has:
                cur += 1
                continue
            else:
                fac_set.append(nums[cur])

            for idx in range(n - 1, end_check, -1):
                if gcd(nums[cur], nums[idx]) != 1:
                    end_check = idx
                    break
            cur += 1
        if end_check == n - 1:
            return -1
        else:
            return end_check



sl = Solution()

# p1 = [4,7,8,15,3,5]
p1 = [4,7,15,8,3,5]

print(sl.findValidSplit(p1))