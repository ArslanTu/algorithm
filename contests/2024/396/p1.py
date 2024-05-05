"""
weekply contest p1
"""
from typing import *


class Solution:
    def isValid(self, word: str) -> bool:
        word = word.lower()
        nums = "0123456789"
        le = '0123456789abcdefghijklmnopqrstuvwxyz'
        ue = le.upper()
        yuan = 'aeiou'
        yuan += yuan.upper()
        if len(word) <  3:
            print(1)
            return False
        for c in word:
            if c not in le and c not in ue:
                print(2)
                return False
        hasYuan = any(c in yuan and c not in nums for c in word)
        hasNoYuan = any(c not in yuan and c not in nums for c in word)
        return hasYuan and hasNoYuan


def test():
    """
    test func
    """
    sl = Solution()
    examples = [("AhI", True), ("UuE6", False)]
    for example in examples:
        word, ans = example
        print(f"Output: {sl.isValid(word)}, Ans: {ans}")


if __name__ == "__main__":
    test()
