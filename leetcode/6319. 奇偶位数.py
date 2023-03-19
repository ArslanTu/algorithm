from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ans = [0, 0]
        cur = 0
        while n:
            if (n & 1) == 1:
                ans[cur] += 1
            n >>= 1
            cur = (cur + 1) % 2
        return ans