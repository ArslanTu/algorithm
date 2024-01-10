from bisect import bisect_left, bisect_right
from typing import *

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        nums = [(num, idx) for idx, num in enumerate(nums)]
        nums.sort()
        fk_nums = []
        pos = []
        ans = [-1, -1]
        for num, idx in nums:
            fk_nums.append(num)
            pos.append(idx)
        for i in range(len(fk_nums)):
            res = bisect_left(fk_nums, fk_nums[i] + valueDifference)
            if res >= len(fk_nums):
                continue
            else:
                for j in range(res, len(fk_nums)):
                    if abs(pos[j] - pos[i]) >= indexDifference:
                        ans = [pos[i], pos[j]]
                        break
            if ans[0] != -1:
                break
        ans.sort()
        return ans


sl = Solution()
examples = [
    ([5,1,4,1], 2, 4, [0,3])
]
for example in examples:
    nums, idxf, vf, ans = example
    print(f"Output: {sl.findIndices(nums, idxf, vf)}, Ans: {ans}")