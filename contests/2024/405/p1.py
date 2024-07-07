"""
weekply contest p1
"""
from typing import *


class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        _s = ""
        for i in range(len(s)):
            idx = (i + k) % len(s)
            _s += s[idx]
        return _s


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
