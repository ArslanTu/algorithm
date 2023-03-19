from collections import Counter
from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        cnt = Counter()
        for idx in range(n):
            nums[idx] = nums[idx] % value
            cnt[nums[idx]] += 1
        ans = 0
        nums.sort()
        for ans in range(n):
            if cnt[ans % value]:
                cnt[ans % value] -= 1
                ans += 1
            else:
                break
        return ans
sl = Solution()
# p1 = [1,-10,7,13,6,8]
# p2 = 5
p1 = [1,-10,7,13,6,8]
p2 = 7

print(sl.findSmallestInteger(p1, p2))