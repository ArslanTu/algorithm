from typing import *

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        n_ou = n // 2 if (n & 1) == 0 else (n - 1) // 2
        n_ji = n - n_ou

        m_ou = m // 2 if (m & 1) == 0 else (m - 1) // 2
        m_ji = m - m_ou

        return n_ou * m_ji + n_ji * m_ou
            
sl = Solution()
examples = [
    (3, 2, 3),
    (1, 1, 0),
]
for example in examples:
    n, m, ans = example
    print(f"Output: {sl.flowerGame(n, m)}, Ans: {ans}")