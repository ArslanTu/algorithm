from typing import *

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = list(nums1), list(nums2)
        n = len(nums1)
        # case 1
        ops1 = 0
        for i in range(n):
            if n1[i] > n1[n - 1]:
                x = n1[i]
                n1[i] = n2[i]
                n2[i] = x
                ops1 += 1
        if max(n1) == n1[n - 1] and max(n2) == n2[n - 1]:
            pass
        else:
            ops1 = -1

        n1, n2 = list(nums1), list(nums2)
        y = n1[n - 1]
        n1[n - 1] = n2[n - 1]
        n2[n - 1] = y
        # case 2
        ops2 = 1
        for i in range(n):
            if n1[i] > n1[n - 1]:
                x = n1[i]
                n1[i] = n2[i]
                n2[i] = x
                ops2 += 1
        if max(n1) == n1[n - 1] and max(n2) == n2[n - 1]:
            pass
        else:
            ops2 = -1
        
        if ops1 == -1:
            return ops2
        elif ops2 != -1:
            return min(ops1, ops2)
        else:
            return ops1
        



sl = Solution()
examples = [
    
]
for example in examples:
    ans = example
    print(f"Output: {sl}, Ans: {ans}")