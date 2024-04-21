"""
weekply contest p1
"""
from typing import *


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        sp = set()
        for c in "abcdefghijklmnopqrstuvwxyz":
            try:
                first_up = word.index(c.upper())
                last_low = word.rindex(c)
            except ValueError:
                continue
            if last_low < first_up:
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
