"""
weekply contest p2
"""
from typing import *


class Solution:

    def valueAfterKSeconds(self, n: int, k: int) -> int:
        last = [1] * n
        MOD = 10**9 + 7
        while k:
            k -= 1
            cur = [1]
            for i in range(1, n):
                cur.append((cur[-1] + last[i]) % MOD)
            last = cur
        return last[n - 1]

def test():
    """
    test func
    """
    sl = Solution()
    examples = [
    ]
    for example in examples:
        ans = example
        print(f"Output: {sl}, Ans: {ans}")


if __name__ == "__main__":
    test()
