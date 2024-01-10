from typing import *


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        ans = 0
        for i in range(n):
            s = maxHeights[i]
            pre_num = maxHeights[i]
            for j in range(i - 1, -1, -1):
                cur_num = min(maxHeights[j], pre_num)
                s += cur_num
                pre_num = cur_num
            
            pre_num = maxHeights[i]
            for j in range(i + 1, n):
                cur_num = min(maxHeights[j], pre_num)
                s += cur_num
                pre_num = cur_num
            ans = max(ans, s)
        return ans

sl = Solution()
examples = [
    ([5,3,4,1,1], 13),
    ([6,5,3,9,2,7], 22),
    ([3,2,5,5,2,3], 18)
]
for example in examples:
    maxHeights, ans = example
    print(f"Output: {sl.maximumSumOfHeights(maxHeights)}, Ans: {ans}")