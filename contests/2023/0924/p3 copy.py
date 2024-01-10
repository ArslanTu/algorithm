import bisect
from typing import *


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        ans = 0
        s1 = [0] * n
        s2 = [0] * n

        pre_num = maxHeights[0]
        for i in range(1, n):
            cur_num = min(maxHeights[i], pre_num)
            s2[0] += cur_num
            pre_num = cur_num

        for i in range(1, n):
            if maxHeights[i] == maxHeights[i - 1]:
                s1[i] += maxHeights[i]
                s2 -= maxHeights[i]
            elif maxHeights[i] < maxHeights[i - 1]:
                
                s2[i] = s2[i - 1] - maxHeights[i]


sl = Solution()
examples = [
    ([5,3,4,1,1], 13),
    ([6,5,3,9,2,7], 22),
    ([3,2,5,5,2,3], 18),
    ([1,1,4,3,3,3,6], 20),
]
for example in examples:
    maxHeights, ans = example
    print(f"Output: {sl.maximumSumOfHeights(maxHeights)}, Ans: {ans}")