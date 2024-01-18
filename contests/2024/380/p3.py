from bisect import bisect_left, bisect_right
from typing import *
from sortedcontainers import SortedList

class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        base = '0' * 50
        for i in range(x, 51, x):
            base = base[:i-1] + '1' + base[i:]
        base = int(base[::-1], 2)

        def count_ones(z):
            count = 0
            while z:
                count += z & 1
                z >>= 1
            return count

        pre_sum = []

        def check(res):
            if res <= len(pre_sum):
                if len(pre_sum) > 0 and pre_sum[res - 1] <= k:
                    return True
                else:
                    return False
            else:
                p = pre_sum[-1] if len(pre_sum) > 0 else 0
                for i in range(len(pre_sum) + 1, res + 1):
                    pre_sum.append(p + count_ones(i & base))
                    p = pre_sum[-1]
                if pre_sum[res - 1] <= k:
                    return True
                else:
                    return False
        
        l = 1
        r = 10 ** 9
        ans = 1
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = max(ans, mid)
                l = mid + 1
            else:
                r = mid - 1 
        return ans

    
sl = Solution()
examples = [
    # (9, 1, 6),
    # (7, 2, 9),
    (3278539330613, 5, 0),
]
for example in examples:
    k, x, ans = example
    print(f"Output: {sl.findMaximumNumber(k, x)}, Ans: {ans}")