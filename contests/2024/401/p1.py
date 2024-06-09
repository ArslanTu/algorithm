"""
weekply contest p1
"""
from typing import *


class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        dir = 1
        cur = 0
        while k:
            k -= 1
            if cur == 0:
                dir = 1
            elif cur == n - 1:
                dir = 0
            if dir == 1:
                cur += 1
            else:
                cur -= 1
        return cur



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
