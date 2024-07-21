"""
weekply contest p3
"""
from typing import *


class Solution:
    def maxOperations(self, s: str) -> int:
        _s = ""
        for ch in s:
            if _s == "":
                _s += ch
                continue
            if ch == "0" and _s[-1] == "0":
                continue
            else:
                _s += ch
        s = _s
        ans = 0
        cnt = 0
        for i in range(len(s)):
            if s[i] == "0":
                ans += cnt
            else:
                cnt += 1
        return ans

def test():
    """
    test func
    """
    sl = Solution()
    examples = []
    for example in examples:
        ans = example
        print(f"Output: {sl}, Ans: {ans}")


if __name__ == "__main__":
    test()
