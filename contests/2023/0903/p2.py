from math import inf
from typing import *

class Solution:
    def minimumOperations(self, num: str) -> int:
        ans = inf
        n = len(num)
        # 25
        cur = 0
        c5 = 0
        c2 = 0
        for i in range(n - 1, -1, -1):
            if c5 == 0 and c2 == 0:
                if num[i] != '5':
                    cur += 1
                else:
                    c5 += 1
            elif c2 == 0:
                if num[i] != '2':
                    cur += 1
                else:
                    c2 += 1
            else:
                break
        if c5 == 1 and c2 == 1:
            ans = min(ans, cur)
        # 50
        cur = 0
        c0 = 0
        c5 = 0
        for i in range(n - 1, -1, -1):
            if c0 == 0 and c5 == 0:
                if num[i] != '0':
                    cur += 1
                else:
                    c0 += 1
            elif c5 == 0:
                if num[i] != '5':
                    cur += 1
                else:
                    c5 += 1
            else:
                break
        if c0 == 1 and c5 == 1:
            ans = min(ans, cur)
        # 75
        cur = 0
        c5 = 0
        c7 = 0
        for i in range(n - 1, -1, -1):
            if c5 == 0 and c7 == 0:
                if num[i] != '5':
                    cur += 1
                else:
                    c5 += 1
            elif c7 == 0:
                if num[i] != '7':
                    cur += 1
                else:
                    c7 += 1
            else:
                break
        if c5 == 1 and c7 == 1:
            ans = min(ans, cur)
        # 100
        cur = 0
        c0 = 0
        for i in range(n - 1, -1, -1):
            if c0 < 2:
                if num[i] != '0':
                    cur += 1
                else:
                    c0 += 1
            else:
                break
        if c0 == 2:
            ans = min(ans, cur)
        # 0
        if '0' in num:
            ans = min(ans, n - 1)
        
        if ans == inf:
            ans = n
        return ans


sl = Solution()
examples = [
    # ("2245047", 2),
    # ("2908305", 3),
    # ("10", 1),
    # ("1", 1),
    ("25", 0)
]
for example in examples:
    num, ans = example
    print(f"Output: {sl.minimumOperations(num)}, Ans: {ans}")