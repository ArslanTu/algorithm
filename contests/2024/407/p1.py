"""
weekply contest p1
"""
from typing import *


class Solution:
    def minChanges(self, n: int, k: int) -> int:
        ans = 0
        # turn n and k to binary string
        n = bin(n)[2:]
        k = bin(k)[2:]
        if len(k) > len(n):
            return -1
        k = "0" * (len(n) - len(k)) + k
        for i in range(len(n)):
            if n[i] == "1":
                if k[i] == "0":
                    ans += 1
            else:
                if k[i] == "1":
                    return -1
        return ans
            


def test():
    """
    test func
    """
    sl = Solution()
    examples = [(13, 4, 2)]
    for example in examples:
        n, k, ans = example
        print(f"Output: {sl.minChanges(n, k)}, Ans: {ans}")


if __name__ == "__main__":
    test()
