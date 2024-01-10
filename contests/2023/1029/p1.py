from typing import *

class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        nums = [bin(num)[2:] for num in nums]
        nums = [num[-1::-1] for num in nums]
        ans = ""
        right = max([len(num) for num in nums])
        for i in range(right):
            cnt = 0
            for num in nums:
                if len(num) < i + 1:
                    continue
                if num[i] == '1':
                    cnt += 1
            if cnt >= k:
                ans += '1'
            else:
                ans += '0'
        ans = ans[-1::-1]
        ans = int(ans, base=2)
        return ans

sl = Solution()
examples = [
    ([7,12,9,8,9,15], 4, 9)
]
for example in examples:
    nums, k, ans = example
    print(f"Output: {sl.findKOr(nums, k)}, Ans: {ans}")