from typing import *

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        ans = [n - i for i in range(1, n + 1)]
        a = x
        b = y
        x = min(a, b)
        y = max(a, b)
        if x == y:
            return [x * 2 for x in ans]
        else:
            for i in range(1, x + 1):
                for j in range(y, n + 1):
                    ans[j-i-1] -= 1
                    ans[x-i+j-y+1-1] += 1
        return [x * 2 for x in ans]



sl = Solution()
examples = [
    # (3, 1, 3, [6,0,0]),
    # (5, 2, 4, [10,8,2,0,0]),
    # (4, 1, 1, [6,4,2,0]),
    # (2, 2, 1, [2, 0]),
    (5, 1, 5, [10,10,0,0,0])
]
for example in examples:
    n, x, y, ans = example
    print(f"Output: {sl.countOfPairs(n, x, y)}, Ans: {ans}")