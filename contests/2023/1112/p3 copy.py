from typing import *

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        def cal(x, y, start=0):
            x, y = list(x), list(y)
            ops = start
            for i in range(len(x)):
                if x[i] > x[-1]:
                    tmp = x[i]
                    x[i] = y[i]
                    y[i] = tmp
                    ops += 1
            for i in range(len(y)):
                if y[i] > y[-1]:
                    tmp = y[i]
                    y[i] = x[i]
                    x[i] = tmp
                    ops += 1
            if x[-1] == max(x) and y[-1] == max(y):
                return ops
            else:
                return -1
            
        
        ans1 = cal(nums1, nums2)
        tt = nums1[-1]
        nums1[-1] = nums2[-1]
        nums2[-1] = tt
        ans2 = cal(nums1, nums2, 1)

        if ans1 == -1:
            return ans2
        elif ans2 == -1:
            return ans1
        else:
            return min(ans1, ans2)


        



sl = Solution()
examples = [
    ([1,2,7], [4,5,3], 1),
    ([2,3,4,5,9], [8,8,4,4,4], 2),
    ([1,5,4], [2,5,3], -1),
    ([1,1,8,9], [1,7,1,1], 1)
]
for example in examples:
    nums1, nums2, ans = example
    print(f"Output: {sl.minOperations(nums1, nums2)}, Ans: {ans}")