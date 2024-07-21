"""
weekply contest p1
"""
from typing import *


class Solution:
    def getSmallestString(self, s: str) -> str:
        ans = s
        for i in range(len(s) - 1):
            if (int(s[i]) % 2) == (int(s[i+1]) % 2):
                if i < len(s) - 2:
                    new_s = s[:i] + s[i+1] + s[i] + s[i+2:]
                else:
                    new_s = s[:i] + s[i+1] + s[i]
                ans = min(ans, new_s)
        return ans


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
