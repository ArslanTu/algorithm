import bisect
from typing import *


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        ans = 0
        s1, s2 = 0, 0
        last_num = [0] * n
        for i in range(n):
            if i == 0:
                last_num[i] = maxHeights[i]

                s1 = 0
                pre_num = maxHeights[i]
                for j in range(i - 1, -1, -1):
                    cur_num = min(maxHeights[j], pre_num)
                    s1 += cur_num
                    last_num[j] = cur_num
                    pre_num = cur_num
                
                s2 = 0
                pre_num = maxHeights[i]
                for j in range(i + 1, n):
                    cur_num = min(maxHeights[j], pre_num)
                    s2 += cur_num
                    last_num[j] = cur_num
                    pre_num = cur_num
            else:
                if maxHeights[i] == maxHeights[i - 1]:
                    s1 += last_num[i - 1]
                    s2 -= last_num[i]
                    continue
                elif maxHeights[i] <= maxHeights[i - 1]:
                    s2 -= last_num[i]
                    last_num[i] = maxHeights[i]

                    s1 = 0
                    pre_num = maxHeights[i]
                    for j in range(i - 1, -1, -1):
                        cur_num = min(maxHeights[j], pre_num)
                        s1 += cur_num
                        last_num[j] = cur_num
                        pre_num = cur_num

                else:
                    s1 += last_num[i - 1]
                    last_num[i] = maxHeights[i]

                    s2 = 0
                    pre_num = maxHeights[i]
                    for j in range(i + 1, n):
                        cur_num = min(maxHeights[j], pre_num)
                        s2 += cur_num
                        last_num[j] = cur_num
                        pre_num = cur_num
            ans = max(ans, s1 + s2 + maxHeights[i])
        return ans

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