"""
weekply contest p1
"""
from typing import *


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        sp = set()
        word = set(word)
        for c in "abcdefghijklmnopqrstuvwxyz":
            if c in word and c.upper() in word:
                sp.add(c)
        return len(sp)


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
